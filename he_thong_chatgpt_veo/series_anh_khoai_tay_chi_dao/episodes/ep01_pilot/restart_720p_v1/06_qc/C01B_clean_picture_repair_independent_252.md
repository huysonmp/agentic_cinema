# REC252 — Review giấy độc lập tuyến sửa chữ

Kết luận: **GO_TO_OWNER_PROPOSAL**, không phải GO submit hoặc media PASS. Owner B chỉ duyệt chuẩn bị; paid edit, retry và reserve chưa được mở.
Đã đọc đầy đủ decision252/proposal252/draft252, hồ sơ chẩn đoán và request REC232; xem screenshot quote20. Không UI/network, submit, sửa media hoặc chi credit.

- Target đúng T02 solo, hash nguồn trong decision `780ab0b3fb29454f732d2f56ed30526a77f81ed98bbaf04ca04cdb5cf094b231` khớp review251 đã kiểm. Chữ nằm trong native; nguồn chưa được chọn.
- Hash draft kiểm từ file `2370455ce81b59aa39ed717e5b1354eda7ee75348d6c059ab0aa29a65c421559` khớp bàn giao. Draft chỉ xóa chữ trắng viền đen trên áo, phục hồi vải/nút/bóng/nếp, yêu cầu giữ framing/timing/performance/audio/watermark; không yêu cầu tái tạo lời hoặc khẩu hình.
- Screenshot thấy một video chip, Omni1.1Flash/Ingredients/720p/9:16/4s theo nguồn/x1 và quote20. Exact asset `cae2fca6-bd20-4251-92e9-385c4a638f49`, chip `fd1953fa-5f7d-4d73-84e5-ead858bbb01b`, trim0–4/readback/AgentOFF theo root live; screenshot đơn lẻ không chứng minh mọi trường.
- Proposal dẫn tài liệu chính thức và có quote đầy đủ input live: đủ làm cơ sở trình một thử nghiệm video-to-video hẹp. Reviewer này không truy cập web kiểm độc lập tài liệu; UI nhận input/quote không bảo đảm backend nhận request hoặc xóa chữ thành công.
- “Original audio/mouth unchanged” là yêu cầu cần kiểm, không phải tính năng bất biến đã được chứng minh. Có thể đổi mặt/miệng/tiếng/timing, phục hồi áo rung hoặc đổi bối cảnh; chưa có tỷ lệ thành công hoặc cam kết chất lượng.
- REC232 thực tế bị từ chối chỉnh lời nói, không output/không tính phí theo UI. Chẩn đoán mouth reconstruction/speaker attribution kích hoạt speech editing vẫn là giả thuyết, không kết luận classifier. Draft252 khác nhiệm vụ, nhưng không suy chắc backend chấp nhận hoặc có thể bỏ qua giới hạn.

## Ngân sách và authority cần trình

- Quote20 vượt trần15/request đúng5; coverage đã14 +20 =34, vượt trần30 đúng4. Một cleanup là đầu ra thứ3 của đợt, không tự dùng slot BR làm cleanup.
- Phải xin riêng một edit x1/20credit và nâng trần đợt ít nhất34; owner B chưa duyệt ngoại lệ này. Không batch, auto retry, mua credit hoặc mở reserve110.
- Nếu chi đủ20: episode88→108/500, remaining412→392; tạo lại124→104. 104+133+45+110=392, phép tính proposal khớp. Đây là dự tính từ ledger/root, không đọc live tài khoản hoặc xác nhận actual billing.
- Trần34 đủ cleanup này, không bao gồm BR kế tiếp. BM chưa đạt và BR chưa có quyền chi tiếp; future BR cần quote/cap/output authority riêng. Snapshot balance992 phải kiểm live trước một submit đã được duyệt.

## Điều kiện kiểm sau output

- Giữ originals, lấy native/hash/probe/PCM; kiểm chữ và vùng áo qua toàn bộ frame, map lại time nếu đổi timing. Đối soát mặt/môi/tay/đạo cụ/performance với T02 theo frame tương ứng.
- Hash/tương quan PCM không thay nghe thực và sync; T02 gốc chưa nghe/duyệt. Không tự mux tiếng để che edit đã đổi audio hoặc gọi sạch hình là cả BM đạt.
- Reviewer nguồn/range và cổng owner nghe/xem thực vẫn bắt buộc; chưa có clean fullword range, voice/lip-sync/joins PASS. Contact Đào ngoài khung UNKNOWN.
- Backend từ chối hoặc output lỗi: STOP/HOLD, ghi số dư/thực chi, không retry hoặc đổi scope. Root đọc toàn report rồi trình proposal; không có blocker giấy buộc sửa draft trước trình owner.
