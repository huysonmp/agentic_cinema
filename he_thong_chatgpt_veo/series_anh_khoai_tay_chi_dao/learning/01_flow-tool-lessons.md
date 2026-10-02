# Nhật ký học từ Flow và công cụ kiểm

## 2026-10-02 — probe nâng nem 160: source pose phải rõ

END gần môi v0.1 bị loại trước Veo và chỉnh v0.2 có gap; tuy nhiên ba Lite vẫn sai động tác/hướng nhìn. Kiểm inventory và ảnh cuối chưa đủ: START/END Đào gần chính diện, chỉ cúi mắt về cốc, không biểu đạt rõ đang quay đi. Sợi nem nguồn rủ về bát, đầu ra kéo dài hơn; đây là giả thuyết source contribution chưa xác nhận nguyên nhân riêng. Preflight cần kiểm trạng thái hành động của từng nhân vật, hướng mắt/đầu và continuity phần nem với insert C01, không chỉ số đạo cụ. Sửa nguồn từng nhóm biến, không đổ lỗi một từ hoặc retry nguyên prompt. N02 kiểm dày thấy mở miệng/tiếp xúc vùng môi dù endpoint an toàn: endpoint không chứng minh trajectory. Ròng 30, trial còn184; không ghép ba bản lỗi hoặc dùng đoạn sau ăn để chuyển nem cho Đào.

## 2026-10-02 — probe cận cảnh gắp 159

Tách một động tác kẹp–nhấc–giữ với START/END mới cho một ứng viên có hình chuyển động đúng trong các khung kiểm. Chưa đủ để kết luận đây là công thức ổn định: hai trong ba lượt lỗi âm thanh, không có ba video đối chiếu. Không dùng việc đưa miệng ra ngoài khung để gọi lỗi ăn đã xử lý ở cảnh rộng. Kiểm continuity khi trở về hai nhân vật, phần nem và trục máy; giữ trạng thái ứng viên riêng cơ học. Nhịp khoảng 3s chờ trước nhấc cần xử lý khi dựng, không kéo nguyên clip 8s vào tập 30s. Đối soát actual 514 so với lần trước 524 => ròng 10, không trừ giá dự kiến 30 khi hai lỗi không tính phí. Imagegen dùng scene source + grip I05 để dựng START; chỉ hai khung START/END được nạp vào Veo, không trộn ảnh studio grip vào scene.

## 2026-10-02 — khóa nhóm hình ảnh 154

Mô tả rõ POTATO/PEACH FRUIT 3D và ụ nem sợi: ba Omni Flash mới giữ dạng nhân vật rau quả trong tám khung kiểm mỗi clip, món trở lại ụ sợi. Tuy vậy source fidelity khuôn mặt/tỷ lệ và texture nem còn lệch. Sửa nhiều chi tiết trong một nhóm không chứng minh một từ là nguyên nhân. Không nâng cải thiện phân loại thành production PASS. Reuse prompt trong màn edit không chuyển compose ra màn project khi back; kiểm compose trống rồi gắn input lại đúng ID, không submit nhầm route edit. Native download UI có file actual, không cần event để xác nhận. ASR vẫn gấp/gắp chưa nghe phân xử. Chi tiết tại [154](../episodes/ep01_pilot/154_visual-lock-voice-pair-retest.md).

## 2026-10-02 — probe cặp giọng 153

Âm thanh thành phần cần ảnh đi kèm mới hoạt động. Click chip compose gỡ input chứ không mở detail; phải khôi phục đúng ID nếu gỡ nhầm. Đã gắn Orus K20/Aoede D06/OPEN7, nhưng ba Omni Flash 360p vẫn có hai bản biến Đào thành người và bản giữ Đào đổi hình món. Gắn preset/ảnh không thay nghiệm thu actual. Cụm “adult peach woman” là giả thuyết mơ hồ cần kiểm, không nguyên nhân đã chứng minh. ASR có đủ ba câu nhưng gấp/gắp chưa nghe phân xử, không dùng để chứng nhận voice/accent. Hai download event timeout vẫn có MP4 thực trong Downloads: đối soát file và decode trước retry/generation. Ròng 18 credit. Chi tiết và evidence ở [153](../episodes/ep01_pilot/153_voice-pair-integration-probe.md).

## 2026-10-02 — bộ thử 127

### L-001: khôi phục tab khi phiên trình duyệt thay đổi

Quan sát: kết nối cũ mất trước lúc gửi generation. Sau khi đọc lại inventory, đã nối lại đúng tab và đúng dự án; không tạo video trong quá trình khôi phục.

