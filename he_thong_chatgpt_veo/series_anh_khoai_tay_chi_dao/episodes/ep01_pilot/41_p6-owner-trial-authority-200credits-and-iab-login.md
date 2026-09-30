# EP01 — Quyền thử P6 200 credit và trình duyệt tích hợp

Ngày: 2026-09-30. Status: OWNER_TRIAL_AUTHORIZED / OWNER_LOGIN_REQUIRED / GENERATION_NOT_STARTED.

Evidence trực tiếp: owner nói “chưa cần chốt trần credit đâu, bạn sẽ được thử cho đến khi dùng hết 200 credit, hãy thao tác đi nào, mở trình duyệt của chatgpt ra tôi đăng nhập cho, lần sau cứ thế mà dùng”.

## Quyết định hiện hành

- Cho chạy thử mẫu nhân vật P6 trên Flow theo hướng/spec đã duyệt. Ngân sách tổng 200 credit cho đợt thử này, thay đề xuất40 ở [request40](40_p6-reference-intake-and-character-trial-request-v0.1.md); không phải 200 mỗi lượt hoặc tự gia hạn ở turn sau.
- Cho lặp thử/rework trong ngân sách thay giới hạn chỉ hai request/no retry của proposal40. Bắt đầu hai base từ text như request40, mỗi vòng phải kiểm output và ghi nguyên nhân sửa/prompt/version/chi phí trước chạy tiếp. Không tiêu hết chỉ để hết ngân sách nếu đã có mẫu đủ tốt để trình owner.
- Dùng trình duyệt tích hợp thay Chrome. Owner tự đăng nhập; tái dùng session khi còn hiệu lực, không hứa phiên tồn tại vĩnh viễn.
- Giữ model/tỷ lệ/count và phạm vi mẫu nhân vật của request40. Không suy quyền quay video toàn tập, sửa script/canon, upload ảnh chưa có quyền, bỏ xác nhận bảo vệ, mua credit/upgrade hoặc publish.
- Kiểm giá thực tế và cumulative spend; không gửi request khiến tổng vượt200. Nếu không xác định được giá/count/cost thì dừng ở preflight, không coi ngân sách là quyền chạy mù. Chưa có số dư/billing thực tế.

## Thao tác thực hiện

Đã mở flow.google.com trong in-app browser visible và bấm Create with Google Flow. Trang chuyển sang xác minh/đăng nhập Google; đã giữ tab handoff cho owner. Không thao tác thông tin xác thực, mật khẩu/OTP, không lưu credential/cookie/token, không nhập prompt/generate, chưa tiêu credit từ generation.

Kỹ năng computer-use yêu cầu dừng điều khiển auth dialog; owner hoàn tất trực tiếp trên tab. Sau owner báo đăng nhập xong, kiểm session/account phù hợp và giá/model, rồi tạo project pilot riêng và chạy theo scope trên. Approval asset cuối vẫn do owner, không tự PASS P6.
