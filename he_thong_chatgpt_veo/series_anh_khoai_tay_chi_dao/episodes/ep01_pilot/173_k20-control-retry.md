# 173 — Thử lại đối chứng K20, kiểm đầu vào sau lỗi172

**Phản hồi owner sau trình nghe — [174](174_owner-provisional-acceptance-k20-controls.md):** cả R01/R02/R03 đều “tạm chấp nhận được”. Gate nghe bộ này chuyển từ pending sang `OWNER_PROVISIONAL_VOICE_ACCEPTANCE`; không phải giống hệt mẫu, voice production PASS hoặc duyệt hình/cặp thoại. Nhật ký dưới giữ trạng thái ở thời điểm bàn giao; không yêu cầu owner nghe lại để chọn winner.

Ngày 2026-10-04. Owner yêu cầu “tiếp tục đi” sau đề nghị chạy lại bộ x3 tối đa21 từ46 còn lại tại172. Trạng thái cuối **UI_INPUT_VERIFIED / THREE_NATIVE_DECODED / OWNER_IDENTITY_REVIEW_PENDING**. Không cấp ngân sách mới, không duyệt thêm nhóm diễn/Đào hoặc Quality.

## Phạm vi đã duyệt

OPEN7 diagnostic-only, K20 custom Orus `fb1188da-e6c8-4156-9bba-0576c01a8da6`; Khoai nói riêng đúng sample109 ký tự/performance audition, Đào im lặng. Giữ prompt-C0 tại evidence172, chèn token thực bằng menu@; không dùng tên giọng làm thay ID. Omni1.1Flash/Thành phần/360p/9:16/10s/x3, cap21; phải đọc quote actual trước submit. Ngân sách đầu lượt46, account live296.

Folder owner: `C:/Users/PC/Downloads/du_an_nem_bui/173_k20_control_retry/`.172 giữ INVALID_CONTROL không ghi đè. Bộ173 chỉ được gọi INPUT_VERIFIED khi kiểm readback cả ảnh+voice, token, route/quote và xem screenshot ngay trước submit. Không bấm chip để kiểm detail; không dùng screenshot chưa xem làm chứng nhận.

Giải mã/ASR không thay nghe identity. Root chưa có năng lực nghe độc lập; owner so trực tiếp mẫu K20 gốc sau nhận đủ ba audio. Chưa tự chọn winner/production PASS hoặc đóng RCA.

## Preflight đã thực kiểm

Account296; quote actual21, Omni1.1Flash/Thành phần/360p/9:16/10s/x3. K20 library giữ sample109 ký tự/performance đúng ID, DOM audio8,76s readyState4. Token prompt thực `data-mention-id=fb1188da-e6c8-4156-9bba-0576c01a8da6`, `data-reference-type=audio`.

Đọc chip không click: hai button Thành phần; chip ảnh có image `43057def-574c-4ca7-916c-d55083f9b670` đúng OPEN7; chip voice có `cancelvoice_selection`, không `error`. Root đã xem screenshot thực `preflight-request-verified.png`: thấy ảnh và voice, không tooltip lỗi. Sau lần kiểm này không đổi compose trước submit. Đây là INPUT_VERIFIED ở UI, không bảo đảm identity output.

Prompt readback khớp nguyên văn `evidence/172/prompt-C0.txt`; copy sang `evidence/173/prompt-C0.txt` để giữ provenance riêng. Bản text không thể biểu diễn token, ID/loại token ghi trên. Screenshot settings và request ở folder owner173. Không reuse prompt edit/history hoặc thay preset.

## Submit

Một lần Bắt đầu tạo sau final readback, không thay compose sau kiểm. Ba ô mới cùng tiêu đề “Recording diagnostic voice for c…” hiện tiến độ6/7/6%; compose trở về trống. Chưa retry hoặc thêm biến. Quote21 phù hợp cap; chi actual/media còn chờ nhận. Manifest preflight tại `evidence/173/preflight.json`. Hướng dẫn nghe đối chiếu lưu folder owner; không ghi agent đã nghe khi mới kiểm kỹ thuật.

## Nhận file và kiểm kỹ thuật thực

| Mẫu | Flow media ID | Native filename | Bytes |
| --- | --- | --- | ---: |
| R01 | 5ad0bca5-a982-478a-841e-5a755233b9ee | Recording_diagnostic_voice_for_c…_20261004114416.mp4 | 1115156 |
| R02 | 47ae1f68-9979-4d2d-aadd-f01e3f0de77d | Recording_diagnostic_voice_for_c…_20261004114535.mp4 | 1093485 |
| R03 | 32ad9a2a-0b6c-4d11-9eaa-6a921056c04a | Recording_diagnostic_voice_for_c…_20261004114656.mp4 | 1059455 |

