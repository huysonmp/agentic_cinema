# EP01 — Phản biện khả thi shot P7 v0.1

2026-10-01. Run `EP01-P7-FLOW-01`; role `AG-FLOW-01 / P7 / PAPER_REVIEW`; rubric `TIER1-RUNTIME-v0.1`.

## Input, quyền và actual access

- Đọc toàn Tier1 runtime02, chỉ section AG-FLOW-01 của role03, envelope/register FLOW-01 trong production_team12; đọc toàn target79 trước sources.
- Target: `79_p7-shot-design-draft-v01.md`, v0.1; SHA256 kiểm local khớp `77876F589D0F2090DCEFC6B75941167752C9809E12E6E6AA8635C7975945C0D7`.
- Sau target, thực đọc toàn episode32/35/38/45/62/71/75/78 và production_team13. Output batch bị truncate phần62/71 nên đọc lại đủ hai file.
- Thực xem duy nhất `media/raw/ep01_p6_food/T-NB-03_v0.8.jpg`: Khoai trái/Đào phải cùng cạnh, cốc ngoài phải, bát trước mỗi người, đũa trên bàn, món giữa và lá/chấm trong bữa ăn. Không đo khoảng cách/reach.
- P03/F05/I03/I05 chỉ đối chiếu metadata/authority trong45/62/71/75/78; không xem lại pixels của bốn refs này, không kết luận fidelity/grip từ lời mô tả.
- Không đọc maker chat, CTD11, maker74/76, reviews18/19 hoặc root verdict; references tới chúng trong allowlist không được mở. Không audience cold-media claim: đây là đọc thiết kế có chủ ý, chưa có clip.
- Authority38 giữ C-v0.5/Q0 và hướng giọng;45 primary;62 grip direction;75 ghi serving approved;78 exact static v0.8 và tiếp tục P7 paper.35 chốt owner ghép Canva/nhận clip pack có QC.
- Không browser/network/audio/generation/upload/credit/Git hoặc agent con; không sửa32/79/upstream. Chưa actual voice, motion, account UI/cost hoặc approved video request.

**P7 paper: `PASS_WITH_ACTIONS` để trình lựa chọn coverage và chuẩn bị P8; chưa shot lock.** Những action dưới không ngăn đọc/so sánh proposal, nhưng phải đóng đúng gate trước khóa request hoặc bàn giao clip.
**Generation readiness: `BLOCKED`.** Thiếu giọng/timing thực, action inputs đúng trạng thái, account feature/audio/cost, manifest/count cap/stop, quyền reference đúng request và owner request approval. Không chuyển UNKNOWN thành PASS.

## Coverage FLOW-1–5

| Check | Status trong scope paper | Evidence và giới hạn |
|---|---|---|
| FLOW-1: beat/lời/join | MET |32 nội dung→79 S01–S05 bao phủ đủ; A đổi hướng trước contact, vào bát, kết gắp B; joins có state. B chưa đủ boundary specification để khóa. |
| FLOW-2: refs/authority | MET paper; UNKNOWN production |79 ledger/staging,45/62/75/78 có exact refs và scope; neutral T08 không được gọi action keyframe; quyền upload/use của từng request chưa kiểm. |
| FLOW-3: tải/conflict | MET nhận diện; UNKNOWN thực thi |79 S04/D3/D4 đã chỉ ra nhiều tay/props và cần motion; S01/S02 cũng có thoại/cue cạnh tranh; chưa media để kiểm reach/lip-sync/nhịp. |
| FLOW-4: feature evidence | MET tài liệu; UNKNOWN account |13 ghi ngày2026-10-01, URLs/sections Google: native4/6/8s, Ingredients Lite/Fast8s, Quality unsupported, extend Lite.79 phân biệt logical shot/request và không đổi sang Omni. |
| FLOW-5: fallback/probe/cost | MET hướng đề xuất; UNKNOWN packet |79 có A/B và acceptance D4; chưa số thử tối đa/count/stop/credit estimate theo request. Đây action P8, không bounded execution authority. |

### Shot/beat và continuity kiểm độc lập

