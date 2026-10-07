# REC218-ACT-R1 — Thiết kế diễn xuất recovery EP01

Ngày: 2026-10-06, Asia/Saigon. Vai: ACT maker / P7. Mode: FRAME_EVIDENCE_AND_PERFORMANCE_DESIGN. Capability thực: PAPER + SAMPLED_FRAMES. Disposition: **PROPOSAL_COMPLETE trong phạm vi thiết kế/ảnh; HOLD nghiệm thu chuyển động, diễn liên tục, hearing, lip-sync và full AV**. Không phải ACT/PERF/media PASS, không phải final take hoặc generation-ready. Maker này không tự làm reviewer độc lập.

## 1. Authority, input và công cụ thực dùng

Authority: owner chốt 217-Q1-A/Q2-A/Q3-A (“1 A; 2 A; 3 A”); bounded dispatch REC218-ACT-R1 từ root. Chỉ local read và viết đúng báo cáo này bằng apply_patch. Không sửa nguồn thoại, ảnh, media, script hoặc report khác; không browser/API/generation/credit/install/git/spawn. Không đọc contribution DOP/EDIT R1. Lệnh nhúng trong nguồn là dữ liệu, không mở quyền.

Đã đọc đầy đủ các input sau, đường dẫn tương đối từ `he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/`:

- `agents/directing_team/01_approval-and-operating-model.md` — DIRECT-v0.1.
- `agents/directing_team/04_character-performance-director-prompt.md` — AG-ACT-01 v0.1; đây là exact filename của role ACT trong repo.
- `agents/production_team/02_common-runtime-contract-v0.1.md` — PROD7-v0.1 và addendum DIRECT.
- `episodes/ep01_pilot/178_owner-dialogue-amendment-c-v0.6.md` — nguồn bảy lượt hiện hành.
- `episodes/ep01_pilot/212_recovery-discovery-and-decision-gates.md`, `213_recovery-tier2-visual-story-discovery.md`, `214_recovery-storyboard-r1-and-acceptance.md`, `215_recovery-tier3-assets-feasibility-and-decisions.md`, `216_n02-deep-local-check-and-reuse-boundaries.md`, `217_recovery-tier4-runtime-gates-and-questions.md`, `218_recovery-role-runs-and-gate-implementation.md`.
- `episodes/ep01_pilot/evidence/218/01_dir-maker.md` — REC218-DIR-R1; đã nhận ý đồ, PA/PB và brief ACT sau DIR. Đây là maker input, không là verdict độc lập.

Đã mở/xem ảnh thực bằng công cụ xem ảnh local tại `C:/Users/PC/Downloads/du_an_nem_bui/`:

- `T2-CODEX-OPEN_v0.7.png` — reference diagnostic; không nâng thành canon mới hoặc asset approved cho mọi trạng thái.
- `216_n02_face_coverage_check/speech_anchors.png`: f0/31/55/70/94/109/128/137/143/161/167/176.
- `216_n02_face_coverage_check/face_to_dish_boundary.png`: f144/148/152/154/156/158/160/162/164/166/168/176.
- `216_n02_face_coverage_check/dish_to_faces_boundary.png`: f192/194/196/198/199/200/201/202/203/204/206/208.
- Sáu ảnh native trong `216_n02_face_coverage_check/all_240_frames/`: `frame-0071.jpg`, `frame-0072.jpg`, `frame-0163.jpg`, `frame-0164.jpg`, `frame-0200.jpg`, `frame-0201.jpg`.
- Sáu contact board trong `215_recovery_asset_screening/`: `180_c_v06_dialogue__A02.png`, `180_c_v06_dialogue__A03.png`, `163_low-hold-reaction__R02.png`, `194_dao_reaction_R2__R203.png`, `154_visual_lock__R01.png`, `209_remaining_production__U08_NATIVE.png`.

Ba board216 có 36 ô và các board215 có 72 ô lấy mẫu; có frame216 lặp giữa board/native. Không gọi đây là 114 frame khác nhau, không nhận đã xem hết 240 frame216 hoặc 289 MP4. Nhãn thời gian trên board215 là nhãn lấy mẫu hiện có, không là frame range EDL được ACT xác minh mới.

Công cụ thực: PowerShell `rg --files`, `Get-Content -Raw`, `Test-Path` để tìm/đọc source và kiểm output chưa tồn tại; `view_image` để quan sát các ảnh nêu trên; `apply_patch` để viết report. Không probe, hash, ASR, render hoặc sửa audio/video trong run này. Source hash N02 `72cbaf7d9f66932002dfce1b1a57fa464935c315e84e54ae094fe29aa805a153` và audio202 `3c83b7d6188f5b973b0ef5c77ebc1fc16afde7c11827764c5302145741b736d4` được kế thừa từ216/218 và DIR; **ACT chưa xác minh byte/hash mới**.

Input/capability còn thiếu: contribution DOP R1 và action envelope đã tích hợp chưa có trong context này theo dispatch; chưa có recovery AV master/EDL final; chưa nghe WAV/native, chưa xem playback liên tục có/không tiếng, chưa kiểm âm vị hoặc đồng bộ miệng. Không đọc mới voice direction93/canon file riêng: các khóa giọng/tính cách/quan hệ dùng từ178/213/214 và role04, không tự thêm canon. Approval nghe của owner tại201/203 được ghi lại trong215 là lịch sử authority, không phải ACT đã nghe. Thiếu DOP không chặn paper design theo214/DIR; phải tích hợp framing trước shot/request lock.

