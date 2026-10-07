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

## Cập nhật T02, checkpoint Đào và T03 không có output

T02 quote10, một submit, cùng tab1.040→1.030; native720×1280/24fps/144frames, SHA256 `0b5615beef4e23a42428771109fe36544510270281ae35129de6f6c585a398a7`. Reviewer độc lập kiểm52 uniqueframes, root đọc đầy đủ: đúng tay ngoài; không thấy lặp rim-occlusion/early-return T01 trong mẫu. Nhưng chữ mới xuất hiện trên bàn ở đầu/giữa/cuối, và lòng tay ngửa/xòe giống giới thiệu món: hai MAJOR mới, không range sạch để nối C01B.

Owner đã nghe riêng tiếng T02 và trả lời “Đúng D06, lời và nhịp chấp nhận được”. Lưu exactWAV/sourcehash trong decision; chỉ đóng checkpoint tiếng Đào đầu tiên, không duyệt hình/khẩu hình hoặc waveform take sau.

Root giữ diagnostic HOLD, đọc đầy đủ ACT/DOP/critic. Đề xuất không đổi canon: palm-down/ngón hơi cong, đầu ngón hướng rim nhưng dừng trên gỗ trước rim; bỏ HIGH ABOVE/gap cứng; mô tả đúng biểu tượng nguồn thay câu watermark chung. Không chứng minh nguyên nhân model đã biết chắc. Preflight T03 qua có điều kiện, root kiểm exactbinding/readback/configquote10 và gửi một lần.

T03 bị Flow từ chối với cảnh báo liên quan nội dung gây hại trẻ vị thành niên; chưa có media. UI ghi không tính phí; số dư1.030→1.020 tạm trừ rồi trở lại1.030, net0. Giữ job/evidence, không chấm hiệu quả sửa tay/chữ hoặc gọi lỗi output. Đang kiểm một lần làm rõ bối cảnh vốn là nhân vật food hư cấu, trưởng thành, trò chuyện bình thường; không đổi source/voice/route hoặc né cơ chế an toàn. Nếu cảnh báo vẫn lặp, dừng trình hướng xử lý, không lặp sửa wording vô hạn.

Sổ sau hoàn T03:50/500 đã dùng, còn450; firstpass140/retake155/postrough45/reserve110 chưa quyền. Git commit local `f275ce3` lưu nhóm C01A evidence/approval; push hai lần gặp remote Internal Server Error, remote xác minh vẫn `4b7e2a6`. Không nhận đã đồng bộ hoặc thay quyền xử lý GitHub. Các cập nhật sau commit này vẫn cần commit riêng.

## Chọn đúng bản cắt C01A T04 và chuẩn bị C01B

T04 đã tải native 6 giây, SHA256 `bbf5c423bff3e30b98aa0ec5b7f56d11b89467456f75dcf1ea2fe3b0829efa43`. Đuôi kéo đĩa nên không chọn toàn native. Owner cho phép chạm vành và cử chỉ tay trong hạn chế, tuyệt đối chưa kéo/lấy món. Bản cắt riêng trên Flow xuất thực 81 khung, 3,375 giây, SHA256 `e22c113204c404e928683c69465237921f601f2b33a3eb9a9187eb0648f4b803`. Owner đã nghe đúng bản này: “Đúng D06, đủ lời và nhịp chấp nhận được”.

Root đọc đầy đủ kiểm độc lập: 42 khung riêng biệt của export, gồm mẫu dày 52–80; không thấy kéo đĩa, chữ mới hoặc cử chỉ giới thiệu món trong phạm vi đó. Root chọn đúng prefix dưới ngoại lệ owner; không nâng thành chứng nhận hình–tiếng liên tục, khớp môi toàn câu hoặc duyệt cả phim. Quyết định tại `00_decisions/C01A-exact-prefix-selection-246.json`; cả hai điểm nối và bản dựng thô vẫn phải kiểm.

Đã chuẩn bị C01B từ nguyên khung cuối80, 720×1280, hash `0cf422f2b28dae631785af6ec19fc7488800c0cf8d22bb95dddd04e1b7ae2acb`; không reset tay. DOP/ACT/EDIT đã có đóng góp và được root đọc đầy đủ. C01B chỉ Khoai/K20 nói “Khoan.” → Đào nghe, buông vành, thu tay; đĩa đứng yên. Đã upload ảnh và gắn đúng custom K20, kiểm prompt readback và cấu hình Omni 1.1 Flash/Ingredients/720p/9:16/4s/x1/Agent OFF, quote7. Chưa submit; còn cổng preflight độc lập.

Sổ trước C01B: đã chi60/500, còn440; firstpass140/retake145/postrough45/reserve110 chưa quyền. Số dư cùng account sau cắt/export/upload ảnh là1.020, không thấy trừ thêm so với sau T04. Giữ các số dư khác tab chưa đối soát như lịch sử, không coi đó là quyền thêm ngân sách.
