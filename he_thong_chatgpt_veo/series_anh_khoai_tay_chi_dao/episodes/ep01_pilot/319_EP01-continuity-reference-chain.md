# REC319 — Chuỗi reference bắt gặp → chữa cháy → nhận → kết

Ngày 15/10/2026. **Đã chuẩn ảnh và kiểm tĩnh; chưa nghiệm thu chuyển động hoặc toàn phim.** Vòng ảnh này dùng built-in imagegen, chi Flow0. Lượt coverage video riêng được ghi ở REC320, không gộp chi phí hoặc approval vào hồ sơ ảnh.

## Một nguồn khung chung, giữ các quyết định đã chốt

Lấy `R04_EXIT_v1_CANDIDATE.png` của318 làm nguồn bố cục/trạng thái chung cho bắt gặp. Không nối thẳng từ khung rộng318 sang khung chặt315 khác cỡ bàn/mặt rồi gọi là khớp. Các ảnh315/316 được giữ nguyên, chỉ dùng đúng vai mốc bố cục/diễn/tư thế đã chấp nhận; không tự chuyển approval sang pixel mới.

Owner yêu cầu “ok làm tiếp đi”: cho tiếp tục công việc trong scope, **không ghi thành duyệt exact ảnh319**. Dịch tay sau N06 vẫn theo quyết định317; cốc vẫn ở tay ngoài Đào, không thừa kế ngoại lệ đặt cốc của rough312. Không đổi lời, K20/D06, nhân vật trưởng thành/bạn bè hoặc mục tiêu30s.

## Sáu ảnh theo câu chuyện

| Nhịp | Ảnh ứng viên | Điều đã kiểm tĩnh |
| --- | --- | --- |
| R05 xác nhận | [T-confirm](restart_720p_v1/02_refs/continuity_chain_319/T_CONFIRM_A_v1_CANDIDATE.png) | Đào đã quay lại rồi, chỉ liếc xuống vùng A. Khoai còn nhìn A; hai bát trống trên bàn, cốc ở tay ngoài cô |
| R05 cuối câu trêu | [T-caught](restart_720p_v1/02_refs/continuity_chain_319/T_CAUGHT_END_v1_CANDIDATE.png) | Hai người nhìn nhau, A còn kẹp phía Khoai, chưa cho/ăn/thả. Cùng nguồn khung rộng của318 |
| R06 chữa cháy | [K-excuse v3](restart_720p_v1/02_refs/continuity_chain_319/K_EXCUSE_HAND_v3_CANDIDATE.png) | Cận ưu tiên mắt/mặt Khoai, vẫn thấy tay/đũa/A và bát anh trống; Đào/cốc ở rìa phải. Đã bỏ khối hồng ở A, thay phần nhỏ phủ thính; đồng nhất chính xác với A khung chung vẫn mở |
| R07 đón bát | [S1](restart_720p_v1/02_refs/continuity_chain_319/S1_RECEIVER_READY_v1_CANDIDATE.png) | Đào nâng đúng bát riêng còn rỗng bằng tay trong; tay ngoài giữ cốc. A còn kẹp, tay Khoai dịch theo biến thể đã chốt; tay nghỉ không đỡ bát |
| R08 sau thả | [S2](restart_720p_v1/02_refs/continuity_chain_319/S2_AFTER_DEPOSIT_v1_CANDIDATE.png) | Phần A trong bát cô; tips trống, rút phía Khoai, có khoảng tách nhìn được. Bát anh vẫn rỗng, không A trên cả đũa lẫn bát |
| R09 kết | [S3](restart_720p_v1/02_refs/continuity_chain_319/S3_NEW_B_ENDING_v1_CANDIDATE.png) | A vẫn trong bát Đào gần người cô; B mới ở đũa Khoai phía anh. Cốc vẫn tay ngoài, hai người gặp mắt/cười kín, chưa ăn |

Đây là **root static candidates**, không phải native frame, owner image approval hoặc production/AV PASS. Năm khung chung dùng hướng bố cục chung; cận K có nhiệm vụ riêng, không biến cả tập trở lại một khung đôi cố định.

## Cận Khoai: lỗi thật, đổi cách xử lý và giới hạn

K v1 làm phần A dày và có khối hồng; v2 thay trực tiếp vẫn giữ dạng đó, không chọn. Sau hai kết quả cùng vấn đề, dừng nhánh thay trực tiếp; chuyển sang tách hai bước: tạo `K_FOOD_CLEAR_v1_EDIT_ONLY.png` xóa phần A, rồi chèn lại phần nhỏ từ ảnh món thật và tham chiếu lượng ở T-caught.

**Khung clear chỉ là trung gian sửa ảnh**, tuyệt đối không là R06, không phải cảnh đã thả hoặc nguồn native cần nói “Anh gắp cho em mà.”: lúc ấy A phải còn trên đũa. V3 phục hồi A, không tự sửa EDL hoặc thay native cũ. File v1/v2 vẫn mang tên CANDIDATE lịch sử nhưng manifest ghi NOT_SELECTED; không chọn nhầm theo filename.

