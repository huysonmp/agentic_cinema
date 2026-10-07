# REC228-CONT/DOP — Điều kiện sản xuất và continuity

Ngày: 2026-10-07. Critic độc lập local-only. Chưa đọc maker228 hoặc kết luận root228 trước khi chốt. Phạm vi là đánh giá thiết kế sản xuất dựa trên nguồn đã có; không phải review video sản xuất mới.

**Kết luận:** bỏ bài thử tay riêng và batch ×3 theo chỉ đạo owner; sản xuất candidate có nhiệm vụ trong phim rồi QC. R01 còn một vấn đề đầu vào/đầu ra mức MAJOR cần cụ thể hóa ngay trong production brief: M tay còn vươn, nhưng đầu N02 B tay đã nghỉ. Không hứa nối liền chỉ từ hai ảnh. Chuỗi R04–R09 phải giữ F0→F4→miếng mới, mặt người nói và nguyên nhân hành động. Dự báo bảy đơn vị/70 credit không chứng minh hoàn thành trong account 77.

## Cơ sở và năng lực thực tế

Đã đọc storyboard214, runtime217, quyết định anchor223, source/state map và review nguồn223, cùng request/input-readback và preflight227 đã lập trong context. Đã parse bảng tám record nguồn và các trạng thái trong `223/source-frames.json`; không coi tên folder hoặc footage cũ đã từng dùng là production PASS.

Đã xem trực tiếp bằng `view_image(detail="original")`: S v01, M v03, E v02 và N02 B `frame-0000.jpg`. Đã tính lại hash ba ảnh S/M/E và native N02 B. Đây là evidence ảnh tĩnh/tệp cục bộ; lượt này không nghe N02, không playback liên tục, không kiểm lip-sync hoặc motion thực. Nhận định về các take cũ khác dựa trên báo cáo223, không được ghi thành quan sát video mới của critic228.

Chỉ đạo hiện hành do root chuyển: owner bỏ test tay riêng, đi vào production rồi QC, account còn 77 và không cấp thêm. 227 batch thử ba Lite/30 credit bị supersede cho mục đích test; không chuyển nó thành quyền chạy ba production take cùng prompt. Không browser, generation, chi tiêu, retry, video/voice hoặc Git trong run critic này.

## Năm kiểm quan trọng giữ lại

1. **Đúng lời–người–mặt:** N01/N03/N05/N07 Đào; N02/N04/N06 Khoai. Thấy mặt/miệng người nói và khẩu hình hợp audio đã chọn; người nghe không nói thay. Silent footage không thay hình người đang nói.
2. **Nhân quả hành động:** Đào định lấy đĩa rồi dừng theo “Khoan”; sau N04 cô lấy cốc, Khoai tranh thủ, bị thấy rồi khựng, mới đổi hướng chữa cháy. Không bỏ nguyên nhân để vá lỗi clip.
3. **Miếng A và bát:** A từ đĩa chung, chưa chạm miệng Khoai, giữ cùng miếng qua bị thấy/đổi hướng, vào bát Đào đúng một lần. Bát chỉ có A sau thả; sau đó mới có B mới hướng về Khoai.
4. **Mặt–tay–bàn và trục:** Khoai trái/Đào phải, cùng phía trục, nhận dạng/outfit/nơ hồng và variation B; mặt/mắt/đường miếng nhìn rõ. Giữ serving geography, món nguội không khói; không dùng crop/cut/zoom để giấu lỗi tay hoặc thiếu face.
5. **Biên nối và AV thực:** ghi đầu/cuối/range/hash của candidate, kiểm mọi frame quanh thao tác/cut và nghe/xem AV đúng export. QC candidate và bản nối cần thiết; ảnh đẹp, metadata hoặc audio-source acceptance không thay QC phim.

Đây là kiểm sản phẩm thực sau production, không yêu cầu một batch test mới. Chỉ đóng lỗi tại source/range/join thực; không xếp nhiều approval cục bộ thành full-film PASS.

## R01: điều kiện đầu vào/đầu ra và nối sang N02 B

Đầu vào production phải nêu rõ N01 nguyên văn “Anh nhìn mãi. Không hợp thì để em.”, giọng Đào D06, mặt Đào nói, Khoai nghe; hình bắt đầu F0 với hai bát rỗng và tay như S. M là pose vươn giữa hành động đã được owner chấp nhận, không bắt buộc là frame cuối của toàn R01. E là ứng viên pose tay về nghỉ, không tự là footage hành động hoặc chứng nhận AV.

Đầu ra cần thấy Đào vươn đúng tay ngoài phía ly, quanh ngoài bát/đũa, dừng trước tiếp xúc đĩa/món khi nghe “Khoan”; tay trong và tay Khoai giữ nhiệm vụ nghỉ. Nếu nối vào N02 B có tay nghỉ, phải có nhịp tay trở về đọc được, đúng thứ tự sau cue. Gap ngón–vành ở pose dừng phải còn thấy; không xuyên bát/đũa/ly, không kéo vật bàn để mở đường. Không bắt cả hai môi khép trong phần N01 hoặc “Khoan”: đó là phần nói, chỉ miệng người nghe khép.