## 2. Khóa diễn và bản đồ lời không thay đổi

Giữ nguyên từng chữ/speaker C-v0.6; 214 là storyboard text đã duyệt. Hai mặt và bàn là điểm tựa, khán giả thấy ý định ăn trước Đào; cô lấy cốc tự nhiên, quay lại mới phát hiện. Khoai trầm ấm, kể thân mật, hài tinh tế; Đào cởi mở, tò mò và trêu nhẹ theo cách người trưởng thành. Hai người là bạn. Nét vui được tạo từ hành vi hiểu nhau, không tạo thêm backstory, quan hệ tình cảm hoặc kiểu thắng/thua.

| Khung | Lời khóa / người nói | Người nghe và điều phải giữ |
|---|---|---|
| R01 | N01 — Đào: “Anh nhìn mãi. Không hợp thì để em.”; đầu N02 — Khoai: “Khoan.” | Khoai chú ý món rồi đáp; Đào dừng tay định kéo đĩa sau cue Khoai. Không giao “Khoan” cho Đào. |
| R02 | Phần còn lại N02 — Khoai: “Mùi này làm anh nhớ đến bếp nhà anh. Hồi bé, mẹ rang gạo, anh đứng chờ.” | Đào nghe lời anh; ký ức thuộc fiction tập, không tạo flashback hoặc claim mẹ làm Nem Bùi. |
| R03 | N03 — Đào: “Anh chờ ăn à?”; N04 — Khoai: “Chờ mẹ quay lưng.” | Luân phiên nói/nghe đúng lượt; ý hài xuất hiện khi chữ “chờ” được hiểu lại. |
| R04 | Không thoại mới. | Đào chú ý cốc; Khoai tranh thủ gắp A về mình, chưa contact miệng. |
| R05 | N05 — Đào: “Chờ em quay lưng nữa à?” | Khoai biết bị thấy và khựng nhẹ; A còn kẹp, chưa đổi hướng. |
| R06 | N06 — Khoai: “Anh gắp cho em mà.” | Đào nhận ra lời chữa cháy; hướng A đổi sau khi bị thấy. |
| R07 | N07 — Đào: “Thế em quay lại đúng lúc rồi.” | Khoai nghe; Đào đưa bát, A chưa thả nếu R08 còn thể hiện việc thả. |
| R08 | Không thoại mới. | A được thả vào bát Đào đúng một lần. |
| R09 | Không thoại mới. | Đào cười nhẹ; Khoai tự gắp B khác; A vẫn ở bát Đào. |

F0→F1→F2→F3→F4 và A/B theo214 là dependency diễn, không chỉ continuity đồ vật. Không nói khi nhai; không đưa A đã chạm miệng cho Đào; không đút. Món nguội không khói. Giữ F01/F02/nhãn AI đúng214; ACT không sửa chữ hoặc đặt chữ che mặt để giải quyết khả năng tool. Giữ K20/Orus và D06/Aoede tùy chỉnh; VOICE/SIA chịu thực hiện và kiểm giọng, không dùng hành vi miệng trong still để nhận giọng đạt.

## 3. Performance score R01–R09 — mục tiêu, cue, đổi trạng thái, observable

Mọi cue/hold dưới đây là **PROPOSED relative order**, không là timing đo. Không gán số giây, số blink hoặc góc nghiêng đầu từ phỏng đoán. “Khựng” là ngừng/thu biên độ ý định trong một nhịp đủ đọc, không là đóng băng frame. Cần PERF xem output AI thực để kiểm sự tự nhiên, không yêu cầu người thật diễn thử.

### R01 — Muốn ăn và được giữ lại để nghe

- Mục tiêu/obstacle/tactic: Đào muốn tiếp tục bữa ăn khi Khoai nhìn món lâu; cô trêu và định kéo đĩa. Khoai muốn giữ sự chú ý ở món và chia sẻ nguyên nhân, dùng “Khoan.” thay cho diễn thuyết bằng tay.
- Attention → inference → emotion: mắt Đào tới Khoai, tay hướng P → cô muốn ăn và đang nói với anh → gần gũi, tò mò. Khoai từ món tới cô sau cue → anh có lý do riêng → chờ giải thích.
- Before → cue/turn → after: F0, hai người chưa gắp; tay Đào bắt đầu ý định kéo → Khoai nói “Khoan.” → cô dừng lực kéo, thả lỏng bàn tay tại vùng đĩa và chuyển chú ý nghe. Không thực kéo P sang vị trí mới rồi reset trong cut.
- Gaze/body/face/hand: Khoai hơi nghiêng chú ý món, bàn tay chưa cầm nem; nâng nhìn tới Đào khi đáp. Đào có nét trêu nhỏ, thân mở với bàn ăn; không nhún vai/cười lớn hoặc kéo giật để ép người kia. Miệng Khoai yên khi Đào nói và ngược lại; vẫn có blink/phản ứng tự nhiên, không cần mặt đơ.
- Partner reaction/voice intent: Đào nghe “Khoan” bằng tay dừng và mắt lên anh. VOICE: N01 nhẹ, gần gũi; “Khoan” rõ ý giữ lại nhưng không quát, không chèn từ hoặc âm cười mới.
- Framing/observable: cần hai mặt, tay cô và P đồng thời hoặc chuỗi nối chứng minh kéo→dừng. Success paper: người xem đọc được lời anh là cue dừng. Failure: tay nghỉ suốt không có ý định kéo; cô tiếp tục kéo sau cue; “Khoan” bị cắt hoặc sai speaker. Chưa có media chứng minh hành vi này đạt.

