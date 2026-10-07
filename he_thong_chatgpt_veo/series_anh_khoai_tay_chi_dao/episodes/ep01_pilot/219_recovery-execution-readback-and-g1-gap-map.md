# 219 — Kết quả thực thi và khoảng thiếu để dựng lại EP01

Ngày 2026-10-06. **Tầng4 A/A/A đã triển khai local; recovery phim chưa đạt.** Đang cụ thể hóa lại P7/thiết kế cảnh và G1, chưa quay lại P11 finishing/P13 bàn giao. Bản210 bị owner từ chối vẫn được giữ làm evidence, không phải master được nghiệm thu.

**Tiếp nối220:** đã đối soát TABLE08/PAIR03/OPEN7, CONT source-hierarchy và kiểm tuyến Flow hiện hành. [Gói N02/preflight220](220_n02-reference-and-feasibility-preflight.md) đề xuất một batch video-conditionedx3/30 credit, còn chờ owner duyệt; không sinh hoặc chi. 219 giữ làm snapshot của vòng trước, không phải media PASS hoặc nguồn quote mới.

## 1. Những gì thực sự đã làm

DIR → DOP/ACT/EDIT đã chạy bằng bốn context chuyên biệt, mỗi vai có contribution riêng; CINE/PERF/CONT/SIA đã chạy bằng bốn context độc lập với makers. Root đọc đầy đủ cả tám báo cáo rồi mới tích hợp. Chi tiết run/capability/giới hạn nằm tại [218](218_recovery-role-runs-and-gate-implementation.md) và `evidence/218/01–08`.

- **DIR:** chốt spine để thực thi: món → ký ức ăn vụng → lặp lại trong hiện tại → bị thấy → chữa cháy → cùng tiếp tục bữa ăn.
- **DOP:** thiết kế R01–R09 về khung, ánh mắt, mặt–tay–món, ánh sáng và động cơ cắt; không tự gán lens/Kelvin.
- **ACT:** mục tiêu, cue, chú ý và thay đổi hành vi cho người nói/người nghe; restrained là baseline đề xuất, không mặc định mọi biểu cảm nhỏ đều tốt.
- **EDIT:** line-to-picture/source-state map; probe native N02, xác minh các cut/frame ranges; chưa dựng hoặc chọn final take.
- **CINE:** mặt đọc rõ trong mẫu, chưa có căn cứ đổi toàn bộ ánh sáng; mất mặt ở mẫu cận món và động cơ cut/gaze còn cần kiểm.
- **PERF:** chưa có đủ bằng chứng để đọc ra ý định ăn → bị bắt → đổi hướng từ những mẫu được giao. Một bữa ăn thân thiện không tự chứa đủ trò đùa đã viết.
- **CONT:** A03 chênh bộ bàn nếu nối cùng bữa ăn; cận món N02 có trạng thái lá/bát khác cần nguồn authoritative. Không đoán tên rau/chấm từ hình.
- **SIA:** kiểm hashes/probe/PCM và provenance; N02 trong WAV202 giữ nguyên, approval nguồn201/203 giữ đúng phạm vi. Không có bằng chứng mới để kết luận đang lẫn giọng. Phản biện schema đã dẫn tới sửa mã cụ thể.

Các nhận xét hình dùng **ảnh mẫu**; SIA có đo bytes/PCM nhưng chưa nghe. Chưa context nào nhận FULL_AV/actual listening PASS của recovery. Không gọi các context AI là nhóm khán giả thật.

## 2. Chốt chặn đã thực thi

Validator và hooks local chặn thiếu báo cáo, sai target/input/source hash, review tự duyệt, scope/capability không đủ, lỗi trọng yếu mở và approval sai phạm vi. Bộ kiểm speaker hiện có được nối vào gate mới, không bị thay bằng một chữ MET. Closure phải có kiểm độc lập đúng scope/capability/version. Offscreen approval203 không thay yêu cầu speaking-face của214. Finisher còn so decoded picture để tránh duyệt AV-A nhưng render picture-B.

**96/96 kiểm thử liên quan đạt**; lệnh finishing thiếu gate thực sự dừng trước tạo thư mục/file. Chi tiết tại [09_gate-code-readback](evidence/218/09_gate-code-readback.md). Đây là kiểm phần mềm, không phải phim đạt; root test và independent static code inspection được ghi riêng. Không tạo report/media PASS giả để vượt gate.

