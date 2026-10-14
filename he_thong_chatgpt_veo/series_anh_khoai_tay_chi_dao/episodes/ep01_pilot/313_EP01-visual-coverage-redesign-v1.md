# REC313 — Đề xuất tái thiết kế hình ảnh EP01, v1

Ngày 14/10/2026. **PAPER_PROPOSAL — chuẩn bị để owner duyệt hướng quay; chưa duyệt ảnh mới, góc máy mới hoặc lượt sinh video.**

Owner đã chỉ ra ba vấn đề ở rough312: khung gần như không thay đổi, chuyển cảnh kém và trọng tâm/góc quay chưa hấp dẫn. Sau đề xuất kiểm lại coverage bằng ảnh và phân loại footage, owner trả lời “ok”. Ghi nhận quyền chuẩn bị tại `restart_720p_v1/00_decisions/visual-coverage-redesign-preparation-313.json`; không coi đó là approval bản quay v1 dưới đây.

## 1. Xem gói đối chiếu trước

[Mở bảng ảnh hiện tại và sơ đồ khung đề xuất](restart_720p_v1/02_refs/coverage_redesign_313/coverage-board.html)

Cột trái dùng PNG nguyên khung từ đúng rough312, không crop/chỉnh mặt/món/ánh sáng. Cột phải là sơ đồ bố cục **không phải ảnh AI hoặc ảnh tham chiếu production**; chỉ biểu thị chủ thể lớn/nhỏ, đường nhìn và phần hành động cần thấy. Sơ đồ không chứng minh tạo được góc mới hoặc giữ được nhận diện. Món trong footage cũ vẫn có lỗi chất liệu; không dùng ảnh này làm chuẩn món mới.

## 2. Chẩn đoán và nguyên tắc cần sửa

Đã đối chiếu contract DOP, storyboard214, plan236, DOP239, prompts309/311 và ảnh rough312. Plan236 yêu cầu cận Khoai ở ký ức, cận hành động nếu cần khi thả A, khung chung cho nguyên nhân–bắt gặp–kết. DOP239 ghi chỉ đạo tích hợp của root chuyển C02 sang khung đôi cố định. Prompts309/311 tiếp tục khung đôi và cấm đổi máy/zoom/cut. Đây là **lựa chọn thực thi đã làm yếu độ phân biệt giữa các nhịp**, không chỉ lỗi model.

Giữ mọi mặt/tay/đĩa đều nhìn thấy là điều kiện kiểm ở cảnh cần chứng minh quan hệ; không phải cách bố cục tốt cho mọi câu thoại. Điều cần bảo vệ là **khán giả biết nhìn đâu và vì sao**, đồng thời không che lỗi. Không thêm chuyển máy cho đẹp, không phủ lời bằng cận món, không dùng dissolve để che trạng thái nhảy.

Ba tầng phải khóa trước prompt:

1. **DIR:** người xem cần hiểu/cảm thấy gì mới ở nhịp này; vì sao giữ hoặc cắt?
2. **DOP/ACT:** mắt/mặt/tay/vật nào là chủ thể chính, bố cục làm nó rõ thế nào, tín hiệu diễn nào dẫn sang nhịp sau?
3. **EDIT/CONT:** khung ra–khung vào và chuyển động có nối được không; đổi range có làm mất nguồn neo hoặc đổi nghĩa?

Tài liệu mới không thu hồi những approval tiếng/take cũ. Các approval ấy vẫn có đúng phạm vi lịch sử; không đủ chứng minh rough312 đạt chất lượng tổng thể.

## 3. Ngữ pháp hình ảnh đề xuất

Giữ đời thường, ấm và hài kín. Một trục tương tác xuyên tập; Khoai phía trái, Đào phía phải trong khung thiết lập. Góc cận lệch nhẹ về phía người nghe nhưng không tự sang phía đối diện trục. Không chốt độ góc/lens/khẩu độ giả từ sơ đồ.

