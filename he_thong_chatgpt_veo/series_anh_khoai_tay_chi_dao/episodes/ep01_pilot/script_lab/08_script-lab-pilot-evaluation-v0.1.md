# EP01 Script Lab — kết quả pilot vòng 1

- **Status:** NON-FINAL / creative test complete; **NO SCRIPT READY FOR PRODUCTION**.
- **Run date:** 2026-09-30 (Asia/Saigon).
- **Input state:** P1 approved; P2 claim boundaries accepted nhưng pack gate pending; P3 brief chưa approved. Sandbox packet được dùng thay brief chỉ để thử agent, không mở gate.
- **Run trace by artifact:** `01` 8 concept từ ba Explorer, 7 chuyển review sau gom trùng; `02` ba critic độc lập; `03` ba test scripts; `04` cold-read mù; `05` script + claim/canon review; `06` Script Doctor S02 v0.2; `07` blind pair trước–sau. Các run là agent trong Codex, không phải workflow tự động/skill đóng gói.

## Kết quả kiểm contract

| Test | Kết quả | Evidence/giới hạn |
|---|---|---|
| 5–7 cơ chế kể độc lập | **PASS sơ bộ** | Tám concept được tạo độc lập; một cặp “quá gần/hai khung” trùng, giữ 7. C03/C07 và C05/C07 còn nguy cơ hội tụ khi viết thật. |
| Hai góc nhìn Khoai–Đào và món/nơi | **PARTIAL** | Concept cards có vai trò; S03 script để Hạ mở và kết, khiến cặp chính thành người cung cấp fact. S01/S02 làm món/nơi xuất hiện muộn. |
| Critic có defect cụ thể và bất đồng | **PASS** | Audience, Dramaturgy, Chemistry nêu beat và rủi ro khác nhau; bất đồng C01 vs C04 được giữ. Script critics độc lập bắt reveal muộn, payoff yếu, Hạ lấn vai, wording “từ Bùi Xá”. |
| Không tự duyệt/không biến AI proxy thành khán giả | **PASS** | Mọi bản ghi NON-FINAL; Cold Reader tự nhận là proxy và không tuyên bố retention. Không script nào được pass. |
| Ranh giới claim | **PARTIAL** | Không thấy F06/F07/F08 được đưa vào như fact. S03 “từ Bùi Xá” có thể ám chỉ hộp cụ thể từ đó, mạnh hơn F01; claim cuối vẫn cần source read-back P2. |
| Timed read / storyboard / người xem thật | **UNTESTED** | Các mốc 21–29s chỉ là writer estimate; chưa đọc thành tiếng, dựng animatic, hoặc thử khán giả. Không được biến thành PASS. |

## Kết quả vòng lặp Script Doctor

S02 v0.1 có bất đồng cận–toàn và hook hình lạ, nhưng reveal món ~13s, payoff giải thích thẳng và địa danh muộn. Doctor v0.2 đưa toàn món và F01 trước ~6s, cho Đào tự nhìn chi tiết, bỏ câu kết về kỹ thuật quay. Hai blind reviewer cùng chọn **v0.1 đáng xem hơn** và **v0.2 rõ món/nơi hơn**. Bản v0.2 giải defect cơ học nhưng bỏ luôn câu hỏi kéo xem; “Ăn nhé? — Khoan một nhịp” trở thành cớ để thuyết minh thính.

**Kết luận nhân quả ở mức giả thuyết:** vòng sửa đã làm rõ thông tin nhưng *có thể* giảm tension. Đây là phản ứng của hai AI reviewer trên chữ, không chứng minh người xem thật sẽ chọn v0.1. Nó đủ để không tự chọn v0.2 làm script production và đủ để điều chỉnh rubric: mỗi rewrite phải được so với bản trước về hook/agency/payoff, không chỉ chấm defect đã sửa.

## Decision packet cho owner — chưa chọn bản thắng

- **S01:** đường khám phá bằng cảm giác có tiềm năng, nhưng video không truyền mùi; logic “ngửi thấy → nhìn tay” chưa liền. Chưa ưu tiên script rewrite.
- **S02 v0.1:** khởi điểm có chemistry và visual mechanism tốt nhất theo Story Critic; cần rework ở **concept/beat** để cho món lộ sớm hơn mà vẫn giữ câu hỏi và xung đột. Không dùng v0.2 như bản sửa đã đạt.
- **S03:** tình huống và câu kết ấm, nhưng Hạ (nhân vật mới) tạo hook/payoff, Khoai–Đào mất trung tâm; “từ Bùi Xá” vượt mức an toàn cho hộp cụ thể. Chỉ tiếp tục nếu owner muốn thử khách thứ ba và viết lại agency của cặp chính.
- **C04 concept:** được Chemistry Critic thích vì có chuyển động quan hệ; Audience/Dramaturgy thấy trừu tượng. Có thể thử một beat/action paper test nếu S02 không cứu được, chưa viết script.

**Khuyến nghị quy trình:** Trả S02 về P4 để sửa cơ chế reveal chứ không lặp tiếp P5 wording; sau khi owner xem, chỉ đưa 1–2 hướng mạnh qua script rewrite. P2 evidence rework + owner gate và P3 approved brief vẫn là điều kiện trước P4/P5 production. Human taste và phản hồi người xem thật cần thiết để biết agent có đang chọn đúng “hấp dẫn” hay không.

## Tồn tại kỹ thuật/đánh giá

- Các agent được gọi thủ công theo contract và chia context; chưa có launcher, sandbox quyền ghi cưỡng chế, trace dashboard hay regression suite chạy tự động.
- Blind readers là cùng lớp công nghệ với writers; tách context giảm anchoring nhưng không bảo đảm sai số độc lập.
- Chưa kiểm được feasibility Google Flow/Veo, diễn xuất, voice, hình món, nhịp dựng và chất lượng audio; không suy từ script text thành video quality.
- Không thể gọi pilot này là bằng chứng cấu hình 5–7 concept tốt hơn một cấu hình khác; chưa có baseline đối chứng hoặc thử nghiệm người xem.
