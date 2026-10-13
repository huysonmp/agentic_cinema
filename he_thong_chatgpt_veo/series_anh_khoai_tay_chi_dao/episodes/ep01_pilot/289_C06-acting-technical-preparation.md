# REC289 — Chuẩn bị kỹ thuật sửa diễn Khoai

Ngày 13-10-2026. Owner yêu cầu tiếp tục; phạm vi vòng này là **lập phương án kỹ thuật**, không tự ghi là đã duyệt mọi chi tiết brief hoặc lượt trả phí mới. Không browser, video/ảnh mới, sửa source/EDL hoặc tạo giọng.

**Cập nhật sau phản hồi owner:** khi hỏi duyệt brief và chuẩn ảnh đầu, owner chọn **“Cần chỉnh sắc thái diễn Khoai trước”**. Vì vậy phương án dưới đây được lưu làm dự thảo, bước chuẩn ảnh chưa được duyệt/thực hiện. Quay lại chốt sắc thái diễn; không coi yêu cầu “tiếp tục” trước đó là đồng ý với bản chi tiết hiện hành.

## 1. Chọn phạm vi hẹp, không làm lại cả bản nối

**Khuyến nghị:** chuẩn bị một cảnh C06 mới, chỉ Khoai nói N06, từ đúng trạng thái cuối C05. Giữ C05 đã duyệt làm nguồn đối chiếu; không đưa cả hai lượt Đào→Khoai vào một yêu cầu sửa video nối nữa.

Lý do theo kết quả thực: REC275 từng tạo được cảnh một người nói với đúng preset được kiểm trên UI; owner duyệt đoạn 57 khung tại REC276. REC286 sửa cả bản nối tạo được file nhưng thêm yếm, đổi hậu cảnh và điểm chuyển camera ngoài phạm vi. Đây hỗ trợ chọn phạm vi nhỏ hơn, **không chứng minh lần mới chắc đạt**. C06 mới vẫn phải sửa diễn và hình món, không chỉ thêm chữ “preserve”.

C05 có món chưa chuẩn; giữ nguồn không phải nghiệm thu toàn cảnh. Việc chuẩn ảnh đầu C06 chỉ đóng đầu vào của C06, **không tự đóng lỗi hình món trước đó**. Cổng toàn tập tiếp tục mở và phải rà riêng trước bản dựng cuối.

## 2. Đầu vào và vai trò từng tài nguyên

| Tài nguyên | Vai trò hợp lệ | Chưa được dùng để kết luận |
| --- | --- | --- |
| `restart_720p_v1/02_refs/C06_START_from_C05_T02_selected_F65_269.png` | Khung vào kế thừa C05: bố cục, nhận diện, quần áo, tay/đũa/A, hai bát và cốc | Chất liệu nem đúng; ảnh sửa sau tự được duyệt |
| Hai ảnh nem thật owner đã duyệt | Chuẩn chất liệu nem và cách trình bày đúng phạm vi món | Đưa thêm món/props từ ảnh thật vào bàn hiện hành |
| START REC283 | Đối chiếu vật liệu và điểm **ra** C06 | Điểm **vào** C06 |
| END REC283 | Đối chiếu nhịp nhận–bỏ sau C06 | Đích kết thúc C06 hoặc approval chuyển động |
| K20 trong `03_voices/bindings-238.json` | Preset Khoai đã chọn, kiểm lại trên UI trước chạy | Bảo đảm âm thanh/khẩu hình của video mới |
| Native REC286 | Chứng cứ lỗi và bài học bảo toàn vùng ngoài sửa | Canon hoặc nguồn tái sử dụng |

Đã xác minh lại hash khung đầu: `f091e35fc7c779591c918c47ba34752a8a2c3b30de507cd99dc0e76143e83196`. Native C05: `3df61217ddf6d09792fe1e5991c3668d115ce5648c00802f196d87abe57d23df`. Đây là kiểm tệp tồn tại/đúng nguồn, không kiểm hình hoặc diễn lại.

