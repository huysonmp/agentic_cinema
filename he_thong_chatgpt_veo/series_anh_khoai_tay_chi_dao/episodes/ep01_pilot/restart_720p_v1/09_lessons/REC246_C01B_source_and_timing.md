# REC246 — Ảnh nguồn đúng chưa bảo đảm đầu video và thời lượng dựng

Scope: C01B T01 duy nhất, native hash f7321e72c952cf849f9b5febede7fb08951c997970de82e6f8d424f54415089b. Chưa final PASS hoặc nguyên nhân model đã chứng minh.

- Ảnh đầu là nguyên frame80 của export C01A được chọn. Upload cloud ID và readback đúng, nhưng root thấy hình tay trong/món ở actualframe0 khác nguồn. Ingredients không phải khóa START tuyệt đối. Kiểm hai phía cut bằng nativeframes, không chỉ kiểm ảnh upload.
- Mẫu Khoai mở miệng trước, Đào nhìn anh rồi release/retract tới khoảng3s. Native4s chỉ là khoảng sinh; opening dự kiến4,5s với C01A3,375s chưa chứng minh đủ. Đo range nhiệm vụ rồi tính lại toàn30s; không tua nhanh hoặc cắt mất phản ứng để giữ mốc giấy.
- Unprompted ASR ghi “Khuán!” cho một từ ngắn. Đây là tín hiệu cần nghe, không chứng minh giọng/lời sai và không lý do tự retake. Owner nghe exact PCM; không chuyển approval K20 của C02 sang B.
- Tải Original qua UI thành công lần đầu, file hash/decode đầy đủ. Giữ original, mọi cut là artifact mới phải probe/hash/kiểm lại.

Còn mở: reviewer actual, owner nghe đúng tiếng, hai điểm nối và timing toàn phim. Không mở chuỗi phụ thuộc từ một endpoint đẹp khi path/source chưa được đóng.
