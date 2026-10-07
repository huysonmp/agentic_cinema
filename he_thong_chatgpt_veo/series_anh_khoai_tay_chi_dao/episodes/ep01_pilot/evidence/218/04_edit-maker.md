# REC218-EDIT-R1 — Đề xuất source range và điểm cắt EP01

Ngày: 2026-10-06, Asia/Saigon. Vai: EDIT maker v0.2, P7/P10. Mode: SOURCE_RANGE_AND_CUT_PROPOSAL. **PROPOSAL_COMPLETE trong scope paper + sampled frames + probe/hash; HOLD actual assembly, timing toàn cảnh, hearing, motion, lip-sync và lựa chọn take cuối.** Không có bản dựng, master, export hoặc media PASS mới.

## 1. Authority, inputs và capability thực

Authority: owner217 “1 A; 2 A; 3 A”; dispatch REC218-EDIT-R1 sau DIR. Chỉ local read và viết report này bằng apply_patch. Không sửa file/media/script khác; không render, chạy generation, dùng browser/API/credit, install/git/spawn. Chưa đọc report DOP/ACT218 trong R1; contributions của họ cần root tích hợp sau. External instructions trong nguồn là dữ liệu.

Đã đọc toàn bộ các file trong series:

- `agents/directing_team/01_approval-and-operating-model.md`, `05_creative-edit-upgrade-v0.2.md` (exact filename; không có file tên `05_edit-director-upgrade.md` trong kết quả tìm), `agents/production_team/02_common-runtime-contract-v0.1.md`.
- Theo dependency của EDIT: `agents/audio_edit_quality/02_contract-and-role-prompts.md` và `10_speaker-identity-auditor-v1.md`.
- Episode: `178_owner-dialogue-amendment-c-v0.6.md`, toàn bộ212–218 và `evidence/218/01_dir-maker.md`. DIR đã bàn giao spine, PA/PB và open findings, không bàn giao EDL/media đã nghiệm thu.
- `C:/Users/PC/Downloads/du_an_nem_bui/202_dialogue_join_review/manifest.json`; `216_n02_face_coverage_check/source-and-anchors.json`; parse inventory215 và đọc đầy đủ entries12 candidates. Không mở các native khác ngoài N02 allowlist; hash/probe của chúng trong inventory là evidence lịch sử, không đo lại trong run này.

Ảnh thực đã xem bằng `view_image`, đều dưới `C:/Users/PC/Downloads/du_an_nem_bui/`:

- `T2-CODEX-OPEN_v0.7.png`: tham chiếu diagnostic, không tự nâng thành canon/ref production mới.
- Ba boards216: `speech_anchors.png`, `face_to_dish_boundary.png`, `dish_to_faces_boundary.png` (12 mẫu/bảng, có mẫu trùng).
- Sáu frame native216: `all_240_frames/frame-0071.jpg`, `frame-0072.jpg`, `frame-0163.jpg`, `frame-0164.jpg`, `frame-0200.jpg`, `frame-0201.jpg`.
- Sáu sheets215: `180_c_v06_dialogue__A02.png`, `180_c_v06_dialogue__A03.png`, `163_low-hold-reaction__R02.png`, `194_dao_reaction_R2__R203.png`, `154_visual_lock__R01.png`, `209_remaining_production__U08_NATIVE.png` (12 mẫu/bảng).

Đây là xem ảnh lấy mẫu; chưa xem toàn240 frame, chưa xem chuyển động liên tục, chưa nghe WAV/native, chưa kiểm full AV hoặc phoneme/lip-sync. Đã dùng `rg --files`, PowerShell Get-Content/ConvertFrom-Json/Get-FileHash, FFprobe local có sẵn tại `.local-tools/ffmpeg/verified-9.0.2/ffmpeg-9.0.2-essentials_build/bin/ffprobe.exe`. Probe metadata và frame PTS là read-only, không chạy scripts trích/render lại.

