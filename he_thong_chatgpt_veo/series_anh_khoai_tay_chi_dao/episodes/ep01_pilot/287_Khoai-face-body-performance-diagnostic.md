# REC287 — Khoai chưa đạt diễn mặt–thân người

Ngày 13-10-2026. **OWNER_PERFORMANCE_CONCERN / DIAGNOSTIC_ONLY / NO_NEW_GENERATION.**

## Owner khoanh vấn đề

Owner: “chuyển động của khoai chưa ok đâu”. Khi hỏi tay/đũa, mặt–thân hay cả hai, owner chọn **“Diễn mặt–thân người”**. Không tự diễn giải thành yêu cầu làm lại tay, giọng hoặc chạy thêm video.

Bản REC286 vẫn NOT_SELECTED vì lỗi yếm/hậu cảnh. Mở thêm **PERFORMANCE_REWORK** cho cảm giác diễn mặt–thân của Khoai; không dùng scope “có giữ A/cốc/bát” trong review286 làm motion/acting PASS. Approval nguồn trước vẫn giữ lịch sử/phạm vi, không phủ nhận phản hồi mới của owner.

## Đối chiếu đã làm

Target286 SHA `4703fb9b34abbb63144364cb388aa4d9921e06d7b7c597f2da77d04a7299e583`; source276 SHA `42d826e1356ce67acc6e1057b4ceefc9703f3e705ffa14ae6c09dea7934b5bdf`. Đã đọc promptC06T03/275 và EDL276: Khoai chữa cháy hơi ngượng nhưng giữ bình tĩnh, không cười mời/ăn mừng; nói rồi chuyển A còn kẹp về phía bát Đào, chưa thả. Đây chưa phải cảnh nhận–bỏ tiếp theo.

Root đối chiếu các board liên tiếp phần cuối F64–F122 và khung full-resolution cùng chỉ số F95/F122 giữa source/output; output124F đã xem đầy đủ ở286. Không giả lập đây là đã xem/nghe AV liên tục. Reviewer độc lập đã ghi report `06_qc/Khoai_motion_independent_diagnostic_287.md`; root đọc đầy đủ. Turn reviewer lỗi capacity ở khâu closeout nhưng artifact đầy đủ đã tồn tại/được đọc; không dùng status turn làm bằng chứng chất lượng. Maker chỉ gửi được một số quan sát đối chiếu rồi lỗi capacity, không có report hoàn tất; không ghi maker run287 completed/PASS.

FFmpeg có sẵn tạo thêm **dẫn xuất QA**, không sửa native:

- Folder owner: `C:/Users/PC/Downloads/du_an_nem_bui/287_KHOAI_MOTION_QC/`.
- `source_full16_01.png`…`08.png`: toàn123 khung nguồn, trang cuối11 khung thật +5 ô đen padding, thứ tự đọc trái→phải/trên→dưới.
- `SOURCE_LEFT_EDIT286_RIGHT_SILENT_COMPARE_QC_NOT_FINAL.mp4`: **trái source, phải286**, scale360×640 mỗi bên, ghép cạnh nhau720×640, 24fps/123F/5,125s, **không tiếng**, SHA `8f8fb12736578f9a26cdc09e37bf8131531b05a9aa7a0f52f1e42f275a017d17`.
- So sánh cùng mốc đầu container, **chưa căn theo động tác/phoneme**; bản so sánh dừng theo nguồn ngắn hơn nên không chứa khung cuối thứ124 của286. Không là film/output native720p dọc hoặc bằng chứng sync. Âm thanh chỉ bỏ trên dẫn xuất QA để xem hình; original audio/native không bị mute/revoice hoặc thay đổi.

## Phát hiện và giới hạn

