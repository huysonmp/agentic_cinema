# REC298 — C06 giữ A đã chạy, tải gốc và kiểm toàn khung

13-10-2026. Owner duyệt **một C06 tối đa 7 credit, không tự chạy lại**. [Approval](restart_720p_v1/00_decisions/C06-KEEP-A-one-run-approval-298.json), [run log](restart_720p_v1/04_requests/C06_KEEP_A_T01_run_298.json). **NATIVE ĐÃ NHẬN / CHƯA CHỌN SOURCE HOẶC RANGE / CHỜ KIỂM NGHE–DIỄN VÀ XỬ LÝ ENTRY.**

## 1. Đúng một lượt và đúng output

Prompt v0.3 đã rehash khớp trước chạy; gói Ingredients/Omni 1.1 Flash/720p/9:16/4s/x1, quote 7 giữ nguyên. Có một ảnh entry v3 và một saved K20 được chuẩn ở REC297, không ảnh P1/P2 hoặc D06. Agent tắt. Không chỉnh preset hoặc tạo preview giọng.

Kết nối IAB 5 mất **trước khi đọc lại prompt trong cell submit**, nên cell đó chưa tới nút tạo. Đọc troubleshooting, xác định IAB cũ không còn trong inventory và IAB 7 cùng session có đúng tab/project; bind lại, đọc gói/quote và chỉ click submit một lần. Không chuyển sang Chrome, cài tool, tìm token hoặc dùng API ẩn. Job mới xuất hiện, composer trống; không gửi lại.

Mở card mới trên cùng, đối soát nhật ký có prompt giữ A (không redirect) và asset mới `781594e4-b7eb-428c-8771-d7823bb2d727`. Tải **720p kích thước gốc** qua listener trước click; Flow báo tải thành công, file MP4 thực đã nhận. Không tải nhầm card trùng tên hoặc upscale.

Native owner: `C:/Users/PC/Downloads/du_an_nem_bui/298_C06_KEEP_A_T01/C06_KEEP_A_T01_NATIVE_720p_298.mp4`.

- SHA256: `0174cf58e30699f59e74c1cef1157dd560999802afa751cead5ee41b462ec639`; 685.289 bytes. Bản tải gốc, bản owner và repo cùng hash.
- H264 720×1280, 24 fps, **96 khung**, video 4 giây; AAC stereo 48 kHz, 4,010 giây.
- Giải mã toàn file thành công, native không đổi. Native/audio/all frames giữ trong folder owner; không ghi metadata thành AV PASS.

## 2. Kiểm ảnh thật đủ 96 khung, không chỉ thumbnail

Helper đã đọc trước chạy: `scripts/inspect_ep01_native_243.py`; tạo toàn frame/timestamp, audio WAV, overview và mouth–hands samples. Bổ sung sáu board mỗi board 16 khung **F0–95 đầy đủ, không padding**, theo hàng; ffmpeg tile có nhãn F trước khi ghép. Cảnh báo fontconfig không làm lệnh lỗi; root đã thấy nhãn đúng F0–95, không gọi đó là cảnh báo native.

Root xem cả sáu board và full-frame F0/F12/F18/F40/F95, so entry v3 đã xem. Findings:

| Scope | Quan sát thực | Trạng thái |
| --- | --- | --- |
| A/đũa | Cùng phần nhỏ vẫn ở tips phía Khoai, không thấy pickup, ăn, handover, thả hoặc chạm đĩa chung trong 96 khung | Đạt mục tiêu **giữ A theo kiểm toàn frame**, không chứng minh bảo toàn pixel/khối lượng tuyệt đối |
| Tay/bát/cốc | Tay trong Khoai nghỉ; Đào giữ cốc tay ngoài, bát cô rỗng trên bàn, không cốc trong bát/đổi tay/nhân bát. Không thấy tay phụ chỉ trỏ như REC293 | Không thấy blocker mới ở props qua ảnh; chưa physical-path PASS nhịp nhận chưa sinh |
| Mặt người nói/nghe | Khoai có chuyển động miệng khoảng F11–42, Đào môi khép. Hai mặt và vùng tay luôn thấy | Đúng phân vai **quan sát hình**, chưa nghe hoặc chứng nhận lip-sync |
| Entry gaze | F0–10 mắt Khoai hướng trước/xuống thay chú ý Đào ở v3; khoảng F12–17 chớp/nhắm khi miệng mở; F18 trở đi hướng Đào | Entry chưa kế thừa đúng, **chưa đóng continuity**. Không tự cắt F0–17 vì có thể mất đầu lời |
| Diễn B | Miệng mở/răng thấy khi nói, mắt chuyển Đào rồi nét nhẹ cuối. Không đủ từ still để quyết định là phát âm tự nhiên hay nụ cười mời/tease lệch B | Chờ playback nghệ thuật trên đúng native, không bác hoặc PASS chỉ vì một miệng mở |
| Đuôi | Khoảng F43–95 phần lớn giữ trạng thái/ánh nhìn với chớp mắt Đào ở F58–61 | Có đuôi cần đo/cắt sau duyệt range; không bắt dùng trọn4s và chưa chọn range |
| Món/trang phục/bàn | Không thấy khói, nem dạng rời phủ thính; áo trắng/váy xanh, vest tối, rau/hai chấm/hai bát giữ | Không thấy fail mới rõ qua ảnh; không tự đóng món các cảnh trước hoặc exact identity/pixel preservation |

