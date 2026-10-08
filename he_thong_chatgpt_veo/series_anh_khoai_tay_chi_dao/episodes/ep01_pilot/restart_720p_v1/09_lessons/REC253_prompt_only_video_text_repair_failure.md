# REC253 — Không suy edit thành công từ việc Flow nhận prompt

Quan sát: một video-to-video 720p/x1/20 credit trên T02, nhiệm vụ hẹp chỉ xoá chữ khỏi áo, vẫn giữ chữ đúng F23–57. Native, 96 PNG, 12 board source/output và audio correspondence đã lưu tại `C:/Users/PC/Downloads/du_an_nem_bui/253_BM_TEXT_REPAIR/`.

Điều đã chứng minh: source/draft đúng, UI báo giá và backend trả output; nhiệm vụ xoá chữ **không đạt trong lượt này**. Điều chưa chứng minh: edit luôn thất bại, một cụm prompt là nguyên nhân gốc, tiếng hoàn toàn bất biến, hoặc công cụ inpainting khác chắc đạt. Không viết thành tỷ lệ thành công/thất bại chung từ một lượt.

Quy tắc sử dụng lần sau: phân biệt feature support, UI acceptance, output existence và task success. Prompt yêu cầu giữ audio/mouth không là API invariant. Kiểm native theo từng frame của vùng cần sửa; decoded PCM khác hash không tự đồng nghĩa đổi voice, số tương quan cao không thay nghe thực. Giữ originals, provenance và failure thay vì overwrite.

Nếu agent báo hết lượt dùng, kiểm file được giao trước khi kết luận không có output: REC253 agent đã lưu report preflight trước lỗi final, root chỉ phát hiện và đọc tại closeout sau submit. Không backdate thời điểm đọc. Review giấy cũ chỉ tái sử dụng khi cùng hash/scope; root đóng authority/live delta không được gọi thành review độc lập mới. Output lỗi hiển nhiên vẫn phải chặn; thiếu review output độc lập không được biến thành PASS.

Không lặp paid cùng tuyến chỉ bằng thêm “no subtitles”. Hướng khác phải chứng minh capability cụ thể và xin quyền theo giá/nguồn/đầu ra mới; không tự mở BR, reserve, phần mềm hoặc API. Chuẩn hình sạch owner chọn B vẫn giữ.