**Quan sát:** ảnh M tay phải còn ở cạnh đĩa và che một phần trước phải bát; B f0 hai tay Đào đã nghỉ, Khoai mở miệng. S/E có tay nghỉ nhưng khác biểu cảm so với đầu B. **Suy luận:** hard cut M→B có nguy cơ nhảy vị trí tay; chưa có motion chứng minh sự chuyển về. Nếu trở về E trước khi audio N02 bắt đầu “Khoan”, causal stop dễ thành hành động đã tự kết thúc trước lời giữ lại.

| Phương án production/nối | Điều kiện và hệ quả | Nhận định |
| --- | --- | --- |
| R01 mới có N01 và coverage đúng mặt Khoai nói “Khoan”, Đào dừng rồi đưa tay về nghỉ; nối sang B ở điểm hình phù hợp | Dùng **nguyên audio native N02 B liên tục, đúng một lần**; phần đầu audio có thể nằm dưới hình production mới chỉ khi Khoai thực sự có khẩu hình đúng. Sau khi tay đã về trạng thái match, quay về hình B ở điểm lời/gaze đã đo. Không thêm một “Khoan” sinh mới vào master. | Phương án xử lý nhân quả rõ nhất. Đây là thay coverage đầu N02, nên cần ghi cụ thể phần picture nào thay, range và tiêu chí AV; acceptance exact B trước đó không tự duyệt coverage/join mới. Route production thoại phải khả thi và có quote riêng. |
| Giữ nguyên cả picture+audio B từ f0 | Candidate R01 và join thực phải chứng minh dừng đúng cue và không làm tay nhảy/reset. Các endpoints S/M/E hiện có chưa đủ chứng minh. | Chưa có phương án đã xác minh đáp ứng đồng thời causal stop và tay nghỉ đầu B. Không ghi READY vô điều kiện, không cắt/che mặt cho qua. |

Khuyến nghị đưa phương án coverage cụ thể vào production brief R01 và review theo chính clip sản xuất, thay vì tiêu credit cho test tay riêng. Không tự trim N02 theo mốc 3 giây của chuyển camera: đó không phải ranh giới của từ “Khoan”. Không cắt giữa từ, lặp từ, phủ bằng silent Khoai môi khép hoặc dùng whole WAV202 cũ; 223 chỉ rõ WAV202 chứa old N02 source200, khác native B hiện hành.

Rủi ro hand–bowl của M vẫn cần QC toàn path: che khuất 2D không tự là xuyên bát, nhưng ngón nhập gốm, đi xuyên lòng bát hoặc đảo trước/sau bất khả lý là lỗi chặn. Gói production cần giữ cả mặt và tay quan trọng trong khung, không đặt camera move để tránh quan sát rủi ro đó.

## Chuỗi R04–R09: điều kiện vào/ra dùng cho production

| Nhiệm vụ | Điều kiện đầu vào | Điều kiện đầu ra / lỗi cần chặn |
| --- | --- | --- |
| R04 — cô lấy cốc, anh tranh thủ | Sau N04; F0, A còn trên P, bát Đào rỗng, đũa Khoai chưa giữ A. Cô chuyển chú ý tới cốc tự nhiên. | Thấy A được gắp từ P sau khi cô quay đi, hướng về anh, chưa contact miệng: F1. Không bắt đầu clip đã cầm A rồi coi đã chứng minh pick-up. Cần đủ hai mặt và đường A để khán giả biết trước Đào. |
| R05 — bị thấy / N05 | F1, cùng A/đũa/cốc. Đào quay lại nhìn A rồi Khoai. | Khoai gặp gaze và khựng, A còn kẹp: F2. Đào nói “Chờ em quay lưng nữa à?” thấy đúng mặt/miệng; không close Đào đơn lẻ thay toàn bộ proof caught/khựng. |
| R06 — chữa cháy / N06 | F2, A chưa ăn và chưa được hướng cho cô từ trước. | Khoai nói “Anh gắp cho em mà.” thấy mặt/miệng, bình thản rồi đổi hướng A về bát Đào: F3. Không silent clip che speaker, không insert tay phủ cả câu, không reset đũa nghỉ. |
| R07 — hiểu và đưa bát / N07 | F3, bát Đào còn rỗng; A trên đũa tới vùng nhận. | Đào nhìn miếng rồi anh, đưa bát và nói “Thế em quay lại đúng lúc rồi.” thấy mặt/miệng. Cô hiểu/trêu nhẹ, không chờ đút, không thắng cuộc. A chưa thả nếu R08 còn riêng. |
| R08 — thả A | Match vị trí bát/tay/đũa/cùng A với tail R07. | A thả vào bát đúng một lần, đũa rút: F4. Có thể gộp vào production R07 nếu thao tác rõ; không đòi một unit/insert riêng chỉ vì storyboard có R08. Không duplicate drop hoặc food teleport. |
| R09 — cùng hiểu và B mới | F4, A vẫn trong bát Đào, đũa Khoai đã rời A. | Khoai gắp miếng B khác từ P hướng về chính anh; Đào cười nhẹ, hai mặt và bữa ăn còn đọc được. Không reset bát rỗng, không đưa B tiếp về Đào hoặc thay kết bằng mutual smile F0. Không yêu cầu ăn/chạm miệng B nếu storyboard chỉ cần tự gắp. |

