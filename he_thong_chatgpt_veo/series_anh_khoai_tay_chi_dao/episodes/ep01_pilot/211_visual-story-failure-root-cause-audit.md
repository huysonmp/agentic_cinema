# 211 — Kiểm nguyên nhân gốc: bản dựng mất nhân vật và nhịp kể

## Phạm vi và trạng thái

Owner phản hồi bản bàn giao: ghép cảnh không đạt, không thấy mặt người nói, quá nhiều hình món ăn; yêu cầu kiểm video thực tế và truy nguyên nhân. Phản hồi này được ghi nhận là **FAIL về kể chuyện bằng hình và thể hiện nhân vật đối với bản 210 hiện tại**. Không suy diễn toàn bộ nghiên cứu, tài nguyên hoặc các bài thử đều mất giá trị.

Đây là audit của root, không phải báo cáo của một agent phản biện độc lập mới. Không sửa bản dựng, không sinh media, không dùng credit, không sửa lịch sử approval. Các approval trước vẫn là lịch sử; chúng không thay thế kiểm chất lượng nghề nghiệp hoặc phủ định phản hồi hiện tại.

## Bản kiểm và cách kiểm

- File: `C:/Users/PC/Downloads/du_an_nem_bui/210_EP01_ban_giao_v1.1/EP01_30S_SUBTITLED_v1.1_FOR_APPROVAL.mp4`.
- SHA-256: `fdbdb10ea63a1889cf58819f1cc51cacd325c63dd7f52ca9999a90ffa79479c3`.
- 720 × 1280, 24 fps, 720 frame, thời lượng 30 giây.
- Đã trích toàn bộ 720 frame nguyên khung. Đã xem bảng 60 mẫu cách nhau 0,5 giây và 9 mẫu theo lượt thoại/phản ứng/kết; đối chiếu timeline 209-v0.5, prompt và hồ sơ các quyết định. Không tuyên bố đã xem thủ công cả 720 ảnh hoặc nghe/xem liên tục toàn bộ phim trong audit này.
- Phân loại theo cảnh, xác nhận qua ảnh lấy mẫu và yêu cầu bố cục trong prompt; không phải kết quả nhận diện mặt tự động trên từng frame.
- Công cụ tái lập: `scripts/audit_ep01_visual_story_failure.py`.
- Toàn bộ ảnh và số liệu: `C:/Users/PC/Downloads/du_an_nem_bui/211_visual_failure_audit/`.
- Bảng 60 mẫu: `full_30s_60_samples.png`; bảng lượt thoại: `seven_lines_and_only_faces.png`; số liệu: `audit-metrics.json`.

## Những gì bản dựng thực sự hiển thị

| Khoảng thời gian | Hình trong bản dựng | Tác động đối với câu chuyện |
|---|---|---|
| 0–4,167 giây | Bàn, món, tay; mặt hai người nằm ngoài khung | Không thiết lập rõ hai người đang giao tiếp |
| 4,167–12,167 giây | Một cận món liên tục 8 giây | Câu Khoai nhớ bếp nhà không có ánh mắt, nét mặt hoặc người nghe |
| 12,167–15,458 giây | Trở lại bàn và tay | Hai câu hỏi–đáp vẫn không có mặt người nói/nghe |
| 15,458–21,333 giây | Thân và tay Khoai gắp/giữ nem | Có thao tác nhưng thiếu ý định, ánh mắt và sự chuyển trạng thái khi bị bắt gặp |
| 21,333–21,958 giây | Mặt Đào phản ứng im lặng 0,625 giây | Phản ứng được giữ rất ngắn, không có đối ứng mặt Khoai |
| 21,958–28,500 giây | Thân, tay, bát và chuyển miếng nem | Ba lượt thoại kết không có mặt người nói; Đào nói nhưng hình vẫn là thân/tay Khoai |
| 28,500–30,000 giây | Hai gương mặt trong cảnh rộng, im lặng | Nhân vật xuất hiện đầy đủ quá muộn để gánh phần đối thoại |

Tổng theo phân loại cảnh: **27,875/30 giây (92,9%) không có gương mặt đầy đủ**; **15,458 giây (51,5%) là bàn/món/tay, không có mặt**. Mặt đầu tiên xuất hiện ở giây 21,333. Chỉ 2,125 giây có mặt đầy đủ, gồm phản ứng Đào và cảnh kết.

**7/7 lượt thoại không thấy mặt người đang nói.** Với N07, cue phụ đề kéo đến 28,503 giây, vượt mốc cảnh kết khoảng 0,003 giây; phần vượt này không được coi là một cảnh nhân vật nói có mặt.