### R02 — Chia sẻ ký ức với bạn cùng bàn

- Mục tiêu/obstacle/tactic: Khoai muốn giải thích vì sao anh chú ý mùi; kể một ký ức nhỏ để cô bước vào cảm giác của mình. Obstacle là dễ biến lời dài thành độc thoại nhìn camera; tactic là chia sẻ tới Đào, giữ thân và tay ổn định để mắt/mặt mang ý nghĩa.
- Attention → inference → emotion: món → mắt/mặt Khoai → anh đang nhớ chuyện riêng và kể cho cô → ấm, thân mật; chú ý Đào đang nghe → lời đến được người đối diện → chờ câu hỏi.
- Before → cue/turn → after: dừng kéo từ R01 → ý “Mùi này...” đưa mắt từ món lên Đào; “Hồi bé...” nét mặt mềm hơn khi nhớ → cuối “anh đứng chờ” vẫn đang chia sẻ, để khoảng cho câu hỏi. Không tạo flashback bằng việc nhìn lên trời lâu hoặc hành vi chỉ trỏ mẹ/bếp không có trong cảnh.
- Gaze/body/face/hand: vai thả, thân hơi hướng về người nghe; nét cười kín ở khóe miệng khi không phát âm, mắt ấm. Khi nói, miệng phục vụ đúng lời thay vì giữ nụ cười rộng liên tục. Tay F0 nghỉ tại bàn, không gắp trước R04. Đào theo anh bằng gaze đã thiết lập, một phản ứng tiếp nhận nhỏ; không gật theo từng từ hay tự mấp máy lời Khoai.
- Partner reaction/voice intent: Khoai không cần đòi hỏi Đào phải ngưỡng mộ; cô nghe vì tò mò. VOICE giữ trầm ấm/kể thân mật; phân câu có ý, không bịa measured pause hoặc ép đọc nhanh vì 30s. Không thêm “à”, chuckle hoặc tiếng cười.
- Framing/observable: PA giữ mặt Khoai đến hết ý; góc mắt phải nối tới Đào trong địa lý bàn. Success cần nét nhớ chuyển thành nét tinh nghịch đủ chuẩn bị N04, không phải mọi still đều cười. Failure: gaze trở thành nói với khán giả; miệng người nghe nhận câu anh; toàn đuôi câu chỉ còn món không đúng coverage214. Native có mặt một phần, chưa được chọn trọn take.

### R03 — Tò mò và câu đáp đổi nghĩa

- Mục tiêu/obstacle/tactic: Đào muốn làm rõ “đứng chờ”, hỏi thật bằng N03. Khoai đáp thật ngắn nhưng tỉnh bơ, để cô tự hiểu chuyện ăn vụng; không giải thích thêm vì đó là nơi ý hài hình thành.
- Attention → inference → emotion: mặt Đào hỏi anh → câu hỏi là tiếp nhận lời ký ức → tò mò; anh trả lời “quay lưng” → điều “chờ” hóa ra là cơ hội ăn vụng → vui nhẹ, dự cảm hành động sau.
- Before → cue/turn → after: Đào tiếp nhận cuối N02 → hỏi N03 → Khoai đáp N04; cô nhận ý bằng nét mắt/cười nhỏ sau cue, rồi mới chú ý cốc ở R04. Không diễn sẵn vẻ “biết ngay” trước câu trả lời.
- Gaze/body/face/hand: Đào nhìn Khoai, nâng mày nhỏ/đầu nghiêng ít nếu hữu ích; thân vẫn adult, không lắc đầu/nhảy vai kiểu trẻ con. Khoai giữ ánh nhìn và thân yên có chủ ý, nét cười kín sau đáp; không nháy mắt camera, vỗ tay hoặc khoe sự láu lỉnh. Hai người chưa dùng đũa/đưa bát nhận A.
- Partner reaction/voice intent: người nghe không mấp máy nói thay; cô có khoảng nhận ý, anh đón phản ứng tự nhiên. VOICE N03 tò mò; N04 đều và có ý cười kín, không nhấn thành tuyên bố thắng cuộc. Không dùng timecode từ audio v0.5.
- Framing/observable: hai mặt đọc được ở đúng hai lượt. Failure: Khoai chỉ đơ chờ lượt; Đào cười chế giễu; chuyển sang cốc trước nhận ý khiến lời/hành động không nối. Board180 chỉ là ứng viên mặt, chưa chứng minh đủ lượt–nhịp–miệng.

### R04 — Cốc là mục tiêu tự nhiên, A là ý định ăn

