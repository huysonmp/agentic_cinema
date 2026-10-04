# 172 — Đối chứng K20 một người nói

Ngày2026-10-04. Owner trả lời “ok” ngay sau đề nghị bộ đối chứng K20 cùng sample audition, x3 Omni10s tối đa21credit. **REQUEST_APPROVED / THREE_NATIVE_RECEIVED / INVALID_CONTROL**. Không mở quyền cho nhóm diễn/Đào tiếp theo, không thêm ngân sách toàn tập hoặc nâng Quality.

**Đính chính sau submit: INVALID_CONTROL / INPUT_REMOVED_DURING_PREFLIGHT.** Root bấm chip để xem ảnh, thao tác đã gỡ OPEN7; ảnh `preflight-request.png` cho thấy chỉ voice/chip lỗi trước gửi. Đã gửi nhầm bộ thiếu ảnh, không dùng ba kết quả để kết luận reference/model giữ hoặc đổi identity. Phần preflight hoàn chỉnh bên dưới là nhận định tại thời điểm thao tác, bị đính chính bởi ảnh và lịch sử sau gửi. Không tự retry vượt cap21.

## Quyết định và tiêu chí

- Khoai K20 custom Orus `fb1188da-e6c8-4156-9bba-0576c01a8da6`; không K12/base. Giữ toàn bộ common/performance audition, không sửa preset.
- OPEN7 diagnostic-only; một người nói, Đào im lặng. Lời109 ký tự đúng mẫu148/149, không đổi script production32.
- Omni1.1Flash/Thành phần/360p/9:16/10s/x3; không gọi bộ Lite. Giá phải đọc actual≤21 trước submit, không dùng quote lịch sử làm actual.
- Giọng nghe phải so với mẫu K20 gốc. Decode/ASR chỉ kiểm kỹ thuật và lời, không tự duyệt identity/accent/diễn.
- Đối chứng chuyển tuyến preview→video; không có seed/model revision nên không tuyên bố tất cả điều kiện model giống nhau. Chưa tách nhân quả mọi khác biệt với170.

Folder owner: `C:/Users/PC/Downloads/du_an_nem_bui/172_k20_control/`. Số dư trước/generation/media ID/native/hash/QC ghi khi có actual. Khoản được phép chi đầu lượt67 theo170, bộ này nằm trong67; không cộng21 thành ngân sách mới.

## Ghi chú preflight ban đầu

Đọc trực tiếp K20 library: ID textbox/performance đúng K20, DOM audio đúng nguồn8,76s readyState4. Khi thêm riêng voice trước ảnh, chip báo lỗi và tooltip “Thành phần âm thanh cần có các thành phần khác thì mới hoạt động được.” Đây là ràng buộc đầu vào UI đã quan sát, chưa phải chứng minh nguồn K20 hỏng hoặc nguyên nhân sai giọng ở170. Phải thêm OPEN7 rồi gắn/kiểm lại voice trước gửi. Không submit đầu vào lỗi.

Ảnh ban đầu `K20-attachment-error.png`; trạng thái trước khi đủ ảnh, không dùng làm bằng chứng request hoàn chỉnh. Kết quả và preflight cuối bổ sung sau kiểm thực.

## Preflight hoàn chỉnh

Giá actual21, Omni1.1Flash/Thành phần/360p/9:16/10s/x3; owner cap21 phù hợp. Số dư account đọc live **317**, cao hơn snapshot267 ngày03; không biết nguyên nhân tăng50, không suy thành quyền chi mới. Quyền dự án vẫn67.

OPEN7 đã chọn từ option `T2-CODEX-OPEN_v0.7.png`, nguồn UI image `43057def-574c-4ca7-916c-d55083f9b670`. Gắn lại K20 sau ảnh, hai chip không còn icon error. Prompt có token thực `.mention-chip`, `data-mention-id=fb1188da-e6c8-4156-9bba-0576c01a8da6`, `data-reference-type=audio`; chỉ một nguồn giọng, không Aoede. Đây là bằng chứng binding UI trước submit, chưa bảo đảm server thực thi hoặc output identity đạt.

Prompt readback nguyên văn tại `evidence/172/prompt-C0.txt`; chữ Orus trong bản text là token có ID trên, không plain-text name-only. Lỗi nhập dài bị ngắt, đã đọc lại phần nhập và dán phần còn thiếu; readback cuối đủ lời/performance, không submit bản dở. Không sửa preset K20. Ảnh `preflight-settings.png`/`preflight-request.png` trong folder owner lưu quote và compose trước gửi.

## Submit thực

Đã bấm Bắt đầu tạo một lần, UI xuất ba ô0% và compose trở về trống. Không retry, không gửi nhóm biến mới. Quote tổng21 nằm trong cap. Chi ròng thực/số dư sau còn chờ đối soát; không ghi ba media thành công khi mới queued. Ảnh `submitted.png` lưu trạng thái gửi.

## Sai sót thao tác cuối và nguyên nhân quy trình

Đã có hai chip và token K20 đúng trước bước kiểm ảnh. Bấm chip ảnh để “kiểm nguồn”, rồi bấm chip lần nữa để “đóng preview” làm thay đổi đầu vào. Root có lưu screenshot cuối nhưng chưa xem/readback lại số lượng/chủng loại chip và cảnh báo trước submit. Khi xem ảnh sau tạo, thấy cảnh báo thành phần âm thanh cần thành phần khác, chỉ còn chip voice. Lịch sử C01 không hiện ảnh/voice như bundle170; không suy token trong text lịch sử là server reference được áp dụng.

