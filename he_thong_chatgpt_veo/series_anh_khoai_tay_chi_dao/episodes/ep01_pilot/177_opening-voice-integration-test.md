# 177 — Thử audio hai câu mở với K20–D06

Ngày: 2026-10-04. Owner trả lời **“ok”** cho đề nghị bổ sung **tối đa 21 credit**, ba mẫu hai câu mở ở 176. Duyệt đúng bước thử này, không toàn bộ cảnh thiếu, Quality hoặc bản cuối.

## Quyền chi

Trần hợp nhất 134 + 21 bổ sung = **155 credit**; trước lượt đã chi 130, còn 25. Phép thử này không vượt 21; khoản 4 cũ không tự mở rộng trần phép thử. Giá/model kiểm trực tiếp trước tạo; không xem toàn bộ số dư account là quyền chi.

## Yêu cầu và nguồn

Giữ script 32: Đào “Anh nhìn mãi. Không hợp thì để em.”; Khoai “Khoan. Mùi này làm anh nhớ cái chảo.”. Không thêm lời, không dùng A03 của bộ 170. Giữ K20 ID `fb1188da-e6c8-4156-9bba-0576c01a8da6`, D06 ID `0ce1551e-e74b-481c-bb9e-d31e04f8b352`; ảnh OPEN7 ID `43057def-574c-4ca7-916c-d55083f9b670`.

Gói dự thảo: `evidence/176/opening-test-draft.md`; kế thừa route 175: **Omni 1.1 Flash / Thành phần / dọc / 360p / 10 giây / x3**, không phải Veo Lite. Hình chỉ dùng kiểm đối chứng, không mặc định cảnh sản xuất. Kiểm đầu vào và ảnh chụp cuối trước submit; tên preset không thay token audio đúng ID.

## Trạng thái thực thi

**THREE_NATIVE_DECODED / OWNER_OPENING_LISTENING_PENDING.** Đã nhận, tải và giải mã đủ ba file. Kiểm trực tiếp đúng cấu hình ở trên, giá 21, Tác nhân tắt; account trước 296. Readback ba chip (OPEN7 + hai audio), token đúng ID và hai câu đúng script; xem ảnh chụp cuối rồi submit một lần, không đổi đầu vào sau kiểm. Không tạo lại, thử thêm hoặc nâng Quality.

Khôi phục trước submit: sửa ở trang chi tiết bị mất khi quay về trang tạo; tái dùng prompt từ menu ô grid tại trang tạo. Lần chọn bằng phím tắt không xóa hết đoạn cũ; đã phát hiện qua readback và xóa chính xác text cũ bằng chọn text/BackSpace. Final readback chỉ còn L01–L02, không còn bốn câu giữa. Không có generation/charge trong các lần sửa này. Bằng chứng và prompt thực tại `evidence/177/` và screenshot trong folder owner.

Folder owner: `C:/Users/PC/Downloads/du_an_nem_bui/177_opening_voice/`. Giữ tất cả ba kết quả/native/hash/PCM và QC. Đã ráp đối chiếu với B01 bộ 175 trong bản nháp riêng có nhãn; audio chưa owner chấp nhận không nhập âm thầm vào bản đã duyệt. ASR không thay kiểm nghe chất giọng, vai hoặc phát âm; không tự đổi script để ép timing.

## Kết quả và review giới hạn

Folder trên đã có file thực. A01/A02/A03 đặt theo ba ô mới từ trái sang phải, không phải bộ A của 170. Native filename chung `Characters_speaking_dialogue_at_…`, hậu tố tải lần lượt `20261004214303`, `20261004214431`, `20261004214451`.

| Mẫu | Media ID | Bytes | Thời gian lời theo ASR | Hình qua kiểm khung mẫu |
| --- | --- | ---: | --- | --- |
| A01 | 2da4f3fb-7ab5-44ff-8f86-80eeb4948020 | 1.006.915 | 0,76–3,48s và 4,28–8,46s | Khoai mất trang phục; không dùng hình. |
| A02 | a053520b-6765-46be-8b47-7a8081229b11 | 897.275 | 0,70–3,22s và 3,72–6,28s | Đổi tỷ lệ bàn/món, áo Đào có nơ mới, thiếu đĩa lá/cốc trong khung; không dùng hình. |
| A03 | eac27f20-f059-48f6-a5cb-ef30f50a1e52 | 868.151 | 0–3,10s và 3,84–6,38s | Tự thêm chữ ở khoảng 5s; mặt/bố cục khác nguồn; không dùng hình. |

Ba MP4: H.264, 360 × 640, 24 fps, 10,005s, AAC 48 kHz stereo; full decode sạch. WAV `A01_VOICE_REVIEW.wav` đến A03 là PCM16bit 48 kHz stereo, 1.921.038 byte/file; **PCM MP4/WAV khớp cả ba**, không thay gain, tốc độ hoặc âm sắc. Hash và timing tại `evidence/177/results.json` và bản sao folder owner.