| Shot / script32 | Lời exact và speaker | State/join và tải cần giữ |
|---|---|---|
| S01 /9–15 | Đào: “Anh nhìn mãi. Không hợp thì để em.” Khoai: “Khoan. Mùi này làm anh nhớ cái chảo.” | P0 chưa gắp; định kéo rồi dừng giữa bàn. J12 giữ đĩa/tay/đuôi “chảo”. TARGET4–6s còn nghiêng/ngửi/kéo-dừng, hai câu và F01→F02. |
| S02 /17–19 | Đào: “Nem thì đây. Chảo ở đâu?” Khoai: “Bếp nhà anh, hồi bé. Mẹ rang gạo, anh đứng chờ.” | P0 giữ; tay trái Đào thu về bát; không flashback/mẹ/chảo xuất hiện. J23 eye-line cùng phía trục. TARGET6–8s và F02 chưa timed. |
| S03 /21–23 | Đào: “Chờ ăn?” Khoai: “Chờ mẹ quay lưng.” | P0, đũa/cốc tại bàn; chuẩn bị quay khác với đã quay. J34 mở rộng trước lấy cốc, không bỏ cú lấy cốc hoặc lặp setup. TARGET3–4s chưa đo. |
| S04 /25–37 | Đào: “Chờ em quay lưng nữa à?” Khoai: “Anh gắp cho em mà.” Đào: “Thế em quay lại đúng lúc rồi.” | Lấy cốc→gắp A về miệng→bị thấy/khựng→đổi hướng→đặt cốc→đưa bát. Cuối A trên đũa trên bát, P0−A; chưa thả. J45 match A/tay/bát/cốc/eye-line. TARGET10–14s tải lớn. |
| S05 /39 | Không thêm thoại | A từ đũa vào bát Đào→rút đũa→gắp B, P0−A−B; B chưa chạm miệng. Không duplicate transfer ở J45. TARGET2–3s còn cần giữ kết để cắt. |

Tổng9 câu nguyên văn/đúng speaker; không câu mới, không ăn/nhai/đút/romance. Causal joke trên giấy được bảo toàn: lưng quay là cơ hội ăn vụng, mắt Đào trở lại gây khựng, đổi hướng mới là chữa cháy; Đào nhìn A rồi anh và trêu chứng tỏ đã hiểu. Hiệu quả khán giả đọc được vẫn UNKNOWN.

Địa lý giấy nhất quán: Khoai trái nhìn phải, Đào phải nhìn trái; cốc ngoài phải; camera cùng phía trước bàn. Chén/lá/bát Khoai/đũa Đào đứng yên. W-HAND và W-PROP là choreography đề xuất, không canon; việc Đào đặt cốc trước đưa bát giải phóng tay phải và tránh cốc/bát cùng chuyển ở cuối.

Phần A/B là ký hiệu theo dõi, không đếm miếng/gram từ ảnh: trước S04 P0; cuối S04 P0−A; cuối S05 P0−A−B. Có thể đối soát joins bằng trạng thái vật thể, chưa thể xác nhận lượng/biến dạng ở motion.

### A so với B và dependency/request map

- A tốt hơn ở mức bằng chứng nguyên nhân: cùng khung giữ đường A→miệng→bát và hai phản ứng. Khuyến nghị A của79 hợp lý về ngữ nghĩa, nhưng không chứng minh A khả thi kỹ thuật hơn B; native10–14s không được tài liệu13 hỗ trợ. Extension/assembly phải kiểm route/điểm nối thực, không đồng nghĩa liên tục không lỗi.
- B có thể giảm tải mỗi đoạn và dùng TARGET4–6s/6–8s, nhưng B1 vẫn gồm lấy cốc, nhấc đũa/gắp/đưa A, quay lại, khựng và câu Đào. Chưa thể gọi nhẹ hoặc vừa native. B2 phải bắt đầu từ A đang dừng ngoài miệng, giữ cup/hand/eye-line và hướng đũa; nếu bắt đầu neutral hoặc A đã hướng tới cô thì mất bằng chứng chữa cháy.
- Trước chọn B cần viết exact boundary: cốc còn trên tay phải Đào hay đã đặt, vị trí bát/tay trái, A và đũa dừng đâu, Đào đã nhìn thấy A chưa, câu thứ7 kết ở bên nào. B hiện nêu match requirement nhưng chưa có hai dòng start/end đủ để request/review riêng.

| Unit | Ref role theo79 / dependency | Mode/duration/count/cost ở P8 |
|---|---|---|
| S01 | T08 địa lý/pre-action + P03 identity + F05 texture; D1/D2/D5 | UNKNOWN; TARGET4–6s không là selection4 hoặc6s. |
| S02–S03 | T08 layout + P03 identity; F05 giữ món; D1/D2/D5 | UNKNOWN; start-frame theo state trước, tránh reset tay/người. |
| S04 hoặc B1/B2 | Layout/identity/texture trên; I03/I05 hướng grip; action-state D3 + motion D4 + D1/D5 | UNKNOWN; native4/6/8s theo13 chỉ khi mode/account phù hợp. A cần route ngoài một native request. |
| S05 | Layout/identity/texture/grip trên; start A chưa thả + D3/D4/D5 | UNKNOWN; TARGET2–3s là phần dùng sau dựng, không native2/3s. |

