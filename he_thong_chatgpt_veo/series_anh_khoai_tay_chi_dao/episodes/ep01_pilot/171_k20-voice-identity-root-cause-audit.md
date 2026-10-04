# 171 — Truy nguyên nhân giọng Khoai khác K20 đã chọn

**Bằng chứng tiếp nối — 174:** owner tạm chấp nhận cả ba control173 có input đã kiểm. Giữ K20 làm baseline tích hợp; chưa chứng minh nguyên nhân sai giọng170 hoặc từng biện pháp là nguyên nhân khắc phục. RCA về cơ chế sinh vẫn mở.172 không được dùng làm control hợp lệ.

Ngày2026-10-04. Yêu cầu chẩn đoán, không tạo media hoặc tiêu credit. Trạng thái **PROCESS_GAPS_CONFIRMED / GENERATION_CAUSE_UNRESOLVED**; chưa đóng RCA.

**Diễn biến sau171:** owner duyệt control21 tại [172](172_k20-single-speaker-control.md). Bộ đã tạo nhưng root gỡ OPEN7 trong preflight, **INVALID_CONTROL**; không dùng bộ này đóng RCA hoặc chứng minh H1–H4.172 xác nhận lỗi thao tác ở chính bộ172, không quy ngược170. Số dư/quyền chi hiện hành xem172, không dùng snapshot dưới làm hiện hành.

## 1. Lỗi và chuẩn đối chiếu

Owner nhận xét giọng nam không giống giọng đã chọn khi nghe gói mở đầu170. Ghi **OWNER_REPORTED_IDENTITY_MISMATCH** cho A03/B01 đang trình nghe; chưa đủ thông tin để quy riêng accent, cao độ, cộng hưởng hoặc một từ. B02/B03 chưa có verdict nghe riêng. Không thu hồi giọng Đào hoặc audio cuối R01 theo suy diễn.

Chuẩn: Khoai K20 Orus tùy chỉnh, ID `fb1188da-e6c8-4156-9bba-0576c01a8da6`; K12 cùng tên nhưng ID `5fbe4f2a-1581-4ec1-9ef2-0a5b9fa64886`. Giữ [152](152_owner-selected-voice-pair-k20-d06.md) và script32. Approval audition không phải nghiệm thu tích hợp.

## 2. Chuỗi bằng chứng kiểm thực

| Mắt xích | Kết quả | Giới hạn |
| --- | --- | --- |
| K20 thư viện live | Sample109 ký tự và performance khớp148/149; DOM audio chứa đúng ID K20, duration8,76s, readyState4 | Mẫu còn nguyên cấu hình; chưa có baseline file/hash để so byte với lần owner nghe |
| Lịch sử A03/B01 | Tên Orus tùy chỉnh; mở nghe tham chiếu trả nguồn `undefined`, readyState0. B01 tạo chip lỗi trong nháp sửa; đã xóa chip, không submit | Bất thường UI hiện tại, không chứng minh server thiếu nguồn khi sinh video ngày03 |
| Chọn nguồn170 | Nhật ký ghi đối chiếu performance custom K20/D06 | Chưa có bằng chứng trực tiếp đủ mạnh cho exact historical request→source→server sử dụng |
| Route | Omni1.1Flash/Thành phần/360p/9:16; A8s, B10s, x3 | Không phải Veo Lite; chưa chứng minh Quality sẽ sửa lỗi |
| File tải | Bốn SHA256 MP4 vẫn khớp media.json QC170 | Không có thay thế file sau QC |
| Tách WAV | PCM giải mã từ MP4 khớp WAV gốc stereo48kHz cả bốn mẫu | Loại trừ extraction làm đổi giọng, không xác nhận giọng sinh ra đúng |
| Review | Root chưa thực nghe/so identity; có decode/ASR/thống kê | ASR/âm lượng không thay kiểm người nói, accent, âm sắc hoặc truyền cảm |

