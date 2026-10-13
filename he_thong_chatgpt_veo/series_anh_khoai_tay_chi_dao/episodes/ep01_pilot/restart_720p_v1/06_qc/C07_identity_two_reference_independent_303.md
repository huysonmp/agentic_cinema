# REC303 — Review độc lập gói hai ảnh C07

**PAPER + STILL_INSPECTION: đủ trình owner duyệt neo nhận diện với các sai khác công bố; chưa được duyệt ảnh, chưa live preflight và chưa có quyền chạy video.** Không thấy MAJOR biến Đào thành người hoặc đổi loài trong portrait mới. Portrait không đạt yêu cầu “exact facial geometry” theo nghĩa bản sao không đổi; chỉ phù hợp vai trò neo nhận diện phụ, tuyệt đối không thay F47 hoặc thành endpoint.

## Bằng chứng và khả năng kiểm

Đã đọc đầy đủ approval `00_decisions/C07-identity-two-reference-preparation-approval-303.json`, regression pack `06_qc/C07_failure_regression_pack_303.md`, actual record `04_requests/C07_T02_run_277.json`, `06_qc/C07_T03_root_actual_280.md`, report actual REC302, image prompt `04_requests/C07_IDENTITY_PAIR_image_prompt_303.txt` và video draft `04_requests/C07_RECEIVE_identity_restore_prompt_DRAFT_303.txt`.

Trực tiếp xem nguyên ảnh:

- Scene `02_refs/C07_START_NATIVE_C06_KEEP_A_F47_CANDIDATE_300.png`: F47 của C06 đã chọn; vai scene/state duy nhất. Hash nguồn đã khóa `34f51b2a30650ed9ffdae1e30f177bbfd28c2e5c53bd47fa57063488ded9a4f2`.
- Portrait `02_refs/C07_IDENTITY_PAIR_v1_CHATGPT_FOR_REVIEW_303.png`: tự kiểm SHA-256 `796a7a9c70cdc3354755f18c95ea1ad9dcb9037912270de3f9bc96703281583d`; ảnh ngang 1536×1024 theo provenance root cung cấp, hai nhân vật từ ngực lên trên nền xám ấm.

Chỉ local read/view/hash và report theo REC217; không browser, API, media edit hoặc paid. Không nghe audio, xem AV hay tự kiểm backend. History REC277/280 được kiểm qua hồ sơ actual đã đọc, không tái xem toàn native trong task này; REC280 ghi rõ hai specialist actual không hoàn tất, không được gọi gate độc lập đã đóng.

## Sai khác cụ thể của portrait

Khoai vẫn là củ khoai tây dài màu vàng nâu có đốm, lông mày đậm, áo khoác than và cổ áo sáng. Đào vẫn là toàn đầu quả đào hồng cam có rãnh, cuống nâu, một lá xanh; mặt nằm trong vỏ quả, không tóc/tai người. Hai môi khép, hướng nhìn về nhau, bố cục Khoai trái–Đào phải phù hợp F47. Không bàn/tay/bát/cốc/A nên ảnh không đưa ra một trạng thái đạo cụ cạnh tranh.

Tuy nhiên đây là **redraw, không identity/pixel lock**. Khoai có mắt/lòng trắng nổi và sắc hơn, nét mày và đường cong miệng được vẽ lại, sắc độ da sáng/vàng hơn. Đào có mắt và mi rõ hơn, môi/mũi được định hình sắc hơn, bề mặt quả tương phản hơn; cuống dài và lá lớn/đậm hơn so F47. Cảm giác đầu Đào rộng hơn tương đối, dù vẫn giữ tương quan Khoai cao–Đào thấp. Nền và ánh sáng portrait khác scene; góc mặt gần nhưng không hoàn toàn trùng. Không có đo landmark nên không báo phần trăm khớp hay chênh kích thước chính xác.

Đó là caveat thật về khuôn mặt/texture/scale, không chỉ khác crop. Draft đã xử lý thứ bậc đúng: **F47 quyết định expression, material, scale, camera và scene; portrait chỉ xác định hai khuôn mặt và hình thái đầu thực phẩm**. Không có mâu thuẫn loài hoặc pose lớn đến mức chặn trình owner, nhưng nếu owner yêu cầu trùng mặt tuyệt đối thì không thể gọi v1 đã đạt mục tiêu ấy.

## Chuỗi hành động và hồi quy

Draft giữ một D06 và nguyên N07 “Thế em quay lại đúng lúc rồi.”; Khoai nghe, môi khép, giữ đúng A. Chỉ tay trong Đào nâng đúng bát rỗng từ bàn lên trước rồi sang dưới A, có khoảng hở tay nghỉ/bát Khoai. Tay ngoài giữ cốc nâng suốt cảnh; không hai tay nâng bát. A không nhả, không tới miệng, không về đĩa; giữ hai bát riêng, đũa nghỉ, rau/hai chấm/nem lạnh. Không lấy portrait làm start hoặc mượn endpoint sai của lịch sử. Paper không có MAJOR tự mâu thuẫn; một tay đỡ bát và khoảng hở thực vẫn là risk output phải kiểm, không chứng minh vật lý từ chữ.

Hồ sơ hồi quy hỗ trợ khôi phục control nhận diện, **không chứng minh hai ảnh sửa được lỗi**: REC277 và REC302 một scene + D06 đều hóa người; REC280 hai ảnh cùng wording khác giữ nhân vật thực phẩm nhưng reset pose/cho ăn/cốc hạ/endpoint sai. Vì ảnh và wording cùng đổi, không tách được tác động hoặc quy lỗi cho giọng D06. Gói mới không được nhập lại động tác cho ăn hay kéo bát của REC280. Việc preflight REC301 chưa đọc lại đầy đủ hồi quy là khoảng thiếu quy trình, không lời giải causal cho mọi lỗi.

## Cổng còn mở

Owner hiện duyệt **chuẩn bị** gói, không duyệt portrait v1 hoặc trả phí. Có thể trình đúng hai ảnh và caveat trên để chốt neo; sau đó mới kiểm actual hai chip ảnh đúng vai, một saved D06, prompt/read-back, config/quote, flags và ngân sách. Không sử dụng lại quyền REC302.

Project 258/500, còn 242, retake còn 5, reserve 110 CLOSED. Quote 7 trước lớn hơn phần retake còn 5; quote mới chưa biết, cần phân bổ được owner chốt trước request nếu không đủ bucket. Không tự chuyển first-pass/post/reserve. Actual F0 và toàn nguồn phải qua nhận dạng, props, miệng/âm thanh, diễn và đường bát; sai identity toàn nguồn thì loại, không prefix che lỗi. Không voice/physics/acting PASS hoặc xác suất thành công giả định. Food seam C05→C06 và final 30 giây so rough 35 giây vẫn mở.
