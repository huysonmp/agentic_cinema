# REC245 — C02 sửa có mục tiêu và bản cắt chờ duyệt

Ngày 07/10/2026. Owner yêu cầu “tiếp tục đi”. Thực hiện theo quyền sản xuất tự vận hành tại REC238; giữ checkpoint C02 trước khi mở C01A.

## Điều đã xác định và thực hiện

Tiếng T01 được owner chấp nhận tại REC244, nhưng ba lỗi hình của T01 vẫn cần sửa: bối cảnh bị thay, camera quá rộng và Đào chắp tay ở đầu đoạn. Root đã đọc toàn bộ review ảnh cận vừa và review request T02. Ảnh mới là coverage riêng C02 theo kế hoạch 236, không thay thiết kế nhân vật hoặc master v5 đã duyệt.

Một lượt C02 T02 đã gửi: Omni 1.1 Flash, Ingredients, 720p, 9:16, 10 giây, x1, Agent OFF, giá thực 15 credit. Chỉ gắn ảnh cận vừa UUID `4e9d7a4c-bf16-4aec-8212-d6e2990425e9` và K20 ID `b447b35c-b35e-4140-af72-ecd277282b1a`. Prompt được lưu và đối chiếu nguyên văn trước gửi. Không có giọng Đào, master rộng thứ hai hoặc thoại mới.

Native đã tải được qua UI, giữ nguyên và đối soát hash giữa bản tải, repo và folder owner. File có 720×1280, 24 fps, 240 khung, hình 10 giây và tiếng 10,005 giây; giải mã toàn file thành công. Root xem overview 1 fps, cả bốn bảng 6 fps và khung cuối vùng cần kiểm. Reviewer độc lập xem 66 khung mẫu cùng ảnh tham chiếu. Không coi kiểm mẫu là xem/nghe liên tục toàn video.

Trong phạm vi khung đã xem, ba lỗi lớn T01 không lặp lại. Hai mặt rõ, giữ phố mở và mái bạt, bốn tay nghỉ riêng, nem không khói. Phát hiện mới: Đào bắt đầu hé môi ở khoảng 7,583 giây. Không suy từ một hình miệng mở rằng cô đang nói hoặc bị gán giọng Khoai.

## Xử lý bằng dựng, không sinh thêm

ASR offline không được mồi bằng kịch bản ghi lời ở khoảng 0,96–6,94 giây; bộ đo im lặng ghi đuôi từ khoảng 6,969 giây. Chữ “rang” bị ASR nhận thành “găng”, độ tin cậy thấp: chỉ đánh dấu nghe lại, không tự sửa lời hoặc kết luận tiếng sai.

Đã tạo scene riêng trên Flow: **EP01_C02_T02 — BẢN CẮT CHỜ DUYỆT**. Picker nguồn được tải đối chiếu hash đúng native T02, đặt range UI 0–7,5 giây và khung 9:16 rồi xuất. Giữ scene T01, không ghi đè native, không thêm lượt tạo video.

File xuất thật dài 7,541667 giây/181 khung; tiếng dài 7,509333 giây. Flow giữ thêm một khung ở biên so với khoảng nửa mở dự kiến. Khung cuối thật tại 7,5 giây vẫn khép môi; không chứa vùng Đào hé môi đã phát hiện. Root xem cả ba bảng 6 fps của export và khung cuối. So PCM với nguồn đúng đạt tương quan 0,999990: chứng minh giữ track, không chứng minh giọng hoặc khẩu hình đạt.

## Quyết định và ranh giới

- Đã chốt từ trước: creative, nguyên văn hai câu, K20 và hướng cận vừa; không tuyển lại voice.
- Đã làm: một T02, tải native, kiểm mẫu, cắt–xuất trực tiếp Flow và gửi đúng bản xuất cho owner xem/nghe.
- Giả định đang kiểm: nguồn cận vừa giúp video giữ camera và nền tốt hơn; T02 hỗ trợ giả thuyết này trong một trường hợp, không phải quy luật thành công.
- Còn mở: owner nghiệm thu hình–tiếng/khẩu hình của **T02 export**, điểm nối C01B/C03A và phân bổ thực của phim 30 giây. Approval tiếng T01 không chuyển sang T02.
- Không mở C01A hoặc tự chạy T03 trước checkpoint. Không dùng cận món để che người nói, tua lời, freeze hình hoặc ghép tiếng mới lên môi khép.

## Ngân sách và lưu trữ

Sau T02, tab tạo video hiển thị 1.020, so với 1.035 trước gửi: quan sát trừ 15. Tab mới sau trim/export lại hiển thị 1.050; đã lưu riêng bằng chứng khác biệt, chưa xác định nguyên nhân hoặc hoàn phí. Sổ dự án giữ bảo thủ tổng 30 trong trần 500, còn 470; không tăng quyền chi theo số dư khác. Khoản tạo lại còn 165/180; dự phòng 110 chưa giải ngân. Chưa dùng khác biệt này để kết luận phí trim/export hoặc giá công cụ nói chung.

Folder owner: `C:/Users/PC/Downloads/du_an_nem_bui/ep01_restart_720p_v1/`.

- Bản duyệt: `07_edits/C02_T02_FLOW_0_7p5S_FOR_APPROVAL.mp4`, hash `d151eb1d9f5f5b4486fed030579d9da3de0d23f434a65db2f6c4dca88b3228f3`.
- Native T02: `05_native/EP01_720_C02_T02_NATIVE.mp4`, hash `2f20ec53b20cf3dea2eb48ee0c3f76913ce8a4da45f05ebf24dc33587a9ed297`.
- Request và prompt: `04_requests/C02_request_245.json`, `C02_prompt_245.txt`.
- Kiểm native/export, registry và ASR: `06_qc/`; bằng chứng media chi tiết trong `C02_T02_245`, `C02_T02_245_ASR`, `C02_T02_FLOW_245`.
- Dấu vết cắt: `07_edits/C02_T02_FLOW_trim_export_245.json`; bài học: `09_lessons/REC245_shot_reference_and_measured_flow_trim.md`.

Skill computer-use hướng dẫn kiểm trực tiếp cấu hình, chip, quote và readback; tạo tab mới sau tab cũ lỗi. Không thêm API/công cụ trả phí. Khâu QC dùng bộ công cụ local đã có, không dựng bản bàn giao bằng local.

## Bước tiếp

Owner xem/nghe bản cắt C02 T02, chốt đúng tiếng K20, lời/nhịp và hình–tiếng. Nếu duyệt, ghi đúng file/hash và chuyển C01A để Đào nói, bắt đầu vươn tay; tiếp đó C01B cho Khoai ngắt và Đào thu tay. Giữ thứ tự phụ thuộc, kiểm nối thực trước mở chuỗi tiếp theo.
