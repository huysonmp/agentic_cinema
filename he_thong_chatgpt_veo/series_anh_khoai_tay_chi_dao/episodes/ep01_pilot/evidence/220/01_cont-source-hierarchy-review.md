# CONT — REC220-CONT-SOURCE-HIERARCHY-R1

## Quan sát riêng trước hồ sơ authority và root proposal

Ngày 2026-10-06. Xem trực tiếp chín ảnh bằng view_image: TABLE08, PAIR03, OPEN7, hai ảnh owner folder và bốn frame N02 0163/0164/0200/0201. Chưa đọc proposal của root hoặc maker report khác. Đây là ảnh tĩnh, không playback.

- TABLE08: Khoai trái, Đào phải, bàn trước mặt; hai bát cá nhân trống, hai đôi đũa, một cốc trong bên phải, hai bát nhỏ có vật đỏ, đĩa lá riêng bên trái, đĩa món chung giữa bàn. Món là một khối nhỏ khá gọn, có sợi/miếng ngắn và lớp phủ hạt mịn, không thấy nhánh lá cắm trên đỉnh. Khung rộng thấy chân/ghế và khá nhiều không gian quán.
- PAIR03: hai nhân vật đứng toàn thân trên nền trơn. Khoai đầu vàng nâu có đốm, mày đậm, áo khoác tối/sơ mi sáng/quần tối; Đào đầu hồng có lá, sơ mi sáng/váy xanh/đai hồng. Không có bàn hay món để làm chuẩn serving-state.
- OPEN7: mặt/đầu hai nhân vật lớn hơn trong khung, vẫn outfit tương ứng. Bộ vật trên bàn tương tự TABLE08; đĩa món có mound rộng hơn, sáng hơn, nhiều sợi dài/miếng nhạt lộ rõ; lá nằm đĩa riêng. Không thấy nhánh lá trên đỉnh. Đèn lồng, độ nét bề mặt, tỷ lệ nhân vật/bàn khác TABLE08; khác bố cục/góc/tỷ lệ không tự là thêm/bớt đạo cụ.
- `nembui.jpg`: ảnh chụp thực đĩa trắng, khối món gọn có miếng phẳng và sợi ngắn phủ hạt mịn; lá bản rộng xếp quanh món cùng các vật đỏ. Không có bát/cốc/đũa hoặc hai nhân vật của cảnh.
- `z7750931050074_6fa76793489e54e476846aad4d233684_806643377.jpg`: ảnh chụp thực món rời trong khay tròn, lá lót dưới và nhiều lá/sợi xanh bên cạnh; khối sợi/miếng nhạt vàng có lớp phủ. Một số món khác hiện ở mép ảnh, không suy là được phép đưa vào EP01.
- N02 0163: cận Khoai, bát cá nhân trước anh trống, một phần Đào bên phải. 0164/0200: cận món nhiều sợi dài khá đều, các miếng phẳng tập trung một bên; có nhánh lá nhỏ trên đỉnh, bát chất lỏng hổ phách ở mép phải, bát trống phía trên, bát nhỏ có vật đỏ phía sau, đĩa lá ở trái. 0201: trở lại hai nhân vật, hai bát cá nhân trống, mound không thấy nhánh lá trên đỉnh; hai bát nhỏ/cốc/đũa/đĩa lá như bộ wide. Crop cận loại người/cốc khỏi khung không chứng minh chúng bị xóa; nhánh lá đỉnh và nội dung bát lại là khác biệt trạng thái không được giải thích chỉ bằng crop.

Không định danh loài lá, thành phần/chủng loại đồ chấm hoặc recipe bằng hình. Các mô tả trên chỉ là shape/color/serving-state, chưa gán ảnh nào là canon.

## Input/capability và authority thực đọc

Vai AG-CONT-01, rubric `TIER1-RUNTIME-v0.1`, G1 source hierarchy cho gói N02; quyền bounded local theo 217-A/A/A. Contract02/03, 178/C-v0.6, 214/storyboard R1 và 217 đã đọc đầy đủ ở vòng REC218 trong cùng context. Vòng này đọc đầy đủ 78, 101, 109, 111, 114, 115 trong `episodes/ep01_pilot/`; 114/115 chỉ dùng xác định giới hạn diagnostic, không đọc ảnh tài khoản/preflight hoặc report độc lập được link trong111. Không đọc root proposal, maker report mới hoặc report reviewer khác. Phần observation đã ghi vào file trước khi đọc sáu hồ sơ này. Nội dung maker/history chứa ngay trong109/111 được đọc vì đó là nguồn authority được cấp, không dùng lời maker để chứng nhận chất lượng.

Các ảnh đã xem, đường dẫn chính xác:

