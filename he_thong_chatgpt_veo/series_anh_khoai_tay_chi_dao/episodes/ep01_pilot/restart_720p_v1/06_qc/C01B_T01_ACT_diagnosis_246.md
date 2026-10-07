# C01B T01 — Diễn và quan hệ nghe → thu tay

**Run:** C01B-T01-ACT-DIAGNOSIS-246. **Mode:** SAMPLED_FRAMES_DIAGNOSIS / PAPER_CORRECTION_PROPOSAL. **Disposition:** HOLD_JOIN / TARGETED_REWORK_RECOMMENDED, root tích hợp critic trước quyết định. Không AV PASS, selected range hoặc quyền retry. Chỉ viết báo cáo này; không UI/API/Git/credit/media edit/generation.

## 1. Evidence thực dùng

Đọc đầy đủ current `04_requests/C01B_T01_request_246.json`, exact `C01B_prompt_DRAFT_246.txt`, `00_decisions/C01A-exact-prefix-selection-246.json`, ASR C01B và lessons source/timing. T01 target hash trong manifest: `f7321e72c952cf849f9b5febede7fb08951c997970de82e6f8d424f54415089b`; ACT không tự tính hash native. C01A selected cut hash `e22c113204c404e928683c69465237921f601f2b33a3eb9a9187eb0648f4b803`, source ref hash `0cf422f2b28dae631785af6ec19fc7488800c0cf8d22bb95dddd04e1b7ae2acb`. Source selection hiện hành đã có picture scope conditional và owner nghe exact cut, thay trạng thái source pending ở ACT prep trước.

Đã xem full source ref; ba board owner QC trong `C:/Users/PC/Downloads/du_an_nem_bui/ep01_restart_720p_v1/06_qc/C01B_T01_NATIVE_246/`: overview1fps + hai mouth/hands6fps, tổng **24 index khác nhau** (0,4,…92). Xem thêm full PNG `00001/00017/00033/00053/00073/00096` = zero-based index0/16/32/52/72/95. Tổng phạm vi **25 index khác nhau / 96 frame**, không tất cả96, không continuous AV. Timestamps dưới theo24fps trong hồ sơ, không đo audio.

ASR ghi “Khuán!” với estimated interval0–0,84s; dispatcher cho silence khoảng0,926s, nhưng ACT chưa nghe và không dùng detector làm chứng nhận. Owner câu hỏi audio còn pending theo request đã đọc. Không kết luận đúng/sai Khoan hoặc K20 từ ASR, preset ID hay hình miệng.

## 2. Quan sát cụ thể

| Index / thời điểm | Hình thấy được | Ý nghĩa và giới hạn |
| --- | --- | --- |
| Source endpoint → B index0 /0s | Source: tay ngoài Đào ở vành phải, tay trong hover gần phía trong bát. B0: tay trong đã đưa ra trước tới gần mép trái/phía sau đĩa; hình nem cũng khác nguồn. | Join không match exact pose; tay trong không tiếp tục settle từ source mà được tái dựng như một tay chuẩn bị ôm đĩa. Drift do Ingredients không start lock là giới hạn tuyến, không lỗi upload đã chứng minh. |
| index8–20 /0,333–0,833s; full16 /0,667s | Miệng Khoai có các dạng mở, ở16 khá rộng và nét cười lớn. Đào vẫn nhìn món; tay trong và ngoài ở vùng hai bên vành. | Lượt miệng nam xảy ra trước sự đổi chú ý nhìn thấy. Không chứng nhận từ/giọng hoặc phonetic sync. Diễn Khoai ở mẫu16 cởi mở hơn “ngắt nhỏ trầm tĩnh”; cần actual nghe/xem mới phân loại tone, không tự gọi quát. |
| index24–36 /1–1,5s; full32 /1,333s | Hai tay Đào sát hai phía đĩa; ở32 mắt đổi sang Khoai/chớp, ở36 hướng nhìn anh rõ hơn. | Việc tiến/giữ hai tay ở rim nối sau speech estimate, làm cô giống vẫn đang chuẩn bị lấy trước khi nhận lời ngắt. Đây là vấn đề quan hệ diễn/cue, không chứng minh thời điểm nghe chính xác từ still. |
| index48–56 /2–2,333s; full52 /2,167s | Đào nhìn anh; ngón đã bắt đầu tách/đường tay lùi lên phía bát trong các mẫu52/56. | Có đoạn release/retract muộn đọc được trên mẫu, không phải thiếu thu tay hoàn toàn. Chưa kiểm toàn đường, contact3D hoặc plate stationary bằng measurement. |
| index68–95 /2,833–3,958s; full72/95 | Hai tay về nghỉ hai bên bát, Đào nhìn anh; môi Khoai trong các full frame này khép. | State ra có thể làm candidate nối C02 sau kiểm, nhưng không sửa được cause/mismatch đầu bằng chọn vài frame đẹp hoặc lấy source cuối làm toàn take PASS. |

