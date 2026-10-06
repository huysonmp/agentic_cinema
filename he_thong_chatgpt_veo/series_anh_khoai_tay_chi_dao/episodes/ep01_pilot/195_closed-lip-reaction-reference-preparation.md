# EP01 — Chuẩn bị khung phản ứng môi khép

**Cập nhật approval tại [196](196_closed-lip-reference-approval-and-motion-test-gate.md):** owner “ok r nhé” đã duyệt hai ảnh thực tế về môi, ánh nhìn và góc đầu. Các nhãn/report chờ duyệt dưới đây là hồ sơ thời điểm chuẩn bị; ảnh/hash giữ nguyên. Chưa duyệt hoặc chạy video, chưa cấp thêm credit.

Ngày 2026-10-06. Owner “ok nhé” cho đề xuất sau 194: chuẩn bị cặp khung mới môi khép rõ, cười bằng mắt, giữ bối cảnh và tay/cốc để owner xem trước. **Chỉ duyệt chuẩn bị ảnh, không duyệt tạo video có phí hoặc thêm credit.**

## Phương pháp đã khóa

Dùng imagegen tích hợp (không CLI/API key), edit từ START185 v0.2, giữ gương mặt/nhân vật trưởng thành, áo/nơ/lá, bàn/cốc, hai tay, mép áo Khoai ở trái, camera và ánh sáng. START chỉ sửa trạng thái môi/cười; END lấy chính START mới làm target và chỉ đổi gaze/góc đầu cần thiết sang Khoai. END185 chỉ hướng dẫn gaze, không nguồn bối cảnh khác.

Giữ nguyên nguồn và tạo sibling195. Phải xem actual từng ảnh trước chọn; không chứng nhận invariant pixel hoặc dynamic consistency từ lời prompt. Cặp ảnh không là phản ứng động đã đạt hoặc bằng chứng chữa lỗi môi. Nếu có drift rõ, sửa một nhóm và kiểm lại trước gửi owner.

Ngân sách Flow theo194:322/322, còn0 quyền chi. Lượt này không mở/chạy Flow, không đọc giá hoặc account live, không Quality/master. C-v0.6/K20/D06/P02 approval nhịp/SIA HOLD giữ nguyên.

## Đầu ra đã lưu — chờ owner duyệt ảnh

Đã tạo hai ảnh bằng hai lần chỉnh ảnh tích hợp, không gọi Flow. START lấy START 185 làm nguồn chỉnh môi. Sau khi root xem START, END lấy chính START mới làm nguồn chính; END 185 chỉ hướng dẫn ánh nhìn. Không chỉnh sửa nội dung ảnh bằng mã sau khi tạo.

| Khung | File trong kho dự án | SHA-256 |
| --- | --- | --- |
| START | `assets/references/195/START_Dao_closed_lip_v0.1.png` | `c7e84f873fd19e7919d0f2d5d8c4877c345dde6a402f91330ea48e4ff894fcf3` |
| END | `assets/references/195/END_Dao_closed_lip_v0.1.png` | `0e6a2f348ecd1cde923fa668d7b2163ad8b584f3be1e3a8cb7a91fa04b33e4de` |

Cả hai là PNG RGB **937 × 1678**, khung dọc gần 9:16, không phải tỷ lệ 9:16 chính xác. Chưa cắt hoặc đổi kích thước file nguồn. Đường dẫn ảnh gốc do công cụ tạo, hash nguồn 185 và file đích được ghi trong [preflight](evidence/195/closed-lip-input-preflight.json). Prompt đầy đủ: [START](evidence/195/prompt-START.txt), [END](evidence/195/prompt-END.txt).

Root đã xem từng file đầu ra và bảng đối chiếu:

