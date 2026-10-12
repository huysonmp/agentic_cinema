# REC277 — C05→C06 được duyệt; C07 dừng để sửa tầng neo hình

Ngày 13-10-2026. **C07 NOT_SELECTED / STOP_FOR_DIAGNOSIS / C08 HOLD / NOT_FINAL.** Giữ tất cả nguồn và approval trước; không chạy T03 tự động.

## Đã chốt

Owner trả lời “Đạt — duyệt điểm nối C05→C06” cho đúng bản nối5,125 giây, SHA `42d826e1356ce67acc6e1057b4ceefc9703f3e705ffa14ae6c09dea7934b5bdf`: đủ âm cuối, đúng Đào rồi Khoai, nhịp và điểm cắt. Không chuyển approval đó sang C07 hoặc toàn phim. Ghi tại `restart_720p_v1/00_decisions/C05-C06-join-owner-acceptance-277.json`.

## Hai nguồn C07 đã làm và nguyên nhân quan sát

| Nguồn | Kết quả thực | Tầng lỗi / xử lý |
|---|---|---|
| T01, SHA `d1ed08ffca20e8bbee1455f14ed672fb4e2f538374a3ba209d6cfe49a195bfc0` | Đào chạm và kéo bát Khoai bên trái; bát riêng cô bên phải đứng nguyên. Đầu cảnh tay/A reset về phía Khoai. | Sai gắn hành động vào vật thể ngay trong native, không phải khi ghép. Không có đoạn hoàn thành đúng nhiệm vụ để chọn. |
| T02, SHA `c793308e55ed02f5b61fb9dfd1f4f6edaa4b3302bdb520defb108cfa5b5140da` | Đào thành phụ nữ người thật từF0 tớiF143; bát Khoai mất; cốc đổi phía/tay và thấp hơn; A reset. Một bát còn lại bị dịch xa về trái. | Regression danh tính/set/entry trong native. Không có đoạn dùng được; không nhận là sửa thành công bát vì nền hình đã sai. |

T02 là một can thiệp có chẩn đoán trong scoped238: hai nhóm sửa (neo bát bằng quan hệ vị trí; khóa tư thế vào), cùng lời N07/D06/camera/boundary, qua maker–critic trên final SHA `ae636235971fb36f5a31234dcb294cb91ea5d12c9231c8b046b797b8ad756ef4`, live kiểm lại rồi chỉ gửi một lần. Không phải thử nghiệm một biến; không chứng minh wording là nguyên nhân duy nhất. Lỗi kế thừa tư thế vào lặp, kèm MAJOR mới: dừng theo238, không tự T03.

Root đã tự xem đủ144 ảnh/take qua18 bảng/take; T02 thêm fullF0/F64/F143 và exactSTART. Maker và phản biện độc lập chạy trên nguồn mới, báo cáo tại `06_qc/C07_T02_maker_actual_277.md` và `06_qc/C07_T02_independent_actual_277.md`; root đã đọc đầy đủ cả hai bản COMPLETE_PROOFREAD, cùng bác T02. Critic gọi cốc đặt bàn ở đuôi; root/maker chưa xác định tiếp xúc chính xác từ ảnh, nên giữ kết luận chắc chắn cốc thấp/đổi tay/reset, không cần thêm claim contact để loại nguồn. Các ảnh không là xem AV liên tục/nghe thực. T01 ASR nhận N07 chỉ là evidence transcript; T02 không chạy ASR vì hình đã bị loại, không cần hỏi owner duyệt giọng một hình sai rõ.

## Đã truy lại ảnh đầu vào, không đổ lỗi đoán mò

Trên lịch sử đúng output T02, prompt khớp final và chip ảnh preview vẫn hiện Khoai–Đào nguyên bản, hai bát cùng bố cục predecessor. Bằng chứng `C:/Users/PC/Downloads/du_an_nem_bui/277_C07_T02/C07_T02_ACTUAL_IMAGE_INGREDIENT_PROOF.png`. Đối chiếu trực quan, chưa tải/băm byte ảnh server. Không có bằng chứng chọn ảnh phụ nữ người thật. Native và ba bản lưu cùng hash, 720×1280/24fps/144 khung, giải mã sạch; lỗi không do tải hỏng hay encode bản cắt.

**Chắc chắn:** output không giữ ảnh tham chiếu/danh tính/props/entry theo yêu cầu. **Chưa chắc:** vì sao model tái dựng như vậy; prompt dài/các ràng buộc cạnh tranh và cơ chế Ingredients chỉ là giả thuyết. Không hứa thêm vài câu cấm sẽ giải quyết. Cần kiểm lại cơ chế neo khung/hình trước trả phí mới.

## Chi phí và thời lượng

Hai lượt10+10 credit; sổ dự án187→207/500, còn293. First-pass còn82, retake56, post-rough45, reserve110 **đóng**. Số dư tài khoản live1043→1033→1023 là dữ liệu khác cap dự án; chênh+133 cũ vẫn park, không mở quyền chi mới.

C01–C06 đã chọn689 khung =28,708333 giây. Còn151 khung =6,291667 giây tới rough35 cho C07–C09. Chưa có range C07 đạt; không hứa fit35, không cắt lời hoặc bỏ hành động nhận/thả/kết để ép thời lượng. Mục tiêu final30 giây chưa tự thay bằng35.

## Bước tiếp theo cần owner chốt một hướng

**A — khuyến nghị: chuẩn bị lại gói neo hình C07, chưa sinh trả phí.** Kiểm live Flow có thể ràng buộc khung bắt đầu/kết thúc với voice hiện hành như thế nào; khóa đúng hai nhân vật, hai bát, tay/cốc/A bằng bộ tham chiếu đủ rõ và prompt tập trung. Chỉ nếu tương thích route/voice đã giao mới trình gói final + quote; route/công cụ mới phải owner chốt. Giữ nhiệm vụ C07 nói và chuẩn bị bát, C08 mới thả. Hệ quả: thêm kiểm đầu vào nhưng không chấp nhận đổi canon hoặc sinh mò; chưa bảo đảm model đạt.

**B — đổi thiết kế coverage/ranh giới hành động.** C07 chỉ phản hồi, chuẩn bị bát chuyển sang đoạn hành động riêng trước thả; cần storyboard/timing/voice–picture map và approval mới. Có thể giảm phối hợp nhiệm vụ trong một lượt, nhưng tăng số điểm nối và nguy cơ vượt35. Không tự triển khai hoặc dùng T01/T02 sai làm source.

Giữ K20/D06/N07, hai nhân vật nguyên bản, món nguội và bàn quán nhỏ. Vấn đề mở: cơ chế neo hình tương thích, continuity/các range cuối, giọng–sync mới và thời lượng cả phim. Owner chỉ cần chọn **A hoặc B**; chưa cần duyệt tiếng take bị loại. Tài liệu kinh nghiệm: `restart_720p_v1/09_lessons/REC277_bowl_ownership_and_direction_binding.md`.