Đây là **lỗi preflight đã xác nhận trong bộ172**, không chứng minh170 cũng mất ảnh/voice. Bài học153 đã có cảnh báo click chip gỡ input nhưng root chưa dùng đúng trước thao tác. Biện pháp: chọn ảnh/voice qua picker; đọc source ID ở picker/mention, không bấm chip compose để mở detail; sau mọi thao tác nguồn phải kiểm số chip/icon error/token và xem screenshot thực trước submit. Nếu đã thay đổi compose sau lần kiểm, preflight cũ hết hiệu lực.

Chưa sửa preset K20; chưa tạo bộ mới hoặc xin thêm ngân sách tự động. Vẫn lưu đủ ba native/QC/bằng chứng như failed experiment, không gọi C0_VALID/PASS hoặc thay master. Không coi thiếu ảnh tất yếu gây sai giọng; đó là lý do control không hợp lệ và binding chưa bảo đảm.

## Kết quả lưu thực

| Mã | Media ID | Native filename | Bytes |
| --- | --- | --- | ---: |
| C01 | 2a6c3e93-6918-4797-974d-16e377db7cc7 | Record_voice_diagnostic_for_char…_20261004104743.mp4 | 710751 |
| C02 | 2ba2363f-3300-4760-994f-27cdc46a4b47 | Record_voice_diagnostic_for_char…_20261004104913.mp4 | 586300 |
| C03 | 6b8484d6-6df4-4603-82d1-bb54e661fec4 | Record_voice_diagnostic_for_char…_20261004105058.mp4 | 652507 |

Tải qua menu360p native trong tab riêng. C01 lần tải trong tab cũ chưa có file khi kiểm, tab mới tải được; C02/C03 tiếp tục cùng tab tải, chỉ chuyển sau xác minh file. Đóng tab tải tạm sau hoàn tất. Toast không thay file thực/bytes/decode. Bản owner `C01_INVALID_CONTROL.mp4` tớiC03 và WAV cùng tên; không dùng file cũ170.

Ba MP4 full decode sạch, H264360×640/24fps/10s, AAC48kHz stereo. WAV PCM16bit giữ48kHz stereo, không chỉnh tốc độ/gain/giọng; WAV16kmono của QC chỉ dùng ASR. Script `scripts/local_voice_qc.py`, `.venv/Scripts/python.exe`, faster-whisper small CPU/int8 offline, không initial prompt/API. QC `artifacts/voice-qc/172-C01` tớiC03, copy folder owner `qc/`.

- C01 ASR đọc đủ câu mẫu, không thêm performance directions trong transcript.
- C02 ASR nhận “mẹ gian gạo” thay vì “mẹ rang gạo”; cần nghe, không kết luận phát âm sai từ ASR.
- C03 ASR đọc đủ câu mẫu, tách Khoan và câu cuối thành segment riêng; không suy biểu cảm/identity từ segment.

Chưa root nghe nghiệm thu; các file đưa owner nghe tham khảo, **không phải control hợp lệ/PASS**. Không dùng hình để ghép EP01. Không chọn winner hoặc quy lỗi cho model/token/performance.

SHA256 MP4:

- C01 `9e17991f15f20dbc50cfa5504618c522b58060ee2cbb497d35aa9807d06100bc`.
- C02 `3f25fddc4f5d08d8fe6d2bac78d232ef33e2aa18477cade6cf72f6738de2283f`.
- C03 `5ae77a339624019bc3413f35cc684b0202cbe03cacb0dcb9800b3fb5467948ef`.

## Chi phí và bước tiếp

Account actual317→296, giảm21 đúng quote. Trần hợp nhất134; lũy kế88, còn **46**. Chênh tăng50 so snapshot account ngày03 không tự mở quyền chi. Không hoàn/ẩn chi phí bộ invalid. Khoản thêm90 vẫn chưa duyệt; không Quality.

Đề nghị owner cho phép chạy lại đúng bộ x3 **tối đa21 lấy từ46 còn lại**, không xin cộng21 vào ngân sách. Nếu được duyệt: preflight hoàn chỉnh readback sau mọi thao tác nguồn và xem screenshot thực; quote actual≤21 mới gửi. Sau chạy lại sẽ còn25 nếu giá21, nên thiếu coverage vẫn phải trình riêng. Chưa chạy lại.

## Tổng hợp vòng

- Đã xác định: tạo/tải/decode đủ ba file, sample có transcript, nhưng OPEN7 bị gỡ trong thao tác preflight của root.
- Đã chốt: quyền bộ21 đã dùng; ghi INVALID_CONTROL, giữ nguồn giọng/script và không dùng master.
- Giả định: identity có thể đánh giá tham khảo qua nghe; không giải thích cơ chế lỗi170 bằng bộ sai input này.
- Còn mở: đối chứng hợp lệ, server voice binding/identity, ngân sách/coverage phần còn lại.
- Tiếp: owner nghe nếu muốn, xác nhận chạy lại21 trong46 còn lại; không tự submit thêm.
