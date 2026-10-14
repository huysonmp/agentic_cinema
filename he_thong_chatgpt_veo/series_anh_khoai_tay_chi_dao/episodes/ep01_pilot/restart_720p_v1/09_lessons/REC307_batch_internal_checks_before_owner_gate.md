# REC307 — Gom kiểm nội bộ trước một cổng duyệt có ý nghĩa

Owner giao thực hiện phương án local và yêu cầu agent kiểm, thay vì hỏi lại từng thao tác. Tracking, chọn donor trong cùng native, mask, remux, hash, unit test, decode và nối nháp là công việc nội bộ trong brief đã giao; không cần thêm approval riêng cho từng phần đó.

Agent EDIT kiểm ngữ cảnh/range/điểm nối và giới hạn thời lượng; agent QA khác kiểm actual output, toàn range và vùng sửa. Root đọc toàn report và tự xem evidence trước trình một gói. Tên vai agent hoặc review giấy không thay review trên file đã xuất.

Giữ cổng owner cho output hình–tiếng/nhịp nối có ý nghĩa, nội dung thay đổi, credit mới hoặc scope vượt brief. Approval tiếng được giữ nhờ copied AAC packets và timestamps đúng bản owner nghe; không hỏi lại tiếng đã duyệt nếu thực sự giữ stream ấy. Join AAC phải encode mới thì ghi rõ, không giả làm bit-exact hoặc chuyển audio approval thành AV approval.

Không bỏ quality gate vì owner không muốn bị hỏi vụn. Các giới hạn thật như clearance bị che, endpoint chớp mắt, food seam và final30 vẫn phải ghi trong backlog và giải quyết ở chặng tương ứng.
