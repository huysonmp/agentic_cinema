# REC275 — C06 T03: phản biện độc lập trên bản gốc

Ngày 12-10-2026. RUN_ID: REC275-C06-T03-INDEPENDENT-ACTUAL.

Kết luận: **FULL_NATIVE_REWORK_EARLY_RELEASE / STOP / C06_NOT_SELECTED / AUDIO_AV_HOLD / C07_HOLD**. Cốc giữ nâng, nhưng Khoai thả A vào bát Đào trong đuôi nguồn. Việc này làm mất endpoint “vẫn kẹp và chờ nhận”, thực hiện sớm hành động thuộc cảnh sau. Không tự T04 hoặc thay coverage.

## Target, authority và phạm vi thực kiểm

Bản gốc: `05_native/EP01_720_C06_T03_NATIVE.mp4`, SHA-256 tự tính lại **`36f04086a2e3d6d3d688f64ca743909184955bf1a714094def5dd8cd3747ff7c`**, khớp run và evidence. Đã đọc đầy đủ final `04_requests/C06_T03_prompt_275.txt`, hash đã xác minh trong preflight là `42b412ec3bb6e7d3dd4b86fd980ad5a9c0a2a494dae899ae2f9bf077028e35d9`; toàn run275 và `00_decisions/C06-one-run-and-T02-audio-approval-275.json`. Run hiện ghi nguồn đã nhận, 96 khung / 4 giây, đang chờ actual review. Không đọc maker actual275.

Evidence: `C:/Users/PC/Downloads/du_an_nem_bui/275_C06_T03/native_qc/`. Đã đọc đầy đủ `native_evidence.json` và `action_all/manifest.json`. Đã trực tiếp xem **toàn bộ 12 board action_all_01–12.jpg, đủ F0–95**, tám khung gốc mỗi board. Xem thêm PNG nguyên khung F0, F17, F35, F60, F64, F68, F72, F76, F80, F95 (tên file = F+1), và exact START từ C05 T02 F65. START hash đã tự xác minh trong preflight: `f091e35fc7c779591c918c47ba34752a8a2c3b30de507cd99dc0e76143e83196`.

Năng lực: **ALL_FRAME_STILLS_NOT_AV**. Không nghe hoặc phát AV liên tục; không chạy ASR. Đọc evidence kỹ thuật H264 720×1280, 24 fps, video4 giây / 96 khung, AAC stereo48 kHz, decode thành công và nguồn không đổi; không tự chạy lại probe/decode. Không browser/API/credit/git/script/media hoặc thay công cụ.

Owner275 đã chốt hướng274-A: ngượng qua mắt–mày–nhịp, bỏ cue nhếch môi chủ động. **Không áp tiêu chí cũ “chỉ một khóe cuối câu” để chấm T03.** Cho phép thấy răng khi phát âm tự nhiên. Owner đã duyệt tiếng T02, không chuyển thành approval K20/N06/sync của T03.

## Findings thực tế

F tính từ0; thời gian=F÷24.