Cách xử lý: đọc lại hướng dẫn và trạng thái tab; xác minh yêu cầu nào thực sự đã gửi trước khi thao tác. Không bấm tạo lại dựa riêng vào lỗi kết nối vì có thể trùng yêu cầu và tốn credit.

Giới hạn: sự cố phiên kết nối không chứng minh Flow mất dữ liệu hoặc Veo lỗi. Chưa có thử nghiệm đối chứng về nguyên nhân.

### L-002: chức năng sử dụng lại câu lệnh

Quan sát: sau R01 và R02, dùng nút sử dụng lại câu lệnh đã phục hồi prompt đầy đủ và ảnh đầu vào; END trống, cấu hình vẫn 720p/8 giây/x1. Đã chụp màn hình trước mỗi lần gửi.

Ứng dụng: thuận tiện cho bộ thử lặp lại, nhưng mỗi lần vẫn phải kiểm trạng thái phục hồi. Không coi nút này là bảo đảm mọi tham số luôn được giữ trong các phiên hoặc phiên bản Flow khác.

### L-003: thông báo tải không phải bằng chứng đã lưu local

Quan sát: Flow báo đã tải, nhưng chưa nhận được file ở các đường lưu đã kiểm. API chờ download hết thời gian; bundle các tài sản video quan sát trên trang lỗi fetch. Chưa xác định nguyên nhân; không khẳng định lỗi mạng, quyền hay hết hạn URL khi chưa có bằng chứng.

Cách xử lý trong bộ 127: giữ tài sản và URL, đối soát số dư, nhờ chủ dự án tải native. Không generation lại để chữa lỗi vận chuyển file; không gọi clip đã bàn giao khi thiếu file/hash.

Điều kiện kiểm lại: khi có file, xác minh nội dung/mã clip, kích thước, hash và khả năng giải mã; ghi cách tải thực sự thành công. Lần sau thử đường tải với tài sản sẵn có trước khi mở bộ tạo mới nếu tình trạng chưa được giải quyết.

Kiểm lại theo yêu cầu chủ dự án: chọn tải 720p gốc thêm một lần cho từng R01–R03, vẫn chưa có file local dù R02/R03 có thông báo thành công. Đường Downloads Windows không đổi. Bấm lại cùng tùy chọn chưa giải quyết được lỗi trong lần kiểm này; cần kiểm đường chuyển file hoặc hỗ trợ tải trực tiếp, không cần tạo lại media.

Đính chính theo kiểm 129: chủ dự án tải thủ công được và đã có file MP4 local đọc được metadata. Không quy lỗi cho Flow hoặc nguồn video. Thử giữ tab và bấm tọa độ 720p trên R01 vẫn chưa nhận được file; chưa chứng minh nguyên nhân nằm ở kiểu click hoặc chuyển tab. Cần đối chiếu đường thao tác thủ công và bảng Downloads của ứng dụng trước khi kết luận. Không dùng generation mới để thay thế việc sửa phương thức tải.

Kết quả media và bài học về diễn xuất/thoại: chờ kiểm sau khi đủ ba file. Không kết luận từ trạng thái đang tạo hoặc thumbnail.

### L-004: bộ tạo lại 130 đã nhận đủ file

Vòng 156–158: ba batch x3 Lite, chín file tải/giải mã được, ròng 90. Chỉ dẫn giữ thấp không đảm bảo model dừng; số đo “five centimetres” đi cùng lỗi sinh chữ ở L02, chưa xác nhận quan hệ nhân quả. Kiểm inventory bàn trong toàn chuỗi phát hiện bát Khoai mất/thay đổi, dù khung đầu có đủ. Không dùng khung sinh lỗi làm nguồn kế tiếp. Imagegen edit OPEN7 tạo END đủ hai bát, nhưng Veo giữa hai khung vẫn tự ăn/morph đạo cụ: endpoint control không tương đương trajectory control. Mẫu cuối đúng không là PASS toàn clip. Sau đối soát còn 24 trong quyền thử, không đủ x3 giá 30; không tự dùng số dư tài khoản 524 hoặc ngân sách Quality để vượt quyền. Lưu nguồn/prompt/output/hash/UI và kết luận riêng từng gate trước xin quyền mới.

