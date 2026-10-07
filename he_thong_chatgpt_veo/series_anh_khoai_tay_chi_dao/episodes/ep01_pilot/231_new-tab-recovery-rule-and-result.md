# 231 — Quy tắc đóng tab lỗi, mở tab mới

Ngày2026-10-07. Owner: “tắt tab đi và làm lại ở tab mới, nếu lần sau lỗi thì tắt tab đó đi mở tab mới ra”.

## Quy tắc làm việc hiện hành cho Flow

1. Khi tab Flow báo lỗi tải/nhận tệp hoặc tương tác không phục hồi, lưu thông báo và trạng thái thực cần đối soát.
2. Đóng **tab bị lỗi**, mở **tab mới** đến đúng project/account; không tiếp tục retry trên tab lỗi. Không thay bằng reload tab cũ.
3. Kiểm lại nguồn/ingredients/cấu hình vì tab mới có thể mất draft. Không coi tên file, config nhớ lại hoặc session cũ là read-back hiện hành.
4. Chỉ retry thao tác trong phạm vi đã được giao. Quy tắc tab không tự cấp paid generation/retry, không xóa media/project, cookie, đổi account hoặc đăng xuất.
5. Nếu lỗi xảy ra sau submit tạo video, kiểm job/balance trước khi retry để tránh gửi hai lượt hoặc chi hai lần. Không đóng tab rồi coi generation chưa chạy.
6. Một lần phục hồi tab vẫn gặp cùng lỗi thì ghi kết quả và kiểm lớp lỗi tiếp; không mở/đóng tab vô hạn và không đổi script/voice để lách lỗi intake.

## Đã làm theo chỉ đạo

- Đóng hai tab Flow1/2 gặp lỗi tại230; tạo tab3 mới đến đúng EP01 project.
- Tải lại **cùng source229**, không chuyển file khác: `C:/Users/PC/Downloads/du_an_nem_bui/229_r01_production_input/R01_SOURCE_GUIDE_NOT_FINAL.mp4`, hash `1ecc6b496291179ce1f5e82153883e2df826b8cf3d7bfdd64edca2a78530b82f`.
- Xác nhận cùng nội dung quyền tải đã được owner cho phép230, chỉ nút “Tôi đồng ý”, không chọn không hiện lại.
- Tab mới3 vẫn báo **Không tải được video lên. Hãy thử lại**. Chưa prompt/ingredients được nhận đủ, chưa generation submit.
- Lưu screenshot/AX lỗi; đóng chính tab3, mở tab5 sạch cùng project. Kiểm inventory: các tab Flow1/2/3 đã đóng; chỉ tab5 là Flow còn mở. Một tab Google One khác tồn tại, không nằm trong phạm vi đóng nên giữ nguyên.
- Tab5 đã tải đúng lưới project, composer trống/submit disabled. Không tiếp tục retry cùng lỗi trên tab đó; giữ để owner hoặc root tiếp thao tác sau giải quyết intake.

## Kết luận đúng phạm vi

**Đã thực hiện đóng tab và mở mới thật, nhưng lần tải trên tab mới vẫn thất bại.** Chưa đủ bằng chứng kết luận lỗi nguồn, Flow hoặc đường chuyển tệp của trình duyệt. Không khẳng định đổi tab chắc chắn chữa lỗi; quy tắc này được giữ như thao tác phục hồi đầu tiên theo owner.

Giữ tất cả khóa229: picture mở quanh “Khoan”, nguyên B audio/phần ký ức, voice/script/refs và production-only. Chi231=0; số dư đã thấy trên tab3=77. Chưa request đủ input/quote/AV/G1/master.

## Còn mở và bước tiếp

Kiểm một lần **upload tay đúng file nguồn** trên tab sạch, không bấm tạo video, để phân biệt lỗi đường thao tác với lỗi file/dịch vụ. Nếu upload tay thành công, root chọn exact source/ref và đọc route/quote trước approval chi; nếu cùng file cũng lỗi, ghi thông báo thực rồi xử lý validation/dịch vụ trong scope. Không yêu cầu owner làm ảnh/dựng/kiểm kỹ thuật thay root.

Evidence: [chỉ đạo và đối soát tab](evidence/231/tab-recovery-instruction.json), [lỗi trên tab mới](evidence/231/01_new-tab-upload-failed.png), [tab sạch giữ lại](evidence/231/02_clean-project-tab.png); AX cùng tên.

Đã chốt quy tắc phục hồi tab; đã xác định đổi tab chưa giải quyết lượt này. Giả định giữ package229 và account/project hiện hành; căn nguyên intake vẫn mở. Bước tiếp là checkpoint upload tay cùng file, không thêm credit hoặc batch thử.
