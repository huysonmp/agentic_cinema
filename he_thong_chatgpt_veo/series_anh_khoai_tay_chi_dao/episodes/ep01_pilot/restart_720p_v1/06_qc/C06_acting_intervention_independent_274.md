# REC274 — Phản biện độc lập: can thiệp diễn xuất C06

Ngày 12-10-2026. RUN_ID: REC274-C06-ACTING-DIAGNOSIS-INDEPENDENT. Trạng thái: **DIAGNOSIS_ONLY / NO_GENERATION_APPROVAL / C06_NOT_SELECTED / C07_HOLD**.

Owner “ok nhé” được hiểu là tiếp tục chẩn đoán, không duyệt T02, T03, đổi voice hoặc thay coverage. Báo cáo này chỉ đề xuất và kiểm ranh giới quyết định; không sửa prompt, ảnh, media hoặc báo cáo273.

## Nguồn và phạm vi thực kiểm

Đã đọc đầy đủ: T01 prompt269, T02 prompt273, owner acting-A273, hai báo cáo actual độc lập271/273 của reviewer này, `03_voices/recreation-blueprint.md`, `03_voices/bindings-238.json` và scoped-autonomy238. Không đọc maker274.

Targets giữ nguyên:

- T01 native SHA-256: `a07433e358a2fa2fa946f51069dc2dc5304609c0a1625216c100d46c6bc775b7`; prompt269: `881cb9a14db21f427c5c13e451e5c5852d40febf9dc178b3d2c24930e1eca940`.
- T02 native SHA-256: `a2422a7e827ef80be3b95ff07335bd66e8ec1207d14af64a3763098e90c91b6a`; prompt273: `cbe71e5a5a2085a2d6f27723a230dd5e6707659aa08ae436b3787782348db5b4`.
- START chính xác từ C05 T02 F65: `f091e35fc7c779591c918c47ba34752a8a2c3b30de507cd99dc0e76143e83196`.

Trong lượt274, reviewer trực tiếp xem lại START, T01 F30/F143 và T02 F24/F42/F95 ở các thư mục QC271/273. Phạm vi trực tiếp lượt này là **SIX_FULL_FRAME_STILLS_NOT_AV**. Kết quả xem đủ144 khung T01 và96 khung T02 đã ghi trong reports271/273, không tự gọi là đã xem lại toàn bộ trong lượt274. Không nghe voice hoặc phát AV; không browser/web/API/credit/git/script/media/new tool.

## Những điều có bằng chứng và những điều mới là giả thuyết

### 1. Cue “cười một khóe cuối câu” có kéo nụ cười vào lời không?

Có lý do để kiểm giả thuyết đó: T02 chỉ yêu cầu nâng một khóe rất nhẹ ở cuối “mà”, nhưng ảnh F24/F42 đã có cả hai khóe nâng trong nhịp nói. Model có thể diễn giải nét cười như trạng thái chung của lượt, thay vì mốc cục bộ. Chỉ đạo “offered-but-not-yet-received” và hành động cho người bên cạnh cũng có thể góp phần gợi một trạng thái thân thiện chủ động.

**Chưa có bằng chứng nhân quả.** T01 chưa có cue nâng một khóe rõ như T02 nhưng vẫn cười vui khi nói và cuối cảnh. Vì vậy cue này không phải điều kiện cần để phát sinh lỗi, và chưa chứng minh bỏ cue sẽ sửa được. Giữa hai take còn đổi thời lượng, entry, thứ tự tay, clearance, mức neo cốc và nhiều câu mô tả. Không được gọi chúng là phép A/B một biến hoặc quy mọi khác biệt cho cue cười.

Kết luận có thể giữ: START không cười; T02 giữ entry khá đúng nhưng nét mặt phát triển thành cười trong lời. Lỗi quan sát được nằm ở **diễn xuất được sinh trong source**, không phải chỉ điểm nối, ảnh đầu hoặc lỗi ghép.

### 2. Blueprint “lấy lại tự tin ở cho em” có chứng minh xung đột voice–hình không?