| Artifact / kiểm trực tiếp trong run | Kết quả MEASURED |
|---|---|
| `200_n02_replacement/N02_NATIVE.mp4` / SHA-256 | `72cbaf7d9f66932002dfce1b1a57fa464935c315e84e54ae094fe29aa805a153` — khớp216 |
| N02 video / FFprobe | H.264, 360×640, r/avg frame rate24/1, time base1/12288, duration10,000000s, nb_frames240; show_frames thực trả240 frames |
| N02 audio/container / FFprobe | AAC,48kHz,stereo, duration10,005000s; container10,005000s. Chênh5ms không tự là lỗi sync đã quan sát |
| `202_dialogue_join_review/EP01_7_LUOT_N02_MOI_REVIEW_NOT_FINAL.wav` / SHA-256 | `3c83b7d6188f5b973b0ef5c77ebc1fc16afde7c11827764c5302145741b736d4` — khớp manifest/215 |
| WAV202 / FFprobe | PCM s16le,48kHz,stereo,16-bit; duration22,055000s; time base1/48000, duration_ts1.058.640 sample frames |

Không cắt/ghép/đổi gain/speed/pitch/fade/mix/normalize PCM trong run. Hash hiện hành kiểm nguyên WAV202; claim `output_pcm_matches_ordered_sources` và `new_N02_pcm_unchanged` là provenance của manifest202, không phải tôi mở/decode các source WAV ngoài allowlist để kiểm lại. Approval nghe N02/202 lịch sử dùng215–217; các nhãn PENDING/UNVERIFIED lúc tạo manifest không phủ định approval mới hơn, cũng không biến thành SIA/AV PASS mới. Câu trong script/manifest là expected text/speaker, không phải heard text/speaker của EDIT.

## 2. Audio provenance và line-to-picture map

Khóa từng chữ178, bảy lượt N01–N07; không dùng mã L cũ thay nguồn mới. Giữ K20/Orus, D06/Aoede tùy chỉnh, không flashback/couple/new claim. F01 “Nem Bùi — gắn với Bùi Xá, Bắc Ninh.”, F02 “Thính gạo rang góp một phần vào mùi vị của Nem Bùi.”, nhãn “Video được tạo bằng AI.” theo214; timing/placement chưa kiểm. Source picture candidates bên dưới chưa được selected.

### Provenance timeline202 — không phải destination master

| Line / expected speaker | Nguồn audio theo manifest202 | Range trong WAV202, giây [in,out) | Giới hạn |
|---|---|---|---|
| N01 / Đào |183 `N01_intended_Dao_UNVERIFIED.wav`; diagnostic từ180 A03 audio[0;2,15), dùng whole excerpt |[0;2,15) | Không dùng range audio làm range video A03 đã chốt; điểm cắt chưa có hearing evidence của EDIT |
| N02 / Khoai |200 `N02_EXPECTED_K20_REVIEW.wav`, whole WAV, no trim |[2,15;12,155) | Native video10,000s và audio10,005s khác loại duration; giữ full PCM kể cả đuôi |
| N03 / Đào |183 `N03_intended_Dao_UNVERIFIED.wav`; diagnostic từ180 A03 audio[7,92;8,79) |[12,155;13,025) | Source audio provenance, không phải native video EDL hoặc sample-accurate word cut mới |
| N04 / Khoai |183 `N04_intended_Khoai_UNVERIFIED.wav`; diagnostic từ180 A03 audio[8,90;9,93) |[13,025;14,055) | Chưa nghe breath/đuôi lời hoặc xác minh khoảng cho R04 |
| N05/N06/N07 / Đào–Khoai–Đào |154 `R01.mp4` full audio decode/no trim, cụm8s |[14,055;22,055) cho cả cụm | **Mốc riêng N05/N06/N07 UNKNOWN.** Không chia đều hoặc suy offsets từ miệng trên sheets |