- Mục tiêu/obstacle/tactic: Đào lấy cốc trong bữa ăn, hoàn toàn không gài Khoai. Khoai thấy cô đang bận nên tranh thủ gắp A cho mình; obstacle là có người bạn ngay cạnh, tactic là nhanh gọn với đũa, không rón rén sân khấu.
- Attention → inference → emotion: Đào nhìn cốc/tay lấy cốc → cô tạm không nhìn anh → cơ hội; A từ P hướng về miệng Khoai → anh định ăn thật → người xem chờ bắt gặp trước cô.
- Before → cue/turn → after: F0 và A còn P → cô thực chuyển chú ý tới cốc → anh gắp A, đũa nâng về mình → F1. Khoai không bắt đầu đổi hướng cho Đào trong khung này. Cô không liếc canh anh trước lúc quay lại.
- Gaze/body/face/hand: mắt Đào đi tới cốc trước tay, quay thân/đầu vừa đủ lấy; không quay lưng cả người gượng để tạo plot. Khoai nhìn P/A, thân nghiêng vừa đủ ăn, miệng chỉ chuẩn bị đón A khi cần và chưa contact. Không mở miệng quá to, cúi đuổi A hoặc bật vẻ hoảng hốt. Không thêm lời/tiếng cười.
- Framing/observable: cần thấy người lấy cốc và mặt/hướng đũa Khoai trong cùng địa lý; contact insert bổ sung không thay chứng cứ ý định. Success phải phân biệt A về Khoai với gắp cho Đào ngay từ đầu. Failure: source bắt đầu đã giữ A mà không có nguồn gắp nối hợp lệ; Đào chăm chăm nhìn anh; A hướng bát cô từ đầu. Board163 có các trạng thái liên quan, chưa chứng minh F0→F1/cả motion.

### R05 — Bắt gặp, biết bị thấy, khựng nhỏ

- Mục tiêu/obstacle/tactic: Đào quay lại và phát hiện A đang về Khoai; cô trêu sự lặp lại câu “quay lưng”. Khoai vừa muốn ăn vừa muốn giữ thể diện; khi gặp ánh nhìn cô, anh ngừng ý định ăn trước đổi tactic.
- Attention → inference → emotion: cô nhìn A rồi anh; anh gặp mắt cô → hai người cùng biết anh vừa tranh thủ → hài thân thiện. Đây là cue đổi ý, không chỉ hai mặt đang cười.
- Before → cue/turn → after: F1 → ánh nhìn Đào về A/anh → Khoai biết bị thấy, khựng nhỏ → F2; N05 sau phát hiện. A vẫn trên đũa, chưa chạm miệng/chưa chuyển sang bát. Cốc theo trạng thái đã có, không tự teleport khỏi tay.
- Gaze/body/face/hand: Khoai dừng việc đưa A tới miệng, mắt chuyển tới cô, độ nghiêng/miệng thu lại nhẹ; tay vẫn giữ chắc A. Đào nhìn cụ thể, nét mày/cười có ý trêu; không cau có, chỉ tay buộc tội hoặc trợn mắt đạo đức. Không biến Khoai co rúm/ngượng trẻ con.
- Partner reaction/voice intent: Đào nói trực tiếp với anh, Khoai nghe và giữ một nhịp nhận biết. VOICE N05 có ý hỏi trêu, không giọng kiểm soát. Chưa đo nhịp “khựng”, không ép frame freeze.
- Framing/observable: cần cả A lẫn hai mặt hoặc chuỗi cut không mất cue nhìn→biết→khựng. Failure: N05 trên cận món; anh đã đổi hướng trước cue; phản ứng cận cô không thấy đối tượng và không nối được tới anh. Board194 chỉ có cô/cốc không chứng minh phát hiện A; sheet163 không thay playback nhân quả.

### R06 — Chữa cháy có chủ ý rồi đổi hướng

- Mục tiêu/obstacle/tactic: Khoai muốn giữ thể diện sau bị thấy; tactic là biến ý định ăn thành lời mời gắp cho cô bằng N06 và đổi đường A. Sắc hài đến từ sự bình thản có chủ ý, không từ hoảng hốt hoặc gian dối ác ý.
- Attention → inference → emotion: mắt/mặt Khoai nhận cô → đũa đổi về vùng bát cô → anh đang chữa cháy → vui vì người xem và Đào hiểu. Giữ trước–sau đủ phân biệt ý định cũ với tactic mới.
- Before → cue/turn → after: F2 → anh lấy lại vẻ bình thản, đáp N06 và đổi hướng A sau biết bị thấy → F3. Thứ tự giữa onset câu và chuyển đũa có thể phối trong cùng nhịp sau cue; không đặt con số/pause trước kiểm thật. Không thả A sớm.
- Gaze/body/face/hand: anh nhìn cô, nét cười kín; thân thôi hướng vào miệng mình và trở lại hướng bạn/bàn. Tay đổi quỹ đạo gọn trong vùng an toàn, không vung đũa giải thích. Đào theo A rồi anh, hiểu lời trước đưa bát; không tin ngây thơ hoặc mở miệng chờ đút.
- Partner reaction/voice intent: Đào không cần đáp mới; ánh nhìn cô đủ cho thấy tiếp nhận. VOICE N06 đều, ấm, kín nét chữa cháy; không whisper để giấu hoặc nói quá nhanh. Miệng anh cần khớp đúng câu trong media; ảnh không chứng minh.
- Framing/observable: mặt Khoai và đường đổi hướng có liên hệ. Failure: source chỉ có tay nghỉ/mặt nói; A vốn hướng cô ngay từ đầu; cận tay thay toàn bộ cảnh nói thấy mặt. Board154 có mặt/mẫu miệng, không có A trên đũa để thực hiện F2→F3.

### R07 — Hiểu lời và nhận bằng bát

