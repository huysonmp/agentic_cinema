# EP01 — duyệt hướng hybrid và kiểm sẵn sàng Quality / hoàn thiện

Ngày: 2026-10-02. Người kiểm: root, kiểm hồ sơ + công cụ local + UI Flow + tài liệu Google hiện hành. **Không phải review độc lập, không chạy generation hoặc sản xuất prototype trong vòng này.**

## 1. Quyết định owner mới và kết luận

Owner: “chọn theo khuyến nghị, check lại xem đã sẵn sàng chuyển sang dùng quality và đủ bộ công cụ, sẵn sàng các thông tin tài nguyên quyết định công cụ để tiến đến các giai đoạn cuối cùng chưa, kiểm tra và trình bày cho tôi xem nào”.

**A tại120 được chọn ở cấp phương pháp:** tách cảnh mở dùng chuyển động có kiểm soát trên ảnh; Veo tạo diễn xuất có chủ đích. Không suy thành duyệt exact crop/thời lượng, xóa hành động/thoại, mọi input production, request Quality hoặc ngân sách mới. Kịch bản32 và T2 vẫn là nền tảng; cần cập nhật coverage bị ảnh hưởng trước tạo final.

Kết luận:

- Có đủ công cụ nền tảng để chuẩn bị prototype hybrid và các thử nghiệm có giới hạn; chưa cần cài thêm nền tảng lớn hoặc Gemini API.
- **Chưa sẵn sàng chuyển cả tập sang Quality hoặc đi thẳng P10–P13.** Thiếu đầu ra đạt, giọng nghe duyệt, action/joins và package theo từng cảnh.
- Quality có trong menu tài khoản, nhưng chưa kiểm request Quality đầy đủ và chưa submit model này. Có thể thiết kế một thử nghiệm Quality riêng; không bắt buộc mọi thứ phải PASS Lite mới được thử model khác, nhưng phải có hypothesis, inputs, budget và gate rõ.
- Công cụ có thật khác với workflow đã vận hành đạt; role prompt/test khác với agent đã review media mới. Không có independent PASS cho bộ10clip119.

## 2. Hiện đang ở chặng nào

| Stage | Trạng thái bằng chứng hiện tại | Điều còn phải hoàn tất |
|---|---|---|
| P2 / P5 | P2-v0.2+E1 approved08; scriptC-v0.5/cue handoff approved38 | Đối soát exact F01/F02/9câu trên tiếng, chữ và hình cuối; không mở lại claim đã loại |
| P6 | Primary45, table78, food/grip directions có approval; voice direction93 | Actual voice Khoai/Đào, consistency theo góc và trạng thái hành động; OPEN7 mới diagnostic |
| P7 | T2 và hướng quay100 approved; A84 giữ causal path | Addendum hybrid: vùng cảnh nào dùng still, thoại/hành động nằm ở đâu; CR-01 S04→S05 vẫn mở |
| P8 | Từng probe cũ có packet riêng; vòng119 đã kết thúc | Exact request mới theo shot, input/hash/model/quote/count/cap/stop và authority |
| P9 | Có V01 và12camera/idle probes, không production-selected | Tạo và review take diễn xuất có chủ đích; đối chứng Quality chỉ khi packet đủ |
| P10 | FFmpeg concat diagnostic thật90; Flow chưa scene ráp | Select log, measured EDL, rough cut liên cảnh có hình/tiếng đúng source |
| P11 | Chưa có picture lock/post pack thật | Mix thoại/ambience, subtitle/F01/F02/AI, màu và transitions trên bản ráp |
| P12 / P13 | Chưa có master QC/owner final acceptance | Export candidate đúng version, kiểm tổng thể, manifest và owner duyệt; không publish |
| P14 |119/120 đã ghi bài học vòng thử | Retrospective toàn tập sau delivery, không dùng thất bại probe để sửa quy trình chưa test |

Không mở lại nền tảng series hoặc nội dung đã duyệt; audit này tập trung dependency từP6 đến bàn giao. Các trạng thái pending của hồ sơ cũ phải đọc cùng approval mới, không dùng chúng để phủ nhận38/78/84/100.