Giữ A đạt trong take này là kết quả quan sát, **không chứng minh choreography mới chắc sửa mọi lỗi**, hoặc kết luận nguyên nhân backend đã cô lập. Entry gaze vẫn lệch dù prompt yêu cầu hướng Đào, đúng giới hạn Ingredients không khóa F0 đã nêu.

## 3. Tiếng và giới hạn kiểm

Offline ASR không mồi lời cho ra **“Anh gấp cho em mà.”**, khoảng 0,46–1,60 giây. Đây là transcript máy, **không kết luận voice nói sai từ “gắp”**, cũng không xác nhận K20/miền Bắc/đủ âm cuối/diễn/khẩu hình. Audio hiện hữu không bằng audio đúng.

Root chưa có bằng chứng actual listening hoặc continuous AV; không ghi đã nghe từ việc phát nút hay xuất WAV. Phần này cần owner nghe/xem native được gửi trong chat. Giữ approval preset K20 cho scope preset, không chuyển sang take mới. Không mute, revoice hoặc ghép giọng đè mặt.

## 4. Ngân sách đã đối soát thực

Account **986 → 979**, giảm **7**; đã lưu BALANCE_AFTER. Sổ project **251/500**, còn **249**; phần tạo lại **12**; dự phòng **110 đóng**. Quyền đúng một lượt đã dùng; không tự retry kể cả khi còn nhiều credit tài khoản/project. Không giữ số 244/256/19 làm hiện hành hoặc dùng chi dự kiến thay debit.

## 5. Kiểm độc lập và điểm quyết định tiếp

[Reviewer độc lập](restart_720p_v1/06_qc/C06_KEEP_A_actual_independent_298.md) đã kiểm toàn96 qua sáu boards và sáu full-resolution frames F0/F10/F13/F18/F42/F95, đối soát hash native/base; root đọc hết report. Xác nhận giữ A/props qua ảnh, không blocker action rõ như thả sai đích REC293; vẫn **HOLD_SELECTION** vì entry gaze có finding thật và chưa nghe/continuous AV/diễn hoặc seam. Không tên vị trí thành PASS. Native hiện **chưa chọn** và range chưa có; không đổi source/EDL hoặc chạy nhịp nhận.

Điểm cần owner xem là **đúng một Khoai/K20, đủ N06 và nét B có chấp nhận được không**, cùng ngoại lệ gaze đầu. Không xin duyệt toàn phim. Cần quyết định entry sau actual review: chấp nhận ngoại lệ nhỏ về gaze hay giữ rework; không giả cắt đầu là chắc chữa được vì ASR lời đã bắt đầu trước F18. Dùng đoạn speech riêng không xóa lỗi điểm nối.

Timing còn mở: 632F trước C06, C06 mới range N thì final30 còn88−N cho N07/nhận/cho/C09. Chưa ép N57, cắt mất từ, bỏ C09 hoặc tự nới mục tiêu. P1/P2 là approved direction, input nhận phải theo khung ra thực của source được chọn và giữ khoảng hở bát–tay, không nhảy sang ảnh nháp.

**Đã xác định:** native tải/giải mã đúng, A còn kẹp và props giữ qua toàn ảnh; entry gaze lệch. **Quyết định đã chốt:** chạy một7/no retry; chưa nghiệm thu output. **Giả định:** có thể chọn range ngắn sau heard/acting review, chưa đo và không chữa gaze bằng giả định. **Còn mở:** owner nghe/diễn, disposition gaze, range/nối/timing/món toàn tập. **Bước tiếp:** hoàn tất phản biện và trình đúng output/phạm vi để owner chốt, không trả phí thêm.
