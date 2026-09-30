# EP01 — P6 design spec và kế hoạch mẫu thử v0.1

Ngày: 2026-09-30. Status: ROOT_DESIGN_DRAFT / NOT_GENERATED / NOT_REVIEWED_AS_MEDIA.

Theo [approval38](38_p5-content-handoff-and-p6-direction-approval.md). Không là runtime PROD7 run hoặc quyền generate. Những chi tiết mỹ thuật dưới đây là giả định thiết kế để có bản thử cụ thể; owner chưa khóa chúng thành canon.

## 1. Thiết kế Anh Khoai Tây

- Silhouette: thân khoai thuôn, phần trên hơi lệch tự nhiên; vai vừa, dáng đứng vững, không lực sĩ hoặc bụng phóng đại. Hình khoai là identity, không đội đầu khoai lên người bình thường.
- Chất liệu: vàng nâu ấm, mắt khoai/lấm tấm nhỏ tiết chế, không vết nứt hoặc bề mặt bẩn. Chất 3D mềm nhưng không nhựa bóng.
- Mặt: mắt nâu vừa phải, lông mày rõ giúp thể hiện nhận xét kín; cười lệch nhẹ, không mặc định nhăn nhó. Tóc/râu không đưa vào baseline.
- Outfit pilot: sơ mi kem mở một nút cổ, tay xắn dưới khuỷu; quần than, giày nâu giản dị, không cà vạt/blazer/logo/đạo cụ nghề.
- Body language: hơi nghiêng để chú ý món, động tác có cân nhắc; khi bị bắt gặp chỉ dừng một nhịp rồi đổi hướng, không trợn mắt giật mình.

## 2. Thiết kế Chị Đào

- Silhouette: quả đào hồng cam, rãnh nhẹ và cuống/lá nhỏ giúp phân biệt với táo; nét mềm, tư thế linh hoạt. Không vòng eo/đường cong hoặc mỹ phẩm phóng đại.
- Chất liệu: lớp lông đào mịn rất nhẹ, không thành thú bông. Màu hồng tự nhiên, không má đỏ như em bé.
- Mặt: mắt nâu sáng, ánh nhìn chú ý; lông mi tiết chế; cười tinh nghịch có chủ ý. Không mắt quá lớn, giọng/dáng toddler hoặc trang phục học sinh.
- Outfit pilot: áo màu ngà, khoác mỏng xanh sage, quần nâu nhạt và giày đơn giản; không tạp dề/bó hoa/trang phục đôi.
- Body language: chủ động kéo đĩa rồi lấy cốc, khi quay lại nhìn miếng nem rồi Khoai; đưa bát như biết trò mà vẫn nhận phần ngon, không khoanh tay tra hỏi.

## 3. Sheet và asset manifest cần tạo

| ID đề nghị | Nội dung | Status hiện tại |
|---|---|---|
| K-BASE-v1 | Khoai toàn thân chính diện, 3/4 và nghiêng; outfit/tỷ lệ thống nhất | PLANNED |
| D-BASE-v1 | Đào các góc tương ứng; phân biệt rõ đào với táo | PLANNED |
| KD-PAIR-v1 | Hai người ngồi bàn như bạn, khoảng cách đời thường; không dựa đầu/ôm | PLANNED |
| KD-EXPR-v1 | Khoai chú ý/khựng nhẹ/chữa cháy; Đào tò mò/nhận ra/trêu kín | PLANNED |
| KD-HANDS-v1 | Bàn tay trưởng thành cách điệu, cầm đũa và bát; kiểm ngón/vật thể | PLANNED |

Không tự coi nhiều góc trong một sheet là consistency đã chứng minh. Sau khi chọn base, cần kiểm identity ở các asset khác và motion sau này. Mỗi file phải có provenance/tool/request/version/approval; ảnh demo là DEMO_ONLY, chưa dùng làm input sinh mặc định.

## 4. Set/food intake trước khi tạo scene reference

Working set: bàn ăn nhỏ ánh sáng ấm trung tính; Khoai bên trái hình, Đào bên phải là giả định staging, chưa khóa shot. Đĩa món ở giữa, bát trước mỗi người, cốc trong tầm lấy phía ngoài Đào. Không gian không được gọi là địa điểm thật Bắc Ninh; không poster/landmark/logo tự thêm.