Được gộp coverage/unit khi production chứng minh đủ nhiệm vụ và thoại, không đổi câu chuyện. Không giả định một unit luôn bằng một dòng R; lời dài, giới hạn route, start/end và công tác lip-sync có thể đòi cấu trúc khác. Các source cũ 163/194/154/207/209 có giá trị pose/action reference theo223, nhưng chưa là toàn chuỗi production usable. Đặc biệt 154 reset F0, 207 thiếu mặt nên không thay R06/R07, và 209 chưa chứng minh rõ hướng B về Khoai.

## Ngân sách: giới hạn thật, forecast có điều kiện

`7 × 10 = 70` chỉ là forecast khi **cả bảy unit đều có quote 10**, route đúng chức năng, output đầu tiên dùng được và không phát sinh unit khác. Chín nhiệm vụ R01–R09 không tự suy thành bảy generation unit. Quote Lite 10/take ở227 là evidence lịch sử cho frames S→M, không phải quote cho thoại/giọng D06/K20/lip-sync hoặc mọi route production.

Account 77 không cấp thêm có nghĩa không được tiêu hơn số dư thực hoặc dựa vào bổ sung sau. Nếu thật sự dùng 70 còn 7, một lượt nữa giá10 đã không vừa. R01 cần thoại + causal hand + bridge; R03 cần hai speaker; R05–R07 cần mặt/thoại/miếng liên tục. Chất lượng các nhiệm vụ này không được bảo đảm bằng số units hay tổng tiền.

Trước mỗi unit production, ghi mục tiêu, source/prompt/output, **route chức năng phù hợp và quote live riêng**, chi đã thực trả, số dư thực và forecast phần còn lại. Nếu route thoại khác Lite hoặc chưa chứng minh hỗ trợ audio/voice được chọn, phải quote và xác nhận tính khả thi trước; không lấy giá Lite để đặt silent video rồi gọi đáp ứng speaker. Khi tổng nhu cầu quote đã biết không vừa số dư, ghi thiếu cụ thể để owner chọn trong ràng buộc hiện hành; không tiêu trước rồi thay story/voice/face để chữa cháy.

Một unit được sinh để dùng trong phim rồi QC; không pre-buy ba biến thể và không auto-retry. QC phát hiện lỗi thì sửa được ở range/join hợp lệ trong phạm vi khi có bằng chứng; lỗi cần generation mới phải được xét theo quyền và số dư còn lại, không coi ngân sách account là quyền retry vô hạn. Report này không cấp quyền chi.

## Evidence định danh và closeout

| Artifact đã rehash ở lượt228 | SHA-256 |
| --- | --- |
| S v01 | `eba9a13c86f359df458022a5a54664264e5bb29fcca08d6181454cb1ee482422` |
| M v03 | `66defd18afc0845da8b34968446b98f547dcad951e6712e2e6a81ff2d5e2017c` |
| E v02 | `8df19973fa6595cd166cab67b08a2009256091fb05bf14be322b1371308dbc03` |
| N02 B native | `660f175775db6b082458846edb5c8edc8beb771b90a3330f53cb37d07f31a535` |

Các hash khớp manifest/nguồn liên quan đã đọc; không có source media mới hoặc thay đổi nguồn. N02 acceptance của owner đúng scope vẫn giữ; joins, replacement coverage nếu dùng, toàn chuỗi, 30 giây và export hiện hành còn phải kiểm thực. Target30 không được chứng minh bằng phép trừ duration cũ, không bỏ lời/ending hoặc tăng tốc để ép vừa.

Đã chốt hướng production rồi QC, không batch test riêng và không thêm credit. Giả định làm việc: giữ N02 B native audio nguyên lượt; dùng S/M/E đúng vai pose, variation B/TABLE08/PAIR03 và F0–F4/A–B giữ khóa. Còn mở: exact R01 speaking route/quote và bridge M→B, line/audio ranges thực R03/R05–R07, media causal R04–R09, chi phí đủ và AV/fullscene. Bước tiếp theo là maker/root khóa một brief production R01 có bridge thật và quote thoại, sau đó sản xuất một candidate phục vụ phim theo authority hiện hành và QC; không gọi forecast70 là guarantee.