1. **Không phải mọi vấn đề diễn đều mới do sửa món.** Chuỗi nhắm/chớp mắt, miệng mở rộng/lộ răng ở khoảngF78–83, đóng môi quanhF95–96 rồi mở lại và chuyển sang nụ cười nhẹ quanhF100–104 đã có trong nguồn. Output gần các pose đó tại cùng chỉ số khung. Đây là quan sát tương đồng, không chứng minh khớp pixel hoặc timing từng âm.
2. **Đầu/vai/ngực phần lớn giữ tư thế trong lượt đáp**, trong khi biến đổi đọc rõ nhất nằm ở mắt/lông mày/miệng; chuyển động cẳng tay đưa đũa nằm ở đuôi. Đánh giá “cứng/tách rời/cười giải thích thay vì chữa cháy kín” là diễn giải nghệ thuật cần xem chuỗi/owner, không kết luận chỉ từ một khung miệng mở.
3. **Không đồng nhất khẩu hình với cảm xúc.** Lộ răng hoặc chớp mắt có thể là động tác tự nhiên khi nói; prompt275 đã cho articulation tự nhiên. Không chữa bằng cấm răng, đóng miệng hoặc đứng bất động hơn. Chưa nghe/sync nên không tự kết luận môi sai âm hay giọng đổi.
4. **Hệ quả cho kế hoạch sửa:** nếu vấn đề cảm nhận nằm trong nhịp diễn đã có ở nguồn, phương án chỉ sửa món/giữ nguyên nguồn sẽ giữ nhịp đó. Cần tách sửa món khỏi nâng diễn và đối chiếu trước quyết định. REC276 từng duyệt riêng cả diễn hơi ngượng/lip-sync/nhịp trên prefix57, REC277 duyệt bản nối; owner hiện bác diễn của REC286, **chưa bác đích danh source276**. Tương đồng pose không chứng minh cảm giác diễn hai bản giống nhau; chưa tự thu hồi approval nguồn hoặc chốt phải tạo lại nguồn.

## Rà tầng gốc

Prompt gốc đã nêu đúng ý định “hơi ngượng, giữ bình tĩnh”, nhưng yêu cầu chữ không chứng minh diễn cảm nhận được. Việc giữ nhiều props/pose và không tách cổng chấm diễn tự nhiên là những điểm cần rà; chưa đủ bằng chứng quy một keyword, bộ phận cơ thể hoặc model là nguyên nhân duy nhất. Food-only edit không phải một yêu cầu sáng tạo diễn mới, nên không dùng nó để sửa đồng thời diễn mà vẫn gọi bảo toàn source.

Khoảng trống review cần đóng: phạm vi286 mới chứng minh A/props còn và thứ tự hoạt động miệng khái quát, chưa nghiệm thu quan hệ **ý định–mắt–đầu–thân–lời** hoặc độ tự nhiên khi phát liên tục. Cảm giác chưa đạt do owner báo là checkpoint thực, không được bác bằng báo cáo technical xanh.

## Đề xuất nghệ thuật — chưa chốt, chưa gửi generation

Khuyến nghị giữ chất Khoai **chữa cháy tỉnh, hơi ngượng, không hồ hởi mời ăn**. Brief cần một chuyển biến nhỏ có ý nghĩa: nhận ra bị bắt → cố giữ bình tĩnh trả lời → bắt đầu chuyển đũa như lời chữa cháy. Mắt, đầu và thân phản ứng cùng ý định; không chỉ hoạt hình miệng/lông mày trên một thân giữ pose. Các cue cụ thể và nhịp phải chốt/xem trong bối cảnh tiếng thật, không tự thêm một loạt chuyển động hoặc đổi lời để “sống động”.

Trước trả phí: chốt mức diễn owner muốn và chọn sửa cảnh nào/phạm vi nào; đánh giá khả năng giữ giọng, hình món, props và continuity cùng ngân sách. Nếu phải đổi source/ảnh/prompt/công cụ/script hoặc chi mới, trình riêng. Không tự sinh lại dưới cap20 đã dùng.

**Đã xác định:** owner ưu tiên mặt–thân, có mẫu diễn tương tự trong source, take286 vẫn không chọn. **Giả định cần kiểm:** thiếu liên kết diễn của cả cơ thể/nhịp câu làm cảm giác chưa tự nhiên; cần xem chuỗi đúng lời, không suy từ ảnh đơn. **Còn mở:** chất diễn nguồn khi so với286, brief diễn cuối, mức source cần thay, cơ chế sửa/giữ tiếng và tính khả thi chi phí. **Bước tiếp:** đối chiếu cảm nhận nguồn và chốt brief diễn Khoai trước quyết định giữ nguyên hay tạo lại nguồn; chưa xem sửa món cục bộ là giải pháp đủ cho cả vấn đề.

Chi mới0; sổ237/500 còn263, tạo lại26 và dự phòng110 đóng. Không browser, paid, voice/tool install, EDL update hoặc release trong vòng này.
