# P6 — Owner chỉ định hai ảnh cầm đũa hiện có

2026-10-01. Sau61, owner: “có ảnh thì cầm đũa đúng rồi, ảnh Hand holding wooden chopsticks và ảnh Potato character holding wooden …”. Ưu tiên kiểm hai ảnh hiện có thay vì tìm/dựng mẫu mới. Không generation/upload/repair trong vòng này.

## Live read-back

Root đã mở hai current canvases trong đúng project9276788e-9781-44fb-ba5b-083006667374, download và view_image thực; đối soát SHA256 với local raw:

| Tên owner chỉ | AssetID | Exact local version | SHA256 | Vai trò được owner xác định |
|---|---|---|---|---|
| Potato character holding wooden … | dba187f0-f6c0-4ef0-8cc1-7efe8a176e53 | H-K-I03_v0.1.jpg | AF53408253A1B24E9D6F31C8462A2EB890F2F790972ED2AF7C77D3238A54AF9F | Mẫu dáng/hướng cầm đúng để tiếp tục |
| Hand holding wooden chopsticks | ef5c30f0-736b-4d59-999f-6ddca114e77b | H-K-I05_v0.1.jpg | 8BC1621C64E728FBFA45BA0526B923274D546D82A6A1AB08EA1A17E5983AB500 | Mẫu dáng/hướng cầm đúng để tiếp tục |

Paths: `media/raw/ep01_p6_consistency/` cho cả hai. Download tạm respectively `C:/Users/PC/Downloads/b63cfafb-9718-4548-95e6-3019f2a7c453 (1).jpg` và `C:/Users/PC/Downloads/a7b05d16-6c3c-4809-8feb-b0ebe1b6cf8f (2).jpg`. Không version mới hoặc ghi đè raw. Tên card không đủ proof; hash live bằng exact local versions.

## Quan sát và đính chính của root

Hai ảnh có phần lưng/ngón cong của tay hướng ra người xem, que đi ngang chéo về phía trước ngực; khác họ I07/I09 với lòng bàn tay/ngón cái được phô ra camera. Owner chọn hai ảnh này là mốc dáng/hướng phù hợp. Các contact khuất vẫn không thể chứng nhận toàn bộ từ still, nhưng **không lấy ngón cái không lộ hoặc các ngón cong thành dải làm bằng chứng duy nhất của grip sai/nắm đấm**.

Root đã đặt visible-thumb requirement quá mạnh trong chuỗi sửa và giữ nó thành invariant; kết quả bảo toàn hình không phù hợp ý owner. Reports cũ nhận định readability/fist-like giữ nguyên lịch sử; recommendation đó không thắng lựa chọn reference hiện hành. Không đánh tráo owner selection thành kiểm chứng khoa học mọi cơ học tay, motion hoặc food-contact.

## Decision lock và next

- OWNER_SELECTED_DIRECTION_REFERENCES: exact I03/I05. Khóa dáng/hướng cầm của hai ảnh làm mốc; không áp tiếp hand geometry I07/I09.
- I09 vẫn rejected theo61; I07 không làm repair reference. Primaryduo45 vẫn identity/outfit baseline.
- Đây không duyệt toàn P6 hoặc video, không tự mở motion/food generation. Không bắt owner tìm ảnh bàn tay mới hoặc chứng minh từng ngón khuất.
- Bước tiếp theo: dùng I03 cho portrait-scale và I05 cho body-scale reference khi cần scene/prop planning; chỉ sửa lỗi cụ thể khác nếu có actual evidence, không sửa grip chỉ để đạt tiêu chí “phải thấy thumb”. Mỗi scene mới cần actual-media review đúng version.
- Research web vừa khởi đầu trước owner clarification chỉ là background; không upload ảnh bên ngoài, không chuyển Japanese dining convention thành canon văn hóa Việt Nam hoặc tiêu chí bác ref owner.

Đã xác định: exact hai ảnh owner chỉ, local/live khớp; lựa chọn hướng cầm rõ. Quyết định: dùng existing references, bỏ hướng repair I07/I09. Giả định: owner acceptance scope là dáng/hướng grip trong hai stills, không toàn bộ asset/P6. Còn mở: thao tác gắp/transfer theo script, food và các gap P6 khác. Tiếp theo: giữ grip này trong phần việc liên quan, không tạo sửa đũa mới vô cớ.
