# REC280 — C07 T03: kiểm bản gốc và dừng vì hành động sai

Ngày 13-10-2026. **SOURCE_REWORK / STOP / C07 NOT_SELECTED / C08 HOLD.** Root đã kiểm đủ 144 khung hình; chưa nghe hoặc xem AV liên tục. Hai nhiệm vụ maker và phản biện độc lập đã được giao nhưng đều thất bại vì giới hạn sử dụng, không có báo cáo hoàn tất. Không lấy kiểm của root thay tên hai agent hoặc đóng gate độc lập.

## Target và bằng chứng

Owner duyệt đúng một lượt theo REC279: prompt SHA `5f3f00fde211ba58118927c9cd3b6e5229938293b913c02b91766ee32a0cd9d3`, hai ảnh tham chiếu, một D06, Ingredients / Omni 1.1 Flash / 720p / 9:16 / 6 giây / x1 / âm thanh bật / Agent tắt. Đã kiểm lại toàn prompt, hai image ID và cấu hình trên UI trước gửi. Không sửa lời, preset hoặc prompt.

Flow output ID `3ab99a03-bc7c-4a82-8ff6-d4f2424c314c`, tên card `Food characters talking at table`. Lịch sử output có đúng hai image ID: pair `ded2a157-f2d7-4be7-9185-31d5fc87f3ea`, scene `9d2280e2-bb03-437a-98f2-553a7d481144`; một voice chip. Locator toàn prompt cuối khớp đúng một nội dung lịch sử. Không tự nhận đã kiểm hash byte server hoặc giọng đã sinh từ các chip này.

Tải bằng lựa chọn UI **720p Kích thước gốc**, nhận sự kiện download thành công. Bản tải, bản owner và bản repo cùng SHA `ae876978fb19265601e4082c5e4cb7079c481786b11a2f8309be362b0881a50e`, 1.254.806 byte. Native `05_native/EP01_720_C07_T03_NATIVE.mp4`; owner copy `C:/Users/PC/Downloads/du_an_nem_bui/280_C07_T03/EP01_720_C07_T03_NATIVE.mp4`.

Đã chạy hai script có sẵn: `scripts/inspect_ep01_native_243.py` và `scripts/board_ep01_c04_action_261.py`, không sửa/cài công cụ. H.264 720×1280, 24 fps, 144 khung / 6 giây hình, container 6,016 giây, AAC 48 kHz stereo; giải mã toàn file thành công. Trích đủ 144 PNG và 18 bảng, mỗi bảng tám khung với toàn cảnh, crop mặt và bàn. Crop chỉ là bằng chứng kiểm, không chỉnh video.

Root trực tiếp xem **toàn bộ 18 bảng F0–143**, thêm PNG nguyên khung F0, F24, F80, F143 và exact scene C06 F56. Scene SHA `69fb0e62a3a6f138a0eae622603945b248ec8d2809c8cda513dcdfdc33d00863`. Evidence tại folder owner `native_qc/`; phạm vi **ALL_FRAME_STILLS_NOT_AV**. Không lấy ảnh/metadata làm bằng chứng D06, đúng người nói, trọn N07, giọng vùng miền hoặc lip-sync. Không chạy ASR vì hình đã có blocker đủ để bác nguồn; chưa cần yêu cầu owner nghe duyệt một candidate hình sai.

## Findings — khung tính từ 0, giây = F/24

| Mục | Expected → observed | Mức độ / bằng chứng |
| --- | --- | --- |
| Nhận diện | Đào là quả đào có cuống/lá, Khoai là củ khoai tây. T03 giữ được dạng nhân vật thực phẩm suốt nguồn; không hóa người thật như T02. | Quan sát F0–143; chỉ kết quả của take này, chưa chứng minh ảnh pair là nguyên nhân sửa được identity. |
| ENTRY01 — tư thế đầu | C06 F56: tay Khoai đã duỗi cạnh cẳng tay trong Đào, A gần mép trái bát cô. T03 F0: tay rút về phía Khoai, A cao hơn và lùi trái, gần giữa hai người; sau đó lại đưa lên. | **MAJOR**, so hai PNG đầu; loại reset entry tiếp tục xảy ra. Không có điểm nối C06→C07 đã nghiệm thu. |
| ACT01 — cho ăn thay chuẩn bị bát | C07 chỉ giữ A kẹp trên vùng nhận, bát Đào rỗng; C08 mới thả vào bát. T03 nâng A lên miệng Đào; cô há miệng và nghiêng tới, A chạm/đi vào vùng miệng khoảng F16–33. Sau đó A vẫn xuất hiện trên đũa. | **MAJOR**, bảng 03–05, PNG F24. Đây là động tác đút/nhận bằng miệng trái ý đồ. Không kết luận A đã bị nuốt hoặc có lần release thật vì miếng vẫn kẹp sau đó. |
| MOUTH01 — Khoai không im miệng | Prompt yêu cầu Khoai kín môi toàn cảnh, chỉ Đào nói N07. Khoai mở miệng rõ từ khoảng F6 tới F37, đồng thời với phần Đào há miệng nhận A. | **MAJOR về diễn/khẩu hình vai nghe**, bảng 01–05. Chưa nghe nên không khẳng định anh phát tiếng, nói câu nào hoặc preset sai. |
| GLASS01 — hạ cốc | Cốc phải giữ nâng ở tay ngoài Đào dưới mặt, không đặt xuống. T03 tay vẫn đúng bên ngoài, nhưng cốc hạ dần tới mặt bàn, rõ khoảng F92 trở đi và cuối nguồn. | **MAJOR mất trạng thái inherited**, bảng 12–18/full F143. Không phải cốc đặt vào bát; không ghi sai loại lỗi cũ. |
| BOWL01 — sở hữu giữ nhưng vị trí kết sai | Hai bát hiện từ đầu; cô nắm bát mình ở bên phải rồi kéo sang trái, không lấy bát Khoai. Tuy nhiên cuối cảnh bát mình tới trước vùng tay trong Khoai, không còn trực tiếp trước cô ở nửa phải; A vẫn lệch phải so tâm bát. | **MAJOR endpoint/blocking**, khoảng F44–143, PNG F80/F143. Không tự gọi T03 lặp sự kiện lấy bát Khoai của T01. Không thấy bát Khoai biến mất như T02. |
| BOWL02 — đáy bát/nhịp | Khi cô di chuyển bát, ở một số ảnh giữa đường đáy có vẻ nâng khỏi bàn. Ảnh đơn không đủ kết luận contact vật lý liên tục; sai endpoint đã rõ và đủ bác nguồn. | Chưa chứng nhận base-on-table; không gán chắc xuyên bàn hoặc nâng bát tại frame chưa xem nguyên kích thước. |
| FOOD/DOP | Giữ hai mặt, bàn, rau, hai chấm, đĩa nem và watermark; không thấy hơi/khói hoặc cut trong nguồn. Tỷ lệ vị trí A/tay đổi so reference. | Phạm vi ảnh toàn khung, không bù các MAJOR hành động và continuity. |