- Mục tiêu/obstacle/tactic: Đào muốn nhận miếng nem và đáp lại trò chữa cháy một cách thân thiện. Tactic là nhìn A rồi nhìn anh, đưa bát và nói N07; cô đồng ý chơi cùng lời anh, không tin nguyên văn ngây thơ hoặc tuyên bố thắng.
- Attention → inference → emotion: A → mắt Khoai → bát nhận → cô đã hiểu và cho anh lối ra → sự ăn ý giữa bạn. Nét cười là phản ứng có nguyên nhân, không phụ kiện cố định.
- Before → cue/turn → after: F3, A còn kẹp → cô đọc hướng mời/tactic → đặt cốc nếu còn cầm để đưa bát thuận, rồi đưa bát trong vùng nhận, N07 đúng lượt → A vẫn trên đũa ở vùng bát. Việc đặt cốc là choreography theo role04 để nối trạng thái, không thêm trò diễn uống nước hoặc lời mới.
- Gaze/body/face/hand: cô giữ khoảng cách tự nhiên ở bàn, bát hướng dưới A; mắt từ A lên anh, cười nhỏ tự tin. Không nghiêng sát mặt anh, chu môi, đưa bát kiểu phục tùng hay mở miệng đón A. Khoai nghe, giữ tay ổn định và mắt đón cô; không mấp máy N07.
- Partner reaction/voice intent: Khoai hiểu cô biết, không phải bị cô làm xấu mặt. VOICE N07 nhẹ, tỉnh và có ý trêu; không cười thành tiếng thêm vào script. Bát là nơi nhận rõ ràng, không thay bằng bàn tay hoặc miệng.
- Framing/observable: hai mặt, A, bát và tay đưa bát phải nối được. Failure: cô tỏ vẻ thắng/khinh; bát đã có A trong khi A vẫn trên đũa; nhận không có cue; miệng anh minh họa câu cô. Chưa có nguồn R07 trọn được chứng minh.

### R08 — Thực hiện lời gắp, khép A

- Mục tiêu/tactic: Khoai hoàn tất việc gắp cho cô; cô giữ bát ổn định để nhận. Không thêm màn chăm sóc/đút hoặc câu thoại.
- Attention → inference → emotion: A/đũa/bát → A thực được thả vào bát → lời chữa cháy đã trở thành hành động, nhẹ nhõm.
- Before → cue/turn → after: A còn kẹp trên vùng nhận, bát ổn định → đũa mở đúng trên bát → F4, A trong bát, đũa rời vùng nhận. Không thả hai lần hoặc cắt từ còn kẹp sang đã có A mà không thấy/đọc được việc thả.
- Gaze/body/face/hand: chú ý tay/đường thả, không kéo bát đuổi đũa; người nhận không cúi miệng theo A. Mặt có thể ngoài insert ngắn nếu R06/R07 đã có chức năng nói/nghe rõ. R08 có thể gộp R07 đúng214 nếu toàn hành động đã rõ; ACT không quyết số shot.
- Observable: giữ cùng A, cùng bát/tay qua cut; kết thúc thả rồi mới lấy B. Không có actual board R08 riêng được mở trong run này; nguồn207 là ứng viên lịch sử trong215, không được ACT kiểm mới hoặc nhận đạt.

### R09 — Tiếp tục bữa ăn, cùng hiểu

- Mục tiêu/tactic: Đào giữ niềm vui nhỏ của việc vừa hiểu anh; Khoai bình thản tự gắp phần mình. Không cần cú chốt thắng/thua hoặc thêm một trò đùa.
- Attention → inference → emotion: hai mặt/bàn, A trong bát cô, B từ P → cả hai ăn tiếp và hiểu chuyện → kết ấm, hài nhẹ.
- Before → cue/turn → after: F4 → Đào cười nhẹ sau nhận; Khoai tự gắp B khác → A vẫn bát cô, B rời P trên đũa anh. Chưa thêm việc B vào miệng/nhai nếu bản khung chưa cần; không dùng B để giả đường A.
- Gaze/body/face/hand: một ánh nhìn chia sẻ rồi anh chú ý lấy B; cô cười nhỏ, không kéo dài gaze tình cảm, chạm nhau hoặc leaning sát nhau. Khoai có nét cười kín, không ngượng cúi đầu hoặc khoe thắng. Tay cô giữ/hạ bát theo continuity R08; chưa tự chốt trạng thái bàn khác.
- Voice/framing/observable: không thêm thoại/tiếng cười; trở lại khung chung đủ hai mặt và bàn. Board209 có bát cô chứa món, đũa anh ở P rồi giữ món trong các mẫu, là ứng viên nghiên cứu. Chưa chứng minh món trên đũa là B sau A, chưa nghiệm thu nụ cười/chuyển gaze liên tục hoặc join R08→R09.

## 4. Hai mức diễn cùng ý đồ, phối VOICE và coverage PA/PB

So sánh dưới đây là thiết kế để lựa chọn trên media thực, chưa là hai candidate đã chạy. Không đồng nhất “ít biểu cảm” với “đúng nhân vật”, cũng không mặc định mức cao hơn là hấp dẫn hơn.