Ví dụ đặc biệt rõ: N02 “Mùi này làm anh nhớ đến bếp nhà anh. Hồi bé, mẹ rang gạo, anh đứng chờ” được phủ bởi bàn/cận món; N05 “Chờ em quay lưng nữa à?” của Đào được phủ bởi thân và tay Khoai. Đây là sai lệch giữa nhiệm vụ kể chuyện của hình và thoại, không tự nó chứng minh giọng đã bị gán nhầm người.

## Chuỗi nguyên nhân có bằng chứng

### 1. Mục tiêu sáng tạo bị thay bằng mục tiêu tránh lỗi kỹ thuật — nguyên nhân chính

Hướng T2 trong `agents/directing_team/pilot_ep01/02_cinematography-contributions-r1.md` yêu cầu từ món chuyển điểm nhìn lên mặt Khoai, có khung hai người cho trao đổi, thấy mắt/mặt trong phát hiện và chữa cháy. Các báo cáo ACT và EDIT cũng yêu cầu giữ người kể, người nghe và quan hệ hành động.

Tại `197_completion-edit-plan-and-budget-proposal.md`, root đề xuất phương án A: đưa lời thoại ra ngoài khung, dùng món/tay hoặc phản ứng im lặng để tránh vấn đề khẩu hình. Đây là thay đổi phương thức kể chuyện, không chỉ thay công cụ thực hiện. Hồ sơ có nói rủi ro cận món 8 giây bị phẳng; rủi ro đó không được chuyển thành điều kiện chặn bản dựng.

Owner đã duyệt A tại 198. Trách nhiệm của root vẫn là giải thích đầy đủ mất mát sáng tạo, kiểm tổng thể và không trình một phương án kỹ thuật như thể đã giữ nguyên hiệu quả T2. Không quy lỗi cho approval của owner.

### 2. Prompt và ảnh đầu vào đã chủ động loại gương mặt

`evidence/209/prompt-U01-v0.1.txt` yêu cầu: “Both faces stay above the frame throughout”, đồng thời cấm mặt đi vào khung.

`evidence/209/prompt-U02-v0.1.txt` yêu cầu: “Both characters and all hands stay outside the composition.”

198 yêu cầu chuẩn bị tham chiếu cận bàn/tay cho U01/U02. 205 yêu cầu mặt Khoai ngoài khung U04. 208 loại phiên bản U01 có miệng Đào trong khung. Như vậy, cảnh không có người nói là kết quả phù hợp với đầu vào đã chọn; không có căn cứ đổ lỗi này cho việc Veo tự cắt mất mặt.

### 3. Ghép theo nhu cầu lấp thời lượng, không theo nhiệm vụ cảm xúc của từng câu

Tại `203_audio-join-approved-and-picture-production.md`, bốn lượt thoại đầu dài 14,055 giây. Root chọn U01 mở 4,1667 giây, U02 cận món 8 giây và U01 thêm 1,9167 giây để phủ đủ, không tạo thêm đơn vị U02.

Việc giữ âm thanh đúng và đủ thời lượng đã trở thành tiêu chí chính. Không có bằng chứng vòng đạo diễn hiện hành đánh giá câu ký ức cần mặt Khoai, người nghe cần phản ứng ở đâu, hoặc cận món có tạo thông tin mới qua từng nhịp không.

Timeline đặt đoạn thoại cuối bắt đầu ở 21,9583 giây; khoảng không có thoại ở giữa là 7,9033 giây. Khoảng này được thiết kế cho hành động, không phải âm thanh bị rơi do mux. Nhưng vì thiếu biểu cảm/đối ứng, chuỗi gắp lén → bị phát hiện → chữa cháy không được thể hiện rõ bằng hình.

### 4. Các cách xử lý cục bộ tích lũy nhưng không tái duyệt ý nghĩa toàn cảnh

205 rút phản ứng Đào từ 1,5 xuống 0,625 giây và chuyển 0,875 giây sang tay Khoai. 208 thay nhịp quay đầu bằng tay chạm cốc để tránh miệng lỗi. Cảnh kết đầy đủ hai mặt chỉ tới sau lời thoại.

Mỗi quyết định có lý do kỹ thuật và có các approval trong lịch sử. Tổng của chúng làm mất hệ thống diễn xuất: nhìn món → gợi ký ức → nghe nhau → nhìn thấy hành động → lúng túng → đáp lại. Không có điểm bắt buộc kiểm lại toàn bộ hệ thống này sau các thay đổi.

### 5. Vai chuyên môn có thiết kế và từng chạy trên giấy, nhưng không được vận hành như cổng kiểm bản phim cuối