Không thấy Đào phát speech-mouth rõ ở các mẫu đã xem; có nét môi/ánh mắt và chớp tự nhiên, chưa chứng nhận “im suốt clip”. Môi nam mở ở nhóm speech trên, khép ở full32/52/72/95; đó là sampled-mouth scope, không AV attribution toàn take. Không thấy platepull rõ trong các mẫu ACT xem, nhưng hình món/source khác và không đo tâm/outline qua toàn path: CONT/critic phải kiểm riêng, không ACT đóng no-pull finding.

## 3. Giả thuyết nguyên nhân theo tầng

Prompt T01 nói “She keeps her intention to take the plate until she hears Khoan”, nhưng không tách **ý định còn có** khỏi **động tác đã ở ngưỡng phải dừng**. Một implementation hợp nghĩa văn bản có thể cho cô tiếp tục tiến/nắm thêm trước khi diễn nghe. Hình actual (hai tay rim → đổi mắt → thu) phù hợp giả thuyết này, **không chứng minh câu đó gây lỗi model**; cue ordering, model stochastic và pose reinterpretation cùng có thể góp phần.

Đặc biệt, inner hand đã hover/rút trong source được prompt gọi chung “settles gently” nhưng chưa xác định hướng duy nhất ngay từ đầu. B0 chuyển nó thành tay tiến tới đĩa. Đây là **thiếu đặc tả dương cho chuyển động tiếp nối** cộng actual source drift, không tự sửa bằng thêm nhiều câu phủ định. “Được phép inner gesture” ở C01A không cho phép đổi thành lần reach/grip mới ở B.

Root nên giữ ba finding riêng: (a) source pose drift tại cut; (b) renewed two-hand approach/grip và phản ứng muộn; (c) lời/giọng pending actual nghe. Không gom (c) thành retake reason từ ASR, không coi endpoint tay nghỉ giải quyết (a)/(b).

## 4. Chỉnh diễn tối thiểu để tích hợp, chưa final prompt

Giữ voice/canon/N01–Khoan–C02, same two-shot/table và source; không freeze/warp/speed hoặc đổi pitch. Đề xuất dương:

1. **Khoai bắt đầu từ Khoan ngay đầu nhịp**, sắc mềm và gọn, nét mặt điềm tĩnh; không grin rộng trước/suốt lời. Timing là relative cue, không hứa số frame hay đòi tiếng rơi exact0s.
2. **Tay ngoài đã tới vành nên bước kế tiếp duy nhất là release**, không cần thêm tiến hoặc nắm. Khi cue bắt đầu, Đào chuyển mắt tới anh và bỏ ý định; ngón ngoài nới/rời vành rồi cẳng tay về ngoài bát. Không cần đợi kết toàn từ mới chuẩn bị phản ứng.
3. **Tay trong tiếp tục chuyển về phía thân/điểm nghỉ cạnh trong bát ngay từ source hover**. Đây là gesture phụ đang khép, không một reach mới và không phải cue “Khoan” chặn tay này riêng. Outer release là hành động có quan hệ nghe rõ; hai tay không cùng ôm vành.
4. Kết hai tay nghỉ thật, Đào chú ý người kể, Khoai sẵn sàng nối ký ức. B0 và đường tay phải được đối soát actual với source; positive cue không biến Ingredients thành frame lock.

Nếu root muốn đổi route để giải quyết first-frame drift, CTD/FLOW phải đánh giá feature/voice cùng intent, không ACT tự chuyển Frames hoặc bỏ voice. Giữ chỉ dẫn tối thiểu trên như **targeted proposal**, không quyền submit hoặc guarantee.

## 5. Kiểm đóng lỗi và thời lượng

- C01A→B actual pose giữ outer rim + inner hover/retreat; không đầu B có renewed two-hand grasp hoặc món reset. DOP/CONT/EDIT xem hai phía cut và path, không chỉ overlay still rồi PASS.
- Cue Khoan/người nói phải được nghe actual; reaction Đào theo cue và mắt→outer release→rest đọc được, không vẫn tiến rim sau cue rồi thu mới.
- Native4s là nguồn diễn, không selected range. C01A3,375s + target mở4,5s chỉ còn1,125s **trên giấy**; không ép B vào1,125s nếu lời/reaction cần dài hơn. Root/EDIT phân bổ lại toàn30s theo actual, giữ C02 approved và các beat còn lại.
- Chọn range giữ nguyên lời/nhịp/stop-release và nối C02; không trim bỏ phần sai đầu để khiến thao tác từ nguồn bỗng teleport, không cận món che cause. Nếu endpoint tốt mà đầu/path hỏng, vẫn HOLD_JOIN.
- Maker ACT không độc lập; root đọc critic và owner audio answer, tổng hợp severity/stop rule238 trước retry. Không generation mới trong diagnosis này.

**Đã xác định:** sampled B0 không match inner-hand pose nguồn, hai tay gần vành trước khi Đào đổi chú ý, thu/rest tồn tại ở phần sau. **Giả thuyết:** “giữ ý định lấy tới khi nghe” + inner-settle không rõ hướng cho phép renew reach trong thực thi; chưa causal proof. **Còn mở:** actual nghe Khoan/K20, fullpath/plate continuity, cut feasibility và critic findings. **Bước tiếp:** root tích hợp đề xuất cue dương tối thiểu với reviewer; không đổi voice hoặc chạy lại từ ASR đơn độc.
