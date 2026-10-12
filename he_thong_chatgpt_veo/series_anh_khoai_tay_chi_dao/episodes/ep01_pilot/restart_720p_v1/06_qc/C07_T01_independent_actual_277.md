# REC277 — C07 T01: phản biện độc lập bản gốc

Ngày 13-10-2026. RUN_ID: REC277-C07-T01-INDEPENDENT-ACTUAL. Kết luận: **WRONG_PERSONAL_BOWL_MAJOR / REWORK / NOT_SELECTED / AUDIO_AV_HOLD / C08_HOLD**.

Đào di chuyển bát bên trái của Khoai, không chuẩn bị bát riêng bên phải của mình. Không có prefix hoàn thành đúng nhiệm vụ C07 để chọn. Cốc nâng và A còn kẹp không bù được lỗi chọn sai vật thể nhận.

## Target, quyền và phạm vi thực kiểm

Native: `05_native/EP01_720_C07_T01_NATIVE.mp4`. SHA-256 tự tính lại **`d1ed08ffca20e8bbee1455f14ed672fb4e2f538374a3ba209d6cfe49a195bfc0`**, khớp evidence/manifest. Owner copy: `C:/Users/PC/Downloads/du_an_nem_bui/277_C07_T01/C07_T01_NATIVE_720p.mp4`.

Đã đọc đầy đủ current final `04_requests/C07_T01_prompt_276.txt`, hash đã xác minh trong preflight là `ff869d873dbad96e81d323d770fb6f656274df691bf0136c1ae2a5f399b5353f`; preparation276, run277, approval `C05-C06-join-owner-acceptance-277.json` và scoped238. Preparation276 còn trạng thái lịch sử trước submit; run277 là nguồn trạng thái thực đã sinh, tải và đối soát chi. Owner đã duyệt đúng encoded C05→C06 join hash `42d826e1356ce67acc6e1057b4ceefc9703f3e705ffa14ae6c09dea7934b5bdf`, không duyệt output hoặc tiếng C07.

Đã đọc đầy đủ `C:/Users/PC/Downloads/du_an_nem_bui/277_C07_T01/native_qc/native_evidence.json` và `action_all/manifest.json`. Trực tiếp xem **tất cả18 board action_all_01–18.jpg, đủ144 khung F0–143**, tám khung mỗi board. Xem thêm PNG nguyên khung F0/F56/F64/F96/F143 (tên file=F+1) và exact START C07 từ C06 native F56. Hash ref đã tự xác minh trong preflight: `69fb0e62a3a6f138a0eae622603945b248ec8d2809c8cda513dcdfdc33d00863`.

Scope: **ALL_FRAME_STILLS_NOT_AV**. Không đọc maker actual277; không nghe/phát AV, không ASR. Evidence kỹ thuật đã đọc: H264720×1280,24fps,144 khung/video6 giây, AAC stereo48kHz/audio6,016 giây, full decode success/source unchanged. Reviewer không chạy lại probe/decode. Không browser/API/credit/git/new script/tool/media edit. Tên preset, metadata và approval tiếng cảnh khác không thay nghe D06/N07 mới.

## Findings thực tế

F tính từ0; thời gian=F÷24.

