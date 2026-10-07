# REC218-SIA-R1 — Kiểm năng lực và provenance SIA/AV

Ngày 2026-10-06. Reviewer độc lập: `REC218-SIA-R1`; scope `CAPABILITY_AND_PROVENANCE`. Quyền theo owner217 A/A/A: đọc local, probe/hash, viết duy nhất report này. Không đọc maker218, root211, tài liệu216 hoặc reviewer khác; không sửa media/code, browser/API/generation/credit/install/git/spawn. Đây là kiểm bằng chứng, **không PASS audio hoặc phim**.

## 1. Năng lực thực tế và đầu vào

| Năng lực | Thực hiện | Giới hạn |
|---|---|---|
| Đọc tài liệu/JSON local | Có | Nội dung văn bản không phải nghe. |
| SHA256, probe, đọc PCM | Có | Chứng minh bytes/stream/nguồn, không nhận dạng giọng. |
| Nghe thực toàn nguồn | Không | `heard_text`, người nói và sắc thái chưa được quan sát. |
| So reference K20/D06 | Không | Chưa được cấp exact local file chuẩn/hash/approval tương ứng. |
| Xem liên tục có tiếng | Không | Không có recovery AV master trong dispatch; không chứng nhận môi hoặc người nghe. |
| Xem ảnh mẫu | Không chạy | Ảnh không bổ sung identity hoặc lip-sync nên không cần cho scope này. |

Đã đọc đầy đủ contract02/10 trong `agents/audio_edit_quality` của series; episode178,179,201,203,214,217; JSON thoại179/approval201; WAV202 và manifest owner. Sau provenance, đọc ba script recovery/finishing/verifier; root mở rộng allowlist để đọc đầy đủ `ep01_speaker_gate.py`. Không chạy renderer/gate với report giả.

Công cụ thật: PowerShell Get-Content/Get-FileHash; FFprobe/FFmpeg sẵn có tại `.local-tools/ffmpeg/verified-9.0.2/ffmpeg-9.0.2-essentials_build/bin/`; Python3.14 với wave/hashlib/subprocess để đọc PCM. FFmpeg giải mã audio vào bộ nhớ; không tạo excerpt hoặc sửa file. Lần tìm FFprobe trong PATH không thấy; dùng executable local đã được manifest/script chỉ rõ, không cài thêm. Không có actual hearing qua những công cụ này; playlink hoặc tên role không tạo năng lực nghe.

## 2. Bytes, nguồn duyệt và phạm vi giữ lại

Ba target tại `C:/Users/PC/Downloads/du_an_nem_bui/` được kiểm trực tiếp:

| File | SHA256 hiện hành | Probe |
|---|---|---|
| `200_n02_replacement/N02_NATIVE.mp4` | `72cbaf7d9f66932002dfce1b1a57fa464935c315e84e54ae094fe29aa805a153` | 10,005s; H264 360×640/24fps, AAC 48kHz stereo; 1.197.956 byte. |
| `200_n02_replacement/N02_EXPECTED_K20_REVIEW.wav` | `52c7a027f55c6e354b0c5ac1d697bd8789682bfbc9ac99907a45e741f129b062` | 10,005s; PCM16/48kHz stereo, 480.240 frame. |
| `202_dialogue_join_review/EP01_7_LUOT_N02_MOI_REVIEW_NOT_FINAL.wav` | `3c83b7d6188f5b973b0ef5c77ebc1fc16afde7c11827764c5302145741b736d4` | 22,055s; PCM16/48kHz stereo, 1.058.640 frame. |

Giải mã native thu 1.920.960 byte PCM, bằng toàn payload WAV N02. Payload đó bằng chính đoạn PCM202 bắt đầu 2,150s, dài 10,005s. Kết quả xác nhận bảo toàn N02, không chứng minh phát âm/identity. SHA256 manifest202: `beea2dbb711024613e836b04e8a0b9159b0df1ca24103b44d8cb0a1ddfa73448`; approval201: `5e736b24142ceee3c375a10f921b971d8f8aa4b1fab909cd1f63fd333cc03cbe`.

Approval201 ghi owner: “Đúng Khoai/K20 xuyên suốt, nhịp chấp nhận được”, bind đúng WAV52c7…; scope toàn N02 và nhịp. `root_heard_audio=false`, sáu lượt khác không được duyệt bởi câu trả lời đó. Đây là human acceptance hợp lệ trong hồ sơ, không biến thành reviewer này đã nghe.

