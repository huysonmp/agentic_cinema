# Route C — Flow UI probe và phương án ghép EP01

Ngày: 2026-09-30. Status: ROUTE_C_SELECTED / UI_READ_PROBE_COMPLETED / GENERATION_AND_EDITING_NOT_TESTED.

## Authority và hoạt động thực

Owner chọn “C, chạy theo c xem; à mà ghép video kiểu gì ấy”, sau đó chỉ URL `https://flow.google.com/`, yêu cầu vào trang đó. Ghi nhận chọn khảo sát UI-assisted Flow thay vì API. Không coi đây là request generate đúng model/prompt/ref/count/cap đã duyệt; chưa bấm tạo, upload hay tiêu credit.

Đã dùng browser computer-use mở đúng URL trong Chrome, mở một project hiện có, xem agent settings, mở/đóng menu model, quay về ô tác nhân. Không tạo/đổi tên/xóa project, không điền prompt, không thay cài đặt/nhấn Lưu. Không lấy cookie/token/browser network, không đăng nhập thủ công hoặc bypass security. Không lưu email/identity tài khoản vào hồ sơ.

## Evidence UI quan sát trực tiếp

| Hạng mục | Quan sát | Điều chưa chứng minh |
|---|---|---|
| Truy cập | Trang và project có session đăng nhập; control đọc/click được | Không phải guarantee mọi lần session còn sống |
| Nội dung project mở | Hiện thông báo bắt đầu tạo/thả media, chưa có clip để thử ghép trong lượt này | Không kết luận mọi project owner không có media |
| Xác nhận trước khi tạo | Radio “Luôn luôn” đang chọn; “Không bao giờ” không chọn | Chưa kiểm dialog approval sau một request thật; giữ nguyên bảo vệ |
| Default image | 16:9, x2 | Chưa phù hợp test dọc x1; chưa thay/save |
| Default video | 16:9, x1 | Chưa đổi 9:16, duration/cost chưa kiểm |
| Menu model video | Omni 1.1 Flash; Veo 3.1 Lite/Fast/Quality | Menu presence không chứng minh selected model, tất cả feature/quota khả dụng |
| Menu model image | Nano Banana Pro; Nano Banana 2; Nano Banana 2 Lite | Chưa xác nhận model đang chọn/quality/cost |
| Navigation | Nhân vật, Cảnh, Công cụ và session panel | Chưa thử character/audio/import/Scenebuilder operations |

UI route có cơ sở để triển khai thử có kiểm soát, không public API integration và chưa end-to-end test. Generation cost/count, download, output fidelity, credit balance và điều kiện automation vẫn chưa kiểm. Chọn C không bỏ P5/P6/P7/P8 gates.

## Ghép video: hai đường, chưa chọn tool cuối

### 1. Rough assembly trong Flow

Theo [Flow editing/Scenebuilder help](https://support.google.com/flow/answer/16935718), Scenebuilder cho sắp clip, đổi thứ tự, trim đầu/cuối, preview sequence và download scene. Đây là capability theo docs, chưa thử trên project/account vì chưa có clip. Không hứa Flow làm mọi hậu kỳ hoặc editing không tốn credit; tạo/extend/edit AI request cần kiểm riêng.

Sau khi có take được owner chọn, thử Scenebuilder để dựng thô. Giữ raw độc lập và log clip/version/trim. Agent không tự generate nối cảnh chỉ vì thấy cut chưa đẹp; báo lỗi và trình pickup/request nếu cần.

### 2. Finishing/timeline bên ngoài

Đề xuất tách picture edit, audio và text ra timeline rõ để kiểm đồng bộ và chữ tiếng Việt. Có thể dùng editor owner đang có; chưa biết ứng dụng nên không chọn/cài giả định. Nếu muốn auto local có thể nghiên cứu FFmpeg: [concat filter](https://ffmpeg.org/ffmpeg-filters.html#concat), [subtitle filter](https://ffmpeg.org/ffmpeg-filters.html#subtitles-1). Filter concat yêu cầu tương thích stream/format/timestamps; cần normalize và kiểm audio chứ không nối mù.

Read-only `Get-Command ffmpeg,ffprobe` không trả command trong PATH ở lượt này; không khẳng định máy hoàn toàn chưa cài. Không tải/cài phần mềm. Chưa có assembly executor hoặc render output; draft EDL/JSON chưa là timeline thực dựng.

## Edit intent EP01 — proposal, không shot lock

Không yêu cầu 30 giây liền hoặc mỗi câu một clip. Chọn độ chia theo câu chuyện/coverage và mode thực hỗ trợ, sau P7/P8:

1. **Hiện tại → ký ức:** thấy Nem Bùi và hai người; Khoai bị tưởng kén rồi kể mẹ rang gạo. Món/nơi/thính có cue rõ; chưa chốt placement chữ.
2. **Cơ hội ăn vụng → bắt gặp:** Đào quay đi lấy cốc; người xem thấy Khoai lấy nem và định đưa về miệng; Đào quay lại.
3. **Chữa cháy → biết mà không vạch mặt:** Khoai đổi hướng trước contact, gắp vào bát Đào; cô nhận và đáp câu approved. Giữ reaction cần đọc subtext.

Ba nhóm beat không phải cam kết ba native clips, không chia thời lượng giả từ count từ. Nếu cut làm mất ý định ăn ban đầu, payoff không đạt dù clip đẹp. Nếu cần thêm shot thì sửa coverage/request và owner approve, không sửa thoại/kết đã duyệt ngầm.

Đối chiếu continuity: vị trí bàn/nhân vật, tay cầm đũa, miếng nem chưa cắn, vị trí bát/cốc, outfit, góc nhìn, ánh sáng. Audio: không đứt câu/trùng lời/đổi giọng/nhạc nền nhảy; thoại khi miệng không nhai; room tone/pause có chủ đích. Caption/F01/F02/AI label dựng riêng để đọc được, không trông chờ chữ sinh trong video chính xác.

P10 chọn và assemble → P11 hậu kỳ tiếng/chữ → P12 master QC → P13 owner nghiệm thu. Chưa tự mở bốn downstream roles mới vì approval trước chỉ chuẩn bị bảy role đầu; hiện mới nêu trách nhiệm/đầu ra cần có.

## Tiếp theo

- Chốt input/permission plan cho thử UI generation: exact request, model/9:16/x1 nếu owner chọn, refs approved/rights, cost/count cap thực và điểm dừng. Không đổi global confirmation sang “Không bao giờ”.
- Cần project pilot riêng trước khi generate để tránh trộn vào project cũ; việc tạo project/setting mới phải được giao rõ, chưa thực hiện lượt này.
- P5 review gaps và P6 ref/voice chưa hoàn tất; UI read probe không tự cho phép generate episode. Có thể chuẩn bị test manifest giấy và kiểm thao tác tiếp theo theo quyền phù hợp.
- Tool ghép cuối còn mở: thử Flow rough scene trước nếu đủ UI/media; editor local hoặc FFmpeg cho finishing nếu owner chọn và đủ công cụ. Không tự cài hoặc báo đã render.
