# 233 — Phương án sản xuất trong 77 credit

Ngày2026-10-07. **BUDGET_AND_ROUTE_PROPOSAL / NOT_OWNER_APPROVED / NO_GENERATION.** Trả lời owner “tóm lại là còn từng kia credit đủ làm theo cách nào”. Không ghi câu hỏi ngân sách thành quyền chi hoặc thay audio.

## Điểm sửa trong cách lập dự toán

232 dùng **video-edit** với source có tiếng; composer báo10, job từ chối chỉnh lời nói, chi0. Không được dùng giá edit đó để tính mọi tuyến. Hồ sơ200 đã dùng **tạo mới từ ảnh + K20**: Omni360p10s/x1 giá7, chi7. Hồ sơ154 từng tạo mới có hai customvoices và ảnh,360p8s giá6/output; giữ voice qua action mới vẫn phải QC, không suy lịch sử là mọi cảnh đạt.

Đã kiểm live composer trống trên đúng project/account: Omni1.1 Flash/Ingredients/360p/9:16/x1 **không video source**:4s=4,6s=5,8s=6,10s=7. Snapshot giá trong evidence233. Account hiện77; lượt233 không prompt/ingredients/video generation. Đã phục hồi kết nối khi runtime cũ không còn, mở cùng project; không đổi account hoặc xóa media.

Giá này là loại tạo cảnh mới, chưa là finalquote của request có đủ ảnh/voice. Trước submit vẫn đọc lại đầy đủ input, route, duration, giá theo215/217. Giá có thể đổi; không blanketauthority.

Nguồn Google đã đọc2026-10-07:

- https://support.google.com/flow/answer/16526234?hl=en — Omni360p tạo mới4/5/6/7; bảng public ghi edit40, **khác quote UI232 là10**, không viết đè evidence lịch sử. Theo chính Google phải đọc giá mới nhất trong settings.
- https://support.google.com/flow/answer/16352836?hl=en — Omni hỗ trợ tạo mới từ text/frame/ingredients, customvoices; Pro/Ultra có upscale Omni360p→720p0credit. Chưa kiểm nút upscale actual account, không hứa nâng đủ detail hoặc Quality miễn phí.

## Phương án khuyến nghị: tạo mới cảnh thiếu, tiếng và miệng cùng lượt

Không tiếp tục dùng video có tiếng làm ingredient để yêu cầu sửa speech/mouth. Dùng ảnh đã kiểm cho đúng từng đầu/trạng thái, cùng customvoiceK20/OrusIDfb1188da-e6c8-4156-9bba-0576c01a8da6 và D06/AoedeID0ce1551e-e74b-481c-bb9e-d31e04f8b352 theo người nói. **Sinh mới cả picture/performance và tiếng cho lượt cần làm trong cùng generation**; không tuyển lại chất giọng. Chỉ một người nói thì chỉ voice đó; cảnh hai người nói cần mapping/mentions rõ và QC attribution.

Giữ đoạn ký ức B đã duyệt làm phần tái dùng, không mặc định sinh lại. R01 có “Khoan” sinh mới sẽ cần owner cho thay cả đoạn tiếng mở liên quan và kiểm nối với B; không nhận approval229 chỉ thay picture như quyền thay tiếng. OriginalB/PCM/source cũ giữ nguyên, không xóa. Không lặp hai lần Khoan hoặc đè tiếng cũ lên miệng mới chưa khớp.

Phương án này tránh bước ghép voice lên một video im rồi phải trả tiền thêm cho sửa miệng. Nó **không bảo đảm** tạo hình, món, tay, giọng và lip-sync đều đúng lần đầu; giảm số công đoạn trả phí không thay cổng QC. Chưa có outputR01 mới theo route này, không gọi khả thi đã chứng minh toàn tập.

## Trần dự toán và phần dự phòng