Đính chính phát biểu trước: “đã chắc chắn gắn đúng nguồn” mạnh hơn bằng chứng. Có mẫu live đúng K20 và nhật ký chọn theo performance, nhưng chưa xác minh trọn exact historical server binding. Không kết luận đã chọn nhầm K12, cũng không loại trừ tuyệt đối lỗi liên kết nguồn. Resource đã tải vào trình duyệt không đủ chứng minh tài nguyên được request cụ thể sử dụng.

## 3. Loại trừ hậu kỳ — phép đo thực

FFmpeg9.0.2 đã có: giải mã audio từng MP4/WAV sang PCM16bit, giữ sample rate/channel, `-f hash -`. Hai hash trong mỗi cặp bằng nhau:

| Cặp | SHA256 PCM chung |
| --- | --- |
| A03 | `9d6c6d99594e65c3b488cbfbcf2c6b07e7f2384095024f67de7a66f77de323b0` |
| B01 | `c1af7a51644294b2b5e8a676834bb20534bfa9585b3724f89693e97cbefe575e` |
| B02 | `54bcdaf0f3dc55da0e80286020dabc4da4eb4b0fe0b59ca066f946bfe0e3fbdd` |
| B03 | `0c5f31be401a90c953d1f3c2329a5c6004fcdf34ec36c47a0ae6733a96bcddfa` |

File tại `C:/Users/PC/Downloads/du_an_nem_bui/170_opening_voice_blocks/`; QC gốc tại `artifacts/voice-qc/170-*`. WAV nghe không resample/time-stretch/chỉnh giọng. Không kiểm hệ loa/phát lại của owner bằng phép đo này.

## 4. Nguyên nhân gốc ở quy trình — đã xác định

1. **Chưa xác nhận chuyển mẫu nghe sang video giữ được giọng.** 152 chốt selection;153/154 chưa integration PASS. Đến170 chưa có đối chứng một người nói cùng sample audition trước khi dùng cặp thoại mới. Gắn preset không đồng nghĩa đầu ra đúng identity.
2. **Thay nhiều biến trước đối chứng.** Preview→video, một→hai người, câu, thời lượng, chỉ dẫn diễn cùng đổi. Kết quả khác không phân biệt nguồn/cách diễn/phân vai/khả năng tuyến sinh.
3. **Gate identity chưa thực kiểm bằng nghe.** Agent/contract đã thiết kế nhưng actual mới decode/ASR/ảnh mẫu. Owner là người phát hiện sai giọng.170 ghi pending đúng; giải thích nguồn trước RCA quá chắc chắn.
4. **Thiếu bằng chứng nguồn bền vững theo request.** Chưa có baseline audio local/hash và liên kết exact source đủ mạnh; tên preset trùng nên kiểm tên không đủ.

Các điểm này giải thích vì sao lỗi chưa được ngăn/định vị sớm, không phải bằng chứng cơ chế trực tiếp khiến model đổi giọng. Thêm agent trên giấy không tự khắc phục thiếu năng lực nghe/đối chứng.

## 5. Giả thuyết sinh lỗi — chưa chốt

| Giả thuyết | Bằng chứng và phần chưa biết | Phép thử phân biệt |
| --- | --- | --- |
| H1: tham chiếu không liên kết/áp dụng đúng | History nghe undefined, tên trùng; nhưng K20 live hoạt động và170 ghi đối chiếu performance | Chọn K20 trực tiếp từ thư viện, lưu bằng chứng trước gửi, một người nói sample gốc; không reuse chip lỗi |
| H2: cách diễn mới đổi cảm nhận âm sắc |170 thêm warm/low/intimate và nhịp riêng; Khoan lặng hơn audition. Trầm/ấm/thân mật vốn phù hợp K20, chưa chứng minh mâu thuẫn | Sau control đạt, giữ lời/nguồn/hình/model/thời lượng, chỉ đổi lớp diễn |
| H3: hai giọng/phân vai ảnh hưởng ổn định | Audition một người,170 hai người; chưa control video một người | Sau control đạt, thêm D06 nhưng Đào im lặng; rồi turn-taking ở nhánh riêng |
| H4: preview→video không giữ identity đủ tốt | Preview được chọn, video bị báo khác; chưa seed/model revision/control cùng sample | Control cùng sample/performance trên video; nếu vẫn lệch sau kiểm nguồn, dừng thử diễn và xem lại tuyến âm thanh |