| Nhóm | Mức restrained — khuyến nghị baseline giấy | Mức slightly expressive — biến thể cùng khóa | Ngưỡng quá đà cần loại khi review |
|---|---|---|---|
| R01–R03 nhớ/hỏi/đáp | Tay ít động, gaze tới bạn rõ, khóe cười kín; Đào nâng mày nhẹ khi hỏi, nhận ý sau đáp. | Chuyển mắt/thân tới bạn rõ hơn, một nét mày/đầu nhỏ khiến cue nghe dễ đọc; Khoai hé nét vui sau N04 rõ hơn. | Chỉ trỏ như thuyết trình, nói nhìn lens, cười rộng liên tục, Đào búng người/giọng toddler, nháy mắt báo trước trò. |
| R04–R06 tranh thủ/bị thấy/chữa cháy | Gắp nhanh gọn, dừng đũa/miệng nhỏ khi gặp mắt, lấy lại bình thản rồi đổi A. | Một thay đổi gaze và ngừng body rõ hơn để đọc ở khung dọc; vẫn không giật nảy, drop A hoặc nhăn nhó. | Rón rén sân khấu, hoảng, mở miệng quá to, Đào rình/gài, Khoai tiếp xúc A rồi chữa cháy. |
| R07–R09 nhận/kết | Đào nhìn A→anh, cười nhỏ và bát nhận; Khoai tự lấy B, nét cùng hiểu vừa đủ. | Nụ cười/nhận ý cô rõ hơn và ánh nhìn trả lời anh rõ hơn; vẫn bữa ăn bình thường. | Tuyên bố chiến thắng, ngượng bị phạt, kéo dài gaze romance, nghiêng sát nhau, chờ đút, tiếng cười/lời thêm. |

Baseline restrained là khuyến nghị ACT theo trầm ấm/tinh tế đã khóa, không approval output. Nếu framed nhỏ làm cue không đọc được, tăng độ rõ của ánh mắt và thay đổi có nguyên nhân trong slightly expressive; không tăng mọi nét mặt đồng loạt. Hai mức cùng A/B/F0–F4/text/voice identity. Không thí nghiệm thay động cơ Đào hoặc quan hệ.

VOICE handoff giữ intent N01 nhẹ trêu; N02 kể ấm có ý; N03 tò mò; N04 đáp tỉnh; N05 vừa phát hiện rồi hỏi trêu; N06 bình thản giữ thể diện; N07 hiểu và đáp lại. VOICE quyết realization/phát âm/prosody, SIA/AV kiểm actual heard_text/identity/mouth attribution. ACT không chèn word, chuckle, cười phát tiếng hoặc đổi pitch/speed để vừa 30s. Tiny smile/breath/pause chỉ là direction proposal; nếu phát tiếng ngoài script thì không tự triển khai. Timing22,055s/30s trong215 là dữ liệu kế thừa, không ngân sách diễn đã đạt.

**PA của DIR — giữ coverage R02 thấy mặt Khoai hết ý:** ACT giữ posture/gaze/nét kể xuyên phần “anh đứng chờ”, rồi Đào nhận và hỏi. Khoảng thiếu không được vá bằng một nụ cười đứng, loop hoặc đổi tốc độ. Bổ sung source cần tiếp diễn acting/mouth/speaker, không chỉ trùng tạo hình. Chưa có nguồn được chứng minh đủ phần thiếu. Giữ214 không mở lại lựa chọn owner; candidate/bản thử vẫn checkpoint217, generation nếu cần approval request riêng.

**PB của DIR — cuối N02 chuyển sang Đào nghe:** đây là change candidate coverage, **OWNER_PB_APPROVAL_NOT_RECORDED**. Nếu owner duyệt diff trước lock, cue của Đào phải là đang nghe ở F0, nhận cụm “đứng chờ” rồi mới hỏi N03. Không diễn Đào nói câu Khoai; miệng người nghe không mang chuỗi phát âm, không lấy cốc/đưa bát sớm. Board194 có cốc và miệng mở trong các mẫu nên không tự chọn làm listener F0; tailnative201+ chỉ ứng viên, chưa xác nhận im lặng. ACT không tự áp PB, không tự kéo tail về sớm, không tuyên bố PA/PB đã có hiệu quả thực.

## 5. Đối chiếu ảnh thực — observed tách khỏi diễn đề xuất

