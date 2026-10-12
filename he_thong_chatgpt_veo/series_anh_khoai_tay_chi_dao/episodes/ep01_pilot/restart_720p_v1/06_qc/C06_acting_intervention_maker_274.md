# REC274 — Chẩn đoán diễn xuất và phương án can thiệp C06

Ngày 12-10-2026. RUN_ID `REC274_C06_ACT_DIR_DIAGNOSIS_MAKER`. **LOCAL_DIAGNOSIS_ONLY / NO_GENERATION / C06_NOT_SELECTED / C07_HOLD.** Owner “ok nhé” đồng ý tiếp tục chẩn đoán, không duyệt T02, T03, đổi giọng hoặc coverage. Đây là đóng góp ACT/DIR của maker, không phải phản biện độc lập. Không sửa báo cáo273 hoặc media.

## Nguồn và phạm vi đã kiểm

Đã đọc đầy đủ prompt T01 `04_requests/C06_T01_prompt_269.txt`, tự hash `881cb9a14db21f427c5c13e451e5c5852d40febf9dc178b3d2c24930e1eca940`; prompt T02 `04_requests/C06_T02_prompt_273.txt`, tự hash `cbe71e5a5a2085a2d6f27723a230dd5e6707659aa08ae436b3787782348db5b4`; owner273; maker actual273; `03_voices/recreation-blueprint.md`; `03_voices/bindings-238.json`; scoped238.

Trực tiếp xem lại **ảnh nguyên khung** START từ C05 F65; T01 F30/F44; T02 F24/F43/F95. Đường dẫn ảnh T01: `C:/Users/PC/Downloads/du_an_nem_bui/269_C06/C06_T01_QC_271/all_native_frames/`; T02: `C:/Users/PC/Downloads/du_an_nem_bui/273_C06_T02/native_qc/all_native_frames/`; file index = F+1. Lượt274 chỉ kiểm các ảnh mẫu trên, không nhận đã xem lại toàn96/144 khung. Báo cáo273 đã có kiểm đủ96 trong lượt trước, với native T02 hash `a2422a7e827ef80be3b95ff07335bd66e8ec1207d14af64a3763098e90c91b6a`.

Không nghe thực tế, không xem AV liên tục, không dùng ASR để xác nhận giọng/nhịp/lời/khớp miệng. Không đọc critic274; không trình duyệt, web/API, chi credit, git, thêm công cụ/script hoặc sửa media.

## Đã chứng minh đến mức nào?

**Quan sát trực tiếp:** START có môi hơi cụp và ánh nhìn Khoai về Đào. T01 F30/F44 và T02 F24/F43 có miệng mở ngang, cả hai khóe nâng, răng đi cùng nét cười; T02 F95 vẫn mỉm cười hai khóe khi giữ A. Trong273, đầu T02 đã bớt vui và cốc/bát giữ đúng, nhưng diễn cười trong phần nói vẫn lặp. Lỗi biểu cảm nằm ở native, trước dựng; không thể chữa bằng cắt đuôi mà giữ nguyên toàn lời/hành động.

**Đã chứng minh bằng đối chiếu input:** T01 đã cấm “broad grin or laugh” và yêu cầu lời chữa cháy hơi ngượng. T02 thêm kiểm soát má, khóe và nhịp, nhưng vẫn không giữ đúng mức cười. Vì vậy không thể quy lỗi là thiếu một câu cấm hoặc coi prompt sửa rõ hơn là bằng chứng đã chữa source.

**Chưa chứng minh nguyên nhân sinh bên trong model:** chưa tách được ảnh hưởng của ngữ nghĩa mời món, cử chỉ tay, tương tác với Đào, preset giọng, độ dài hay mật độ prompt. T01→T02 đồng thời thay thời lượng và nhiều chỉ dẫn; không có thử nghiệm kiểm soát để suy nguyên nhân duy nhất.

## Cue nào có thể cạnh tranh với ý định chữa cháy?