Prompt170 gọi attached custom Orus/Aoede, chưa dùng token `@Voice` trực tiếp. [Google Flow hướng dẫn](https://support.google.com/flow/answer/16353334?hl=en) chọn giọng và tham chiếu trực tiếp bằng `@Voice`, custom có base/performance. Không suy token là bắt buộc, thiếu token là nguyên nhân đã chứng minh hoặc thêm token bảo đảm clone chính xác. [Khả năng model](https://support.google.com/flow/answer/16352836?hl=en) phân biệt Omni/Veo; không coi các tuyến thử là một.

## 6. Phép thử kế tiếp đề xuất — NOT_RUN

**C0: K20 một người nói, cùng sample audition**, không thoại Đào, không thêm âm sắc mới:

> Hồi bé, mỗi lần mẹ rang gạo trong bếp, anh cứ đứng cạnh cái chảo, đợi mẹ quay lưng. Khoan! Anh gắp cho em mà.

OPEN7 diagnostic-only; Omni1.1Flash/Thành phần/360p/9:16/10s/x3.10s tránh ép sample8,76s vào8s. Giữ common/performance K20; dùng tham chiếu thực do UI hỗ trợ, kiểm exact nguồn và lưu prompt trước gửi; không sửa preset đã duyệt. Quote lịch sử21, phải đọc giá actual. Bộ Omni chẩn đoán, không gọi ba Lite. Chưa chạy/chi/ghi owner duyệt C0.

Gate owner so nghe trực tiếp K20: identity, Bắc/Hà Nội, ấm/chắc/bo âm, nhịp nhớ mẹ, phản xạ/chữa cháy. Tách identity với performance; đúng lời không đủ PASS. Nếu không có reviewer nghe thực thì ghi rõ, không thay bằng ASR. Nếu cả bộ lệch, không sinh thêm ba kiểu diễn mù; xác minh reference/tuyến và trình lựa chọn âm thanh. Nếu có mẫu sát, chỉ thêm từng lớp biến, giữ đủ cả ba kết quả. Một mẫu tốt không chứng minh ổn định/nhân quả. Sample chỉ chẩn đoán, không đổi script production.

Ngân sách giữ nguyên:67 được phép chi theo170; account267 là snapshot ngày03, chưa đọc lại hôm nay. Nếu C0 được duyệt/giá21 thì còn46, ảnh hưởng coverage. Khoản thêm90 chưa duyệt; không tự mở ngân sách.

## 7. Bằng chứng UI và giới hạn

Folder `C:/Users/PC/Downloads/du_an_nem_bui/171_voice_identity_rca/`: `K20-library-verified.png` là thư viện thực đúng performance và nguồn đã kiểm; `B01-history-reference.png` là popover lịch sử. `K20-library.png` chụp trang trắng sau tải thất bại, **không dùng làm bằng chứng**. DownloadMedia audio chưa xuất file và chuyển tab sang media; đã trở về Flow. Không fetch signed URL ngoài UI. Không export được không có nghĩa library không phát được: DOM audio đã tải đủ8,76s. Không khẳng định đã nghe bằng tai trong lượt này.

## 8. Tổng kết vòng

- Đã xác định: PCM nguyên vẹn; K20 live đúng ID/performance; bất thường nghe lịch sử; thiếu đối chứng/gate nghe tích hợp.
- Đã chốt: giữ K20/D06/script32, không đưa A03/B01 vào master khi owner báo sai identity; không generation/credit.
- Giả định: lời/performance và hai người có thể ảnh hưởng giọng, chưa chứng minh.
- Còn mở: exact historical binding, cơ chế/thuộc tính lệch; RCA chưa đóng.
- Tiếp: xin xác nhận C0x3 tối đa21, kiểm giá/nguồn rồi so nghe thật trước lớp thử sau.