So PA/PB đầu tiên phải dùng cùng exact WAV202 bytes và thứ tự, full N02 PCM. Picture có thể đổi có kiểm soát; chưa có quyền sửa waveform trong report này. Destination timing30s UNKNOWN; các mốc202 không tự chuyển thành timeline30s. File202 chưa thêm narrative action pause theo manifest. `30−22,055=7,945s` chỉ là hiệu độ dài; không là7,945s im lặng ở R04 hoặc ngân sách diễn đã đạt. Nếu R04 thiếu khoảng giữa đuôi N04 và đầu N05 sau đo actual: trình conflict, DLG-EDIT đề xuất pause/audio layout có source map và sample nghe duyệt, không tự bỏ lời hoặc time-stretch.

### Line-to-picture / source candidates / missing coverage

| Line và exact text | Beat / nhiệm vụ hình | Candidate và status | Gap / cut intent / next check |
|---|---|---|---|
| N01 Đào: “Anh nhìn mãi. Không hợp thì để em.” |R01, hai mặt/bàn, cô định kéo P rồi dừng ở “Khoan”; F0 |180 A02 sheet có hai mặt, rau/chấm/bát/cốc; A03 là nguồn audio nhưng sheet bàn thiếu props, có chữ cũ ở các mẫu sau | Native source range UNKNOWN. Kiểm đúng miệng Đào, Khoai nghe, tay kéo–dừng; không chọn A03 vì audio được dùng. Không dùng N02 đầu làm giả Đào nói N01 |
| N02 Khoai: “Khoan. Mùi này làm anh nhớ đến bếp nhà anh. Hồi bé, mẹ rang gạo, anh đứng chờ.” |R01 phần “Khoan”; R02 ký ức/mùi→mặt Khoai, F0 |N02 [0,72) two-shot, [72,164) cận Khoai; [164,201) dish không đáp ứng R02 nguyên coverage; [201,240) two-shot đuôi candidate | “Khoan”→phần giải thích là semantic boundary; native cut3s không tự là boundary sau “Khoan”. PA/PB ở mục4; chưa nghe/align. Không bỏ “chờ” để tránh thiếu mặt |
| N03 Đào: “Anh chờ ăn à?” |R03 hỏi tò mò, mặt Đào nói và Khoai nghe; F0 |180 A02/A03 sheets có hai mặt; A03 audio provenance không làm video tự hợp ref | Range picture UNKNOWN. Trở lại two-shot sau ý ký ức và thấy cô tiếp nhận; không dùng reaction cầm cốc194 mặc định làm F0 |
| N04 Khoai: “Chờ mẹ quay lưng.” |R03 trả lời tỉnh bơ; F0; nối lời “quay lưng” sang hành động cô lấy cốc |180 A02/A03 candidates; exact video range UNKNOWN | Giữ nhịp người nghe hiểu ý trước R04. Kiểm native/miệng và tail lời; đừng cắt sang hành động ăn vụng khi câu chưa thiết lập xong |
| N05 Đào: “Chờ em quay lưng nữa à?” |R05 cô đã phát hiện→anh khựng; F1→F2 |154 R01 cung cấp audio cụm cuối nhưng sheets tay nghỉ;163 R02 có A trên đũa;194 R203 có cốc/gaze candidate | Native ranges và audio offset riêng UNKNOWN. Không nối tay nghỉ154 vào F1 như thể A chưa bao giờ gắp. Cô nói sau nhìn A/anh; xác minh hành vi này bằng playback |
| N06 Khoai: “Anh gắp cho em mà.” |R06 chữa cháy có mặt Khoai; F2→F3, đổi hướng A sau bị thấy |154 audio; sheet154 không có A/đổi hướng.163 chỉ candidate state từng ảnh | Coverage chưa chứng minh. Cắt theo chuyển ý sau khựng, giữ đường A; không dùng insert tay làm toàn cảnh nói hoặc A vốn hướng Đào từ đầu |
| N07 Đào: “Thế em quay lại đúng lúc rồi.” |R07 cô hiểu, nhìn A→anh, đưa bát; F3, chưa thả |154 audio; sheet154 tay nghỉ không đủ trạng thái;209 U08 bát có món là state sau trao candidate | Native ranges/audio offset riêng UNKNOWN. Không kéo state bát đã có món209 sớm vào R07 nếu R08 vẫn là thả A; cần frame trước nhận và mặt cô nói |