## Không chọn range để che lỗi

Đoạn đầu có reset rồi cho ăn; đoạn sau có bát kéo quá xa và cốc hạ. Cắt riêng đoạn đáp ở đuôi sẽ bỏ trình tự đầu/giữa nhiệm vụ C07 và truyền state sai sang C08; lời thực tế chưa được nghe/định thời. Không có range đã chứng minh hoàn thành toàn nhiệm vụ và các gate, nên **không chọn prefix hoặc lấy endpoint T03 làm ref C08**. Không ghép vào phim, đổi nhãn vai hoặc crop món để che lỗi mặt.

## Truy tầng lỗi, không bịa nguyên nhân model

1. **Đã xác định tầng phát sinh:** lỗi có ngay trong native Flow trước mọi cắt/encode; không do local ghép sai, tải nhầm độ phân giải hoặc thiếu frame.
2. **Đã kiểm ràng buộc request:** prompt đúng bản khóa, cả hai ảnh còn trong lịch sử đúng job, một voice chip; âm thanh bật và Agent tắt trước submit. Sự cố gỡ chip của REC279 đã khắc phục trước job này, không có bằng chứng gắn lỗi đó cho T03.
3. **Can thiệp chưa đạt đích hành động:** thêm neo nhận diện đi cùng prompt phân vai vẫn không giữ inherited pose hoặc nhiệm vụ nhận bằng bát. Ingredients là tham chiếu mềm; take này không cho phép coi ảnh tĩnh/prompt dài là khóa động tác.
4. **Giả thuyết chưa chứng minh:** mô hình có thể diễn giải cảnh hai người chia món thành đút ăn, hoặc nhiều điều kiện ảnh/giọng/hành động tranh ảnh hưởng. Không có log nội bộ/trọng số và phép so sánh kiểm soát để chốt nguyên nhân cụ thể. T03 vừa có ảnh pair vừa có wording khác T02, nên không tách được tác động của từng biến.
5. **Vấn đề quy trình còn mở:** cổng giấy đã nêu rủi ro nhưng không thể chứng minh thực thi; tuyến đồng thời voice reference + nhiều trạng thái không có ràng buộc F0/Fend cứng. Cần chọn một thay đổi cơ chế kiểm soát trước request mới, không chỉ thêm câu cấm và chạy lại.

## Disposition và ranh giới quyền

Đã gửi đúng một lượt, debit 10 credit, số dư account 1.023→1.013. Sổ dự án 217/500, còn 283; first-pass 82, retake 46, post-rough 45, reserve 110 đóng. Không T04, không đổi voice/tool/route hoặc mở dự phòng.

Đã chọn đến C06 vẫn là 689 khung / 28,708333 giây; còn 151 khung / 6,291667 giây cho C07–C09 nếu dùng bản thô 35 giây. T03 không được tính vào tiến độ đã hoàn thành. Mục tiêu cuối 30 giây vẫn còn xung đột cần xử lý ở dựng, không tự ép tốc độ hoặc bỏ beat.

Hai agent actual chưa hoàn tất vì giới hạn sử dụng. Gate độc lập **HOLD**, không khai root đã đọc báo cáo chưa tồn tại. Root có đủ bằng chứng để dừng nguồn lỗi nhưng chưa đủ để chọn một nguồn hoặc kết luận cơ chế sửa mới sẽ đạt. Bước tiếp: trình owner chọn cơ chế chuẩn bị mới, làm đầu vào không trả phí trước; một request mới chỉ trình sau review, quote và quyền riêng. Không yêu cầu owner duyệt lại hình T03 như candidate đạt.
