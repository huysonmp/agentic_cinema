# CINE-LIGHT — EP01 V01 R1

2026-10-01. Run `EP01-CINE-R1`; independent reviewer; scope `MEASURED_MEDIA_EVIDENCE` giới hạn ở xem still/frame samples và `PAPER_EDIT_PLAN` review thiết kế. Không full playback, không nghe. Status `REVIEW_RESPONSE_COMPLETE / NEED_MORE_EVIDENCE`; không production pass hoặc take approval.

## Authority, inputs và trình tự độc lập

Chỉ local read/view và tạo report này bằng apply_patch theo dispatch. Không browser/API/credit/generation, media edits, Git hoặc quyết định mới thay owner. Không đọc report reviewer khác, file91/92/93 hoặc root verdict. Các mục self-review trong source79/81 là nội dung bắt buộc đọc sau cold pass; không dùng chúng làm bằng chứng quality PASS.

Đã đọc toàn bộ `09_cinematography-lighting-critic-contract.md` và `02_contract-and-role-prompts.md` trước task. Đã thực xem bằng `view_image`, theo thứ tự trước khi đọc script/approval:

1. `C:/Users/PC/Downloads/du_an_nem_bui/T-NB-03_v0.8.jpg`.
2. `C:/Users/PC/Downloads/du_an_nem_bui/V01_native_1sec.png`.
3. `C:/Users/PC/Downloads/du_an_nem_bui/V01_visual_2fps.png`.

Sau đó đọc đầy đủ episode32 C-v0.5,78 static-reference approval,79 shot draft,81 boundary addendum,84 coverage/choreography approval và85 exact Vietnamese voice-probe request. Output tổng lần đọc đầu bị truncate ở79; đọc lại riêng79 và81 đầy đủ trước kết luận. Không mở linked sources ngoài allowlist.

Dispatch mô tả contact sheet là16 samples trong192 frames, t=0..7.5s bước0.5s; tôi dùng mapping row-major4×4 này để ghi thời điểm. Không tự đo duration/fps/frame count hoặc xác thực provenance/hash của PNG/video. Tool hiển thị contact sheet giảm từ1440×2560 xuống1152×2048; chi tiết nhỏ không được coi như native inspection. Ref hash/kích thước trong78 là evidence tài liệu, chưa kiểm lại bytes ở lượt này. Không có actual video playable/audio, V02, các shot sản xuất khác, boundaries giữa các clip, export caption/safe-zone hoặc photometric measurement trong phạm vi xem.

## Cold descriptions — trước đối chiếu tài liệu

**Ref v0.8 riêng:** portrait hai nhân vật hình củ/quả ngồi cùng phía bàn gỗ, người lớn hình khoai bên trái áo tối và sơ-mi sáng, hình đào bên phải sơ-mi sáng, lá xanh trên đầu. Hai mặt và mắt đọc rõ; tay đặt gần hai bát. Đĩa đồ ăn beige giữa tiền cảnh, lá xanh trái, hai chén chấm, đũa và cốc nước ngoài phải. Phố/quán nhiều người, xe máy, đèn lồng và bóng đèn ở hậu cảnh mờ. Tông ấm; áo tối tách nhờ sơ-mi và mặt sáng. Bàn/ghế gỗ tiền cảnh và không gian phố phía trên chiếm đáng kể khung; mặt và món là cụm focus, nhưng đèn/nền vẫn có điểm hút mắt. Không thể suy chất lượng chuyển động từ ảnh này.

**Native1s riêng:** cùng arrangement nhìn từ trước bàn. Khoai quay mắt về phía Đào, miệng mở, một bàn tay nâng gần ngực; Đào nhìn về phía anh, cười nhẹ, tay gần bát. Đĩa/lá/chấm/cốc nhìn rõ. Hậu cảnh phố có xe/người, chi tiết mềm hơn chủ thể; hai mặt và món giữ tông sáng ấm. Có chữ `Khoai` ở đáy trái và dấu nền tảng ở đáy phải. Không biết lời đang phát, đúng voice/sync hay không từ still.

