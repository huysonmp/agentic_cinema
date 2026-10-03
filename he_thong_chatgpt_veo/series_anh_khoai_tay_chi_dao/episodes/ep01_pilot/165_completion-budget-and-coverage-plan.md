# 165 — Tính ngân sách hoàn thành EP01

Ngày: 2026-10-03. Trạng thái: PLANNING / NO_NEW_GENERATION / REALLOCATION_PENDING.

Owner yêu cầu “ok tính toán đi xem nào” sau đề xuất kiểm tài nguyên và dựng nháp đủ tập trước khi tiêu thêm. Lượt này lập tính toán, không sinh media, không điều chuyển ngân sách hoặc tự duyệt ngoại lệ hình/giọng.

## 1. Ngân sách và căn cứ

Theo đối soát cuối vòng 164: trial còn 34; Quality riêng còn 100; số dư tài khoản lần kiểm cuối 334. Không đọc lại UI trong lượt tính toán, không coi toàn bộ số dư là quyền chi. Nếu owner duyệt điều chuyển toàn bộ Quality thì trần hoàn thiện là 34 + 100 = 134, không phải 334.

Giá dùng lập dự toán là quote đã quan sát: Veo Lite x3 = 30 (164), Omni voice-pair x3 = 18 (153/154). Giá Omni không phải giá Lite và không được gọi các lượt Omni là “ba Lite”. Đọc lại giá/model trước mọi submit. Không lấy tỷ lệ lỗi âm thanh hoặc refund làm nguồn ngân sách chắc chắn.

## 2. Coverage thực có và khoảng thiếu

| Nhịp cần có | Tài nguyên/căn cứ | Trạng thái dùng |
| --- | --- | --- |
| Mở bàn ăn, Đào trêu, Khoai liên tưởng | Ảnh bàn/nhân vật đã duyệt; clip mở cũ có lỗi hơi/cử chỉ theo 131–141 | Có nguồn cho animatic; chưa khóa đoạn video production |
| Chuyện mẹ rang gạo, chờ mẹ quay lưng | Kịch bản 32; giọng K20 đã chọn | Chưa có audio đầy đủ được nghiệm thu; chưa có shot đã khóa cho đoạn này |
| Đào quay đi, Khoai gắp | C01 thực có trong folder 159; owner đồng ý riêng cơ học gắp | Có ứng viên gắp; cần chọn in/out và đối chiếu continuity, chưa tự gọi toàn cảnh PASS |
| Đào bắt gặp trước khi Khoai ăn | Các bộ 160–164 đều chưa đạt trọn diễn; 163 V02-03 giữ thấp tốt hơn nhưng thêm cử chỉ/mở miệng | Chưa có reaction shot đạt; đoạn giữ thấp chỉ là ứng viên cắt, chưa chọn timecode |
| Khoai chữa cháy, chuyển nem vào bát Đào | Kịch bản 32; 153/154 có ba câu cuối | Chưa có động tác chuyển/nhận đạt; audio ba câu cuối có file nhưng chưa nghe nghiệm thu |
| Kết, Khoai gắp miếng khác, chữ fact/AI | Chưa khóa coverage cuối | Cần xác định có thể dựng từ tài nguyên hay sinh thêm; không bỏ nhịp kết ngầm |

File C01: `C:/Users/PC/Downloads/du_an_nem_bui/159_closeup_pickup/C01.mp4`.
File voice-pair thử có thật: `C:/Users/PC/Downloads/du_an_nem_bui/154_visual_lock/R01.mp4`, R02/R03 cùng folder. Audio tách/QC đã có tại `D:/Workspace/agentic_cinema/artifacts/voice-qc/154-R01` tới 154-R03. ASR đủ ba câu cuối nhưng ghi “gấp” thay “gắp”; đây là nghi vấn phải nghe, không sửa transcript rồi tự nhận đạt. Mẫu giữ nem thấp: `C:/Users/PC/Downloads/du_an_nem_bui/163_low-hold-reaction/V02-03.mp4`.

Không tính tám giây file bằng tám giây có thể dùng. Không coi clip fail toàn cảnh là approved; nếu chọn một đoạn phải kiểm lại đoạn đó, cả khung đầu/cuối và nhịp nối.

## 3. Thời lượng làm việc — chưa đo giọng

Chín câu thoại chính thức có 57 đơn vị cách nhau bằng khoảng trắng (gần âm tiết tiếng Việt, không phải 57 từ ngôn ngữ học). Nếu đọc 3–3,5 đơn vị/giây thì riêng lời khoảng 16,3–19 giây; khoảng nghỉ, biểu cảm và hành động phải được đo bằng bản nghe thật, không tăng tốc chỉ để vừa 30 giây.

| Khối | Nội dung | Đơn vị thoại | Timeline nháp |
| --- | --- | ---: | --- |
| A | Hai câu đầu | 16 | 0–7s |
| B | “Nem thì đây…” và “Bếp nhà anh…” | 17 | 7–14s |
| C | “Chờ ăn?” / “Chờ mẹ quay lưng.” + quay đi/gắp | 6 | 14–20s |
| D | Bắt gặp / chữa cháy / nhận vào bát / kết | 18 | 20–30s |