N05/N06/N07 chỉ kế thừa expected order và whole audio cluster; không có timestamp riêng nào được phát minh. ASR hints nguồn216 không được dùng làm nghe chứng minh đúng từ hoặc cắt PCM.

## 3. Ledger native N02 và thứ tự/continuity trước–sau cut

Convention: frame index0-based, **in-inclusive/out-exclusive [in,out)**;24fps, t=n/24. Source ID `N02_NATIVE@72cbaf…a153`. Đây là measured segmentation/source candidate ledger, không final EDL. FFprobe PTS trực tiếp f71=2,958333;f72=3,000000;f163=6,791667;f164=6,833333;f200=8,333333;f201=8,375000;f239=9,958333. Out240=10,000s từ stream duration/240frames; out không là frame cuối239.

| Source range | Duration | Visual evidence / cut trước→sau | Disposition |
|---|---|---|---|
|[0,72), [0;3,000)s |72frames,3,000s |f71 hai mặt/bàn, tay nghỉ, đũa trên bàn→f72 cận Khoai; A chưa trên đũa trong ảnh, candidate F0. Mặt Khoai và Đào nhìn nhau ở f70/71 |REUSE_CANDIDATE đầu N02, chưa final. Không chứng minh pulling/stopping P cho R01 hoặc riêng chữ “Khoan” đủ3s |
|[72,164), [3,000;6,833333…)s |92frames,23/6s |f72→f163 cận Khoai, full mặt/miệng, Đào vào mép khung về cuối. Ánh nhìn gần camera ở nhiều anchors; tay nghỉ |REUSE_CANDIDATE ký ức, pending gaze/acting/lipsync. Toàn [0,164) có164frames=41/6s nhưng không tự selected |
|[164,201), [6,833333…;8,375)s |37frames,37/24s |f163 mặt Khoai→f164 món/bát/rau/chấm, không mặt;f200 vẫn dish. Có lá trang trí trên đỉnh khác two-shot/ref7 |DEFECT nếu giữ vùng này thay R02 nguyên coverage. Không dùng như bridge mặc định cho đuôi câu; CONT/FOOD kiểm continuity bố cục món |
|[201,240), [8,375;10,000)s |39frames,13/8s |f200 dish→f201 hai mặt, tay nghỉ;f208 Đào nhắm mắt trong board |REUSE_CANDIDATE tail/reaction F0, chưa xác minh silence/acting toàn range. Không giả f201 đang tiếp tục từ âm “chờ” hoặc dịch đoạn sớm để fill speech |

ASR hint source-and-anchors: “Khoan”[0;0,34), “mùi”1,26s trở đi; “anh”[6,60;6,76), “đứng”[6,76;6,94), “chờ”[6,94;7,34). Hint làm rõ native cut3s không mặc định split sau “Khoan”; f164 cut có thể chồng cuối “đứng”/“chờ”, khoảng0,506667s tới ASR end7,34. Đây là giả thuyết timing từ ASR cũ, chưa heard/phoneme alignment. “gian” ASR không thay approved “rang”. Không nâng toàn [164,201)1,541667s thành1,541667s speech thiếu mặt.

