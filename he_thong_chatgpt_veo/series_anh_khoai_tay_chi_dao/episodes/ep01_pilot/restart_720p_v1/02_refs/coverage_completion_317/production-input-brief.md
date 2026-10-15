# REC317 — Brief bù đầu vào R01/R04 và cổng audio

Ngày15/10/2026. **Brief chuẩn bị, chưa có ảnh mới hoặc request video.** Không đổi lời/canon/reference đã chốt. Đọc cùng storyboard317 và quyết định `00_decisions/receive-ending-handshift-approval-317.json` (các path trong brief tính từ `restart_720p_v1`).

## A. Phân vai nguồn — không dùng một ảnh cho mọi thứ

| Nguồn | Được dùng cho | Không dùng để chứng minh |
| --- | --- | --- |
| `02_refs/caught_excuse_315/T_CAUGHT_END_v1_FOR_REVIEW.png` | Nhận diện hai người, trang phục, hướng khung chung, bảng màu/quán/bàn và scene inventory | Không phải trạng thái R01: đang kẹp A, cốc đang ở tay Đào. Không phải master món đã nghiệm thu |
| `02_refs/coverage_A_314/K_memory_ENTRY_v1_FOR_REVIEW.png`, `K_memory_v2_FOR_REVIEW.png`, `D_question_v2_FOR_REVIEW.png` | Nhận diện/góc cận/thần thái đã duyệt; kiểm mặt mới không drift | Không chứng minh tay/bát/đũa ngoài khung biến mất hoặc geometry3D |
| `C:/Users/PC/Downloads/du_an_nem_bui/nembui.jpg` và `z7750931050074_6fa76793489e54e476846aad4d233684_806643377.jpg` cùng thư mục | Ảnh món người dùng cho phép sử dụng, phải xem lại đúng tệp trước khi dùng làm reference vật liệu | Không tự suy thành quyền sở hữu bản quyền, không dùng làm pose/camera/ánh sáng của cả cảnh |
| `02_refs/coverage_A_314/R01_EXIT_F148_UNEDITED_NOT_NEW_MASTER.png` | Đối chứng trạng thái cuối R01 cũ: đã thu tay, chưa A, hai bát rỗng, cốc trên bàn | Không làm chuẩn vật liệu nem: ảnh này có món cũ phẳng |
| `02_refs/C05_START_from_C04_T02_selected_F143_263.png` | Đối chứng logic cuối tranh thủ và hướng nhìn đã chấp nhận trước đây | Không phải exit của rangeC04[12,124), không cho phép kế thừa món sai |
| `02_refs/receive_ending_316/S1_READY_HANDSHIFT_VARIANT_FOR_REVIEW.png`, S2/S3 cùng bộ | Ràng buộc tương lai: ai giữ bát/cốc/đũa, A→bát, B mới và kết | Không lấy vị trí tay S1 làm đầu R01/R04, không dùng ảnh cuối nhận làm nguồn trước nhận |

Đã kiểm lại hai tệp tồn tại và xem nội dung trong vòng317. SHA256: `nembui.jpg` = `a51303f7100edd0944dc00daa19402fecfe24bb0e15a4143da8f8eae7b9e3a2d`; ảnh tên dài = `1237956e99458385f95f1edf18e0a98e1bddb777030ac1d69fab05fa7a51d741`. Hash là neo tệp, không chứng nhận quyền sở hữu bản quyền. Trước lần dùng tiếp phải kiểm lại nếu tệp đổi.

Quan sát ảnh thật: sợi/miếng mảnh không đồng đều, bề mặt phủ thính có hạt, tông vàng-be; ảnh thứ nhất còn có lát mỏng lớn xen kẽ, không phải mọi phần đều là sợi. Không giản lược thành mì hoặc dải nhựa trơn đều nhau. Ảnh AI mới vẫn có nguy cơ quá trơn/đều và thiếu lớp thính so ảnh thật; approval tư thế S1–S3 **không đóng kiểm món**. Dùng ảnh thứ nhất làm đối chứng chính texture/mix, ảnh thứ hai kiểm vẻ rời/tơi; không sao chép các món khác trong ảnh thứ hai sang bàn dự án.

## B. MASTER_R01_START — toàn cảnh bữa ăn trước lời Đào

**Nhiệm vụ:** khán giả hiểu hai người cùng bàn ở quán phố nhỏ bình dân gọn gàng, sắp trò chuyện tự nhiên. Hai mặt đủ lớn để theo đối đáp; không để đĩa hoặc phố chiếm vai chính.

**Trạng thái:** Khoai trái, Đào phải, ngồi cạnh nhau; hai bát riêng rỗng trên bàn. Một đĩa nem nguội dạng sợi/miếng mảnh phủ thính theo ảnh thật; đĩa rau riêng trước-trái, hai chén chấm riêng. Cốc trên bàn phía ngoài Đào, không trong bát. Chưa ai cầm/gắp A, chưa B. Đũa Khoai ở phía anh, Đào ở phía cô; tay trước hành động không tự cầm thêm một đôi. Tư thế đầu không là pose đã nâng cốc/bát hoặc đang nhận món.