V3 bỏ được khối hồng, bề mặt phần kẹp gần texture thính trong ảnh thật hơn theo quan sát. Nhưng màu/lượng A khác khung chung/S1, đĩa chung cũng có redraw. **Không gọi đã khớp vật liệu và bảo toàn lượng tuyệt đối**, không suy ảnh đẹp thành native transfer đạt.

[Đo pixel đọc-only](restart_720p_v1/06_qc/K_food_reinsert_pixel_scope_319.json): so clear→v3, ngoài vùng A xấp xỉ [315,1000,485,1180], khoảng98,83% pixel có ít nhất một kênh RGB đổi, trung bình chênh tuyệt đối2,15/255 mỗi kênh. Vùng chỉ định không phải segmentation. Điều này phủ nhận pixel lock, **không chứng minh mặt sai hoặc continuity đạt/không đạt về ngữ nghĩa**.

## Kiểm nguồn và những gate vẫn mở

[Manifest319](restart_720p_v1/02_refs/continuity_chain_319/reference_manifest_319.json) ghi9output/9prompt, original path, hash, kích thước và input có thứ tự. Prompt được ghi trước mỗi call; output copy ngay sau khi trả về, không sửa pixel local. K v1:940×1672; tám ảnh còn lại940×1673, không đúng tuyệt đối9:16 và chưa native720×1280.

- Hai bát đúng vai/trạng thái; cốc tách khỏi bát, không thêm đôi đũa Khoai trên bàn khi đã cầm; rau trước-trái và hai chén chấm còn cùng vai. Chưa chứng nhận va chạm/ngón tay/3D clearance bằng still.
- S1→S2 chỉ cho trạng thái trước/sau; phải thấy một lần nhả A thật. T-caught→S1 vẫn cần bridge dịch tay/nâng bát sau N06, không jump pose.
- S2→S3 còn thiếu đường đũa trống xuống đĩa rồi lấy B mới và Đào thu bát. Không cho B tự xuất hiện ở cut.
- T-caught→K→khung chung nhận cần actual eyeline, camera geometry, tốc độ tay và nội dung miệng. Không lấy khung chung tĩnh làm endpoint native của cận K.
- Màu/độ hạt và lượng A/B/đĩa chưa khớp tuyệt đối. Bố cục ổn định ở ý đồ không phải cùng pixel; nguồn319 chưa làm cả phim đồng nhất.
- Chưa tạo voice hoặc nghe/xem AV ở vòng ảnh. Không báo cáo agent độc lập mới; root tự kiểm, không gán tên vai thành người đã review.
- Không lập EDL30 hoặc phân bổ slot giả từ still. Baseline840F/35s của312 vẫn là đối chứng, không final30.

## Tiến sang sản xuất trong đúng quyền đã có

Đã đọc lại `scoped-autonomy-238.json`: owner cấp riêng45credit cho **post-rough-cut coverage**, native720p/x1, quote tối đa15/output; không phải mọi lượt đều cần xin lại. Hồ sơ trước nêu approval ảnh không duyệt paid là đúng về scope ảnh, nhưng không hủy quyền coverage độc lập đã cấp ở238.

REC320 chuẩn/chạy riêng một góc cận ký ức mới bằng ảnh K-entry314 đã được duyệt và saved K20; **không dùng ảnh319 chưa duyệt để chạy**. Phân loại coverage vì bổ sung góc còn thiếu sau rough bị từ chối; giữ C02 cũ làm fallback, không lấy retake0 gắn nhãn mới để bù retake và không chuyển bucket/mở reserve. Chỉ tiến hành khi preflight/livequote đúng scope, sau đó vẫn giữ checkpoint owner cho exact C02 mới.

### Tổng hợp vòng ảnh319

- **Đã xác định:** có chuỗi sáu ảnh cùng nguồn cho bắt gặp/nhận/kết và cận có A; lỗi khối hồng được xử lý bằng clear→insert, không local pixel lock.
- **Đã chốt giữ:** thoại/giọng, vai tay/bát/cốc, biến thể dịch tay sau N06, A một lần sang bát và B mới; không duyệt thay owner.
- **Giả định:** cùng parent giảm nguy cơ lệch bố cục, nhưng chưa đo native continuity hoặc xác suất thành công.
- **Còn mở:** A giữa các cỡ cảnh, geometry/motion/AV, format, timing và approval exact output.
- **Bước tiếp:** kiểm native coverage mới riêng ở320; đối soát nguồn/điểm nối trước khi đưa vào phim, không tự mở chuỗi retry.

Built-in imagegen theo skill; prompt/nguồn được lưu đầy đủ trong folder319. Ảnh/QC lưu local theo `.gitignore`, Git chỉ lưu hồ sơ/prompt/hash. Vòng ảnh319 Flow0; ngân sách thực của coverage320 ghi riêng, không nói cả lượt công việc này0 nếu320 đã debit.
