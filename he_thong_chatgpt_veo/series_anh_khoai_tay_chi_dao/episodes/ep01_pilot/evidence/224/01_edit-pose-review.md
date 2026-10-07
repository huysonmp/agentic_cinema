# REC224-EDIT-POSE-QC — Review độc lập bốn pose mở EP01

Ngày: 2026-10-07, Asia/Saigon. Reviewer EDIT, scope **ACTUAL_STILL_IMAGE_REVIEW + HASH_VERIFICATION**. Review output do root chạy trên Flow, không tự duyệt source-map maker223. **REVIEW_COMPLETE trong scope ảnh tĩnh; REWORK/HOLD theo từng pose, không full G1 hoặc media PASS.** Chưa chọn output thay owner.

## 1. Input, authority và capability thực

Đã đọc đầy đủ `evidence/224/native-output-manifest.json`, `evidence/224/owner-approval.json` và bốn exact prompts trong `evidence/223/`: `REF01-S.prompt-DRAFT.txt`, `REF01-M.prompt-DRAFT.txt`, `REF01-E.prompt-DRAFT.txt`, `REF03-S.prompt-DRAFT.txt`. Owner duyệt tối đa bốn ảnh, một attempt/ảnh, cap0 credit và source upload exact B frame175; approval chạy **không là output acceptance**, không video/voice/retry/paid/release. Manifest ghi bốn submissions, không retry, balance77→77 và không có billing receipt; reviewer không kiểm UI/billing mới hoặc suy số dư hiện tại.

Đã xem ảnh thực toàn kích thước bằng local `view_image`, không chỉ thumbnail:

- Anchor: `C:/Users/PC/Downloads/du_an_nem_bui/223_g1_source_frames/ANCHOR_B/frame-0175.jpg`.
- Bốn repo natives tại `D:/Workspace/agentic_cinema/he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/episodes/ep01_pilot/media/224_g1_opening_refs_v01/`: `REF01-S_v01_NATIVE.jpg`, `REF01-M_v01_NATIVE.jpg`, `REF01-E_v01_NATIVE.jpg`, `REF03-S_v01_NATIVE.jpg`.

PowerShell đọc JSON/text và Get-FileHash SHA-256 trực tiếp trên anchor, cả repo/owner copies và bốn prompt files. Các hash đều khớp manifest; owner/repo bytes giống nhau. Dimensions768×1376/JPEG của bốn outputs là metadata trong manifest, không probe mới của reviewer. Không sửa native, không chạy generation/retry/browser/paid/git, không đổi script/story hoặc tạo replacement prompts. Chỉ viết report này qua apply_patch.

| Input | SHA-256 trực tiếp |
|---|---|
|B frame175 |`5bec51d789cebc8b891b26c70d4c52a4a2185ed18b34d0fb933ab6e1cab8c6c5` |
|REF01-S native |`eba9a13c86f359df458022a5a54664264e5bb29fcca08d6181454cb1ee482422` |
|REF01-M native |`bd48acb3223c417a22918a9d717cb0e1f5f22e118b8584fd2609581f3460f037` |
|REF01-E native |`887f00f0f78ea093529825b108b16d04a63c541b2b637281c7ebb4a52782c6c4` |
|REF03-S native |`4a4c4a9ae0dcd017b44a3e7b59b775577cbe7184594994f674526b93f915962e` |
|REF01-S prompt |`09ab77326cfa1d6c6d85836a44212a215759254cd71fb148ddc7f63b15618451` |
|REF01-M prompt |`38c160d65b4ba1e88e967dee84b2382de1242a29c4114bbf2122718e9bbc0fda` |
|REF01-E prompt |`c434ac94c16f7c6b2d341507fedbe68eaa833425e861f88cb5435989da92e6d4` |
|REF03-S prompt |`dd338deadd66412fc5c1ff638c39cf4cf91d7d12043ce6a22d77678a34490a29` |

Không nghe audio, không xem continuous motion/full AV. B frame175 tương ứng native175/24=7,291667s; đó là timestamp nguồn của một still, **không speech-end hoặc motion-start đã xác minh**. Anchor đã được duyệt về variation; chưa phải approved pose đầu N01, đầu B hoặc đầu R03. Bốn ảnh mới không bao phủ toàn chín nhiệm vụ R01–R09.

## 2. Expected → observed và scope dùng được

Nhìn chung, bốn ảnh giữ Khoai trái/Đào phải; mặt, mắt, miệng và tay liên quan đọc được; trang phục Khoai áo khoác sẫm/áo sáng, Đào áo sáng/nơ hồng, nền quán và ánh sáng ấm gần anchor. Hai người nhìn món hoặc nhìn nhau, không hướng thẳng tới camera để thuyết trình. Không thấy food/chopsticks/cốc đang được cầm; hai bát cá nhân trống trong bốn ảnh. Rau trước-trái, hai đĩa chấm, đũa nghỉ và cốc ngoài phải Đào còn thấy; không thấy khói/khói hơi hay chữ thoại mới. Đây là quan sát đúng bốn still, không continuity toàn hành động hoặc food/identity audit đầy đủ.