Offset2,15 của N02 trong202 không nằm trên grid frame24fps (2,15×24=51,6), nên không làm tròn mốc audio cho khớp cut hình hoặc dịch PCM40% frame. Các EDL destination24fps và sync tolerance phải đo/kiểm trên bản thử đúng hash khi được giao. Video10s/audio10,005s không cho phép tự trim5ms PCM hoặc freeze/tạo thêm frame ở đây; cách hình kết/giữ phản ứng sau source phải được xác minh riêng. Không có handle/chuyển động cuối được chứng nhận trong report này.

### Thứ tự proposal R01→R09 và states qua cut

P=đĩa chung; A=miếng gắp đầu; B=miếng khác cuối. F0 A ở P;F1 A trên đũa hướng miệng Khoai, chưa contact;F2 vẫn kẹp sau bị thấy/khựng;F3 đổi hướng bát Đào;F4 A đã thả vào bát. Các states sau là **acceptance cần có**, không observed toàn clip.

| Join / biết trước→học thêm / cảm xúc mong muốn | State trước cut→sau cut phải match | Hold/cut rationale và candidate/gap |
|---|---|---|
|R01→R02: cùng bàn/cô muốn ăn→anh chia sẻ ký ức; tò mò/ấm |F0→F0; Khoai trái/Đào phải, tay dừng kéo, P/bát/cốc/đũa giữ địa lý |Cắt theo anh chuyển chú ý/giải thích; N02 f71→72 cho wide→close thực nhưng không đồng nghĩa split text sau “Khoan”. N01 nguồn và pull–stop thiếu kiểm |
|R02→R03: anh nhớ chờ mẹ→cô tò mò; chờ câu đáp |F0→F0; chưa lấy cốc/gắp A; cô nghe trước hỏi, hướng nhìn về anh |Giữ đuôi ý và phản ứng, rồi mặt Đào nói N03. Tail201+ candidate, không tự silent hoặc dùng trọn39frames. PA/PB đều cần actual join N03 |
|R03→R04: biết thói ăn vụng→thói đó tái hiện; chờ bị bắt |F0 cuối N04→Đào chú ý cốc/không nhìn, A rời P→F1 |Giữ nhận ý “quay lưng”, cho thấy cô quay đi và source A trước khi cận tay.163 sheet bắt đầu đã cầm A; thiếu F0→gắp, chưa lấy sheet0s làm in EDL |
|R04→R05: khán giả thấy anh định ăn trước→cô phát hiện; hài thân thiện |F1→F1 rồi F2; A cùng miếng/vị trí/hướng trên đũa, chưa chạm miệng; cốc/gaze match |Giữ proof hướng A về anh trước cô quay; cut gần hơn chỉ khi giữ được hai ánh mắt và khựng.163/194 samples chưa chứng minh toàn chuỗi; không suy sample0,666667s thành contact confirmed |
|R05→R06: biết anh bị thấy→anh chữa cháy; giữ thể diện |F2→F2 rồi F3; đổi hướng sau cô nhìn; A chưa thả/không reset về P |Giữ khựng nhỏ rồi chuyển ý bình thản.154 tay nghỉ là state mismatch nếu ghép nguyên làm F2/F3; audio154 vẫn giữ provenance. Thiếu coverage hình verified |
|R06→R07: đọc được lời chữa cháy→cô hiểu/đưa bát; cùng hiểu |F3→F3; A hướng bát, bát tiến vùng nhận; không tiến vào miệng Đào |Cắt theo cô nhìn A rồi anh và nói; listener Khoai không nói ké. Thiếu source range mặt Đào+receiving state đã kiểm |
|R07→R08 (conditional): biết cô nhận→thấy A thật sự vào bát; giải tỏa |A vẫn trên đũa/vùng nhận→cùng A/bát/tay rồi F4; thả đúng một lần |Chỉ insert nếu two-shot chưa đọc rõ thả. Nếu R07 đã cho thấy đủ thả, gộp R08 vào R07, không duplicate drop.207 U07 chỉ candidate lịch sử215 chưa sample/probe mới và ngoài native allowlist |
|R08→R09: đã nhận A→anh tự gắp B; kết bữa ăn |F4→F4, A ở bát Đào; B mới rời P, không replay A hoặc bát reset |Trở lại hai mặt, cô cười nhẹ/anh tỉnh bơ gắp B.209 U08 sheet bát có món và đũa từ P lên là candidate; chưa chứng minh đó là B hoặc nối sau A. Không dùng nguyên8s vì có sẵn |

