"""Copy and SHA256-verify local EP01 media; never move or delete source files."""
import argparse
import csv
import hashlib
import json
import re
import shutil
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT/'he_thong_chatgpt_veo'
EP=PROJECT/'series_anh_khoai_tay_chi_dao/episodes/ep01_pilot'
THREAD='01a0eb0e-6ec3-7121-a6a5-ea0ccdb77744'
ROOTS=[('project',PROJECT),('artifacts',ROOT/'artifacts'),
       ('handoffs',Path('C:/Users/PC/Downloads/du_an_nem_bui')),
       ('generated_images',Path('C:/Users/PC/.codex/generated_images')/THREAD)]
IMAGES={'.png','.jpg','.jpeg','.webp','.gif','.bmp','.tif','.tiff','.svg'}
VIDEOS={'.mp4','.mov','.mkv','.webm','.m4v','.avi'}
AUDIO={'.wav','.mp3','.m4a','.aac','.ogg','.flac'}
MEDIA=IMAGES|VIDEOS|AUDIO
DOCS={'.md','.json','.txt','.srt','.ass','.csv','.tsv','.yaml','.yml'}
SELECTED=EP/'restart_720p_v1/07_edits/EP01_TWO_JOIN_REPAIR_v2_323_FOR_REVIEW.mp4'
SELECTED_HASH='d7f380e05bdcafb3eb2768ce0cc4d011c6ee7570a4ec24788ce0cdf4305e2845'
INPUT_NAMES={'nembui.jpg','z7750931050074_6fa76793489e54e476846aad4d233684_806643377.jpg',
             'f3035b95-3deb-4752-b473-9de3b563084a.jpg'}
CATEGORIES=['00_BAN_DANG_CHON','01_VIDEO_NGUON','02_VIDEO_DUNG_VA_THU',
            '03_ANH_TAO_VA_THAM_CHIEU','04_ANH_DAU_VAO','05_AM_THANH',
            '06_ANH_KIEM_TRA_VA_KHUNG_TRICH','07_MEDIA_KHAC']


def sha(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream,'sha256').hexdigest()


def key(path):
    return str(path.resolve()).casefold()


def under(path,root):
    return path==root or root in path.parents


def role(path):
    lower=path.as_posix().casefold(); ext=path.suffix.casefold()
    if key(path)==key(SELECTED): return 0
    if path.name.casefold() in INPUT_NAMES: return 4
    if ext in AUDIO: return 5
    if ext in VIDEOS:
        return 1 if '/05_native/' in lower or '/downloads/' in lower and '/du_an_nem_bui/' not in lower else 2
    if ext in IMAGES:
        if any(x in lower for x in ('/06_qc/','/all_native_frames/','/frames/','/selected_frames/',
                                    '/encoded_frames/','/patch_frames/','/native_qc/','/evidence/')):
            return 6
        if any(x in path.stem.casefold() for x in ('contact','overview','seam16','board','screenshot')):
            return 6
        return 3
    return 7


def inventory():
    found={}; roots=[]
    for tag,root in ROOTS:
        root=root.resolve()
        if not root.is_dir():
            roots.append({'tag':tag,'path':str(root),'exists':False}); continue
        count=0
        for path in root.rglob('*'):
            if path.is_file() and not path.is_symlink() and path.suffix.casefold() in MEDIA:
                found[key(path)]=(path,tag); count+=1
        roots.append({'tag':tag,'path':str(root),'exists':True,'media_files':count})
    # Only extra media paths explicitly referenced by this project's text. No Downloads sweep.
    command=['rg','--files','-g','*.md','-g','*.json','-g','*.txt','-g','*.py',str(PROJECT),str(ROOT/'artifacts'),str(ROOT/'scripts')]
    listed=subprocess.run(command,capture_output=True,text=True,encoding='utf-8',check=True).stdout.splitlines()
    extensions='|'.join(sorted(x[1:] for x in MEDIA))
    pattern=re.compile(r'[CD]:[\\/][^"<>|`,;\r\n]*?\.(?:'+extensions+r')(?=[\s\)\]\}\"\'<>;,`*]|$)',re.I)
    allowed=[Path('C:/Users/PC/Downloads').resolve(),Path('C:/Users/PC/.codex/generated_images').resolve(),Path('C:/Users/PC/.codex/attachments').resolve()]
    missing=set(); extra=0
    for name in listed:
        path=Path(name)
        try: text=path.read_text(encoding='utf-8-sig')
        except (UnicodeError,OSError): continue
        text=text.replace('\\\\','\\')
        for match in pattern.finditer(text):
            candidate=Path(match.group()).resolve()
            if not any(under(candidate,root) for root in allowed): continue
            if candidate.is_file() and not candidate.is_symlink():
                if key(candidate) not in found:
                    found[key(candidate)]=(candidate,'explicit_project_reference'); extra+=1
            else: missing.add(str(candidate))
    return list(found.values()),roots,extra,sorted(missing)


