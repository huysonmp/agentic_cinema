# REC255 — Clip nguồn dài không phải thời lượng dùng trong phim

Với nhịp chỉ có “Khoan”, 4 giây nguồn để kiểm sửa áo không cần giữ nguyên trong bản dựng. Cắt phần chờ trước/sau sau khi đối soát chuyển động miệng và khoảng âm nguồn; lần này giữ F20–37, 0,75 giây.

Khi kiểm clip đã cắt, output F0 tương ứng source F20, không phải F0. Dùng offset rõ ràng trong mọi board/report; so nhầm gốc thời gian tạo kết luận QC sai.

Hình và tiếng phải cắt cùng gốc. Cắt chính xác rồi xuất AAC làm PCM thay đổi nhẹ, không được tiếp tục ghi “bit-exact” từ chứng minh của clip trước. Giữ bản PCM đúng lát nguồn để dựng tiếp; tương quan ở độ trễ 0 không thay kiểm nghe và khẩu hình.

Lệnh owner yêu cầu cắt không phải lời duyệt giọng/hình, cũng không cấp quyền sinh thêm. Sau cắt vẫn kiểm đúng clip và điểm nối; không suy diễn clip ngắn thành cả phim đã đạt.
