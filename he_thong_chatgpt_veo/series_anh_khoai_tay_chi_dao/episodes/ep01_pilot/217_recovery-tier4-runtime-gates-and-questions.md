# 217 — Tầng 4: vận hành vai chuyên môn và cổng kiểm không được bỏ qua

Trạng thái: TIER4_OWNER_APPROVED / LOCAL_EXECUTION_STARTED. Các mô tả chưa thực thi bên dưới là trạng thái tại lúc trình 217; kết quả thực phải đọc ở run log 218. Không paid generation, external tools/API hoặc cài mới. Tier3 A/A/A/A giữ nguyên.

## Không bắt đầu bằng thêm chức danh

Đã đọc operating model DIRECT01, common runtime PROD7/02, readiness DIRECT07 và SIA10. Các hợp đồng cũ đã có độc lập, version, capability và chốt chặn; lỗi 209–210 là không thực thi đủ và không gắn tất cả đường dựng vào gate. Kế hoạch khắc phục cần đưa các vai hiện có vào các run thật theo đúng artifact, không chỉ viết thêm thiết kế.

Các nguồn cấp hiện hành: C-v0.6/178, tier1/212, tier2/213, storyboard approved/214, asset screening/215 và N02 local216. Script32/canon/report giấy cũ chỉ là lịch sử/context không thắng 178–216. Audio202 là ứng viên owner đã duyệt, chưa là formal SIA mới hoặc AV PASS trên hình mới.

## Phân công dự kiến và bằng chứng cần có

| Vai | Nhiệm vụ trong khắc phục | Đầu ra thực, không chỉ tên vai |
|---|---|---|
| DIR | Giữ đích kể chuyện; tích hợp thay đổi từ clip sang cảnh | Beat map, lý do giữ/cắt, vùng được đổi/chờ owner và bản tích hợp theo đúng storyboard |
| DOP | Mặt/mắt, composition, ánh sáng, góc và hướng nhìn | Bố cục/camera intent, vùng mặt–món–tay cần thấy, so reference và coverage gap |
| ACT | Ý định, nghe, nhớ, gắp lén, biết bị bắt, chữa cháy | Hành vi quan sát được, cue/đầu–cuối hành động, lỗi diễn cụ thể, không tính từ chung |
| EDIT + DLG-EDIT | Chọn đoạn và nối toàn cảnh đúng lời/nguồn/ý nghĩa | EDL có frame/range/hash, line-to-picture map, continuity A/B và bản dựng thử có trạng thái thật |
| CTD + PROMPT/FLOW | Chuyển nghệ thuật thành phép thử/request khả thi trong Flow | Feature/route/quote live, inputs đã duyệt, giả thuyết/biến, tiêu chí dừng; không tự đổi ý đồ hoặc tiêu tiền |
| CINE-LIGHT, PERF, CONT/FOOD | Phản biện hình/diễn/cắt/món trên candidate và cả phim | Findings theo frame/timecode, scope/capability, severity, expected/observed và bằng chứng kiểm lại |
| SIA + AV-VOICE/AV-CUT | Đúng câu–người nói–giọng–miệng và hình/tiếng | Bảng từng lượt, reference/provenance, kiểm nghe/AV thật khi có capability; không lấy transcript làm heard_text |
| Root | Quản phiên bản, capability, dependency và đóng lỗi | Run registry, tổng hợp bất đồng, change log, readiness theo từng scope; không tự đóng phản biện vì đã duyệt một clip |
| Owner | Lựa chọn nghệ thuật, thay đổi nền tảng, request/chi và nghiệm thu | Approval có artifact/version/hash/phạm vi; không mặc định phải tự tìm lỗi kỹ thuật hoặc đọc mọi log |

Maker và reviewer không được tự duyệt cùng artifact. Cùng một agent có thể làm task khác nhưng không gọi review chính output của mình là độc lập. Run có RUN_ID/output thực; NOT_RUN/PAPER/SAMPLED_FRAMES/CONTINUOUS_VISUAL/FULL_AV/ACTUAL_LISTENING là các bằng chứng khác nhau.

## Các cổng đề nghị

### G0 — Context và capability

Khóa phiên bản, nguồn, ranh giới quyền; thử xác nhận công cụ nào xem ảnh, nghe và xem AV thật. Reviewer chưa nghe không nhận scope audio PASS. Ảnh dày giúp hình/continuity nhưng không tự thành nghe/xem AV liên tục. Thiếu capability phải ghi HOLD và phân công human checkpoint hoặc trình lại; không tự mở tool ngoài tier3-Q3-A.

