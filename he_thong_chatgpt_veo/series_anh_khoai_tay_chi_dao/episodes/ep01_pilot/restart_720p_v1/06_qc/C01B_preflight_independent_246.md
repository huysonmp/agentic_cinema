# C01B — Preflight độc lập REC246

Ngày 07/10/2026. Run C01B-CRITIC-246, không phải maker. **PASS_PAPER cho đúng draft/hash và nguồn bên dưới; không phát hiện blocker giấy.** Điều kiện một output trả phí theo scoped238: root chịu trách nhiệm xác nhận live input/readback/config/quote còn đúng ngay trước submit. Không PASS video, chuyển động, tiếng, khẩu hình hoặc điểm nối chưa có output.

## Nguồn và phạm vi kiểm

Đã đọc đầy đủ plan236, scoped-autonomy238, quyết định chọn prefix246, ngoại lệ contact, audio approval exact cut, report actual T04 của reviewer, input preparation hiện hành, exact C01B draft và các report C01B DOP/ACT, C01A T04 EDIT options. Đã trực tiếp xem toàn ảnh đầu C01B; không UI/API/Git/credit/generation hoặc nghe thực trong run này.

Hash tính lại bằng PowerShell:

| Đối tượng | SHA256 thực |
| --- | --- |
| `04_requests/C01B_prompt_DRAFT_246.txt` | `c9487b6fd95f6d072840662ef8dd6da8d4a5cd149523e77a5d8c80d13113e3fd` |
| `02_refs/C01B_START_from_C01A_T04_FLOW_v1.png` | `0cf422f2b28dae631785af6ec19fc7488800c0cf8d22bb95dddd04e1b7ae2acb` |
| Owner QC `C01A_T04_FLOW_246/all_native_frames/00081.png` | `0cf422f2b28dae631785af6ec19fc7488800c0cf8d22bb95dddd04e1b7ae2acb` |

Ảnh start byte-identical với PNG frame80 của exact export đã kiểm; không ảnh tái tạo pose. Export nguồn e22c113204c404e928683c69465237921f601f2b33a3eb9a9187eb0648f4b803 có81frames, video3,375s/audio3,370667s, không duration3,333s từ tên file. Actual T04 review ghi42 unique exportframes, gồm từng frame52–80: chưa thấy platepull trong phạm vi đó, không continuous AV/3D/no-unseen-frame guarantee.

Root producer đã chọn exact prefix bằng `C01A-exact-prefix-selection-246.json`; owner cho rim-touch + inner supporting gesture nhưng không kéo/lấy/ăn; owner nghe exact cut và chấp nhận D06/trọn N01/nhịp. Đây là source closure có giới hạn để chuẩn bị đơn vị tiếp theo, **không** owner picture/whole-film approval. Các trường PENDING cũ trong report maker/ngoại lệ/audio record là snapshot trước selection; không tự xóa giới hạn hoặc suy thành nguồn vẫn chưa được chọn. Root nên đồng bộ status vận hành để tránh người sau đọc sai, không cần sửa input nghệ thuật vì các heading cũ.

## Đối soát độc lập