| ID / mức độ | Mong đợi và quan sát | Bằng chứng / disposition |
|---|---|---|
| ENTRY01 — không thấy MAJOR reset | F0 giữ môi cụp, nét bị bắt gặp và mắt hướng Đào khá sát START; không vào cảnh bằng cười vui hoặc khám phá lại miếng A. | Exact START → F0; board01–02. Chưa có encoded C05→C06 seam nên không tự chứng nhận điểm nối. |
| ACT01 — **diễn nghệ thuật chưa đóng, không chấm MAJOR chỉ vì răng** | Trong lời, mày trong nhấc và ánh mắt còn hướng Đào, có nét ngượng. Một số nhóm khẩu hình mở ngang tạo nét cười khá rõ, nhất là F16–19 và F32–38; sau lời môi khép, giữ nét nhẹ và mày ngượng. Không thấy cười lớn hoặc chuyển sang nét hớn hở cực đoan. | Board03–05, full F17/F35; cuối F40–95. Không dùng hai khóe cùng nâng đơn độc làm lỗi của rule273 đã thay. Tổng nét có cả ngượng và cười; reviewer chưa nghe ngữ điệu nên không chứng nhận owner274-A đạt hoặc kết luận toàn cảnh vui chủ động chỉ từ răng. Root/owner cần kiểm đúng actual AV và nghệ thuật. Không tự chuyển thành acting PASS. |
| MOUTH01 — attribution hình phù hợp | Khoai có chuỗi khẩu hình khoảng F9–39, rồi môi khép từ khoảng F40. Đào khép môi, không thấy nhóm khẩu hình nói. | Board02–06 và toàn12 board. Chỉ chứng minh attribution hình; không xác nhận đủ lời, K20, single speaker trong tiếng hoặc sync. Không gán âm “mà” vào frame khi chưa nghe. |
| GLASS01 — không thấy MAJOR | Cốc vẫn nâng trong tay ngoài Đào từ đầu đến cuối, đáy lơ lửng tách bát; không hạ, đặt xuống, đổi tay hoặc uống. | Đủ96 khung; full F0/F60/F95. Scope ảnh đủ dày, không gọi continuous AV PASS. |
| ACTION01 — đường chuyển có thực nhưng endpoint sai | A vẫn một miếng ở own pair / tay ngoài trái của Khoai lúc đầu. Sau khẩu hình, tay đưa A sang phải trên bàn, hướng bát riêng Đào; không ăn hoặc lấy miếng thứ hai. Tuy nhiên tay không dừng ở khoảng hở mà tiếp tục hạ A vào bát. | Board06–10: chuyển khoảng F41–64; tiếp tục hạ F65–79. Own pair và tay không đổi; việc này không bù lỗi thả sớm. |
| RELEASE01 — **MAJOR, A được thả sớm** | Expected A vẫn kẹp, bát nhận rỗng, giữ chờ Đào nhận ở cảnh sau. Actual F72 A sát/chồng vùng vành, F76 xuống thấp, F80 A đã tách khỏi tips và ở trong bát; F95 tips trống và miếng A nằm trong bát. | Board09–12 và full F68/F72/F76/F80/F95. Contact chính xác ban đầu có giới hạn projection; **release ở F80 và endpoint F95 rõ**, không chỉ contact uncertainty. FULL_NATIVE REWORK; STOP theo approval275, không tự T04. |
| BOWL01 — MAJOR phụ thuộc release | Hai bát riêng tồn tại, không bị cốc thay thế; nhưng bát Đào chỉ rỗng trước thả. Đuôi nguồn có A bên trong, sai trạng thái C06. Cô chưa nhấc bát hoặc làm beat nhận. | Full F0/F60/F80/F95. Không ghi “hai bát rỗng suốt” vì chỉ cốc đạt. Không dùng F95 làm ref C07 rồi lặng lẽ đổi nhiệm vụ C07/C08. |
| CONT/FOOD01 — không thấy MAJOR khác | Nem nguội không hơi, rau trước trái, hai chấm, trang phục, hai mặt, góc máy và ánh sáng giữ. Đũa riêng của Đào nghỉ trên bàn phải, tay trong hai người vẫn nghỉ. | Toàn12 board và full F0/F95. Không thấy nhân miếng hoặc ăn; A vào bát vẫn là blocker dù các props khác giữ. |

## Đánh giá tổng thể và giới hạn

T03 không chứng minh can thiệp bỏ cue đã sửa hoàn toàn diễn. Nét mày/mắt ngượng tồn tại; miệng vẫn có nét cười ở vài nhóm khẩu hình, nên cần đánh tổng thể với tiếng, không áp tiêu chí cũ về một khóe hoặc chỉ thấy răng. Không nâng report giấy thành actual PASS và không chuyển tiếng T02 đã duyệt sang T03.