**Contact sheet riêng:**16 khung cho thấy thay đổi miệng/mắt và tay Khoai, Đào hướng chú ý về anh trong nhiều mẫu. Xe/người hậu cảnh đổi vị trí. Bố cục tổng thể và vị trí bàn/hai nhân vật nhìn ổn định ở mức mẫu; không thấy cut rõ trong các samples. Các mẫu có miệng đóng/mở, mắt nhìn lên/nhắm là pose rời, không tự chứng minh diễn xuất tự nhiên hoặc nhịp. Không thấy thao tác gắp/ăn/trao món trong các mẫu; không kết luận toàn video không có thao tác đó.

## Capability và coverage

| Scope | Evidence thực | Coverage / giới hạn |
|---|---|---|
| Composition/visual hierarchy | Ref, native1s,16 samples | MET cho mô tả thấy mặt/món/props; aesthetic concern ở khung rộng, không điểm đẹp/retention |
| Light readability | Quan sát màu, mặt/mắt/món trong ảnh | MET ở still/mẫu: đọc được; exposure, CCT, lens, light ratio thực UNKNOWN |
| V01 staging | Native1s và samples | MET cho đọc vị trí hai người/tay trong mẫu; giữ action đơn giản trong mẫu; all-frame compliance UNKNOWN |
| Causal action S04/S05 |32/79/81/84 trên giấy | N/A cho V01; actual reach/contact/đổi hướng/nhận bát UNKNOWN |
| Camera/motion |16 sparse samples | Không thấy thay đổi framing lớn trong mẫu; full playback, flicker, jitter, temporal deformation UNKNOWN |
| Cut readiness | Một clip được sample; paper joins79/81 | UNKNOWN actual inter-shot continuity; paper specification có, không transition PASS |
| Voice/lip-sync/ambience | Không nghe/playback | UNKNOWN, route AV; không đoán từ miệng mở hoặc prompt |
| Captions/render | Native1s actual chữ `Khoai` | DEFECT so no-caption85 ở asset sample; export layout/master UNKNOWN |
| Production/owner selection |78/84/85 + sample | NEED_MORE_EVIDENCE; static approval giữ nguyên, không tự chọn take |

## Findings

Severity là tác động trong đúng scope, không chấm điểm đẹp. Timestamp dưới đây dùng dispatch mapping, không measured audio timecode.

