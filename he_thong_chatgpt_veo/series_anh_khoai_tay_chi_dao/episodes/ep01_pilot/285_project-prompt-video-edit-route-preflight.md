# REC285 — Đối soát tuyến thêm video vào prompt của dự án

Ngày 13-10-2026. **NONPAID_ROUTE_INSPECTION / NEW_DRAFT_PREPARED / NO_NEW_SUBMIT.** Owner “ok nhé” cho tiếp tục bước xác minh không trả phí sau REC284; không duyệt thêm lượt generation.

## Phát hiện chính

Video nguồn đã tải lên có mục **Thêm vào câu lệnh** ở menu card trong danh mục Tệp tải lên. Dùng mục đó đưa video vào **composer tại trang dự án**, không nhập prompt ở editor `/edit/a9912c46-8593-41d0-8d0c-1fe4894169d6` như request REC284.

Composer mới hiện **một video ingredient**, rồi gắn cùng START v1 material-only và nhập nguyên prompt REC283. Gói này có cấu hình rõ hơn: Video / Thành phần / Omni 1.1 Flash / 720p / 9:16 / x1 / Agent OFF, độ dài dựa trên video **5,14 giây**, quote live **20 credit** sau khi đủ video + ảnh + prompt. Chưa bấm tạo. Không sinh/upload thêm asset, không đổi giọng hoặc lời.

Đây là **khác biệt điểm vào và cấu hình UI quan sát được**, chưa là nguyên nhân gốc REC284 đã chứng minh. Không có output nên chưa biết backend nhận được gói này, giữ tiếng/cut hoặc sửa món đạt. Giá editor12 / composer20 / public40 phải phân biệt, không gọi đây là giảm giá hoặc dùng 20 nhân cả kế hoạch sửa phim.

## Đầu vào exact và provenance

- Source local: `C:/Users/PC/Downloads/du_an_nem_bui/276_C05_C06_JOIN/C05_C06_5p125S_JOIN_QC_NOT_FINAL.mp4`, SHA `42d826e1356ce67acc6e1057b4ceefc9703f3e705ffa14ae6c09dea7934b5bdf`; nguồn đã upload REC283, giữ nguyên.
- Root chọn card tên đúng `C05_C06_5p125S_JOIN_QC_NOT_FINAL` trong Tệp tải lên → menu Thêm vào câu lệnh. DOM chip có alt **Hình ảnh thành phần video**, thumbnail image ID `55781f96-55b4-428c-ab54-40f5bc918bc1`. Đây là ID ảnh thumbnail quan sát, không tự nhận là backend request/source hash.
- Một ảnh START v1 SHA `491575988bbbea26e16fda3a7f02401b874f9abcc24eda7cdef340764ab232d8`, thumbnail image ID `ff0578c3-808f-4504-bd5f-4b294b1c1906`. Không END, không saved voice mới.
- Exact prompt giữ `04_requests/C05_C06_food_only_edit_DRAFT_283.txt`, SHA `332915713148401fe4aacc8ddda761d86c84e5e50cbb2471c2106e854e513faf`; đã paste/read-back toàn nội dung. Chỉ sửa vật liệu đĩa/A, giữ diễn, mặt, miệng, tay/cốc/bát, lượng A, tiếng/timing/cut; ảnh là material-only, không endpoint.
- Proof local: `C:/Users/PC/Downloads/du_an_nem_bui/285_ROUTE_PREFLIGHT/Flow_project_prompt_video_edit_quote20.png`, đủ hai thumbnail input, model/config/giá. Screenshot không tự chứng minh toàn prompt hoặc audio retention; hashes/read-back riêng.

## Đối chiếu tài liệu chính thức và giới hạn