| Kiểm | Expected / observed trên giấy và ảnh | Kết luận / điều kiện đóng |
| --- | --- | --- |
| B-START / CONTACT | Actual ảnh: Khoai trái, Đào phải; outer arm Đào từ screen-right xuống vành phải đĩa, inner hand cong/hover cạnh trong bát; chưa rest. Draft giữ exact pose, không reset đầu cảnh. | PASS_PAPER dưới ngoại lệ. Không tự giả lại khoảng hở trước-contact; không dùng C01B trả đĩa để chữa một nguồn đã kéo. |
| B-SPEAKER | Chỉ Khoai nói một lần đúng “Khoan.”; một K20 ID `b447b35c-b35e-4140-af72-ecd277282b1a`, không D06 hoặc phần ký ức N02. Mặt/miệng anh phải nhìn thấy; tay anh nghỉ. | PASS_PAPER. Actual đúng giọng/người/lời và môi người nghe vẫn UNKNOWN. Approval tiếng C01A/C02 không chuyển sang C01B. |
| B-CAUSE | Giữ ý định lấy cho đến khi nghe Khoan; đổi chú ý → nới/rời vành → thu tay ngoài; tay trong settle từ hover. Prompt và ACT không đòi đợi hết âm rồi freeze. | PASS_PAPER, một chuỗi đọc được, không mâu thuẫn cue. After-output phải kiểm cue trước release; hình tĩnh không chứng minh nghe. |
| B-PATH / PLATE | Nới ngón trước rồi forearm về trên vùng đũa nghỉ; ngoài bát riêng, không tới cốc. Inner settle cạnh trong bát. Đĩa stationary suốt, không pull/lift/take/eat. | PASS_PAPER. Route từ2D là giả định khả thi, không clearance/motion guarantee. Kiểm toàn đường và rim/plate outline sau tạo, không chỉ endpoint đẹp. |
| B-FACE / SET / FOOD | Ảnh giữ hai mặt/miệng, vùng tay và đĩa; phố mở/đèn lồng/mái bạt; nem nguội, rau trước-trái, hai chấm, bát trống, đũa nghỉ, cốc ngoài phải. Draft khóa same fixed camera, no cuts/zoom, no smoke implied by cold dish. | PASS_PAPER. Không food-cover hoặc mất mặt Khoai ở từ Khoan. Không coi no-steam là hand PASS. |
| B-END / JOIN | Cả hai tay Đào về nghỉ để nối C02; Khoai sau từ Khoan môi khép, sẵn kể tiếp. Không bắt đầu từ F0 giả, không thêm lời. | Target hợp lý; exact C01A→B và B→C02 geometry/gaze/light/voice/phonetics UNKNOWN trước output/rough. Ingredients không khóa chắc start/end. |
| B-TEXT | Giữ symbol bốn điểm hiện có dưới-phải, bàn không chữ; không overlay/caption/logo mới. | PASS_PAPER, không xung đột source. T02 text/presenting từng fail phải kiểm hồi quy trên native B mới, không dự đoán chắc đã hết. |

Không thấy giả định đổi canon, đổi nghề/couple, flashback, thay đồ bàn hoặc nhãn nhà hàng. Preamble adult fictional food characters minh bạch, không keyword-evasion/model/account workaround. Nếu provider refusal lặp phải STOP/report theo hồ sơ, không paper PASS thành quyền bypass.

## Quyền, live gate và timing

Scoped238 **thay thế xin owner cho từng request trong phạm vi**: native720p, x1, quote≤15, trần500 và các bucket, reserve110 chưa được cấp; stop hai actual output liên tiếp cùng MAJOR. Checkpoint owner giữ master/voices, C02, rough toàn phim, final; plan còn yêu cầu nghe actual đầu Khoai/Đào, nay đã đóng trên exact targets. Không có quy định phải thêm owner picture checkpoint mới cho mọi clip. Không suy việc source dùng được thành delivery approval.

Input prep đọc mới ghi cloud source `59429038-2b6d-4e2d-879e-1535f60feba6`, K20 trên, một ảnh/một voice; root báo readback match exact draft, Omni1.1 Flash Ingredients720p9:16/4s/x1/AgentOFF, quote7, balance1020, submit0. **Đây là root-reported live verification, critic không kiểm UI độc lập.** Quote7 nằm trong≤15; phải giữ exact chip/performance/config/readback, không submit batch hoặc video-edit route. Chuỗi status/preflight còn NOT_RUN cần root cập nhật với report này trước submit.

Native4s là thời lượng sinh, không selected EDL. Prefix C01A3,375s để lại1,125s theo opening target4,5s giấy: chưa chứng minh đủ từ Khoan + nghe/release/thu. Không trim mất nguyên nhân/âm/đường tay hoặc speed/pitch để ép. C02 ngắn hơn slot giấy không phải slack chắc chắn; đo actual toàn sequence rồi phân bổ, giữ30s/canon và nghiệm thu rough.

## Handoff

- **Đã xác định:** exact prompt/source hash, byte-identical frame80, pose rim/inner-hover và source selection có giới hạn; không blocker giấy hiện hành.
- **Quyết định review:** PASS_PAPER cho đúng package; đủ preflight để root thực hiện một output trong238 nếu live gate vẫn đúng. Không reviewer cấp quyền chi mới hoặc bảo đảm output.
- **Giả định:** release/retract tự nhiên có thể thực hiện trong native4s; chưa biết range đủ nhịp để nối.
- **Còn mở:** actual tiếng/K20/lời/AV, cue→release, đĩa/tay, hai joins và timing30s. Giới hạn sample C01A/khẩu hình vẫn theo source selection, phải quay lại rough AV.
- **Bước tiếp:** root đọc toàn report, đồng bộ readiness và kiểm live lần cuối; sau đúng một output tải native, ghi hash/probe, QC mặt–cue–tay–đĩa và audio có capability, chọn range thực rồi kiểm hai điểm nối. Nếu cùng MAJOR hai output liên tiếp thì STOP chẩn đoán, không autorun vòng retry.
