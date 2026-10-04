# 174 — Chủ dự án tạm chấp nhận cả ba mẫu K20 của bộ 173

Ngày ghi nhận: 2026-10-04. Phản hồi trực tiếp của owner: “ca 3 đều tạm chấp nhận được rồi đấy”. Đối tượng: R01/R02/R03 của bộ 173 vừa trình nghe, không phải bộ 172 sai đầu vào.

**Tiếp nối — [175](175_k20-d06-dialogue-integration.md):** owner trả lời “ok” để duyệt lượt cụm B x3 tối đa 21 credit. Đã thực hiện và bàn giao ba mẫu, chờ nghe duyệt cặp thoại; ngân sách còn 4 credit. Đề xuất chưa duyệt dưới đây giữ làm lịch sử ở thời điểm ghi nhận 174, không phải trạng thái hiện hành.

## Quyết định đã ghi nhận

**OWNER_PROVISIONAL_VOICE_ACCEPTANCE — R01, R02, R03.** Cả ba được tạm chấp nhận về giọng trong phạm vi đối chứng một người nói, cùng câu audition. Không ép owner chọn winner khi cả ba đều dùng để đối chiếu. Giữ K20 Orus tùy chỉnh và D06 Aoede đã chọn; không tuyển lại hoặc sửa preset.

| Mẫu 173 | Media ID | Quyết định owner |
| --- | --- | --- |
| R01 | 5ad0bca5-a982-478a-841e-5a755233b9ee | Tạm chấp nhận |
| R02 | 47ae1f68-9979-4d2d-aadd-f01e3f0de77d | Tạm chấp nhận |
| R03 | 32ad9a2a-0b6c-4d11-9eaa-6a921056c04a | Tạm chấp nhận |

Không tự chuyển phản hồi thành “giống hệt K20”, điểm accent/diễn hoặc nghiệm thu phát âm từng chữ. Chỗ ASR rang/gian ở R02/R03 chưa có phán quyết riêng; không hỏi lại approval chung, nhưng vẫn phải kiểm lời trước dùng production. Root không nhận công đã nghe độc lập; bằng chứng cảm nhận là phản hồi owner.

## Ý nghĩa với RCA

Bộ 173 có ảnh và token nguồn được kiểm trước khi chạy; cả ba đầu ra được owner tạm chấp nhận. Điều này đủ giữ K20 làm mẫu đối chứng cho bước tích hợp tiếp, không đủ kết luận lỗi 170 do thiếu token, mất ảnh, chỉ dẫn diễn hoặc hai người nói. Bộ 172 vẫn INVALID_CONTROL; không quy lỗi thao tác của bộ 172 ngược sang bộ 170.

Chuyển tình trạng nghe bộ 173 từ chờ duyệt sang tạm chấp nhận; RCA 171 về cơ chế giọng lệch vẫn mở. Chưa nghiệm thu EP01, chưa duyệt hình, chuyển động, đồng bộ môi, cặp thoại hoặc bản cuối. Câu thử giọng không được ghép thay lời kịch bản 32.

## Bước tiếp đề xuất — chưa chạy, chưa duyệt request

Ưu tiên thử lại **cụm B: ký ức và đối đáp**, dùng lời thật ở kịch bản 32, K20 và D06 với token nguồn trực tiếp. Đây là kiểm thử ứng dụng vào sản xuất, không phải thử nhân quả đơn biến vì vừa đổi lời vừa thêm giọng thứ hai.

- Đào: “Nem thì đây. Chảo ở đâu?”
- Khoai: “Bếp nhà anh, hồi bé. Mẹ rang gạo, anh đứng chờ.”
- Đào: “Chờ ăn?”
- Khoai: “Chờ mẹ quay lưng.”

Giữ OPEN7 diagnostic-only, Omni 1.1 Flash / Thành phần / 360p / 9:16 / 10 giây / x3; ảnh + hai giọng, token đúng từng ID, đối chiếu screenshot sau thao tác nguồn. Không đổi âm sắc K20 bằng lớp chỉ dẫn mới; chuyển ý diễn phù hợp lời thật phải ghi rõ trong prompt request tiếp theo. Kiểm đúng người nói, không chồng lời, giữ chất giọng, nhịp đời thường và đủ câu. Chưa dùng hình bộ thoại để lấp coverage chưa đạt.

Báo giá ở lượt trước là 21 credit; nếu owner duyệt và giao diện vẫn báo 21 thì lấy từ 25 credit còn lại, còn 4. Không chi trong lượt ghi nhận phản hồi này. Cụm B đạt vẫn chưa hoàn thành cụm A hai câu đầu hoặc bộ cảnh hình; không hứa 25 credit đủ hoàn thành EP01. Không tự mở khoản thêm 90 credit, nâng Quality hoặc hạ tiêu chuẩn.

## Tổng kết vòng

- Đã xác định: owner nghe và tạm chấp nhận cả ba mẫu 173.
- Đã chốt: giữ K20/D06; không cần chọn một winner audition; phạm vi acceptance chỉ bộ đối chứng.
- Giả định làm việc: dùng cấu hình nguồn và hướng diễn K20 của bộ 173 làm mẫu đối chứng chuyển sang lời thật; chưa bảo đảm cặp thoại giữ được chất giọng.
- Còn mở: tích hợp K20–D06 với lời thật, phát âm và diễn chi tiết, nguyên nhân lỗi 170, bộ cảnh và bản cuối.
- Tiếp: trình yêu cầu chạy cụm B x3, tối đa 21 credit từ 25 credit còn lại; chờ owner duyệt trước khi tạo. Lượt này không chi credit mới.

Ngân sách theo lần đối soát 173: chi lũy kế 109/134 credit, còn 25 credit được phép chi; số dư tài khoản 275 credit là ảnh chụp trạng thái lượt 173, không kiểm trực tiếp lại trong lượt ghi quyết định này. Tài liệu và quyết định được lưu, commit/push theo chỉ dẫn dự án hiện hành.