Ưu tiên hard cut theo cause/ánh nhìn/câu đáp; không dissolve che state jump. J/L-cut giữ nguyên thoại/speaker chỉ là khả năng proposal sau kiểm actual source/handle/tool và bản nối; chưa có quyền hoặc capability chứng minh audio bridge trong Flow. Không hard cut một lần mỗi câu vì count. Không bù missing causality bằng insert món hoặc thoại mới.

## 4. PA/PB cho N02, missing-source tickets và thứ tự validation

**PA — tiếp tục trên mặt Khoai hết ký ức, fidelity với214.** Giữ những ranges N02 thực qua QC, bổ sung coverage F0 thấy Khoai nói qua “anh đứng chờ”, với same audio. Gap bắt đầu tại native f164 khi vùng mặt chuyển thành dish; phạm vi speech replacement cuối cùng UNKNOWN cho tới hearing/AV, không mặc định37frame đều cần sinh hoặc một extension nhỏ đủ. Candidate mới phải nối f163 về nét mặt/ánh mắt/tay/bàn và trở về phản ứng trước N03. Source bổ sung/version/hash/range hiện MISSING; không chọn take, không viết request sinh từ report này. Nếu mới cả N02 cho continuity tốt hơn, root trình phạm vi/quote/inputs/criteria riêng.

**PB — chuyển chú ý sang Đào đang nghe cuối ký ức.** Giữ full exact N02 PCM, đổi phần cuối R02 sang reaction F0 có nguyên nhân: lời “đứng chờ” khiến cô muốn hỏi. PA/PB khác variable chính là điểm nhìn cuối ký ức; cùng dialogue order, audio bytes, intent và các beat còn lại. Coverage PB là diff214 cần owner duyệt trước lock.194 R203 có cốc cầm từ đầu và miệng mở ở nhiều samples nên chưa là silent F0 reaction hợp lệ. Native tail201+ hiện ở8,375s, sau speech-end ASR7,34; không tự chuyển sớm/loop, không dùng vật tay nghỉ cùng mặt như bằng chứng lipsync phù hợp. Reaction nguồn/version/range verified hiện MISSING.

Trade-off: PA giữ cơ hội đọc nét nhớ của người kể nhưng có risk jump face/gaze/miệng nếu phải bổ sung; PB tăng thông tin nghe/chuẩn bị câu hỏi nhưng giảm mặt Khoai cuối ý và có risk listener bị hiểu đang nói. Không rank hấp dẫn/retention chưa thử. PA ưu tiên sơ bộ về đúng coverage đã duyệt; PB conditional change candidate, **cả hai chưa final**. Nếu candidate khác nhau về face/lighting/acting/props chất lượng, ghi confounds trong phép so, không gọi là A/B test kiểm soát sạch.

