# 176 — Chấp nhận test giọng, ráp lại mạch EP01

Ngày: 2026-10-04. Owner: **“giọng test ok r đó, next đi”**.

## Quyết định và giới hạn

Chấp nhận bộ test giọng 175 để chuyển sang bước tích hợp; giữ Khoai K20 (Orus tùy chỉnh) và Đào D06 (Aoede tùy chỉnh). Không tuyển lại giọng. Owner không chỉ định winner B01/B02/B03 hoặc đánh giá riêng từng chữ; không suy rằng cả ba đã được nghe chấm độc lập. B01 là lựa chọn làm việc của root cho bản ráp, không phải winner owner đã chọn.

Approval này không nghiệm thu hình bộ 175, đồng bộ môi, cảnh chuyển nem, toàn tập, Quality hoặc ngân sách mới. Giữ nguyên chín câu trong kịch bản [32](32_p5-script-c-v0.5-approved-content.md). Audio cuối R01 được tái dùng theo [168](168_budget-approval-and-close-reaction-test.md), không phải approval mới suy từ câu này. RCA 170/171 vẫn mở về cơ chế sinh lệch; chấp nhận test không chứng minh nguyên nhân đã được sửa.

## Đầu ra thực hiện trong vòng này

Folder: `C:/Users/PC/Downloads/du_an_nem_bui/176_story_assembly/`.

- `EP01_30s_PLANNING_v0.3.mp4`: bản kiểm mạch, không phải video bàn giao.
- `manifest.json`: nguồn, hash, thời điểm hình/audio, captions và trạng thái từng phần.
- `technical-qc.json`: kiểm cấu trúc, đối chiếu captions với kịch bản 32, giải mã và hash.
- `animatic-contact.png`: 15 khung mẫu để kiểm bố cục chữ/nhãn; không thay kiểm chuyển động hoặc nghe.
- `176_REPORT.md`: bản sao tài liệu này cho owner.

Thực tế: **30,000 giây, 720 × 1280, 24 fps, H.264/AAC**, 2.932.347 byte; SHA256 `840fddcac8f8cb7d0a4a6a45b065fe3801f08ace8919c2ea3ae2123fa1bc3c08`. Đây là upscale phục vụ đọc bản nháp, không nâng chất lượng nguồn hoặc gọi bản Quality. Giải mã toàn file sạch; chín captions khớp đúng vai và nguyên văn script 32; timeline hình liên tục 0–30 giây. Đầu 0–5,9 giây kiểm PCM hoàn toàn im lặng, không đưa audio Khoai từng bị phản hồi lệch vào nháp.

Đã xem contact sheet: chữ/nhãn nằm trong khung, thể hiện các khoảng thiếu. Bản nháp có **27,5 giây ảnh tạm và 2,5 giây video gắp**, không phải nghiệm thu một hình thức phim ảnh tĩnh. Cắt từ toàn bàn sang cận tay rồi trở lại các ảnh pose còn thay crop/bố cục; không che thành continuity đạt. Không dùng hình B01/B02/B03 bộ 175 cho master.

## Bảng nối lời — nguồn — mạch chuyện

| Câu | Lời giữ nguyên | Vị trí dự kiến | Nguồn và trạng thái |
| --- | --- | --- | --- |
| L01 Đào | Anh nhìn mãi. Không hợp thì để em. | 0–3s | Chỉ caption; **thiếu audio đạt**. Đào thấy Khoai chần chừ, không phán xét món. |
| L02 Khoai | Khoan. Mùi này làm anh nhớ cái chảo. | 3–6s | Chỉ caption; **thiếu audio đạt**. Đây là tiền đề bắt buộc cho câu hỏi “Chảo ở đâu?”. |
| L03 Đào | Nem thì đây. Chảo ở đâu? | 6–8s | B01 của 175, đoạn nguồn 0–2s; test giọng được owner chấp nhận. |
| L04 Khoai | Bếp nhà anh, hồi bé. Mẹ rang gạo, anh đứng chờ. | 8,46–12,22s | B01 của 175, đoạn nguồn 2,46–6,22s. Ký ức hư cấu, không claim cách làm Nem Bùi của mẹ. |
| L05 Đào | Chờ ăn? | 12,82–13,54s | B01 của 175, đoạn nguồn 6,82–7,54s. |
| L06 Khoai | Chờ mẹ quay lưng. | 14,18–15,08s | B01 của 175, đoạn nguồn 8,18–9,08s; dẫn sang hành động lặp lại ở hiện tại. |
| L07 Đào | Chờ em quay lưng nữa à? | 22–23,90s | R01 của 154, đoạn nguồn 0–1,90s; tái dùng theo 168. |
| L08 Khoai | Anh gắp cho em mà. | 24,62–25,84s | R01 của 154, đoạn nguồn 2,62–3,84s; chưa có cảnh chuyển hướng/gắp vào bát. |
| L09 Đào | Thế em quay lại đúng lúc rồi. | 26,74–28,34s | R01 của 154, đoạn nguồn 4,74–6,34s; chưa có cảnh nhận nem và kết. |

