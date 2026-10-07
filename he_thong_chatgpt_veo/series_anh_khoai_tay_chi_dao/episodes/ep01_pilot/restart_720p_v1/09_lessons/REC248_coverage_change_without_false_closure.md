# REC248 — Đổi coverage nhưng không che hoặc đóng nhầm lỗi nguồn

Ngày 08/10/2026. Trạng thái: bài học thiết kế từ evidence247; chưa có kết quả video mới248.

- T01/T02 lặp sai pose đầu; bản ghép phản ánh lỗi native. Đổi cách dựng đơn thuần không sửa tầng phát sinh này.
- Owner chọn A mở thiết kế riêng C01B. Tách người nói và người phản ứng là giả thuyết giảm nhiệm vụ đồng thời, không tỷ lệ thành công đã đo.
- DIR/DOP/ACT/EDIT phải có output riêng rồi tích hợp; DOP/EDIT đã cập nhật khi root chọn BR trở về góc bàn gốc. Không giữ yêu cầu visibility của draft cũ như cổng hiện hành.
- Một shot người nói có thể không thấy tay người nghe; ghi vùng đó UNKNOWN. Shot phản ứng sau vẫn phải trực tiếp chứng minh contact→release→return, không cho phép reset ngoài khung.
- Nếu BM đã cho Đào phản ứng rồi BR START dùng A80 mắt thấp/contact, sẽ phát lại trạng thái cũ. Phải kiểm dependency này trước tạo BR, không đợi tới phim cuối.
- Tái dùng hai ảnh exact cùng camera cho BR tránh tạo thêm reference bàn/pose chưa cần. Không suy endpoint đúng thành đường chuyển động hoặc frame-lock đúng.
- Ảnh ChatGPT BM mới được probe 941×1672, không gọi exact9:16/720p. Preset video và native phải kiểm riêng; nguồn và dấu gốc giữ nguyên.
- A/C02 selected đã chiếm10,916667s. B2–3s chỉ giả định, không ép1,125s hoặc lập EDL giả. Chưa có nguồn sau để chứng minh toàn phim30s.
- Tiếng T01 đã duyệt không chuyển sang BM waveform mới. Mặt nói, nghe thực, tiếng và actual joins là các scope khác nhau.
- Lượt248 tạo một preview ảnh bằng công cụ tích hợp; không Flow video, không debit video. Hai đầu ra ≤30 credit mới là trần đề nghị, chưa quote hoặc chi thực.

Vòng kiểm chứng tiếp: live feature/quote → BM actual → dependency/range → BR actual → ba joins → tổng nhịp. Chỉ đóng finding bằng target/evidence mới, không bằng việc đã viết thêm prompt/report.
