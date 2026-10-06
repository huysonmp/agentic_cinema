# EP01 — chốt tách đưa bát và chuyển–thả nem

Ngày 2026-10-06. Owner trả lời “duyeejt” cho phương án206: giữ U06 đoạn đưa bát0–1,5s; U07 thực hiện chuyển cùng miếng nem rồi thả vào bát Đào, một lượt đã dự trù, không tăng ngân sách. Approval về kế hoạch, không nghiệm thu đầu ra chưa sinh.

## Quyết định và khung thực thi

Giữ C-v0.6, K20/D06, toàn PCM tiếng202 đã duyệt; không sinh lại thoại. [Timeline207-v0.4](evidence/207/timeline-v0.4.json) thay duy nhất ranh giới S08/S09: S08 frame590–626/36frame; S09 frame626–684/58frame. Tổng94frame và video720frame/30s giữ nguyên. Mọi audio placement giữ nguyên205. Chưa render phim30s, không freeze/loop/slowdown.

Root xem36frame đầu U06: bát riêng Khoai giữ giữa bàn; bát Đào đi vào từ phải và vẫn có tại frame35, không lấy đoạn sau mất bát. Miếng nem vẫn giữ; tay Đào thứ hai hiện ở tiền cảnh, không tự xóa khỏi source hoặc giả đã review độc lập. Đoạn entry là ứng viên có điều kiện cho nối, không full-U06/FOOD/ACT PASS. Bản local10,625s/255frame không tiếng nối bản hình205 với36frame entry để kiểm; chưa phim cuối.

START U07: native U06 frame35, hash `eaaad7c27cb7f29d54638bd00f77de59c1c39cd09012ab29f0230901daef175b`,720×1280, [ảnh](evidence/207/U07_START_native_U06_frame35.png). Không dùng endpoint8s mất bát hoặc END189 đổi camera. Chỉ START; Đào giữ bát, Khoai chuyển rồi thả, không nhặt thêm. Prompt chỉ đạo release khoảng1,8s, nhưng phải đo actual để xác nhận fit58frame; chưa giả sẽ tuân mốc.

## Preflight, ngân sách và kiểm đầu ra

Skill computer-use dùng để đọc Flow, kiểm model/mode/source/quote/prompt trước gửi và tải native qua UI. Lite/Frames/dọc9:16/720p/8s/x1, dự toán10; không Quality, voice tokens hoặc END. AAC nếu có không dùng cho tiếng202. Sổ trước:369/422/còn53. Nếu debit10:379/422/còn43; bốn đơn vị U01/U02/U03/U08 forecast40/dự phòng3. Không tự sửa U07 trả phí, không đổi earmark hoặc thêm quyền chi.

Đầu ra cần tải/hash/probe/decode; root kiểm58frame đầu và mẫu toàn8s. Bắt buộc: cùng miếng nem được chuyển và nằm thật trong bát Đào, không rơi nhầm bát/đĩa, không biến mất/sinh thêm, hai bát/tay nhất quán, chuyển động đúng chiều/grip, không ăn/lặp, mặt ngoài khung, nem lạnh không hơi nóng. Nếu đủ, chọn native range/endpoint thật và ráp bản hình có nhãn, không tự báo AV/master PASS. Nếu không đủ, ghi REWORK và phương án trong quyền còn lại, không gửi thêm.

## Thực thi và ứng viên đầu ra

Đã gửi đúng một lượt Lite/Frames/9:16/720p/8s/x1, giá 10 credit; prompt đọc lại khớp tuyệt đối, START đúng file/hash, không END hoặc voice token. Số dư cuối mốc206 là107, sau lượt207 còn97; chi10, **đã chi379/trần422/còn43**. Không chạy thêm lượt hoặc Quality.

Flow tạo `Man drops food into bowl`, ID `daaff548-a029-4a6a-a52e-1bef5bff170f`. Tải native một lần qua menu720p; sự kiện timeout20s nhưng có file thật `Man_drops_food_into_bowl_20261006152052.mp4`. Bản lưu `C:/Users/PC/Downloads/du_an_nem_bui/207_u07_production/U07_NATIVE.mp4`, SHA256 `9792a637316692967383990b0eb174471e4ede21edb37b470ef1d7fe60f0bdad`; H264720×1280/24fps/192frame/8s, AAC48kHz stereo, decode exit0. Không dùng AAC hoặc giả đã tắt sinh âm.