| Ticket / scope | Input còn thiếu và acceptance | Next validation / route |
|---|---|---|
|EDIT218-T01 / R01/R03 |Native A02/A03 đúng hash, toàn frames+AV của line phù hợp và props reference; range N01/pull–stop, N03/N04 có miệng đúng speaker/listener |Root cấp bounded native read scope kế tiếp; EDIT/DLG-EDIT đo range source/frame, SIA/AV và CONT/FOOD kiểm. Không chuyển audio original_in thành video in tự động |
|EDIT218-T02 / N02 PA/PB |Đuôi lời nghe/phoneme-lipsync, gaze continuity [0,164), tail [201,240), coverage mới/nguồn reaction F0 |G2 N02 trước: actual hearing/reference và continuousAV. CTD chỉ lập thiếu nguồn sau root tích hợp/cold review; request paid riêng nếu cần; PB coverage diff owner |
|EDIT218-T03 / R04–R08 |F0→P gắp→F1→caught F2→redirect F3→bát/thả F4; native163/194/154 và insert207 ranges chưa được cấp/kiểm sâu |G3 sau N02: native/state ledger rồi review không tiếng và fullAV bản nối. Không lấy nguồn154 tay nghỉ thay A đang kẹp; xác minh contact/drop một lần |
|EDIT218-T04 / N05–N07 |Word/turn/cut offsets riêng trong cụm1548s, intervals reaction/no speech thật; source nghe và refs |DLG-EDIT/SIA/AV đo trên source/version thực, ghi heard evidence; no invented offsets. Audio selection source approval không thay AV assembly |
|EDIT218-T05 / R09 và30s |Native209 U08 A/B continuity, range gắp B và nét cả hai; time fit actual lời+action+holds |G1/G4 bản thử NOT_RELEASE có exact range/hash/audio placement. Nếu conflict30s, root trình lựa chọn timing/coverage hoặc pause đúng quyền; không bỏ R09/nhai nói/đổi text |

Ordering đề nghị: (1) root tích hợp DOP/ACT sau R1 và cold reviewers frame đúng phạm vi; (2) đối chiếu paper map ở G1, range mới chỉ sau mở scope nguồn cụ thể; (3) G2 N02 actual AV/hearing trước mở sản xuất các cảnh thoại; (4) G3 source action và joins R04–R09; (5) G4 continuous silent/fullAV và đo30s; (6) G5 caption/mix/export current hash + SIA FINAL_AV + owner. Run này chưa chạy các phép validation media trên.

## 5. Findings, disposition và handoff

| ID / rule / coverage / severity | Expected / observed / evidence / uncertainty | Action, route, owner và closure |
|---|---|---|
|EDIT218-F01 / R02 face coverage / DEFECT nếu dùng nguyên vùng [164,201) / MAJOR |214 cần mặt Khoai nguyên ý; f163→164 vàf200→201 thực cho dish không mặt. ASR hint chồng đuôi “đứng/chờ”, không hearing/lip-sync defect confirmed |PA hoặc PB theo mục4; EDIT+DOP+ACT/CONT+SIA/AV. Owner PB diff hoặc request chi nếu phải bổ sung. Closure candidate/hash/ranges và review đúng hình+full lời; OPEN |
|EDIT218-F02 / native range provenance / MET trong segmentation scope / MINOR tracking |Probe trực tiếp240frames24fps; các cặp native xác nhận cut72/164/201; [0,72)+[72,164)+[164,201)+[201,240)=240. Không có final destination ranges |Ledger đủ để tiếp tục, không là cut-safety PASS; selected ranges hoặc source đổi phải kiểm lại. Closure technical source segmentation có evidence tại mục1/3; không đóng artistic findings |
|EDIT218-F03 / hearing-speaker-mouth/AV / UNKNOWN / MAJOR gate |Không nghe/xem continuousAV trong run; manifest label/transcript/probe không xác minh voice, speaker, mouth attribution hoặc cut breath |Root bố trí reviewer capability/human checkpoint trong Flow/local. SIA AUDIO_SELECTION→AV_ASSEMBLY→FINAL_AV đúng hashes; AV-VOICE/AV-CUT actual logs và owner checkpoint. Closure nghe/reference/fullAV thật; OPEN |
|EDIT218-F04 / R01/R03 coverage + props / UNKNOWN / MAJOR |A02 samples hai mặt/table; A03 samples thiếu rau/chấm/bát/cốc và chứa chữ cũ. N01 pulling/stopping và N03/N04 actual native range chưa kiểm |EDIT/DLG-EDIT source-read scope mới, CONT/FOOD/CINE/PERF. Owner chỉ khi thay coverage/ref/nội dung. Closure verified native ranges/source state/cut evidence, không sheet timestamp; OPEN |
|EDIT218-F05 / cause→caught→redirect→bowl / UNKNOWN / MAJOR |163 samples đầu đã cầm A,194 cầm cốc/reaction,154 tay nghỉ; không chứng minh full F0→F4 hoặc A chưa contact. Không kết luận toàn kho thiếu/acting lỗi đã thấy |Source ticketsT03/T04, CONT/PERF và fullAV review. Closure current candidate/join silent+AV có trước/sau cut, A/state ledger và actual turn offsets. Owner nếu đổi ý đồ214; OPEN |
|EDIT218-F06 / R09 A/B và timing30s / UNKNOWN / MAJOR |209 U08 samples bát có món+đũa từ P lên, chưa chứng minh B sau A; WAV20222,055s không chứng minh fit hành động hoặc vị trí khoảng nghỉ |T05, EDIT đo actual trial, CONT/PERF/AV. Owner nếu conflict ràng buộc/pause layout cần duyệt. Closure bản thử/hash/timeline/source ranges và fullscene đúng version; OPEN |
|EDIT218-F07 / full PCM preservation / MET trong run; provenance compatibility UNKNOWN / MAJOR gate nếu thay audio |WAV202 hash giữ đúng source manifest; không mutation trong run. PCM matching ordered sources chỉ kế thừa manifest;5ms tail N02 chưa là drift defect |Comparison PA/PB dùng whole202; audio edit chỉ proposal mới đúng quyền/owner, SIA/AV kiểm lại dependency. Closure cho run: hash nguyên bytes; closure AV/tail/master vẫn OPEN |