Thử hành động 155: ba đầu ra được yêu cầu nhưng chỉ hai thành công, một lỗi âm thanh không tính phí; ròng 20 không phải giá quote 30. Hai take gắp được nhưng đều ăn nem, nên chưa đạt trạng thái để chữa cháy/gắp vào bát. Khi prompt chỉ định tay, phải đối chiếu giải phẫu nhân vật với vị trí đạo cụ trên màn hình: cốc ngoài phía phải màn hình gần tay trái Đào, không phải tay phải. Đây là lỗi chuẩn bị đầu vào đã xác định. Giả thuyết “đưa về miệng” khiến model hoàn tất ăn chưa được xác nhận. Tách kiểm nhấc/giữ vật trước, rồi điểm dừng gần miệng, sau đó trao bát; không sửa kịch bản chỉ để hợp lỗi model. 16 khung mỗi clip cộng kiểm dày đoạn cuối phát hiện lỗi mà thumbnail đẹp không cho thấy. Giữ tách technical PASS, động tác thành phần và toàn cảnh PASS; không gọi agent độc lập đã review khi chỉ người điều phối tự kiểm.

Theo yêu cầu chủ dự án, tạo một yêu cầu Lite x3 cùng ảnh/prompt, tổng giá 30. Tải lần lượt từ menu thẻ thư viện, giữ tab và kiểm file trước khi chuyển clip; nhận đủ ba MP4. ffprobe và giải mã sạch, hash/path lưu tại tài liệu 130. Đây là đường thực hiện đã thành công trong vòng này, không phải kết luận nguyên nhân Stopped của vòng cũ. Không tuyên bố tạo lại luôn chữa được lỗi tải; cần kiểm lại đường tải trên tài sản cũ ở một vòng diagnostic riêng nếu cần tìm nguyên nhân.

Bài học thao tác: khi index thẻ không còn đúng và click lỗi, đọc lại AX/screenshot, dùng nút menu của đúng thẻ; không lặp click hoặc generation mù. x3 là một yêu cầu ba đầu ra, phải ghi khác ba lần x1. Sau hoàn tất trả x1, và kiểm lại giá/cấu hình trước lần gửi sau. Thông báo tải chỉ là tín hiệu trung gian; file/hash/giải mã mới là bằng chứng nhận file.

### L-005: mùi của món nguội không được minh họa bằng hơi nóng

Chủ dự án thấy N01 có khói dù nem nguội; prompt đã cấm `extra steam` nhưng vẫn chưa đạt. Kiểm nguồn và frame tại hồ sơ 131, chưa có đối chứng nguyên nhân. Đề xuất mô tả trạng thái vật lý tích cực (món nguội, không khí trên đĩa trong và tĩnh), loại rõ khói/hơi/heat shimmer/đường mùi; diễn mùi bằng phản ứng nhân vật. Không bảo đảm prompt sửa sẽ đạt cho tới khi thử. Checklist món phải kiểm nhiệt độ và vật lý, không dùng vẻ đẹp hoặc độ hấp dẫn bù lỗi này.

Kiểm thực tế 133–134: đã thử ba mẫu prompt v1.1 nhưng cả ba vẫn có vệt hơi ở frame kiểm, một mẫu thêm chữ và một mẫu cầm đũa ngoài yêu cầu. Giả thuyết prompt sửa đủ mạnh chưa được xác nhận; không đưa bản này vào công thức đã kiểm chứng. Nên tách lớp hình/động tác với thoại/mùi để kiểm nguyên nhân, không lặp nguyên gói thất bại. Ba mẫu là bằng chứng của bộ này, không là thống kê tỷ lệ lỗi của Veo nói chung. Lưu file thành công không đồng nghĩa chất lượng nội dung đạt.

Kiểm tiếp 135–136: bỏ thoại và mô tả mùi/chảo, cả ba vẫn có vệt hơi trong ảnh mẫu; không quy lỗi chỉ cho thoại. Nhân vật tự mở miệng và diễn tay dù prompt yêu cầu im lặng. Không có âm thanh không đồng nghĩa không có động tác nói. Bộ ban đầu lỗi tạo âm thanh, UI báo không tính phí; bật tạm “Trả về video không có âm thanh”, thử lại từng thẻ một và nhận ba video chỉ có stream hình. Đối soát số dư 830→800, ròng 30; khôi phục tùy chọn về tắt sau thử. Phục hồi này hữu ích cho chẩn đoán hình, không dùng để bỏ qua gate voice/lip-sync ở cảnh thoại. Chưa có bằng chứng khống chế khói thành công.

### L-006: truy lỗi cuối chặng theo chuỗi nguồn, không chỉ sửa câu lệnh cuối