| Kiểu cảnh | Nhiệm vụ | Bố cục / độ sâu / ánh sáng đề xuất | Không được làm |
| --- | --- | --- | --- |
| **A — Cùng bàn** |Thiết lập quan hệ, chứng minh cơ hội gắp lén, trở về bữa ăn |Hai mặt đủ lớn, bàn chỉ chiếm phần cần kể; giảm khoảng phố trên đầu; đèn nền là phụ, không ngang độ nổi bật với mắt |Không giữ làm mặc định cho toàn phim; không gom mọi đạo cụ vào khung bằng cách làm mặt nhỏ |
| **K — Điểm nhìn Khoai** |Ký ức riêng, câu đáp tỉnh và nét chữa cháy |Cận vừa đầu–vai/ngực, lệch nhẹ phía Đào; nhìn về cô, không nhìn lens. Khi nói ký ức, món chỉ là ngữ cảnh thấp khung, không cạnh tranh với mắt. Tay/đũa/A phải còn nếu đang liên quan |Không biến thành độc thoại MC; không dùng crop mạnh để giả góc nghiêng; không cắt mất âm cuối |
| **D — Điểm nhìn Đào** |Câu hỏi hoặc phản ứng “em hiểu anh rồi” |Cận vừa tương thích cùng trục. Mắt cô là chính; nét/tay/bát nào cần hiểu được giữ dưới khung. Người nghe có cue riêng ở cảnh kề, không bắt hai mặt lớn ngang nhau mọi frame |Không biến cô thành người xét xử hoặc nhìn máy; không bỏ cốc/bát khỏi scene chỉ vì ngoài coverage |
| **T — Khung căng thẳng chung** |Cho khán giả thấy ý định, Đào không thấy rồi thấy |Hai mặt + cốc + đường A trong một envelope liên tục; chọn scale đủ đọc khựng/caught, không chỉ kiểm được số đạo cụ |Không cut vào thao tác thiếu nguyên nhân; không tạo hai shot cùng góc gần giống chỉ vì đổi câu |
| **I — Cận chuyển món** |Chứng minh A vào đúng bát một lần |Bát đang được Đào cầm, đầu đũa, A và tay hỗ trợ là chính. Góc hơi cao ở phía trước bàn nếu hình mới đạt; bối cảnh còn dấu liên tục |Chỉ dùng ở cảnh không thoại hoặc khi không mất cảnh nói đã khóa; không bắt món to/đẹp làm mất đường đi |

“Focus” ở đây là ưu tiên thị giác. Chưa đề nghị rack-focus hoặc thông số độ sâu trường ảnh cụ thể. Nếu sau này thử chuyển nét, phải có mục đích và kiểm mặt/đường A thực, không mặc định làm mờ người nghe sẽ đẹp hơn.

## 4. Coverage theo chín nhịp — lựa chọn nghệ thuật, chưa phải shot lock

