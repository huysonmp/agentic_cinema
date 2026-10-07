# REC227-CONT — Preflight motion S → M

Ngày: 2026-10-07. Review độc lập CONT/FOOD, local-only. Đã đọc đầy đủ owner-reference-approval, motion-request và prompt tại 227; đã xem trực tiếp nguồn S v01 và M v03 ở độ phân giải native bằng `view_image(detail="original")`. Chưa đọc báo cáo EDIT hoặc kết luận root trước khi chốt.

**Disposition: READY_TO_REQUEST_APPROVAL.** Gói thử ba take Lite cùng prompt đã đủ cụ thể để trình owner duyệt. Không có lỗi bắt buộc sửa ở mức chuẩn bị CONT/FOOD. Chưa có video để kết luận motion pass. Quyền duyệt pose M và chuẩn bị không đồng nghĩa quyền chạy batch có phí; `paid_motion_request_approved=false` và `generation_approval=PENDING_EXACT_BATCH` vẫn có hiệu lực.

## Gói được review và nguồn đúng

- START: `REF01-S_v01_INPUT_REC227`, asset `c618f06b-fc7a-474c-be1d-9ed62ce87347`, image `46352b9d-1834-40fa-8133-076bfecc9a6d`.
- END: `REF01-M_v03_ACCEPTED_REC227`, asset `d9e64ec1-dc0d-4c80-bcb6-b1e77ece951e`, image `83124e9c-4f6a-4c11-b9ce-697c4e3fcd6c`.
- Route trong request: start/end frames, Veo 3.1 Lite, 9:16, 8 giây, 720p, một output/request, ba request cùng tệp prompt; quote ghi trong request là 10 credit/take, trần batch đề xuất 30 credit.
- Tệp prompt: `R01-SM-motion.prompt-DRAFT.txt`; mục đích là một lần vươn tay và dừng trước tiếp xúc, không phải cảnh thoại cuối.

Đã mở đúng hai tệp `native_path` trong request và tính lại hash cả hai bản download đã tách. Bốn tệp đều khớp hash start/end; hai asset riêng được khai báo trong request. Đây là xác minh byte cục bộ, không phải kiểm tra UI trực tiếp. Reviewer không dùng browser để xác nhận route/quote hiện tại.

## Quan sát ảnh và rủi ro đường chuyển

| Điểm | Quan sát trực tiếp ở START/END | Rủi ro khi sinh chuyển động / đánh giá preflight |
| --- | --- | --- |
| Tay đúng phía | START hai tay Đào nghỉ; END chỉ tay ngoài phía phải, gần ly, vươn xuống/hơi vào trong. Tay trong Đào và hai tay Khoai giữ vị trí. | Prompt xác định đúng tay; cần phát hiện việc model đổi tay giữa shot hoặc làm tay nghỉ chuyển theo. |
| Bát Đào | END tay che một phần đường bao trước phải của bát, nhưng hình tay và gốm còn phân biệt; không thấy lỗi nhập hình chắc chắn. | Rủi ro chính, mức cao cho phép thử: nội suy từ tay nghỉ ở cạnh ngoài đến tay phía trước bát có thể xuyên thành bát, cắt qua miệng bát hoặc nhập ngón vào gốm. Pose tĩnh đã được owner chấp nhận với caveat; caveat chưa đóng ở mức motion. |
| Đũa phải và ly | START tay nghỉ gần đầu đôi đũa; END tay ở bên trái đũa, ly vẫn ngoài cùng bên phải. | Cần chuyển tay ra phía trước/ngoài bát trước khi vào trong; không coi đường thẳng nối tọa độ 2D đầu–cuối là đường an toàn. Không để đũa dính theo ngón, ly bị đẩy hoặc tay xuyên ly. Đây là giả thuyết đường đi để kiểm chứng, không phải quỹ đạo đã quan sát. |
| Đĩa và gap cuối | END đầu ngón ở cạnh phải đĩa, thấp hơn đỉnh ụ nem; có nền bàn nhìn thấy giữa ngón và đĩa. | Khi ease-in hoặc hold, model có thể làm mất gap, vượt vào đĩa/món rồi lùi lại. Phải kiểm cả quá trình đến đích và toàn bộ hold, không chỉ frame cuối. |
| Camera, mặt và bàn | Hai ảnh cùng khung, Khoai trái/Đào phải; mặt và môi khép, ánh mắt, trang phục/nơ hồng, bàn và món giữ nội dung. | Reference tĩnh tương thích để thử. Prompt khóa camera và mặt; cần phát hiện zoom/reframe, head drift hoặc camera move dùng để che lỗi tay. |
| Nội dung bữa ăn | Nem giữa bàn, rau trước trái, hai chén chấm, hai bát rỗng, hai đôi đũa nghỉ và ly ngoài Đào giữ. | F0/bố trí bữa ăn cần giữ xuyên shot: không tráo vị trí/số lượng, không xuất hiện thức ăn trong bát, không mọc thêm món/đũa, không hơi nước/khói hoặc food transfer. |

