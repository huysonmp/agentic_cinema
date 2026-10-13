# REC302 — C07 một lượt đã chạy; native bị loại vì sai Đào và trạng thái cốc/tay
13-10-2026. **ROOT REJECT / NOT_SELECTED / NO_RETRY / C08 HOLD.**

## Quyền chạy và debit
Owner duyệt đúng một C07_RECEIVE_D06_T01 tối đa7, không tự chạy lại; [authority](restart_720p_v1/00_decisions/C07-RECEIVE-D06-one-run-approval-302.json). Final read-back prompt/hash/ảnh+mộtD06, quote7/Ingredients/Omni1.1Flash/720p/9:16/4s/x1, AgentOFF và noAudioOFF khớp bound; chỉ click tạo một lần.
Job mới “Characters at street eatery table”, ID `64c0154c-8b0c-487f-9685-cd9fcbdc4055`; composer được xóa sau submit. Số dư1.029→1.022: debit **7**. Sổ **258/500**, còn **242**; first82/retake5/post45/reserve110 đóng. Phần tăng50 trước job chưa xác định, không tăng cap. Screenshot BALANCE_AFTER ban đầu không hiện account menu, chỉ ghi job13%; **không dùng làm chứng cứ số dư**. BALANCE_AFTER_VERIFIED mới đọc1.022 và là proof debit.

## Native và QC thực
Tải UI **720p Kích thước gốc**, download thành công. Original/owner/repo cùng SHA256 `85fb15de347d8054803eeeef186ea6d4f2985baa9fe46018bf281af9a6cfe527`,823.064byte.
Owner: `C:/Users/PC/Downloads/du_an_nem_bui/302_C07_RECEIVE_D06_T01/C07_RECEIVE_D06_T01_NATIVE_720p_302.mp4`.
H.264720×1280/24fps/96F/4s; AAC48kstereo4,010s. Full decode sạch, native không đổi. Helper có sẵn tạo96PNG/audio/evidence; FFmpeg tạo6denseboards16F/page, nhãnF0–95 đủ liên tiếp, fps_mode passthrough, không lặppage. Fontconfig báo warning nhưng exit0/nhãn hiển thị, không lỗi media.
Root xem **toàn96frames qua six full16 boards**, PNGfull F0/F32/F64/F95; không actual nghe hoặc continuousAV. Offline ASR không prompt đọc “Thế em quay lại đúng lúc rồi” khoảng0,86–2,60s; không chốt D06, accent, người phát tiếng, âm cuối hoặc sync.

## Expected → observed
| Gate | Native quan sát | Disposition |
| --- | --- | --- |
| Đào quả đào có cuống/lá, không thay mặt | NgayF0 và toàn96F là cô gái tóc nâu/ tai người, mất đầu quả đào/cuống/lá | **MAJOR identity; không range nào sửa bằng cắt** |
| Cốc tay ngoài vẫn nâng, một tay trong nâng bát | Cốc đã ở bàn từF0; tay ngoài rời cốc rồi cả hai tay đỡ bát | **MAJOR trạng thái nhập và choreography; không tự đổi vì động tác dễ hơn** |
| Khoai nghe kín môi | Mở miệng rõ khoảngF5–11 rồi khép | Lỗi diễn vai nghe; chưa kết luận có tiếng nam hoặc nói sai vai |
| A giữ, chưa thả/ăn | Cùng phần nhỏ vẫn kẹp trên tips trong toàn nguồn; bát riêng được đưa sang gần A | Điểm tiến triển về đường nhận, **không bù identity/cốc/tay hoặc chứng minh mọi contact sạch** |
| Mặt người nói/props | Hai mặt thấy, hai bát/rau/hai chấm/đĩa/cold food còn; không cận món | Coverage còn nhưng không productionPASS |

Không ghép bản này, chọn prefix, crop che đầu Đào, lấy endpoint C07 hoặc chuẩn C08 từ nó. Approval300 lời/range của C06 vẫn đúng exactfile, không truyền sang native mới. Không cần yêu cầu owner duyệt hình có lỗi rõ.

## Đối soát ảnh job — tránh chẩn đoán nhầm input
Đọc image ingredient hiện trong history, tải qua API downloadMedia của img thực, ID `e40803c5-9a46-44af-84d6-a588ef762895`; local evidence `06_qc/C07_RECEIVE_HISTORY_IMAGE_302.jpg`, SHA `2d195991e9db1194f34edb4ca1c0f1df09faac79733185d0ebe63a05cee90176`.
Root xem JPEGfull: đúng Đào quả đào/cuống/lá, cốc raised, hai bát, poseF47. Kích thước720×1280; MAEpixelPNG→historyJPEG RGB khoảng0,83/0,60/0,96 mức0–255, phù hợp mã hóaJPEG lại, **không byte-identical PNG**.
Popup screenshot HISTORY_INPUT_IMAGE có preview video/cached view dễ bị nhầm là ảnh source; không dùng screenshot đó một mình kết luận source đã human. Matched downloaded image thực là nguồn đối soát. Không gọi xác minh byte input nội bộ model hoặc truy hiddenAPI.

