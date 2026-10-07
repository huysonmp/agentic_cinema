# REC247 — Kiểm điểm nối thực trước khi quyết định sửa clip

## Đã xác định và chốt

Owner trả lời `ok` cho hai câu hỏi trực tiếp: đúng tiếng C01B T01/K20/“Khoan” và cho phép xác nhận quyền nhập lại exact C01A một lần trên Flow. Không mở rộng sang approval hình C01B, điểm nối, voice take mới hoặc cả phim. Xem quyết định247; nativeB vẫn nguyên vẹn.

Đã nhập exact cut C01A, tạo scene QC riêng `8c86ece4-e270-4da9-975d-088556e2024f`, thêm nativeC01B T01 đầy đủ4s sau C01A. Không chạm scene C01A/C02 đã chọn, không thay tiếng, tăng tốc, cận món che lỗi hoặc sinh video mới. Chọn khung dọc9:16 trước lưu/xuất; scene mới ban đầu mặc định16:9 nên phải kiểm khung trước export.

File `07_edits/C01A_C01B_T01_FLOW_JOIN_QC_247.mp4`, SHA256 `4f92cfd00ddf51b30dd99ec1d779fc703d22ea4fec0a51fd83ec8f0f4322a58d`: video177frame/7,380013s; audio7,36s, decode sạch. Flow xuất1280×2274, avgfps2718720/113357 (VFR), không tự gọi native720p/24fps hay final đúng tuyệt đối9:16. Trước final phải kiểm lại format, timestamps, audio và kích thước actual; không suy từ UI hoặc source.

Ghép/xuất/upload trong lượt này: cùng tài khoản số dư1.013 trước/sau, observed debit0; không suy mọi tính năng Flow đều miễn phí. Dự án vẫn67/500, còn433; reserve110 chưa được giải ngân.

## Bài học thao tác

Sau khi thêm clip, UI có thể tạm còn tổng thời lượng cũ/placeholder xám. Không nhấp lại theo stale state. Lưu scene và mở lại xác nhận hai thumbnail/2clip, tổng00:07:09 trước export. Không đổi native hoặc tạo lại vì preview đang tải.

Đăng ký download listener phải trước click download, và timeout của call phải đủ dài cho listener. Lần này listener đăng ký muộn, một call timeout còn reset runtime; listener sau không nhận event. Tuy nhiên Downloads có file mới7.208.023byte được UI xuất; đối soát đúng tên/thời điểm/hash/full decode rồi copy archive. Listener timeout không đồng nghĩa tải thất bại; không lặp export hoặc sinh clip để chữa lỗi điều phối listener. Không lấy file cũ/trùng tên khi chưa đối soát.

## Quan sát root và giới hạn

Root xem board6fps trang2/3 và fullframe zero-based80/81/96. Frame80 là cuốiA,81 là đầuB: tay trong đổi rõ sang trái/gần rim, ngón ngoài và food pile cũng khác. VùngB sau đó có two-hand rim trước khi thu. Đây là mẫu ảnh, không continuousAV, không AI nghe hay chứng nhận lip-sync. Phản biện độc lập bản ghép thực được giao riêng; chưa dùng draftT02 làm quyền submit.

Giả thuyết request: T01 “keeps her intention to take … until she hears” có thể cho phép thêm tiến/nắm; inner settle không khóa rõ hướng về thân/bát. DOP/ACT đã chỉ ra cùng mơ hồ. Không causalproof từ một output; source adherence của Ingredients cũng có giới hạn, không được hứa exactframe-lock.

DraftT02 chỉ sửa transition và sắc diễn: contact hiện có → nghe → release → rest; tay trong chỉ settleINWARD, không reach mới. Giữ source/voice/lời/camera/model/duration/đồ bàn. Không đổi audio chỉ vì ASR “Khuán”; tiếng exactT01 đã owner chấp nhận.

## Còn mở / bước tiếp

Root phải đọc đầy đủ report actualjoin độc lập, chốt severity và khả năng cứu bằng cut trung thực trước preflightT02. Chưa chọn B hoặc mở C03A; không bỏ onset “Khoan”, dùng audio overlay/speed/freeze/cover để che lỗi. Nếu T02 được phép và cùng blockerMAJOR lặp actual thì STOP theo238, chẩn đoán tuyến thay vì tự T03. Approval audioT01 không chuyển sangT02. Full phim30s/continuousAV/final vẫn chưa đạt.