Blocker đủ chắc để dừng **không phụ thuộc tranh luận diễn** là A đã được thả. Prompt đã ghi A stays clamped / never released, end hold và bát rỗng; output vẫn tự hoàn tất hành động cho món. Lỗi nằm trong native trước ghép, không do cut/encode. Chưa có bằng chứng nguyên nhân riêng lẻ là wording, độ dài4 giây, route, voice hoặc mật độ prompt; không tự nhận chỉ thêm câu cấm nữa sẽ sửa được.

Nguồn có đoạn trước khi thả, nhưng báo cáo này **không chọn prefix**. Nếu root muốn xét trim, phải khóa target/range mới và kiểm đủ N06, diễn, đường A, khoảng hở, nhịp hold, source-to-cut dependency và seam; không được xem trim là cách duyệt full4 giây hoặc đổi coverage để bỏ receiving beat. Lựa chọn như vậy còn cần owner chốt đúng phạm vi, không bypass STOP/T03-only authority.

## Disposition và bước tiếp

- Giữ nguồn T03 cùng hai nguồn trước; không chạy T04 hoặc tự chuyển sang ghép voice/coverage mới.
- C06 **NOT_SELECTED**, C07 **HOLD**, audio/K20/fullN06/lip-sync **NOT_CERTIFIED** trên T03.
- Root đọc đầy đủ báo cáo độc lập và maker, đối chiếu findings rồi trình chính xác: cốc đạt về ảnh, diễn còn checkpoint, thả A là lỗi nguồn chắc chắn. Không đề nghị owner duyệt như take đã đạt mọi scope.
- Ledger run275 ghi chi7, tổng187/500, còn313, retake66; reserve110 vẫn đóng. Reviewer chỉ đọc ledger, không tự đối soát tài khoản live. Thay đổi số dư sẵn có +133 đã được park, không thành quyền tăng ngân sách.
- Nếu dùng4 giây C06, tổng qua C06 là30,333 giây, phầnC07–09 còn4,667 giây đến35. Vì C06 chưa chọn, đây chỉ là tính điều kiện; không hứa video hoàn thành vừa trần.

## Rà thêm prefix trước F72 — không chứng minh endpoint giữ chờ

Theo yêu cầu root, reviewer xem thêm PNG nguyên khung **F56/F63/F67**, ngoài board đã xem đủ F56–71 và các full F60/F64/F68. Giữ đúng source/hash T03 nêu trên; không render, chọn range hoặc tạo reference mới.

- F56–60: A vẫn kẹp, đã chuyển sang phía Đào và còn khoảng hở nhìn rõ trước vùng vành. Cốc nâng, bát nhận rỗng. Đường tay chưa dừng: qua F63/F64/F67, A/tip tiếp tục tiến và hạ thấp về vành.
- F63–67: A còn kẹp, nhưng khoảng hở gần vành nhỏ dần; chiếu hình dễ chồng mép bên trái. Không chứng nhận clearance vật lý tuyệt đối hoặc giữ đủ air gap bằng một ảnh này.
- **Không thấy một đoạn hold ổn định sau redirect và trước F72.** Chỉ cắt trước thả sẽ loại release, nhưng không tự hoàn thành nhiệm vụ gốc “chuyển tới vị trí chờ, dừng và giữ A cho phản ứng nhận tiếp theo”.
- Chuỗi khẩu hình đã về môi khép từ khoảng F40, trước vùng F56–67. Điều đó **không xác nhận trọn N06/âm cuối/K20/sync**; reviewer vẫn chưa nghe nguồn. Không dùng mouth closed làm mốc audio end.

Vì vậy phân biệt hai phạm vi: **prefix-held theo brief hiện tại chưa được chứng minh**, còn **cut-on-motion trước rim** là một phương án boundary mới có thể trình owner. Nếu owner chọn cách cắt giữa chuyển động, phải chốt exact range, cách nối chuyển động vào cảnh sau và timing/voice/AV; không được gọi đó là C06 đã có hold đúng brief. Không chọn endpoint/ref C07 từ F63/F67 trong báo cáo này. STOP full native và không tự T04 giữ nguyên.
