# Flow — kiểm preset giọng và bản nghe trước

2026-10-02. Owner duyệt kiểm capability/baseline sau RCA146, tiếp tục yêu cầu thao tác. Không phê duyệt thay pipeline production sang Omni hoặc voice đạt. Khoản thử mới còn170; không generation video trong lượt này.

## Actual UI và nguồn

Phiên IAB cũ không còn kết nối. Inventory tìm thấy cùng project đang mở ở IAB5/tab2, chọn đúng URL9276788e-9781-44fb-ba5b-083006667374; không dùng Chrome hoặc nguồn giọng web khác.

Đã mở cấu hình và chọn Omni1.1Flash chỉ để kiểm capability, đổi mode Frames → Thành phần. Omni720p/8s/x3 UI báo36credit cho video, không submit. Trong picker thành phần có tab Giọng nói; danh sách preset thật có Algieba (Male, easy-going, mid-low pitch), Algenib, Achird, Charon, Iapetus cùng các preset khác. Không có nhãn Bắc/Nam trên những preset đã xem. Không suy preset name thành accent.

Chọn **Algieba**, nhập đúng hai ô:

```text
Hội thoại mẫu:
Bếp nhà anh, hồi bé. Mẹ rang gạo, anh đứng chờ.

Tuỳ chỉnh đặc điểm giọng nói:
Nam trưởng thành nói tiếng Việt giọng Hà Nội, miền Bắc Việt Nam. Phát âm và ngữ điệu miền Bắc tự nhiên. Âm sắc trung trầm, kể bình thản, thân mật.
```

Bấm Phát bản nghe trước đúng một lần. Nút tạm disable rồi khả dụng lại; DOM audio readyState4/duration5.520917s. Đây là preview native Flow, không kiểm nghe accent bởi root. Không tạo hoặc dùng audio người thật, không clone. Algieba là preset base có provenance, phần Hà Nội vẫn là yêu cầu tùy chỉnh chưa có bằng chứng nghe đạt.

Lưu giọng mới. Actual item/name đọc lại: **Algieba tuỳ chỉnh**, ID `f491dbef-8fd8-4fb1-8b0d-945ab44c2abe`. Tên mong muốn nhập `KHOAI_BAC_TEST_Algieba_R1_PENDING` không được giữ sau lưu, nên manifest dùng tên/ID actual, không khẳng định rename thành công. Không bấm thêm vào prompt, không generation video. Lưu candidate không là owner approval.

## Xuất file / bàn giao / credit

DOM có audio blob ẩn. Thử supported locator downloadMedia(audio) một lần timeout vì media không visible; không dùng fetch/hidden API hoặc shell để lấy blob. Chưa có audio file local để embed. Không dựng file giả hoặc dùng lại mẫu cũ. Owner nghe qua nút preview trong Flow; sample nằm trong preset tùy chỉnh đã lưu. Mở lại picker xác nhận lời, performance và ID được giữ, nút Phát bản nghe trước khả dụng.

Đọc số dư UI sau preview/save:620, bằng số dư trước gần nhất ở145. Không quan sát giảm credit trong scope này; không suy mọi preview luôn miễn phí. Khoản170 giữ nguyên; Quality riêng chưa dùng. Screenshot actual `D:/Workspace/agentic_cinema/artifacts/voice147-preset-preview/voice-preview.png`, copy owner folder147. Tab được giữ làm deliverable.

## Owner cần duyệt / còn mở

1. Trong tab Flow hiện mở, preset **Algieba tuỳ chỉnh**, bấm **Phát bản nghe trước**. Kiểm có đúng **nam miền Bắc** chưa; nếu sai tiếp, loại ngay, chưa chấm hay/dở.
2. Nếu đúng Bắc, ghi accent acceptance cho candidate-ID trước thử tích hợp. Không coi preset base hoặc saving là voice lock qua video.

Đã xác định: tài khoản có actual preset/customization/preview trong Omni Ingredients. Đã chốt: chỉ capability và candidate preview, không production model change. Giả định: Hà Nội là miền Bắc cụ thể để thử, chưa canon. Còn mở: nghe accent, xuất file, giữ giọng qua lời/cảnh, dùng preset trong Veo có được không (chưa test), lip-sync và quyền đổi route. Bước tiếp: owner nghe baseline; nếu đạt thì trình phép thử tích hợp có model/settings/credit rõ, nếu không đạt nghiên cứu nguồn giọng Bắc khác có quyền dùng. Quy tắc ba Lite áp dụng cho video tests, lượt này là một preset preview, không video test ba lượt.
