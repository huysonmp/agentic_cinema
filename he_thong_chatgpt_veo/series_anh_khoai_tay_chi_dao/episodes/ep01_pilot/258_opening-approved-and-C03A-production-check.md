# REC258 — Chốt mở đầu, sản xuất C03A và kiểm bản nối

## Điều đã xác định và quyết định đã chốt

Owner chọn A của REC257: chấp nhận ngoại lệ tư thế hai tay sát vành đầu đoạn BR và nhịp/hình–tiếng của đúng opening 13,75 giây. Quyết định ghi tại `restart_720p_v1/00_decisions/opening-join-and-BR-selection-258.json`; không chuyển thành duyệt native BR 4 giây hoặc các cảnh sau.

Ngày 09-10-2026 tiếp tục C03A theo scoped autonomy238. Cảnh này chỉ Đào hỏi **“Anh chờ ăn à?”** sau ký ức Khoai; Khoai nghe, hai người chưa gắp, chưa quay lấy ly. Không đổi kịch bản, preset hoặc công cụ.

## Đầu vào và thực thi

- Ảnh tham chiếu là khung cuối thực F180 của C02 đã chọn, không chỉnh sửa: hash `42417d1a4d9a350060f2db05b108f6109f757eba151432759a6da6d2a8cea492`, cloud UUID `2d80f77d-1c54-4991-a613-6571711c12aa`.
- Giọng Đào/D06 đúng saved preset `6dadc0b1-00c3-493c-943d-f4a1e4a88feb`, không kèm K20. Root đọc đầy đủ preflight độc lập; kiểm picker ID, hai chip, prompt readback, Omni 1.1 Flash/Ingredients/720p/9:16/4s/x1/Agent tắt và trả video không âm thanh tắt.
- Một submit, một output; job `d3dda26b-2cc3-41eb-81c7-715a3ec7780e`. Tải native bằng menu 720p kích thước gốc. UI xác nhận tải; đã kiểm bytes/giải mã, không dùng proxy thumbnail.
- Quote và khoản trừ cùng tab: **7 credit, 1.015→1.008**. Số dư trước cao hơn snapshot965 cũ 50; chưa xác định nguyên nhân, không coi đó là ngân sách thêm.

## Kết quả kiểm và bản trình owner

Native hash `051202d30ea7317b38ee74de8a690db48510940f3311543e208f2807b56b3b0c`, 720×1280, 24fps, 96 khung/4 giây, AAC stereo48kHz/4,01 giây, full decode sạch. Native được giữ nguyên.

Root đã xem đủ 96 khung qua 12 board: Đào có khẩu hình câu hỏi, bàn/đồ món ổn định, không gắp/kéo đĩa/hơi nóng/chữ thoại. Reviewer độc lập kiểm đủ96 khung, thêmPNG riêng: Khoai bắt đầu khe môi F42, mở rõ F43–47, khép lạiF49 và khe nhẹ F94–95; full native **HOLD**, không dùng nguyên4 giây. Root đã đọc đầy đủ report độc lập.

ASR offline không mồi kịch bản nhận “Anh chờ anh à?”, mốc cuối1,36 giây; từ “ăn” chưa được chứng nhận. Chỉ là bằng chứng nhận dạng, không kết luận âm thực chắc chắn sai và không sửa transcript thành lời mong muốn. Root/reviewer không có chứng nhận đã nghe giọng hoặc xem AV liên tục.

Candidate `[0,42)` gồm42 khung/1,75 giây giữ câu hỏi dự kiến và khoảng nghỉ, kết ở hai môi khép, loại trước Khoai hé môi. Reviewer xác định Đào khép ổn từF38, endpointF41 hợp; không coi F36 là đã khép chắc. Hash `ddf8fc6481bfc3ab9593d31cd528060359bec3cf0c0c758a0db98bacf1cfe463`; chưa chọn. Không đổi tốc độ/pitch, không vá môi/lồng giọng.

Bản nối QC opening+C03A dài **15,5 giây/372 khung**, hash `47b779559c643770a4cd63eb7ca5c65836df408d148a9eddd8789e51a8fb343d`. Root xem đủ48 khung encoded F324–371, gồm chỗ nối F330/13,75 giây và toàn C03A. C03A rộng hơn nhẹ, nhân vật nhỏ hơn so với C02: chưa coi là camera khóa tuyệt đối; trình owner xem chỗ đổi cỡ khung. Tiếng/hình derivative cùng gốc0; probe/full decode sạch, không chứng nhận lip-sync bằng kỹ thuật này.

Preview tại `C:/Users/PC/Downloads/du_an_nem_bui/258_C03A/EP01_OPENING_15p5S_OWNER_REVIEW.mp4`; bản riêng tại `C03A_1p75S_OWNER_REVIEW.mp4` cùng folder. Screenshot/preflight/native/khung/ASR lưu ở đó, không đưa ảnh tài khoản vào Git.

Reviewer xem đủ48 khung encoded, xác nhận seam nhìn thấy ởF330: nhân vật nhỏ/thấp hơn và tay ngoài Khoai đổi từ cạnh đũa sang gần bát. Không phải chỉ thay cỡ khung nhẹ hoặc exactsourcepositions PASS. Đã bổ sung câu hỏi owner chấp nhận **cả cỡ khung và tư thế tay** trên đúng chỗ nối này; không dùng ngoại lệ BR cho tay C03A. Kết luận độc lập **GO_FOR_OWNER_CANDIDATE_AV_AND_JOIN_CHECK**, chưa chọn/voice/sync/whole-film PASS. Dòng request pending trong report là snapshot trước cập nhật root; request hiện đã ghi nhận native và debit, không hiểu thành chưa submit để gửi lại.

## Giả định, vấn đề còn mở và bước tiếp

- D06 đã chọn là tham chiếu giọng; **waveform mới vẫn chờ nghe thực**. Owner được hỏi rõ giọng D06, “ăn à”, nhịp/khẩu hình và cỡ khung mới trên đúng bản nối.
- Bản cắt/nối chưa duyệt; C03B chưa submit. Không dùng acceptance opening cũ để duyệt phần nối mới.
- Đã dùng **122/500**, còn **378**: first-pass126, retake97, post-rough45, reserve110 đóng. Không tự retry hoặc dùng dư8 đợt BR đã đóng.
- Nếu candidate được nhận, phần mở đầu là15,5 giây, còn14,5 giây trong mục tiêu30 giây cho C03B và C04–C09. Đó là quỹ thời lượng, không phần trăm chất lượng hoàn tất; phải cập nhật bằng lời/hành vi/take thực, không ép thoại/tăng tốc để vừa.
- Tiếp theo: đọc hết review độc lập output/nối, ghi nhận owner checkpoint đúng hash/range; chỉ khi các gate đóng mới chuẩn bị C03B **Khoai: “Chờ mẹ quay lưng.”**. Nếu lời mới nghe sai thì sửa đúng lỗi trước, không tiếp diễn bằng script dự kiến.

## Hồ sơ đối soát

Request/prompt ở `04_requests/*258*`; preflight và kiểm native/ASR/derivative ở `06_qc/*258*`; bài học ở `09_lessons/REC258_single_speaker_tail_and_cut_gate.md`. Mốc257 trở xuống giữ lịch sử. Media cũ và các thay đổi ngoài phạm vi được giữ nguyên.