Ba native tải qua menu360p trong tab tải riêng; đọc file thực/bytes và full decode sạch bằng FFmpeg9.0.2. H264360×640/24fps/10s, AAC48kHz stereo. Bản owner `R01.mp4` tớiR03, WAV `R01_VOICE_PENDING.wav` tớiR03 giữ48kHz stereo PCM16bit, không đổi gain/tốc độ/giọng. Lịch sử R01 có cả chip ảnh và voice; không bấm để reuse/chỉnh. Đây là bằng chứng đầu vào UI, chưa trực tiếp chứng nhận server hoặc identity.

QC offline: `.venv/Scripts/python.exe scripts/local_voice_qc.py`, faster-whisper small CPU/int8, tiếng Việt, không initial prompt/API. Báo cáo `artifacts/voice-qc/173-R01` tớiR03; copy folder owner `qc/`. WAV16kmono trong QC chỉ dùng ASR, không bản nghe audition.

| Mẫu | Transcript cần đối chiếu | Mean/max dBFS |
| --- | --- | --- |
| R01 | ASR nhận đủ lời sample | -17,4 / 0,0 |
| R02 | ASR nhận “mẹ gian gạo” thay “mẹ rang gạo” | -17,6 / -0,0 |
| R03 | ASR nhận “mẹ gian gạo” thay “mẹ rang gạo” | -18,7 / 0,0 |

ASR khác không xác nhận phát âm sai hoặc sai vùng giọng; peak sát0dBFS không đủ kết luận nghe thấy clipping. Chưa root nghe nghiệm thu, chưa review hình/chuyển động/lip-sync toàn bộ; không dùng hình của bộ này cho master theo mặc định. Chưa winner hoặc production PASS.

SHA256 MP4:

- R01 `23a22cf49801bf58d4aee9dbe9f1d60fc845037fd33d5eef69349c547eb90c6a`.
- R02 `385faa935c33f12b7f2559948d1e27161f8ef3adfea6820a9a3c5fb4dc6f3c97`.
- R03 `2fb039757fca2fae62059478133fcaf9d679e7e7e6f76d2c305b5704061b43aa`.

Đối soát PCM của mỗi MP4/WAV, giải mã cùng PCM16bit giữ rate/channel, hai hash bằng nhau:

- R01 `96e0293d72e3b2fc6b96f8444e31b1fd3c9bf09194315a45ad5a5686d674c3b8`.
- R02 `959f927525e8f75b4258255df58a5445fff2072a1e8a1f17aa76c6b6a474d6be`.
- R03 `3ce852446f98061ee7369bb5c31028247b57b9549b77eb8e2c1ebe01c998c1f0`.

## Đối soát chi và gate nghe

Account live296→275, chi ròng21 đúng quote/cap. Trần dự án134, lũy kế109, còn **25** được phép chi. Không retry/Quality/nhóm Đào mới; khoản thêm90 vẫn chưa duyệt. Account275 không là quyền chi275. Tab tải tạm đã đóng; tab dự án giữ ở thư viện K20 đúng ID/performance để owner bấm **Phát bản nghe trước** so trực tiếp, không tạo audition mới.

Owner cần đánh giá từng R01/R02/R03: cùng chất K20, gần nhưng khác, khác rõ hoặc chưa chắc; ghi riêng identity với nhịp/diễn. `HUONG_DAN_NGHE.md` ở folder owner. Nếu cả ba khác, không tự thử tiếp các kiểu diễn; ưu tiên kiểm tuyến tham chiếu/preview→video. Nếu có mẫu sát, chỉ sau quyết định owner mới trình lớp thoại/diễn/hai người tiếp theo và chi phí trong phần25 còn lại. Không đóng RCA171 chỉ từ decode/ASR hoặc một mẫu sát.

## Tổng kết vòng

- Đã xác định: input ảnh+K20 và token đúng ở final preflight, tạo/tải/decode đủ ba native; WAV khớp PCM gốc.
- Đã chốt: chạy lại bộ21 từ46; không đổi K20/D06/script32; bộ172 giữ INVALID_CONTROL.
- Giả định: bộ173 cho phép owner so nghe cùng sample; chưa biết server giữ identity tới mức nào.
- Còn mở: nghe identity/accent/diễn, hai chỗ ASR rang/gian, cơ chế lỗi170 và coverage cuối; chưa production PASS.
- Tiếp: owner nghe cả ba so K20, ghi nhận từng mẫu rồi chọn phép thử phân biệt kế tiếp; chưa generation thêm.
