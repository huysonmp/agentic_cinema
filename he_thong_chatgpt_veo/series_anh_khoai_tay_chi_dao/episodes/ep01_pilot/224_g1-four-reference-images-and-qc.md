# 224 — Bốn ảnh tham chiếu mở cảnh và kiểm chất lượng

Ngày: 2026-10-07. Giai đoạn: P7 khắc phục / hoàn thiện G1. **Đã tạo và tải đủ bốn ảnh; chưa duyệt toàn bộ đầu ra, chưa tạo video hoặc đóng G1.**

## 1. Quyền và thực thi

Owner trả lời “ok” cho đề xuất tại 223: REF01-S, REF01-M, REF01-E và REF03-S, mỗi ảnh một lượt/x1, trần tổng 0 credit, dùng cùng frame175 của N02 B. Approval thực thi không là nghiệm thu ảnh hoặc quyền retry/video/voice/Quality. Xem [approval](evidence/224/owner-approval.json).

Đã kiểm trực tiếp trước từng lần gửi: chế độ Hình ảnh, Nano Banana 2.1, 9:16, x1, Tác nhân tắt, một ảnh nguồn đúng, prompt đã duyệt, báo giá 0 credit. Model UI hiện hành là 2.1, không tiếp tục dùng nhãn 2 cũ để mô tả lượt này. Đã gửi đúng bốn lần, không gửi lại.

Số dư quan sát trước và sau vẫn 77 credit. Không có hóa đơn để đối chiếu; kết luận giới hạn ở quote 0 và số dư không đổi. Đã tải cả bốn ảnh bằng lựa chọn **1K kích thước gốc**, thực tế 768 × 1376 JPG. Đây là tỷ lệ gần 9:16, không phải export TikTok chính xác 1080 × 1920.

Ảnh nguồn, prompt nguyên văn, UUID output, hash, bằng chứng UI và đối soát ba bản sao được lưu trong [manifest](evidence/224/native-output-manifest.json). Script kiểm decode và prompt trong cả preflight/output chạy thành công. Download event hết thời gian nhưng file thực tế đã tải; không sinh lại để xử lý lỗi tín hiệu tải. Xem [nhật ký và bài học công cụ](evidence/224/execution-log.md).

## 2. Bộ ảnh để xem

Thứ tự bảng: trên-trái S, trên-phải M, dưới-trái E, dưới-phải REF03-S. Bảng chỉ thu nhỏ toàn ảnh để so sánh; không chỉnh gương mặt, tay, món hoặc xóa watermark. Native được giữ riêng.

![Bốn ứng viên, chưa được duyệt](C:/Users/PC/Downloads/du_an_nem_bui/224_g1_opening_refs_v01/REC224_FOUR_CANDIDATES_NOT_APPROVED.png)

Ảnh gốc và hồ sơ cho owner: [folder REC224](C:/Users/PC/Downloads/du_an_nem_bui/224_g1_opening_refs_v01).

![Bằng chứng bốn ảnh trên Flow](D:/Workspace/agentic_cinema/he_thong_chatgpt_veo/series_anh_khoai_tay_chi_dao/episodes/ep01_pilot/evidence/224/four-images-flow-grid.png)

## 3. Kết quả kiểm và ranh giới

Root đã xem B frame175 và đủ bốn ảnh native. Hai reviewer đã thực xem ảnh và đối soát hash độc lập; [báo cáo EDIT](evidence/224/01_edit-pose-review.md) và [báo cáo CONT](evidence/224/02_cont-image-review.md). Root đã đọc đầy đủ cả hai báo cáo; cùng kết luận S là ứng viên, E/REF03-S cần sửa miệng. Với M, EDIT ghi HOLD do đích tay chưa rõ, CONT ghi REWORK/HOLD vì chưa đúng vành gần-phải; root chọn sửa tay trước khi chọn làm reference. Không diễn giải sự khác nhau về nhãn thành đã duyệt M. [Root read-back](evidence/224/03_root-image-readback.md) không thay review độc lập.

| Ảnh | Điều dùng được | Điều chưa đạt | Trạng thái |
|---|---|---|---|
| REF01-S | Môi khép, tay nghỉ, F0; Đào chú ý Khoai, Khoai nhìn món | Nét Khoai khá nghiêm; cần owner chọn sắc thái, chưa chứng minh diễn trong chuỗi | Giữ làm ứng viên |
| REF01-M | Một tay Đào vươn, tay kia nghỉ, hai mặt thấy rõ | Điểm ngón tay gần mép sau/đỉnh món, chưa rõ vành gần-phải như brief; không khẳng định chắc chạm món | HOLD — chưa chọn làm reference hành động |
| REF01-E | Hai tay đã nghỉ, ánh nhìn qua nhau, bàn ăn giữ cấu trúc | Cả Khoai và Đào hé miệng, khác yêu cầu khép miệng | REWORK |
| REF03-S | Khoai cười kín, Đào tò mò, tay nghỉ/F0 | Miệng Đào hé, khác yêu cầu reference khép miệng | REWORK |