- Hai ảnh có đường môi khép, không thấy răng hoặc khoang miệng mở. END vẫn có khóe môi hơi nhấc; không tuyên bố biểu cảm chỉ thay đổi ở mắt hoặc môi giống nhau từng pixel.
- START nhìn xuống cốc phía phải; END nhìn sang trái, về phía mép áo Khoai. Góc đầu thay đổi nhẹ cùng ánh nhìn.
- Hai tay, cốc và mực nước vẫn ở vị trí tương ứng qua quan sát; áo, nơ, lá, bàn, bối cảnh và ánh sáng giữ được hình thức chung. Đây là quan sát hình ảnh, không chứng nhận mọi pixel/chi tiết bất biến.
- Không thấy chữ, hơi nóng hoặc động tác nhấc cốc trong ảnh. Ảnh tĩnh không cho biết đường chuyển động, diễn miệng, nhịp quay hay tính liên tục của video.

**Trạng thái: STILL_CANDIDATES_AWAIT_OWNER_REVIEW.** Không có review độc lập; không gán kết quả này thành PASS của agent, diễn xuất hoặc chuyển động Veo. Giả thuyết môi khép rõ hơn giúp giảm diễn miệng vẫn chưa kiểm chứng.

## Bảng xem và kiểm công cụ

[Bảng START/END](evidence/195/195_START_END_STILL_CANDIDATES_v0.1.png) có nhãn ứng viên/chờ duyệt, giữ toàn khung nguồn, kích thước **1080 × 1130**. SHA-256 `0966e9c1c62cf410729ca704981dd1fc207b368e7b7f1db3103969336771223a`. [Báo cáo](evidence/195/board-report.json) ghi kích thước/hash thực tế.

Mở rộng script `scripts/render_ep01_bridge_reference_board.py` bằng chế độ hai ô tùy chọn, không thay mặc định sáu ô. Đã kiểm biên dịch Python; render lại bảng 187 cho hash `0cecd73cecef9b6f026fe4324fb1384d1968fb77c79d711c6c081ef009d475c4`, khớp bản trước. Thử render vào thư mục đã có đầu ra bị từ chối, hash bảng 195 không đổi. Chỉ là kiểm công cụ trình bày, không nâng cổng chất lượng nội dung.

## Gói cho owner và ranh giới bước sau

Đã lưu hai PNG gốc, bảng xem và tài liệu/prompt/báo cáo tại `C:/Users/PC/Downloads/du_an_nem_bui/195_closed_lip_references/`. Bản gốc của công cụ và nguồn 185 giữ nguyên.

Lượt này chi **0 credit Flow**; chi phí/quota của công cụ tạo ảnh tích hợp không được đối soát, không suy thành “mọi tạo ảnh miễn phí”. Sổ video giữ **322/322, còn 0**. Không kiểm số dư tài khoản trực tiếp trong lượt này, không lấy snapshot 154 ở vòng 194 làm quyền chi mới. `ready_for_paid_submission=false`.

Owner cần xem và duyệt **môi, hướng nhìn và góc đầu của cặp ảnh thực tế**. Sau đó mới đề xuất phép thử chuyển động x3 Lite với giá/cấu hình kiểm trực tiếp và quyền chi riêng. Duyệt ảnh không đồng nghĩa duyệt video, cấp ngân sách, nghiệm thu chuyển động hoặc đóng nguyên nhân lỗi môi.

## Tổng hợp vòng 195

- **Đã xác định:** có hai ảnh ứng viên môi khép và ánh nhìn đúng hướng để owner xem.
- **Đã chốt:** chỉ chuẩn bị ảnh; C-v0.6/K20/D06 và duyệt nhịp P02 0–2,5 giây giữ nguyên, SIA HOLD.
- **Giả định:** lấy START mới làm nguồn END giúp hạn chế tái tạo lệch; chưa chứng minh bằng thử nghiệm đối chứng.
- **Còn mở:** owner duyệt ảnh thực tế, diễn chuyển động và nguồn gây lỗi môi trong Veo.
- **Bước tiếp theo:** owner xem cặp ảnh; chưa gửi video có phí, chưa Quality/master/phát hành.