Đây là phân bổ animatic, không phải timing đã nghiệm thu. Nhịp D tương đối chật: ba câu đã chiếm xấp xỉ 5–6s chưa kể nghỉ, còn khoảng 4–5s cho nhận món/kết. Chữ fact và nhãn AI chồng lên khung có khoảng trống, không kéo dài video mặc định.

## 4. Dự toán có điều kiện

Tách hình và âm thanh là phương án cần owner duyệt trước khi production. Route voice-pair Omni có đầu ra video với audio; dùng riêng audio chỉ sau nghiệm thu nghe. Hình thoại thấy rõ miệng vẫn cần đồng bộ tiếng–miệng; không ghép tiếng lên miệng sai rồi coi hoàn thành. Không giả định đã có TTS miễn phí, preview xuất được file, hoặc Lite giữ được custom presets.

Giả định tối thiểu cho bảng dưới: dựng/đo giọng cho phép chia audio thành 3 hoặc 4 nhóm 8s; cần 2 nhóm hình mới là phản ứng và chuyển/nhận, còn mở đầu/nhớ lại/giữ/kết tìm được coverage hợp lệ. Nếu không tìm được thì cộng thêm ít nhất một nhóm hình 30. Mỗi nhóm hình thử x3 Lite; mỗi nhóm audio thử x3 Omni theo quote lịch sử, cần trình rõ khác route. Không bảo đảm một bộ ba có mẫu đạt.

| Kịch bản dự toán | Audio mới | Hình mới | Tổng | So với trần 134 nếu được điều chuyển |
| --- | ---: | ---: | ---: | --- |
| Thuận lợi: 3 nhóm audio, 2 nhóm hình | 3 × 18 = 54 | 2 × 30 = 60 | 114 | Còn 20, chưa đủ dự phòng một bộ hình x3 |
| Cần 4 nhóm audio, 2 nhóm hình | 4 × 18 = 72 | 60 | 132 | Còn 2, gần như không có dự phòng |
| Cần 3 nhóm audio, 3 nhóm hình | 54 | 90 | 144 | Thiếu 10 |
| Cần 4 nhóm audio, 3 nhóm hình | 72 | 90 | 162 | Thiếu 28 |

Nếu ba câu cuối trong file 154 được nghiệm thu và tái sử dụng, trừ 18 khỏi từng tổng tương ứng: 96 / 114 / 126 / 144. Không ghi giảm này vào ngân sách chắc chắn trước khi nghe. Nếu thêm một nhóm hình mở/kết nữa, cộng 30. Chi phí chạy lại vì mẫu không đạt chưa nằm trong các tổng; đây là coverage estimate, không là báo giá bảo đảm hoàn thành. Không tính phí credit cho thao tác local lập manifest, chọn đoạn, animatic, dựng, chữ, cân tiếng và xuất file; vẫn cần thời gian làm và kiểm.

## 5. Phương án thực thi khuyến nghị

1. Chưa chạy bộ phản ứng 30 ngay: sẽ chỉ còn 4 trial mà voice và chuyển món vẫn thiếu.
2. Lập manifest timecode, nghe ba câu cuối và dựng animatic 30s bằng nguồn sẵn có. Phân biệt video / still placeholder / audio chưa duyệt rõ ràng. Xác minh chuyển từ C01 sang wide, và shot nhận/kết cần gì. Không coi animatic là bản bàn giao.
3. Khóa nhịp thoại trước để biết cần 3 hay 4 nhóm audio. Chỉ sau đó chốt số nhóm hình; hình mới tập trung một nhiệm vụ mỗi shot, không cố gộp toàn chuỗi động tác.
4. Trình owner một trong các tổng 96–162 (hoặc cập nhật nếu thêm coverage), kèm giá UI actual và khoảng dự phòng. Đề nghị điều chuyển 100 Quality, không tự thực hiện từ yêu cầu tính toán. Mục tiêu bàn giao Lite nếu đạt, không bắt buộc upscale/Quality.
5. Mỗi bộ có kiểm nhận file, nghe/xem và gate nối cảnh. Nếu một bộ không có mẫu đạt, cập nhật forecast ngay; không tự tiêu hết reserve để retry cùng lỗi. Muốn vượt trần phải xin thêm quyền.

## Tổng hợp vòng

- Đã xác định: chỉ trial 34 không đủ dự toán coverage hoàn thiện; tổng nhỏ nhất có điều kiện là 96 nếu audio cuối tái dùng và còn hai nhóm hình, không phải đã có thể hoàn thành với 96.
- Đã chốt: lượt này chỉ tính toán, không generation, không Quality/reallocation, không đổi chín câu hoặc cặp giọng.
- Giả định: có thể tìm coverage mở/giữ/kết và tách audio hợp lệ; chưa kiểm chứng; giá lịch sử cần xác nhận lại.
- Còn mở: nghe audio cuối, in/out có thể dùng, nhịp đủ 30s, số shot mới, lip-sync, giá hiện tại và quyền chuyển 100 Quality.
- Bước tiếp: manifest và animatic không tiêu credit, rồi trình dự toán hẹp hơn; quyết định cần owner là điều chuyển ngân sách, không chọn thêm giọng hoặc viết lại câu chuyện.
