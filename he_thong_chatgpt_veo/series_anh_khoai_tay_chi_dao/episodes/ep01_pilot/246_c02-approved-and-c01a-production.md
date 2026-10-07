# 246 — C02 đã duyệt, mở sản xuất C01A

## Quyết định của owner

Owner: “ok được rồi đấy”. Đối tượng là bản cắt C02 T02 đã gửi ở lượt 245: `C02_T02_FLOW_0_7p5S_FOR_APPROVAL.mp4`, SHA256 `d151eb1d9f5f5b4486fed030579d9da3de0d23f434a65db2f6c4dca88b3228f3`. Root đã đối soát lại hash bản trong folder owner. Chấp nhận hình–tiếng, giọng Khoai, lời và nhịp của đúng bản cắt này. Đóng checkpoint C02, không chuyển approval sang đuôi native 10 giây hoặc bản phim chưa dựng.

Các báo cáo 245 giữ nguyên kết luận tại thời điểm chưa owner duyệt; hồ sơ approval mới ở `restart_720p_v1/00_decisions/C02-export-approval-246.json` cập nhật trạng thái hiện hành. Duration video thực 7,541667 giây/181 khung/24 fps; chưa khóa EDL 30 giây.

## Nhiệm vụ kế tiếp

C01A: Đào nói đúng “Anh nhìn mãi. Không hợp thì để em.”, bắt đầu đưa tay ngoài về mép đĩa, chưa chạm/di chuyển đĩa hoặc lấy món. Khoai im lặng lắng nghe. Kết ở trạng thái tay đang định lấy để C01B tiếp nối “Khoan.” → cô dừng/thu tay → C02 ký ức, không lặp từ Khoan.

Giữ người trưởng thành, bạn bè, quán bình dân ven phố, địa lý bàn và món nguội. Dùng ảnh trạng thái F0 trích nguyên khung 0 của export C02 được duyệt, không tạo lại master hoặc nhập footage nick cũ. Ảnh `02_refs/C01A_F0_from_C02_T02_v1.png`, 720×1280, SHA256 `c59ad1e436ad42e7525c564a883269ef9f80288f4c76b675e64bba1798500cad`. Đây là ảnh nguồn dẫn xuất, không video đầu ra đã đạt.

## Vận hành và quyền

Registry246 đăng ký DOP/ACT/EDIT đóng góp riêng, root tích hợp DIR và reviewer độc lập kiểm preflight sau tích hợp. Mỗi agent chỉ đọc local inputs và viết báo cáo được giao, không browser/API/Git/credit/tạo media. Root phải đọc đầy đủ báo cáo.

Cấu hình dự kiến C01A: Omni 1.1 Flash, Ingredients, một ảnh, một voice D06/Aoede mới `6dadc0b1-00c3-493c-943d-f4a1e4a88feb`, 720p/9:16/6 giây/x1/Agent OFF. Giá tham chiếu 10 không thay quote live. Quyền238 tối đa15/output trong phân bổ đã duyệt; sổ bảo thủ 30 đã dùng/470 còn, không sử dụng dự phòng110. Không test tay rời hoặc batch.

Tiếng Đào trong C01A là mốc nghe output sản xuất đầu, chưa được thay bằng duyệt preset239. Khi có candidate không mắc lỗi rõ, gửi owner nghe/xem trước mở rộng các đoạn Đào nói. Điểm nối chọn trên trạng thái ra thực và âm cuối, không tự khóa timestamp từ dự kiến.

## Tổng hợp vòng

- Đã xác định: C02 T02 đúng bản cắt đã được owner chấp nhận; chuyển sang chặng mở đầu/hỏi–đáp P3 của kế hoạch làm lại236.
- Đã chốt: giữ C02, không tạo lại vì nhãn test; giữ lời/vai và một voice mỗi clip.
- Giả định làm việc: khung F0 hiện tại đủ đường tay tới mép đĩa; chỉ là giả thuyết cần kiểm motion, không chứng nhận từ ảnh đẹp.
- Còn mở: tiếng Đào thực, đường tay C01A, dừng–thu C01B, khớp hai điểm nối và timing toàn phim.
- Bước tiếp: maker/reviewer → quote/binding/readback → một C01A sản xuất → tải/QC → owner nghe tiếng Đào và chọn endpoint thật cho C01B.

## Kết quả C01A T01 và sửa có mục tiêu

Root đọc đầy đủ DOP/ACT/EDIT và preflight độc lập, kiểm một ảnh nguồn/một D06, prompt readback, Omni 1.1 Flash/Ingredients/720p/9:16/6 giây/x1/Agent OFF. Giá đầy đủ đầu vào 10; gửi một lần. Native tải qua UI Original thành công, SHA256 `0c42df876e8d3b7b46fe1b7930f3fc33ecf1e462f6c3f66ddabf677efb6c67d4`, video 6 giây/144 khung/24 fps, tiếng 6,016 giây, giải mã toàn file thành công.

Hình mẫu cho thấy Đào dùng đúng tay ngoài để vươn, hai mặt và bối cảnh còn rõ; không thấy khói hoặc món bị lấy. Nhưng ngón tay che mép đĩa từ khoảng 3,333 giây tới sau âm cuối theo ASR, nên không xác nhận được khoảng hở. Tay tự thu từ khoảng 4,083 giây, trước “Khoan” ở clip chưa có. Reviewer đã xem 52 khung riêng biệt, gồm đoạn 3,5–4,208 giây từng khung; root đọc đầy đủ báo cáo. Kết luận **HOLD điểm ra C01B / sửa boundary hình**, không nói chắc tay đã chạm vật lý và không gọi lời ASR đúng là giọng đúng.

Không cứu bằng cắt trước “em”, giấu tay hoặc phủ hình món. T02 dự kiến sửa hai điểm: tay dừng cao hơn trên vùng trống bát–đĩa với khoảng hở hình rõ, giữ ý định chưa hoàn tất tới cuối. ACT phản biện thêm nguy cơ tay thành cử chỉ giới thiệu món; root tích hợp bàn tay thư giãn theo hướng vươn, không xòe lòng bàn tay trình bày. Giữ nguồn, giọng, lời và cảnh. Đây là giả thuyết sửa, chưa chứng minh nguyên nhân duy nhất hoặc chắc sẽ đạt.

Khoản T01 quan sát cùng tab: 1.050→1.040, trừ10. Sổ dự án bảo thủ 40/500 đã dùng, còn460; khoản lượt đầu còn140, tạo lại còn165, dự phòng110 chưa được giải ngân. T02 chưa gửi tại thời điểm viết mục này. Nếu cùng lỗi lớn lặp lại ở T02, dừng chẩn đoán, không tự T03.