QC offline dùng faster-whisper small / CPU / int8 / tiếng Việt, không initial prompt hoặc API. Cả ba ASR nhận “chào” thay “chảo”; A01 còn nhận “Khoai, khoan”. Đây là chỉ điểm nghe lại, **chưa kết luận phát âm sai hoặc đọc tên vai**. Mean/max dBFS lần lượt A01 −18,5/−0,1; A02 −18,2/−0,6; A03 −18,2/−0,8. Không dùng số đo peak để tự chứng nhận không méo hoặc chất giọng tốt. Root chưa nghe độc lập, không ghi agent đã chấm diễn/identity/lip-sync.

Đã xem mỗi mẫu một khung/giây, không toàn bộ chuyển động; cả ba **VISUAL_REWORK**. Phạm vi thử vẫn là audio hai câu mở. Không sửa hình lẻ tẻ hoặc dùng hình thử làm cảnh bàn giao.

## Ráp trong ngữ cảnh, không đổi lời

- Ba file `A01_9-cau_REVIEW.wav` đến A03: mỗi file 28,01s, ghép **toàn bộ audio mở → B01 giữa của175 → R01 cuối của154**, không khoảng hành động và không cắt lời. Kiểm PCM output bằng đúng phép nối ba nguồn, không gain/tốc độ hoặc đảo/lặp đoạn. Chỉ phục vụ nghe mạch và đối chiếu chất giọng; không chứng minh phim30s hoàn tất.
- `story_review_A02/EP01_30s_PLANNING_v0.4.mp4`: bản nháp đủ chín captions với audio mở A02 **CHƯA DUYỆT**, giữa đã được chấp nhận và cuối được phép tái dùng. A02 là lựa chọn làm việc theo timing, không winner giọng.
- Audio mở lấy đoạn **0,50–6,50s** vào timeline0–6s; ASR kết thúc lời6,28s, mức thấp liên tục từ6,317583s. Đây là cơ sở trim tạm, không nghe kiểm cuối âm. Giữ WAV gốc để đối soát; không cắt còn6s ngay từ nguồn0 vì sẽ bỏ cuối câu. Caption mở từ script32, timing theo ASR trừ offset0,50s.
- Bản nháp30s kiểm kỹ thuật đạt: 720 × 1280, 24 fps, decode sạch, chín captions đúng script32, hash nguồn khớp, timeline liên tục. Bytes3.073.006; SHA256 `69505f6bb53fac3258c261a3b4cb0c01b77ae61c30018c87155e9948f0d390e8`.
- Đã xem contact sheet: nhãn audio mở CHƯA DUYỆT và các chỗ thiếu hình rõ trong khung. Vẫn27,5s ảnh tạm +2,5s C01, chưa lip-sync/diễn hình/continuity/overlay, không phải bản cuối hoặc Quality. Không ghi chín câu audio đúng tuyệt đối chỉ vì captions khớp.

## Tải và ngân sách thực

Menu native360p trong tab tải riêng đã tải đủ ba file. A01 tín hiệu download-event hết45s nhưng **file thực đã có**, không tạo lại hoặc bấm tải lại mù. A02/A03 có toast và file thực; căn cứ bàn giao là bytes/hash/decode. Đã đóng tab tải, để tab dự án A02 cho owner nghe.

Account **296 → 275**, chi21 đúng trần. Lũy kế **151/155**, còn **4 credit được phép chi**; không coi account275 là quyền chi. Dựng nháp, nối PCM và ASR cục bộ chi Flow0. Không tự mở khoản thêm90 trước đây.

## Tổng kết và quyết định tiếp

- Đã xác định: tạo/tải/kiểm đủ ba native và WAV; hai câu đúng trong prompt; bộ mới chi21; audio mới chưa owner duyệt.
- Đã chốt: bổ sung21 cho đúng phép thử; giữ K20/D06/script32; không Quality hoặc sinh hình thêm.
- Giả định: A02 thuận tiện ráp thử theo timing; trim0,50–6,50s còn đủ lời theo gợi ý công cụ, cần nghe xác nhận.
- Còn mở: identity/nhịp và chữ “chảo” của audio mới; dấu hiệu “Khoai” A01; cảnh hình/continuity và gate cuối; RCA170 chưa đóng.
- Tiếp: owner nghe A02 trong bản ráp; có thể so A01/A03 qua gói nghe. Nếu chấp nhận nguồn mở thì ghi phạm vi, chuyển sang phần hình thiếu đã liệt kê176 và trình dự toán riêng trước tạo. Không yêu cầu tuyển lại giọng hoặc tự sửa lời sau approval.
