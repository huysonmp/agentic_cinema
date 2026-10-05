# EP01 — Sửa chất liệu nem bằng ảnh thật đã duyệt

Ngày 2026-10-05. Owner yêu cầu tiếp tục; làm bước local sửa nguồn món, không chi Flow. Dùng skill imagegen tích hợp, giữ bản gốc và lưu asset dự án/folder owner. Không API/key, cài đặt hoặc reviewer độc lập mới.

## 1. Hiệu chỉnh nhận định từ 187

Đã xem lại actual hai ảnh `nembui.jpg` và `z7750931050074_6fa76793489e54e476846aad4d233684_806643377.jpg` được owner cho dùng. Ảnh thật cũng có miếng/dải không đều, một số khá rộng. Vì vậy **“sợi to là sai nem” không phải tiêu chí hợp lệ**. 187 chỉ xác định nguồn cận tay lệch với bàn ăn 78; không dùng tạo hình AI ở 78 để phủ nhận chi tiết có trong ảnh món thật.

Phân vai nguồn: ảnh thật hỗ trợ chất liệu/cấu trúc món; 78 kiểm bố trí bàn và continuity lượng/đĩa; ảnh động tác cũ chỉ hỗ trợ grip/pose. Không nhập giỏ, lá lót, ớt trang trí hoặc món khác từ nền ảnh thật vào bàn đã duyệt. Đây là đối soát thị giác, không thêm claim về công thức, xuất xứ hoặc cách ăn từ ảnh.

## 2. Hai khung ứng viên mới đã tạo

- [START](../../assets/references/188/START_pickup_food_v0.1.png): sửa riêng phần nem từ START gắp 187, có miếng thịt/bì không đều và lớp thính rõ hơn; đầu đũa vẫn ở vị trí tiếp xúc, bát trống.
- [END](../../assets/references/188/END_pickup_food_v0.1.png): chỉnh từ START mới, frame H185 chỉ hướng dẫn pose tay. Một phần nem nhỏ được giữ trên bát Khoai, chưa đặt xuống bát và không tiến tới miệng.
- Root đã xem actual hai đầu ra: không thấy hơi; rau/chấm/bát/tay nghỉ vẫn trong bối cảnh cũ; không thấy nhập món/đạo cụ từ nền ảnh thật. Vẫn chưa kiểm bảo toàn phần nem, chiều dài đũa hoặc giải phẫu qua chuyển động.
- Đây là **FOOD_CORRECTION_CANDIDATE**, chưa owner texture approval hoặc FOOD/continuity PASS. Lượng nem, tỷ lệ đĩa so với wide shot 78 và đồng bộ toàn bàn còn phải kiểm; đĩa cận tay bị crop nên không chứng nhận từ hai ảnh rằng toàn lượng đã khớp.

Folder owner: `C:/Users/PC/Downloads/du_an_nem_bui/188_food_source_correction`. PNG đều 941×1672 RGB, đọc/giải mã ảnh thành công; bản workspace và owner khớp SHA256. [Preflight/provenance](evidence/188/food-source-preflight.json) và [prompt START](evidence/188/prompt-pickup-food-v0.1.txt), [prompt END](evidence/188/prompt-pickup-food-end-v0.1.txt) lưu đúng nơi. Dùng công cụ tích hợp, không khẳng định giá của công cụ ảnh.

## 3. Hệ quả đối với nguồn nâng/chuyển–nhận

END mới là ảnh sinh lại, **không còn trùng frame native H185**. Không dùng sự gần nhau của pose làm bằng chứng nối pixel hoặc gắn clip V02 vào bản ráp như đã sạch FOOD. V02 giữ tham khảo động tác; nếu sử dụng trong tương lai phải kiểm source compatibility thật.

Chưa sửa khung đổi hướng 187 hoặc đặt nem 186 sang chất liệu mới; chúng vẫn là nguồn làm việc cũ, không ghép lẫn rồi gọi đồng bộ. Bảng 187 giữ nguyên để truy vết. Chưa tạo video hoặc tăng coverage đạt; bản 30 giây 182 không đổi, C-v0.6/K20/D06 giữ nguyên, SIA vẫn hoãn/HOLD.

## 4. Gate và bước tiếp theo

1. Owner xem/chốt **chất liệu món** ở hai ảnh này, không phải duyệt cả bố cục/diễn/video. Nếu chưa đúng, sửa food trước, không dùng credit thử chuyển động để chữa source.
2. Dùng chất liệu được chọn để thống nhất lượng/đĩa/phần nem ở chuỗi gắp → nâng–khựng → đổi hướng → đặt vào bát. Tiếp tục giữ nhịp Đào rời cốc/quay lại/đỡ bát là thiếu thật, không ảnh thay video.
3. Sau khi khung và continuity đủ rõ, đọc quote live và xin quyền chi trước batch x3. Sổ còn 23, quote cũ 30; chưa ngân sách mới hoặc Quality/master/publish. Riêng một batch nếu vẫn 30 thiếu ít nhất 7, không cam kết đó đủ hoàn thành video.
4. Trước bàn giao vẫn bắt buộc các gate hình/món/diễn/dựng/nhãn AI và SIA trên audio thật/bản ráp. Không đổi voice hoặc coi việc owner hoãn kiểm là PASS.

## Tổng kết vòng

- **Đã xác định:** ảnh thật có cấu trúc không đều; đã tạo/lưu hai khung sửa chất liệu món từ nguồn owner duyệt.
- **Quyết định giữ nguyên:** nội dung, giọng, ranh giới claim, đặt nem vào bát; không chi Flow hoặc tăng coverage.
- **Giả định:** sửa food từ ảnh thật có thể tăng độ nhận diện; chưa kết luận owner thấy đạt hoặc motion sẽ ổn.
- **Còn mở:** duyệt chất liệu mới, lượng/tỷ lệ đĩa và đồng bộ các khung; diễn động, điểm nối, speaker QC và ngân sách.
- **Bước tiếp theo:** owner xem chất liệu cặp ảnh mới, rồi đồng bộ các khung trước thử Lite.
