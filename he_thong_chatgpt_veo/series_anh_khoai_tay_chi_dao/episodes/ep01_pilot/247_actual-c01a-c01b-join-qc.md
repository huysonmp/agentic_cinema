# 247 — Tiếng C01B đã chấp nhận; kiểm bản ghép thực trên Flow

## Kết luận hiện hành — 08/10/2026

Đã chạy một T02 giá7 trong quyền238, tải native và kiểm độc lập25 mẫu. Root đọc đầy đủ: thu/rest sớm hơn nhưng lỗi lớn start-pose lặpT01. **STOP sinh thêm, không tựT03; C01B chưa được chọn, chưa mởC03A.** Lỗi có ngay ở clip sinh, không do Flow ghép nhầm. Dự án đã dùng74/500, còn426;110 dự phòng chưa giải ngân. Giữ C01A/C02/voices. Owner cần chốt hướng thiết kế lại coverage hay staging ở `restart_720p_v1/00_decisions/C01B-stop-and-coverage-options-247.md`; các đoạn phía dưới giữ lịch sử của bước ghép/preflight trướcT02.

## Quyết định đã chốt

Owner trả lời “ok” cho hai điểm đã hỏi: tiếng Khoai/K20 nói một từ “Khoan” ở đúng C01B T01 chấp nhận được; cho phép bấm “Tôi đồng ý” một lần để nhập lại bản cắt C01A trên Flow. Đã ghi đúng phạm vi vào `restart_720p_v1/00_decisions/C01B-T01-audio-and-C01A-reimport-confirmation-247.json`. Không chọn tùy chọn “không hiện lại”; không coi đây là duyệt hình C01B hay cả phim.

## Đã thực hiện

Đã nhập bản C01A được chọn, tạo scene QC riêng `EP01_QC_C01A-C01B_JOIN_T01 — CHƯA DUYỆT HÌNH`, ghép C01A → C01B T01 đầy đủ, giữ tiếng gốc và khung dọc. Scene C01A/C02 được chọn và native không thay đổi.

Đã tải bản ghép về folder owner tại `C:/Users/PC/Downloads/du_an_nem_bui/ep01_restart_720p_v1/07_edits/C01A_C01B_T01_FLOW_JOIN_QC_247.mp4`, copy vào kho project và kiểm decode sạch. Video dài7,380013 giây,177 khung, bản xuất Flow1280×2274/VFR; không phải native720p hoặc final đúng tuyệt đối9:16. Manifest và source hashes ở `restart_720p_v1/07_edits/C01A_C01B_join_QC_preparation_246.json`.

## Vấn đề còn mở

Đã nhận report độc lập `restart_720p_v1/06_qc/C01A_C01B_actual_join_independent_247.md`:76 khung, root đọc đầy đủ. Kết luận `JOIN_REWORK / SOURCE_C01B_HOLD`; lỗi tay có ngay ở native B và được tái hiện tại điểm nối thực, không có bằng chứng Flow dựng sai clip. Không tìm được offset hợp lệ đã chứng minh giữ toàn lời và nhân quả. Root mở preflight riêng cho targeted T02 trong quyền238, chưa submit. Đây là kết luận mới thay trạng thái “đang kiểm” dưới đây; không thay approval tiếng T01.

Root đã xem các mẫu quanh điểm cắt: tay trong đổi vị trí và món thay hình, rồi có động tác hai tay tiến về vành. Đang kiểm độc lập đúng bản ghép để phân biệt lỗi clip sinh với lỗi dựng; chưa chọn C01B hoặc mở C03A. Xem report độc lập247 khi hoàn tất, không lấy metadata hoặc tiếng đã chấp nhận để đóng lỗi hình.

## Giả thuyết và bước tiếp

T01 có cue “giữ ý định lấy tới khi nghe” và chưa đặc tả rõ tay trong chỉ đi về thân/bát, có thể dẫn tới reach mới. Đây là giả thuyết, chưa causal proof. Draft T02 đã tích hợp đóng góp DOP/ACT: chỉ tiếp nối contact → nghe → buông → thu; giữ lời, giọng, source, camera và toàn bối cảnh. Cần root đọc đầy đủ report actual join và preflight độc lập trước submit; không cứu bằng audio overlay, tăng tốc, cận món hoặc cắt mất nguyên nhân “Khoan”.

## Ngân sách

Lượt ghép/xuất không có paid generation; số dư cùng tài khoản vẫn1.013, observed debit0. Dự án đã dùng67/500, còn433; reserve110 chưa giải ngân. Không suy ghép/xuất miễn phí cho mọi tính năng khác. Kế hoạch và quyền236/238 giữ nguyên.