| ID / loại / severity | Asset/time, expected → observed / method / certainty | Action, stage/owner và closure |
|---|---|---|
| CL01 / confirmed constraint defect / MINOR | `V01_native_1sec.png`, t=1s:85 yêu cầu `No added people, captions, music or narration`; native frame có chữ `Khoai` ở đáy trái. Confirmed visual bằng xem native still; không biết chữ tồn tại suốt clip hay do upstream extraction/overlay. Watermark là phần được yêu cầu giữ, không defect. | P9/P11 + AV/MASTER/root đối soát native video và provenance PNG để xác định chữ baked-in hay overlay extraction. Nếu nằm trong video, giữ V01 làm diagnostic có exception hoặc chuẩn bị phương án xử lý ở revision đúng quyền trước dùng clip sản xuất. Closure: actual source playback/native frames và version sạch nếu cần, không xóa watermark. Không tự crop/generate. |
| CL02 / aesthetic concern / MINOR | Ref v0.8 và V01 t=1s, contact sheet0..7.5s: cả mặt/món rõ, nhưng khoảng phố phía trên và ghế gỗ phía dưới rộng; mắt còn bị hút bởi đèn/người/xe phía trên. Expected là visual hierarchy hỗ trợ đối thoại/ký ức. Đây quan sát bố cục và preference, không vi phạm static approval78 hoặc chứng minh hiệu suất khán giả kém. | P7/SHOT/ART: proposal framing gần hơn cho shot cần đọc mặt, giữ hai mặt, đường tay/bát, toàn món/lá/chấm/cốc/watermark theo84. Owner xem version đề xuất trước thay baseline. Closure: review frame/crop version mới trong bối cảnh shot thực, không gỡ approved v0.8. |
| CL03 / aesthetic concern + temporal UNKNOWN / MINOR | V01 t=1s và samples khoảng1..3.5s: tay Khoai lên gần ngực và gesture trong khi prompt85 nói `Only subtle natural facial movement and speech`. Gesture không cầm đũa/food trong mẫu; có thể hỗ trợ đối thoại, cũng có thể kéo chú ý khỏi câu ký ức. Không gọi là confirmed forbidden utensil action, không suy tốc độ/intensity từ still. | PERF kiểm fullplayback ý nghĩa gesture; SHOT cân nhắc giữ tay gần bát trong future voice diagnostic nếu gesture cạnh tranh việc nghe. Closure: playable V01 và xác nhận owner/reviewer trong scope; không sửa hình để chữa chất giọng. |
| CL04 / UNKNOWN / MAJOR cho scope motion | V01 samples0..7.5s: framing/light tổng thể nhìn nhất quán trong mẫu, không chứng minh giữa mẫu không flicker, warp, jerk hoặc zoom. Expected85 locked camera và chuyển động mặt tự nhiên; chưa đủ evidence đóng gate. | CINE-LIGHT/CONT/PERF nhận playable actual V01 đúng version, xem liên tục; AV riêng sync. Closure: version-specific fullplayback report với mốc lỗi nếu có. Không gắn technical PASS từ contact sheet. |
| CL05 / UNKNOWN / MAJOR cho cut/production | Actual chỉ V01 diagnostic hai câu Khoai;85 chủ ý không thử ăn vụng. S04 causal A approved84 cần thấy plate→miệng chưa contact→Đào bắt gặp→đổi hướng→bát. Không có actual các shot/boundary/transfer. | P7/P8/CONT/PERF/EDIT: dùng action-specific starts/ends79/81 và bounded probe đúng quyền ở vòng sau. Closure: actual coverage và real joins đúng version với face/food path/eye-lines/light đọc được; không dùng V01 làm final action take. |

Không có confirmed lighting/exposure defect trong ảnh đã xem. Hai mặt/mắt và món được phân biệt với nền; có phần dưới bàn tối nhưng không phải khu vực hành động probe cần đọc. Không suy lamp direction thực, nhiệt độ Kelvin hoặc highlight clipping từ viewer chưa đo.

## Ba phương án sửa/tiếp tục — proposals, không thực thi

1. **KEEP V01 cho voice diagnostic với exception CL01 ghi rõ.** Giữ visual baseline78, nghe/đo tiếng và kiểm gesture/playback trước owner chọn voice. Nhanh và không phát sinh media ở vòng này; hạn chế là chữ hiện có và framing rộng không được chuyển thành production-ready. Khuyến nghị hiện tại vì mục tiêu85 là chẩn đoán tiếng.
2. **REFRAME proposal cho future shot/diagnostic:** giữ two-shot cùng phía trục, đặt trọng tâm hai mặt và món; giảm khoảng trống nền/ghế qua một version framing mới có đủ tay/cốc/bát/lá/chấm/watermark. Mặt đọc tốt hơn, giảm cạnh tranh hậu cảnh; trade-off mất không khí phố và có nguy cơ cắt vùng action/cốc/watermark nếu quá chặt. Không crop file hiện có ở lượt này; frame mới cần owner review theo78/84 và kiểm native export. Với S04 phải chọn khung theo toàn đường nem và mặt Đào, không theo portrait đẹp riêng.
3. **RELIGHT/staging proposal nhỏ chỉ nếu fullplayback xác nhận cạnh tranh nền:** giữ tông ấm đã duyệt, tăng phân tách thị giác bằng giảm độ nổi các điểm đèn/nền sau đầu hoặc bố trí điểm sáng nền sang vùng không tranh mắt; giữ mặt/món readable, tay trung tính khi chẩn đoán tiếng. Trade-off đổi appeal quán và có thể làm mất baseline light match giữa shot; cần version mới, approval và kiểm joins. Chưa đủ căn cứ ưu tiên relight ngay, không gọi exposure defect hay tiến hành generation.

