# REC283 — Duyệt ảnh; chuẩn bị một phép sửa món trên video nguồn

Ngày 13-10-2026. **STILLS_APPROVED_FOR_REFERENCE / LIVE_EDIT_DRAFT_PREPARED / NO_PAID_SUBMIT.**

## Đã xác định và quyết định đã chốt

Owner “ok rồi đấ” duyệt START v1 và END v2 REC282 về ngoại hình món và tư thế nhận–bỏ làm tham chiếu. END v1 bị bác vẫn không dùng. Không chuyển approval ảnh sang master, chuyển động, giọng, khẩu hình, điểm nối hoặc toàn phim.

Owner xác nhận “Xác nhận — bấm Tôi đồng ý” cho thông báo quyền tải bản nối C05→C06 lên Flow. Đã bấm đúng một lần, không chọn “không hiện lại”; tải hoàn tất và mở được video nguồn. Chưa bấm tạo.

Nguồn duy nhất: `C:/Users/PC/Downloads/du_an_nem_bui/276_C05_C06_JOIN/C05_C06_5p125S_JOIN_QC_NOT_FINAL.mp4`, SHA-256 `42d826e1356ce67acc6e1057b4ceefc9703f3e705ffa14ae6c09dea7934b5bdf`. Hash kiểm lại khớp. Đây là bản nối 123 khung/24 fps/5,125 giây; cut F66 tại 2,75 giây, được owner duyệt phạm vi tiếng/nhịp/cắt REC277. Không sử dụng full C06 có tail lỗi.

## Đề nghị sửa, không làm lại diễn

Chỉ sửa **chất liệu nem trên đĩa và phần nhỏ đang được giữ ở đầu đũa**: thịt/bì rời, dải mỏng không đều, thính; không lát đặc đồng dạng, không khói. Giữ vị trí, đường đi và kích thước phần gắp gần nguồn, chưa thả. Toàn bộ mặt, miệng, tay, diễn, cốc/bát, bối cảnh, camera, tiếng và cut theo video nguồn.

Đã gắn đúng START v1 SHA `491575988bbbea26e16fda3a7f02401b874f9abcc24eda7cdef340764ab232d8` làm **tham chiếu vật liệu, không tư thế/endpoint**. Không END, không voice preset mới, không yêu cầu tái dựng lời hoặc miệng. START có redraw và phần gắp dài hơn nguồn nên không được sao chép toàn ảnh.

Prompt exact đã lưu và nhập/read-back tại `restart_720p_v1/04_requests/C05_C06_food_only_edit_DRAFT_283.txt`. Maker và reviewer độc lập thực chạy local; báo cáo tại `06_qc/food_repair_maker_preflight_283.md` và `06_qc/food_repair_independent_preflight_283.md`. Scope là tài liệu + still mẫu, không nghe/xem AV liên tục; không nhận quality PASS.

## Kiểm live và giới hạn còn mở

- Trang editor nguồn: https://flow.google.com/project/bcb1f53c-13b6-4719-b866-01348dfcddd6/edit/a9912c46-8593-41d0-8d0c-1fe4894169d6.
- UI ghi “Mô tả cách chỉnh sửa video này…”, Omni 1.1 Flash, một clip đang chọn; tổng thời lượng hiển thị `00:05:03`, phù hợp cách đọc 5 giây 3 khung nhưng chưa là kiểm metadata output.
- Nhập source/ingredient thành công không chứng minh backend sẽ nhận hoặc giữ cut/audio. Có một ảnh ingredient; ID `ff0578c3-808f-4504-bd5f-4b294b1c1906`. Không lưu signed URL, account screenshot hay dữ liệu phiên vào Git.
- **Quote live trên tooltip nút tạo: 12 credit.** Root dùng Tab đưa tiêu điểm đến nút, không bấm nút. Tài liệu Google hiện công bố video edit 40 credit; giá public không được thay quote live của gói này. Nguyên nhân khác biệt chưa xác định; không tự kết luận được giảm giá/hoàn phí hoặc rằng hai route hoàn toàn đồng nhất.
- Editor không hiện lựa chọn khóa 720p/x1 hoặc giữ tiếng nguồn. UI playback có tiếng bật không phải cấu hình bảo toàn audio cho output. Không có video DOM metadata để đối soát bằng cách đọc thông thường; không truy hidden state/backend. Native nguồn là 720×1280 theo evidence đã duyệt, **output chưa có nên resolution/frame count/duration/audio đều chưa xác nhận**.
- Proof local: `C:/Users/PC/Downloads/du_an_nem_bui/283_REPAIR_PREFLIGHT/Flow_food_edit_live_quote12_283.png`. Không đưa screenshot account lên Git.