**Việc chuẩn ảnh do tôi làm:** sửa chất liệu món trên đúng khung đầu, không thay mặt, quần áo, bố cục, tay hay cốc/bát. So toàn ảnh và phần A, lưu phiên bản/lineage/hash, trình đúng ảnh cho owner. Không hứa công cụ sửa được pixel chính xác; nếu vùng khác đổi thì không dùng. Chưa thực hiện ở REC289; đang hỏi owner chốt brief và bước ảnh qua câu hỏi trong chat.

## 3. Phương thức đề xuất — chưa phải cấu hình live

Chuẩn bị tuyến **Video Ingredients: ảnh đầu đã sửa + một preset K20**, bản dọc 720p, một đầu ra, âm thanh bật, Agent tắt. Mô hình/thời lượng đề xuất ban đầu theo tuyến từng chạy REC275: Omni 1.1 Flash, 4 giây. **Phải kiểm lại UI live; không coi tên model, availability, giá hoặc ingredient binding lịch sử là hiện hành.**

“Ảnh đầu” ở đây là vai trò nghệ thuật, không chứng minh tuyến Ingredients khóa được khung F0. Phải kiểm mức ràng buộc ảnh UI thực hỗ trợ. Nếu cân nhắc tuyến Frames để khóa đầu, cần kiểm lại khả năng dùng saved voice; không ngầm coi hai khả năng cùng có hoặc đổi tuyến khi gửi.

Giá từng chạy REC275 là 7 credit; đây chỉ là số lịch sử, không báo giá lượt mới. Không dùng quote 20 của REC286 cho tuyến này. Chỉ trình request mới khi UI hiện cấu hình/giá và nguồn/giọng đúng; không tự gửi dựa vào tài liệu này.

Giữ đúng preset `EP01_Khoai_K20_Orus_720p_v1`, mapping lịch sử `b447b35c-b35e-4140-af72-ecd277282b1a`; không chọn Orus nền, K12 hoặc D06. Chỉ một giọng nam và một câu trong C06. Không tạo preset, không nhập câu audition dài thành thoại tập phim, không mute/overdub tự động.

## 4. Thay đổi prompt có mục đích

Prompt REC275 đã nêu ý định chữa cháy nhưng vẫn ép dừng–giữ cuối cảnh. Không sao chép nguyên prompt đó. Bản mới cần:

1. Giữ trạng thái đã bị bắt ở đầu; không phát hiện Đào lần nữa.
2. Một chỉ dẫn diễn chủ đạo: cằm ổn định/hạ rất nhẹ khi tự trấn tĩnh; mắt vẫn chú ý Đào, thân có độ sống tự nhiên. Không bắt đồng thời nhún vai/gật/nghiêng người.
3. Một câu nam duy nhất **“Anh gắp cho em mà.”** theo K20: ấm, trầm, thân mật, hơi ngượng kín; phát âm tự nhiên, không thêm cười mời ăn.
4. Nói trọn âm cuối rồi chuyển cùng A về phía bát Đào; chưa thả trong phần C06 được chọn. Không yêu cầu đứng chờ bất động suốt đuôi video; chọn điểm ra đang chuyển động theo kết quả thực.
5. Giữ vật lý bàn: cốc tay ngoài Đào vẫn trên không ngoài bát, bát riêng còn rỗng trước nhận; mặt hai người và vùng đũa/bát đủ thấy; nem lạnh không khói, không lát đặc đồng dạng.

**Chưa có prompt cuối:** ảnh đầu chưa sửa/duyệt và UI chưa kiểm. Đây là bản đặc tả nội dung để chuyển sang prompt sau khi đúng tài nguyên; không ghi hash giả hoặc preflight PASS.

## 5. Trình tự thực hiện và điều kiện dừng

