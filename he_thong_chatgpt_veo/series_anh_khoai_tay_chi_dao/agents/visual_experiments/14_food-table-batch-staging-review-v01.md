# CONT — TABLE-BATCH01-STAGING/2026-10-01/MEDIA_REVIEW

Run: 2026-10-01; role AG-CONT-01 + AP-v0.1; P6; MEDIA_REVIEW. Reviewer context độc lập. Report v0.1.

## Cold observation — ghi trước khi đọc script32

Media thực mở bằng local image viewer: `C:/Users/PC/Downloads/du_an_nem_bui/T-NB-02A_v0.1.jpg`, `T-NB-02B_v0.1.jpg`, `T-NB-02C_v0.1.jpg`. Chỉ xem still; không có nhân vật/tay, không có video.

| Candidate | Vật thực thấy / count | Geometry, crop, chỗ ngồi | Nền / residue |
|---|---|---|---|
| 02A v0.1 | 1 đĩa món giữa với sợi vàng và miếng nâu; 1 đĩa lá/râu rau phía sau trái; 2 bát rỗng; 2 chén đỏ; 2 đôi đũa, mỗi đôi thấy hai thanh; 1 cốc nước bên phải | Bàn chữ nhật nhìn chéo từ phía trước. Hai ghế đẩu ở cạnh gần: trái bị crop, ghế trước-phải phần chân bị crop. Đồ ăn/chén/bát/đũa/cốc đều nằm trong ảnh. Đèn phía trên bị crop chụp. Không thấy mặt bàn xuyên vật hoặc chân ghế nối lỗi rõ | Tường sáng bên phải, cửa/vỉa hè bên trái, ánh vàng. Dấu hình sao trắng góc dưới-phải |
| 02B v0.1 | 1 đĩa món giữa; 1 đĩa lá phía sau-trái; 2 bát rỗng; 2 chén đỏ; 2 đôi đũa, mỗi đôi thấy hai thanh; 1 cốc nước bên phải; 2 kê đũa nhỏ | Hai ghế đẩu cạnh gần, trái bị crop; ghế trước-phải lớn hơn do phối cảnh, bị crop phần chân. Hai bộ bát/đũa phân bố trái và phải dọc cạnh gần. Tất cả bộ phục vụ trong ảnh. Bàn/chân/đũa không có collision rõ | Cửa/vỉa hè/đường ở trái, xe/người mờ ngoài cửa; tường và đèn sáng. Hai dấu hình sao trắng vùng dưới-phải |
| 02C v0.1 | 1 đĩa món giữa; 1 đĩa lá phía sau-trái; 2 bát rỗng; 2 chén đỏ (chén phải có hoa văn); 2 đôi đũa, mỗi đôi thấy hai thanh; 1 cốc nước bên phải | Hai ghế đẩu cạnh gần, ghế trái bị crop; ghế trước-phải thấy mặt và phần chân. Đĩa món, bát, chén, cốc không bị crop. Bàn có vân gỗ thô, nhìn chéo; không thấy collision rõ | Tường ở trái, cửa/vỉa hè/xe mờ ở phải. Dấu hình sao xám-trắng góc dưới-phải |

Cold limits: ghế trống không xác nhận ai ngồi đâu. Hai vị trí cạnh gần có thể dùng cho hai người cạnh nhau nhưng chưa xác nhận screen-left/right khi ghép nhân vật. Không có tay: AP-1 anatomy/side, AP-3 grip supports, AP-4 hand scale/forearm N/A. Đũa nằm trên bàn, AP-2 chỉ kiểm được số/thanh nhìn thấy; không kiểm grip. AP-5 contact gắp N/A. AP-6 motion NOT_TESTED. Chưa đối chiếu identity hoặc food canon.

## Đối chiếu sau cold observation

Đã đọc sau cold: `episodes/ep01_pilot/32_p5-script-c-v0.5-approved-content.md` (C-v0.5, OWNER_CONTENT_APPROVED). Đã đọc trước cold: full Tier1 common contract02, CONT section Tier1 prompts03, full VEXP runtime02 và owner approval01. Invariants/bộ phục vụ nhận qua dispatch: Khoai trái, Đào phải, ngồi cạnh nhau; cốc ở ngoài phải Đào; nem giữa, đĩa lá sau, hai bát nhận, hai chén tương ớt riêng, hai đôi đũa, một cốc nước; quán nhỏ ven phố chiều tối; không text/logo/biển hiệu. Approval01 xác thực quyền chạy reviewer, không phải asset approval; staging serving-set approval là record trong dispatch, không có thêm file owner lock trong allowlist.

