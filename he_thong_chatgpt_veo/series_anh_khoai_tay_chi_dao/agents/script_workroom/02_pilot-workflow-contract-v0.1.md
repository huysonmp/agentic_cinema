# Phòng biên kịch agent P3–P5 — contract pilot v0.1

- **Status:** DESIGNED FROM OWNER DECISIONS; not yet executed or quality-validated.
- **Decision source:** `01_owner-decision-2026-09-30.md`.
- **Mục tiêu:** tìm, phân loại, phản biện và thử các kịch bản có khả năng giữ người xem, làm người xem nhớ món/nơi, thể hiện đúng sức sống của Khoai–Đào; không tối ưu số lượng bản thảo hay thay owner quyết định thẩm mỹ.

## 1. Input và thứ tự gate

1. P3 nhận P1 Bible đã duyệt và P2 claim/evidence pack **được owner duyệt**. Episode Brief phải xác định một audience moment, điều người xem cần nhớ, trọng tâm cảm xúc, 1–2 claim có thể dùng, điều không được ngụ ý và giới hạn 15–30 giây. Owner duyệt đúng version P3.
2. P4 chỉ từ brief đã duyệt mới tạo 5–7 concept; owner duyệt shortlist 2–3 concept để đi vào P5 test script. Một bản `NON-FINAL` có thể dùng cho paper exercise trước gate nhưng không được gắn nhãn P4 approved.
3. P5 viết, thử và so kịch bản trên shortlist; owner chọn bản để khóa. Timed read và previsualization thô là bằng chứng P5, không thay P7 shot package/P8 request.

## 2. Vai trò agent và sản phẩm cụ thể

| Vai trò | Input riêng | Hành động quan sát được | Output và điều không được làm |
|---|---|---|---|
| **Creative Explorers** — nhiều run/lens độc lập | Cùng brief + bible + claim boundary; không đọc concept của nhau ở lượt đầu | Tạo các cơ chế kể khác nhau: câu hỏi, xung lực nhân vật, hành động thấy được, chuyển biến, điểm nhớ. Tự chỉ ra vì sao hướng đó không chỉ là bản rewrite. | 5–7 concept cards có claim ID, hook/payoff, vai trò riêng của Khoai/Đào, điểm mới, rủi ro; không tự chọn concept thắng. |
| **Diversity Editor** | Toàn bộ concept cards | Gom trùng *cơ chế kể* và chỉ ra vùng ý tưởng chưa được khám phá; yêu cầu bổ sung khi 5–7 thẻ chỉ khác câu chữ. | Diversity map, loại trùng có lý do; không sửa âm thầm bản gốc. |
| **Audience-Pull Critic** | Concept/script đã ẩn tên tác giả | Tìm điểm mở khiến người xem muốn ở lại, mỗi nhịp bổ sung điều gì, payoff có trả lời lời hứa hay không; chỉ ra giây/beat yếu. | Chẩn đoán theo beat và A/B comparison; không tuyên bố đã đo retention thật. |
| **Dramaturgy Critic** | Concept/script | Kiểm nguyên nhân–hệ quả, thay đổi trạng thái, xung đột/khác biệt có ý nghĩa, setup–payoff và thừa lời. | Defect kịch tính + cách sửa ở đúng stage; không tự viết lại để tự chấm bản mình. |
| **Character Chemistry Critic** | P1 character canon + script | Kiểm Khoai/Đào có lựa chọn, động lực và tiếng nói riêng; đối đáp có làm câu chuyện/món mở ra, hay chỉ pha trò và chấm món. | Character defect theo câu/beat; không áp mẫu “Khoai luôn sai, Đào luôn đúng”. |
| **Script Writer / Script Doctor** | 2–3 concept shortlist + nhận xét reviewer | Viết timed scripts riêng theo từng concept; sửa bản được chọn theo defect cụ thể, giữ changelog và claim IDs. | Script versions, ước lượng/đo lời đọc, mapping audio–visual; không đổi fact hoặc brief ngầm. |
| **Cold Reader Proxy** | Chỉ script/animatic và câu hỏi đánh giá; không xem brief, intent hay lời giải thích của tác giả | Sau một lượt đọc/xem, nói lại món, nơi, điều nhớ, lúc mất chú ý, điều tưởng nhân vật muốn và câu nào gây hiểu sai. | Comprehension report có bằng chứng; đây là proxy AI, không là dữ liệu khán giả. |
| **Selection Synthesizer** | Toàn bộ bản, critique, timed read, storyboard, bất đồng | Lập so sánh cặp, các trade-off và lý do giữ/loại; phân biệt đủ điều kiện sản xuất với sức hấp dẫn tương đối. | Decision packet cho owner; không dùng tổng điểm/đa số phiếu để tự chọn. |

