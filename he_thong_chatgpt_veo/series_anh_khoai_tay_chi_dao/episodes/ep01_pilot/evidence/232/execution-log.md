# REC232 — Intake, route, quote và một lượt production

Ngày2026-10-07. Owner báo “tải lên rồi nhé”.

1. Tab5 ở collection trống chưa có tên; root dùng nút back về project, không xóa collection. Lưới/picker vẫn hiện failed/uploading và Add disabled. Lưu trạng thái đó, hỏi owner ngắn về kết quả tải.
2. Theo231, đóng5, mở6 mới cùng project. Tab mới hiện **R01_SOURCE_GUIDE_NOT_FINAL** có thumbnail; mở asset373eec41-efdb-45ea-8196-49d91b6f980a và Flow hiển thị duration4s. Trạng thái ban đầu không còn là kết luận upload hiện hành. Không yêu cầu owner tải lại khi source đã dùng được.
3. Bấm download kích thước gốc trong UI; công cụ chờ download event timeout15s. Đóng6/mở7 cùng asset theo quy tắc khôi phục. Sau đó kiểm đúng tên file trong Downloads phát hiện download thực **đã hoàn tất** tại `R01_SOURCE_GUIDE_NOT_FINAL_20261007125205.mp4`. Timeout event không chứng minh download thất bại; trước yêu cầu tải lại phải kiểm file đúng tên/path và decode/hash. Không xóa file hoặc retry paid.
4. Download Flow có video1280×2274/24fps/4s, AAC48kHz/stereo4,010667s; không đồng byte source360×640. Local script kiểm hai range thoại zero-offset waveform: N01 correlation0,99998585, prefixB0,99986010. Root xem sáu ảnh contact, nội dung tương ứng guide. Đây là correspondence kỹ thuật, không hearing/voice/AV PASS. ExactPCM của229 vẫn là nguồn master, không thay bằng download Flow.
5. Tab7 project composer nhận videoUUIDffcf5a2e-1449-4167-aafd-8bb8dd842fa3 + S/M/E đúng phiên bản. Các imageUUID đã read-back từ DOM chip; prompt nhập nguyên bản hash98ee8c…8b29, normalize newline/trim khớp. Không voicepreset khác hoặc fullA03/oldN02.
6. Live route Ingredients/Omni1.1 Flash/360p/9:16/x1, durationbasedoningredient4s, AgentOFF; quote10. Lưu screenshot/AX. Owner trả lời rõ **Duyệt một lượt R01 — 10 credit**.
7. Submit đúng một lần, composer reset và job **Edit animated food story shot** progress3%. Chưa retry. Quote10/dự kiến77→67; số dư thực sau đang được kiểm, không dùng phép trừ làm xác nhận.
8. Sau đó UI job báo **Không thể chỉnh sửa lời nói trong video này. Vui lòng thử một câu lệnh khác hoặc gửi ý kiến phản hồi. Bạn chưa bị tính phí cho lượt tạo này.** Account hiện77. Quote10 không thành actualcharge10; chi thực0, không output. Lưu AX/screenshot/balance; đóng7, mở8 sạch cùng project theo231, không submit lại.
9. Giao maker DIR/EDIT/CTD và critic độc lập chẩn đoán local trên exact request/error; không giao generation/browser/network/credit/Git hoặc gọi run này thành QC sản phẩm chưa có.

Tiêu chí QC giữ229: mặt/miệng đúng speaker/voice/text, reach→Khoan→stop→return trước usablejoin, quỹ đạo tránh bát, F0/mónnguộikhôngkhói/table/refs, picturejoin sang B, exactsourceaudio. Chưa output PASS hoặc fullG1/master. BoundaryB1s vẫn provisional; không đưa0,85s guidepad vào master.

**Kinh nghiệm:** lỗi intake và lỗi quan sát/trễ cập nhật phải tách nhau. Owner upload + fresh tab làm source hiện dùng được, chưa chứng minh tất cả lỗi cũ chỉ do stale tab. Download eventtimeout nhưng file hoàn tất: kiểm evidencefilesystem của đúng thao tác trước khi kết luận thất bại. Gặp lỗi tab đổi tab đúng231; không suy đổi tab là quyền generationretry.
