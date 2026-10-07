# C02 T02 — Phản biện request độc lập, REC245

Run **C02-T02-PREFLIGHT-CRITIC-245**, ngày 07/10/2026. Mode **PAPER_REQUEST_REVIEW_WITH_ACTUAL_STATIC_REFERENCE**. **Verdict: PASS_PAPER, không VIDEO_PASS hoặc approval thay owner.** Không thấy lỗi chặn trong logic prompt/manifest hiện đọc; live binding/config/quote còn phải root kiểm trước submit.

## Input thực và giới hạn

Đọc đầy đủ `04_requests/C02_prompt_245.txt`, `C02_request_245.json`, registry245; xem lại toàn `02_refs/C02_MEDIUM_v1_CHATGPT_NATIVE.png`. Đối soát reports243/244 và audioapproval244 đã đọc trong run trước, đọc lại report244 và audioapproval trong run này. Contracts217/236/238 và PROD7/DIRECT01 đã đọc đầy đủ các run trước, giữ cùng bounded local review scope. Không UI/API/Git/credit/generation, không sửa input; chỉ viết report này. Không nghe hoặc xem AV actual, không suy output từ prompt.

Hash tính lại bằng PowerShell:

- Reference: `c0ec77283233b4b4f49c172697f8c7b42fd2a7cc4bf3960670723b1a871fd0a7`.
- Prompt245: `3a62eef954b64601cc6c33974600aaa587fc60bfad5499133719c65ad556bfb7`.

Cả hai khớp request. Actual still giữ hai mặt lớn, mắt/miệng rõ, bốn tay nghỉ riêng, môi khép, bát trống/đũa trên bàn và nem nguội; nền phố mở, đèn lồng, mái bạt cam-đỏ phải. Crop rau/cốc ngoại vi là coverage cận riêngC02, không dời props; giới hạn static244 vẫn áp dụng. Source này khác master rộng, không dùng cùng lúc hai bố cục đối nghịch trong request.

## Đối soát sửa đúng nguyên nhân quan sát

| Rule / status | Expected → observed | Closure / giới hạn |
| --- | --- | --- |
| PF245-GEO / PAPER_MET | Sửa set drift243 → prompt animate đúng ảnh medium, giữ phố/đèn/mái bạt, không thay wall/rollerdoor/fan/sign. | Khóa scene có bằng chứng source rõ hơn; chưa chứng minh model tuân thủ. Actual take phải đối chiếu nền, không chỉ cùng tên “quán”. |
| PF245-FRAME / PAPER_MET | Sửa widecamera243 → source đã cận, prompt giữ exact framing/camera locked, không yêu cầu invent góc mới từ master rộng. | Actual giữ hai mặt/miệng/hands đọc được, không full seated legs/shoes. Hash/nguồn live phải đúng medium, không v5wide. |
| PF245-HAND / PAPER_MET | Sửa head clasp243 → prompt all four hands resting separately từ first tới last, không clasp/reach/gesture. Still phù hợp. | Không coi first/last lock là bảo đảm Ingredients. Kiểm toàn range thực và onset/audio handles; không crop/cắt mất lời để né lỗi tay. |
| PF245-TEXT / MET trên giấy | Giữ178/236 → exact “Mùi này làm anh nhớ đến bếp nhà anh. Hồi bé, mẹ rang gạo, anh đứng chờ.” Không Khoan/N03/audition. | Actual listening vẫn bắt buộc; không ASR hoặc caption thay nghe. |
| PF245-VOICE / PAPER_MET; OUTPUT_UNKNOWN | MộtKhoai/K20 → tên và ID `b447b35c-b35e-4140-af72-ecd277282b1a` khớp; không D06. Đào lipsclosed/listens. | Root live verify mộtvoicechip; actualT02 phải nghe/kiểm attribution, nhất là “Hồi bé”. Approval244 chỉ T01, manifest ghi đúng không transfer. |
| PF245-CANON-F0 / PAPER_MET | Cùng bạn bè, tay/bát/đũa/món/geography giữ, không gắp/steam/flashback → prompt không đổi lời/voice/chuyện hoặc thêm claim. | Các props ngoài coverage vẫn tồn tại đúng scene, không đủ count PASS trong actual nếu không nhìn thấy. |
| PF245-TIME / TARGET_ONLY |10s request, khoảng yên đầu/cuối → không timecode bịa, không speed/pitch/cắt lời. | Nếu actual chưa vừa slot8,5s thì đo/trình conflict; prompt10s chưa chứng minh 30s phim. |
| PF245-LIVE / UNKNOWN | Fullinputs/quote≤15/x1/720p → cloudUUID và finalquote đang null, submit0, config chỉ required. | Root kiểm picker/chip/source/config/fullprompt/screenshot cuối. Không dùng null hoặc record balance1035 thay quote/quyền chi hiện hành. |
| PF245-STOP / MET hồ sơ | SameMAJOR ở lầnC02 kế tiếp → request ghi STOP/diagnose, không autoT03. | Sau T02 so findings243 exactscope; không tự đổi tên lỗi để né stoprule. |

Không phát hiện contradictory lock giữa cận mặt và peripheral coverage, hoặc giữa diễn mắt/đầu nhẹ với tay giữF0. Cụm “The only movement” có thể làm nền quá tĩnh; đây là **rủi ro chất lượng MINOR cần xem actual**, không lỗi canon hoặc lý do thêm biến/test ngay. Giữ camera/set ổn định không đồng nghĩa mọi pixel phải đứng yên; không kết luận sửa prompt này bảo đảm thành công.

## Handoff

Request245 là retake có mục tiêu GEO/FRAME/HAND-head, không tuyển giọng lại, không đổi câu hoặc master toàn phim. Referenceauthority ghi đúng shot-specific preparation236/staticreview244, **không giả owner đã duyệt ảnh mới**. Root chịu trách nhiệm xác nhận framing nằm trong scope đã có; nếu đổi identity/canon/geography vượt scope phải hỏi owner. Owner “tiếp tục” theo hồ sơ245 và autonomy238 không thay nghiệm thu T02.

Đã xác định: source/prompt/hash và paper sửa ba lỗi hình nhất quán. Đã chốt trong review: PASS_PAPER. Giả định: conditioning source cận sẽ giữ camera/set tốt hơn; chưa proof. Còn mở: livebinding/quote/config và actualvideo/voice/AV/timing/joins. Bước tiếp: root hoàn tất livepreflight; nếu hợp lệ mộtT02 trong238, giữ native/evidence, review đúngscope và checkpointC02 trước mở cảnh tiếp.

**Không actual listening, lip-sync/AV/motion PASS, generation-ready hoặc quyền retry do reviewer cấp.**
