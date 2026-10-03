# 166 — Bản nháp 30s và kiểm coverage thực tế

Ngày 2026-10-03. Owner “ok vậy làm đi nhé” cho bước không tiêu credit sau 165. Đã dựng nháp local bằng FFmpeg đã có, không dùng Flow/Canva/API, không tạo ảnh/giọng mới hoặc điều chuyển Quality. Không dựng tác phẩm hoàn thiện rồi tự ghi approved.

## Đầu ra và giới hạn

Folder: `C:/Users/PC/Downloads/du_an_nem_bui/166_completion_animatic/`.

- `EP01_30s_PLANNING_v0.1.mp4`: 30,000s, 720x1280, H264/24fps, AAC; giải mã toàn file không lỗi.
- `manifest.json`: chín shot, timeline/source in-out, hash đầu vào, lời thoại, metadata output; `animatic-contact.png` cho kiểm bố cục.
- `closing_voice_R01_UNAPPROVED.wav`, R02/R03 tương ứng: audio native tách lossless PCM từ ba file 154, không đổi tốc độ/giọng, không nhận là TTS mới. File không bị cắt câu; mỗi bản 8s.
- `C01-selected-dense.png`: kiểm đoạn gắp 2,75–5,25s ở 6fps; không lặp hoặc tua nhanh động tác.
- Script tái dựng: `D:/Workspace/agentic_cinema/scripts/build_ep01_budget_animatic.py`; fail nếu ghi đè media có sẵn, không overwrite nguồn.

Header bản nháp và nhãn ảnh tạm/thiếu cảnh hiển thị từng shot. Chỉ C01 là video chuyển động; 27,5s còn lại là ảnh tạm, không chứng minh đã đủ video. 0–22s không có giọng; chín câu giữ nguyên ở caption để tham khảo thời lượng. 22–30s dùng audio R01 bộ 154 cho owner nghe, chưa nghiệm thu voice/miền Bắc/phát âm. Không đồng bộ miệng với ảnh tĩnh, không gọi lip-sync đạt. Không thêm nhạc hoặc ambience; không có F01/F02/nhãn AI final hoặc gate release, vì đây là nội bộ, không đăng.

## Timeline được xuất thực tế

| Shot | Timeline | Actual source / in-out | Thiếu hoặc gate |
| --- | --- | --- | --- |
| S01 | 0–6,5 | OPEN7 tĩnh | Hai câu đầu chưa có audio; chuyển động/động tác kéo đĩa chưa có |
| S02 | 6,5–13,5 | OPEN7 tĩnh | Đối đáp và ký ức chưa có audio hoặc diễn |
| S03 | 13,5–16 | OPEN7 tĩnh | “Chờ ăn?” / “Chờ mẹ quay lưng.” chưa có audio |
| S04 | 16–17,5 | OPEN7 tĩnh | Chưa có Đào quay đi lấy cốc; ảnh tạm còn nhìn Khoai |
| S05 | 17,5–20 | C01, 2,75–5,25 | Có kẹp/nhấc/giữ; owner duyệt riêng cơ học, continuity chưa duyệt |
| S06 | 20–22 | START161 tĩnh | Nem giữ thấp; thiếu nâng về miệng và khựng trước tiếp xúc |
| S07 | 22–24,6 | END163 tĩnh + audio R01 | Cần phản ứng Đào thực; timing tiếng theo ASR chưa nghe duyệt |
| S08 | 24,6–27 | END163 tĩnh + audio R01 | Miếng nem không chuyển/nhận trong actual hình |
| S09 | 27–30 | OPEN7 tĩnh + audio R01 | Reset pose không chứng minh nem vào bát; chưa có Khoai gắp miếng khác |

Nguồn C01 và OPEN7 giữ hai bát/hai đồ chấm/cốc/lá tương tự, nhưng thay góc/crop; START161 và END163 khác framing, sợi/mound và vị trí tay so với OPEN7. Bản nháp làm lộ jump-cut/reset này, không sửa bằng crop để gọi continuity đã đạt. C01-selected grid cho thấy nhấc tuft nhỏ, hai đũa còn rõ, không thấy hơi nóng ở mẫu kiểm; chưa kiểm từng frame.

