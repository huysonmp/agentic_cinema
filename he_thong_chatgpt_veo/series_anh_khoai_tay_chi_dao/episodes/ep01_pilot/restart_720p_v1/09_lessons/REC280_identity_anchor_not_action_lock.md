# REC280 — Neo nhận diện không thay khóa trạng thái và hành động

Ngày 13-10-2026. Exact native C07 T03 SHA `ae876978fb19265601e4082c5e4cb7079c481786b11a2f8309be362b0881a50e`; root xem toàn 144 frame, không AV/listening. Hai agent actual chưa hoàn tất vì giới hạn sử dụng.

T03 không còn Đào người thật và không mất bát Khoai, nhưng tay/A reset tại F0, miếng tới miệng Đào khoảng F16–33, Khoai mở miệng khoảng F6–37, cốc hạ và bát kéo quá xa. Không chuyển partial improvement thành whole-shot PASS. Không chứng minh ảnh pair là biến gây cải thiện vì prompt cũng thay đổi; không suy camera/voice/semantic model cause từ ảnh output.

Lịch sử đúng job có hai ảnh đúng ID và một voice chip; prompt cuối khớp. Tải native 720p thành công, hash ba bản khớp, giải mã đầy đủ. Lỗi ở nguồn sinh trước cut/encode, không đổ cho cách tải/ghép hoặc sự cố chip đã khắc phục trước submit.

Quy tắc vận hành: đóng các scope identity → inherited state → hành động/props → thoại/diễn → điểm nối riêng; scope tốt không bù MAJOR scope khác. Prompt dài/negative cues và giấy preflight không phải bằng chứng điều khiển động tác. Mỗi thay cơ chế phải có giả thuyết, điểm đầu/đích quan sát được, dependency voice/khẩu hình/timing và quyền riêng; không retry nguyên trạng vì còn credit.

Khi agent failed, registry ghi FAILED và gate còn HOLD, không tạo báo cáo PASS giả hoặc gọi root review là độc lập. Có thể bác lỗi rõ bằng root evidence, nhưng chọn nguồn đạt vẫn cần đủ các gate theo contract.