Các role ref là dependency planning, không khẳng định phải upload tất cả cùng request hoặc cùng mode. P8 phải đánh dấu required/optional, conflict, exact input slots và right-to-use riêng; không gom Ingredients+frames+extend thành capability duy nhất. Số logical shots5 không khóa số requests/clips/candidates.

## Findings, severity, route và closure

| ID / severity / status | Evidence/impact | Action → route / closure |
|---|---|---|
| FLOW-F01 / MAJOR / UNKNOWN |79 S04 TARGET10–14s;13 native4/6/8s. Chưa tuyến A continuous usable; B cũng chưa timed. Không kết luận generation-ready. | P8 FLOW chọn route có account read-back và packet được duyệt; đóng khả thi actual bằng take/join theo version, không chỉ tên feature. |
| FLOW-F02 / MAJOR / UNKNOWN |79 S04/S05 và D3/D4; T08 là neutral still. Chuỗi A/grip/cốc/bát và ánh mắt có nhiều event, không motion proof. | P6 action-state brief→P8 probe→P9 PERF/CONT. Closure: A chưa contact, không biến mất/nhân đôi, Đào nhìn thấy, transfer đúng bát và B riêng; actual boundary frames. |
| FLOW-F03 / MAJOR / UNKNOWN |79 TARGET25–35s, chín câu + actions/cue; không tiếng/reading test. S01/S02 và B1 đều có tải cần đo. | VOICE/AV theo quyền riêng, P8 timing rồi P11/P12 cue/export. Closure: exact9 câu đúng người, không cắt âm/ép nói, actual timeline và đọc đủ F01/F02/AI không che payoff. |
| FLOW-F04 / MINOR / DEFECT khi khóa B |79 bảng alternatives B chưa khóa state cốc/tay/bát ở B1→B2; trạng thái reset có thể làm A thành cho cô ngay từ đầu. | AG-SHOT bổ sung v02 nếu chọn B; CONT/FLOW paper kiểm hai boundary rows rồi media join. Không bắt revision B nếu owner chọn A. |
| FLOW-F05 / MAJOR / UNKNOWN production |79 D5 hoãn manifest; chưa exact model/mode/audio/ref rights/count cap/stop/giá/approval.13 là general docs, không UI account. | P8 PROMPT/FLOW/RIGHTS lập manifest, estimate có căn cứ hoặc UNKNOWN, bounded probe số thử tối đa/fail/stop và owner request approval. Không chạy khi còn blocker. |

## Disposition và tối đa ba quyết định owner

- KEEP79 làm proposal P7 có coverage đầy đủ; không rewrite script để vừa công nghệ. HOLD shot lock/request/media pass/clip pack cho đến evidence đúng gate. Giữ watermark và cue đã duyệt; crop chưa approved/delivery ratio chưa exact9:16 theo78.
- Quyết định1 cần owner: giữ A làm coverage ưu tiên có điều kiện chứng minh route, hay phát triển B với boundary bổ sung? Sơ bộ giữ A làm intent, chuẩn bị B fallback; không chốt generation route chỉ từ paper.
- Quyết định2 có thể gộp lúc duyệt shot: chấp nhận W-HAND/W-PROP và crop chức năng cùng phía trục? Đây thêm staging cụ thể so neutral78; khuyến nghị như79, sau khi có boundary/action-state đối soát.
- Không hỏi thêm quyền media ở report này. Account/voice/motion là task kiểm chứng; chỉ trình quyết định request/cap/spend khi packet P8 cụ thể đã reviewable, không yêu cầu owner đoán feasibility.

## Handoff năm phần

1. Đã xác định:9 câu/beat đủ, chronology/state giấy nhất quán; A giữ causal evidence tốt nhưng route thực thi chưa biết.
2. Quyết định owner hiện có: C-v0.5/Q0, primary/grip/serving/static78, P7 paper và owner dựng Canva; chưa shot/request/media approval.
3. Giả định: choreography tay/cốc, crop, A/B portions và TARGET ranges; không assumption về giọng/native capability/cost.
4. Còn mở: lựa chọn A/B, action-state/boundaries, audio/timing/cue, account features/rights/cap/cost/request, fidelity/reach/motion thực.
5. Tiếp theo: root đọc report80→trình coverage/staging→AG-SHOT revision cần thiết→P8 manifest/probe có stop/cap và đúng approval; media về sau mới PERF/CONT/AV rồi QC clip pack/Canva export theo35.