| Ảnh / expected theo exact prompt | Observed trên native | Dùng được / không dùng được / disposition |
|---|---|---|
|**REF01-S** — trước vươn tay; Đào nhìn Khoai với tò mò/trêu nhẹ; Khoai chú ý món và cô; cả hai môi khép, tay nghỉ |Đào nhìn trái về Khoai, môi khép/nét cười nhẹ; Khoai mắt hạ về vùng bàn, môi khép nhưng ít nét cười hơn B frame175. Hai tay mỗi người nghỉ gần bát, không cầm đạo cụ |**CANDIDATE_FOR_OWNER_POSE_REVIEW** cho F0 trước hành động và bố cục. Gaze của Khoai hỗ trợ chú ý món. Nét khá nghiêm có thể đọc là đang nghĩ hoặc dè dặt; chưa đủ kết luận đúng cảm xúc liên tục. Không dùng làm bằng chứng N01 đã nói hoặc cô đã định kéo |
|**REF01-M** — chỉ một tay cô vươn tới mép gần-phải đĩa, ngón vừa tới rim; đĩa chưa dịch; tay kia gần bát; Khoai nhận ra/đổi chú ý, môi khép |Một tay Đào ở phía trong vươn xuống rõ; tay còn lại nghỉ gần bát/cốc. Cô nhìn Khoai, Khoai nhìn cô; môi hai người khép. Đầu ngón vươn nằm sát vùng mép sau/trên của đĩa và bị món/mép che một phần; không đọc rõ riêng rim gần-phải như prompt |**HOLD_FOR_GESTURE_TARGET**. Dùng để thảo luận ý “cô sắp lấy đĩa/anh chú ý” và cấu trúc một tay, chưa duyệt làm intermediate anchor rõ đích. Không khẳng định ngón đang chạm/gắp món; occlusion làm đích vươn mờ. Một still không chứng minh đĩa chưa từng dịch hoặc không merged hand khi chuyển động |
|**REF01-E** — sau dừng ý định vươn, hai tay trở về nghỉ; Khoai chuẩn bị chia sẻ/Đào nghe; cả hai môi khép |Tay hai người về gần bát, không còn vươn; đĩa/bộ bàn vẫn ở bố cục tương tự S. Khoai nhìn Đào/nét cười, **miệng hé mở**; Đào nhìn anh, **môi hé mở**, chân mày cao hơn pose S |**REWORK_POSE** cho settled closed-mouth exit. Hand-rest silhouette hữu ích để so tail→B, nhưng không đạt trạng thái môi của exact pose. Không gọi cô đang nói ké hoặc hai người đang nói đồng thời từ một ảnh. Không dùng ảnh này để chứng minh stop đã được quay |
|**REF03-S** — đầu R03 sau ký ức; Đào tò mò thật; Khoai nhìn cô/cười kín, không cười khoe trước camera; hai môi khép, tay nghỉ, chưa lấy cốc/gắp |Khoai nhìn cô, cười nhỏ/môi khép; Đào nhìn Khoai, mắt mở/nét tò mò và **môi hé mở**. Tay nghỉ gần bát, cốc/đũa chưa cầm, bát trống |**REWORK_CLOSED_MOUTH_POSE**, giữ useful scope cho private-smile/gaze/F0 reference. Không chứng minh Đào đã nói N03 hoặc khẩu hình đúng câu. Nét tò mò đọc được trong still nhưng “vừa nảy câu hỏi”/nghe hết ký ức là inference cần chuỗi thực |

M có một tay vươn và một tay nghỉ, khác rõ S/E/REF03-S về silhouette. Điều đó có giá trị trong storyboard ảnh, nhưng đích đầu ngón cần rõ hơn để không bị hiểu là với món thay vì định kéo đĩa. Không đo plate displacement bằng pixel trong run; quan sát bố cục tương tự không thay phép kiểm chuyển động. S và REF03-S khác nhau về gaze/nét mặt; không tuyên bố độ tinh tế ấy chắc đọc được khi xem video nhỏ hoặc ở nhịp30s.

## 3. Potential cut continuity với B và giữa các poses

B frame175 có hai mặt nhìn nhau, môi khép/nét cười nhỏ, tay nghỉ và F0. Bốn ảnh mới là phái sinh có frame lớn hơn; mặt/ụ món/nền được dựng lại gần hơn và có khác biệt chi tiết/scale. Không nhận chúng là pixel-exact match hoặc bằng chứng nối không jump. Không áp thời điểm7,291667s thành destination time hay approved speech endpoint.