| Nhịp | Khán giả nhìn / hiểu gì | Coverage và lý do chuyển | Điều phải kiểm trước duyệt |
| --- | --- | --- | --- |
| R01 — Đào định lấy, Khoai “Khoan” |Một bữa ăn tự nhiên; anh ngắt vì mùi gợi nhớ, không phán món |A thiết lập. Cận Khoai hiện có cho “Khoan” là ứng viên; trở về không được làm tay Đào tự về chỗ trước phản ứng |Đủ tay định lấy→dừng→thu; cut cận không mất nguyên nhân, tiếng đúng người |
| R02 — Ký ức bếp nhà |Mắt Khoai rời món, chuyện riêng mở ra với Đào |K ưu tiên Khoai trong cả ý ký ức; cảnh yên có điểm chú ý rõ. Không thêm flashback hoặc mỗi câu một cut |Có thay đổi cỡ/điểm nhìn thật so A; mặt kể đủ sắc thái, không chỉ “thấy đủ miệng”. Tiếng mới không tự kế thừa approval246 |
| R03 — Hỏi và đáp |Đào đoán “chờ ăn”; anh hé chuyện ăn vụng |D cho câu hỏi, K cho câu đáp nếu pair hai góc khớp; hoặc một T chặt hơn giữ cả phản ứng nếu pair thất bại. Cut vì thông tin đổi, không vì hết file |Không nháy máy quá vụn; cuối câu đáp còn thời gian Đào hiểu rồi chuyển chú ý; cùng trục/món/tay |
| R04 — Tranh thủ |Khán giả thấy cơ hội và ý định trước Đào |T/A mở đúng envelope. Giữ action chính liên tục: cô chú ý cốc→anh lấy A→kéo về mình→cô nhìn lại |Không dùng cut tay để giấu gaze sớm. Vùng action đủ đọc ý định, không giữ phần ngồi trống để chờ lượt sinh |
| R05 — Bị thấy |Ánh mắt Đào chạm A rồi anh; Khoai khựng |T chặt hơn hoặc D tương thích có A và dấu phản ứng Khoai. Không cắt sang chân dung cô làm mất việc anh biết bị thấy |Phản ứng và A thấy được, không đổi người cầm/chất miếng tại cut; chính điểm24s hiện còn lỗi |
| R06 — Chữa cháy |Miệng nói tỉnh, mắt có nét ngượng kín |K thấy mắt/miệng và A vẫn giữ; chưa gộp chuyện “cho” thành anh vốn có ý định cho từ đầu. Nhịp chuyển A sang bát vẫn ở R07/08 theo quyết định gần nhất |Cận phải giữ A/tips ở vùng đủ đọc; không đổi wave K20 cũ mà tự gọi vẫn giọng đã duyệt |
| R07 — Nhận lời chữa cháy |Đào hiểu, tiếp trò, đưa bát chủ động |D hoặc T chặt: mặt Đào, bát riêng và A cùng ý nghĩa. Chỉ đổi góc nếu không mất đường nhận |Cốc/bát/tay rõ; không reset A. Ngoại lệ đặt cốc ở C09 đã duyệt chỉ scope312, không tự dời sự kiện vào câu R07 |
| R08 — A vào bát |Được cho thật, không chỉ nói |I ngắn đúng lúc đũa hạ, hoặc giữ T nếu động tác đã đủ rõ. Insert là công cụ kể, không bắt buộc phải thêm cut |Exact A/bát/tips đầu–cuối; một lần thả; vật thể/chất nem chuẩn. Không lời ở insert |
| R09 — Ăn ý |Anh vẫn muốn ăn; hai người cùng hiểu |Trở A hoặc T mềm: B mới về phía Khoai, A còn bát Đào, kết ở gặp mắt. Trả cảm giác chung bàn sau các điểm nhìn riêng |Không kết chỉ bằng bát. Mẫu8khung nhìn nhau trong rough35 chưa đủ bằng chứng; phải có thời gian cảm xúc được đọc, không freeze hoặc speed |

Các kiểu K/D không có nghĩa mọi câu phải là single shot hoặc mọi người nghe luôn ngoài khung. Chỉ tạo shot reverse khi pair cho thấy giá trị; số cảnh sinh sẽ được xác định sau reference/coverage test, không giảm hoặc nhân thêm quy trình vì cảm tính.

## 5. Footage giữ được, có thể dựng lại, và thiếu nguồn hình

Phân loại **ứng viên**, không promotion production. Lấy source/range theo EDL312 và các approval hiện hành; bảng không sửa nguồn hoặc range cũ.

