# EP01 — Duyệt phản ứng ngắn, tiếp tục cảnh nâng/khựng tay

Ngày 2026-10-06. Owner trả lời: **“Duyệt phản ứng ngắn, tiếp tục theo ngân sách còn lại”**. Approval đúng bản cắt 0–0,625 giây/15 frame tại204, SHA256 `3470254b657ecc371fb29d7def13a972302b6f05f8ec5afb2e7cccc7996f7e81`; không duyệt cả clip tám giây có môi mở. Giữ nguyên tiếng202/C-v0.6/K20/D06.

[Timeline205-v0.3](evidence/205/timeline-v0.3.json) là bản làm việc hiện hành, chưa render phim cuối: S05 frame431–512, S06 frame512–527, S07 frame527–590. Bù21 frame phản ứng vào nhịp nâng/khựng tay Khoai; tổng720 frame/30 giây. U04 cần sáu giây sạch: dự kiến0–3,375s và3,375–6s, không dùng một range hai lần. Timing thoại không đổi; việc đạt nhịp vẫn phải kiểm actual.

## Kiểm nguồn U04

Root đã xem lại actual START: `C:/Users/PC/Downloads/du_an_nem_bui/192_approved_pickup_join/inputs/P02_APPROVED_OUT_frame59.png`; SHA256 đúng `db95be527d709dd39bb1107f5ac94a036bc480be28691d2c64b694112ae640c8`, 720×1280. Đây là frame cuối đoạn P02 đã chọn về nhịp, không thay bằng endpoint ảnh sinh188.

END ứng viên198 tái tạo làm đổi góc lòng bát, chi tiết món và ánh sáng. Không chứng nhận continuity hoặc upload như endpoint đã duyệt. Quyết định triển khai: **dùng START native duy nhất**, bỏ END tái tạo để tránh ép clip biến đổi đồ trên bàn theo nguồn khác. Đây là lựa chọn kỹ thuật trong gói sản xuất đã giao, không thêm lượt hoặc đổi câu chuyện. Endpoint chuyển động phải lấy từ output thật; không tự báo input một frame bảo đảm tay/món không biến dạng.

Chỉ đạo U04: nâng đúng một phần nem đã gắp, dừng trước cổ áo/miệng, giữ tay và miếng nem đến sáu giây; bát riêng còn rỗng, đĩa/rau/chấm và tay nghỉ không đổi; không nhai, thêm phần ăn hoặc hơi nóng. Mặt nằm ngoài khung, tiếng N05 ngoài hình. Phải kiểm quote/model/x1 và nguồn trước gửi, sau đó decode/frame/entry–exit; không chi lượt sửa nếu vượt dự phòng3.

Sổ trước U04:349/422/còn73. Dự kiến một x1 giá10 →359/còn63; sáu đơn vị sau dự kiến60, dự phòng3. Không coi số dư account127 là quyền chi. Chưa Quality/API/phát hành hoặc AV/master PASS.

## U04 đã thực thi và kiểm đầu ra

Flow đọc lại START đúng file, chỉ một ảnh đầu, END trống; DOM xác nhận Veo3.1-Lite/Frames/9:16/720p/8s/x1 quote10 và prompt khớp. Gửi một lần; account127→117, **chi10; sổ359/422/còn63**. Clip `f919a3e8-15da-4374-9a5d-5e786b26ad36` hoàn tất. Native một yêu cầu tải đã có trong Downloads dù event timeout20s, không retry; sao lưu/hash đối soát đúng. H264720×1280/24fps/8s/192 frame cóAAC, full decode sạch. **AAC của video không dùng**, giữ tiếng202 đã duyệt; bản xem hình loại audio hoàn toàn.

Root xem48 mẫu xuyên clip, đủ144 frame vùng tay/đũa/miếng nem trong0–6s và7 frame ở điểm nối bản ráp. Miếng nem còn ở tips, không thấy ăn/thả/gắp thêm; bát riêng rỗng và bộ bàn giữ bố cục nhận diện, không thấy hơi nóng trong mẫu toàn cảnh. Có **nâng rồi hạ nhẹ/settle**, không khớp tuyệt đối chỉ đạo nâng rồi giữ một cao độ. Giữ thành **ứng viên hình có sai lệch đạo diễn được ghi rõ**, chưa agent độc lập/diễn xuất/full-AV PASS hoặc owner duyệt phim cuối; không chi sửa tự động khi dự phòng3.

Native U04 SHA256 `8e41154c45e85ba4a3cad4d2e31d009f680bf93b2f7cebd70535cb1260c95a38`; chọn tạm0–6s cho working assembly theo hai range không lặp0–3,375 và3,375–6. Frame143 là đầu ra nối tiếp U06, SHA256 `2fcdb78f592c1e4ee25cfb5c571d8beb70eb99c465a717f6e9211bcb5b9a070e`. Cảnh U06 vẫn cần cho bát Đào vào khung rồi đổi hướng cùng miếng nem, không lấy nguồn189 đã có bát trên tay để giả đã thực hiện việc đưa bát.

Đã ráp **bản xem hình riêng9,125s/219 frame** theo P02→U04 nâng/khựng→U05 ngắn đã duyệt→U04 giữ. File owner `EP01_PICKUP_REACTION_HOLD_9.125S_PICTURE_REVIEW.mp4` trong folder205; chưa thoại/mix/phụ đề hoặc video30s. [Kết quả/range/hash](evidence/205/results-U04.json), [điểm nối đã xem](evidence/205/join-boundaries.png). Không kéo dài hình bằng freeze/loop/slowdown.

Kinh nghiệm xuất: stream-copy `-t6` với native B-frame cho146 frame/6,083333s. Đã giữ file chẩn đoán dưới tên `U04_STREAMCOPY_146FRAMES_NOT_FOR_TIMELINE.mp4`, không đưa vào dựng. Bản hiện hành dùng trim theo144 frame và encode, probe xác nhận6s/144 frame/no audio. Kiểm số frame sau xuất, không tin tên file hoặc tham số lệnh là độ dài actual.

Skill [computer-use](C:/Users/PC/.codex/plugins/cache/openai-bundled/computer-use/26.930.41038/skills/computer-use/SKILL.md) giúp kiểm UI đầu vào/quote trước gửi và nhận native; khi browser binding mất, đã đọc troubleshooting và nối lại đúng IAB/clip, không chuyển sang automation terminal hoặc gửi lặp. Bảng tài khoản đóng trước lưu ảnh công khai; không lưu email vào hồ sơ.

## Tổng hợp hiện hành

- Đã xác định/chốt: phản ứng15 frame đã owner duyệt; tiếng202 giữ nguyên; U04 đã tạo một lần và có ứng viên6s.
- Giả định: nhịp hạ nhẹ U04 có thể dùng như do dự trong bản ráp, cần đánh giá khi xem cùng toàn câu chuyện; không coi đó là chỉ đạo đã đạt100%.
- Còn mở: U06/U07/U08 và U01/U02/U03, điểm nối hình–tiếng, mix/phụ đề/master. Sáu lượt đầu dự kiến60 trong63 còn lại, không bảo đảm hoàn tất nếu lỗi.
- Tiếp: dùng native U04 frame143 chuẩn bị U06 đưa bát vào/đổi hướng; kiểm đầu vào rồi mới gửix1. Không sinh thêm U04/U05 hoặc Quality trong bước này.