| ID / mức độ | Expected → observed | Bằng chứng và disposition |
|---|---|---|
| ENTRY01 — cần kiểm nối / reset nhỏ rõ | START A/tip ở bên Đào, gần trên vùng tay trong của cô; F0 A/tip bị tái dựng lùi trái về vùng giữa hai người. Khoai nhìn xuống thay vì nhìn Đào ở ref; Đào môi cụp, nét suy nghĩ hơn. Cốc và hai bát còn riêng. | Exact START→full F0, board01–03. Không thấy discovery hoặc head turn lại; không chứng nhận continuation seamless từ ảnh tĩnh. Actual C06→C07 seam chưa có. |
| ACTION01 — có đường đưa và giữ A | Từ vị trí lùi trái, Khoai đưa A sang phải F0–35, rồi giữ gần phía tay trong Đào; vẫn cùng miếng trên tip own pair / tay ngoài trái. | Board01–06 và toàn144 khung. Không thấy ăn, lấy miếng B, nhân miếng, đổi pair/tay hoặc thả A. Có giữ A nhưng handoff/bát chuẩn bị vẫn sai. |
| BOWL_TARGET01 — **MAJOR: Đào chọn bát Khoai** | Expected tay trong Đào chạm thành ngoài của bát Đào bên phải, rồi slide ngắn sang trái dưới A. Actual tay cô xoay thành cử chỉ lòng bàn tay hướng lên ở F49–59, đi xa sang trái, rồi chạm bát trước Khoai ở F60–65. | Board07–09/full F56/F64. Bát Đào còn nguyên bên phải, gần đũa riêng/cốc. Bát bị chạm là bát bên trái trước Khoai; không đổi tên vật thể theo vị trí sau dịch. |
| BOWL_MOVE01 — **MAJOR phụ thuộc target** | Bát Khoai trượt dần screen-right về vùng giữa F64–90. Bát Đào bên phải không được chuẩn bị. Cô bỏ tay khỏi bát trái rồi về vị trí cũ khoảng F96–105. | Board09–14/full F64/F96/F143. Đây không phải slide đúng bát Đào screen-left. Không có trạng thái bát cô tới dưới A để chờ C08. Hai bát có vẻ vẫn rỗng, nhưng ý nghĩa nhận sai. |
| HAND01 — cử chỉ phụ, không đúng tiếp xúc | Thay vì đi ngay dưới A tới thành trái bát Đào, cô mở lòng bàn tay về phía Khoai và vươn sang bát trái. Không thấy tay cắt xuyên A/tip trong ảnh đủ dày. | F49–65, full F56/F64. Đọc như gesture nói chuyện rồi đụng nhầm bát; không dùng nhãn “chuẩn bị nhận” để đóng lỗi target. Không đo lực/ma sát/vật lý từ stills. |
| GLASS01 — không thấy MAJOR | Cốc liên tục nâng trong tay ngoài phải Đào, đáy tách hai bát; không hạ, đặt, uống hoặc đổi tay. | Đủ18 board/full F0/F96/F143. Cốc được giữ không bù sai bát. |
| MOUTH01 — phần chính phù hợp, Khoai mở môi ở tail | Đào bắt đầu nhóm khẩu hình khoảng F49/2,0417 giây, tiếp tục đến khoảng F103; nhìn Khoai với nét trêu thân mật. Khoai phần này môi khép. F141–143 Khoai hơi mở môi dù brief yêu cầu im. | Board07–14 và18/full F143. Chưa đủ chứng minh có lời nam hoặc sai speaker trong tiếng. Ghi ambiguity cần AV/tiếng, không bịa Khoai đã nói N07. |
| ACT/DOP/FOOD01 — không thấy MAJOR độc lập khác | Hai mặt rõ; cô nhìn lên Khoai trước nói và thân mật hơn sau F37. Bàn, Nem Bùi nguội, rau trước trái, hai chấm và đôi đũa Đào nghỉ phải giữ; không hơi. | Toàn144 khung/full F0/F64/F143. Không nhận D06/đủ N07/sync/rhythm PASS; framing đạt không giải quyết blocker bát. |

## Không có prefix hoàn thành nhiệm vụ

Trước F60, bát Đào chưa được chuẩn bị. Từ F60 trở đi, cô chỉ chạm và di chuyển bát Khoai; bát Đào giữ nguyên đến F143. Không có khoảng nguồn nào hoàn thành phản hồi và chuẩn bị **đúng own bowl**. Trim loại tail mở môi Khoai hoặc bát trái đã dịch không làm nhiệm vụ thiếu xuất hiện.

Không đề xuất prefix selected, không lấy endpoint F143 hoặc frame giữa làm ref C08. Nếu chuyển sang để C08/C09 sửa bát, đó là đổi ranh giới hành động/coverage, cần trình owner; không âm thầm hợp thức hóa C07.

## Tầng lỗi và giả thuyết sửa có mục tiêu

Lỗi nằm trong native: chọn sai bát và dịch sai hướng so với brief, trước encode/cut. Input ref có hai bát riêng đúng; prompt có “her OWN EMPTY bowl” nhưng output vẫn chọn bát Khoai. Không kết luận thiếu dữ liệu mẫu hoặc thêm chữ “own” chắc sửa được.

Giả thuyết cho T02: “OUTSIDE LEFT wall” cùng “screen-left” có thể khiến model ưu tiên bát bên trái khung thay vì thành trái của bát Đào bên phải. **Chưa chứng minh wording là nguyên nhân duy nhất.** Phân giải object/owner, gesture nói chuyện tự phát và trạng thái A/tip cũng có thể liên quan; chưa có controlled comparison một biến.