def write_csv(path,rows,fields):
    with path.open('x',encoding='utf-8-sig',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=fields,extrasaction='ignore')
        writer.writeheader(); writer.writerows(rows)


def execute(destination):
    destination=destination.resolve()
    if destination.exists(): raise ValueError('Archive already exists; no overwrite')
    for _,root in ROOTS:
        if under(destination,root.resolve()): raise ValueError('Archive must not be nested in a source root')
    entries,roots,extra,missing=inventory()
    raw_bytes=sum(path.stat().st_size for path,_ in entries)
    free=shutil.disk_usage(destination.parent if destination.parent.exists() else destination.anchor).free
    if free<raw_bytes+2*1024**3: raise ValueError('Insufficient free space for worst-case copy plus safety margin')
    print(json.dumps({'phase':'inventory','files':len(entries),'bytes_before_dedup':raw_bytes,'extra_explicit_references':extra,'destination':str(destination)}),flush=True)
    rows=[]; groups=defaultdict(list)
    for i,(path,origin) in enumerate(entries,1):
        before=path.stat(); digest=sha(path); after=path.stat()
        if (before.st_size,before.st_mtime_ns)!=(after.st_size,after.st_mtime_ns):
            raise ValueError(f'Source changed while hashing: {path}')
        item={'source':str(path),'origin':origin,'bytes':before.st_size,'mtime_ns':before.st_mtime_ns,
              'sha256':digest,'role_index':role(path),'source_retained':True}
        rows.append(item); groups[digest].append(item)
        if i%500==0 or i==len(entries):
            print(json.dumps({'phase':'hash','done':i,'total':len(entries)}),flush=True)
    unique_bytes=sum(items[0]['bytes'] for items in groups.values())
    destination.mkdir(parents=True)
    copied=[]; category_counts=Counter()
    selected_seen=False
    for i,(digest,items) in enumerate(sorted(groups.items()),1):
        canonical=min(items,key=lambda r:(r['role_index'],0 if r['origin']=='project' else 1,len(r['source'])))
        category=CATEGORIES[canonical['role_index']]
        source=Path(canonical['source'])
        if canonical['role_index']==0:
            assert digest==SELECTED_HASH
            filename='EP01_BAN_DANG_CHON_v2_323.mp4'; selected_seen=True
        else:
            stem=re.sub(r'[<>:"/\\|?*\x00-\x1f]','_',source.stem)[:80].rstrip(' .')
            filename=f'{digest[:16]}__{stem}{source.suffix.casefold()}'
        relative=Path(category)/filename
        output=destination/relative
        output.parent.mkdir(exist_ok=True)
        if output.exists(): raise ValueError(f'Archive filename collision: {output}')
        current=source.stat()
        if (current.st_size,current.st_mtime_ns)!=(canonical['bytes'],canonical['mtime_ns']):
            raise ValueError(f'Source changed before copy: {source}')
        temporary=output.with_suffix(output.suffix+'.partial')
        shutil.copy2(source,temporary)
        if sha(temporary)!=digest: raise ValueError(f'Copy checksum mismatch: {source}')
        temporary.rename(output)
        for item in items:
            item['archive_relative']=relative.as_posix()
            item['category']=category
            item['same_content_source_count']=len(items)
            item['archive_copy_verified']=True
            item['deletion_permission']='NONE; paths may be referenced by editing scripts'
        copied.append({'sha256':digest,'bytes':canonical['bytes'],'archive_relative':relative.as_posix(),
                       'category':category,'source_copies':len(items),'canonical_source':str(source),'verified':True})
        category_counts[category]+=1
        if i%250==0 or i==len(groups):
            print(json.dumps({'phase':'copy_verified','done':i,'unique_total':len(groups)}),flush=True)
    assert selected_seen,'Latest selected video not found in archive'
    fields=['source','origin','bytes','sha256','category','archive_relative','same_content_source_count','archive_copy_verified','source_retained','deletion_permission']
    write_csv(destination/'DANH_MUC_TAT_CA_NGUON.csv',rows,fields)
    write_csv(destination/'DANH_MUC_TEP_DUY_NHAT.csv',copied,['sha256','bytes','archive_relative','category','source_copies','canonical_source','verified'])
    write_csv(destination/'CAC_BAN_TRUNG_NOI_DUNG.csv',[row for row in rows if row['same_content_source_count']>1],fields)
    write_csv(destination/'DUONG_DAN_THAM_CHIEU_CHUA_TIM_THAY.csv',[{'path':p,'status':'Missing historical literal path; not proof of a unique lost asset or cloud inventory'} for p in missing],['path','status'])
    # Keep project prompts, decisions and manifests next to media; no credentials or unrelated repos.
    docs=[]
    for source in PROJECT.rglob('*'):
        if not source.is_file() or source.is_symlink() or source.suffix.casefold() not in DOCS: continue
        if source.name.casefold() in ('credentials.json','secrets.json','token.json'): continue
        relative=Path('08_HO_SO_DU_AN')/source.relative_to(PROJECT)
        output=destination/relative; output.parent.mkdir(parents=True,exist_ok=True)
        digest=sha(source); shutil.copy2(source,output)
        assert sha(output)==digest
        docs.append({'source':str(source),'archive_relative':relative.as_posix(),'bytes':source.stat().st_size,'sha256':digest,'verified':True})
    tool=destination/'08_HO_SO_DU_AN/collect_ep01_media_324.py'
    shutil.copy2(Path(__file__),tool)
    write_csv(destination/'DANH_MUC_HO_SO.csv',docs,['source','archive_relative','bytes','sha256','verified'])
    summary={'record':'REC324','date':'2026-10-17','status':'LOCAL_ARCHIVE_COPIED_AND_SHA256_VERIFIED_NO_SOURCE_DELETED',
             'destination':str(destination),'source_roots':roots,'source_files':len(rows),'source_bytes':raw_bytes,
             'extra_explicit_reference_files':extra,'unique_media_files':len(copied),'unique_media_bytes':unique_bytes,
             'duplicate_source_copies':len(rows)-len(copied),'duplicate_source_bytes':raw_bytes-unique_bytes,
             'unique_category_counts':dict(category_counts),'project_documents_copied':len(docs),
             'project_document_bytes':sum(d['bytes'] for d in docs),'missing_historical_literal_paths':len(missing),
             'every_unique_copy_SHA256_verified':True,'selected_video_SHA256':SELECTED_HASH,
             'source_deletions':0,'source_moves':0,'cloud_Flow_assets_inventoried_or_deleted':False,
             'scope_limits':['Local files in four scoped roots plus existing media explicitly linked in project text','No broad Downloads/Pictures/other project sweep','Undownloaded Flow media not included or counted','Image category is a storage hint, not quality approval or deletion permission'],
             'manifests':{name:sha(destination/name) for name in ['DANH_MUC_TAT_CA_NGUON.csv','DANH_MUC_TEP_DUY_NHAT.csv','CAC_BAN_TRUNG_NOI_DUNG.csv','DUONG_DAN_THAM_CHIEU_CHUA_TIM_THAY.csv','DANH_MUC_HO_SO.csv']}}
    (destination/'TONG_HOP_324.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    readme=f'''# EP01 Nem Bùi — kho media local đã gom

Ngày 17-10-2026. Chỉ sao chép, không di chuyển/xóa nguồn và không thay nguồn trong project.

- {len(rows):,} tệp nguồn local, {raw_bytes/1024**3:.3f} GiB trước lọc trùng.
- {len(copied):,} nội dung media duy nhất, {unique_bytes/1024**3:.3f} GiB, tất cả copy được kiểm SHA256.
- {len(rows)-len(copied):,} bản nguồn trùng nội dung; không chép lặp binary trong kho, mọi đường dẫn vẫn được liệt kê.
- Giữ kèm âm thanh, {len(docs):,} tài liệu/prompt/quyết định/manifest để còn truy xuất và sửa tiếp.

## Mở video đang chọn

[EP01 v2 REC323](00_BAN_DANG_CHON/EP01_BAN_DANG_CHON_v2_323.mp4). Đây là video mới nhất owner vừa chấp nhận; không đổi các giới hạn final30/finishing trong hồ sơ dự án.

## Cách tra cứu

- DANH_MUC_TAT_CA_NGUON.csv: mỗi file gốc → nội dung SHA256 → vị trí trong kho.
- DANH_MUC_TEP_DUY_NHAT.csv: một dòng/một nội dung đã copy.
- CAC_BAN_TRUNG_NOI_DUNG.csv: các nguồn có nội dung trùng, không phải lệnh xóa.
- DANH_MUC_HO_SO.csv: tài liệu đi kèm và hash.
- TONG_HOP_324.json: số lượng, phạm vi và hash các danh mục.
- DUONG_DAN_THAM_CHIEU_CHUA_TIM_THAY.csv: literal path lịch sử chưa tìm thấy; có thể là đường dẫn cũ/biến/đổi tên, không kết luận từng dòng là mất asset duy nhất.

Mỗi binary trùng hoàn toàn chỉ lưu một lần. Tên có tiền tố hash để không đè lên nhau. Giữ riêng ảnh đầu vào, ảnh tạo/tham chiếu, video nguồn, bản dựng/thử, âm thanh và ảnh kiểm tra/khung trích. Phân loại không chứng nhận chất lượng hoặc quyền sử dụng.

## Có nên xóa hàng loạt không?

**Chưa nên.** Kho này vẫn ở cùng máy, không thay thế bản backup ngoài máy. Trước khi xóa, sao lưu thêm ổ khác/cloud và kiểm mở video/ảnh cần giữ.

Ưu tiên dọn các bản tải/bàn giao trùng ở Downloads sau khi đối soát; có thể xem xét ảnh trích/QC tái tạo được nếu còn video nguồn và lệnh. Không mặc định xóa toàn bộ ảnh trong evidence hoặc QC: có ảnh nguồn/bằng chứng chỉ còn ở đó.

**Không xóa nguồn trong repository, voice đã chọn, master/reference/đầu vào hoặc project Flow hàng loạt.** Nhiều file không nằm trong Git; xóa đường dẫn gốc có thể làm script/EDL không chạy dù binary đã nằm trong kho. Muốn biến kho thành nguồn duy nhất phải cập nhật/relink và kiểm dựng lại trước.

Chỉ gom media đang có local. Những ảnh/video chỉ còn trên Flow chưa được kiểm kê/tải về trong lượt này. Không xóa gì trên Flow và không sử dụng credit.
'''
    (destination/'README.md').write_text(readme,encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False),flush=True)


def supplement(destination):
    """Recover paths ending at Markdown backticks; preserve first-pass metadata."""
    destination=destination.resolve()
    initial=json.loads((destination/'TONG_HOP_324.json').read_text(encoding='utf-8'))
    if (destination/'TONG_HOP_324_V2.json').exists(): raise ValueError('Supplement already exists')
    with (destination/'DANH_MUC_TAT_CA_NGUON.csv').open(encoding='utf-8-sig',newline='') as stream:
        rows=list(csv.DictReader(stream))
    with (destination/'DANH_MUC_TEP_DUY_NHAT.csv').open(encoding='utf-8-sig',newline='') as stream:
        unique=list(csv.DictReader(stream))
    for row in rows: row['bytes']=int(row['bytes'])
    for row in unique: row['bytes']=int(row['bytes'])
    previous={key(Path(row['source'])) for row in rows}
    byhash={row['sha256']:row for row in unique}
    entries,roots,extra,missing=inventory()
    new=[(path,origin) for path,origin in entries if key(path) not in previous]
    print(json.dumps({'phase':'reference_supplement','new_referenced_paths':len(new),'corrected_missing_literals':len(missing)}),flush=True)
    added_unique=0
    for source,origin in new:
        digest=sha(source); size=source.stat().st_size
        if digest not in byhash:
            category=CATEGORIES[role(source)]
            stem=re.sub(r'[<>:"/\\|?*\x00-\x1f]','_',source.stem)[:80].rstrip(' .')
            relative=Path(category)/f'{digest[:16]}__{stem}{source.suffix.casefold()}'
            output=destination/relative; output.parent.mkdir(exist_ok=True)
            if output.exists(): raise ValueError('Supplement filename collision')
            partial=output.with_suffix(output.suffix+'.partial')
            shutil.copy2(source,partial); assert sha(partial)==digest
            partial.rename(output)
            row={'sha256':digest,'bytes':size,'archive_relative':relative.as_posix(),'category':category,
                 'source_copies':0,'canonical_source':str(source),'verified':True}
            unique.append(row); byhash[digest]=row; added_unique+=1
        item=byhash[digest]
        rows.append({'source':str(source),'origin':origin,'bytes':size,'sha256':digest,
                     'archive_relative':item['archive_relative'],'category':item['category'],
                     'archive_copy_verified':True,'source_retained':True,
                     'deletion_permission':'NONE; paths may be referenced by editing scripts'})
    counts=Counter(row['sha256'] for row in rows)
    for row in rows: row['same_content_source_count']=counts[row['sha256']]
    for row in unique: row['source_copies']=counts[row['sha256']]
    fields=['source','origin','bytes','sha256','category','archive_relative','same_content_source_count','archive_copy_verified','source_retained','deletion_permission']
    write_csv(destination/'DANH_MUC_TAT_CA_NGUON_V2.csv',rows,fields)
    write_csv(destination/'DANH_MUC_TEP_DUY_NHAT_V2.csv',unique,['sha256','bytes','archive_relative','category','source_copies','canonical_source','verified'])
    write_csv(destination/'CAC_BAN_TRUNG_NOI_DUNG_V2.csv',[r for r in rows if counts[r['sha256']]>1],fields)
    write_csv(destination/'DUONG_DAN_THAM_CHIEU_CHUA_TIM_THAY_V2.csv',[{'path':p,'status':'Missing literal; not a unique-asset loss verdict'} for p in missing],['path','status'])
    tool=destination/'08_HO_SO_DU_AN/collect_ep01_media_324_v2.py'
    shutil.copy2(Path(__file__),tool); assert sha(tool)==sha(Path(__file__))
    summary={**initial,'status':'LOCAL_ARCHIVE_AND_MARKDOWN_REFERENCE_SUPPLEMENT_VERIFIED_NO_SOURCE_DELETED',
             'source_roots':roots,'source_files':len(rows),'source_bytes':sum(r['bytes'] for r in rows),
             'extra_explicit_reference_files':extra,'unique_media_files':len(unique),
             'unique_media_bytes':sum(r['bytes'] for r in unique),'duplicate_source_copies':len(rows)-len(unique),
             'duplicate_source_bytes':sum(r['bytes'] for r in rows)-sum(r['bytes'] for r in unique),
             'unique_category_counts':dict(Counter(r['category'] for r in unique)),
             'missing_historical_literal_paths':len(missing),
             'reference_parser_correction':{'new_paths':len(new),'new_unique_media':added_unique,'reason':'Treat Markdown backticks as path terminators, do not absorb prose into a fake filename'},
             'active_manifest_version':2,'initial_metadata_preserved':True,
             'manifests':{name:sha(destination/name) for name in ['DANH_MUC_TAT_CA_NGUON_V2.csv','DANH_MUC_TEP_DUY_NHAT_V2.csv','CAC_BAN_TRUNG_NOI_DUNG_V2.csv','DUONG_DAN_THAM_CHIEU_CHUA_TIM_THAY_V2.csv','DANH_MUC_HO_SO.csv']}}
    (destination/'TONG_HOP_324_V2.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destination',type=Path,required=True)
    parser.add_argument('--execute',action='store_true')
    parser.add_argument('--supplement',action='store_true')
    args=parser.parse_args()
    if args.supplement:
        if not args.execute: raise ValueError('Supplement requires --execute')
        supplement(args.destination)
    elif not args.execute:
        entries,roots,extra,missing=inventory()
        print(json.dumps({'roots':roots,'source_files':len(entries),'source_bytes':sum(p.stat().st_size for p,_ in entries),'extra_referenced':extra,'missing_literals':len(missing),'copy_or_delete_performed':False}))
    else:
        execute(args.destination)
