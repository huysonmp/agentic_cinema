# REC307 — ACTUAL EDIT: bản sửa miệng C07 v1 và nối C06→C07

Ngày 14/10/2026. Reviewer `/root/c07_edit_context_307`, local read-only và ghi report này; không browser/credit/Git, không sửa EDL/media. Report context307 giữ nguyên. Kết luận: **READY_FOR_BUNDLED_5S_REVIEW / NOT_PRODUCTION_OR_FULL_AV_PASS**. Không thấy technical fail hoặc seam reset lớn trong evidence thực đã kiểm; có thể trình một gói5s thay vì hỏi từng thao tác nhỏ.

## Target, provenance và tự kiểm kỹ thuật

- Join: `07_edits/C06_C07_LOCAL_MOUTH_JOIN_5s_REVIEW_ONLY_307.mp4`. Tự SHA-256 `e97dd894d5225d64953145008494854fa154c691373b243e16490fdf41269fef`, khớp manifest/QC.
- C07 local: `07_edits/C07_TWOREF_LOCAL_MOUTH_v1_REVIEW_ONLY_307.mp4`. Tự SHA-256 `3637542889efc4dacbd1c86ebd67988b3e65472dd990fbc4a7ebc7ec9dc94d9c`, khớp repair manifest.
- Đọc đầy đủ `C07_MOUTH_LOCAL_v1_307/repair_manifest.json` và `C06_C07_LOCAL_JOIN_v1_307/native_evidence.json`; các authority/range/provenance đã full đọc trong context307, không chuyển scope approval306.
- Tự chạy ffprobe count_frames: join H.264720×1280,24fps,120F,video5s; AAC stereo48kHz5s, start_time0. C07 local72F,24fps,video/audio3s,start_time0. Tự full decode join bằng FFmpeg sang null: exit0, không lỗi.
- Join đúng source range C06native298 [0,48), C07local v1 [0,72); cut J48/2s. Đây là bản review120F, không bản toàn tập.
- Repair manifest xác nhận10F F5–14, donors nativeF4/F15, ROI[180,526,296,590], outsideROI0pixel khác trước encode,62frame không sửa nguyên; audio approved3s142packet payload/timing equal. Reviewer đã đọc bằng chứng này, **không tự chạy lại pixel hoặc packet comparison**. Đây là evidence kỹ thuật root, không nên trình thành phép đo reviewer độc lập đã thực hiện.
- Standalone C07 remux AAC approved3s; join dùng concat/new AAC encode, không bit-exact tiếng. Không voice mới/speed/gain/crossfade theo pipeline đã báo. Codec/probe/nguồn đúng không tự chứng minh đủ lời, giọng hay tiếng không pop.

## Phạm vi ảnh thực đã xem

Xem hai cutboard `cut12_01..02.png` đủ J36–59/cutJ48; sáu denseboard C07 `full12_01..06.png` đủF0–71 khôngpadding; hai board sequence join6fps F0–116; hai cropcompare pre-encodeF0–19; full encoded join J47/J48/J53/J58/J62/J63/J96/J119. Quy ước PNG số=J+1; F_C07=J−48. **Chưa xem mọi join frame full resolution, chưa nghe/xem continuous AV**; C07 range có all-frame board review.

## ACTUAL expected→observed

| Hạng mục | Quan sát thực | Kết luận scoped |
| --- | --- | --- |
| Cut C06→C07 | FullJ47/J48 và cutboards: hai người cùng trục/vị trí, mặt/pose gần khớp; cùng A/cốc nâng/2bát/đũa nghỉ/rau/đồ chấm. Không bước nhảy reset hoặc đổi chủ thể lớn. | Không thấy MAJOR visual seam trên stills; exact-pixel/nhịp cut AV chưa chứng nhận. |
| Repair miệng Khoai | C07F5–14 đã khép môi trên denseboard; fullJ53/F5 vàJ62/F14 không thấy miệng kép, răng còn sót hoặc viền rectangle rõ; biên F4→5/F14→15 gần đều qua crop/denseboard. Eyes/brows/head và Dao không bị freeze toàn khung. | Lỗi mở–khép người nghe đã được xử lý trên ảnh encoded; chưa kết luận nhịp mặt tự nhiên ở playback. |
| Vai nói nhìn thấy | C06Khoai có mở/khép môi, Đào nghe; C07Đào có chuỗi khẩu hình từ khoảngF12, Khoai giữ môi khép. Hai mặt không bị thay bằng món/crop. | Attribution hình hợp hướng N06Khoai→N07Đào, không chứng minh sync đúng audio chỉ từ stills. |
| Hands/props/A | C07 nâng bát bằng tay trongĐào, tay ngoài giữ cốc; Khoai giữ A trên đũa, chưa thả/ăn/gắp lại. Range0–71 chỉ2bát; đũa nghỉ/rau/2đồ chấm còn; không steam. | Không thấy lỗi duplicated-bowl đuôi native lọt vào range này hoặc regression ownership mới. |
| Clearance | FullJ96/F48 vàJ119/F71: bát/tayđỡĐào che một phần taynghỉKhoai. Không thấy xuyên rõ, nhưng bề mặt sau không đọc đủ. | CLEARANCE_NOT_CERTIFIED, không tự physicsPASS hoặc bịa collision. |
| Endpoint | J119=C07nativeF71: đúng bát dưới vùngA, cốc ngoài; Đào đang chớp mắt. Chưa thảA. | Không autochọn đầuC08 hoặc kéo thêmđuôi nativeF77+ cóbátmới. |

## Timing và giới hạn không được mất khi nghiệm thu

Local repair không đổi độ dài. QuaC05=632F; thêmC06=48F→680F; thêmC07candidate=72F→752F/31,333333s. Final30=720F đã vượt32F/1,333333s trước thả/C09. Rough35=840F còn88F/3,666667s cho phần còn lại, chưa actualproof đủ. Không bỏ lời, tăng tốc hoặc bỏC09. Food/A seam C05→C06 vẫn productionblocker riêng; success miệng C07 không đóng nó.

## Bước root nên làm trong cùng gói

1. Tổng hợp với reviewer pixel/voice và kiểm root; gửi **một bản5s** đã qua kỹ thuật, giải thích scope rõ: sửa miệng/range/nối thử, không toànphim.
2. Không hỏi lại các thao tác mask/hash/remux đã nằm trong quyền sửa local. Owner chỉ cần đánh giá perceived diễn/nhịp/đối thoại/sync của bản cuối gói khi tool không thực nghe được; không cần hỏi lại approved D06 standalone nếu track giữ nguyên.
3. Nếu gói perceived đạt, ghi scope đúng, rồi hoàn tất clearance/entryendpoint/timing kết trước mởC08. Không tự promote EDL, chạy trảphí/retry hoặc mởdựphòng. Không lấy stills,ASR hoặc packet equality làm FULL_AV_PASS.

`actual_listening=NOT_PERFORMED`; `continuous_AV_review=NOT_PERFORMED`; `production_selected=false`; `C08_authorized=false`; `Flow_credit_debit=0` trong phần việc reviewer.
