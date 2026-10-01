# P6 — Đối soát món và preflight tay

Ngày 2026-10-01 Asia/Saigon. Owner yêu cầu “đối soát lượt món và kiểm đầu vào cho thử nghiệm tay mới”. Scope read-only Flow + local checks/log; không submit generation, upload, retry, restore/ghi đè canvas hoặc đổi model. P6 OPEN.

## F-NB-02 — kết quả đối soát

Đã đọc56, vào đúng project `9276788e-9781-44fb-ba5b-083006667374` trên in-app browser hiện hành. Library không có thẻ món hoặc thông báo terminal/tiến trình F-NB-02. Một truy vấn `Nem` trả các thẻ nhân vật, không có output món nhận diện được; search có thể match nội dung khác nên không dùng làm chứng minh lịch sử request chưa từng tồn tại. Đã bỏ filter và kiểm library. Session panel trống không cung cấp log request món. Không có provider request ID để truy exact terminal state.

Kết luận **UNRECONCILED / NO_ACCESSIBLE_OUTPUT**, không biến thành FAIL/SUCCESS hoặc no-charge. F-NB-01 no-charge/moderation failure ở56 vẫn là dữ kiện riêng, không áp cho02. Không retry duplicate. Owner cần xác nhận nếu có terminal notification/output/log bên tài khoản; nếu không truy được, cần quyết định riêng về request mới, giữ02 unresolved thay vì xóa lịch sử. Không cản các preflight tay độc lập.

Proof local/gitignored `media/raw/ep01_p6_food/F-NB-02_recheck-2026-10-01.png`.

## T1 — input binding

Đọc exact proposal08 và root disposition09: T1 đổi hướng que trên **I04**, giữ wrist/hand; T2 HOLD do tương tự repair đã fail. Không mở lại T2.

| Input | Verified actual | Readiness |
|---|---|---|
| Local I04 v0.1 | SHA256 `412367B419CD3EEADD65390BD853A790776FFC7E354B6ACFB1F1970A74C93557`, đúng manifest55 | Byte control AVAILABLE |
| Local I05 v0.1 | SHA256 `8BC1621C64E728FBFA45BA0526B923274D546D82A6A1AB08EA1A17E5983AB500` | Không thay I04 trong T1 |
| Current Flow canvas `ef5c30f0-736b-4d59-999f-6ddca114e77b` | Download JPEG; hash bằng I05 nêu trên | **TARGET_MISMATCH**, không chạy T1 trên canvas này |
| History I04 | Download ảnh history gắn với prompt expand; đã xem actual WEBP 286×512, hình tương ứng I04; SHA256 `DA1F265AF7C2D3FABD7142A319B70FB69419E875ECE49C229B040182471F5293` | Preview khác bytes/resolution I04; không lấy làm exact edit target |
| Editor model/aspect/price | UI Nano Banana Pro,9:16,0credit; editor một output theo mode hiện hành, chưa submit | Current preflight evidence, không billing guarantee |
| Library default | Nano Banana2/x1 | Khác editor; không tự chọn library default thay Pro |

Current canvas JPEG downloaded path `C:/Users/PC/Downloads/a7b05d16-6c3c-4809-8feb-b0ebe1b6cf8f (1).jpg`; history preview `C:/Users/PC/Downloads/unnamed.webp`. Không đưa hai download tạm thành canon assets; raw controls trong workspace vẫn giữ nguyên. Proof UI `media/raw/ep01_p6_consistency/T1_preflight-2026-10-01.png`, local/gitignored.

**T1 status: INPUT_CONTROL_VERIFIED / FLOW_BINDING_NOT_READY.** Cách chuẩn cho lượt sau: đưa đúng local I04 vào asset mới riêng, mở editor và read-back/download so hash trước submit. Hoặc chọn historical full-resolution version nếu UI cung cấp và xác minh bytes; không restore ghi đè I05 chỉ để chuẩn bị. Upload chưa làm trong scope này. Không attach I04 như support rồi dùng I05 làm target: đó là thí nghiệm khác, phải revision manifest. Exact prompt tại08 giữ nguyên, chưa điền composer/chưa chạy.

## Tổng hợp vòng

Đã xác định: food chưa có terminal evidence; target Flow đang I05, không I04; local control I04 nguyên vẹn; UI editor Pro9:16/0credit hiện tại. Quyết định: giữ food unresolved và không submit duplicate; chặn T1 sai target, giữ T2 HOLD. Giả định: local I04 là control của T1, không asset grip đã duyệt. Còn mở: F-NB-02 outcome; đưa đúng I04 vào editor; test geometry/contact thật sau generation. Tiếp theo: chuẩn bị asset I04 riêng và verify binding trước một T1 image-only trial; owner xác nhận tình trạng lượt món trước request món mới. Không đóng P6 hoặc mở voice/video.