Không. Blueprint K20 đồng thời yêu cầu ngượng đáng mến ở cuối “mà”, không tán tỉnh, không nũng nịu; điều này vẫn tương thích với người đang chữa cháy. Lấy lại tự tin có thể là ổn định nhịp và cách nói, không đòi cười vui. T02 prompt cũng yêu cầu nói tỉnh và hơi ngượng, không vui vẻ mời.

Một giả thuyết cần kiểm là output voice có thực trở nên vui/chủ động khiến hình đi theo hay không. Reviewer chưa nghe T01/T02 và chưa có bằng chứng về cơ chế model phối hợp preset với diễn mặt, nên không kết luận “giọng gây cười” hoặc “preset sai”. Saved K20 được owner chốt là identity phải giữ; không sửa preset để chữa lỗi mặt dựa trên chữ “tự tin”.

Kiểm nghe do owner trên đúng source có thể phân biệt **giọng nghe hợp** với **giọng vui quá**. Kết quả đó vẫn không tự chứng minh cơ chế nhân quả hoặc lip sync, nhưng giúp chọn tầng can thiệp. Không yêu cầu tuyển lại giọng hay thử mười mẫu.

### 3. Bảo toàn hình học vẫn là điều kiện, không phải mục tiêu đã xong vĩnh viễn

T02 đã giữ cốc nâng, bát riêng rỗng và A còn kẹp suốt phần ảnh kiểm. Phải giữ các ràng buộc đó trong phương án sửa; không chuyển cốc sang chỗ khác hoặc bỏ Đào/bát khỏi khung để giảm nhiệm vụ. Thành công một take không chứng minh độ tin cậy tuyệt đối của phương pháp. Lỗi mặt không được giải bằng che mặt người nói hoặc insert đĩa nem.

## Tối đa ba phương án can thiệp

| Phương án | Cơ chế dự kiến và lợi ích | Rủi ro / điều kiện / authority |
|---|---|---|
| **A — Bỏ cue cười; thể hiện ngượng bằng mắt, mày và nhịp** | Giữ nét mặt từ START, nhìn Đào, khựng ngắn; nói bình thản với má thả lỏng; sau lời vẫn chờ phản ứng, chuyển SAME A. Không ra lệnh một khóe môi phải nâng. Giảm một tín hiệu cảm xúc có thể bị lan ra toàn lượt; không đổi K20, lời, hai-shot hoặc hình học. **Khuyến nghị ưu tiên để trình owner, không phải đã duyệt chạy.** | Bỏ nét nhếch cuối khác với chỉ đạo ownerA273, nên cần owner chấp thuận rõ. Mặt có thể quá buồn hoặc thiếu hài; phải giữ nét bị bắt gặp, không khóc/ủ rũ. Không cấm thấy răng khi phát âm bình thường. Sau STOP cần quyền mở lại một can thiệp có mục đích; không tự T03 dưới ngân sách cũ. Actual phải kiểm cả diễn, cốc/bát, A, voice/AV và seam. |
| **B — Neo đúng START mạnh hơn, giữ mô tả diễn** | Dùng START hiện đã duyệt làm entry bắt buộc; nhấn giữ quan hệ mắt–mày–má từ entry qua lời, không tái dựng thành người mời món vui vẻ. Có thể bảo vệ entry mà không đổi thiết kế hay voice. | START hiện đã tốt trong T02, nhưng lỗi xảy ra khi nói: chỉ thêm “preserve reference” có thể không tác động tầng lỗi. Không gọi ảnh tĩnh là khóa mặt xuyên video. Nếu định chuyển route hoặc dùng endpoint/ref mới, chưa xác minh feature → **HOLD**, phải có kiểm khả năng thực và owner duyệt ảnh/coverage thay đổi. Chỉ sửa lời mô tả trên giấy root được làm; sinh mới sau STOP cần quyết định. Không đề xuất ảnh môi khép làm endpoint bắt mọi frame nói phải khép môi. |
| **C — Tách lượt nói và chuyển tay thành hai đoạn** | Đoạn đầu rõ mặt Khoai nói, props giữ; đoạn sau thực hiện SAME A chuyển tới bát. Giảm số nhiệm vụ đồng thời và cho kiểm diễn / chuyển động riêng. Không dùng món ăn thay mặt khi N06 đang nói. | Thay coverage và cấu trúc hiện hành; tăng điểm nối, công việc và khả năng cần thêm lượt/credit. Có thể bị đứt chữa cháy và nhịp gắp; geometry phải nối đúng cốc, bát, A, ownpair. Không mặc định ghép voice riêng được hỗ trợ, không mặc định route giữ saved K20 hoặc clip ngắn có giá cụ thể. Khả năng công cụ và quote chưa xác minh → **HOLD**. Cần owner chốt coverage mới; đổi workflow voice/tool phải có quyền riêng. |