`agents/directing_team/08_ep01-paper-pilot-run-log.md` ghi bốn vai DIR, DOP, ACT, EDIT, vòng tích hợp và phản biện độc lập đã chạy trên giấy ngày 2026-10-01. Không đúng nếu nói chưa từng có agent nào chạy.

Tuy nhiên các báo cáo đó không phải review bản media 209–210 và không tự chuyển sang phiên bản C-v0.6. `evidence/209/results.json` ghi `independent_agent_pass: false`; formal SIA chưa được tạo. Root chủ yếu kiểm ảnh mẫu về tay, món, khẩu hình và điểm nối; 210 kiểm thêm chữ và âm lượng. Không có báo cáo độc lập hiện hành chặn mất nhân vật/nhịp kể trên bản xuất này.

Vì vậy vấn đề không phải thiếu tên chức danh; là **không bắt buộc thực thi, bàn giao và đóng phát hiện trên đúng phiên bản video**.

### 6. Kiểm kỹ thuật được thực hiện, nhưng bị dùng thay cho kiểm chất lượng phim

`scripts/build_ep01_frame_bound_review.py` kiểm frame/range/hash/PCM; trạng thái lựa chọn chỉ cần bắt đầu bằng `ROOT_CANDIDATE`, không yêu cầu PASS đạo diễn/diễn xuất trên media. Các bước finishing giữ nguyên picture, kiểm gain, chữ và hash.

Đúng 720 frame, đủ 30 giây, không đổi giọng và chạy test thành công không chứng minh cảnh hấp dẫn hoặc đúng ý nghĩa. 209 trình bốn sai lệch đạo cụ/điểm nối nhưng không nêu vấn đề lớn hơn: 7/7 thoại không thấy mặt, 92,9% phim không có mặt đầy đủ. 210 thu hẹp yêu cầu owner kiểm vào phụ đề/âm lượng. Đây là lỗi chọn tiêu chí và trình duyệt của root.

## Kết luận, giới hạn và phần chưa kết luận

- Có bằng chứng mạnh rằng bản dựng làm đúng nhiều chỉ dẫn kỹ thuật nhưng sai mục tiêu kể chuyện của series. Root chịu trách nhiệm tích hợp và đề xuất phương án đó.
- “Ghép sai” ở đây xác nhận được ở cấp ngữ nghĩa và hiệu quả cảnh. Chưa có bằng chứng FFmpeg tự đảo thứ tự scene hoặc tự crop mặt trong bước xuất; timeline và prompt đã thiết kế các khung không mặt.
- Lời thoại ngoài khung không tự nó là lỗi. Lỗi là áp dụng gần như toàn bộ, thiếu cả mặt người nghe và biểu cảm đối ứng, trong câu chuyện dựa trên tính cách hai nhân vật.
- Không dùng audit này để kết luận Veo không làm được mặt/diễn xuất, hay giọng mới bị hoán đổi. Khả năng công cụ và danh tính âm thanh cần bằng chứng riêng nếu mở lại.
- Đây không phải thử nghiệm khán giả hoặc đo sức hút TikTok. Kết luận sáng tạo dựa trên đối chiếu mục đích cảnh với những gì thực sự hiện trong phim.

## Trạng thái sau vòng này và bước tiếp theo đề nghị

**Đã xác định:** bố cục thực tế, thoại–hình, thời lượng không mặt, chuỗi quyết định tạo ra lỗi và lỗ hổng vận hành vai chuyên môn.

**Quyết định lịch sử:** A/offscreen và các cách xử lý cục bộ từng được duyệt; không xóa hoặc viết lại approval cũ. **Phản hồi mới:** bản 210 hiện tại không đạt yêu cầu kể chuyện của owner; không tiếp tục coi là bản sẵn sàng bàn giao/phát hành.

**Giả định làm việc:** giữ kịch bản C-v0.6 và tài nguyên hiện có để phân tích; chưa có quyền đổi thoại, tạo media hoặc chi thêm credit trong lượt audit này.

**Còn mở:** lượng footage có mặt/diễn xuất đúng có thể tận dụng, phần cần thay và hiệu quả một dựng lại. Chưa hứa hoàn thành chỉ bằng các clip hiện có.

**Bước kế tiếp đề nghị, chưa thực hiện:** dựng lại bảng ý nghĩa từng nhịp gồm câu thoại, người nói/nghe, cảm xúc/hành động cần thấy và hình thực tế có; đối chiếu kho footage rồi trình các khoảng thiếu. DIR/DOP/ACT/EDIT cần review đúng bản dựng và ghi phát hiện có frame/timecode trước khi gọi là đạt. Không ưu tiên thêm agent hoặc tiếp tục finishing chỉ để giữ bản dựng hiện tại.
