# MASTER01 v5 — Kiểm ảnh ChatGPT trước trình owner

Ngày07/10/2026. Root tích hợp/maker, không reviewer độc lập. Phạm vi: xem toàn nativePNG, đối chiếu nativev2, tính SHA256, verifyPNG và kích thước bằngPillow. Không audio/video/khẩu hình/chuyển động.

Target: `02_refs/MASTER01_v5_CHATGPT_NATIVE.png`, SHA256ab31c41ec168aea7fff2206d1536c9ff61c763c3da175defe7cc4bd14649bf96,941×1672. Bản ownercopy có hash trùng.

## Expected và observed

| Kiểm | Quan sát thực | Kết luận trong scope |
| --- | --- | --- |
| Rau/cốc không bị cắt |Toàn đĩa rau và các lá nằm trong ảnh; cốc đầy đủ với khoảng trống tới mép phải. Không còn crop của v2/v3/v4 |Đóng lỗi crop tĩnh trong phạm vi root; margin còn hẹp hơn ý định8–10% |
| Hai mặt/nhận diện |Khoai trái, Đào phải, khuôn mặt/mắt/miệng đọc rõ; giữ dấu hiệu potato/peach và trang phục. Tái dựng có thay đổi nhỏ biểu cảm/chi tiết mặt |Candidate cho owner đánh giá fidelity, không hứa identitypixel-exact |
| F0 và serving |Bốn tay nghỉ, không cầm đũa; hai bát trống, hai đôi đũa nằm bàn, đĩa nem giữa, rau trước trái, hai chấm đúng vùng trái/front-right, cốc ngoài phải Đào |Phù hợp state tĩnh và geography tương đối, chưa motionPASS |
| Món |Thịt/bì dạng lát không đều, thính phủ; không thấy khói/hơi nóng |Không thấy regression rõ như lỗi noodlesv1; không là nghiên cứu món mới độc lập |
| Khung/ánh sáng |Hai nhân vật và serving trọn hơn, ánh sáng ấm/mắt rõ; nền phố đã tái dựng và còn chiếm nhiều phía trên |Master geography candidate, không ép mọi shotC02 giữ framing này |
| Ratio |941×1672, exact9:16=false; chênh khoảng0,053% |Ghi đúng native; không kéo giãn/crop hoặc báo720×1280. Video vẫn kiểm format riêng |

**Disposition:** ROOT_STATIC_REVIEW_COMPLETE / PRESENT_CANDIDATE_WITH_LIMITS. Không tuyên bố toàn bộ yêu cầu numericmargin đã đạt. Không tự duyệt thay owner hoặc independentreview, không gán báo cáo v2 sang v5.

Nguồn sinh: built-in imagegen, một lượt sửa từ đúngv2 đã xem. Không CLI/key/install, không Flow request mới trong241. Originaltooloutput giữ nguyên và copy riêng vào repo/ownerfolder. Prompt nguyên văn lưu tại `02_refs/MASTER01_chatgpt_frame_v5.txt`.

## Cổng còn mở

Owner quyết định đúngv5: mặt/biểu cảm, món/bố cục và minorlimits. Sau acceptance mới cập nhật manifest/ảnhFlow/binding/promptC02 và review phần ảnh hưởng; toolassembly/fullinputquote vẫn chưa đóng. Không production tiếng/lipsync/motionPASS từ ảnh này. Các giọng approved239 và thoại178 không đổi.