Owner quyết định ở 141: đủ bằng chứng để dùng cách xử lý tạm, dừng nghiên cứu sâu lỗi hơi và không tái lập control lúc này. Giữ M0 không câu cấm làm nền thử tiếp; kết quả chỉ là chưa thấy hơi trong ảnh mẫu, không thành cam kết. Bài học quản lý: tách quyết định dừng nghiên cứu nguyên nhân khỏi đóng lỗi sản phẩm; vẫn kiểm nhanh món nguội và các lỗi chặn trên take mới, ưu tiên hoàn thành giọng/diễn xuất/ráp thay vì điều tra vô hạn.

Review 140: thêm riêng câu cấm hơi vào M0 thì cả ba M1 có vệt trắng vùng serving, trong khi 137/138 chưa thấy trong ảnh mẫu. Đây là bằng chứng hỗ trợ yếu tố câu cấm trong prompt chính, không xác nhận từng từ hoặc negativePrompt API. Bước cần làm để tăng độ tin cậy là tái lập control, giữ rõ khác biệt thời điểm/seed/fallback. Lỗi có trong native video nên không truy nhầm sang Canva/download. C01 có camera drift dù không thay câu máy; mọi gate khác vẫn phải review khi chỉ sửa một lỗi. Không lấy kết quả tốt của một gate làm PASS chung.

Thử giọng 142/143: cố định lời và ảnh, mỗi hướng diễn ba mẫu Lite; đọc prompt ở từng asset để gán mã, tải native 720p rồi xác nhận file tồn tại và giải mã. Tách WAV không xử lý âm lượng/cao độ để nghe bản thật. Chỉ dẫn giọng Bắc không chứng minh output giọng Bắc; file có audio không chứng minh đúng lời hoặc đúng chất. Chọn take bởi owner trước kiểm giữ voice identity qua cảnh. Trích đoạn ngoài thứ tự chỉ là audition, không tự thành bản episode. Chín file tải được trên tab mới, không cần tái sinh vì lỗi tải; ngân sách thử chạm trần thì dừng, không dùng ngân sách Quality riêng cho Lite.

Owner review 144 loại cả chín mẫu vì giọng miền Nam. Bài học bổ sung: accent là gate nền, phải nghe đạt trước khi nhân ba hướng diễn. Không dùng cùng chỉ dẫn accent chưa kiểm chứng để mở rộng hàng loạt. “Northern Vietnamese” trong prompt không tương đương output đúng Bắc; technical PASS không thay listening PASS. Nguyên nhân model/prompt cụ thể chưa xác định; không tuyên bố sửa vài từ sẽ chắc chắn đạt.

Thử lại 145: tiếng Việt/Hà Nội cụ thể + một câu ngắn, ba mẫu; thay nhiều yếu tố nên nếu đạt cũng không quy công riêng tiếng Việt. Chờ nghe accent trước diễn; trần 200 không có nghĩa phải tiêu hết. Lưới không hiện thumbnail mới dù AX có title hết progress: reload một lần sau completion mở được asset, không tái sinh. Helper đọc prompt cần hỗ trợ ngôn ngữ actual hoặc đọc UI riêng; prompt field rỗng không được coi là đã đối chiếu.

RCA 146 sau owner loại cả 145: không có nguồn giọng Bắc thực nạp vào model, chỉ ảnh/prompt. Cần phân biệt yêu cầu giọng, voice source và kết quả nghe. PCM equality 12 cặp xác minh extraction không đổi giọng, không chứng nhận accent; technical QC không là nghe. Thiết kế agent có listening contract không đồng nghĩa actual reviewer đã nghe. Khóa capability/source/positive baseline trước diễn; thất bại nhiều prompt không chứng minh Veo mọi cấu hình bất lực, cũng không biện minh sửa chữ mò tiếp. RCA có process causes rõ nhưng cơ chế model còn mở.

Capability147: Omni/Thành phần có tab Giọng nói, preset + sample dialogue + performance + preview/save. Có thể kiểm candidate trước video generation; không suy Veo cũng hỗ trợ hoặc preset đảm bảo accent. Saving đổi actual name về mặc định dù đã nhập tên riêng: readback name/ID là SoT. Preview audio hidden blob không export được qua locator download; trình owner nghe trong UI, không fallback bằng hidden request. Đọc số dư sau thao tác không giảm ở lượt này, không generalize miễn phí.

Audition148: dùng chung 109 ký tự, gồm câu dài 83 ký tự, phản xạ ngắn và chữa cháy; viết riêng âm sắc/nhịp/ngắt/nhấn/chuyển biểu cảm cho 10 mẫu. Đã lưu đủ, không đồng nghĩa đã nghe đạt. Search theo base có thể tự chọn preset duy nhất; kiểm ID trước click để tránh thêm vào prompt. Search theo performance không có kết quả trong phép thử này. Số dư cuối 670 so với mốc 620: chênh +50 chưa giải thích, không suy giá preview. UI giới hạn sample 120 ký tự nên cần test dài hơn sau shortlist; giữ accent gate trước xếp hạng diễn, rồi kiểm ổn định nhiều lượt và tích hợp video riêng.