| ID | Actual path |
|---|---|
| TABLE08 | `D:/Workspace/agentic_cinema/he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/media/raw/ep01_p6_food/T-NB-03_v0.8.jpg` |
| PAIR03 | `D:/Workspace/agentic_cinema/he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/media/raw/ep01_p6_character_base/EP01_P6_PAIR_CONCEPT_v0.3.jpg` |
| OPEN7 | `C:/Users/PC/Downloads/du_an_nem_bui/T2-CODEX-OPEN_v0.7.png` |
| REAL1 | `C:/Users/PC/Downloads/du_an_nem_bui/nembui.jpg` |
| REAL2 | `C:/Users/PC/Downloads/du_an_nem_bui/z7750931050074_6fa76793489e54e476846aad4d233684_806643377.jpg` |
| N02 samples | `C:/Users/PC/Downloads/du_an_nem_bui/216_n02_face_coverage_check/all_240_frames/frame-0163.jpg`, `frame-0164.jpg`, `frame-0200.jpg`, `frame-0201.jpg` cùng thư mục |

Get-FileHash SHA256 trên bytes thực của năm source: TABLE08 `AEB6DFAEE1773109243F9F952235A44F2417C6FB7FB4FAF15BE61C34CA40D924`; PAIR03 `ECFBE7A3C543730C268A77CA08D508147115CA804154F85EBDBB38C5C601E8C7`; OPEN7 `A3D80F09BFB7242BAE3007AD7B4F37473BB2F0ED019A84CC4956C4D32A8DBF9A`; REAL1 `A51303F7100EDD0944DC00DAA19402FECFE24BB0E15A4143DA8F8EAE7B9E3A2D`. Bốn giá trị khớp hồ sơ78/101/109/115. REAL2 `1237956E99458385F95F1EDF18E0A98E1BDDB777030AC1D69FAB05FA7A51D741`, không có hash/selection record đối chiếu trong sáu hồ sơ. Chưa tự xác minh native N02 hash hoặc lineage frame→native ở vòng này.

Scope `PAPER_REVIEW / SAMPLED_FRAMES / SOURCE_HIERARCHY`; không continuous visual/full AV, không recipe/rights certification. Không sinh, browser, spend, git, sửa tài liệu cũ hoặc chọn clip thay owner.

## Source hierarchy: quyền cụ thể của từng ảnh

| Nguồn | Authority và chức năng | Disposition G1 |
|---|---|---|
| TABLE08 | 78 decision locks1–3 chọn exact v0.8 làm bàn trước hành động, spatial geography, bộ phục vụ, warm light và ụ nem gọn. 78 không xác nhận công thức/khẩu phần; camera/crop được đề xuất, dời props/quan hệ phải ghi khác biệt. | `USE_AS_APPROVED_STATIC_BASELINE`; không thu hồi78. Đây là chuẩn serving-state khi đối chiếu N02/F0. |
| PAIR03 | 101 dẫn approval45: mặt/thân/outfit, không lấy nền studio/tư thế đứng. 78 giữ primary nhân vật v0.3. Không đọc45 lần này nên chuỗi approval dựa trên78/101, chưa independently read-back45. | `USE_FOR_IDENTITY_COMPARISON`; không đủ chuẩn món/bàn/động tác. |
| REAL1 | 109 xác nhận ảnh thật owner đã duyệt để hỗ trợ texture; dải/lát mỏng hiện hữu. 109 cấm chuyển lá trang trí/vật đỏ/đĩa/nền sang bàn và giữ TABLE08. | `TEXTURE_SUPPORT_ONLY`; không thay serving geography hay recipe. |
| REAL2 | Có trong allowlist mới và đã xem/hash thực; sáu hồ sơ không chỉ định nó là ref production hoặc permitted transfer. | `DIAGNOSTIC_SUPPORT`; chỉ so shape/texture. Không chuyển toàn khay, lá, món mép ảnh sang EP01. |
| OPEN7 | 109/111 giữ candidate, yêu cầu source hierarchy/owner selection; không đổi TABLE08/PAIR03. 114 duyệt method/preflight, không input/spend. 115 nói rõ diagnostic-only, không production canon; nội dung file vẫn pending exact execution. | `KEEP_DIAGNOSTIC_CANDIDATE`; đủ ảnh để truy rendition/margin của N02, chưa approved production anchor. Không tự suy quyền thử mới từ115. |

Thứ tự này phân theo thuộc tính, không chọn một ảnh thắng tất cả: identity theo PAIR03; serving/không gian theo TABLE08; texture có REAL1 hỗ trợ; OPEN7 là derivative candidate phải đối soát cả ba. 178 thay script v0.5 của78 bằng v0.6 nhưng không ghi thay bàn/món; 214 tiếp tục F0→F0 cho N02 và món nguội/không khói.

## Comparison, findings và closure

