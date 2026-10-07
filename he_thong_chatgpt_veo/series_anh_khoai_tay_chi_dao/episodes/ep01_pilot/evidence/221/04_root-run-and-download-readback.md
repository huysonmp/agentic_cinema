# 221 — Nhật ký chạy và đối soát native

## Thực thi

Owner “ok” duyệt đúng REC220-N02-PA-V-R1; quyền ghi trong owner-approval.json trước submit. Đã rehash N02 local, khớp `72cbaf7d…805a153`. Picker trong đúng project trả duy nhất `Character recording audio direction Video`; gắn một video chip, không voice preset. UUID không lộ trong chip, không tuyên bố đã hash cloud source.

Giữ nguyên prompt220, Omni 1.1 Flash / Video / Thành phần / 360p / 9:16 / thời lượng theo video 10 giây / x3 / Agent OFF. UI quote30; số dư107. Lưu pre-submit fullAX+PNG. Gửi **đúng một lần** lúc `2026-10-06T16:15:37.902Z`. Ba đầu ra hoàn tất, native đã tải; số dư77, delta30 (không phải billing receipt). Không retry generation/fallback/Quality/voice mới.

Mapping cloud asset và file/hash: run-manifest.json. Labels A/B/C theo ba vị trí trong batch; thứ tự tải thực C→A→B, không theo thứ tự hoàn tất.

## Download: sự cố công cụ, không suy diễn lỗi Flow

- C, tab1: chờ event download20s rồi timeout sau chọn360p.
- Mở tab3 đến đúng assetC, thử cùng native: event15s timeout. Sau đó đọc metadata Downloads thấy **cả hai file đều đã lưu**, cùng1.015.240byte và SHA256 `9bd637ed…2a494d`.
- Không cần sinh lại. Copy bản tải đầu vào folder221; giữ nguyên hai downloads, không xoá dữ liệu.
- A/B: chọn native360p qua UI, kiểm file mới theo tên timestamp tương ứng, hash/probe. B có toast “Đã tải video của bạn xuống!”.
- Đã đọc browser troubleshooting và pageAssets docs. Inventory tab sạch không có video asset; không dùng guessed URL, fetch, source-code API hoặc bundle media khác để thay output.
- **Kinh nghiệm:** timeout của waitForEvent không chứng minh tải thất bại. Đối soát file mới trên disk, thời gian thao tác, kích thước/hash và probe trước retry. Khả năng event của browser layer chưa trả download vẫn là giả thuyết; không khẳng định nguyên nhân nội bộ chưa được kiểm.
- Tab phụ3 đã đóng. User tab1 giữ project, prompt trống, Generate disabled; AgentOFF, Omni360p10s/x3. Không sửa source, watermark/account/voice.

## Đối soát kỹ thuật và giới hạn

Script `scripts/inspect_ep01_n02_edit_trial.py` đã chạy thực, ba file: 360x640, H.264,24fps,240frame/10s, AAC48k stereo10,005s. Mỗi file trích đủ240ảnh, WAV review, board0,5s và scene-hints; lưu folder Downloads221/inspection. Hash nguồn/outputs kiểm trước và sau khớp. Script compile thành công, không tạo vendor media/chi credit.

PCM cả ba khác nguồn. Tương quan waveform zero-lag: A0,9657/B0,7068/C0,9702. Đây là phép đo tín hiệu, **không** kết luận sai giọng hoặc đổi lời. Cần kiểm alignment/nguồn tiếng và nghe thực; không ghép đè WAV gốc để che khác biệt.

Root xem thật ba contact boards toàn10s với sampling0,5s:

- A vẫn có cận món khoảng7–8s, chưa khắc phục mục tiêu visible-speaking coverage.
- B không có cận món trong20mẫu, nhưng cắt sang hai người trước7s; cần kiểm hết lời/khẩu hình chứ không chỉ “có mặt”.
- C không có cận món trong20mẫu, giữ cận Khoai lâu hơn, nhưng **sinh phụ đề ngoài yêu cầu** khoảng4–7s.

Đây là quan sát ảnh lấy mẫu, chưa continuous AV, actual hearing hay final coverage verdict. Các reviewer EDIT/CONT/SIA được giao kiểm độc lập cùng media/hash và giới hạn capability, không chỉ prompt. Không full-film PASS.

## Khôi phục phiên reviewer

Các follow-up ban đầu không có report trên disk. Snapshot runtime chỉ thấy EDIT/SIA `pending_init`, CONT cũ không còn trong danh sách. Root không nhận các phiên này là đã thực hiện kiểm221.

Root khởi động CONT mới cho đúng phạm vi reviewer đã duyệt (`rec221_cont_review`); thử tạo SIA mới bị giới hạn số thread nên không có run mới từ lần thử đó. Ngắt hai phiên pending và gửi lại task vào EDIT/SIA cũ. Snapshot tiếp theo xác nhận ba reviewer đều `running`. Các báo cáo chỉ được tính sau khi file thực tồn tại và root đọc đầy đủ; sự tồn tại tên vai/trạng thái running không phải PASS.

## Sửa sai số của bảng ảnh chẩn đoán, không sửa native

EDIT chỉ ra board cũ dùng `fps=2` có thể chọn input frame gần mốc nhưng nhãn là output PTS. Ví dụ C, thumbnail nhãn4s có chữ trong khi native frame96/4s chưa có chữ. Vì vậy không dùng nhãn board cũ để kết luận chính xác onset/cut. Những khoảng root ghi ở trên chỉ là định vị sơ bộ.

Root đã tạo thêm `contact-exact-native-0.5s.png` cho cả ba bằng `select='not(mod(n,12))'`, giữ input PTS ở24fps: n=0,12,…,228; không ghi đè board cũ hoặc native. Đã xem board exact C: mốc2,5s có hình hòa chồng; 4s chưa caption,4,5s có caption. Biên chính xác phải mở native frames. Script inspector đã đổi sang chọn exact frame và kiểm24fps cho lượt sau, compile thành công. `technical-inspection.json` vẫn là bản chạy ban đầu, không giả nó được sinh lại với thuật toán mới.

Kinh nghiệm: label thời gian sau resampling không mặc định là thời gian/frame nguồn; QA boundary phải dùng index/PTS của native. Đây là lỗi định vị ảnh review, không bằng chứng output đã đổi lời hay lý do generation lỗi.