Audition149: thêm 10 trên tám base nam khác đọc trực tiếp trong UI, vẫn cùng sample để đối chiếu. K16 save chậm giữ base ID tạm, sau completion đã có custom theo tên mã; tìm mã trước retry để tránh tạo trùng. Tên trở lại base ngay sau bấm chưa đủ kết luận rename lỗi; kiểm lại danh sách sau completion. Chín mẫu khác vẫn tên base ở readback cuối. Số dư 670 giữ nguyên trong lượt, chưa nghe nghiệm thu. Thay base và diễn đồng thời là khám phá lựa chọn, không truy nguyên nhân bằng thử nghiệm kiểm soát.

Audition150: tên base trùng không đủ để khóa quyết định: hỏi owner phân biệt K20/K12 và nhận K20. Tuyển Đào dùng lời riêng cùng tình huống, có câu dài 87 ký tự, phản xạ ngắn rồi mềm lại; không dùng “tính cách trẻ con” thành giọng trẻ em. Lưu năm nữ trên base actual Female; sample/performance đúng không thay nghe. Tab picker có thể không hiển thị thành phần đang có trong compose; giữ compose owner, không xóa để tìm lại giọng. Số dư cuối 670, không video generation.

Audition151: thêm 10 nữ, tám base mới + hai biến thể diễn trên base cũ, giữ sample để so sánh. D07 chưa hoàn tất sau 20 giây: readiness/nút enabled mới là gate lưu, không dựa timer. Link số dư AX có thể thiếu label số dù screenshot hiển thị 670; dùng screenshot thay vì suy số từ lần trước. Tên base trùng phải đối chiếu ID/performance, không chỉ tên hoặc vị trí. Chưa nghe thì không gọi chất giọng/biểu cảm đã đạt; đổi base và diễn cùng lúc chỉ là khám phá ứng viên, không kết luận nguyên nhân.

Review 138 đã tải đủ ba M0: chưa thấy hơi trong 16 ảnh mỗi clip nhưng cả ba tự diễn tay/miệng. Bài học: tách từng tiêu chí, không dùng việc giảm một lỗi để gọi cả clip PASS; khác biệt sau khi bỏ nhiều nhóm chỉ hỗ trợ giả thuyết cấp nhóm. Bước truy tiếp phải thêm lại riêng một nhóm và giữ nhật ký actual settings, không khẳng định từ khóa gây lỗi hoặc ảnh nguồn chắc chắn vô can. Tab mới tải đủ bộ, xác nhận workaround vận hành, chưa xác nhận cơ chế lỗi tải.

Phục hồi tải M01 của 137: mở tab mới cùng URL video theo yêu cầu owner và tải 720p thành công; file có đủ hình/âm thanh, giải mã sạch. Có thể thử tab mới trước khi đề nghị owner tải hộ hoặc tạo lại. Đây là workaround kiểm chứng một lần, chưa xác nhận nguyên nhân tab cũ thất bại; không gán cho cache/token khi chưa có bằng chứng.

Owner yêu cầu ghi kinh nghiệm truy nguyên nhân cốt lõi. Đã lập [quy trình tám bước](02_root-cause-tracing-protocol.md): đóng băng bằng chứng, định nghĩa lỗi, truy phiên bản ngược, lập giả thuyết kèm phản chứng, thử kiểm soát, thêm lại từng lớp, kiểm hồi quy và chốt phạm vi kết luận. Tách nguyên nhân tạo lỗi khỏi nguyên nhân lỗi lọt cổng kiểm. Một workaround không là nguyên nhân đã xác nhận.

[Đối chứng 137](../episodes/ep01_pilot/137_minimal-motion-root-cause-control.md) đã tạo ba mẫu M0, cùng OPEN7, bỏ nhóm mô tả/cấm/diễn tay/thoại; 30 credit. Vì thay nhiều nhóm so với 135, không dùng kết quả để buộc lỗi cho một từ. Tải native chưa được; thumbnail hoặc xem trước nhỏ không đủ để đóng lỗi hơi. Bài học vận hành đã xác định: thông báo tải không thay file hiện hữu; lỗi xuất file cần hồ sơ riêng, không tiêu thêm credit để tái sinh khi chưa chứng minh video hỏng. Hiệu quả M0 vẫn chưa kiểm chứng, không thêm vào công thức thành công.