Không chọn 163 V02-03 vào montage: grid cho thấy cử chỉ/mở miệng/gaze ngoài yêu cầu, dù giữ nem thấp tốt hơn. Chưa tìm được một đoạn phản ứng đủ mục tiêu để giảm nhóm hình. Các bộ 153/154 không chọn hình vì food/identity/lip-sync chưa đạt. Các opening cũ chưa được tái chứng nhận, nên không đưa chúng vào forecast như tài nguyên production đã có.

## Audio cuối — đo được và chưa biết

ASR R01: câu Đào 0–1,90s; câu Khoai 2,62–3,84s; câu Đào 4,74–6,34s. Đặt file tại22s, không speed-up, nên lời kết khoảng28,34s; còn khoảng1,66s cho kết trong slot30s. Hình nhận món cần diễn dưới khoảng nghỉ hoặc khi Đào nói, không đợi hết lời mới làm tất cả. Timestamp là bằng chứng ASR, không nghe xác nhận onset/offset tuyệt đối.

ASR ghi “gấp” thay “gắp” là nghi vấn, không kết luận phát âm sai. Root chưa có bằng chứng nghe xác nhận accent/voice identity/cảm xúc; không ghi agent đã nghe. Owner nghe file tách để quyết định tái dùng. Không đổi preset K20/D06 hoặc tìm giọng mới. Giữ điều kiện tiết kiệm18 credit pending.

## Điều chỉnh dự toán sau kiểm

Phương án114 trong165 giả định tìm được video mở/giữ/kết; lượt này chưa xác nhận giả định đó, nên **không dùng114 làm ngân sách hoàn thành đáng tin cậy**. Khoản trial34 và Quality100 vẫn riêng; số dư lần kiểm cuối334, không đọc UI lại, chi mới0.

- Nếu giữ chuyển động/coverage như kịch bản: ngoài C01, ít nhất ba nhóm hình mới dự kiến là mở/kể chuyện/quay đi; nâng-khựng/phản ứng; chuyển-nhận/kết. Mỗi nhóm chỉ là một cụm coverage, không bảo đảm một clip8s đủ hết nhiệm vụ. 3 × 30 =90; audio 3–4 nhóm ×18 =54–72; tổng **144–162**, trước dự phòng. Nếu phải tách thêm một nhóm hình thì +30. Nếu audio cuối được duyệt tái dùng thì -18, thành126–144. Cần duyệt giá actual, route và ngân sách; không cam kết pass một bộ.
- Nếu owner chấp nhận kết hợp ảnh–video có chủ đích cho đoạn mở/ký ức: có thể bỏ một nhóm hình, còn114–132 (hoặc96–114 nếu audio cuối tái dùng). Đây là thay cách thể hiện so với full-motion kỳ vọng, phải owner duyệt và thiết kế rõ; không bàn giao bản nháp27,5s ảnh tĩnh như phương án này đã đạt.
- Nếu cần một bộ hình dự phòng: +30; đây chỉ là reserve, không bảo đảm đủ khắc phục mọi lỗi.

## Vòng quyết định

- Đã xác định: đã có bản nháp thực30s và nguồn gắp2,5s; còn27,5s ảnh tạm, sáu câu chưa có giọng, ba câu cuối chưa nghiệm thu. Dự toán thấp chưa được kiểm chứng.
- Đã chốt: lượt này0credit, giữ script/voices, không giảm gate hay tự chuyển Quality; đây là artifact review, không master final.
- Giả định: nhóm hình và audio có thể gộp theo khoảng thời gian; chưa có kết quả thử mới chứng minh.
- Còn mở cần owner: nghe audio cuối có được tái dùng không; giữ chuyển động hay duyệt hình thức ảnh–video; quyền điều chuyển Quality và mức trần thực thi sau chọn hình thức.
- Bước tiếp: owner xem nháp/nghe audio, chốt hai điểm ảnh hưởng ngân sách. Sau đó mới khóa shotlist và bảng chi theo từng bộ, kiểm giá UI trước submit; chưa tiếp tục generation từ approval dựng nháp.