## 3. Công cụ — kiểm thực ngày hôm nay

| Công cụ / vai trò | Kiểm thực và giới hạn | Đánh giá |
|---|---|---|
| Flow/Veo | Project hiện hành mở được; menu có Lite/Fast/Quality/Omni; vẫn giữ Lite, không Generate | Khả dụng để preflight, chưa Quality-tested |
| Scenebuilder | Mục Cảnh hiện trống; official guide có arrange/reorder/trim/preview/download | Có hướng ghép, chưa chứng minh import hybrid + export liên cảnh |
| FFmpeg/FFprobe9.0.2 portable | Chạy version; có crop/scale/zoompan/concat/drawtext/subtitles/loudnorm/afade, libx264/AAC; decode119 đã chạy thật | Công cụ nền sẵn sàng; không suy mọi filter đã production-tested |
| Python3.12.14 riêng | pip check: No broken requirements found | Environment hoạt động |
| faster-whisper1.2.1 / PyAV16.1.0 / CTranslate2 4.8.2 | Import đúng; tải modelsmall từcache local_files_only thành công | ASR offline có thể chạy, không thay nghe nghệ thuật |
| Script local_voice_qc.py | Đã có extraction/ASR/log/hash thật ở89; hôm nay kiểm source và model load, không ASR media mới | Có diagnostic, chưa kiểm giọng mới |
| voice_assembly_diagnostic.py | Chỉ chấp nhận exact hashV01; unit tests5/5 OK hôm nay | Không phải renderer tổng quát cho EP01 production |
| Motion/EDL renderer hybrid | FFmpeg có primitives, chưa có manifest/runner/QA prototypeA | Phải chuẩn bị và test; không gọi đã build |
| Canva | Owner từng chọn cho hoàn thiện/dự phòng35/64/89 | Chưa kiểm login, import/export hiện tại; không coi tự động available |
| Nghe/đọc lip-sync | ASR/timestamps và frames hỗ trợ; root chưa nghe đầy đủ hoặc xem continuous audiovisual119 | Listening owner + review thực còn bắt buộc; cài ASR không tạo năng lực thẩm mỹ nghe |

Không cài thêm software, sửa PATH, gọi Gemini API hay chuyển dữ liệu lên dịch vụ mới. Ưu tiên công cụ hiện có; nếu Flow không ráp được hybrid thì đề xuất FFmpeg local cho rough cut, Canva để owner hoàn thiện. Chưa đổi final assembly workflow thay owner.

## 4. Quality: khả năng, chi phí và giới hạn