Adapter finishing/verifying vẫn gắn EDL209/210 cũ, **chưa phải đường xuất recovery mới**. Chỉ cập nhật khi có EDL/caption layout mới được chọn và kiểm. Gate không khóa Flow/Canva bên ngoài, không tự nghe hoặc xác minh lời khai người review là thật. `release_authorized=false` luôn.

## 3. Bảng G1 — có thể dùng gì, còn thiếu gì

“Chưa chứng minh” là chưa có range nguồn được kiểm và chọn cho nhiệm vụ đó, **không phải khẳng định toàn bộ kho không có footage**. Tham chiếu/source candidate khác với khung storyboard sản xuất đã duyệt. Chín dòng này là nhiệm vụ biên tập, không chín lượt sinh.

| Nhiệm vụ | Evidence/candidate hiện có | Khoảng phải xử lý trước lock |
|---|---|---|
| R01 — Đào định kéo đĩa, Khoai “Khoan” | OPEN7/bảng A02 và phần đầu N02 có bố cục hai mặt | Chưa chứng minh kéo → lời giữ → dừng; N01 video range chưa chọn |
| R02 — ký ức trên mặt Khoai | Native N02 có khung chung và cận mặt [0,164) | Cut [164,201) sang món; cần coverage giữ nhiệm vụ cuối câu, gaze tới Đào và AV thực |
| R03 — hỏi/đáp tỉnh bơ | Bảng A02/A03 có hai mặt; audio202 chứa N03/N04 | Chọn đúng source/range, bộ bàn, miệng người nói/người nghe, nhịp nhận ý |
| R04 — Đào lấy cốc, Khoai gắp A về mình | Bảng163 có cốc và A gần mặt | Mẫu đầu đã giữ A; chưa chứng minh A rời đĩa sau cô chuyển chú ý, chưa contact |
| R05 — cô phát hiện, anh khựng | Bảng163 và cận Đào194 có các trạng thái liên quan | Chưa có chuỗi nhìn A → nhìn anh → anh biết bị thấy → khựng nối được |
| R06 — Khoai chữa cháy và đổi hướng A | Audio kết154 đã dùng trong202, bảng154 có mặt | Tay nghỉ không thay trạng thái A đang kẹp; cần mặt nói và quỹ đạo đổi sau bị thấy |
| R07 — Đào hiểu, đưa bát | Audio154, U08 có bát trong tay cô | U08 bát đã có món không tự làm nguồn “trước thả”; cần đúng state/miệng/cue hiểu |
| R08 — thả A vào bát đúng một lần | Nguồn207 là candidate lịch sử trong inventory | Reviewer vòng này chưa kiểm source liên tục; chọn và đối soát trước/sau contact. Gộp R07 nếu đã rõ, không bắt buộc insert |
| R09 — cô cười, anh tự gắp B | U08 có đũa quay về đĩa và món trên đũa | Chưa chứng minh B sau A và kết cùng hiểu; không lấy trọn clip vì có sẵn hoặc ép B phải vào miệng |

Toàn cảnh30s chưa được đo lại. WAV202 dài22,055s; chênh7,945s không chứng minh đủ hành động, không phải khoảng im lặng mặc định. Không bỏ lời/nhịp/kết hoặc đổi tốc độ để vừa.

## 4. Điểm N02 cần xử lý trước tiên

Các cặp ảnh native đã mở thực; source360×640/24fps, chỉ là minh họa diagnostic, không upscale/master mới. Mốc giây dưới là mốc **hình**, không phải phoneme alignment:

- f163 / 6,791667s: mặt Khoai còn thấy.
- f164 / 6,833333s: chuyển sang món, mất mặt.
- f200 / 8,333333s: vẫn món.
- f201 / 8,375s: trở lại hai mặt.

![N02 f163 — còn mặt Khoai](C:/Users/PC/Downloads/du_an_nem_bui/216_n02_face_coverage_check/all_240_frames/frame-0163.jpg)

![N02 f164 — cut sang món](C:/Users/PC/Downloads/du_an_nem_bui/216_n02_face_coverage_check/all_240_frames/frame-0164.jpg)