Không đọc: maker prompt/log, root QC, report reviewer khác, episodes69–73. Không dùng browser/Flow/generation/upload/Git. Không có approved food visual ref/food-fidelity notes, character composite, shot plan hoặc state-transition media. Vì vậy đây là static table-staging review, không phải continuity pass toàn clip hoặc full P6 asset approval.

**Status:** `PASS_WITH_ACTIONS` cho kiểm đếm/geometry của bàn trống trong scope này; `HOLD` cho promotion thành reference hoàn chỉnh dùng cho diễn xuất. Điều status không xác nhận: fidelity Nem Bùi, identity, posture/reach, đổi hướng nem trước miệng, đặt vào bát, motion hoặc temporal joins. Owner vẫn chọn candidate và duyệt asset.

## Coverage

| Check | Rule | Result | Evidence / limitation |
|---|---|---|---|
| CONT-T01 | Bộ phục vụ đủ count | MET A/B/C | Mỗi ảnh có một đĩa món, một đĩa lá, hai bát rỗng, hai chén đỏ riêng, hai đôi đũa, một cốc. B có thêm hai kê đũa; C chén phải hoa văn. Đây là accessory/appearance variation, không làm thay count |
| CONT-T02 | Nem giữa / lá phía sau | MET về placement A/B/C | Đĩa món ở giữa vùng bộ phục vụ; đĩa lá nằm xa camera hơn. Food identity UNKNOWN, không gán sợi vàng là thính đã xác thực |
| CONT-T03 | Hai người cạnh nhau, Khoai trái Đào phải | UNKNOWN final; geometry có hỗ trợ | Hai ghế dọc cạnh gần, không bố trí rõ đối diện hai phía bàn. Ghế trái crop trong cả ba ảnh; chưa có nhân vật để xác thực screen order/seat width |
| CONT-T04 | Cốc bên ngoài phải Đào | MET ở static prop layout; reach UNKNOWN | Cốc ở ngoài phải bộ bát/đũa phải trong A/B/C. Có thể đặt Đào ở vị trí phải nhưng chưa thấy tay/thân/quay lấy cốc |
| CONT-T05 | Bát Đào nhận món từ Khoai | UNKNOWN performance | Bát phải rỗng, miệng bát không bị crop; có khoảng trống giữa hai bộ. Không có tay/bát được đưa ra nên không chứng minh đường chuyển nem |
| CONT-T06 | Geometry/crop đủ đọc | MET tabletop A/B/C | Không mất bộ phục vụ vì crop; hai thanh mỗi đôi đũa đọc được. Crop ghế/đèn không thành defect bàn trống, nhưng không kiểm toàn thân nhân vật |
| CONT-T07 | Quán nhỏ ven phố, chiều tối | MET visual cues; exact time UNKNOWN | Bàn gỗ/ghế đẩu, cửa sát vỉa hè, ánh đèn vàng; B/C có đường và xe mờ. Không xác nhận giờ từ still |
| CONT-T08 | Không text/logo/biển hiệu | MET phần chữ/biển hiệu đọc được; residue DEFECT | Không thấy chữ đọc được hoặc biển hiệu; có dấu sao trắng/xám góc dưới-phải cả ba ảnh (finding TST-01). Không kết luận nguồn/quyền từ dấu này |
| CONT-1 | Identity | N/A | Không có nhân vật trong media |
| CONT-2 | Food fidelity | UNKNOWN | Không cấp primary food ref/allowed variation; shape/color thực thấy ghi ở cold table |
| CONT-3 / CONT-4 | Temporal/object state và joins | NOT_TESTED | Ba variation still riêng, không phải ba frame liên tiếp; không có transition/video |
| AP-1 / AP-3 / AP-4 | Anatomy, functional grip, hand scale | N/A | Không có tay/thân người |
| AP-2 | Stick count/continuity | MET static visible count | Hai thanh tách được mỗi đôi trong A/B/C; không chứng minh grip/upper-lower support |
| AP-5 / AP-6 | Contact/gravity transfer và motion | N/A contact; NOT_TESTED motion | Không có gắp/chuyển thức ăn |

## Findings