| Nhóm nhiệm vụ mới | Số đơn vị dự kiến | Trần dự toán mỗi lượt đầu | Tổng trần |
| --- | ---: | ---: | ---: |
| R01 mở có hai lượt nói và hear–stop–return |1|7|7|
| R03 hỏi/đáp |1|7|7|
| R04 cô lấy cốc, anh gắp A về mình |1|7|7|
| R05 cô bắt gặp, anh khựng |1|7|7|
| R06 chữa cháy và đổi hướng A |1|7|7|
| R07–R08 nói, đưa bát, thả A |1|7|7|
| R09 A trong bátĐào, B mới vềKhoai |1|7|7|
| **Lượt đầu tối đa** |**7**| |**49**|
| **Giữ lại trong77** | | |**28**|

7 là trần giá10s/native360p đã kiểm, **không yêu cầu mọi clip đều10s**, không mặc định7request đã duyệt. Thời lượng sinh chọn theo lời/action thực; chỉ dùng range đạt trong master30s. R07/R08 gộp chỉ nếu media chứng minh đủ nhiệm vụ; tách thì cần output bổ sung từ28 và owner approval riêng. Dự phòng28 dùng cho phần thiếu/phải sửa theo finding, không batchtest hoặc auto-retry. Không dùng hết dự phòng cho cảnh mở.

Nếu chọn được duration4s cho sáu đơn vị và6s cho R07/R08 thì firstpass chỉ29, nhưng timing/action chưa khóa nên **không lấy29 làm dự toán cam kết**. Trần49 hợp lý hơn để giữ slack, không đơn giản giảm diễn/action cho đủ4s.

Dựng/cắt/đối soát/ghép/caption/mix bằng công cụ local đã có không dùng Flowcredit. Upscale720p chỉ tính0 nếu feature/quote thực đúng tài liệu; Quality không nằm trong77.

## So các đường khác

- **Tiếp sửa video có tiếng cũ:** exactrequest232 đã bị từ chối, căn nguyên chưa cô lập; không dùng làm đường cam kết hoàn thành77.
- **Hình im riêng → voice mới riêng → lip-sync → ghép:** là phương án sáng tạo hợp lệ, nhưng chưa có route lip-sync/sourcevoice export/giá end-to-end được xác minh trong Flow/local. Nếu hai giai đoạn trả phí đều10 mỗi7cảnh thì140, vượt77; đây là ví dụ có điều kiện, không giá thật của mọi pipeline tách tiếng. Không kết luận cách này luôn đắt/không thể, nhưng hiện chưa đủ cơ sở hứa đủ77.
- **Làm tất cả mới bằngLite10/output:**7output đã70, chỉ còn7; chưa kể việc giữ đúng customvoices và nếu phải lip-sync thêm. Không khuyến nghị dùng mặc định cho mọi shot.
- **Quality100/output:** giá public đã vượt77 chỉ một output; không dùng cho kế hoạch hiện tại.

## Kết luận và bước tiếp

**77 có thể bao được phương án tạo mới bằngOmni360p và tái dùng đoạn B: lượt đầu≤49, dự phòng28. Đây là đủ về kế hoạch chi, không bảo đảm nghiệm thu toàn phim.** Không cấp thêmcredit, không bỏ mặt/miệng/action hoặc đổi kịch bản để tạo cảm giác đã đủ.

Cần owner chốt phương án mới và phạm vi thay tiếng cho những đoạn làm mới, giữ chấtgiọngK20/D06 và phầnkýứcB. Sau đó chuẩn bị một requestR01native từ ảnh+giọng, quote theo durationthực, trình khoản đó trước submit, QC chính output sản xuất. Nếu R01 thất bại cùng yêu cầu nội dung, trình nguyên nhân/findings trước đổiroute hoặc dùng dự phòng, không chạy paidtest riêng/x3.

Đã xác định: credit77 và giá tạo mới4–7live khác edit10lịch sử. Đã chốt trước đó: sản xuất rồi QC, không testtay/x3/Quality; chưa chốt route/gói chi mới ở lượt233. Giả định dự toán:7đơn vị đầu, duration≤10s, phần B tái dùng, R07/R08 có thể gộp nếu đạt. Còn mở: approval thay voicefile/phầnmở, inputroute thực, acting/voice/sync và sốoutputcuối. Bước tiếp là duyệt phương án, không tự dùng49 hoặc28.