### G1 — Thiết kế và bản dựng thử

Chạy đóng góp DIR/DOP/ACT/EDIT, tích hợp bảng source range/coverage, review độc lập đúng scope. Bản dựng thử bằng ảnh/audio có nhãn hạn chế; kiểm đủ N01–N07, người nói/nghe, mặt, F0–F4, đường A/B và thời lượng 30 giây. Chưa đủ timing phải trình conflict, không bỏ lời/biểu cảm.

### G2 — Phép chứng minh N02

Kiểm ứng viên 216 trước, xác định khoảng thiếu thực. Nếu cần sinh, trình inputs/prompt/route hiện hành/quote/output/cap/criteria và owner duyệt. Sau kết quả kiểm nguồn, mặt, giọng và khẩu hình; không áp PASS paper/ASR cho output. N02 chưa đạt không mở sản xuất cả phần thoại, không dùng Quality như cách sửa lỗi ngữ nghĩa.

### G3 — Đóng chuỗi hành động

Tiếp R04–R08: ý định gắp về miệng → Đào quay lại → Khoai khựng → đổi hướng → bát nhận → thả. Phản biện theo clip và bản nối. Món/đũa/miệng/cốc/bát/rau/chấm kiểm trong cùng bối cảnh, không sửa lẻ để làm ảnh đẹp rồi mất action. Đo nhịp thực, giữ R09 kết.

### G4 — Bản dựng toàn cảnh

Xem chuỗi không tiếng để kiểm ý nghĩa hành động; nghe/xem có tiếng để kiểm diễn, speaker, sync và nhịp; đo các cut và kiểm tiêu chí diễn xuất ở đúng phiên bản. Cần thực xem/nghe để đóng các scope đó. Không lấy trung bình điểm để bù lỗi người nói hoặc mất quan hệ hành động.

### G5 — Finishing và bàn giao

Chỉ finishing sau G4 và lựa chọn của owner. Caption/mix/cut sửa phải kiểm lại phần phụ thuộc trên export hiện hành; các approval source audio không đổi có thể giữ cho scope source, nhưng không thay kiểm AV mới. Hash/source/gate evidence sai hoặc report stale phải chặn đường bàn giao. File export kỹ thuật hợp lệ vẫn có thể chưa được nghiệm thu/phát hành.

## Chốt chặn đề nghị, không nhận đã code xong

Một wrapper/gate manifest dùng chung cho đường dựng/finishing/bàn giao: target hash + EDL/source hashes + approved input versions + reports theo scope + open findings/closure + owner decisions. Đường PLANNING được phép render thử nhưng nhãn NOT_RELEASE và giữ UNKNOWN; đường DELIVERY phải từ chối thiếu report hoặc blocker.

Validator chỉ kiểm sự tồn tại/tính nhất quán/phạm vi của bằng chứng. Không tự đánh giá một bộ phim, không xác minh reviewer khai thật đã nghe chỉ bằng boolean, không bảo đảm tuyệt đối chống mọi sai sót. Root phải read-back nội dung thực và owner checkpoint kiểm nơi AI thiếu capability.

Phạm vi chặn bằng code là các đường local được tích hợp trong repo; không hứa chặn nút tạo/xuất trên Flow hoặc thao tác Canva bên ngoài. File từ đường ngoài cần nhận về, đối soát hash và review như target mới trước khi repo ghi là đủ điều kiện bàn giao.

Những tình huống phải thử khi triển khai: bỏ report DIR/PERF; SIA chỉ transcript; báo cáo khác hash; báo cáo cũ sau đổi range/cut; MAJOR chưa đóng; duyệt short reaction bị dùng thay duyệt cả cảnh; mặt không được thể hiện nhưng technical tests xanh; PLANNING bị gọi là DELIVERY. Mọi test mới là fixture integrity, không phải chất lượng phim thật.

## Dừng, xử lý lỗi và quyền thay đổi

