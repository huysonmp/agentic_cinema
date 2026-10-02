# Nhật ký học từ Flow và công cụ kiểm

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

Review 138 đã tải đủ ba M0: chưa thấy hơi trong 16 ảnh mỗi clip nhưng cả ba tự diễn tay/miệng. Bài học: tách từng tiêu chí, không dùng việc giảm một lỗi để gọi cả clip PASS; khác biệt sau khi bỏ nhiều nhóm chỉ hỗ trợ giả thuyết cấp nhóm. Bước truy tiếp phải thêm lại riêng một nhóm và giữ nhật ký actual settings, không khẳng định từ khóa gây lỗi hoặc ảnh nguồn chắc chắn vô can. Tab mới tải đủ bộ, xác nhận workaround vận hành, chưa xác nhận cơ chế lỗi tải.

Phục hồi tải M01 của 137: mở tab mới cùng URL video theo yêu cầu owner và tải 720p thành công; file có đủ hình/âm thanh, giải mã sạch. Có thể thử tab mới trước khi đề nghị owner tải hộ hoặc tạo lại. Đây là workaround kiểm chứng một lần, chưa xác nhận nguyên nhân tab cũ thất bại; không gán cho cache/token khi chưa có bằng chứng.

Owner yêu cầu ghi kinh nghiệm truy nguyên nhân cốt lõi. Đã lập [quy trình tám bước](02_root-cause-tracing-protocol.md): đóng băng bằng chứng, định nghĩa lỗi, truy phiên bản ngược, lập giả thuyết kèm phản chứng, thử kiểm soát, thêm lại từng lớp, kiểm hồi quy và chốt phạm vi kết luận. Tách nguyên nhân tạo lỗi khỏi nguyên nhân lỗi lọt cổng kiểm. Một workaround không là nguyên nhân đã xác nhận.

[Đối chứng 137](../episodes/ep01_pilot/137_minimal-motion-root-cause-control.md) đã tạo ba mẫu M0, cùng OPEN7, bỏ nhóm mô tả/cấm/diễn tay/thoại; 30 credit. Vì thay nhiều nhóm so với 135, không dùng kết quả để buộc lỗi cho một từ. Tải native chưa được; thumbnail hoặc xem trước nhỏ không đủ để đóng lỗi hơi. Bài học vận hành đã xác định: thông báo tải không thay file hiện hữu; lỗi xuất file cần hồ sơ riêng, không tiêu thêm credit để tái sinh khi chưa chứng minh video hỏng. Hiệu quả M0 vẫn chưa kiểm chứng, không thêm vào công thức thành công.