| Bước | Đầu ra cần có | Ai kiểm / điều kiện sang bước |
| --- | --- | --- |
| A. Chốt chi tiết diễn và chuẩn ảnh vào | Brief được owner chốt; một ảnh đầu có lineage/hash | Root + phản biện ảnh toàn khung + owner; ảnh ngoài món đổi thì dừng, không upload làm chuẩn |
| B. Chuẩn gói live | Prompt cuối, đúng ảnh/voice, cấu hình và quote read-back | Kiểm tên + mapping + chỉ một speaker; không khớp thì không submit |
| C. Xin lượt mới | Số lượt, quote/cap, bucket, điều kiện dừng rõ | Owner duyệt bounded request; không dùng quyền một lượt REC286 đã tiêu thụ |
| D. Chạy và tải gốc | Native 720p, hash, thông số, full decode, số dư trước/sau | Không coi tải hoặc ASR là chất lượng đạt; lỗi thì giữ source và báo, không retry tự động |
| E. Kiểm cảnh và hai đầu | Toàn-frame hình/props, diễn liên tục, tiếng/speaker/lời/sync, nối C05 và nhận | DIR/ACT, kiểm hình/camera/continuity, SIA/AV, phản biện độc lập; thiếu playback/nghe thì giao owner checkpoint đúng file |
| F. Chọn/cắt/nối | Khoảng khung có đủ lời + A chưa thả, nối động tác hợp lý | Đo thật, không mặc định 57 khung; không rút lời/tăng tốc/thay giọng để ép thời lượng |

Mọi lỗi lớn về mặt/trang phục/bối cảnh/props, speaker sai, diễn không đúng ý định hoặc thả A sớm trong đoạn chọn ⇒ **không chọn**. Không che mặt bằng cận món; không lấy kỹ thuật đạt bù diễn sai. Nếu clip chỉ có đoạn hợp lệ thì phải kiểm và trình đúng đoạn; approval full take không được suy từ approval tiếng hoặc ảnh.

## 6. Ngân sách, thời lượng và dự báo

Sổ vẫn **237/500**, còn **263**; phần tạo lại **26**, dự phòng **110** đóng. Không phân bổ lại dự phòng hoặc cho một chuỗi thử từ yêu cầu “tiếp tục”. Chưa có báo giá live nên chưa trừ hoặc khẳng định đủ số lượt.

Theo phần đang giữ trước đây, qua C06 là 689 khung/24 fps = 28,708 giây; trần bản nháp 35 giây còn 151 khung = 6,292 giây cho kết. Nếu C06 mới thay đoạn cũ 57 khung bằng đoạn có N khung, phần qua C06 sẽ là **632 + N khung**. Đây là phép tính kịch bản timing, không EDL mới hoặc dự đoán N. Mục tiêu cuối 30 giây vẫn giữ; cần đo nhịp nhận/N07/C09, không hứa giữ mọi đoạn cũ sẽ tự vừa 30 giây.

Đối soát phản biện: kết trong bản nháp 35 giây còn **208 − N khung**; kết trong mục tiêu 30 giây chỉ còn **88 − N khung** nếu các range trước C06 giữ nguyên. Với N = 57, mục tiêu 30 giây chỉ còn 31 khung, khoảng 1,292 giây. Đây là xung đột timing cần xử lý bằng quyết định dựng có đo thực, không tự bỏ lời/C09 hoặc kéo mục tiêu cuối thành 35 giây.

**Dự báo định tính:** giảm còn một speaker và một cảnh bỏ được nhu cầu model tái dựng cut C05→C06; đầu vào đúng giúp giảm reset tư thế. Rủi ro còn đáng kể ở liên kết diễn nhỏ, giọng mới sinh, A mềm mảnh và cốc/bát. Không có dữ liệu để báo xác suất thành công hoặc chắc đạt sau một lượt. Đầu vào có bằng chứng và cổng kiểm giúp phát hiện sai trước khi dùng trong bản dựng, không bảo đảm model không sai.

Phản biện PAPER độc lập đã hoàn tất và root đọc đầy đủ: `restart_720p_v1/06_qc/C06_ACT_technical_paper_independent_289.md`. Không có mâu thuẫn PAPER nghiêm trọng; các giới hạn ràng buộc ảnh và timing nêu trên đã được bổ sung. Không cấp chất lượng ảnh/video đạt hoặc quyền chạy.

**Hiện trạng:** đề xuất kỹ thuật đã lập và phản biện; ảnh vào, prompt cuối, kiểm live và request mới chưa có. Owner yêu cầu chỉnh sắc thái Khoai trước: bước kế tiếp là chốt sắc thái, chưa chuẩn ảnh hoặc sinh video trả phí.