| Nguồn / nhịp | Giá trị có thể giữ | Khoảng thiếu / cách xử lý đề xuất |
| --- | --- | --- |
| C01A/BM/BR |Tiếng và trạng thái mở; BM có cỡ cảnh khác |Ứng viên giữ, chọn lại biên theo tay/ánh nhìn. Pair chung→cận→chung vẫn cần kiểm chuyển động, không chỉ ảnh |
| C02 |Tiếng K20 trên exact export246 và diễn đã được owner chấp nhận |**Chưa có góc K như đề xuất.** Reframe nhẹ cùng góc chỉ ứng viên, không giả thành góc mới. Cận 3/4 cần ảnh/footage mới. Không hứa ghép tiếng cũ lên miệng mới sẽ khớp; phương án audio/AV phải được kiểm trước chọn |
| C03A/C03B |Lời, giọng và nét đối đáp có giá trị |Cũ chủ yếu chung cùng góc. Có thể giữ làm phương án T; phương án D→K cần coverage mới, không cắt nửa ảnh rồi nhận là reverse-angle |
| C04 |Chuỗi cốc→gắp A là nền chứng minh hành động |Ưu tiên giữ làm backbone T; timing và caught pause phải kiểm actual. Món chưa đồng nhất với phần sau; không dùng approve hành động để waive hình món |
| C05 |Tiếng Đào và mặt nói câu bắt gặp |Có thể giữ như T ứng viên nhưng không có D/T chặt mới. C05→C06 food seam chặn selection. Cận mới cần source-reference đúng A và trạng thái bị thấy |
| C06/C07 block308 |Tiếng, range và bản sửa miệng có approval cụ thể |Giữ block nguyên làm phương án an toàn so sánh. K/D mới là thiếu footage; bỏ block cũ vì muốn đẹp hơn không tự cho quyền sinh lại. Chất A/plate tại entry C06 phải sửa hoặc tạo nguồn mới đúng, không để insert che rồi gọi khớp |
| C08 |A vào đúng bát, tips rút trống ở prefix64F |Giữ làm phương án T; **chưa có insert I thực**. Crop phải kiểm pixel, tay và watermark; không có crop hợp lệ thì I cần native hình mới. Không lặp thả A khi đổi coverage |
| C09 |B mới/ngoại lệ đặt cốc, gặp mắt ở đuôi đầy đủ |Giữ candidate nguồn; ưu tiên khôi phục đuôi để đọc kết nếu timing cho phép. Trim đổi entry F8 không mặc định khớp C08. Chưa promise final30 hoặc ending tốt chỉ bằng thêm8F |

Quy tắc lựa chọn: giữ lời/giọng/canon; dùng footage có giá trị đúng nhiệm vụ. Chỗ chưa có góc mới được ghi **NEEDS_NEW_VISUAL_SOURCE** chứ không “dựng chắc được”. Không sửa mặt bằng phép crop để che lỗi miệng hoặc xóa watermark.

## 6. Thứ tự chuẩn bị và kiểm — chưa mở sinh video

1. Owner chọn hướng K/D/T/I trên bảng này; chưa cần chốt từng prompt hoặc credit.
2. Chuẩn **ảnh cặp trước–sau quan trọng**, không tạo cả lô mù: R01→R02 (món sang chuyện riêng), R04→R05→R06 (bị thấy/chữa cháy), R07→R08→R09 (bát/cho–nhận/kết). Mỗi ảnh ghi nguồn, không gian, điểm chú ý, nhân vật, object-state và redraw risk. Cận mới phải có reference mới đúng món/pose, không lấy PNG cũ lệch món làm master duy nhất.
3. Kiểm liên tục storyboard ảnh cùng lời/timing thực. Nếu ảnh đa dạng nhưng đoạn nối vẫn nhảy hoặc mất cause thì sửa giấy/reference trước request. Ảnh đẹp không chứng minh motion/voice.
4. Inventory lần hai: chỗ giữ/retime/reframe thật đạt, chỗ cần sinh mới; chốt cách bảo vệ tiếng. Với cảnh nói mới, native speech/lipsync/identity và tiếng exact source cũ phải đối soát; không lấy preset cùng tên làm PASS. Không tự cài tool hoặc mở API để giải bài toán đó.
5. Lập từng request thật sau gate ảnh và audio: route/inputs/quote/bucket/exit-reference; chỉ khi có quyền phù hợp mới submit. Sau đổi range phải cập nhật reference nối, không dùng endpoint cũ. Same-major lặp hai lần dừng chẩn đoán, không tiếp tục thử mù.
6. DIR/DOP/ACT/EDIT review **exact assembled export**, trước finishing. Ngoài count/miệng/props, phải trả lời: shot có nhiệm vụ không, có điểm chú ý rõ không, shot đổi có đem thông tin/cảm xúc mới không, caught/punchline/ending có đọc được không? Thiếu khả năng nghe/xem thật ghi HOLD, không đẩy whole quality sang owner.