“Tay che bát” là hiện tượng hình chiếu; không tự động đồng nghĩa xuyên bát. Kiểm motion phải dựa trên thứ tự che khuất liên tục, đường viền và tính toàn vẹn của gốm/ngón qua các frame. Không bắt buộc có khoảng nền riêng giữa mọi pixel tay và bát ở END vì pose đã duyệt có che khuất. Tuy nhiên, sự nhập vật liệu, đảo thứ tự trước/sau bất khả lý hoặc ngón xuất hiện xuyên lòng/thành bát là lỗi chặn.

Prompt hiện tại đã nêu đi quanh ngoài bát, đi phía trước cạnh ngoài với separation, tránh gốm/đũa/ly, dừng có gap và giữ đích. Không cần sửa prompt trước trình duyệt vì đây chính là phép thử clearance còn mở; không coi việc viết các ràng buộc là chứng minh model sẽ đáp ứng.

## Tiêu chí kiểm từng frame sau khi có quyền và có output

Kiểm từng take độc lập bằng playback tốc độ thường và toàn bộ frame native theo FPS thực tế. Không chỉ chọn các frame đẹp; ghi timecode/frame đầu tiên và cuối cùng của lỗi. Tập trung hơn ở pha vươn khoảng 0–2 giây, thời điểm giảm tốc và toàn bộ pha giữ đích khoảng 2–8 giây. Không bỏ qua frame đầu/cuối hoặc một lỗi thoáng qua giữa hai frame chọn mẫu.

