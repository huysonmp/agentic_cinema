# AG-CONT-01 — REC218-CONT-R1

## Quan sát lạnh, ghi trước khi đọc 178/214/217

Đã xem thực OPEN v0.7, sáu frame N02 0071/0072/0163/0164/0200/0201 và năm contact sheet A02/A03/R02/R01/U08_NATIVE bằng công cụ xem ảnh. Chưa đọc script, maker, RCA hoặc reviewer khác khi ghi phần này. Đây là so sánh hình, không phải kiểm playback.

Reference-state quan sát từ `T2-CODEX-OPEN_v0.7.png`: Khoai bên trái, thân/đầu vàng nâu lốm đốm, lông mày đậm, áo khoác tối trên sơ mi sáng; Đào bên phải, đầu hồng có lá, áo sáng, phần váy xanh và đai hồng. Bàn có đĩa món sáng màu dạng sợi/miếng nhỏ ở giữa, đĩa lá bên trái, hai bát nhỏ có các miếng đỏ, hai bát cá nhân đang trống, hai đôi đũa và một cốc trong bên phải. Không thấy nhánh lá đặt trên đỉnh món. Không suy loài lá, thành phần món hay loại đồ chấm từ màu/hình; OPEN là đối tượng chẩn đoán, chưa tự coi là canon món.

N02 0071 giữ bố cục hai người và phần lớn cấu hình bàn; 0072 chuyển sang cận Khoai. 0163 cận Khoai, chỉ còn một phần Đào; 0164 chuyển hẳn sang cận đĩa món, giữ đĩa lá ở trái, một bát có miếng đỏ phía sau, một bát trống phía trên và đôi đũa chéo ở sau. 0200 vẫn cận món; 0201 trở lại hai người. Crop loại nhân vật/cốc khỏi khung và làm đĩa đổi độ elip là hệ quả góc chiếu, không đủ chứng minh đạo cụ bị xóa. Hai frame cận món có nhánh lá xanh trên đỉnh và một bát lớn ở mép phải chứa chất lỏng hổ phách; hai trạng thái này không thấy tương ứng trên bàn wide 0071/0201. Nguồn/hành động giải thích chưa biết, nên ghi khác biệt cần kiểm thay vì gán tên thực phẩm.

A02 và R01 giữ bộ bàn gần với OPEN trong các ô đã xem; nhân vật vẫn nhận ra được. A03 có bàn trống ngoài đĩa giữa ở cả các ô wide: không thấy hai bát cá nhân, hai đôi đũa, cốc, đĩa lá và hai bát có miếng đỏ; vì vùng bàn tương ứng hiện rõ, không thể giải thích tất cả chỉ bằng crop. Món A03 có các đoạn lớn, ít cảm giác sợi mảnh hơn A02; chưa có food sheet để kết luận sai món. R02 cho thấy Khoai cầm đũa hướng lên miệng và Đào chạm/nâng cốc qua các mẫu. U08 cho thấy Khoai gắp từ đĩa chung, Đào cầm bát có phần món; các ô cuối có phần món treo trên đũa. Contact sheet không chứng minh đủ diễn tiến giữa các mẫu.

## Input, authority và capability thực tế

Ngày 2026-10-06; rubric `TIER1-RUNTIME-v0.1`, vai AG-CONT-01; P7/P10 recovery, recommendation G1/G2/G3. Đã đọc đầy đủ contract `agents/quality_system/02_runtime-contract-and-stage-map-v0.1.md` và `03_tier1-role-prompts-v0.1.md`; sau quan sát lạnh mới đọc `178_owner-dialogue-amendment-c-v0.6.md`, `214_recovery-storyboard-r1-and-acceptance.md`, `217_recovery-tier4-runtime-gates-and-questions.md`. Các tên tài liệu episode tính từ `episodes/ep01_pilot/`; ảnh tính từ `C:/Users/PC/Downloads/du_an_nem_bui/`. OPEN nằm tại root; frame nằm dưới `216_n02_face_coverage_check/all_240_frames/`; các sheet nằm dưới `215_recovery_asset_screening/`.