Hints ASR cho thấy cut có thể che một phần “đứng”/“chờ” (~0,507s tới speech-end hint), **không phải cả1,542s cận món đều là thoại**. Không dùng ASR thay nghe/khẩu hình; không cắt mất chữ “chờ”.

**Khuyến nghị PA:** tìm/bổ sung coverage Khoai nói thấy mặt qua hết ý, cùng audio đã duyệt nếu khả thi. Hai cơ chế cần so sau kiểm route: nối phần thiếu với nguồn mặt phù hợp, hoặc làm một N02 thống nhất để tránh jump pose/gaze. Chưa chứng minh cơ chế nào làm được, chưa quote hoặc quyền sinh.

**PB chỉ là phương án dự phòng:** cuối ký ức chuyển có động cơ sang Đào đang nghe, rồi N03. Cần diff coverage owner duyệt và nguồn F0/listener phù hợp; không tự lấy cận Đào cầm cốc/mấp máy hoặc dịch tail sớm để vá. Không dùng PB cho toàn bộ lượt thoại.

## 5. Ai xử lý phần nào tiếp theo?

**Tôi/root và các vai xử lý:** đối soát source/ref bàn–món đúng phiên bản; kiểm thêm native/ranges cần thiết; lập gói G1 hình có nhãn candidate/gap; chuẩn bị brief PA, kiểm route hiện hành, ràng buộc giữ giọng/PCM/face, biến thử/acceptance/stop. Không đẩy việc chuẩn bị frame hay truy dữ liệu kỹ thuật sang owner.

**Owner trực tiếp chốt khi có gói đủ rõ:** G1 storyboard ảnh/bản dựng thử, G2 N02 proof, G4 toàn cảnh, G5 export; PB nếu thay coverage; đổi audio/pause/sample nếu đề xuất; mỗi request chi riêng theo215. Lượt này không yêu cầu trả lời lại lời thoại, POV, động cơ hoặc lựa chọn tầng4 đã khóa.

**Phải kiểm dữ liệu/thử thật trước kết luận:** N02 hình–giọng–môi liên tục; chuỗi A/B; source food/table authoritative; actual turn offsets và nhịp30s; khả năng Flow giữ đồng thời hình và giọng. Mẫu giọng chuẩn local chưa được cung cấp cho SIA, root cần truy nguồn/chốt cách cấp evidence, không tuyển lại giọng. Khi AI thiếu kênh nghe, checkpoint nghe/xem của người thật phải ghi đúng target/scope, không nhận thành agent đã nghe.

Không gọi generation-ready hoặc chuyển Quality vì paper/checklist/test code xanh. Chưa dùng browser/API/credit/cài mới/git trong218. Ngân sách/feature live chưa kiểm nên không đưa giá từ log cũ ra xin duyệt.

## 6. Tổng hợp vòng

1. **Đã xác định:** tám role runs thực có báo cáo; mã chốt chặn đã được phản biện và kiểm thử; nguồn N02/audio202 không đổi. Có candidate dùng một phần, chưa có trọn chuỗi hình đáp ứng214 được chứng minh.
2. **Quyết định đã chốt:**217 A/A/A; giữ C-v0.6, K20/D06, storyboard214/POV/cốc tự nhiên/A→bát→B/bạn bè; owner checkpoints như đã duyệt. Không tạo approval media mới.
3. **Giả định sử dụng:** audio202 giữ cho comparison đầu; OPEN7 là diagnostic;30s là target; nguồn ngoài phạm vi đã xem chỉ là candidate, không mặc định tốt/xấu.
4. **Còn mở:** G1 hình/bản dựng thử đầy đủ, N02 coverage/AV/gaze, dữ liệu bàn–món, causal action/ending, timing và actual hearing/fullAV. Finishing giữ chặn.
5. **Bước tiếp:** hoàn thiện gói hình/input N02 theo PA và preflight khả thi; chỉ trình request thử có quote/cap/criteria hiện hành khi đủ đầu vào. Chứng minh N02 trước mở phần thoại còn lại, rồi action chain → full rough cut → finishing/export. Không nhận dự án đã khắc phục xong từ lượt triển khai này.