| Giai đoạn / hạng mục | Tiêu chí đạt | Lỗi chặn hoặc điều cần ghi |
| --- | --- | --- |
| Frame đầu | Tư thế S: cả hai tay Đào nghỉ, hai tay Khoai nghỉ, camera/mặt/bàn khớp nội dung START. | Tay đã vươn ngay từ frame đầu; nguồn sai; crop làm mất mặt hoặc bàn tay. START không cần gap ngón–đĩa giống END vì tay còn nghỉ xa đĩa. |
| Toàn pha vươn | Chỉ tay ngoài Đào vươn một lần; cánh tay liên tục, cổ tay/ngón tự nhiên; đường đi giữ tay trước/ngoài bát mà không nhập gốm. | Ngón xuyên thành/miệng bát, biến dạng thành bát, tay dư/mất ngón bất thường, đổi tay hoặc tay trong bị kéo theo. |
| Clearance đũa/ly/chén | Vật thể đứng yên, tay không xuyên/nhập, không kéo theo đũa, không chạm/đẩy ly hoặc chén chấm. | Collision nhìn thấy, vật dính tay, vị trí vật thay đổi để mở đường hoặc vật biến mất/tái xuất. |
| Đến đích | Ngón ở cạnh phải nhìn thấy của đĩa, dưới đỉnh ụ nem; gap với vành đĩa nhận ra rõ; dừng trước tiếp xúc. | Đi sau/trên ụ nem, ngón chồng vùng thức ăn, chạm/nắm vành, đĩa bị kéo/nhấc hoặc overshoot rồi sửa lại. |
| Hold đến frame cuối | Giữ pose M bình tĩnh với gap còn nhìn thấy; chỉ thở nhẹ/chớp mắt tự nhiên; không retract, loop hoặc reach lần hai. | Gap đóng lại trong hold, tay giật/trôi vào món, lùi tay, reach lặp, freeze bất thường cần ghi riêng theo mức ảnh hưởng. Frame cuối đạt không xóa lỗi trước đó. |
| Mặt và môi toàn shot | Cả hai mặt và tay động luôn nhìn thấy; giữ nhân dạng/góc nhìn, cả hai môi khép, Đào nhìn Khoai và Khoai biểu cảm tiết chế như nguồn. | Miệng mở hoặc nhép, head/face morph, mặt khuất/cắt, biểu cảm/gaze chuyển làm thay đổi beat. |
| Camera và bàn/F0 toàn shot | Khung camera khóa; bữa ăn giữ đúng bộ vật, vị trí và trạng thái nguồn; không steam/smoke/food transfer; nơ hồng/quần áo giữ. | Camera move/cut/reframe, đồ ăn/bát/rau/chén đổi, bát có thức ăn mới, tay cầm/ăn/uống hoặc thêm vật mới. |
| Watermark và audio | Giữ dấu native, không chữ/panel mới. Prompt không thoại/nhạc hát/narration và môi khép. | Watermark/chữ mới cần ghi; có lời nói/giọng hát/lip movement là fail phạm vi bài thử. `audio_off_control_verified=false` nên chưa được gọi là audio đã tắt. Nếu output có audio thì phải kiểm riêng trước sử dụng, không suy im lặng từ prompt. |

Disposition hậu kiểm từng take: PASS_MOTION_TEST chỉ khi không có lỗi chặn trong tất cả frame được kiểm; FAIL_MOTION_TEST khi có lỗi xác nhận; REVIEW_NEEDED nếu occlusion hoặc chất lượng không đủ kết luận clearance. Dù PASS_MOTION_TEST, vẫn chỉ là bài thử S→M, không tự phê duyệt full G1, cảnh thoại hoặc full AV.

## Hash kiểm tại lượt này

| Tệp / nhóm | SHA-256 tính lại | Kết quả |
| --- | --- | --- |
| START native và download tách | `eba9a13c86f359df458022a5a54664264e5bb29fcca08d6181454cb1ee482422` | Hai bản khớp request |
| END native và download tách | `66defd18afc0845da8b34968446b98f547dcad951e6712e2e6a81ff2d5e2017c` | Hai bản khớp request và hash pose owner duyệt |
| `owner-reference-approval.json` | `5ddf90a02f945e5610768d950a1fc08cae5cad565427a7a1e6cb48f6f2230fa0` | Định danh tài liệu đã đọc |
| `motion-request-DRAFT.json` | `6215936e98c019d1bcc635ed7c5e9a364da5dec50fdf35ff780024c0f40434ae` | Định danh bản request được review |
| `R01-SM-motion.prompt-DRAFT.txt` | `af94764252de0a2a057490eec874059d9804b1caa92e7bfa01d552c054cfafc5` | Định danh prompt cùng batch đề xuất |

## Closure và quyền còn mở

CONT/FOOD preflight hoàn tất: **READY_TO_REQUEST_APPROVAL** cho đúng ba take Lite, cùng prompt, quote đề xuất 10/take và trần 30 credit. Đây là chuẩn bị trình duyệt, không phải approval chạy có phí hoặc motion pass. Trước submit, root vẫn phải có owner duyệt exact batch, xác nhận balance và route/quote live, giữ đúng start/end, dừng khi điều kiện request không đáp ứng. Nếu native download lỗi thì giải quyết trước khi sinh tiếp; không tự retry hoặc mở rộng batch.

Reviewer không thực hiện browser, Git, chi tiêu hoặc generation. Bước tiếp theo là tổng hợp báo cáo độc lập và trình owner quyết định batch; rủi ro hand–bowl clearance chỉ được đóng sau khi có motion thực tế và kiểm từng frame.
