# REC303 — Gói hai ảnh C07 đã chuẩn; neo nhận diện chờ duyệt

Ngày 13-10-2026. **Chuẩn ảnh và tài liệu, chưa chạy video.** Owner trả lời “ok” cho đề xuất sau REC302: giữ ảnh cảnh F47, tạo thêm ảnh neo nhận diện riêng và kiểm lại gói đầu vào. [Approval](restart_720p_v1/00_decisions/C07-identity-two-reference-preparation-approval-303.json) không cấp quyền chi thêm, đổi ngân sách hoặc nghiệm thu đầu ra.

## Hai ảnh, hai vai trò

| Ảnh | Phạm vi sử dụng | Không được dùng để |
| --- | --- | --- |
| F47 thật, 720×1280 | Trạng thái đầu, bố cục, tỷ lệ hai nhân vật, ánh sáng, biểu cảm, trang phục và toàn bàn; A còn trên đũa, bát Đào rỗng, cốc đang nâng | Tự chứng minh model giữ F0 hoặc chuyển động sẽ đúng |
| Neo nhận diện v1, 1536×1024 | Hình thái và khuôn mặt Khoai–Đào: củ khoai tây và quả đào có cuống/lá, không hóa người | Thay ảnh cảnh, tư thế tay/bát/cốc, điểm đầu/đích, góc máy hoặc ánh sáng toàn cảnh |

F47 giữ nguyên SHA256 `34f51b2a30650ed9ffdae1e30f177bbfd28c2e5c53bd47fa57063488ded9a4f2`. Bản owner được đặt tên `C07_SCENE_F47_UNCHANGED_303.png`; không sinh lại hoặc xử lý pixel ảnh này.

Neo mới `02_refs/C07_IDENTITY_PAIR_v1_CHATGPT_FOR_REVIEW_303.png`, SHA256 `796a7a9c70cdc3354755f18c95ea1ad9dcb9037912270de3f9bc96703281583d`, RGB, 1536×1024. Tạo bằng **imagegen tích hợp, một lượt**, chỉ tham chiếu F47 hiện hành; không dùng demo cũ, portrait278 cũ hoặc bản C07 đã hóa người. Skill imagegen giúp tách vai trò ảnh, nhắc giữ các đặc điểm bất biến và lưu phiên bản mới; không coi lời yêu cầu “giữ” là bằng chứng pixel được giữ.

Root đã xem ảnh nguồn và kết quả sinh: Khoai bên trái có đầu củ khoai tây, Đào bên phải có đầu quả đào, cuống/lá; mắt nâu, môi khép, áo khoác tối/áo sáng của Khoai và áo trắng của Đào còn nhận ra. Nền trơn, không tay hoặc đạo cụ. **Đây là ảnh vẽ lại:** chi tiết mặt, màu/texture, ánh sáng và tỷ lệ nhỏ không giống pixel F47 tuyệt đối. Ảnh cảnh phải thắng nếu portrait có khác biệt biểu cảm/trang phục/ánh sáng. Không nhận đã giữ nhận diện trên video.

## Đã sửa khâu chuẩn bị, không chỉ đổi câu prompt

Đã đọc đầy đủ C07 T02 REC277, actual T03 REC280 và review actual REC302 trước chuẩn mới. [Gói hồi quy](restart_720p_v1/06_qc/C07_failure_regression_pack_303.md) ghi cụ thể:

- Một ảnh cảnh + D06 từng hóa Đào thành người; ảnh nguồn đúng không đủ chứng minh nhận diện được giữ.
- Bản có thêm portrait giữ được dạng nhân vật thực phẩm nhưng vẫn sai hành động, cốc và tư thế đầu. Không kết luận hai ảnh riêng lẻ là nguyên nhân hoặc bảo đảm sửa được.
- Giữ choreography REC295: Đào dùng tay trong nâng đúng bát riêng; tay ngoài giữ cốc nâng; Khoai nghe và giữ A, chưa thả. Không nhập lại động tác đưa A tới miệng hoặc kéo bát trên bàn của các draft cũ.
- Không xem đường nhận có tiến triển là đủ bù lỗi mặt/cốc/tay/đũa nghỉ. Gate F0 và toàn nguồn phải thực hiện lại trên native mới.

