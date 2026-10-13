# REC284 — Bài học từ request sửa món không có output

## Quan sát

Exact approved source C05→C06 + approved START food-material-only + prompt đã read-back, quote live12, tài khoản/số dư đủ. Một submit trả lỗi chung ngay trong lịch sử, không video mới. Số dư sau reload không đổi. Không retry hoặc sửa nguồn.

## Điều không được suy

Upload/ingredient được UI nhận + quote hợp lệ không chứng minh backend nhận được phép sửa hoặc chất lượng đạt. Không có output thì không có visual/audio findings; không gán lỗi cho cut, giọng, món hoặc độ dài chỉ vì chúng là rủi ro preflight. Net debit0 không mở lại quyền một lượt, không chứng minh đã hoàn tiền. Không có diagnostic không đủ kết luận prompt là nguyên nhân gốc.

## Cách áp dụng lần sau

Khóa request trước gửi bằng source/ingredient/prompt hashes, route/quote/settings và authority; tách request failure khỏi content failure. Khi lỗi chung: giữ job/screenshot, đối soát balance sau reload, đọc diagnostics được công cụ cho phép; nếu không có thì UNKNOWN. Chỉ thay biến hoặc route sau khi đề nghị mới có căn cứ/phạm vi/cap, không phản xạ bấm Retry. Giá công bố và quote UI khác nhau phải lưu cả hai, không lấy một giá nhân cả kế hoạch.

Lỗi này chưa chứng minh một tuyến sửa khả thi để đóng food gate toàn phim; cần tiếp tục kiểm route không trả phí trước quyết định mới. Không dùng technical source validity, old audio approval hoặc preflight paper làm quality approval output không tồn tại.
