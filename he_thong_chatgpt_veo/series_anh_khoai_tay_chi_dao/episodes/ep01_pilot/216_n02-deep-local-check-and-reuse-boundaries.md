# 216 — Kiểm sâu N02: phần mặt dùng được tới đâu?

Trạng thái: ROOT_LOCAL_VISUAL_DIAGNOSTIC / PARTIAL_REUSE_CANDIDATE / VOICE_LIPSYNC_ACTING_NOT_NEWLY_PASSED. Thực hiện sau owner chốt tier3 A/A/A/A; chỉ local, không chi, không sinh hoặc sửa nguồn.

## Nguồn và thực thi

Native: `C:/Users/PC/Downloads/du_an_nem_bui/200_n02_replacement/N02_NATIVE.mp4`.
SHA-256: `72cbaf7d9f66932002dfce1b1a57fa464935c315e84e54ae094fe29aa805a153`.

Chạy `scripts/check_ep01_n02_visible_coverage.py` với output mới `C:/Users/PC/Downloads/du_an_nem_bui/216_n02_face_coverage_check/`.

- Trích toàn bộ 240 frame, 360 × 640, 24 fps. Audio container/native dài 10,005 giây; 240 frame video tương ứng 10,000 giây. Không lấy chênh 0,005 giây làm lỗi lệch tiếng đã xác nhận.
- Root xem ba bảng gồm 36 ảnh theo anchor/cut và sáu ảnh native cặp liền trước/sau cut. Có ảnh trùng trong các bảng; không gọi là 42 ảnh khác nhau hoặc đã xem hết 240.
- Dùng scene-change threshold 0,25 như gợi ý, sau đó xác nhận cut bằng cặp frame native. Không dùng ngưỡng này làm nhận diện mặt tự động.
- SHA nguồn không đổi sau trích. Không cắt/ghép PCM, không ASR mới, không nghe liên tục hoặc review độc lập.

## Phân đoạn hình đã đối chiếu

| Range frame, out-exclusive | Thời gian nguồn | Hình thực tế | Đối chiếu R01/R02 |
|---|---|---|---|
| 0–72 | 0–3,000 giây | Hai người và bàn, Khoai có mặt | Có hình cho đầu N02, chưa chứng minh hợp nhịp nối từ N01/động tác kéo đĩa |
| 72–164 | 3,000–6,833333 giây | Cận vừa Khoai thấy mặt | Có hình cho phần ký ức, gồm vùng ASR “Hồi bé, mẹ ... gạo”. Chưa nghiệm thu sắc thái, hướng nhìn hoặc khẩu hình |
| 164–201 | 6,833333–8,375 giây | Cận món, không thấy mặt | Cắt vào phần cuối câu theo ASR; chưa đáp ứng bản R02 cận Khoai nguyên ý, cần xử lý hoặc trình thay đổi coverage có lý do |
| 201–240 | 8,375–10,000 giây | Hai người và bàn | Có thể là đuôi phản ứng; chưa coi toàn đuôi là im lặng hoặc cắt dùng khi chưa kiểm nghe/nhịp |

Cặp frame đã xem trực tiếp: 71/72, 163/164, 200/201. Khoai có mặt ở 163, món thay ở 164; món ở 200, hai mặt trở lại ở 201. Điểm cut không còn là ước lượng vùng từ contact sheet 215.

## Thoại và hình: chỉ là gợi ý thời gian, không nghe thay owner

ASR nguồn 201, không prompt mồi:

- 0–2,94: “Khoan, mùi này làm anh nhớ đến bếp nhà anh.”
- 3,92–7,34: “Hồi bé, mẹ gian gạo, anh đứng chờ.” Từ “gian” là ASR nhận nhầm so với lời duyệt “rang”; không sửa script hoặc kết luận nghe sai từ ASR.
- Gợi ý word timing: “anh” 6,60–6,76; “đứng” 6,76–6,94; “chờ” 6,94–7,34. Cut sang món ở 6,833333 có thể che một phần “đứng” và “chờ”; khoảng chồng tới speech end ASR khoảng 0,507 giây. Không gọi đây là phoneme alignment đã kiểm.

Nhận xét quan trọng: **không phải cả câu “Hồi bé, mẹ rang gạo...” không có mặt trong native này**. Nguồn native có phần mặt; bản 209 dùng audio của nó nhưng phủ hình khác không mặt, là vấn đề kế hoạch dựng. Nguồn audio giữ lịch sử owner đã duyệt đúng K20/nhịp; 216 không tự thêm kết luận nghe mới.

## Kết luận tái dùng và vấn đề còn mở

- Giữ native này trong ứng viên có giá trị; không làm mới cả N02 chỉ vì bản bàn giao 210 thất bại.
- Chưa được chọn đoạn 0–6,833333 làm final. Cần kiểm mặt/miệng theo từng câu, khớp N01→N02→N03, tạo hình/bàn/món và direction nhìn Đào thay vì chỉ nói về camera.
- Không nối frame đứng/lặp/đổi tốc độ để lấp từ “chờ”. Không dùng cận món đuôi làm cách che lỗi mà không review ý nghĩa và approval coverage.
- Không cắt audio đúng chữ để bỏ vùng hình thiếu. Nếu cần ảnh người nghe hoặc cảnh nối mới, đó là đề xuất biên tập có lý do, cần kiểm giọng/miệng/continuity theo bản ghép mới và trình khi đổi storyboard.
- Nguồn chỉ 360p; có thể dùng để kiểm diễn/coverage, không suy upscale thành chất lượng master đã đạt.
- Có thay đổi bố cục và trang trí món trong các đoạn cận, cần FOOD/CONT đối chiếu nguồn bàn đã duyệt; chưa chốt bằng nhận xét chất lượng chung.

## Bước tiếp theo, chưa thực hiện

Khi tier4 được chốt: giao maker/reviewer theo phạm vi, dùng bảng frame/word hint để lập đề xuất source range và phần thiếu, kèm bản dựng thử có nhãn chưa kiểm AV. Nếu thiếu công cụ nghe/xem, trạng thái scope giữ HOLD; không tạo thêm chỉ để lấp UNKNOWN. Phép thử trả phí, nếu cần, có brief/quote/số output/criteria và owner approval riêng.