Đã đọc lại ngày 13-10-2026: [edit workflow](https://support.google.com/flow/answer/16935718?hl=en), [model support](https://support.google.com/flow/answer/16352836?hl=en), [credits](https://support.google.com/flow/answer/16526234?hl=en). Tài liệu mô tả Omni sửa uploaded/generated video, segment tối đa10s và thêm ingredients; Veo Lite/Fast/Quality không hỗ trợ video-to-video. Vì vậy không chuyển sang Veo như một cách sửa nguồn đã được chứng minh. Agent workflow là lựa chọn khác, không cần bật Agent trong phép đề nghị này.

Tài liệu công bố edit40, UI gói hiện20; chưa có căn cứ giải thích. Không lấy giá generation720p4/6/8/10s để thay giá edit. Source file khoảng5,125s có timeline123F, UI duration5,14 có thể phản ánh container/audio hoặc làm tròn: **giả thuyết chưa kiểm**, không tự sửa file hoặc cắt audio để ép nó.

UI đã xác nhận cấu hình chọn720/x1/9:16, nhưng đó chưa chứng minh metadata output hoặc exact frame/cut. Không thấy control giữ bit-exact tiếng/môi; speaker icon trong menu model không đồng nghĩa giữ nguyên audio nguồn. Approval N05/N06/điểm nối cũ không chuyển qua output mới. Rủi ro START kéo pose, A phình/nhả, mất cut hoặc revoice giữ nguyên từ preflight283.

Trong lúc đọc UI, root mở nhầm chế độ sửa tên source rồi bấm Huỷ ngay, không nhập/lưu tên; đã read-back tên không đổi. Context menu của clip chỉ copy/save/download/delete, không cho mã lỗi chi tiết. Lỗi click theo container card không thành công đã được kiểm lại bằng screenshot rồi dùng nút More có trong giao diện; không bấm retry/paid action. Không truy hidden state/backend/cookies hoặc cài mới.

## Quyết định đề nghị — chưa approved

Khuyến nghị **một request qua composer dự án**, source/ảnh/prompt như trên, 720p/9:16/x1/Omni/Agent OFF, **cap20 credit**, trừ retake, không tự retry. Chỉ thay điểm vào/config đã quan sát, không đồng thời đổi nội dung/ảnh/model để khó truy lỗi. Owner cần duyệt riêng vì20 vượt max15 REC238 và một lượt cap12 REC284 đã dùng.

Trước khi gửi, kiểm lại gói, giá và số dư; giá vượt 20 hoặc model/nguồn/đầu vào đổi thì dừng. Nếu có kết quả: tải bản gốc, kiểm hash/giải mã/thông số và đối chiếu mọi khung với nguồn, đặc biệt điểm cắt 2,75 giây/123 khung, đĩa/A, mặt/miệng, tay/cốc/bát và hai đầu; nghe/xem đúng N05 Đào rồi N06 Khoai cùng khẩu hình. Không có output hoặc lỗi lớn thì giữ bằng chứng, không chọn và không tự chạy lại. Không tự nâng độ phân giải, co giãn, đổi giọng, tắt tiếng hoặc che mặt để hợp thức hóa.

Hiện chi 217/500, còn 283; lượt đầu còn 82, tạo lại còn 46, hậu bản thô còn 45 và dự phòng 110 đang đóng. Nếu được duyệt và thực bị trừ 20: chi 237, còn 263; tạo lại còn 26, tổng đã phân bổ còn 153; dự phòng không đổi. Phép này chỉ kiểm sửa nguồn 123 khung riêng, chưa chốt tổng chi sửa cả 689 khung hoặc cảnh nhận mới. Không đưa tỷ lệ đạt khi chưa có dữ liệu.

Reviewer độc lập đã kiểm lại hashes, trực tiếp xem proof/config/quote và đọc toàn prompt; báo cáo `06_qc/project_prompt_food_edit_preflight_independent_285.md`. Root đọc đầy đủ, đồng ý chỉ đóng phạm vi preflight cấu hình/đầu vào, không backend/output PASS. Giữ **OWNER_ONE_REQUEST20_HOLD**.

**Còn mở:** nguyên nhân REC284, chênh giá, backend acceptance và preservation audio/cut/quantity, kế hoạch food toàn tập/timing cuối. **Bước tiếp:** trình owner một lượt cap20 hoặc giữ HOLD. Không paid GO từ tài liệu này.