Owner 217-A/A/A cho phép role local độc lập; 214 duyệt storyboard chữ; 178 khóa C-v0.6. Không chọn clip thay owner hoặc đổi món/kịch bản. Không đọc 211/215/216.md, maker218, RCA hoặc reviewer R1 khác; không dùng browser/API, generation, credit, install hoặc git.

Capability chỉ `PAPER_REVIEW + SAMPLED_FRAMES`: xem 12 ảnh, gồm 6 frame đơn và 5 sheet, cộng OPEN; không mở native video/playback/âm thanh. SHA-256 native N02 v200 do dispatch cung cấp là `72cbaf7d9f66932002dfce1b1a57fa464935c315e84e54ae094fe29aa805a153`, **chưa tự hash bytes hoặc xác minh lineage frame→native**. Nhãn thời gian trên sheet là tọa độ ảnh cung cấp, không phải phép đo playback của reviewer. Thiếu approved character multi-angle/allowed variation và authoritative food-fidelity sheet trong allowlist. Food fidelity vì vậy `UNKNOWN`, OPEN v0.7 không tự trở thành canon.

## Coverage sau đối chiếu ý đồ

| Kiểm | Status trong scope | Bằng chứng và giới hạn |
|---|---|---|
| CONT-1 identity, outfit | MET ở mẫu nhìn thấy; canon đầy đủ UNKNOWN | Khoai/Đào còn nhận diện được trong N02, A02/A03/R01/R02/U08; không thấy đổi outfit trọng yếu. Mặt cận/vẻ biểu cảm khác không tự là identity drift. |
| CONT-2 food fidelity | UNKNOWN | Màu/cấu trúc A03, nhánh lá và bát ở N02 cần food sheet; không đủ nguồn kết luận đúng/sai Nem Bùi. |
| CONT-3 trạng thái bàn/miếng A–B | DEFECT cho đề xuất nối A03 vào bộ bàn A02/R01; temporal NOT_TESTED | Chênh bộ đạo cụ hiện rõ; sheets R02/U08 chỉ gợi ý hoạt động, không chứng minh F0→F4 và B. |
| CONT-4 camera/style/joins | UNKNOWN ngoài mẫu | Trái Khoai/phải Đào giữ trong wide; N02 gần→món→wide có thay cảnh. Perspective/crop chấp nhận được về nguyên tắc, axis/eyeline và chuyển động qua cut chưa kiểm. |
| CONT-5 sửa có truy vết | MET ở report | Mỗi finding dưới có source, route và closure; chưa có evidence đóng lỗi. |
| Món nguội, không khói | MET chỉ tại mẫu | Không thấy luồng khói ở ảnh đã xem. Không chứng nhận nhiệt độ hay toàn take không khói. |

214 yêu cầu N02/F0 giữ mặt Khoai, không phủ cả lượt bằng món; 0072/0163 cho thấy mặt, 0164/0200 là món. Chưa map lời→frame nên timing UNKNOWN. 178/214 khóa chưa chạm miệng trước chuyển A, nhận rồi thả, sau đó gắp B; U08 không đủ xác định A/B.

## Findings và điều kiện đóng