Thứ tự khuyến nghị: phương án1 cho V01 hiện có; phương án2 cho thiết kế shot chức năng; phương án3 chỉ sau evidence động và owner quyết định aesthetic. Không cần đổi lời thoại/canon hoặc coverage A đã duyệt để xử lý các concerns này.

## Verdict theo scope

| Scope | Verdict |
|---|---|
| v0.8 static reference | KEEP theo lịch sử approval78; aesthetic concern không thu hồi approval |
| V01 sampled composition/light | KEEP cho diagnostic; REFRAME proposal cho shot cần mặt/action lớn hơn; không RELIGHT bắt buộc |
| V01 no-caption constraint | REWORK hoặc diagnostic exception pending provenance/owner; confirmed chữ trên native1s |
| Motion/voice/lip-sync | NEED_MORE_EVIDENCE; listening thuộc AV/owner, không tự nghe |
| S04/S05/actual cut readiness | NEED_MORE_EVIDENCE; V01 không kiểm choreography; paper A ưu tiên theo84, B dự phòng chưa tự chuyển |
| Production/export/take approval | HOLD_FOR_INPUT; không production PASS, tự approve hoặc retention claim |

## Năm probe oracle — expected responses, chưa fixture-qualified

Đã đọc năm probe trong contract09. Đây self-check đáp án hành vi kỳ vọng, không có independent fixtures, test execution hoặc root qualification ở lượt này; không claim fixture pass.

| Probe | Response kỳ vọng |
|---|---|
| Chỉ metadata/transcript | Hình/diễn xuất UNKNOWN; xin visual evidence, không chấm composition từ lời mô tả |
| Một still đẹp | Chỉ đánh giá still; flicker/motion/cut/fullplayback UNKNOWN |
| Approved ref không phục vụ shot mới | Giữ approval lịch sử; đề xuất crop/version phù hợp shot cùng trade-offs, không sửa canon/tự generate |
| Một clip chia rồi nối | Chỉ technical concat nếu có measured evidence; chưa narrative transition giữa cảnh khác nhau |
| Owner chê giọng | Ghi owner listening evidence với nguồn; không tự nghe, đổ lỗi Lite hoặc sửa visual để chữa voice |

## Handoff năm mục

1. **Đã xác định:** đã xem riêng ref/native1s/contact sheet trước script. Mặt/món đọc rõ trong samples; native1s có chữ `Khoai`; framing còn nhiều nền/ghế. Actual asset đang xét là voice diagnostic.
2. **Quyết định đã chốt:**78 v0.8 static warmth/layout giữ nguyên;84 A ưu tiên/B dự phòng và D2A staging trên giấy. Lượt này không quyết định take/crop/light mới hoặc generation.
3. **Giả định:** timing contact sheet theo dispatch row-major; PNG đại diện frame V01 nhưng provenance overlay chưa verified. Tông/khả năng đọc nhận xét bằng mắt, không số đo ánh sáng.
4. **Còn mở:** chữ nguồn video hay extraction; full motion/flicker/sync/listening; actual action coverage và clip joins; master/caption/export. Role chưa independently fixture-qualified.
5. **Bước tiếp:** root read-back scope/report; đối soát provenance chữ và nhận actual playback/listening evidence phù hợp. Giữ V01 để xét tiếng với exception, trình framing proposal khi shot thực cần; route action→P7/P8/CONT/PERF, audio→AV/P10/P11, final→MASTER/P12 + owner. Không retry/generate/crop/relight tự động.