| ID / severity / status | Expected và observed | Route / bằng chứng đóng |
|---|---|---|
| SH-01 / MAJOR / `UNKNOWN-HOLD` production anchor | OPEN7 giữ số nhóm phục vụ của TABLE08, nhưng mound lớn/rộng hơn và rendition sáng, sợi dài hơn; mặt/nền/quy mô framing cũng rerender. 109/111 chưa owner chọn nguồn này làm anchor production. Crop khác có thể được đề xuất; exact food/identity correspondence chưa được duyệt. | P6 + owner chốt có tiếp nhận **những khác biệt cụ thể** của OPEN7 hay quay về baseline78. Cần approval exact image/hash và scope allowed variation; không dùng tên file hoặc diagnostic approval thay selection. |
| SH-02 / MAJOR / `DEFECT_IN_PROPOSED_SERVING_USE` | TABLE08/OPEN7/F0 không có nhánh lá đỉnh và không có bát lớn chứa chất lỏng hổ phách. N02 0164/0200 có cả hai; 0163 bát Khoai trống, 0201 hai bát trống và không thấy nhánh lá đỉnh. Khác biệt trạng thái so chuẩn đã duyệt quan sát được; chưa biết bát mép phải là thêm mới hay bát cũ đổi nội dung. | P7/EDIT giữ finding mở nếu sử dụng insert này; P6/FOOD đối chiếu layout. Đóng bằng source/range sửa có serving-state match và kiểm lại cùng version, hoặc owner duyệt thay đổi được nêu rõ. Không tự thêm canon để hợp footage. |
| SH-03 / MAJOR tiềm tàng / `UNKNOWN` food rendition | Món cận N02 nhiều sợi dài khá đều; TABLE08 mound gọn, REAL1/REAL2 có dải/lát và sợi độ dài/độ dày khác nhau. Không được nói “fine strands” là recipe fact; khác TABLE08 không chứng minh món thật sai. | Food/static specialist và owner chốt allowed rendition theo ảnh đã có nếu đưa macro vào production. Cần closeup approved hoặc chú giải visual bounds tối thiểu; recipe vẫn ngoài scope. |
| SH-04 / MAJOR gate gap / `NOT_TESTED-HOLD` temporal | Bốn ảnh biên cut đủ chẩn đoán trạng thái, không đủ giải thích các thay đổi xảy ra lúc nào hoặc chứng minh contact/action/AV. Cận bỏ mặt/cốc vì crop không tự là xóa vật; đĩa đổi elip không tự là drift. | EDIT map exact native hash/range/F-state; CONT kiểm liên tục nếu muốn kết luận continuity N02. G1 paper không đóng G2/G3/G4 hoặc AV. |

CONT-1: identity vẫn nhận ra ở mẫu, outfit/screen side tương ứng PAIR03/TABLE08; chưa exact multi-angle pass. CONT-2: authority serving đã rõ hơn vòng218, có thể xác định deviation SH-02; recipe/absolute fidelity vẫn UNKNOWN. CONT-3/4: static boundary comparison thực hiện, transition/axis/eyeline toàn chuỗi NOT_TESTED. CONT-5: repairs có route và closure, chưa finding nào đóng bằng media mới. Không thấy khói tại bốn mẫu; đó không đo nhiệt độ hay xác nhận toàn take.

## Recommendation và input/approval tối thiểu

`REVIEW_COMPLETE_FOR_STATIC_SOURCE_HIERARCHY`; `HOLD_FOR_PRODUCTION_N02`. TABLE08 tiếp tục là baseline approved; OPEN7 `KEEP_DIAGNOSTIC_CANDIDATE`; native dish insert `REWORK` nếu đề xuất dùng như F0 phục vụ đã khóa, vì SH-02; không tự chọn một source/cut thay owner. Không `PASS_FOR_NEXT_GATE` whole-media, recipe hoặc rights.

Tối thiểu trước gói N02 production: root trình một sheet đối chiếu TABLE08↔OPEN7 ghi rõ variation về mound/rendition/identity/framing và exact hash, để owner chọn scope anchor, giữ78 trừ phần được sửa rõ. Không cần hỏi lại approval78. Nếu chỉ chẩn đoán lỗi hiện hữu, có thể tiếp tục dùng bộ ảnh hiện tại read-only, chưa cần production selection. Nếu giữ insert native có serving-state khác, phải owner duyệt rõ nhánh lá/nội dung bát hoặc có phiên bản sửa match; không xem acceptance OPEN7 là acceptance các chi tiết mới của native. Ngoài quyết định nguồn, cần native source-map/hash/range và continuous visual checkpoint để đóng temporal; input tĩnh không thay checkpoint đó.

1. **Đã xác định:** exact sources/hash; TABLE08 có authority serving; OPEN7 candidate; insert native lệch serving-state ở mẫu.
2. **Đã chốt:** approval78 còn nguyên, identity hierarchy theo78/101, texture scope109; C-v0.6/178 và F0/R02 của214 giữ.
3. **Giả định:** N02 thuộc cùng bữa ăn/F0; REAL2 chỉ hỗ trợ diagnostic vì chưa có selection record.
4. **Còn mở:** variation production của OPEN7, allowed closeup rendition, nội dung/bowl identity trong insert, native lineage và transition/AV.
5. **Tiếp theo:** root read-back report, trình quyết định anchor có ảnh/hash/diff; EDIT chuẩn bị source map. Kiểm lại serving/static sau lựa chọn và transition đúng version, không sinh hoặc chi từ báo cáo này.
