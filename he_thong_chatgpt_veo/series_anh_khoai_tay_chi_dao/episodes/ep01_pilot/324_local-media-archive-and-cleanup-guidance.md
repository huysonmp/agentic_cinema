# REC324 — Đã gom kho media local; chưa xóa nguồn

Ngày 17-10-2026. Owner yêu cầu gom ảnh/video đã tạo từ dự án vào một folder và hỏi có nên xóa một lượt không. **Đã sao chép và kiểm toàn bộ media tìm được trong phạm vi local dưới đây; không di chuyển/xóa nguồn và không thao tác trên Flow.**

## Mở kho đã gom

[Kho EP01 Nem Bùi](D:/Workspace/agentic_cinema_media_archive/EP01_Nem_Bui_20261017)

[Hướng dẫn và danh mục](D:/Workspace/agentic_cinema_media_archive/EP01_Nem_Bui_20261017/README.md)

Chọn ổ D vì khi bắt đầu ổ C còn khoảng8GB, không đủ cho worst-case bản sao. Kho nằm ngoài Git repository để không vô tình commit/upload media. Không nén, chuyển mã hoặc giảm chất lượng file.

## Kết quả kiểm đã hoàn tất

| Hạng mục | Kết quả |
| --- | --- |
| Các đường dẫn tệp nguồn local | 13.020; kiểm cuối vẫn tồn tại toàn bộ |
| Nội dung media duy nhất | 11.784 file; 9.447.100.717 byte ≈9,45GB/8,798GiB |
| Ảnh, gồm ảnh tạo/đầu vào/bằng chứng/khung trích | 11.345 nội dung duy nhất |
| Video nguồn/bản dựng/thử | 280 nội dung duy nhất, gồm bản v2 đang chọn |
| Audio giữ kèm để bảo toàn tài nguyên giọng | 159 nội dung duy nhất |
| Bản nguồn trùng nội dung | 1.236 bản vượt số nội dung duy nhất; được ánh xạ trong CSV, không copy lặp binary |
| Hồ sơ/prompt/quyết định/manifest giữ kèm | 1.494 tài liệu, 8.340.702byte; có checksum riêng |
| Xác minh copy | Mỗi media unique được kiểm SHA256 sau copy; checksum các danh mục và sự tồn tại11.784 đích được kiểm lại |
| Xóa / di chuyển / relink | 0 / 0 / chưa làm |

Dung lượng trùng1.609.481.263byte là tổng logic theo các đường dẫn nguồn, **không phải cam kết dung lượng thực có thể xóa ngay**. Chưa giải phóng ổ C vì chỉ sao chép.

Video đang chọn có tên dễ tìm: `00_BAN_DANG_CHON/EP01_BAN_DANG_CHON_v2_323.mp4`. SHA256 giữ nguyên `d7f380e05bdcafb3eb2768ce0cc4d011c6ee7570a4ec24788ce0cdf4305e2845`. Phản hồi “ok r nhé” của owner giữ đúng bản323; việc gom kho không biến các mục final30/finishing trước đó thành đã hoàn tất hoặc cho phép phát hành.

## Phạm vi đã gom và giới hạn

1. `D:/Workspace/agentic_cinema/he_thong_chatgpt_veo`.
2. `D:/Workspace/agentic_cinema/artifacts` của pipeline EP01.
3. `C:/Users/PC/Downloads/du_an_nem_bui`.
4. Folder generated_images đúng thread `01a0eb0e-6ec3-7121-a6a5-ea0ccdb77744`.
5. 64 file media ngoài các root trên được tìm qua đường dẫn thực, đang tồn tại và được tài liệu/script của dự án dẫn chiếu; không quét rộng toàn Downloads/Pictures hoặc các repo nhánh khác.

Đã kiểm thêm: root repo, docs và folder visualization đúng thread không có media để bổ sung. Ảnh/video **chỉ còn trên Flow, chưa tải local**, không được kiểm kê hoặc tải trong vòng này. Không hứa đây là bản export đầy đủ tài khoản cloud.

Kho phân nhóm video đang chọn, video nguồn, bản dựng/thử, ảnh tạo/tham chiếu, ảnh đầu vào, audio và ảnh kiểm tra/khung trích. Đây là nhãn lưu trữ, không là quality approval hoặc điều kiện xóa. Các file trùng hoàn toàn theo SHA256 chỉ lưu một bản; khác encoding/kích thước hoặc có pixel thay đổi vẫn được giữ riêng, không lọc trùng theo cảm quan.

## Danh mục chính — dùng V2

- `DANH_MUC_TAT_CA_NGUON_V2.csv`: mỗi đường dẫn gốc → hash → vị trí lưu trong kho; đánh dấu không có quyền xóa.
- `DANH_MUC_TEP_DUY_NHAT_V2.csv`: mỗi nội dung media được copy một dòng.
- `CAC_BAN_TRUNG_NOI_DUNG_V2.csv`: nguồn có nội dung trùng, **không phải lệnh hoặc danh sách đã duyệt xóa**.
- `DANH_MUC_HO_SO.csv`: tài liệu đi kèm và checksum.
- `TONG_HOP_324_V2.json`: số lượng/phạm vi/hash danh mục. SHA256 của file này: `e1e6752f3b6025d360554460a2e6730728375172d76ade4ee5bee97c23fa289f`.

Lần quét đầu chưa nhận đúng dấu backtick cuối path Markdown. Đối soát bổ sung thêm19đường dẫn và3nội dung unique; cũng loại tám chuỗi văn xuôi bị đọc nhầm thành tên file thiếu. Giữ metadata ban đầu để truy vết, V2 là mốc hiện hành; không suy tám chuỗi đó thành tám asset bị mất.

## Có nên xóa một lượt?

**Chưa nên xóa hàng loạt.** Kho mới vẫn ở cùng máy và các script/EDL còn tham chiếu đường dẫn gốc. Phần lớn media không được lưu trong Git, nên commit/push không phải backup của chúng.

Thứ tự dọn an toàn được đề xuất, chưa thực hiện:

1. Sao lưu kho này thêm lên ổ khác hoặc nơi lưu ngoài máy, rồi kiểm checksum/mở thử media quan trọng.
2. Đối soát bản tải/bàn giao trùng ở Downloads với đường dẫn còn được script/EDL dùng. Chỉ xóa các bản sao thật sự không còn cần dùng sau khi có phạm vi được owner cho phép.
3. Xem xét frame trích/boardQC có thể tái tạo nếu video nguồn và lệnh còn đủ. Không coi mọi ảnh trong `evidence`/QC là đồ thừa: có đầu vào hoặc bằng chứng chỉ nằm ở đó.
4. Không xóa nguồn dựng, giọng đã chọn, master/reference hoặc projectFlow hàng loạt. Muốn dùng kho làm nguồn duy nhất phải relink và kiểm dựng lại trước.

Không gọi dọn trùng là đã thu hồi credit hoặc đã giảm dung lượng Flow. Không phát sinh credit hay upload bên ngoài trong vòng này.

Tool: `scripts/collect_ep01_media_324.py`, copy binary tạm rồi kiểm hash trước đổi tên thành bản lưu, không overwrite archive có sẵn và không có thao tác xóa nguồn. Snapshot hồ sơ trong kho được tạo trước tài liệu324 này; hướng dẫn root và summaryV2 là cập nhật sau đối soát.
