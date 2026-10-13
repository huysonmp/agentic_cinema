# REC281 — Chốt nhịp đưa bát–bỏ nem; món cần sửa từ đầu vào

Ngày 13-10-2026. **ARTISTIC_DIRECTION_RECORDED / FOOD_REFERENCE_REWORK / NO_PAID_RUN.**

## Quyết định owner

Owner nhận xét “hình ảnh nem bùi fail quá, mà đoạn này có cần thiết không vậy”, rồi chỉ định: **“đoạn này chỉ nên là gắp bỏ vào bát cho thôi, đào đưa bát ra và nói là được”**.

Chốt đúng nhịp: **Đào đưa bát của mình ra và đáp; Khoai bỏ phần nem đang giữ vào bát cô.** Không đút ăn, không gắp lại từ đầu, không thêm cảnh kéo bát/giữ pose cầu kỳ. Nhịp này xác nhận lời “Anh gắp cho em mà”, nên còn vai trò trong câu chuyện; một cảnh chuẩn bị C07 riêng kéo dài không bắt buộc.

Giữ N07 “Thế em quay lại đúng lúc rồi”, D06, K20 và hai nhân vật là bạn theo lựa chọn trước; owner không yêu cầu đổi lời/giọng hoặc bỏ C09. C07–C08 có thể thành một nhịp nghệ thuật liền, chưa tự chốt một request duy nhất hoặc số take. Quy tắc endpoint C07 bắt buộc chưa nhận/C08 mới thả ở hồ sơ cũ không áp nguyên xi cho thiết kế mới; không hồi tố video lỗi thành đạt.

## Nem sai ở đâu — đã đối chiếu trực tiếp

Đã xem lại hai ảnh thật được duyệt, master v5, ảnh C06 F56 và native T03 F0. Mẫu thật có cấu trúc thịt/bì rời, mỏng, cong và mép không đều, thính phủ hạt nhỏ. Đĩa trong scene có nhiều phiến rộng/dày/đều hơn; phần A trên đũa thành lát đặc hình chữ nhật, không đọc giống phần gắp từ mẫu.

**Sai lệch đã có trong master/ảnh cảnh trước T03.** Vì vậy chỉ sửa chuyển động, đổi model hoặc thêm “cold Nem Bui” vào prompt không đủ. Prompt sửa món trước tại `02_refs/MASTER01_food_repair_v2.txt` nhấn mạnh flat slices/ribbons để chống sợi mì; đây là một điểm cần hiệu chỉnh cho khớp ảnh thật. Không khẳng định một cụm từ là nguyên nhân duy nhất của kết quả model.

**Thiếu sót của kiểm trước:** mục FOOD ở báo cáo REC280 chỉ ghi bàn/đĩa còn và không khói; chưa đối chiếu đủ hình thái món với hai ảnh thật. Việc đó không chứng nhận chất liệu nem đạt. Nay ghi FOOD_REFERENCE_REWORK, không lấy approval master cũ để bác vấn đề owner vừa phát hiện. Các scope tiếng/diễn của cảnh đã duyệt vẫn giữ, nhưng hình món và điểm nối liên quan cần rà lại đúng phạm vi, chưa tự làm lại toàn tập.

### Bằng chứng và hash

- `nembui.jpg`: `a51303f7100edd0944dc00daa19402fecfe24bb0e15a4143da8f8eae7b9e3a2d`.
- `z7750931050074_6fa76793489e54e476846aad4d233684_806643377.jpg`: `1237956e99458385f95f1edf18e0a98e1bddb777030ac1d69fab05fa7a51d741`.
- Master v5: `ab31c41ec168aea7fff2206d1536c9ff61c763c3da175defe7cc4bd14649bf96`.
- C06 F56: `69fb0e62a3a6f138a0eae622603945b248ec8d2809c8cda513dcdfdc33d00863`.
- T03: `ae876978fb19265601e4082c5e4cb7079c481786b11a2f8309be362b0881a50e`, vẫn NOT_SELECTED.

## Bước tiếp và vấn đề còn mở

Brief mới: `restart_720p_v1/04_requests/receive-deposit-artistic-brief-281.md`; quyết định: `00_decisions/receive-and-deposit-simple-beat-281.json` trong folder restart.

Tiếp theo chuẩn lại phần món và khung đưa bát–bỏ nem; đồng thời kiểm mức món xuất hiện trong các cảnh đã có để xác định phần nào cần sửa và điểm nối nào bị ảnh hưởng. Chưa tự áp phương án tách hình–thoại từ REC280, tạo ảnh hoặc video mới, dựng/rút lời hay tăng ngân sách. Ảnh sửa sau đó cần được xem và chốt trước request mới; căn cứ chọn route/số take/timing phải bám nhịp mới.

Đã xác định: hành động lõi gọn và tự nhiên, phần món trong nguồn còn lệch. Quyết định: Đào đưa bát–nói, Khoai bỏ nem vào bát. Giả định giữ lời/giọng/C09. Còn mở: nguồn món sửa, phạm vi cảnh cũ bị ảnh hưởng, route/khẩu hình/timing và review độc lập. Bước tiếp là chuẩn đầu vào, chưa chạy trả phí.

REC281 chi 0; sổ giữ **217/500, còn 283 credit**, reserve 110 đóng. Agent actual REC280 chưa hoàn tất vì giới hạn sử dụng; không có báo cáo mới hoặc chất lượng media PASS từ việc viết brief.