Không lấy MET hash/range bù các MAJOR UNKNOWN/DEFECT. Caption safe-zone/readability, actual mix/pop/ambience là UNKNOWN trước có export/actual listening; không ghi N/A để bypass finishing. Chi phí/route/quote live chưa kiểm, không lấy số dư/cap cũ thành quyền chi. Report này không tự approve PA/PB, coverage, take hoặc nguồn audio mới.

Handoff năm mục:

1. **Đã xác định:** audio provenance bảy lượt trong202, exact native segmentation24fps và cut72/164/201; N02 có partial reuse mặt, vùng dish thiếu face cho R02. Line-to-picture và state joins R01–R09 đã lập, những nguồn chưa kiểm sâu vẫn candidate/UNKNOWN.
2. **Quyết định đã chốt:** kế thừa178/212–217; không quyết định take mới. Giữ full PCM202 trong run/comparison đề nghị; PA fidelity-first proposal, PB cần diff coverage owner, cả hai chưa final. Không sửa lời hoặc quay lại discovery nền tảng.
3. **Giả định đang dùng:** OPEN7 diagnostic làm đối chiếu; source approval nghe lịch sử còn giá trị trong scope nguồn nhưng không thay SIA/AV mới; t=n/24 cho native N02 đã được probe;30s là target chưa đạt. Chưa giả tail silent, B đúng miếng mới, hoặc đủ7,945s cho action.
4. **Vấn đề còn mở:** ranges nguồn khác/native action chưa có scope đọc sâu; exact offsets N05–N07, mouth/voice/gaze, N02 PA/PB coverage thiếu, match A/B/props và fit30s. Root cần bố trí actual hearing/fullAV; owner cần duyệt PB nếu dùng, waveform/pause/sample nếu thay, request chi và checkpoints217 theo đúng artifact.
5. **Bước tiếp:** root tích hợp makers+cold reviewers, trình G1 source/gap map/bản thử theo permission riêng, giải quyết G2 N02 trước, rồi G3 action/G4 fullscene/G5 export. Mỗi closure phải gắn artifact/version/hash, native ranges và quan sát thực; không chuyển report giấy này thành media PASS hoặc release-ready.
