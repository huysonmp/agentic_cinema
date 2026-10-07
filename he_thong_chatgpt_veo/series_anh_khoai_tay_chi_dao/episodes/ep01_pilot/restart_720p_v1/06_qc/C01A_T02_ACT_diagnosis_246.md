# C01A T02 — Chẩn đoán diễn tay, ACT-246

**Mode:** SAMPLED_FRAMES_DIAGNOSIS + TARGETED_PAPER_PROPOSAL. **Disposition:** INTENT_REWORK_RECOMMENDED / ROOT_INTEGRATION_PENDING. Không là reviewer độc lập, media PASS hoặc quyền T03. Không UI/API/Git/credit/generation; chỉ viết tài liệu này.

## 1. Nguồn và khả năng kiểm thực

Đọc exact T02 prompt/request246; native evidence owner QC gắn hash `0b5615beef4e23a42428771109fe36544510270281ae35129de6f6c585a398a7`; đối chiếu ACT intent/T01 frames đã xem ở run trước. T02 request vẫn có heading SUBMITTED_PENDING nên không lấy heading đó phủ nhận media local hiện có. Xem ba board 6fps: 36 mẫu index0,4,…140; xem full frames `00057`, `00065`, `00073`, `00089`, `00121`, `00141` trong `C:/Users/PC/Downloads/du_an_nem_bui/ep01_restart_720p_v1/06_qc/C01A_T02_246/all_native_frames/`. Đây là **mẫu hình**, không toàn144 frame hoặc continuous AV. Index zero-based = số tên file−1; thời gian theo evidence24fps, không đo audio. Không nghe giọng/lời hoặc chứng nhận lip-sync. Root sẽ đọc critic độc lập riêng.

## 2. Quan sát và diễn giải phải tách nhau

| Evidence T02 | Quan sát hình | Diễn giải ACT / giới hạn |
| --- | --- | --- |
| index56, 2,333s / file00057 | Tay ngoài Đào nâng khỏi chỗ nghỉ, cẳng tay từ phía ngoài bát đưa vào trước thân; tay trong vẫn ở vùng nghỉ. | Đúng **cánh tay ngoài screen-right**, không phải lỗi chọn tay. Chuyển động này còn có thể là cử chỉ nói, chưa tự chứng minh sắp lấy đĩa. |
| index64, 2,667s / file00065 | Cẳng tay tiến chéo vào trái, lòng bàn tay mở hướng lên, các ngón trải; chưa gần contact đĩa. | Dễ đọc thành mời/chỉ món, nhất là pose lòng bàn tay ngửa. Không gọi đây là chứng minh chủ ý model. |
| index72/88, 3/3,667s / file00073/00089 | Tay ngoài duỗi về trung tâm bàn, lòng bàn tay mở, các ngón cùng hướng xuống-trái trên ảnh; bàn tay nổi trên khoảng bàn phía sau đĩa, không chồng mép như T01 ở các mẫu đã xem. | Mối liên hệ tay–món có, nhưng **không có dáng bàn tay chuẩn bị tiếp cận/nắm mép**. ACT đánh giá “giới thiệu/mời xem món” mạnh hơn “đang định lấy”; đây là judgment theo mẫu, không cold audience finding. |
| index120/140, 5/5,833s / file00121/00141 | Pose mở lòng bàn tay còn giữ, không thấy thu như T01 ở mẫu4,167s; môi Khoai hé ở hai mẫu tail. | Hold cải thiện mẫu endpoint nhưng kéo dài hình thức trình bày. Môi Khoai hé không tự chứng minh nói; cần AV/PERF kiểm listener trước chọn range. Không dùng tail để đạt hold rồi bỏ qua mouth attribution. |

T01 vấn đề chính là sát/chồng rim và tự thu trước cảnh Khoan; T02 ở mẫu đã xem giảm hai biểu hiện đó nhưng tạo **trade-off nghệ thuật**: tay sạch clearance mà ý định lấy yếu đi. Không nhận đã đóng whole-path clearance chỉ từ36 mẫu. Text mới xuất hiện trên hình được root phát hiện: giữ finding riêng; xóa/che chữ không thuộc nhiệm vụ ACT và không chữa ý nghĩa gesture.

## 3. Giả thuyết tầng prompt, không causal proof