Episode203 ghi owner “ok r đấy”, duyệt người nói/chỗ nối cả WAV3c83… của202. Hash live khớp. Giữ approval nguồn này; không vô hiệu vì thiếu formal SIA. Manifest202 còn `owner_join_approval=PENDING` là snapshot trước203, không phải quyết định hiện hành; phải đọc kèm203, không sửa lịch sử. Chưa đọc approval JSON203 trong dispatch; provenance approval203 ở đây dựa vào tài liệu203, không tự nhận đã đối soát JSON đó.

Tên EXPECTED_K20, preset IDs trong179 và transcript không phải voice reference. N02 đang kiểm không được làm mẫu chuẩn cho chính nó. Package179 giữ nguồn lời/vai C-v0.6; các trường media/budget năm179 là lịch sử, không dùng kết luận readiness hoặc quyền chi hiện tại. Storyboard214 hiện hành cần mặt người nói; ý đồ offscreen cũ tại203 không tự miễn kiểm hoặc thay214.

## 3. Bảy lượt: expected và observed

Timing dưới là khoảng **mapping WAV202**, không phải speech boundary đã nghe hoặc timeline recovery30s. N05–N07 chỉ có khoảng cụm; không chia mốc riêng. Mỗi dòng: heard_text, observed_speaker, observed_reference, within-turn/overlap và AV đều UNKNOWN bởi reviewer.

| Lượt | Expected / lời đã duyệt | Khoảng202 | Observed / identity |
|---|---|---|---|
| N01 | Đào/D06: Anh nhìn mãi. Không hợp thì để em. | 0–2,150s | UNKNOWN / HOLD |
| N02 | Khoai/K20: Khoan. Mùi này làm anh nhớ đến bếp nhà anh. Hồi bé, mẹ rang gạo, anh đứng chờ. | 2,150–12,155s | UNKNOWN / HOLD; owner201 duyệt toàn nguồn |
| N03 | Đào/D06: Anh chờ ăn à? | 12,155–13,025s | UNKNOWN / HOLD |
| N04 | Khoai/K20: Chờ mẹ quay lưng. | 13,025–14,055s | UNKNOWN / HOLD |
| N05 | Đào/D06: Chờ em quay lưng nữa à? | Cụm14,055–22,055s | UNKNOWN / HOLD |
| N06 | Khoai/K20: Anh gắp cho em mà. | Cụm14,055–22,055s | UNKNOWN / HOLD |
| N07 | Đào/D06: Thế em quay lại đúng lúc rồi. | Cụm14,055–22,055s | UNKNOWN / HOLD |

Manifest khai N01/N03/N04 là excerpt diagnostic183, cut_boundary_heard_by_root=false; cụm kết là full audio R01. Đây là provenance đọc được, chưa kiểm bytes từng nguồn phụ ngoài allowlist. Approval203 chấp nhận bản nối; vẫn cần nghe-reference độc lập trước formal AUDIO_SELECTION. Không có bằng chứng trong lượt này để kết luận đang lẫn speaker, cắt âm hoặc có lỗi “rang”; ASR201 nhận “gian” chỉ là nghi vấn ASR.

## 4. Findings và chốt chặn

