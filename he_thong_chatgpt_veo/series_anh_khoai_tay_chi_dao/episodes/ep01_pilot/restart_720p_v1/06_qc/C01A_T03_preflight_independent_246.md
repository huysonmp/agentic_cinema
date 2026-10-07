# C01A T03 draft — Preflight độc lập REC246

Run **C01A-T03-PREFLIGHT-246**, ngày 07/10/2026. **Verdict: PASS_PAPER_CONDITIONAL / SUBMIT_HOLD_LIVE_FIELDS.** Đủ coherent để root chuẩn bị một targeted retake trong scope238; chưa cấp quyền từ report, chưa media PASS hoặc guarantee. Không cần lựa chọn canon mới từ owner ở phạm vi draft này.

## Source đã đọc và exact version

Sau hoàn tất actual T02 critic, đọc full root diagnosis246, ACT/DOP diagnosesT02, `C01A_T03_prompt_DRAFT_246.txt`, `C01A_T03_DRAFT_controls_246.json` và `C01A-T02-audio-approval-246.json`. SourceF0/actualT02 đã xem trực tiếp trong run trước ngay cùng chuỗi; không xem lại toàn video hoặc nghe. Chỉ local read/hash + assignedreport, không UI/API/Git/credit/generation.

Prompt SHA256 thực **`9e68e8ff9ec8d9e63bc7cc931936a77da2ee34c2bc972c31bef7fa4260b0c282`**. SourceF0 hash `c59ad1e…` không đổi. Owner WAV hash tính lại **`1082833d4066616f50b410ffa3c820373063acf12c18ebe1ea3dc91fde699863`** khớp exact approval. Owner đã chấp nhận **T02 audio D06/lời/nhịp**, đóng mốc nghe đầu tiên; không T02 picture/sync hoặc futureT03 waveform. ActualT02 report là historical lúc approval audio còn pending, không được giả reviewer đã nghe.

## Targeted review

| Tiêu chí | Draft hiện hành / đánh giá | Gate cần giữ |
| --- | --- | --- |
| Ý định tay | Mu tay lên/lòng xuống, ngón hơi cong chuẩn bị tới mép đĩa; ngón hướng mép trên-phải, không hướng Khoai/bát anh. | Sửa dương trực tiếp presentingT02, giữ **đang định lấy** chưa hoàn tất, không canon review/giới thiệu món. Khẩu lệnh không bảo đảm diễn đạt; cold actual interpretation vẫn bắt buộc. |
| Đích/gap | Đầu ngón trên gỗ trống trái-trước bát Đào, trước outline mép trên-phải đĩa; còn strip gỗ nhìn thấy, không finger overlap. Bỏ HIGH ABOVE và width rigid. | Phù hợp DOP conditional geometry, không yêu cầu cả bàn tay nằm lọt ô nhỏ. Hai mô tả trước-bát/sau-đĩa cùng vùng; không thấy contradiction giấy. Nguy cơ **quay lại GAP-01 T01** phải kiểm dày actual, không chấp nhận rim occlusion/contact ambiguous vì gap nay nhỏ hơn. |
| Route/hold | Outerhand ban đầu nearestglass tiến inward abovechopsticks; otherhand rest; afterword môi khép/giữ ý định chưa contact đến cuối, không return/eat/interruption. | Phù hợp C01B cue, giữ foodF0 nhưng statehand khác; không fake start/end lock Ingredients. Hold chỉ nativebuffer, không bắt dùng đủ6s hoặc freeze hậu kỳ. |
| Text | Chỉ giữ small existingfour-point symbol dưới-phải, bàn unlettered, không graphic/caption/logo/readabletext mới; không đưa chuỗi chữT02 vào creativeprompt. | Sửa ambiguity “preserve watermark” mà **không xóa symbol nguồn**. Không chứng minh watermark wording chính là nguyên nhân; sourceclean và outputlettering mới chỉ đóng tầng phát sinh. Nếu chữ tái xuất vẫnREWORK, không crop/overlay cứu hoặc đổi tên nguồn. |
| Voice/canon | Chỉ peachwoman/attachedfemalevoice, exactN01 một lần; potatoman im/môi together/tay nghỉ. Controls exactD06 ID, cùngF0/scene/camera/bàn/coldfood/6s720px1. | Bỏ filename khỏi prose không đổi giọng nếu exactchipbinding vẫn đúng; **không được genericfemalevoice** hoặc chuyểnapprovalT02 sangT03. “Single female sentence” cuối prompt hiểu là lượtN01 đã quote hai câu, không đổi lời; có thể sửa thành “dialogue” để rõ hơn nhưng không blocker. |

## Chẩn đoán và stop gate

Root đã đọc đầy đủ actualcritic và ACT/DOP, phân biệt observed với hypotheses. Hai MAJOR T01 **rim-occlusion/no-visiblegap** và **prematurereturn** không quan sát lặp ở samplesT02; text/presenting là newblockers. Không có evidence model-internalcause chung, không được đổi nhãn mọi “C01A fail” thànhsameMAJOR hoặc coi paper wording là causalproof.

T03 là proposal sau diagnostic HOLD đã thực hiện, không automaticT03 nhờ đổi tênfinding. Same-MAJOR rule238 **vẫn giữ**: nếuT03 lặp presenting/textT02 là hai output liên tiếp cùng blocker ⇒ STOP chẩn đoán/trình, khôngT04. NếuT03 quay lạigapT01 (không liềnT02 theo observedscope) thì vẫn REWORK và HOLDdependency; không suy ngưỡng consecutive miễn chất lượng. Root phải giữ report/case mapping và scope chưa xem, không né gate bằng “newwording”. Draft không đổi canon/camera/voice/tool/reserve nên không thấy materialownerchoice bắt buộc tại paperstage; nếu route thay các mục ấy hoặc cần waiveblocker thì phải hỏi.

## Trước submit và sau output

Controls là **DRAFT**, quote null/submit0; expectedroute chưaliveevidence. Cần request executable có exactprompthash trên, mộtF0UUID `4c83356f-ac72-437b-8dd7-f8534b61103a`, mộtD06ID `6dadc0b1-00c3-493c-943d-f4a1e4a88feb`, newgenerationIngredientsOmni1.1Flash720p9:16/6s/x1/AgentOFF, fullreadback/finalscreenshot và quote≤15. Không video-edit route, không dùng quoteT02 choT03. Budget bảo thủ spent50/remaining450/retake155, reserve110 chưa quyền; live balance không thay budgetauthority.

Sau output phải kiểm **text ngay frame0/giữa/cuối + wholepath/coldintent/visiblegap/noearlyreturn**, hồi quy hai mặt/Khoai listener/bàn/nem nguội. Nghe/xem actualT03 và chọn endpoint sau trọn“em” có ý định/gap thật; giữ ownerT02 approvalscope, không mặc định productionvoice mới accepted. C01B vẫnHOLD tới endpointactual + range/hash và review đủ nghĩa; không dùngfakepose hoặc cắt âm/foodcover.

**Tổng hợp:** paper treatment đủ cụ thể và đúng lỗi mục tiêu; nguyên nhân còn giả thuyết, không forecast. PASS_PAPER conditional, SUBMIT_HOLD tới rootlivegates; actualintent/text/path/voice/sync/endpoint chưa biết. Bước tiếp root lậprequestvàreadback trong238, một lượt nếugatesđóng; outputlỗi phảichẩnđoán/ápstoprule đúng finding, khôngautorun hoặcapprove thayowner.
