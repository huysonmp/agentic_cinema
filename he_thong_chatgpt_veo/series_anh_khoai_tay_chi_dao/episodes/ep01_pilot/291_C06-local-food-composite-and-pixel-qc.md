# REC291 — Ghép riêng vùng món, giữ khung vào C06 gốc

13-10-2026. Owner cho phép **“ghép ảnh cục bộ, giữ nguyên phần ngoài món”**. Biên bản: `restart_720p_v1/00_decisions/local-food-composite-approval-291.json`. Không cấp quyền chạy video trả phí, đổi giọng, source/EDL hoặc duyệt đầu ra chưa xem.

## Thực hiện

Đã đọc skill imagegen và hướng dẫn bảo toàn/kiểm toàn khung; thực hiện local đúng ngoại lệ người dùng yêu cầu, **không** gọi imagegen/API hoặc cài thư viện. Helper riêng `scripts/composite_ep01_food_entry_291.py` dùng Pillow đã có trong bundled runtime.

- **Base:** đúng khung cuối C05 REC269, 720×1280; không resize base. SHA `f091e35fc7c779591c918c47ba34752a8a2c3b30de507cd99dc0e76143e83196`.
- **Donor:** ảnh thử REC290, chỉ lấy vật liệu nem, không lấy mặt/hậu cảnh làm chuẩn. SHA `40be91b97b873979f09f01d1e530cd9512674dd2b26b1fc339237b0f23f37077`.
- **Hai vùng:** ụ nem trong đĩa và phần A đang kẹp. Mặt nạ là các envelope vẽ tay theo silhouette món/bóng sát mép, không phải semantic segmentation đã được chứng minh. Không thay cả đĩa hoặc di chuyển tay/đũa/bát/cốc.
- Feather hướng vào trong, không làm vùng sửa tràn khỏi polygon. Vùng đũa được chỉ rõ và lấy lại từ base. Nền lộ ra bên trong footprint miếng A cũ được dựng từ phần áo gốc kế cận, không donor body; **không khẳng định giữ pixel áo vốn bị món che hoặc mọi khoảng trống nằm bên trong mask**.

## Vòng chỉnh local, không thử thêm bằng credit

1. **V1:** số pixel ngoài mask đổi = 0; root xem toàn ảnh và crop phóng to, thấy viền miếng A cũ và phần phiến đặc phía trước đĩa chưa phủ hết. Không chọn.
2. **V2:** mở đúng footprint phiến cũ phía trước đĩa, giảm phần A donor và tách màu món; root vẫn thấy viền xám phía dưới A. Không chọn.
3. **V3:** tách nền native trong vùng A khỏi lớp vật liệu, phủ đủ silhouette/bóng sát miếng cũ rồi trả lại vùng đũa. Root xem toàn ảnh và crop A; viền cũ giảm, đĩa giữ vật liệu rời hơn. Bản để reviewer/owner kiểm, chưa tự duyệt.

Các config v1/v2 giữ lịch sử khám phá; chỉ v3 đã được chạy lại với helper cuối để kiểm tái lập. Không tuyên bố các v1/v2 tái lập bit-identical bằng helper cuối sau khi logic đã được chỉnh.

## Kết quả kiểm kỹ thuật v3

Candidate: `restart_720p_v1/02_refs/C06_ENTRY_LOCAL_v3_FOR_REVIEW_291.png`, **720×1280, đúng 9:16**, SHA `7c8023cbe655745b941e1a47dd1df3614ba66fcef512a41c5c4c4048bb33f8cc`.

Config v3 SHA `a64501e0543109d66386e4015023ab5bb85593349bf887444371229b9217b4a8`; helper cuối SHA `1debf60359207153ad9a7216d34dd22fda7ce75565ffee090f0c642dc17db432`.

PNG được mở lại để đối soát RGB: **ngoài mask 0 pixel thay đổi**, trong mask có **36.890 pixel thay đổi**; hash hai input không đổi. EDIT_MASK SHA `286f34063e546bc1151a8d4a0ed376191c6bffbf491809c8bb1d843d403118fa`. Chạy lại v3 ở folder riêng cho cùng output SHA. Dấu nguồn được giữ bằng pixel base, không vẽ lại hoặc thêm dấu giả. Ảnh là **dẫn xuất composite**, không giả là frame native Flow chưa chỉnh.

Root chạy phép đối chiếu đọc lại riêng cho tám ROI chữ nhật: mặt Khoai, mặt Đào, phố, cốc, hai bát, rau và dấu nguồn — tất cả pixel bằng nguồn. Tọa độ ghi trong registry; các mẫu ROI này không được diễn giải thành đã phân vùng hết mọi đối tượng theo ngữ nghĩa.

Bằng chứng số: `restart_720p_v1/06_qc/C06_ENTRY_local_pixel_evidence_291.json`. Folder owner `C:/Users/PC/Downloads/du_an_nem_bui/291_C06_LOCAL_COMPOSITE/` có inspection, v1/v2/v3 và v3_reproduce_check; trong v3 có mặt nạ, changed-pixel map, mask overlay, crop hai vùng và board **trái nguồn/phải bản ghép**.

## Phạm vi chất lượng và bước tiếp

Kỹ thuật giữ pixel ngoài **mask đã khai** không tự chứng minh mask chỉ chứa món theo ngữ nghĩa hoặc mép ghép đẹp. Phản biện độc lập đã xem source/candidate, mask/crop/board và tự tính lại pixel, root đọc toàn bộ [báo cáo](restart_720p_v1/06_qc/C06_ENTRY_local_composite_independent_291.md): ngoài mask 0 pixel đổi, trong mask 36.890, mask có 36.892 pixel khác 0. Không thấy lỗi lớn mới; **v3 đủ trình duyệt ảnh, có caveat nhỏ** ở cạnh A/nền áo vá khi phóng to, không nhận là ghép vô hình. Không dùng ảnh để nghiệm thu sắc thái B, voice, chuyển động, lip-sync hoặc điểm nối video.

Sau review ảnh: trình owner duyệt đúng candidate v3 làm tham chiếu vào, rồi mới lập prompt C06 theo sắc thái B và kiểm live route/voice/quote. Không đồng nhất image ingredient với khóa F0; cổng hình món C05/các cảnh trước và timing cuối 30 giây vẫn mở. Nếu reviewer tìm lỗi lớn thì giữ nguồn, không upload ảnh chưa đạt hoặc tự chạy video.

**Đã chốt:** phương thức local và sắc thái B. **Đã xác minh:** bảo toàn decoded RGB ngoài mặt nạ, giữ khung gốc và tái lập v3. **Giả định cần kiểm:** vật liệu/mép ghép/A đủ tự nhiên khi làm đầu vào. **Còn mở:** duyệt ảnh, route/giọng/quote live, video và continuity/timing toàn tập. Flow chi mới **0**; sổ **237/500**, còn **263**, phần tạo lại **26**, dự phòng **110** đóng. Không upload/đổi refs hoạt động, voice hoặc EDL.