| Cue đã có trong input | Giả thuyết liên quan | Giới hạn kết luận / cách xử lý |
|---|---|---|
| Câu “Anh gắp cho em mà”, đưa món sang bát bạn, bữa ăn yên tĩnh của hai người trưởng thành | Model có thể diễn theo khuôn “mời bạn ăn thân thiện”, thay vì “bị bắt gặp rồi chữa cháy”. Đây là giả thuyết về ý nghĩa xã hội, phù hợp nụ cười lặp khi nói và đưa món. | Không chứng minh model hiểu câu theo cách này. Không đổi câu, không biến quan hệ thành cặp đôi hoặc bỏ chuyển đích. Cần nhấn ý định giữ thể diện bằng hành vi cụ thể, không chỉ tính từ “embarrassed”. |
| Đào nghe với nét hiểu chuyện, mắt về Khoai/A; vẻ mặt mẫu có nét mỉm cười | Tương tác ấm áp có thể kéo Khoai đáp bằng nụ cười qua lại. | Không có phép thử chỉ đổi phản ứng Đào. Không tự làm cô nghiêm/khó chịu để ép Khoai; nét biết chuyện của cô thuộc câu chuyện. |
| T02 yêu cầu một khóe môi nhích rất nhẹ cuối “mà” | Model có thể khuếch đại cue cười hoặc kéo nó sớm vào khẩu hình. Việc đồng thời bắt khẩu hình nói và bất đối xứng khóe cũng là mục tiêu khó điều khiển. | **Không phải nguyên nhân gốc của cả hai take:** T01 chưa có cue “ONE mouth corner” nhưng đã cười. Chỉ xem đây là giả thuyết khuếch đại hoặc biến can thiệp có thể bỏ để giảm cạnh tranh. |
| K20 trong blueprint: ấm, tự trêu; câu cuối lấy lại tự tin ở “cho em”, kết “mà” thấp, ngượng đáng mến | Nét tự tin/ấm có thể liên quan biểu cảm thân thiện nếu model kết hợp voice và hình; cũng có thể hoàn toàn phù hợp chữa cháy. | Blueprint đã chỉ rõ “kết mà thấp”, hơi ngượng, không tán tỉnh. Chưa nghe T01/T02 và chưa chứng minh preset gây nụ cười. **Không kết luận voice sai hoặc sửa preset.** Giữ K20 đã chọn; kiểm actual tiếng riêng. |

## Tối đa ba phương án can thiệp

### 1. Giữ một shot, bỏ cue nhích khóe; chuyển nét ngượng sang mắt, mày và nhịp — ưu tiên sơ bộ

Giữ nguyên K20, câu thoại, START, set, camera, cốc nâng, hai bát và một A. Khoai khựng ngắn; mắt thoáng về A rồi gặp Đào; phần trong mày căng/nâng rất nhẹ; má thư giãn; nói để giữ bình thản. Không chỉ đạo một nụ cười mới trong hoặc cuối câu. Sau âm cuối, môi khép, ánh mắt chờ câu trả lời rồi tay chuyển A; không dùng từ gợi “đáng yêu” hoặc “thân thiện” làm cue biểu cảm hình.

Đây là **đổi micro-cue đã được owner273 chốt**, không phải quyền maker tự sửa. Owner cần duyệt bỏ riêng nhịp một khóe, vẫn giữ đích trầm, hơi ngượng, hài tinh tế. Lý do ưu tiên: giữ đường sản xuất đơn giản hiện có, giảm một mục tiêu vận động miệng cạnh tranh với phát âm, không đổi giọng hoặc bỏ câu chuyện. **Không hứa sẽ hết cười**, vì T01 đã không có cue ấy nhưng vẫn lỗi; cần xem đây là một can thiệp có giả thuyết, không “sửa đúng nguyên nhân đã chứng minh”.

Lời→tay→bát giữ nguyên: bắt đầu lời trước tay, chuyển A sau âm cuối, dừng còn kẹp trên phía Khoai của bát Đào, chưa thả; Đào chưa chuẩn bị nhận bát cho tới C07. Không đổi đầu shot sang A đang ở bát. Nếu đường4s hiện hành còn hỗ trợ và quote vẫn7, một lượt có thể là7 credit, nhưng **giá mới phải kiểm live**, không tự dùng giá cũ hoặc autoT03 sau STOP.

### 2. Giữ cue một khóe, tăng neo tham chiếu diễn — bảo toàn lựa chọn nghệ thuật chặt hơn

Giữ micro-cue owner273: cuối “mà” chỉ một khóe nhẹ. Chuẩn bị neo biểu cảm trước/sau lời và trạng thái A gần bát, giữ tất cả nhân vật/đạo cụ; yêu cầu owner duyệt ảnh neo nếu phải tạo/chỉnh ảnh. Không lấy F24/F43 của T02 làm chuẩn biểu cảm vì chính đó là lỗi. START hiện tại đã mang nét caught đúng, nên thêm neo cần thể hiện giá trị mới — **chỉ gắn lại START không phải can thiệp mới**.

Nếu route hỗ trợ điều khiển khung bắt đầu/kết hoặc nhiều tham chiếu mà vẫn dùng saved K20 và giữ speech/action, đó có thể giảm tự diễn ở đuôi. **Chưa xác minh route hỗ trợ đồng thời các điều kiện này**, không nhận có thể “khóa mặt” bằng ảnh, và không lấy ảnh cuối đẹp làm bằng chứng quá trình nói đạt. Phát âm vẫn có thể kéo cười giữa shot dù endpoint đúng.