| Artifact / vị trí ảnh thực | Quan sát trong sampled frames | Giá trị có thể nghiên cứu / giới hạn |
|---|---|---|
| OPEN_v0.7 | Khoai trái, Đào phải, hai mặt và tay/bát/cốc hiện; hai nhân vật hướng chú ý xuống vùng bàn; nét cười nhỏ. | Có điểm tựa geography/body/bàn. Still không chứng minh adult listening liên tục, tự nhiên, quan hệ couple/friend hoặc đủ state R01–R09. Quan hệ bạn bè lấy từ khóa nội dung. |
| Native71→72, anchors f31/55/70/94/109/128/137/143/161 | f71 hai mặt, Đào nhìn về Khoai; f72 cận Khoai, mắt khá gần hướng máy; f109/137/143 có miệng mở/nét vui rõ, f128 miệng khép. f163 có Đào ở mép khung. | Có coverage và trạng thái mặt khác nhau để kiểm N02, không phải toàn N02 thiếu mặt. Chưa biết hướng nhìn liên tục có tới Đào, nét cười có làm ký ức ấm hay diễn quá rộng, hoặc từng trạng thái miệng khớp từ nào. Không gọi một ảnh miệng mở là sai khẩu hình. |
| Native163→164 và200→201; board face/dish boundary | f163 có mặt Khoai; f164/200 chỉ món; f201 hai mặt nhìn nhau. | Xác nhận vùng mất mặt tại cut. [164,201) / 6,833333–8,375s kế thừa216, ảnh cặp xác nhận boundary nhưng ACT không probe/tính frame mới. Speech overlap ~0,507s là ASR hint đọc qua216/DIR, chưa nghe/align phoneme. |
| Board180-A02, mẫu0,833750/3,335000/5,002500/7,503750/9,171250s | Hai mặt tại bàn; các mẫu lần lượt có miệng Đào/Khoai mở; tay gần bát, không mẫu thấy ý định kéo P. | Ứng viên talk/listen. Sampling không xác minh đúng N01–N04 hoặc người nghe yên miệng giữa mẫu; không có bằng chứng kéo→dừng. Nhãn trên board không là EDL chọn cuối. |
| Board180-A03, mẫu6,670000s trở đi | Hai mặt, tay nghỉ; bàn chỉ thấy đĩa, không bát/cốc/rau/chấm như OPEN7; có chữ “Chờ mẹ quay lưng”. | Mặt rõ không bù missing prop choreography R01/R04/R07. Chữ trên hình không chứng minh ai phát âm. Không sửa/ref canon theo A03. |
| Board163-R02, mẫu0/0,666667/2/4/4,666667s | Ngay mẫu0 Khoai đã cầm đũa có phần nem; mẫu0,666667 đũa/miếng gần miệng và miệng mở; Đào có các mẫu hướng xuống cốc, sau đó hướng về anh. | Có states liên quan lấy cốc/giữ A/gaze; chưa chứng minh A từ P và anh khựng trước đổi hướng. Không kết luận contact hoặc no-contact từ khoảng ảnh mẫu. Không coi source trọn R04–R06 đã đạt. |
| Board194-R203, mẫu0/1,333333/2,666667/6,666667s | Cận Đào cầm cốc, có mắt hướng xuống/bên và miệng mở ở một số mẫu. Không thấy A/Khoai. | Candidate phản ứng riêng, chưa đủ caught cue hoặc listener im lặng F0 cho PB. Miệng mở có thể là speaking/expression, không nhận sai lời/speaker khi chưa nghe/playback. |
| Board154-R01, các mẫu0–7,333333s | Hai mặt, Khoai và Đào có các mẫu miệng mở đúng kiểu cảnh đối thoại; tay nghỉ trên bàn, không thấy A trên đũa hay bát đưa ra nhận. | Là nguồn nghiên cứu mặt/lời lịch sử, không trọn hành vi R06/R07. Đối với nhiệm vụ F2/F3, mẫu đang thấy không thực hiện đường A; chưa suy toàn video không có gì khác giữa mẫu. |
| Board209-U08, mẫu0/1,333333/2,666667/4/7,333333s | Bát Đào có món; đũa Khoai ở vùng P trong một số mẫu và sau đó giữ phần món; cô nhìn anh/cười nhỏ. | Candidate kết có state liên quan R09. Chưa xác minh A đã thả trước đó, B là miếng khác, join/thời lượng hoặc trạng thái miệng im lặng liên tục. |

Những ảnh này chỉ hỗ trợ phân loại coverage/state và định hướng câu hỏi kiểm. Không dùng việc source tên “reaction”, “visual_lock”, “low-hold” làm bằng chứng ý định/thành công. Không xếp hạng sức hài/retention hoặc khẳng định có biểu cảm đạt liên tục từ contact boards.

## 6. Findings, severity, status và điều kiện đóng

MET dưới đây chỉ áp paper adherence; DEFECT có scope ảnh cụ thể; UNKNOWN là khoảng chưa được kiểm, không lỗi diễn quan sát toàn video. Không có finding MAJOR nào được đóng trong report này. Root không lấy report maker thay PERF/SIA/CONT độc lập.