Root kiểm58frame đầu ở contact sheet toàn khung,48 mẫu toàn8s, tất cả58frame đoạn chọn ở crop động tác; thêm frame20/35/44/57/72/77/83 lớn và các điểm nối. **Đã quan sát chuyển phần nem xuống bát Đào; tại77 đũa rỗng nhấc khỏi phần nem nằm trong bát**, bát Khoai vẫn rỗng. Không thấy ăn, nhặt thêm hoặc hơi nóng rõ trong đoạn chọn. Không báo FOOD/ACT toàn tập hoặc agent độc lập PASS.

Release muộn hơn chỉ đạo1,8s. Chọn source frame20–78 exclusive, tức0,833333–3,25s/58frame/2,416667s; bỏ thời gian chờ đầu, không tăng tốc/freeze/loop. Bát Đào nhích lên/trái ở phần đầu clip: **có sai khác vị trí ở cut U06frame35→U07frame20**, chưa continuity PASS. Không gọi toàn8s đạt hoặc tự chấp nhận sai khác thay owner.

Đã xuất ứng viên không tiếng `U07_REDIRECT_RELEASE_f20-f77_SILENT_CANDIDATE.mp4` hash `5ba6c9b63052b7e056a0aa730e0f988e7388e35fbf506eb5d5abebe597167df1`. Ráp hình P02→U04→U05ngắn→U04→U06entry→U07: `EP01_ACTION_THROUGH_DEPOSIT_13.042S_PICTURE_REVIEW_NOT_FINAL.mp4`,313frame/13,041667s, không tiếng, decode sạch, hash `0f6dada0bf51d974b0a009a6851e509405df2fc7da165cd5c17d1094fa985193`. Đây chỉ khối hành động tương ứng timeline15,458333–28,5s, không phim30s/full-AV. Owner cần xem nhịp nối và vị trí bát.

Endpoint kế tiếp chỉ là [native U07frame77](evidence/207/U07_SELECTED_OUT_frame77.png), hash `059e0702483faa581990c7dd1b12ace465a3670f39645df11bfdd9793c957616`, không native cuối8s đã đặt đũa xuống bàn. U08 chưa tạo; khung hiện tại ngoài mặt, nếu đổi sang shot kết có mặt phải chuẩn bị coverage/continuity, không lấy ảnh rộng cũ như đã ăn xong.

## Trạng thái và bước tiếp theo

Đã chốt kế hoạch tách206 theo approval207; đã thử một U07, có ứng viên chuyển–thả và bản xem13,042s. Giả định làm việc: nhịp nối bát dịch nhẹ có thể chấp nhận, **chưa được owner xác nhận**, không ghi thành quyết định. Vấn đề mở: review output/continuity, bốn cảnh U01/U02/U03/U08, ráp toàn30s, hình–tiếng/phụ đề/AI disclosure/mix/master. Giữ tiếng202. Forecast bốn lượt40 từ43; không tự lấy3 dự phòng để sửa10 hoặc bỏ cảnh khác.

Bài học: sau tách bát vào khỏi chuyển–thả, lượt này thực hiện được hành động đích; đây là một quan sát, chưa chứng minh phương pháp luôn hiệu quả hoặc nguyên nhân gốc của206. Chọn range theo release thật và endpoint thật, không coi mốc prompt là timing actual. Tiếp kiểm khung kết và cảnh mở/hồi tưởng, rồi ráp đầy đủ; không sinh thêm U07 để tối ưu tiểu tiết khi không có quyền sửa.

U06 full8s vẫn REWORK theo206, không xóa lịch sử. Chưa agent phản biện độc lập, AV/mix/master hoặc phát hành. Skill computer-use đã ảnh hưởng kiểm preflight/tải một lần/native và [bằng chứng Flow](evidence/207/flow-completed.png) không panel tài khoản.