Phương án A và B không nên trộn âm thầm thành nhiều thay đổi rồi gọi là một biến. Có thể giữ cùng reference/geometry như control chung, nhưng việc bỏ cue cười và việc đổi route/endpoint là hai can thiệp khác nhau. Phương án C chỉ đáng mở khi can thiệp diễn trực tiếp chưa đủ hoặc owner chọn chủ động đổi cấu trúc; chưa có bằng chứng nó rẻ hơn hoặc chắc đạt hơn.

## Ràng buộc thời lượng và ngân sách

Qua C05 đã chọn là 26,333 giây; trần rough hiện được duyệt là35 giây. Toàn bộ C06–09 chỉ còn **8,667 giây**. Nếu C06 dùng đủ4 giây, C07–09 còn **4,667 giây**. Đây là khoảng thời gian cần đo thực, không phải bằng chứng các cảnh còn lại sẽ vừa. Tách C06 không mặc định tăng tổng thời lượng; phải có source-range/beat timing đủ N06, N07, nhận bát, thả A và kết bằng B. Không tự bỏ lời, rút phản ứng quan trọng hoặc tăng trần35 giây.

Ledger gần nhất ghi180/500, còn320; retake còn73, first-pass92, post-rough45; reserve110 đóng. Số còn lại không bỏ quy tắc STOP hoặc tự cho phép chi. Native720p, x1 và live quote≤15 vẫn là giới hạn; chưa có quote mới cho các phương án, không ghi dự báo chi cụ thể như giá đã xác minh.

## Root có thể làm ngay, và điều owner cần chốt

Root có thể thực hiện phần local đã được giao: bảo toàn nguồn và trạng thái STOP, đối chiếu prompt/ref/reports, soạn phương án giấy với giả thuyết và tiêu chí, lập timing từ nguồn hiện có, đọc đầy đủ report độc lập và trình gọn các quyết định. Không cần owner tự tìm lỗi kỹ thuật, đọc mọi report hoặc chuẩn bị ref thay root. Scope274 chưa mở browser/tool mới; việc xác minh live phải do root ở scope có quyền, không được ghi đã xác minh trong báo cáo này.

Owner cần chốt những thay đổi thật sự: (1) có bỏ nét nhếch cuối để thử A hay giữ nguyên hướng hiện tại; (2) nếu chọn C, có chấp nhận coverage hai đoạn; (3) có mở lại một lượt sau STOP với target và cap cụ thể. Đổi K20, tools, preset, route ảnh mới làm thay đổi creative/voice workflow, tăng trần thời lượng hoặc mở reserve đều phải xin quyền đúng phạm vi. “ok nhé” ở đầu274 không chốt những việc đó.

Không đề nghị owner trả lời cả ba phương án cùng lúc khi chưa cần: **trình A trước, giữ K20 và toàn bộ geometry; B là đường giấy có hạn chế, C là phương án dự phòng cần feature/timing proof**. Khi owner chọn, root đóng exact current-final hash, paper review và live gates trước mọi chi. Không có lựa chọn nào trong báo cáo này là media quality PASS hoặc bảo đảm xác suất đạt.

## Tổng hợp vòng

Đã xác định: lỗi cốc T02 được kiểm là không lặp trên ảnh; lỗi diễn khi nói còn lặp và đã chặn. Đã chốt trước đó: giữ nhân vật, K20, lời N06, geometry và trần rough35 giây. Giả thuyết làm việc: cue nét cười có thể gây lan trạng thái, nhưng T01 chứng minh vấn đề không chỉ xuất hiện sau cue ấy. Còn mở: sắc thái tiếng actual, hiệu quả từng can thiệp, khả năng route/timing nếu tách đoạn. Bước tiếp: root tích hợp, trình owner quyết định về phương án A; chưa sinh thêm, chưa mở C07.
