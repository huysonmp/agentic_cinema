# Quyết định chọn cặp giọng — Khoai K20 / Đào D06

Ngày ghi nhận: 2026-10-02. Người duyệt: OWNER.

## Quyết định đã chốt

Owner xác nhận trước đó “K20 — Orus đầu danh sách” và lần này “Aoede tuỳ chỉnh chốt nhé”. Aoede trong bộ nữ 151 là duy nhất D06; không cần hỏi lại để phân biệt.

| Nhân vật | Mẫu được chọn | Tên actual trong Flow | ID preset |
|---|---|---|---|
| Anh Khoai | K20 — Ấm chắc, vụng về đáng mến | Orus tuỳ chỉnh | fb1188da-e6c8-4156-9bba-0576c01a8da6 |
| Chị Đào | D06 — Thoáng, duyên đời thường | Aoede tuỳ chỉnh | 0ce1551e-e74b-481c-bb9e-d31e04f8b352 |

Trạng thái: **VOICE_PAIR_SELECTION_APPROVED**. Đây là lựa chọn giọng của owner sau vòng nghe audition, không chỉ đề xuất của root. Không gọi là production/integration PASS. Không tự diễn giải approval thành điểm chấm accent hoặc mọi biểu cảm đã đạt.

## Nguồn đầu vào giữ nguyên

- K20: sample và common performance từ 148, performance riêng và ID từ [149](149_ten-more-voice-auditions.md); approval phân biệt K20/K12 tại [150](150_k20-selection-and-dao-voice-auditions.md).
- D06: sample và common performance từ [150](150_k20-selection-and-dao-voice-auditions.md), performance riêng và ID từ [151](151_ten-more-dao-voice-auditions.md).
- Không thay K20 bằng K12 hoặc Orus nền. Không thay D06 bằng Aoede nền chưa tùy chỉnh. Tên nền đủ cho nhận diện trong vòng hiện tại nhưng ID/performance mới là liên kết nguồn để dùng tiếp.
- Hướng miền Bắc/Hà Nội và nữ trưởng thành giữ theo audition. Không đổi nhân vật, quan hệ, thoại tập hoặc tạo giọng dựa người thật.
- Các preset khác giữ nguyên lịch sử, không xóa hoặc tự coi owner đã loại riêng từng mẫu.

## Phạm vi lượt này

Ghi quyết định vào tài liệu, cập nhật trạng thái và commit/push theo chỉ dẫn lưu trữ hiện hành. Không chạy generation mới, không tiêu credit, không tự đổi model/route, không sửa compose hoặc preset Flow. ID ở đây đối chiếu tài liệu actual đã readback ở vòng trước, không xác nhận live lại trong lượt chỉ ghi approval này.

## Còn phải kiểm trước đầu ra production

1. Hai giọng trong một đoạn đối thoại: không nhầm người nói, có tương phản và nghe tự nhiên trong tình huống đã duyệt.
2. Lời dài hơn preview 120 ký tự, đổi cảm xúc và độ ổn định qua nhiều lượt; giữ giọng Bắc và đúng nhân vật.
3. Khả năng dùng đúng preset trong route video actual, nhịp/lip-sync, thời lượng, tải và ghép. Không suy việc preset lưu được trong Flow chứng minh Veo giữ được voice.
4. Trình thông số route, đoạn thoại, tiêu chí và credit theo quyền hiện hành trước thử tích hợp; quy tắc ba Lite dùng cho video test, không tự thay bằng một preview.

## Tổng kết vòng

Đã xác định: owner chọn Aoede D06 cho Đào. Đã chốt: cặp giọng Khoai K20 / Đào D06. Giả định làm việc: giữ nguyên preset/performance được chọn, dùng làm baseline thử tiếp. Còn mở: nghiệm thu cặp thoại và tích hợp video, không phải chọn thêm giọng. Bước tiếp đề xuất: chuẩn bị phép thử đối thoại dùng hai ID trên, với route/settings và gate rõ; chưa thực thi trong lượt approval này.
