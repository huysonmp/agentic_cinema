# REC254 — Phục hồi cục bộ không đồng nghĩa sinh lại toàn clip

Case: chữ burn-in trên áo, source720p/24fps/4s. Hai lượt sinh thoại và một Flow video-edit chưa cho hình sạch. Owner duyệt thử local; sửa đúng vùng chữ từ áo sạch F22/F58 cho ra candidate không còn chữ qua kiểm đủ96 frame của root và reviewer độc lập. Chi0, không thay tool hoặc voice. Chưa owner AV approve tại lúc ghi.

Điều học được:

- Phải phân loại lỗi cuối chặng: chữ thuộc hình native; dựng/caption track không là nguồn. Không tiếp tục sửa lời/voice hoặc chỉ tăng câu cấm chữ. Phục hồi cục bộ là nhiệm vụ khác với regenerate toàn performance.
- Khung áo nhìn gần giống không có nghĩa đứng yên. Phạm vi dò nhỏ chạm biên; đo lại được dịch dọc24px. Dừng căn chỉnh khi chạm giới hạn thay vì xuất bản vá lệch. Hai lượt analysis giữ evidence và không tạo clip/chi credit.
- Dùng vùng áo sạch gần thời gian, căn chuyển động, chỉ thay vùng chữ và feather; giữ các vùng còn lại trước encode. Vải đã bị che vẫn là phục hồi xấp xỉ; blend có thể làm mềm/nảy viền hoặc texture shimmer. Đủ frame kiểm chữ nhưng vẫn cần playback để xét chuyển động.
- Copy stream audio có thể kiểm bằng packet hash/timing và PCM decoded. REC254 cả hai bằng tuyệt đối nguồn; khác với video-edit253 chỉ tương quan cao. Điều này không biến nguồn chưa nghe thành giọng/lời/sync được duyệt.
- Tách nguyên vẹn pixel compositor khỏi MP4 mã hóa lại: ngoài patch pre-encode bằng tuyệt đối, encoded RGB có thể đổi do nén/chuyển màu. Không nói “mọi pixel/mọi chất lượng giữ y nguyên”.
- Đây không phải cách sửa chung cho camera động, chữ che mặt/miệng/tay, thiếu áo sạch hoặc chuyển động phức tạp. Giữ source, output/hash/range, 96frame comparison và owner checkpoint; không coi thành mẹo crop/freeze hoặc che lỗi.

Nơi lưu: `254_LOCAL_SHIRT_REPAIR/compositor_v2/repair_manifest.json`, `encoded_qc/`, `encoded_comparison/`; versioned scripts/approval/reports/registry254 trong repo. Không cập nhật memory cá nhân, không mở budget hoặc BR từ kết quả local.