Audio giữa giữ nguyên toàn đoạn B01 10s, đặt ở 6–16s; audio cuối giữ nguyên R01 8s, đặt ở 22–30s. Không thay tốc độ, gain, preset, thêm nhạc hoặc chồng lời. Caption timing dùng gợi ý ASR để ráp; caption đúng chữ không chứng minh audio phát âm đúng chữ hoặc nói đúng vai. Root chưa nghe độc lập; những tín hiệu ASR “nem/chảo/rang/gắp” chưa được adjudicate riêng, không ép owner nghe lại trước khi làm bước có ích tiếp theo.

## Coverage hành động — không bỏ mất phần gây cười

| Nhịp | Slot tạm | Tình trạng và tiêu chí còn thiếu |
| --- | --- | --- |
| Chần chừ → liên tưởng → ký ức | 0–16s | OPEN7 ảnh tạm. Cần diễn tự nhiên, đúng mặt/trang phục và môi theo người nói; không flashback tự phát. |
| Đào quay lấy cốc | 16–17,5s | Thiếu video; Đào phải quay đi trước lúc Khoai lấy nem. |
| Khoai gắp một miếng | 17,5–20s | C01 nguồn159, source 2,75–5,25s; chỉ tái dùng ứng viên cơ học, nối cảnh chưa duyệt. |
| Đưa về mình → bị bắt gặp → khựng nhẹ | 20–24,6s | Hai ảnh pose tạm. Cần đường chuyển động và gaze; nem không chạm môi hoặc bị cắn. |
| Chữa cháy: chuyển nem vào bát Đào | 24,6–27s | Thiếu video. Không đút cho Đào; bát/đũa/miếng nem phải nối đúng trạng thái. |
| Đào nhận, trêu; Khoai gắp miếng khác | 27–30s | Thiếu video. Hành động nhận phải diễn ra cùng lời, không dồn toàn bộ sau câu cuối. |

Thời lượng từng slot là **giả định dựng**, chưa khóa duration diễn thực. Không rút gọn mất hành động để vừa 30s. Nếu clip mới không khớp nhịp, cần review lại cut; đổi lời phải trình revision, không sửa ngầm.

## Còn thiếu trước bản bàn giao

1. Audio hai câu mở L01–L02 dùng đúng K20/D06, nối được với B01 mà không đổi chất giọng.
2. Các cụm hình mở/diễn thoại, nâng–khựng–phản ứng và chuyển–nhận–kết. Việc tạo clip riêng không tự chứng minh nối cảnh đạt.
3. Kiểm trên bản ráp: đúng lời/vai, nhịp hài, continuity mặt–món–tay–đạo cụ–ánh sáng, chuyển cảnh, lip-sync và audio cuối.
4. Bố trí F01/F02/nhãn AI theo script32, kiểm đọc được và nguồn claim, xuất bản bàn giao rồi owner duyệt. Bản nháp nội bộ chưa triển khai các overlay này.

Không ghi các agent đã review nếu chưa có lượt chạy và bằng chứng. Vòng này là đối soát nguồn/cấu trúc do root thực hiện, không phải một hội đồng đạo diễn hoặc kiểm nghe độc lập.

## Ngân sách và bước kế tiếp

Vòng này dựng/kiểm cục bộ, **chi Flow 0**. Lũy kế vẫn **130/134**, còn **4 credit được phép chi**. Số dư account296 là snapshot175, không kiểm live ở lượt này; không lấy toàn bộ account làm quyền chi.

Đề xuất gần nhất: thử **hai câu mở** theo gói dự thảo `evidence/176/opening-test-draft.md`, ba mẫu cùng điều kiện; báo giá gần nhất của Omni10s x3 là **21 credit**, phải kiểm lại giá live. Đề nghị bổ sung tối đa21 credit riêng bước này; **chưa được duyệt, chưa chạy**. Chưa xin gộp ngân sách tạo mọi cảnh, chưa cam kết21 hoàn tất video. Mỗi bước tạo hình tiếp phải đối soát coverage và trình chi phí thực trước khi vượt quyền chi.

## Tổng kết vòng

- Đã xác định: owner chấp nhận test giọng175; mạch chín câu không đổi, lỗi trình bày test rời làm thiếu tiền đề được khắc phục bằng bản kiểm mạch.
- Đã chốt: giữ K20/D06; chuyển sang tích hợp; R01 audio cuối tái dùng theo168.
- Giả định: B01 làm nguồn tạm, vị trí audio6–16/22–30 và slot dựng; không mặc định winner hoặc final PASS.
- Còn mở: hai câu mở, diễn hình/continuity, nghe toàn mạch/đúng từng chữ, overlay và bản cuối; RCA cơ chế170 vẫn mở.
- Tiếp: owner xem nháp theo mạch, duyệt hoặc điều chỉnh ngân sách thử hai câu mở; sau đó kiểm và hoàn thiện hình theo thứ tự, không thay kịch bản.