- **S→M:** việc một tay rời vùng bát và vươn về đĩa đọc được từ hai endpoints; cần kiểm đường tay thật, rim target, đĩa không dịch sớm, gaze Khoai nhận ra và miệng khi thoại. Các ảnh chưa chứng minh cause/timing.
- **M→E:** tay trở về nghỉ ở E là useful tail state; chưa chứng minh dừng vì “Khoan” hoặc hành động không teleport. E có hai môi hé, nên chưa là exact closed-mouth settled reference; không tự đổi yêu cầu pose sang speaking để hợp thức hóa.
- **E→B:** left/right, tay nghỉ, bát và cốc cho điểm tựa so hình. Gaze và shape miệng/nét mặt khác B frame175 có thể tạo jump nếu dùng như endpoints trực tiếp. Đích nối actual B phải xét frame/range thực được chọn và linked audio, không mặc định frame175 là đầu lời. Đây là potential continuity check, chưa cut-safety PASS.
- **B→REF03-S:** Khoai cười kín/nhìn cô tương đối phù hợp ý kết ký ức rồi câu hỏi; tay nghỉ/F0 giữ trên still. Môi Đào hé trái yêu cầu pre-question môi khép. Actual tail B→head R03 và thứ tự người nói/nghe cần motion/AV; không dùng N03 text làm heard evidence.

Ảnh pose khép miệng là ràng buộc reference, không quy định nhân vật phải giữ miệng khép trong video có thoại. Ngược lại, ảnh hé miệng không chứng minh đang nói đúng/sai speaker. Review này giữ hai tiêu chí riêng: pose compliance và actual speaking performance chưa kiểm.

## 4. Findings và closure

| ID / rule / status / severity | Expected / observed / impact | Action, route và closure |
|---|---|---|
|POSE224-F01 / source integrity / MET / MINOR tracking |Anchor, bốn prompt và native owner/repo hashes khớp manifest |Root giữ exact artifacts/hashes. MET chỉ integrity, không bù pose defects |
|POSE224-F02 / S restrained attention / UNKNOWN về sắc thái / MINOR |Expected thoughtful attention/gently teasing; S có gaze xuống món và tò mò của Đào nhưng Khoai khá nghiêm so B |ACT/PERF/owner xem đúng S trong packet. Có thể giữ candidate nếu sắc thái được chấp nhận; không bắt buộc thêm nét cười bằng suy đoán. Closure là disposition pose đúng artifact, motion vẫn riêng |
|POSE224-F03 / M fingertip-rim target / UNKNOWN / MAJOR gate cho intermediate pose |Expected rim gần-phải/just approaching; ngón tại mép sau/trên bị món/mép che, gesture endpoint chưa rõ |HOLD selection cho pose M. Root/ACT/EDIT kiểm đích/tay bằng artifact rõ hơn hoặc owner disposition có phạm vi. Không kết luận chắc chạm món; không retry tự động hoặc tạo prompt mới trong run này |
|POSE224-F04 / E closed-mouth exit / DEFECT / MAJOR |Exact prompt yêu cầu hai môi khép; native E có miệng Khoai và môi Đào hé mở, làm reference state lệch |REWORK exact pose hoặc owner chấp nhận exception minh bạch. Closure bằng artifact/hash được review lại đúng trạng thái; hand-rest useful không tự đóng mouth defect |
|POSE224-F05 / REF03-S closed-mouth pre-question / DEFECT / MAJOR |Expected cả hai môi khép; Khoai khép/cười kín nhưng Đào hé môi |REWORK pose reference hoặc scoped owner exception. Không suy wrong speaker/lipsync từ still; closure exact pose/hash và review |
|POSE224-F06 / action/cut/AV meaning / UNKNOWN / MAJOR gate khi chuyển media |Không có filmed pull→stop, actual listening, speaking attribution, lipsync hoặc fullscene ở bốn ảnh |Sau pose selection cần motion/AV evidence đúng target/hash và checkpoints. Không closed finding bằng storyboard đẹp/metadata; không G1 toàn tập PASS |

Không có CRITICAL lỗi được xác nhận trong phạm vi ảnh này; các MAJOR đủ để chưa duyệt cả bộ đúng exact closed-mouth/rim requirements. Four-image generation approval không là quyền chạy lại. Nếu root thấy cần sửa tiếp, đưa findings cụ thể vào gói trình; report này không tạo replacement prompts hoặc authority mới.

## 5. Handoff năm mục

1. **Đã xác định:** source/prompt/copy hashes khớp; S có F0 môi khép/tay nghỉ; M có one-hand reach nhưng rim target mờ; E và REF03-S có môi hé ngoài yêu cầu pose. Gaze giữa hai người đọc được, không camera-facing presentation.
2. **Quyết định đã chốt:** kế thừa owner chạy bốn ảnh đúng scope. Reviewer không chọn/approve output hoặc đổi script; B vẫn visual anchor, chưa là motion-start/speech-end riêng từ frame175.
3. **Giả định đang dùng:** judgments cảm xúc là interpretation của still; occluded fingertip chưa biết contact; bộ ảnh là reference candidates, không filmed action hoặc dialogue evidence.
4. **Còn mở:** owner/role disposition S và M; correction/exception E/REF03-S; pose-to-motion continuity, N01 pull–Khoan–stop, N03 actual speaking/listening và toàn chín beats. Chưa nghe/fullAV hoặc full G1.
5. **Bước tiếp:** root tích hợp review độc lập, giữ S làm candidate; HOLD M cho đích vươn; REWORK E/REF03-S ở closed-mouth criterion. Chỉ trình bounded sửa/exception khi cần; không generation/retry tự động. Nghiệm thu pose rồi mới kiểm media/join thực theo quyền riêng.