## Truy tầng nguyên nhân và lỗi quy trình
1. **Đã xác định:** identity/cốc/tay sai ngay trong native trước cắt ghép. Không do localedit, chọn nhầm720p, tải thiếu hoặc ảnh F47 gốc đã human.
2. **Đã xác định control:** saved D06 + một ảnh, route/quote/toggle và prompt đúng bản đã duyệt. Tháo/reattach voice và Agentinspection đã khôi phục trước job; không có chứng cứ quy chúng là nguyên nhân.
3. **Hồi quy bỏ sót ở preflight301:** đọc choreography295/range300/ảnh296 nhưng chưa đối soát actual lịch sử C07_T02_277 và C07_T03_280 trước trình chạy. T02 từng hóa Đào thành người với1scene+D06; T03 dùng scene+portrait/explicit fruit identity giữ nonhuman nhưng hành động sai. Gói301 quay về1scene và chỉ mô tả “adult peach woman”, bỏ neo nhận diện riêng và chi tiết hình thái quả đào mà không ghi lý do/kiểm nguy cơ hồi quy. Đây là **thiếu sót kiểm soát của root/preflight**, không đổ cho owner đã duyệt.
4. **Chưa chứng minh causal:** T03 thay cả prompt và reference; không chứng minh thêm2ảnh chắc chắnfix, thiếu từno-hair là nguyên nhân duy nhất, savedvoice gây human hoặc model nội bộ cụ thể nào. Ingredients+reference trong các take thực không được coi khóaF0/identity/props.
5. **Gate cần bổ sung:** mọi retake phải đọc failure ledger actual của cùngscene; ghi biện pháp đã thử/giữ/bỏ và lý do; identity/state regression trước action success. Reviewer301 đúng scopepaper/still nhưng inputcontext chưa có đủfailurehistory nên không đủ dự báo rủi ro hồi quy.

Phản biện actual độc lập `06_qc/C07_RECEIVE_actual_independent_302.md` đã hoàn tất; root đã đọc toàn báo cáo. Reviewer tự kiểm hash native/JPEG, xem đủ96frames và bốn ảnh fullres: cùng kết luận NOT_SELECTED, không có prefix hợp lệ; thêm finding đũa nghỉ Đào mất so START, root đối chiếu full F0 xác nhận không thấy ở vị trí cũ. Khoảng hở bát với tay nghỉ vẫn bị che một phần, không kết luận chắc xuyên tay. Reviewer không actual nghe/continuousAV và không tự browser hay tái audit277/280; phân tích lịch sử là kiểm của root, không gán cho reviewer. Không phải mediaPASS.

## Đề xuất tiếp — chưa quyền chạy lại
Chuẩn gói phục hồi **scene F47 thật + neo nhận diện riêng khớp khuôn mặt hiện hành**, giữ choreography nhận trước/thả sau và D06; explicit peach skin/cleft/stem/leaf, khônghuman/hair/ears. Không lấy nguyên ảnh portrait278 cũ làm endpoint hoặc mặc định khớp mặt mới.
Đây chỉ **giả thuyết kiểm soát input**, dựa take280 đã giữ dạngfoodcharacter; không cam kết action đạt. Cần duyệt scope chuẩn ảnh/gói mới, reviewfullcontext và quote trước request. Không tự sinh ảnh mới/tự chạyvideo hoặc mởreserve trong REC302.
Phần tạo lại còn 5 credit, thấp hơn báo giá 7 credit của cùng cấu hình. Nếu muốn thêm một lượt 7 credit, owner cần chốt phân bổ ngân sách trong trần 500; không tự lấy từ phần tạo mới 82, hậu kỳ 45 hoặc dự phòng 110 để vượt giới hạn phần tạo lại. Chưa xin chi khi đầu vào chưa chuẩn.
Một hướng khác là xét đổi cơ chế ràng buộc hình/voice sau nghiên cứu hiện hành, nhưng đó là thay workflow, không tự triển khai/tách hoặc thay giọng.

**Đã xác định:** một lượt 7 credit đã chạy, tải và kiểm; ảnh đầu vào đúng nhưng video gốc sai nhận diện Đào, cốc và phân công tay. **Quyết định:** root loại, không tự chạy lại, không dùng làm đầu vào C08 hoặc thay bản dựng chính. **Giả định:** hai neo có thể giảm sai lệch nhận diện nhưng chưa được chứng minh riêng. **Còn mở:** gói sửa nhận diện, ngân sách tạo lại, lỗi món ở điểm nối và thời lượng cuối. **Bước tiếp:** owner chốt hướng chuẩn đầu vào chưa trả phí; chỉ trình lượt mới sau khi kiểm đủ.