| ID / severity / status | Expected → observed, evidence | Impact, route và closure |
|---|---|---|
| CONT-R1-01 / MAJOR / OPEN-DEFECT | Cùng bữa ăn cần match đạo cụ trước/sau shot. A03 mọi ô wide chỉ còn đĩa giữa, khác A02/R01 và OPEN với bát, đũa, cốc, đĩa lá, bát có miếng đỏ. | Nếu nối như trạng thái bàn liên tục, đạo cụ biến mất không có action. P7/EDIT xác định range; P6 xác nhận gói bàn. Đóng bằng reference approved và đầu/cuối shot/chuỗi liên tục cùng version cho thấy match hoặc biến đổi đã được owner duyệt. |
| CONT-R1-02 / MAJOR tiềm tàng / UNKNOWN-HOLD | N02 F0 không tự thêm món/đạo cụ. 0164/0200 thấy nhánh lá trên đỉnh và bát hổ phách; 0071/0201 không thấy trạng thái tương ứng. | Chưa biết là vật thêm, bát cá nhân đổi nội dung hoặc góc khác của cấu hình approved. Không gọi phần bị crop là bị xóa. P6/FOOD xác minh layout; P7/EDIT kiểm source/range. Đóng bằng food/table sheet và frame đủ góc qua hai cut, không chỉ giải thích bằng văn bản. |
| CONT-R1-03 / MAJOR gate gap / NOT_TESTED-HOLD | 214 đòi một đường A: gắp về miệng→khựng→đổi hướng→thả vào bát→gắp B. R02 sheet ô 0,666667 s gần miệng; U08 ô 0 s đã có món trong bát Đào, ô 4–7,333333 s còn phần treo trên đũa. | Không thể chứng minh không contact/không nhân đôi/reset, hoặc gọi phần treo là B. Đây là thiếu kiểm transition, không kết luận video vi phạm. P7/EDIT/CONT-G3 cần source ranges và playback liên tục; đóng bằng chứng A vào bát đúng một lần và B chỉ sau F4. |
| CONT-R1-04 / MAJOR gate gap / UNKNOWN-HOLD | 217 yêu cầu đúng version, đủ input. Food sheet/allowed variation/lineage native chưa xác minh. | Không cấp food/temporal/full-film PASS. Root cung cấp input approved và map/hash; kiểm lại đúng target, không đổi canon để hợp output. |

Không có finding quyền sử dụng: scope này không kiểm RIGHTS và không đưa bảo đảm rights.

## Disposition và tổng hợp giao lại

| Asset | Recommendation đúng task |
|---|---|
| A02, R01 | KEEP_CANDIDATE cho bố cục/identity/bộ bàn tại mẫu; owner chưa chọn, timing/food/AV còn mở. |
| A03 | REWORK đề xuất sử dụng trong chuỗi cùng bàn do chênh đạo cụ; chưa kết luận sai chủng loại món. |
| N02 v200 | HOLD continuity toàn take/G2; mặt Khoai tại 0072/0163 có thể giữ làm candidate coverage, chưa chọn range. |
| R02, U08_NATIVE | HOLD chuỗi A–B/G3; KEEP_CANDIDATE cho kiểm tiếp action, không coi sheet là chứng minh transfer. |

Status tổng: `REWORK` cho nối A03; `HOLD` cho food/temporal/whole-sequence. Không `PASS_FOR_NEXT_GATE`, không xác nhận action, full AV, phim đã hoàn thành hoặc release.

1. **Đã xác định:** identity nhìn thấy còn nhận ra; A03 chênh bộ bàn; N02 macro có hai trạng thái cần giải thích bằng nguồn.
2. **Quyết định đã chốt:** 178 C-v0.6, 214 R01–R09/F0–F4/A–B, 217-A/A/A; reviewer không bổ sung quyết định owner.
3. **Giả định làm việc:** cùng bàn/same meal theo 214; chỉ so OPEN như chẩn đoán. Crop/đổi góc không mặc nhiên là mất vật.
4. **Còn mở:** approved food/table/variation, native lineage, contact miệng, hành trình A/B, eyeline/axis qua join và line-to-frame N02.
5. **Bước tiếp:** root/EDIT map range–hash–F-state và cung cấp food sheet; CONT kiểm continuous visual đúng cut/version tại G2/G3. Nếu cần đổi canon/món/cách dùng, trình P6 và owner; không tự sửa hoặc chọn clip.