Nguồn đọc mới2026-10-02: [Flow models](https://support.google.com/flow/answer/16352836?hl=en), [Flow credits](https://support.google.com/flow/answer/16526234), [Scenebuilder](https://support.google.com/flow/answer/16935718?hl=en).

- Tài liệu model: Quality hỗ trợ Text và Frames(first / first+last) cho cả hai tỷ lệ; không hỗ trợ Ingredients/References hoặc video-to-video edit. Không đóng gói nhiều references dạng Ingredients rồi mặc định đổi Lite→Quality được.
- Tài liệu model liệt kê Quality4/6/8s; bảng giá chỉ ghi Quality8s với100credit/generation. Đây là khác biệt mức chi tiết giữa hai trang: duration/cost của request phải đọc UI, không tự suy giá4/6s hoặc dùng tính năng Extend của Quality. Bảng model hiện ghi Extend không hỗ trợ Quality; không lấy hàng giá có chữExtend làm capability approval.
- **100credit là giá công khai cho Quality8s, chưa là quote UI của exact request.** MenuQuality đã thấy, không chọn/chạy hoặc thay cấu hình.
- Số dư live hiện920. Theo119, observed spent từmốc1050 là130; cap thử200 chỉ còn70. Một Quality8s giá100 vượt phần authority còn lại30, dù tài khoản đủ tiền/credit. Cần owner duyệt budget riêng hoặc điều chỉnh cap trước submit; không mua thêm.
- Nâng Quality không được xem là cam kết sửa tay, contact, voice hay continuity. Nếu thử, so đúng mục tiêu với baseline và ghi những thay đổi ngoài model; không dùng upscale để gọi thành generationQuality.

UI proofs local:121_FLOW_MODEL_MENU.jpg,121_FLOW_SCENE_EMPTY.jpg,121_BALANCE.jpg. Accountpanel chỉ lưu local, không nhúng thông tin tài khoản vào bản public.

## 5. Tài nguyên / thông tin đã có và còn thiếu

Đã kiểm file/hashes hiện tại:

| Asset | HashSHA256 / tình trạng |
|---|---|
| PrimaryPAIRv0.3 tạiproject45 | ECFBE7A3C543730C268A77CA08D508147115CA804154F85EBDBB38C5C601E8C7, khớpapproval |
| T-NB-03_v0.8.jpg tạiowner | AEB6DFAEE1773109243F9F952235A44F2417C6FB7FB4FAF15BE61C34CA40D924, khớp78 |
| OPEN7 tạiowner | A3D80F09BFB7242BAE3007AD7B4F37473BB2F0ED019A84CC4956C4D32A8DBF9A, khớp119; diagnostic không tự làfinal |
| nembui.jpg | A51303F7100EDD0944DC00DAA19402FECFE24BB0E15A4143DA8F8EAE7B9E3A2D, filecó/owneruse68 |
| z775…806643377.jpg |1237956E99458385F95F1EDF18E0A98E1BDDB777030AC1D69FAB05FA7A51D741, filecó/owneruse68 |

Có script32, research06/07/08, cue38, staging84, context75, storyboard99/100 và10clips119 với manifest. Tuy nhiên **chưa có bộ production inputs theo từng shot** chứng minh đủ cốc-trên-tay, nem-ngoài-miệng, trên-bát-chưa-thả và sau-thả. Chỉ tạo khung thật sự cần theo shot; không yêu cầu bộ360° vô ích.

Đầu vào phải bổ sung:

1. Shot addendumhybrid với beat/line/camera/method/ref/version/start/end/cut mapping. Một still không thể vừa đứng yên vừa thực hiện Đào kéo đĩa và Khoai nói; không xóa hai beat này. Hướng đề xuất: still chỉ phục vụ dẫn mắt không có miệng nói nhìn thấy; phần thoại/hành động chuyển sang take riêng có sync. Exact timing/cut chưa được duyệt.
2. Mẫu voice Khoai theo93 và Đào + đối đáp; đo thời lượng thật. V01 bị owner bác92/93, voice95 là draft chưa chạy; không lấy voice description làm voiceIDlock. Nếu dùng voice từ takeVeo, mọi extraction/ghép giữ source và kiểm lip-sync trên hình người nói.
3. Dynamic probe S04/S05: cốc đúngtay/thứtự, gripđúng, nem đổi hướng trướcchạmmiệng, đúngbát, transfermộtlần. CR-01 gộp cảnh vẫn chưa duyệt, không tự áp dụng.
4. Production requestmanifest riêng mỗi take: refs vàrights, model/mode/resolution/duration/x1/quote, prompt exact, expectedstates, criteria/retry/stop, ownerauthority và outputhash.
5. EDL/caption/audio map thật:9câu đủ/khônglặp/khôngcắt từ; F01/F02 đúngqualifier; AIlabel, font và vùng chữ; nguồn ambience/music nếu dùng. Không tự thêm nhạc cần quyền.
6. Deliveryspec và package: master dọc30s theo mục tiêu, độ phân giải/fps/audio/export cụ thể cần chốt sau tech test; clean/overlay versions nếu cần phải rõ, không xóa nativewatermark. Raw/select/master manifest, nguồnclaim/rights notes, QC và owneracceptance.

Owner cho sử dụng ảnh68 không tự là chứng minh đầy đủ commercialrights của mọi ảnh/nhạc/platform; RIGHTS phải ghi scope/provenance trước delivery. Không đưa ảnh research-only lênFlow. Không phát sinh claim mới hoặc lời khẳng định pháp lý từaudit này.

## 6. Agent: đã có thiết kế/test, còn phải chạy ở đâu

| Nhóm đã có | Cần đầu ra tiếp theo | Không được tự tuyên bố |
|---|---|---|
| DIR/DOP/ACT/SHOT/CTD/EDIT | Hybridaddendum, ý đồ thị giác/diễn xuất, source/cutmap nhấtquán32/84/100 | Mô tảđạo diễn = đã cómediađạt |
| CINE-LIGHT/PERF/CONT + CHAR/ART/FOOD | Kiểm prototype/candidate đúngversion, đủsequence/frames/contact/crop/light/food | Root16samples119 = reviewđộc lập hoặc fullplayback |
| VOICE/AV +4rolesAEQ90 | Listeningtickets, dialogue boundaries, đo timings, lip-sync và exportjoin audit | ASR/fixturePASS = giọng hay/đã nghe |
| FLOW/PROMPT/RIGHTS | Kiểm requestQualityspecific, inputroles, provenance vàquoteUI | MenuQuality = request/budgetapproved |
| MASTER/owner | MasterQC rồiacceptance trên exactexporthash | Cóagentprompt = finalPASS |

Hôm nay không dispatch subagent, không có report độc lập mới. Có role chuyên biệt không thay quyền chọn/duyệt củaowner. Không đề xuất agent mới trước khi dùng đúng contract hiện có; thiếu hiện tại là artifact và lần kiểm thật.

## 7. Thứ tự hoàn thiện và điều cần owner quyết định

1. DIR/SHOT/EDIT chuẩn bị addendum hybrid cùng storyboard và bản đồ nguồn/điểm cắt; thử một prototype 2D local, không tiêu credit. Giữ đầy đủ bữa ăn, mặt và đạo cụ; không giả chuyển góc 3D hoặc diễn xuất. Đối chiếu reference và trình owner. Hướng A đã duyệt; prototype, crop và timing chưa duyệt.
2. Chuẩn bị gói thử lại giọng và thử động tác riêng. Kiểm giá/tuyến thực hiện trước, chạy trong đúng phạm vi được phép. Không trộn đổi giọng, góc máy và đũa trong cùng phép thử rồi suy nguyên nhân.
3. Nếu Quality giúp trả lời một rủi ro cụ thể: trình một request x1 với ảnh đầu/cuối đúng mode, giả thuyết, rubric và ngân sách. **Không buộc phải thử Lite bất tận; cũng không nâng cả tập khi chưa có bằng chứng.**
4. Take đạt và được owner chọn → EDL theo thời lượng đo thật → rough cut (ưu tiên Flow nếu import/export hybrid thực đạt; local/Canva dự phòng) → voice/caption/mix → master QC → owner acceptance → delivery manifest.

Quyết định nền tảng đã chốt: phương pháp A; nội dung/canon/staging không đổi; API tiếp tục hoãn. Không hỏi lại.

**Điều owner cần trả lời sau audit:** có duyệt ngân sách Quality riêng 100 credit cho một lượt 8s/x1 sau khi exact packet đạt preflight hay chưa? Khuyến nghị chỉ duyệt một diagnostic, chưa chạy production hàng loạt. Nếu quote thực >100 hoặc request khác phạm vi thì HOLD. Đây là đề xuất, **NOT_APPROVED / NOT_SUBMITTED**; số dư 920 không thay quyền chi tiêu.

Giả định để tiếp tục: dùng công cụ local hiện có, ưu tiên native voice, không nhạc ngoài, output dọc 30s là mục tiêu. Phải thử trước kết luận: chất lượng pan/crop trên ảnh, import hybrid/export Flow, giọng/lip-sync thực, động tác/nối cảnh, timing 30s và master đọc/nghe đạt. Các vấn đề mở có role nhận và điều kiện đóng ở bảng trên; không báo toàn bộ ready.

Audit này không tiêu credit, không thay model đã chọn, không upload media, không tạo/edit video, không cài phần mềm, không chốt Quality/release. Hồ sơ được lưu và version-control; media/proofs giữ local.