**Reviewer factual/canon độc lập:** Fact & Source Auditor P2 và claim-trace check P5 phải kiểm câu factual được chọn; các creative critic không được tự quyết claim đúng. Việc gọi các vai trò trên là *contract thiết kế*; chưa có prompt agent hoặc run thực tế cho P3–P5.

## 3. Vòng lặp và bằng chứng

`P3 brief approved → P4 5–7 concept cards → de-duplicate → 3 creative reviews độc lập → owner shortlist 2–3 → P5 timed scripts → blind/cold read + timed read + storyboard thô → reviewer so sánh cặp → Script Doctor sửa có mục tiêu → owner chọn/khóa hoặc route lỗi về P2/P3/P4/P5.`

Mỗi lần lặp phải giữ: input version, concept/script ID, rubric version, nhận xét nguyên văn, bản sửa thay đổi gì, điều vẫn yếu, disposition của owner. Không xóa bản thua: lý do loại là dữ liệu học cho P14. Giới hạn số vòng chưa được ấn định trước; dừng khi owner chấp nhận một bản, đổi premise upstream, hoặc nhận thấy vòng tiếp chỉ thay câu chữ mà không giải quyết defect.

## 4. Hai lớp đánh giá, không ép thành một điểm

**Đủ điều kiện (hard boundaries):** P1 fit; claim có nguồn/được phép dùng; không ngụ ý review món là mục tiêu duy nhất; nhân vật đúng canon; có thể hiểu trong 15–30 giây; không phụ thuộc hình/âm thanh không thể giải thích hoặc quyền asset chưa rõ. Không đạt thì sửa/route, không được thắng nhờ “rất vui”.

**Sức hút tương đối (so sánh A/B, kèm chứng cứ):** hook cụ thể; tò mò tiến triển qua từng beat; Khoai–Đào có khác biệt làm mở thêm ý nghĩa; có thay đổi hoặc khám phá; một điểm nhớ về món/nơi; lời và hình bổ trợ nhau; kết thúc có dư vị; không giống công thức cũ của series. Reviewer phải chỉ rõ beat/câu làm căn cứ và một điểm mà phương án thua vẫn làm tốt hơn. Chủ sở hữu được quyền chọn theo taste/risk khác recommendation, với rationale.

## 5. Bài thử tối thiểu trước script lock

- **Timed read:** đọc thoại ở nhịp dự kiến, cộng chỗ nghỉ/âm thanh; ghi thời lượng thực hoặc ước tính có phương pháp, không chỉ đếm chữ.
- **Silent pass:** từ storyboard thô, người xem còn nhận ra món/nơi và hành động kể chuyện gì khi tắt tiếng?
- **Audio-only pass:** nếu không nhìn hình, có hiểu diễn biến/nhân vật quá khác không? Không đòi mỗi kênh tự kể trọn câu chuyện, chỉ phát hiện lệch nghĩa.
- **Cold read:** kiểm nhớ món, nơi, một nét đặc trưng và điều giữa Khoai–Đào đã thay đổi; ghi hiểu nhầm, không coi proxy AI là người xem thật.
- **Pairwise review:** so hai script cùng độ hoàn thiện, đảo thứ tự trình bày để giảm thiên kiến vị trí; owner xem cả bất đồng, không nhận một điểm tổng hợp che trade-off.

## 6. Các giả thuyết cần kiểm chứng trong pilot

1. 5–7 concept có tạo đa dạng cơ chế kể thật hay chỉ là biến thể bề mặt? Kiểm bằng diversity map.
2. Reviewer độc lập có tìm ra defect khác nhau, hay đồng thuận giả vì cùng bible/model? So finding overlap và trường hợp bỏ sót.
3. Cold Reader Proxy có dự báo được điểm người thật hiểu nhầm hoặc nhớ sai không? Chưa thể kết luận trước một thử nghiệm với người thật.
4. Vòng Script Doctor có làm kịch bản tốt hơn theo đánh giá owner/độc giả mù, hay chỉ dài và trơn hơn? So bản trước–sau ẩn nhãn.
5. Có giữ được món/nơi làm trung tâm khi tăng chemistry không? Kiểm recall và claim trace; không lấy số câu thoại nhân vật làm proxy.

## 7. Việc chưa quyết định

- P2 owner gate và P3 brief cụ thể của EP01.
- Có mời người xem thử thật trước Veo hay sau bản rough cut; tiêu chí chọn mẫu và cách ghi consent/feedback.
- Có cần feasibility Veo probe cho một concept cụ thể hay không; chỉ quyết sau khi thấy rủi ro và có P8 request/cap được duyệt.
- Rubric chi tiết và prompt từng agent phải được thử trên script pilot rồi hiệu chỉnh; v0.1 này không phải SOP đã chứng minh hiệu quả.
