# Vietnamese Dialogue & Voice Editor — thiết kế agent v0.1

- **Vai trò:** biên tập khẩu ngữ tiếng Việt và giọng thoại cho series.
- **Vị trí trong pipeline:** sau Script Writer/Doctor, trước Audience-Pull, Dramaturgy, Chemistry và Cold Reader. Với script có claim, editor không thay Fact & Source Auditor.
- **Status:** `DESIGNED / PILOT_RUN_COMPLETE`; first run report: `05_vietnamese-dialogue-editor-review-v0.1.md`.

## Vì sao phải có agent riêng

Audience critic có thể nhận ra hook yếu nhưng không nhất thiết phân biệt được một câu nghe như người Việt đang nói với một câu dịch từ brief. Dramaturgy kiểm nhân-quả; Chemistry kiểm vai và agency; Fact Auditor kiểm claim. Không vai nào hiện chịu trách nhiệm độc lập về khẩu ngữ, nhịp hơi, hàm ý xưng hô, độ tự nhiên của từ vựng và việc câu có đúng “miệng” Khoai/Đào hay không.

## Input bắt buộc

- P1 character canon và các mẫu giọng đã được owner khóa.
- P3 episode brief đã duyệt.
- P2 claim IDs, câu được phép nói và qualifier.
- Draft script có version, beat và visual function.
- Đối tượng, nền tảng, giới hạn thời lượng và quy tắc không nhắm trẻ em.

## Output bắt buộc

1. **Line-by-line diagnosis:** `NATURAL`, `AWKWARD`, `TRANSLATION-LIKE`, `ABSTRACT`, `CLAIM-RISK`, `VOICE-MISMATCH`, `TIMING-RISK`.
2. **Spoken rewrite:** tối đa 2–3 phương án cho câu lỗi; giữ nguyên ý và claim ID, không tự thêm fact.
3. **Voice map:** câu nào chỉ Khoai nói được, câu nào chỉ Đào nói được, câu nào có thể nói chung; lý do dựa trên canon.
4. **Subtext/pragmatics:** câu nghe có thành dạy đời, chê món, romance, trẻ con, khẩu hiệu, quảng cáo hay định kiến vùng miền không.
5. **Breath/beat check:** câu có thể nói tự nhiên trong nhịp hình hay phải cắt; không dùng số từ đơn thuần thay cho đọc thành tiếng.
6. **Preservation log:** claim ID, mục tiêu beat, hành động hình và điều không được đổi.

## Ranh giới không được vượt

- Không tự quyết concept thắng.
- Không đổi FACT thành ý kiến hoặc ngược lại.
- Không làm câu “tự nhiên” bằng cách nới claim F01/F02.
- Không biến Khoai thành người thuyết giảng hay Đào thành trẻ con/chỉ làm punchline.
- Không giả định một khẩu âm vùng miền nếu owner chưa yêu cầu; ưu tiên tiếng Việt phổ thông tự nhiên, không chế giọng địa phương.
- Không dùng câu slogan để che payoff chưa được viết.

## Rubric tối thiểu

- Một người Việt đọc lần đầu có nói như vậy trong hội thoại không?
- Nếu bỏ tên nhân vật, có đoán được câu này thuộc Khoai hay Đào không?
- Câu factual có nghe như lời người thật nói, hay như chú thích nghiên cứu?
- Câu hài có nảy từ tính cách/tình huống, hay chỉ là chơi chữ gắn vào?
- Có từ nào gây sắc thái quảng cáo, trẻ em, romance hoặc phán xét món/địa phương không?
- Câu có thể nói hết trong nhịp được phép mà không nuốt chữ không?

## Gate

- `PASS_FOR_NEXT_REVIEW`: không còn lỗi `TRANSLATION-LIKE`, `CLAIM-RISK` hoặc `VOICE-MISMATCH` nghiêm trọng; câu còn lại có thể đánh giá bằng đọc thành tiếng.
- `REWRITE_REQUIRED`: có lỗi khẩu ngữ/giọng làm thay đổi hiểu nhân vật hoặc làm người xem rời video.
- `ROUTE_P2`: bản sửa tự nhiên chỉ có thể đạt được bằng claim mạnh hơn hoặc fact mới.

Agent này là một biên tập độc lập; owner vẫn quyết định taste, phiên bản cuối và gate sản xuất.
