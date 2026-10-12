# REC275 — Endpoint tự hoàn tất và trim đổi boundary

Bind source T03 `36f04086a2e3d6d3d688f64ca743909184955bf1a714094def5dd8cd3747ff7c`, prompt `42b412ec3bb6e7d3dd4b86fd980ad5a9c0a2a494dae899ae2f9bf077028e35d9`, proposal cut `58f13ea424300e0cde09000d37cf42839ac7b8ba7c6d2d6f64c02eeb9022594d`.

1. Nguồn giữ cốc nhưng tự hạ/thả A vào bát. Đóng từng scope, không dùng việc sửa cốc làm toàn-shot PASS.
2. Bỏ cue một khóe là thay tiêu chí diễn; không dùng “hai khóe nâng” hoặc “lộ răng” đơn độc để tái áp brief cũ. Vẫn cần nghe/xem đúng target về nét ngượng.
3. Prompt đã cấm thả, nhưng output vẫn hoàn tất động tác. Chỉ kết luận tầng sinh source; không tự chứng minh model, wording, duration hoặc can thiệp diễn là nguyên nhân duy nhất.
4. Prefix[0,57) giữ A còn kẹp/cách vành, nhưng tay vẫn chuyển. Trim loại release không tự tạo stop-and-hold. Đây là boundary proposal cần owner, rồi kiểm chuyển động nối/C07/nhận/thả.
5. Cut theo frame + AAC stream-copy: xác minh counts/hash/decode và packet payload/PTS. Audio packet boundary có thể dài hơn video vài ms; ghi số thực, không bảo đảm AV/voice từ metadata.
6. Công tắc return-without-audio nằm trong Cài đặt lưới ô hiện hành; model có icon loa không thay state switch. UI ID preset hiện có thể đọc trực tiếp từ các voice fields, nhưng không gọi là backend API verification.
7. Nhiều tile trùng tên: chọn tile hiển thị, dùng active thumbnail aria-current, kiểm URL/full prompt rồi tải kích thước gốc. Không force click nhãn ẩn hoặc lấy first trùng tên mà không bằng chứng chọn.
8. Park riêng chênh account trước+133; debit lượt1050→1043=7 khớp. EP01 cap500 và reserve110 vẫn giữ, không cộng số dư tăng vào quyền chi.

Full native STOP; một requestT03 đã tiêu thụ quyền, không autoT04. Prefix là PLANNING_ONLY, không selected/release hoặc ref downstream trước quyết định và gate tương ứng.