| ID / severity / status | Expected → observed; bằng chứng và độ chắc | Action / stage / closure |
|---|---|---|
| SIA218-01 / MAJOR / HOLD_FOR_INPUT | SIA10 yêu cầu actual hearing + K20/D06 chuẩn; hiện thiếu capability và exact reference. Chắc về thiếu input, UNKNOWN về chất lượng nguồn. | Root cấp file/hash/preset/approval chuẩn; reviewer nghe toàn nguồn, ghi từng lượt và so mẫu. Đóng AUDIO_SELECTION bằng log thật bind đúng bytes; giữ duyệt201/203. |
| SIA218-02 / MAJOR / HOLD_FOR_INPUT | AV_ASSEMBLY/FINAL_AV cần target hiện hành; dispatch chưa có recovery master hoặc xem-nghe đầy đủ. Không suy mouth attribution từ ảnh. | EDIT/root cung cấp AV/hash/source map; kiểm mặt nói, người nghe im, sync và cut. Sau finishing kiểm lại export, owner duyệt đúng mốc217. |
| SIA218-03 / MAJOR / MITIGATED_CODE_INSPECTION_NOT_TESTED | Snapshot đầu thiếu bảng/reference SIA. Read-back cuối bridge bind target/package/reviewer/AV mode; evaluator kiểm fingerprint, nguồn/range, lời/vai/ref, bảy lượt và within-turn/overlap/sync. | Giữ lịch sử; cần evidence test thiếu/sai/stale trước closure cấu trúc. Không claim code đã nghe. |
| SIA218-04 / MAJOR / MITIGATED_CODE_INSPECTION_NOT_TESTED | Snapshot đầu closure thiếu scope/capability/checks. Read-back cuối đã yêu cầu ba nhóm này tương ứng finding. Chắc về patch, chưa chạy fixture độc lập. | Root lưu test/closure đúng snapshot; reviewer đọc log thật. Các chuỗi capability hoặc MET vẫn không thay actual hearing. |
| SIA218-05 / MINOR / MITIGATED_CODE_INSPECTION | Snapshot đầu verifier dòng1 nói identity “remains the owner's listening approval”. Read-back mới đã tách SIA/AV evidence và owner approval. | Giữ lịch sử; mitigation bằng đọc code mới, không phải nghe. |
| SIA218-06 / MAJOR / MITIGATED_CODE_INSPECTION_NOT_TESTED | Snapshot evaluator PASS_APPROVED_OFFSCREEN chỉ kiểm file/hash. Gate recovery mới yêu cầu đúng bảy dòng PASS_ONSCREEN, chặn kế thừa offscreen203 theo214. | Giữ lịch sử; cần evidence test trước closure. Không cấm insert có nhiệm vụ khi vẫn có speaking-face; chưa xác nhận media. |

Gate đã có kiểm hash/dependency, reviewer khác makers, chặn HOLD/paper và full-episode owner approval; các điểm này hữu ích nhưng không chứng minh nghệ thuật. Finishing vẫn bind209/210 cố định: chưa là renderer recovery tổng quát, không chạy chỉ vì có gate. Đây là giới hạn routing đọc từ code, không claim bypass đã xảy ra. Các phép loudness, caption mapping và technical-only không là bằng chứng nghe. Delivery cần report mới đúng export sau mix/caption; không cộng approval nguồn thành AV PASS.

Read-back cuối: recovery gate SHA256 `dba5141217112df41825ef9be32f5674e286e3b1e9fa50e7e0cb8047ae4f816e`; evaluator `1319e134a3a302574478b09d48522675532d559e5e2aa74c9d8325db02da6521`; verifier `640ee9db2d32f324cf8f66754b05b484cf2df6f245ad8f0c75934a9f8fdf4d60`; finisher `b97351f00f2214f44da7c5d80197e9d464cb22cb87849a61343a6dbca0995aec`. Finisher mới so decoded-picture hash của approvedAV với picture sẽ render trước ghi output. FINISHING cần AV_ASSEMBLY/FINAL_AV; DELIVERY cần FINAL_AV. Root báo 96 fixture tests đạt; chưa rerun/đọc log độc lập. Provenance vẫn cần reviewer đọc thực; code không biết nghe hoặc phát hiện lời khai gian. Không nâng mitigation thành closure/quality PASS.

```json
{"run_id":"REC218-SIA-R1","scope":"CAPABILITY_AND_PROVENANCE","actual_audio_reviewed":false,"references_compared":false,"actual_full_av_reviewed":false,"audio_selection":"HOLD_FOR_INPUT","av_assembly":"HOLD_FOR_INPUT","final_av":"HOLD_FOR_INPUT","release_authorized":false}
```

## 5. Tổng hợp vòng

- Đã xác định: bytes/hash/PCM N02 và bản202 khớp; đúng lời/vai expected theo178/179, không phải observed.
- Quyết định giữ: owner201 duyệt N02, owner203 duyệt bản nối; owner217 duyệt bounded local runs/gates/checkpoints, không cấp generation.
- Giả định sử dụng: provenance source phụ theo manifest202, chưa independently hash các nguồn đó; không giả mẫu chuẩn từ N02.
- Còn mở: actual hearing/reference, bảy lượt identity, cut boundaries, AV hiện hành và evidence test/closure gate SIA đã bổ sung.
- Bước tiếp: root cấp đúng reference và AV, bố trí reviewer có năng lực nghe/xem; kiểm tại bản dựng thử → N02 proof → toàn cảnh → export. Report này chỉ hoàn tất capability/provenance; mọi quality scope nêu trên giữ HOLD.