Draft C07 mới giữ đúng N07 **“Thế em quay lại đúng lúc rồi.”**, một D06; bổ sung mô tả rõ đầu quả đào và vai hai ảnh, làm rõ chỉ một tay nâng bát và cốc không được đặt xuống. Đây là **draft**, chưa đọc lại trên Flow, chưa quote hoặc sẵn sàng submit. Hai ảnh và wording cùng thay, không gọi là phép thử một biến.

[Manifest nguồn/hash/phạm vi](restart_720p_v1/04_requests/C07_two_reference_input_manifest_303.json), [prompt tạo portrait](restart_720p_v1/04_requests/C07_IDENTITY_PAIR_image_prompt_303.txt), [draft prompt video](restart_720p_v1/04_requests/C07_RECEIVE_identity_restore_prompt_DRAFT_303.txt).

## Phản biện và cổng duyệt

Reviewer độc lập đã hoàn tất [báo cáo](restart_720p_v1/06_qc/C07_identity_two_reference_independent_303.md); root đã đọc toàn bộ. Reviewer đọc lại hồ sơ actual 277/280/302, không tái xem toàn các video cũ; trực tiếp xem F47 và portrait mới, tự kiểm hash portrait. Không thấy lỗi đổi loài/hóa người hoặc mâu thuẫn dàn cảnh trên giấy cản việc trình owner. Kết luận chỉ là **đủ trình duyệt làm neo phụ với sai khác công bố**, không phải nhận diện đã khóa trên video.

Sai khác cụ thể: mắt/lòng trắng, nét mày và đường miệng Khoai sắc hơn; mắt/mi/môi Đào rõ hơn, texture tương phản hơn, cuống và lá lớn hơn. Tương quan đầu và ánh sáng có thay đổi nhỏ; không đo landmark để báo tỷ lệ khớp. Nếu cần một bản sao khuôn mặt tuyệt đối thì v1 chưa đạt tiêu chí đó. Draft vẫn lấy F47 làm nguồn chính, không lấy portrait làm biểu cảm hoặc pose mới.

Owner cần chốt **neo nhận diện v1 dùng cùng F47**, không duyệt tư thế đầu mới, voice, motion, point nối, video hoặc toàn phim. Nếu ảnh còn sai nhận diện rõ, root sửa ảnh trước trình; không yêu cầu owner bỏ qua lỗi.

Sau duyệt ảnh: mới chuẩn binding hai ảnh + D06, đọc quote/config thực và trình request có giới hạn nếu ngân sách phù hợp. Quyền một lượt REC302 đã dùng xong. Phần tạo lại còn 5, thấp hơn quote 7 của lần cũ; chưa chuyển ngân sách từ phần tạo mới, hậu kỳ hoặc dự phòng. Không xin chi cho gói chưa chuẩn.

## Trạng thái, lưu trữ và bước tiếp

Folder owner: `C:/Users/PC/Downloads/du_an_nem_bui/303_C07_TWO_REFERENCE_INPUTS/`. Ảnh nguồn và neo có bản trong workspace; các bản copy đã kiểm cùng hash. Không ghi đè nguồn hoặc ảnh cũ.

**Đã xác định:** ảnh cảnh không đổi; portrait mới chỉ là neo nhận diện; failure history được đưa vào preflight.
**Quyết định đã chốt:** chuẩn gói hai ảnh, giữ lời/giọng và nhịp nhận trước–thả sau; chưa chạy video.
**Giả định đang dùng:** portrait có thể hỗ trợ nhận diện nhưng chưa chứng minh trên output.
**Còn mở:** duyệt portrait, kiểm live/request/ngân sách, motion/AV thực, lỗi món ở cut C05→C06 và mục tiêu cuối30 so với rough35.
**Bước tiếp:** hoàn tất phản biện ảnh/gói, trình owner duyệt neo; không chạy lại video trước quyền mới.

Flow upload 0, paid submit 0, debit **0**. Sổ giữ **258/500**, còn **242**; phần tạo lại **5**, dự phòng **110 đóng**. Không thay EDL chính, voice hoặc release cuối.