Nguồn chính thức đã đọc để phân biệt khả năng/giá, không dùng làm cam kết chất lượng: [video edit](https://support.google.com/flow/answer/16935718?hl=en&ref_topic=16908930), [model features](https://support.google.com/flow/answer/16352836?hl=en), [credits](https://support.google.com/flow/answer/16526234?hl=en), [saved voice chỉ Ingredients](https://support.google.com/flow/answer/16353334?hl=en). Giá live 12 là quan sát UI riêng, không suy từ các trang này.

## Đề nghị owner chốt một lượt có giới hạn

**Đề nghị, chưa được cấp:** cho phép đúng một phép sửa trên nguồn nêu trên, quote không quá **12 credit**, trừ bucket retake, không tự chạy lại. Owner cần biết trước rằng editor chưa cho khóa rõ resolution/giữ audio; đây là phép kiểm năng lực sửa nguồn, chưa là production PASS. Nếu anh muốn chỉ chạy khi có khóa rõ cấu hình, giữ HOLD và không chi.

Trước submit phải làm mới source/ingredient/prompt/quote và kiểm số dư tài khoản. Giá vượt 12 hoặc route/input đổi thì dừng; không coi câu “tiếp tục” là miễn cổng này sau STOP REC280. Không mở reserve hoặc mặc định sửa hàng loạt.

Nếu được phép và có output: tải bản gốc, hash/full decode/metadata; kiểm toàn bộ khung thực với nguồn, đặc biệt mặt/miệng, đĩa/A, lượng món, tay/cốc/bát, cut 2,75 giây và hai đầu. Kiểm N05 Đào “Chờ em quay lưng nữa à?” rồi N06 Khoai “Anh gắp cho em mà.” trên output thực, không chuyển duyệt tiếng cũ. Thiếu capability nghe/AV thì trình owner exact candidate, không dùng ASR làm nghe thật.

Sai món, biến đổi diễn/mặt/miệng/voice/cut, nhả A hoặc phình phần gắp: NOT_SELECTED, lưu lỗi và chẩn đoán; không retry tự động, không che mặt bằng cận món, không revoice/patch động để giả đóng lỗi. Output khác 720p hoặc thay duration/cut phải giữ HOLD và trình lại, không tự upscale/co giãn.

## Ngân sách và bước tiếp

Hiện chi **217/500**, còn **283**: first-pass 82, retake 46, post-rough 45, reserve 110 **đóng**. Chi mới REC283 **0**. Nếu thực debit đúng 12: chi 229, còn 271; retake 34, ba bucket usable tổng 161; reserve không đổi. Đây không phải dự báo chắc đủ sửa mọi cảnh.

Giả định đang kiểm: model có thể thay vật liệu món mà giữ các thành phần khác. Rủi ro quan trọng: START kéo lệch pose/nhận diện; model làm mượt cut hoặc thay audio/timing. Phải dùng output thực kiểm, không ghi xác suất thành công khi chưa có dữ liệu.

Food gate các cảnh cũ vẫn mở; chín mẫu REC282 không phải audit toàn 689 khung. Một repair đạt chỉ đóng phạm vi target 123 khung, không cả phim. Sau kết quả mới chốt phạm vi/chi phí sửa phần còn lại và route nhịp Đào đưa bát–nói/Khoai bỏ nem. N07/D06/C09, mục tiêu 30 giây và conflict rough 35 giây giữ nguyên; không tự bỏ lời/beat hoặc đổi giọng để tiết kiệm.

**Bước tiếp:** owner chọn thử một lượt cap 12 với giới hạn trên, hoặc giữ HOLD chờ cấu hình rõ. Chưa paid generation, chưa video mới, chưa release.