Có thể làm rõ bằng screen-space: bát Đào là **bát bên phải, ngay bên phải tay trong đang nghỉ của cô, dưới và phía trong cốc nâng, cạnh đôi đũa nghỉ bên phải**. Bát Khoai là **bát bên trái trước Khoai**, không được Đào chạm hoặc dịch. Cô chạm thành ngoài gần tay nhất của bát phải rồi dịch ngắn sang trái; bát Khoai đứng yên. Giữ SAME A, khoảng hở, cốc, giọng, lời và camera; không thêm gesture vươn về bát trái.

Đây là đề xuất readiness giấy, chưa có T02 final/hash/live gates/quote, không paid command. Root phải tích hợp, review current final độc lập và kiểm live dưới238 trước một sửa có mục đích. Mới có một C07 take lỗi, không ghi thành hai C07 output lặp; nếu cùng MAJOR lặp ở take sau thì STOP_FOR_DIAGNOSIS.

## Disposition

C07 **REWORK / NOT_SELECTED** vì sai bát nhận; C08 **HOLD**. D06, trọn N07, heard text, sync và nhịp **NOT_CERTIFIED** trên nguồn mới. Không hỏi owner như thể hình đã đạt, chỉ còn tiếng cần duyệt. Có thể tách tiếng để nghe, nhưng approval đó không làm hình đạt hoặc tự chuyển sang take mới.

Run ghi debit10, tổng197/500, còn303, first-pass82, reserve110 đóng. Reviewer đọc ledger, không tự đối soát live account. Qua C06 còn151 khung /6,291667 giây đến35 cho C07–09; chưa có range C07 đạt nên timing phần sau phải đo, không hứa vừa trần.

## Review riêng bản sửa DRAFT277 — chưa là current-final approval

Đã đọc đầy đủ `04_requests/C07_T02_prompt_DRAFT_277.txt`, tự tính hash **`6014f1c07324b7937d18cbb3f657c7d8c15363156f5fae34fdce670ccc5aa5b7`**; đối chiếu exact START C06F56 đã xem ở phần evidence. Không đọc maker277.

Draft sửa đúng tầng chọn vật thể: gọi riêng RIGHT-SCREEN bowl trước Đào và LEFT-SCREEN bowl trước Khoai; liên kết bát đúng với tay nghỉ, cốc nâng, đũa riêng; bát trái đứng yên. Mô tả entry A bên cẳng tay trong Đào và trên vùng mép trái bát phải phù hợp tương đối với START, không ép nó đã ở trên tâm bát hoặc coi single image khóa tọa độ pixel. Không thấy mô tả sai phía hoặc yêu cầu tái reset A về ngực/phía Khoai.

Root nêu cách diễn đạt entry chính xác hơn: **“just LEFT of her RIGHT-SCREEN bowl, visibly above rim height, beside her free forearm”**. Reviewer đồng ý nên dùng trước final: A còn lệch sang trái bát theo chiều ngang, nhưng cao hơn vành; câu “above the LEFT edge” có thể bị đọc thành ngay thẳng trên vành. Đây là refinement độ rõ trên giấy, không MAJOR làm đổi ý nghĩa hoặc target. Nếu final đổi, vẫn cần hash refresh trước paid gates.

Tay Đào bắt đầu bên trái bát mình nên **đi ngắn sang phải để chạm thành trái bát phải, sau đó nắm kéo ngắn sang trái** là thứ tự hợp lý hơn việc chỉ nói “screen-left”. Grip ngoài thành dưới vành hỗ trợ lực kéo; không thấy yêu cầu phải xuyên A/tip hoặc vượt qua tay Khoai. Actual vẫn phải kiểm grip, lực và khoảng hở: ảnh giấy không chứng minh model tạo tiếp xúc vật lý đúng.

Không thấy MAJOR conflict giấy mới. Có thể giữ **DRAFT_PAPER_CONDITIONAL_GO**, nhưng draft không thắng final hiện hành và không mở paid run. Root cần tạo file final riêng, kiểm hash/readback và refresh reports trên exact final trước submit.

Rủi ro còn lại: model có thể vẫn nhầm target hoặc tự hoàn tất thả khi bát tới dưới A; lệnh chống reset không bảo đảm continuation motion từ Ingredients. “No speech or mouth movements” ở Khoai phải hiểu là giữ im/nghe, không làm mặt đông cứng; Đào được normal articulation. Không đổi voice/canon/camera; không dùng report giấy nhận D06/AV PASS. Nếu sai bát nhận lặp trên T02 thì STOP, không T03 tự động.