| ID | Severity / type | Artifact / region | Expected → observed / impact | Disposition / route | Closure evidence |
|---|---|---|---|---|---|
| TST-01 | MINOR DEFECT | 02A/02B/02C v0.1; góc dưới-phải cạnh/chân bàn | Reference sạch residue → dấu hình sao nhìn thấy; B có hai dấu, A/C một dấu rõ. Nếu nhập nguyên ảnh sẽ mang residue vào reference/background | REWORK before clean-reference promotion; P6 operator/ART. Không chặn owner xem bố cục hiện tại; không coi dấu là logo nhãn hàng đã xác định | Actual local clean revision được mở lại; vùng góc sạch, không crop mất vật/geometry trọng yếu; trace version mới |
| TST-02 | UNKNOWN trọng yếu, không phải defect đã xác định | 02A/02B/02C v0.1; đĩa món trung tâm | Cần Nem Bùi theo approved primary → chỉ quan sát được sợi vàng/miếng nâu, chưa có primary/invariants để đối chiếu. Không có căn cứ gọi món đúng hoặc sai | HOLD food-fidelity approval; P6 CONT food comparison. Owner không cần chọn cuối ở report này | Cấp approved food reference + allowed variation/notes; reviewer so vùng đĩa trên revision định dùng |
| TST-03 | UNKNOWN trọng yếu cho action, không phải defect bàn trống | 02A/02B/02C v0.1; hai ghế, bát phải và cốc ngoài-phải | Script32 cần Đào quay lấy cốc, Khoai đổi hướng trước miệng rồi đặt nem vào bát cô đưa ra → không có nhân vật/action. Khoảng trống bàn chỉ cho thấy khả năng bố trí, không chứng minh physical reach | HOLD action-readiness; P6 character placement → P7 action states. Không yêu cầu generation mới ngoài authority | Composite/blocking có Khoai trái Đào phải; xác thực turn/reach/cốc; start/near-mouth-before-contact/redirect/bowl-receive states; video mới kiểm continuity theo thời gian |

## Disposition

| Candidate | Static table disposition | Full reference / performance disposition | Lý do |
|---|---|---|---|
| 02A v0.1 | KEEP_FOR_OWNER_REVIEW | HOLD; clean residue action | Count/layout đọc được. Nền cửa phía trái, tường nhiều khoảng trống; không xem đó là ưu/nhược appeal. Food và nhân vật/action chưa kiểm |
| 02B v0.1 | KEEP_FOR_OWNER_REVIEW | HOLD; clean residue action | Count/layout đọc được; kê đũa là thêm prop nhỏ cần lock nếu chọn. Nền đường phía trái. Food và nhân vật/action chưa kiểm |
| 02C v0.1 | KEEP_FOR_OWNER_REVIEW | HOLD; clean residue action | Count/layout đọc được; chén phải hoa văn và cửa ở phải khác A/B, cần lock nếu chọn. Food và nhân vật/action chưa kiểm |

Không xếp hạng sức hút hoặc chọn cuối thay owner. Ba ảnh là alternatives cùng brief; đổi background trái/phải giữa alternatives không bị gọi là join lỗi vì chưa có sequence approved. Khi chọn một ảnh, vị trí cửa, chén, kê đũa và vân bàn của ảnh đó cần giữ nhất quán ở shot phụ thuộc.

## Handoff

- Đã xác định: cả ba đủ bộ phục vụ và cốc ở ngoài phải bộ vị trí phải; tabletop không bị crop vật cần dùng; có residue ở dưới-phải.
- Quyết định owner hiện có: reviewer workflow được approval01; script32 nội dung đã duyệt; dispatch truyền staging serving-set/seat invariants. Chưa có owner asset selection trong run này.
- Giả định: hai ghế cạnh gần là hai vị trí intended; người bên phải sẽ là Đào. Đây là giả định layout, chưa phải character placement đã xác thực.
- Còn mở: primary food fidelity; frame với nhân vật; turn/reach/chuyển nem; clean revision; chọn candidate và lock variation.
- Bước tiếp theo: owner xem ba bố cục với limits này; trên candidate owner chọn, operator chuẩn bị revision sạch và P6 placement theo quyền hiện có, cấp food primary cho CONT. P7 phải kiểm action states; chỉ video/transition đúng version mới có thể đóng temporal findings. Không promote full P6 hoặc mở video gate từ report bàn trống này.