Food vẫn EVIDENCE_INTAKE_PENDING. Task: đối chiếu ảnh/tư liệu Nem Bùi và provenance từ nguồn nghiên cứu P2; lập appearance ledger mô tả phần thấy được, biến thể/unknown. Chỉ mô tả những gì nguồn hỗ trợ; không tự đoán hình nem bằng tên, thính luôn bám ngoài hoặc món đồng nhất với nem chua. Tài liệu xem để nghiên cứu không tự cấp quyền upload ảnh vào Flow. Nếu không có usable ref, dùng mô tả được kiểm và ghi giới hạn, không giả rights clearance.

## 5. Voice/performance map — giữ nguyên lời

Khoai: giọng nam trung ấm, trưởng thành; nhịp có cân nhắc nhưng không kéo lê. Đào: giọng nữ sáng, trưởng thành; linh hoạt và tự chủ, không the thé/giọng em bé. Không clone hoặc gắn giọng với người nổi tiếng.

| Câu mẫu exact | Ý định / cách thể hiện đề xuất | Fail cần nghe thấy mới kết luận |
|---|---|---|
| Khoai: “Mùi này làm anh nhớ cái chảo.” | Ý nghĩ riêng vừa xuất hiện; nhẹ ở “nhớ”, không giới thiệu bài học | Gượng như đọc slogan, nghe thành xác nhận nguyên liệu |
| Khoai: “Bếp nhà anh, hồi bé. Mẹ rang gạo, anh đứng chờ.” | Ký ức gần gũi; nghỉ tự nhiên giữa hai ý, không sướt mướt | Giọng thuyết minh lịch sử hoặc giả già |
| Khoai: “Chờ mẹ quay lưng.” | Thừa nhận gọn, tỉnh; không cười trước để báo joke | Nhấn quá mạnh hoặc diễn lén lút cường điệu |
| Đào: “Chờ em quay lưng nữa à?” | Đã nhận ra, trêu nhẹ; không chất vấn | Giọng mẹ mắng hoặc không hiểu chuyện |
| Khoai: “Anh gắp cho em mà.” | Chữa cháy bình thản, không nhấn “em” kiểu tán tỉnh | Hoảng hốt, lãng mạn hoặc xin lỗi |
| Đào: “Thế em quay lại đúng lúc rồi.” | Vui vì bắt được trò và nhận món; kết kín | Nói ngây thơ tin thật hoặc thêm câu ngoài script |

Khoảng nghỉ/tốc độ chưa có số đo. Sample sẽ ghi duration thực tế và cảm nhận khi nghe; không ghi lời đọc target thành measured. Native tiếng trong Flow và hậu kỳ là hai workflow còn phải kiểm, chưa khóa; không hứa giữ giọng/lip-sync chỉ từ prompt.

## 6. Kế hoạch thử và trình duyệt

1. Character stills: kiểm riêng identity/outfit/adult cues trước khi dùng vào scene/clip; không dùng món chưa kiểm làm phương tiện quyết định nhân vật.
2. Pair/expression/hands: kiểm quan hệ bạn, biểu cảm kín và khả năng cầm đạo cụ. Nếu ảnh tĩnh đạt vẫn chưa chứng minh chuyển động đổi hướng đạt.
3. Voice sample: nghe từng người và đoạn đối đáp exact; kiểm nhịp, thái độ, tính nhất quán. Dùng đoạn ký ức để kiểm câu “cái chảo”, không chỉ thử hai câu cuối.
4. Owner chọn asset/version. Không tự nhân bản cả bộ khi base chưa chấp nhận; đây là vòng thử theo mục tiêu chất lượng, không bỏ hạng mục QC.
5. Giao refs đã duyệt sang P7 shot plan. Motion và diễn payoff kiểm bằng take thật sau request được duyệt.

Request tạo mẫu sau intake phải ghi tool/model thực, prompt exact, ref được phép dùng, số output/lượt, credit/cap và stop condition. Hiện tất cả là PENDING; không có lệnh chạy. Trước khi upload/generate cần trình request cụ thể, không biến duyệt hướng38 thành quyền tiêu credit.

## 7. Tổng hợp vòng này

- Đã xác định/chốt: hướng hình, trang phục, giọng và Q0 theo approval38; nội dung C-v0.5 không đổi.
- Giả định: silhouette/màu/trang phục chi tiết, layout trái–phải, set bàn ăn; có thể sửa khi thấy mẫu, chưa là asset/canon lock.
- Còn mở: food appearance/rights intake, model/workflow tiếng, sample thực và approval mẫu; runtime PROD7 version review chưa được suy rộng từ approval hướng.
- Tiếp theo: hoàn tất intake/reference và soạn request mẫu cho owner duyệt; chưa tạo video toàn tập.