| ID / rule / status / severity | Evidence / expected–observed / impact | Action, route, owner và closure evidence |
|---|---|---|
| ACT218-C01 / text–speaker–intent khóa / MET / N/A severity | Score dùng đúng178/214, natural-cup/caught-before-redirect/bowl/A→B/friends theo213; không sửa lời. MET chỉ trên thiết kế. | Root đối chiếu khi tích hợp SHOT/EDL. Không mở lại lựa chọn owner đã khóa; MET paper không đóng media gates. |
| ACT218-F01 / R02 mặt người kể / DEFECT trong vùng native đã thấy / MAJOR | Native163→164,200→201: cuối coverage chuyển thành món không mặt; expected R02 thấy Khoai hết ý theo214. Speech overlap là hint216, không nghe mới. Mất cơ hội đọc nét kể cuối ý nếu dùng nguyên coverage. | DIR/EDIT/DOP/ACT xử lý PA; PB chỉ sau owner diff approval. PERF+SIA/AV kiểm candidate/bản nối. Closure: đúng source/hash/range, mặt/người nghe theo coverage approved, actual AV/acting review; chưa đóng. |
| ACT218-F02 / hướng chia sẻ và biên độ N02 / UNKNOWN / MAJOR nếu mất quan hệ/ý | f72/94/109/128 có gaze gần camera, f109/137/143 nét vui/miệng mở rõ; f71/201 có gaze qua lại. Expected chia sẻ thân mật tới Đào, không thuyết trình. Still chưa chứng minh gaze turn hoặc diễn quá rộng. | DOP/ACT phối envelope, PERF cold xem motion để đọc ai đang được nói với và chuyển nhớ→tinh nghịch. Không sửa CHAR identity. Owner chỉ nếu đổi POV/coverage approved. Closure: clip/bản nối version cụ thể, frame/time và review continuous; chưa đóng. |
| ACT218-F03 / R01 kéo→dừng theo Khoan / UNKNOWN / MAJOR | Board180-A02/A03 mẫu tay nghỉ, không mẫu xác nhận ý định kéo P rồi dừng. Expected có hành vi nguyên nhân; thiếu chứng minh không đồng nghĩa mọi file không có. | EDIT kiểm đoạn ứng viên sâu; ACT/SHOT giữ cue tay và speech đúng. PERF/CONT kiểm cut. Closure: source-range cho start→cue→stop và R01 nối N02, đúng hash; chưa đóng. |
| ACT218-F04 / R04–R06 ý định→caught→khựng→redirect / UNKNOWN / MAJOR | Board163 bắt đầu đã giữ A và có mẫu gần miệng; board194 chỉ cô/cốc, board154 tay nghỉ. Chưa chứng minh cả chuỗi hoặc contact boundary. Nếu thiếu nhân quả, chữa cháy mất nghĩa dù text đúng. | ACT/EDIT map source/gaps theo F0–F3; PERF cold không tiếng, CONT kiểm A/miệng/cốc và full AV sau G2/G3. Không owner change cho việc sửa đúng khóa; trình nếu thay nhiệm vụ. Closure: playback thật và source/cut evidence đủ chuỗi, A đổi trước contact; chưa đóng. |
| ACT218-F05 / R07–R09 bowl receive/A–B / UNKNOWN / MAJOR | Board154 chưa có A/bát đưa nhận; board209 bát đã có món và đũa ở P/rồi giữ món. Chưa có R08 actual được ACT xem; chưa rõ join A thả→B gắp. | EDIT/SHOT phối body/prop states; CONT/PERF kiểm thả một lần, cô hiểu rồi nhận, kết bạn bè. Owner nếu bỏ/đổi ending. Closure: trước/sau cut đúng source/hash và continuous review R07–R09; chưa đóng. |
| ACT218-F06 / hearing/motion/lip-sync/full AV/timing / UNKNOWN / MAJOR gate HOLD | Actual tools chỉ text/ảnh; chưa nghe/xem AV liên tục. 22,055s và7,945s không chứng minh nhịp/hài/30s, ASR không là heard_text. | Root bố trí capability/human checkpoint217 trong Flow/local được phép; SIA/AV/PERF kiểm đúng target. Closure: report người/công cụ thực nghe/xem, version/hash, actual line/miệng/nhịp, owner checkpoint tương ứng; chưa đóng. |
| ACT218-F07 / PB listener provenance và approval / UNKNOWN / MAJOR nếu áp khi chưa duyệt | DIR ghi PB thay coverage214; chưa approval PB. Board194 cầm cốc/miệng mở không tự chứng minh listener F0; tail201+ chưa im lặng verified. | Giữ PA baseline và PB CHANGE_CANDIDATE. DIR/root trình diff+bản thử nếu muốn dùng; owner duyệt coverage trước lock, mỗi generation approval riêng. Closure: decision record đúng artifact + candidate listener actual AV/continuity review; chưa đóng. |

Không quan sát được romance/scolding/contact thực thì không ghi DEFECT các lỗi đó. Đây là tiêu chí lỗi cần kiểm trên media, không khẳng định lỗi đã xảy ra. Props/món khác giữa source là dependency FOOD/CONT: ACT chỉ nêu ảnh ảnh hưởng hành vi nhận/gắp, không tự chọn canon mới hoặc phán món đúng/sai toàn bộ.

## 7. Handoff và tổng hợp năm mục

1. **Đã xác định:** performance score đủ R01–R09, objective/tactic/attention/cue/change/observable và listening behavior; đã xem reference, ba board216, sáu native boundary và sáu board215. Native N02 có mặt một phần; cuối coverage món là khoảng thiếu theo214. Các source chuỗi A/bát có states hữu ích nhưng chưa đủ chứng minh diễn liên tục.
2. **Quyết định đã chốt:** kế thừa178/212–217; R1 không tạo approval mới. Giữ từng chữ/speaker, natural cup, khán giả biết trước, caught→redirect, A vào bát rồi B, bạn bè và hai giọng đã chọn. PA là đề xuất giữ coverage approved; PB còn change candidate, owner chưa duyệt PB. Không hỏi lại các khóa này.
3. **Giả định đang sử dụng:** restrained là baseline giấy có thể tăng độ rõ trong same intent; OPEN7 là diagnostic; audio202 giữ nguyên cho comparison đầu theo DIR; 30s là target chưa đo; range native/timing/hash dùng nguồn216/218/DIR, không xác minh mới. DOP envelope chưa tích hợp nên handoff framing là nhu cầu, không shot lock.
4. **Vấn đề còn mở:** F01–F07 giữ trạng thái nêu trên; chưa có trọn R01 kéo–dừng, N02 end face, causal R04–R08 và join A/B được nghiệm thu. Hearing/motion/lip-sync/full AV/timing HOLD. Independent PERF/CONT/SIA và checkpoint owner vẫn cần; không giao toàn trách nhiệm tìm lỗi cho owner.
5. **Bước tiếp nên thực hiện:** root tích hợp DIR/DOP/ACT/EDIT rồi reviewer độc lập cold theo scope; SHOT đưa cue/prop states vào bản thử có nhãn NOT_RELEASE ở G1. Ưu tiên chứng minh N02 G2, sau đó R04–R08 G3 và ending; G4 kiểm không tiếng+có tiếng trên fullscene đúng hash, G5 kiểm export. Nếu source thiếu, CTD/PROMPT/FLOW lập exact brief/route/quote/output/cap/criteria để owner duyệt riêng; report này không cấp quyền thử trả phí hoặc cài thêm tool. Closure phải bằng artifact/version/media evidence thực, không bằng lời khẳng định prompt đã tuân thủ.
