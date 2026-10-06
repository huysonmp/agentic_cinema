# EP01 — Một lần thay nguồn N02 bằng riêng Khoai/K20

Ngày 2026-10-06. Owner **“ok”** sau đề nghị199: dành tối đa10 trong100 còn lại cho đúng một output thay trọn N02. Đây là đổi phạm vi, **không cộng ngân sách**, không mở tuyển giọng/x3 hoặc retry.

## Quyết định và preflight

- C-v0.6 giữ nguyên: “Khoan. Mùi này làm anh nhớ đến bếp nhà anh. Hồi bé, mẹ rang gạo, anh đứng chờ.” Toàn bộ thuộc Khoai; đoạn hồi tưởng không là giọng trẻ em/Đào.
- K20 custom Orus `fb1188da-e6c8-4156-9bba-0576c01a8da6`; picker kiểm ID/sample/performance đã chọn, không sửa preset. Chỉ một voice chip và một mention audio đúng ID; **không D06/Aoede**.
- Ảnh OPEN7 `43057def-574c-4ca7-916c-d55083f9b670` gắn trước giọng; đọc ID từ ảnh chip qua DOM, không bấm chip làm gỡ nguồn. Đây là input diagnostic tiếng, không approval hình final.
- Đọc trực tiếp Omni1.1Flash / Thành phần / 360p / 9:16 /10giây /x1; **giá7**. Không lấy quote Lite10 làm giá tuyến giọng. Tác nhân tắt, không cảnh báo input; prompt đầy đủ và screenshot cuối được xem trước gửi.
- Có hai Orus tùy chỉnh trong picker; chọn theo ID K20 và performance “Nam khoảng33 tuổi…bo tròn âm”, không theo tên giống nhau. Khi gõ@, picker tự hiện giọng khác; đã lọc lại Orus, kiểm ID rồi mới thêm mention.

[Approval](evidence/200/approval.json), [preflight](evidence/200/preflight.json), [prompt thực tế](evidence/200/prompt-actual.txt), [ảnh giá](evidence/200/settings-preflight.png), [ảnh trước gửi](evidence/200/final-preflight.png).

## Kết quả tạo và giới hạn tải/QC

Đã bấm tạo **một lần**; compose trống và một ô mới xuất hiện, sau đó UI hiện tiến độ. Account **154→147**, trừ7 khớp quote. Không gửi lại. [Nhật ký gửi](evidence/200/submission.json).

Đã có một clip mới trên Flow, tên **Character recording audio direction**, ID `3b312ed6-ac2b-4798-b965-cffe5f738893`; UI hiện10giây/360p, phát chạy được rồi đã tạm dừng. [Mở đúng clip mới](https://flow.google.com/u/1/project/9276788e-9781-44fb-ba5b-083006667374/edit/3b312ed6-ac2b-4798-b965-cffe5f738893). [Ảnh kết quả](evidence/200/completed-ui.png) chỉ chứng minh UI có kết quả, không chứng minh giọng đúng.

Hai lần chọn tải **360p Kích thước gốc** (tab hiện hành rồi tab mới cùng media ID), mỗi lần wait download20s timeout. Kiểm folder Downloads chưa thấy native mới. Thử capability asset sau khi phát: không có video asset được liệt kê, DOM cũng không có video element; không đoán URL hoặc gọi API nội bộ. Đã dừng retry tải, không tạo clip mới để chữa lỗi tải. Giữ tab kết quả cho owner.

Chưa có file native/SHA/decode/WAV/ASR hoặc kiểm nghe. Không dùng metadata/input binding để tuyên bố giọng đã đúng. N02 cũ/A03 vẫn REWORK; N02 mới **chờ nghe và nhận file**, chưa SIA PASS hoặc ghép vào phim. Sáu lượt khác chưa có nghiệm thu đầy đủ. Một screenshot cho thấy góc hình thay đổi trong timeline; hình chỉ diagnostic, không chọn làm coverage final.

Handoff cụ thể: owner mở clip trên, nghe toàn N02 để xác nhận một giọng nam K20 xuyên suốt; dùng menu tải360p gốc, lưu vào folder200 và báo tên file. Root đối soát đúng media/file, full decode, tách WAV giữ nguyên và kiểm điểm nối trước thay nguồn dựng. Không yêu cầu owner tuyển lại giọng hoặc sửa script.

Skill computer-use dẫn đến kiểm qua UI trình duyệt, dùng ID thực và kiểm trạng thái sau thao tác; không điều khiển login/cửa sổ native. Lưu screenshot trước/sau và file thực khi tải, không coi toast là hoàn tất.

## Tổng hợp

- Đã chốt: một N02/only-K20/x1/tối đa10, giữ lời và cặp giọng; không retry.
- Đã xác định: đầu vào đúng ảnh/một giọng/một mention; giá actual7, đã gửi, account giảm7.
- Giả định: single-speaker giảm nguy cơ lẫn vai; vẫn phải nghe đối chiếu.
- Còn mở: native chưa nhận qua điều khiển trình duyệt; lời/giọng thực tế, nhịp nối N01/N03 và gate bản cuối.
- Tiếp: owner nghe/tải clip đúngID; root nhận/decode nguyên nguồn, tách WAV không đổi tốc độ/pitch/gain trước thay nguồn dựng. Không báo tải thành công khi chưa có file.

Cap422, spent329, còn93; chi vòng này7. Phần hình theo dự trù reallocation còn90;3 chưa dùng của trần sửa tiếng không là quyền retry. Chưa Quality/master/phát hành. Folder owner: `C:/Users/PC/Downloads/du_an_nem_bui/200_n02_replacement/`.