- Thiếu media/tool/report → HOLD, không gọi là lỗi output đã được quan sát nếu chưa có evidence.
- Sai lời, speaker/voice, mouth attribution; mất mặt nhịp chốt; ý định–phát hiện–chữa cháy không đọc được; miếng nem vào miệng trước cho Đào; sai món quan trọng → REWORK scope, không mở finishing.
- Mỗi finding có nguồn gốc: source/ref → prompt/request → take → range/EDL → audio placement → export. Sửa tầng phát sinh, kiểm dependency bị ảnh hưởng, không xử lý bằng che mặt hoặc đổi nhãn speaker.
- Cắt/coverage thay đổi nhiệm vụ kể chuyện, canon/lời, voice identity, món/cách dùng hoặc vượt ngân sách/công cụ → trình owner. Sửa lỗi file/format trong scope được giao có log; không mặc định hỏi mọi thao tác kỹ thuật nhỏ.
- Mỗi lần sinh mới: approval riêng theo tier3-Q4-A. Retry không tự được cấp, dù cùng prompt hoặc còn số dư.

## Tầng 4 — ba quyết định cần owner chốt

### Q1. Cách chạy các vai hiện có

- A: giao DIR/DOP/ACT/EDIT thành các nhiệm vụ chuyên biệt có đầu ra riêng; reviewer độc lập theo scope, tích hợp sau đóng góp. Khuyến nghị sơ bộ: truy rõ trách nhiệm/phát hiện, không tự review thành độc lập; nhiều report hơn nhưng root phải tổng hợp gọn cho owner.
- B: một context maker tổng hợp nhiều vai, một context critic độc lập tổng hợp các scope. Ít đầu mối, vẫn maker–critic tách; dễ mất sâu chuyên môn/khó truy hơn nên cần checklist scope đủ.

Nếu owner chọn A/B với yêu cầu chạy agent rõ, đó là quyền giao bounded local role work/đọc media trong allowlist và viết report; không là quyền agent browser/credit/API/git/release. Không dispatch paid generation hoặc tác vụ outside scope.

### Q2. Chốt chặn cần được thực thi bằng gì?

- A: registry/checklist chuyên môn và gate local bắt buộc trong các đường dựng/finishing/bàn giao. Khuyến nghị sơ bộ để khắc phục việc contract có nhưng renderer bỏ qua; code kiểm bằng chứng, không chấm nghệ thuật.
- B: registry/checklist và root kiểm bằng tay trước mỗi bước, chưa sửa code gate. Bắt đầu nhẹ hơn nhưng phụ thuộc thực thi thủ công, vẫn không được thiếu review; không gọi fully enforced.

### Q3. Owner muốn duyệt ở các mốc nào?

- A: bản dựng thử/storyboard ảnh → phép chứng minh N02 → bản dựng toàn cảnh → export cuối. Khuyến nghị sơ bộ; root/agent sàng lọc lỗi rõ, trình phát hiện và phần chưa kiểm. Khi thiếu kênh nghe của AI, owner nghe/xem ở mốc tương ứng là human evidence, không ghi thành agent đã nghe.
- B: thêm duyệt từng cảnh được chọn trước ghép, rồi vẫn duyệt bản toàn cảnh và export. Kiểm soát chặt hơn lựa chọn clip, đổi lại nhiều lượt duyệt; approval clip vẫn không thay full-film review.

Cả hai không thay approval chi từng phép thử. Không đề nghị owner duyệt mọi output lỗi đã rõ hoặc tự làm công việc kiểm nguồn/hash/EDL của root.

## Tổng hợp vòng và bước tiếp

Đã chốt tier3 A/A/A/A; đã kiểm local sâu N02 tại216, chưa trả phí. Giả định giữ các vai hiện có và cơ chế Flow/local, không tuyển thêm chức danh. Còn mở: Q1–Q3, capability nghe/xem và source ranges đủ R02, các cổng chưa triển khai.

Sau owner trả lời: đăng ký run phạm vi local, thực chạy các vai/reviewer được chọn trên input hiện hành theo capability, triển khai gate nếu được chọn, rồi trình khoảng thiếu/brief thử có quote hiện hành trước xin chạy. Không kết luận recovery đã hoàn thành từ việc thêm các file thiết kế này.

## Owner chốt tầng 4

Owner trả lời nguyên văn: “1 A; 2 A; 3 A”. Ghi nhận nhiệm vụ chuyên biệt với reviewer độc lập, checklist và gate local bắt buộc, owner duyệt bản dựng thử → phép chứng minh N02 → bản dựng toàn cảnh → export cuối. Root được thực thi bounded local role runs và gate code; không có quyền chi/generation/API/cài mới từ approval này.

Nhật ký thực thi: `218_recovery-role-runs-and-gate-implementation.md`. Không nâng 217 thành media quality PASS.