Hệ quả: bảo toàn ý đồ một khóe và lời→tay→bát, nhưng phải có input mới được duyệt, nghiên cứu khả năng route hiện có và quote trước sinh. Nếu buộc đổi route mà không gắn K20 được, phương án chưa sẵn sàng. Không thay bằng giọng nền hoặc VO off-screen để vượt hạn chế. Số lượt/credit chưa tính chắc khi route chưa xác minh; không tự dùng model mới hoặc reserve.

### 3. Tách lời chữa cháy và động tác đưa món — chỉ dự phòng khi cần giảm coupling

Shot lời vẫn thấy mặt Khoai đang nói và Đào nghe; A đứng ở phía Khoai. Shot sau bắt đầu đúng trạng thái ấy, Khoai đã khép môi, tay đưa một A sang bát Đào; cốc/bát giữ trạng thái. Tiếng chỉ thuộc shot mặt nói; **không che người nói bằng cảnh món ăn** hoặc dùng toàn cảnh bát để chữa lỗi khẩu hình. Mục đích là tách diễn miệng khỏi tay, không chia nhỏ để bỏ nhiệm vụ.

Hệ quả: ít mục tiêu đồng thời hơn, nhưng thêm điểm nối và nguồn media; phải kiểm eye-line, độ cao A, tay, cốc/bát, nhịp sau lời và single voice. Nếu phần lời riêng vẫn cười, tách tay **không giải quyết ACT**. Muốn tận dụng tay T02 phải tìm điểm vào đủ continuity và kiểm source/range/join mới; không mặc định được cắt hình lỗi rồi gọi wholeC06 đạt. Hai lượt mới có thể tốn nhiều hơn một lượt; giả định hai quote7 sẽ là14 credit, **chỉ là dự toán từ giá273, không giá live hay quyền chạy**.

Đổi coverage cần owner chốt; nếu cần công cụ, voice pipeline hoặc route khác, tiếp tục cần quyền riêng. Chưa xác minh route sinh phần tay không thoại và giữ các điều kiện trong cùng workflow. Không mở C07 từ candidate chưa chọn.

## Timing và ngân sách không được che bằng dự toán

C05 đã chọn đủ632 khung =26,333333s. Trần rough đã được duyệt là35s, còn208 khung =8,666667s cho C06–09. C06 nguyên4s sẽ đưa phim tới30,333333s, còn4,666667s cho C07–09. Ước lượng cũ của ba cảnh cuối khoảng6,5s, tức thiếu khoảng1,833333s so ước lượng nếu giữ fullC06; **chưa phải actual overrun đã đo**, vì ba cảnh sau chưa sản xuất/chọn.

Phương án1/2 giữ một shot không tự thêm cut hoặc tổng thời lượng. Phương án3 có thể chọn tổng lời+tay khoảng3–3,5s nếu actual trọn nhiệm vụ, nhưng đó là giả định kiểm, không chứng minh hai clip native4s có thể cắt đủ lời/beat xuống số ấy. Không ép giọng nhanh, cắt âm cuối, bỏ đưa bát/thả A/kết B hoặc xin nới35 một cách ngầm. Cần bảng timing có điều kiện trước request; actual mới thắng dự toán.

Sổ273: đã dùng180/500, còn320; còn retake73, first-pass92, post-rough45, reserve110 **đóng**. Giới hạn từng video output≤15, x1, native720p; không mua/topup. Same-major hai lần đã dừng, nên còn ngân sách **không tự mở T03**. Lượt274 này chi0; mọi giá7/14 ở trên chỉ minh họa quy mô dưới điều kiện live, không allocation hoặc approval mới.

## Khuyến nghị và quyết định cần chốt

Ưu tiên sơ bộ **phương án1**, vì giữ một shot/giọng/set và tập trung nét ngượng ở hành vi mắt–mày–nhịp, nhưng phải nói rõ **T01 không có cue một khóe vẫn cười**: việc bỏ cue không bảo đảm chữa được lỗi. Phương án2 hợp khi owner coi micro-cue một khóe là bắt buộc và route thực sự hỗ trợ neo mới; phương án3 chỉ khi cần tách coupling hoặc phương án giữ single shot không khả thi, không phải giải pháp chắc thắng.

Root tổng hợp với phản biện độc lập rồi hỏi owner chọn **giữ hay bỏ cue một khóe, và có cho phép coverage tách hay không nếu route không hỗ trợ neo**. Không hỏi lại giọng, câu thoại hoặc nhân vật đã chốt khi chưa có bằng chứng buộc đổi. Sau quyết định: khóa can thiệp/version, kiểm route/input/quote và bảng timing, xin mở lại một request cụ thể sau STOP, rồi kiểm actual đủ scope. Chưa có T03; T01/T02 không được duyệt; C07 vẫn HOLD.