T02 đồng thời yêu cầu `HIGH ABOVE`, khoảng cách ảnh ít nhất một bề rộng bàn tay, “behind the rim”, hold tới cuối, và “not an open-palm presenting gesture”. Tập ràng buộc tạo **xung đột mục tiêu biểu diễn trên giấy**: đích cao/xa và giữ yên giống một động tác trình bày, còn “định lấy” thường đọc từ hướng cổ tay/ngón tiếp cận một mục tiêu cụ thể. Prompt cũng không nói mặt lòng bàn tay quay xuống hoặc ngón chuẩn bị nắm; chỉ “relaxed/aligned”.

Hình actual phù hợp giả thuyết pose trình bày, nhưng nhiều wording cùng đổi, một output, không có causal experiment: **không kết luận HIGH ABOVE là nguyên nhân model đã được chứng minh**, hoặc model không thể làm reach. ACT từng cảnh báo đúng rủi ro này ở treatment T02; cảnh báo không thay proof/output review.

## 4. Đề xuất triển khai tối thiểu, chưa prompt final

Giữ ảnh/scène/camera/bàn/D06/N01 và chỉ retarget **một hành động có đích**:

1. Đào nhìn anh ở “Anh nhìn mãi”; khi “Không hợp thì để em”, ánh mắt đi ngắn tới **mép phải đĩa chung**, cẳng tay ngoài tiến tới mục tiêu ấy. Không đưa tay về Khoai/bát anh hoặc sweep giới thiệu toàn món.
2. Dáng tay chủ đạo: **mu bàn tay hướng lên, lòng bàn tay hướng xuống**, ngón thư giãn hơi cong như chuẩn bị tới mép đĩa; chưa khép nắm, không chạm/thực kéo. Chuyển động nhỏ của cẳng tay rõ hơn một bàn tay xòe xoay ngửa. Đây là cue dương thay cho việc thêm nhiều câu “không được”.
3. Đích **thấp trên vùng trống trước bát Đào, còn cách mép đĩa một khoảng hở nhìn rõ**, thay “HIGH ABOVE” và bỏ chuẩn cứng “ít nhất một bề rộng bàn tay”. Giữ yêu cầu tay/đĩa không overlap trên ảnh nếu framing hiện hành cho phép; DOP phải xác nhận đích thấp vẫn đọc được gap. Không coi khoảng hở nhỏ là tự được chấp nhận nếu mơ hồ contact. Không đổi địa lý hoặc dùng pose contact để đơn giản hóa.
4. Sau âm “em”, còn một **ý định đang tiến chưa hoàn tất**, giữ buffer ngắn mà không xoay lòng bàn tay mời món, không tự thu. EDIT chọn actual range gần lời cuối; không cần chiếu hold trọn native6s. Khoan và dừng/thu vẫn thuộc C01B.

Đây là thay đổi action specification/clearance target, không đổi canon/script; cần root/DOP/critic tích hợp rồi chốt đúng request theo authority. Nếu DOP thấy đích thấp gây rim occlusion với camera đã khóa, **HOLD tuyến này** và trình xung đột thay vì gộp cả thấp/cao trong một prompt. Không thêm test tay riêng hoặc tự mở T03. Root quyết định có cùng MAJOR hai output và ngưỡng dừng238 sau đọc critic; ACT không miễn stop rule vì tên lỗi đổi.

## 5. Tiêu chí kiểm lần được phép tiếp theo

- Cold actual interpretation phải nhận ra **tay tiến để lấy đĩa**, không một cử chỉ mời nhìn/giới thiệu. Đúng arm và gap đẹp không đủ.
- Mu tay/lòng tay, hướng cổ tay/ngón và điểm nhìn cùng hướng tới mép phải đĩa; toàn đường không contact, xuyên props, lấy nem hoặc tự thu. Kiểm mẫu dày và playback đúng capability.
- Có usable interval sau **âm cuối nghe thật** mà tay còn trước contact, chưa hoàn gesture; range có mặt Đào và listener, đúng D06/N01. Không lấy ASR/preset ID làm voice/lip-sync PASS.
- Endpoint C01B trích từ actual selected range; sau Khoan mới dừng/thu. Không dùng fake still, reset về F0 tay nghỉ hoặc đổi ý định qua cut.

**Đã xác định:** cánh tay ngoài đúng ở các mẫu; pose mở/ngửa và hold quan sát được; khoảng hở tốt hơn T01 trên mẫu kiểm. **Giả thuyết:** đích cao/xa/hold + orientation thiếu cụ thể góp phần làm gesture trình bày. **Còn mở:** whole-path/AV/voice, critic và endpoint actual, feasibility đích thấp trong camera hiện hành. **Bước tiếp:** root tích hợp diagnosis + DOP/critic, đóng stop-rule decision trước lượt trả phí; không generation mới từ report này.