Cấu trúc bàn còn đủ món nguội, rau, hai bát chấm, hai bát riêng rỗng, hai đôi đũa nghỉ và cốc bên phải Đào; không thấy khói. Gương mặt, trang phục, ánh sáng và bối cảnh gần B nhưng không bảo toàn pixel. Không bác biến thể món B đã được owner duyệt chỉ vì khác chuẩn TABLE08 lịch sử.

## 4. Tầng lỗi và cách sửa đề nghị

Đã đối soát đúng source → prompt/preflight → UUID output → file tải. E/REF03-S vẫn hé miệng dù prompt ghi khép miệng: lỗi được quan sát ở **output tạo ảnh**, không có bằng chứng tải nhầm, nhầm voice hoặc lỗi ghép. Nguyên nhân nội tại model chưa xác định. Giả thuyết cue hội thoại lấn yêu cầu môi chỉ dùng để thiết kế thử, không gọi là nguyên nhân đã chứng minh.

Đề nghị **sửa vùng nhỏ trên chính ba ảnh v01**, không dựng lại cả bối cảnh:

- M: chỉ sửa tay vươn và đích ngón tay; hướng tới vành đĩa phía phải ảnh, có khoảng hở thấy rõ, không xuyên bát hoặc đặt trên món.
- E: chỉ khép miệng cả hai, giữ ánh nhìn, góc đầu và tay.
- REF03-S: chỉ khép miệng Đào; giữ nguyên nét cười kín của Khoai.

Giữ S làm ứng viên, không tạo lại. Ba [prompt draft](evidence/224/repair-request-DRAFT.json) đã có exact source UUID/hash, prompt/hash và giới hạn. **Chưa được duyệt/chưa gửi:** tối đa ba request ảnh, một lượt/x1 mỗi request, tổng trần 0 credit; kiểm quote live trước từng submit, dừng nếu quote khác 0 hoặc scope/model/input thay đổi. Không retry, video, voice, Quality hoặc auto-accept. Sửa vùng nhỏ vẫn có nguy cơ model làm lệch vùng phải giữ, nên phải kiểm lại toàn ảnh.

## 5. Tổng hợp vòng

**Đã xác định:** đúng bốn lượt, native tải đủ, hash/copies/prompt khớp; có lỗi pose cụ thể, không chấp nhận cả bộ chỉ vì ảnh đẹp. N02 B và canon C-v0.6 không thay đổi.

**Quyết định đã chốt:** thực thi gói bốn ảnh theo approval owner. Chưa có owner output acceptance hoặc quyền sửa ba ảnh.

**Giả định đang dùng:** giữ B là chuẩn hình riêng EP01; giữ S để xem xét, không bắt buộc sinh lại vì sắc thái nghiêm. Cảm xúc đọc từ ảnh là diễn giải, không bằng chứng nhịp diễn thực.

**Còn mở:** disposition S, đích tay M, môi E/REF03-S; toàn bộ R01–R09 và bản dựng thử G1. Ảnh này không chứng minh kéo–dừng, speech-end, chuyển động, người nói/giọng/khẩu hình, cut continuity hoặc full AV.

**Bước tiếp:** trình kết quả đã đối soát hai reviewer và xin duyệt riêng ba lượt sửa ảnh nếu owner đồng ý. Sau khi ảnh đúng mới tiếp tục bộ khung toàn cảnh; không chuyển thẳng sang video cuối/Quality.

## 6. Hướng dẫn và lưu trữ

Áp dụng skill [computer-use](C:/Users/PC/.codex/plugins/cache/openai-bundled/computer-use/26.930.61225/skills/computer-use/SKILL.md) để vận hành Flow theo UI được quan sát, kiểm quyền/quote và lưu bằng chứng. Áp dụng hướng dẫn [imagegen](C:/Users/PC/.codex/skills/.system/imagegen/SKILL.md) để ghi rõ vùng phải giữ/vùng được sửa. Theo lựa chọn của owner, tạo ảnh trên Flow, không đổi nhà cung cấp hoặc dùng API tạo ảnh khác.

Native, nguồn B, prompt đã dùng, bảng so sánh và hồ sơ QC đã được sao lưu vào folder owner. Không sửa/xóa các file download gốc hoặc media lịch sử. Đợt này đã lưu local; chưa commit/push các thay đổi recovery đang tồn đọng, không nhận đã đồng bộ Git.