**Camera/ánh sáng:** dùng khung chung cùng thế giới với T-caught đã duyệt, không đổi bàn/ghế để giả shot mới. Giữ vùng rau/chấm/cốc đủ an toàn ở biên, giữ đầu/lá. Mặt ưu tiên hơn đèn nền; không ánh đèn hút mắt mạnh ngang mắt nhân vật. Nắng/ánh sáng chiều ấm theo reference, chưa chốt thông số lens/khẩu độ giả. Không crop cực mạnh từ ảnh sai rồi gọi master mới.

**Exit dự kiến về state, chưa timecode:** sau N01→“Khoan”, Đào đã dừng/thu tay; món chưa bị lấy/đĩa chưa kéo; Khoai nhìn xuống trước khi kể. Không dùng MASTER_START làm exit nếu tay khác nhau. Quyền chạm vành đĩa hạn chế của C01A cũ không là quyền kéo/lấy món.

**Review một gói:** identity; food so hai ảnh thật; vị trí/đủ mép đạo cụ; scale hai mặt; cùng bàn/ghế; state đầu–cuối; khả năng chuyển K-entry mà không đổi chỗ ngồi. Nếu ảnh đẹp nhưng thiếu bát/rau/cốc hoặc có A sớm: không chọn.

## C. R04_ENTRY / R04_EXIT — cùng món, cùng camera, đúng cơ hội

**ENTRY:** sau “Chờ mẹ quay lưng.”, A chưa gắp, hai bát trên bàn. Cốc phải còn trên bàn hoặc có chuyển động nhấc quan sát được; không từ ngoài khung tự xuất hiện trong tay. Không dùng T-caught đã cầm A làm entry.

**Quá trình cần giữ:** Đào chuyển chú ý sang cốc và nhấc bằng tay ngoài → Khoai dùng tay ngoài lấy đúng một A từ đĩa về phía mình → Đào nhìn lại → Khoai vẫn giữ A, chưa ăn/thả. Tay trong Đào chưa nâng bát. Tay nghỉ Khoai không đỡ bát cô.

**EXIT:** hai bát còn rỗng trên bàn, cốc trong tay ngoài Đào, A trên đũa Khoai. Đào đã nhìn lại; T-confirm chỉ thêm ánh nhìn xác nhận A, không phát hiện lại từ đầu. Nguồn món ở entry/exit phải là cùng hướng hình, không một đầu flat-chip một đầu ribbon.

**Hai route kỹ thuật còn mở, chưa tự chọn:**

1. Giữ nativeC04 và sửa cục bộ món/A nếu có phương pháp bảo toàn tay/mặt/chuyển động, có phép kiểm actual; không suy từ sửa still thành sửa video đạt.
2. Tạo nguồn chuyển động mới từ entry/exit đúng món/pose nếu route1 không đủ bằng chứng. Cần quote/bucket và quyền chạy riêng; không lấy retake0 làm first-pass để chi tránh gate.

Không thể chọn route bằng chất lượng endpoint tĩnh hoặc danh nghĩa ít credit hơn. Kéo end124→144 chỉ thay timing, không sửa món hoặc redraw. Hai route đều phải kiểm dải chuyển tiếp, gaze cơ hội và exact endpoint thật sau trim.

## D. Audio route — việc có thể kiểm trước khi có phí

1. Inventory exact accepted audio/video đối chứng theo bảng thoại317; xác định đường dẫn thật, hash, số kênh/tần số mẫu/duration và approval gốc. Không dùng sample test cùng tên voice thay tiếng take đã chọn.
2. Khi có browser hoạt động, chỉ đọc khả năng UI liên quan audio input/lipsync/native voice, phạm vi clip và giá hiện; chưa upload, đồng ý điều khoản mới, submit hoặc cài công cụ ngoài scope. Ghi đúng observed/inferred/unknown. Không gọi tính năng được hỗ trợ chỉ từ tên model.
3. Lập route cho từng shot nói mới: có tái dùng exact audio điều khiển miệng hay không; nếu tạo tiếng native thì saved voice nào, ai nói, câu nào, gate đối chiếu nào; chi phí thực nằm đâu. Giữ đường audio cũ làm đối chứng trong mọi route.
4. Nếu thiếu khả năng nghe/xem hoặc native tải về, báo HOLD đúng năng lực thiếu; không tuyên bố agent đã nghe và không hỏi owner xác nhận lặp từng thao tác kỹ thuật.

## E. Điều kiện chuyển khỏi bước chuẩn bị

- Có masterR01 và cặpR04 chọn được với nguồn/hash/đúng vai nguồn; reference mới chỉ promotion đúng phạm vi review thực.
- Có ranh giới trạng thái đầu–cuối được định danh; slot thời gian vẫn dựa trên đo actual, không tự gán ảnh bằng4s/6s.
- Có audio route được kiểm và đủ thông tin request, không hứa giữ đúng K20/D06 bằng tên preset.
- Cấu hình/quote/bucket/authority được kiểm ngay trước paid. Budget gần nhất221 không là quyền chi221.

Không phát sinh Flow credit hoặc generation ở brief này. Không tự mở reserve, không auto-rerun, không thay nguồn video đã chọn hay EDL.