Không build thêm agent lúc này. Vai sẵn có cần sản phẩm và gate chất lượng này; chưa có báo cáo agent độc lập REC313. Các task reviewer312 trước bị giới hạn không được viết thành đã chạy xong hoặc thay bằng model khác để né giới hạn.

## 7. Timing và ngân sách — không hứa quá khả năng

35s là rough cap264, final30 vẫn giữ. Thay coverage **không tự rút thời lượng thoại/hành động**. Không lấy sự đa dạng góc máy làm bằng chứng vừa30, không tính lại bằng thời gian tưởng tượng. Slot mới chỉ đo sau ảnh/footage/audio cụ thể; ending cần cảm giác thực chứ không quota8F.

Sổ gần nhất đã kiểm312: còn221/500; tạo mới66, tạo lại0, hậu kỳ45, dự phòng110 đóng. Vòng313 chi0, không refresh tài khoản. **221 không phải quyền tự chi221.** Coverage mới có thể thuộc hậu kỳ45 hoặc thay take cũ cần chuyển bucket; phải phân loại và trình scope/quote trước mọi paid step. Không đưa xác suất thành công hoặc số lượt/giá mới chưa có gate.

## 8. Một quyết định cần duyệt: cách kể bằng hình

| Phương án | Cách kể | Hệ quả cần kiểm |
| --- | --- | --- |
| **A — Khuyến nghị: điểm nhìn có chọn lọc** |A/T giữ quan hệ hành động; K/D làm rõ ký ức, câu đáp và phản ứng; I chỉ khi cần chứng minh thả A |Tạo tương phản theo cảm xúc, không cắt mỗi câu. Thiếu một số góc thật: cần reference mới và phương án bảo vệ tiếng/khẩu hình trước dự trù video |
| **B — Quan sát bằng diễn liên tục** |Ưu tiên các khung T dài hơn, dàn động tác và ánh nhìn trong cùng cảnh; cận K cho ký ức và I khi thật cần |Ít đổi điểm nhìn hơn nhưng đòi hỏi diễn, ánh sáng và bố cục mạnh. Không phải giữ nguyên khung đôi hiện tại; cũng có thể cần nguồn mới, chưa chắc ít credit hơn |

Owner chỉ cần chọn A hoặc B, hoặc chỉnh nhịp cụ thể. Bảng chín nhịp đang minh họa A. Không hỏi lại tên/voice/canon hay quyền chuẩn bị đã chốt. Sau khi chốt hướng, bước tiếp là chuẩn ảnh cặp và kiểm storyboard; approval hướng không tự duyệt ảnh, tiếng mới hoặc lượt video trả phí.

## 9. Tổng hợp vòng này

- **Đã xác định:** khung đôi mặc định và cổng thẩm mỹ yếu là vấn đề cấp hệ thống; không phải chỉ thiếu chuyển cảnh. PNG được đối soát nguồn/hashes, chưa ảnh mới.
- **Quyết định đã chốt:** chuẩn gói tái thiết kế; giữ kịch bản/nhân vật/giọng đã chọn, không chi mới hoặc release.
- **Giả định làm việc:** đời thường/ấm/hài kín vẫn đúng mục tiêu; cận/đối đáp có thể giúp phân cấp chú ý nhưng chưa tested. Sơ đồ không chứng minh feature công cụ.
- **Còn mở:** owner camera revision, cặp reference mới, AV/audio bảo vệ, food seam, timing, review độc lập và final30/finishing.
- **Bước tiếp:** duyệt hướng → chuẩn ảnh cặp → kiểm storyboard liên tục → inventory/dự trù theo gap thực → gate video riêng.
