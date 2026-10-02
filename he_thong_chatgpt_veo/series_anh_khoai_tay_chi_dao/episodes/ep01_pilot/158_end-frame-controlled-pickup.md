# Thử kiểm soát động tác bằng khung kết thúc

## Quyền và mục tiêu

Owner yêu cầu tiếp tục sửa, chỉ gửi bản qua kiểm nội bộ để test. Sau 156/157 còn 54 credit thử, số dư Flow 554; không dùng Quality. Không đổi kịch bản 32, giọng K20/D06 hoặc tự khóa hình production.

## Chuẩn bị END

Dùng skill imagegen, built-in image tool, edit từ `C:/Users/PC/Downloads/du_an_nem_bui/T2-CODEX-OPEN_v0.7.png`. Không dùng Gemini API hoặc CLI. Nguồn không bị ghi đè. Ảnh mới `C:/Users/PC/Downloads/du_an_nem_bui/158_end_frame_control/END_hold_v0.1.png`, SHA-256 `0E42DDD4703C38EB8E2AA9ADC4DF938968AD421AC3A85130203208DB9FE811BD`.

Prompt ảnh: giữ camera/crop/nền/ánh sáng/nhân vật/trang phục và toàn bộ bàn; Khoai dùng tay phải giải phẫu giữ hai đũa đúng hướng, kẹp ít nem thấp trên đĩa; Đào quay đầu/mắt sang cốc và giữ cốc bằng tay trái; hai bát, rau, hai chấm, cốc và đũa Đào không đổi. Không ăn/đút ăn/chữ/hơi. Đây là edit giữ identity, không tạo lại nhân vật.

Kiểm actual: giữ đủ hai bát và đạo cụ chính, Đào nhìn sang cốc, nem chưa chạm miệng. Nem nằm trên bát Khoai thay vì trực tiếp trên đĩa; chỉ dùng làm nguồn thử giữ vật dưới miệng, không tuyên bố mọi yêu cầu ảnh đạt hoặc owner duyệt. Mắt/mặt cần kiểm production sau. END mới là thử nghiệm, không canon. Nạp END qua file chooser Flow; START vẫn OPEN7.

## Prompt video thực tế

```text
Static tripod shot connecting the exact supplied first and last frames. Preserve both adult fruit characters, faces, clothing, lighting, background and the full table inventory throughout. Dao turns her head and eyes toward her glass on screen right and rests her anatomical left hand around it, as in the final frame. Khoai uses his anatomical right hand to pick up his existing wooden chopsticks, pinches a small tuft from the central cool shredded nem plate, then lifts that same tuft to the low position shown in the final frame. He holds the tuft there steadily with his lips closed and jaw still. The movement ends in the exact supplied final pose. Both personal bowls stay present and unchanged through the entire shot; herb plate, two dipping saucers, glass and Dao's chopsticks stay in their original places. Keep the two wooden sticks continuous and the tuft visibly pinched between their eating tips. Soft street ambience, silent characters, stationary camera, native watermark.
```

Veo Lite Frames/9:16/720p/8s/x3, kiểm giá trước gửi. Kiểm đủ file, toàn cảnh và dày điểm dừng; chưa có nghe thì không chứng nhận không lời. Hai khung đầu/cuối đúng không chứng minh đường chuyển động đúng. Chưa reviewer độc lập.

## Kết quả

Đã nạp START/END và chạy một batch ba Lite. Tải đủ ba native MP4, H.264 720×1280/24fps/8s + AAC, giải mã không lỗi. Chưa nghe audio. Số dư 554 → 524, ròng 30; khoản thử còn 24. Tổng chi phí video trong lượt tiếp tục này: 90 credit, chín đầu ra thành công (156–158). Quality riêng chưa dùng. Không quy chi phí ảnh built-in vào Flow hoặc tuyên bố chi phí ảnh bằng không.

| Mã | Asset ID | SHA-256 MP4 |
| --- | --- | --- |
| E01 | c1fdd1cb-93bc-4feb-b33f-c3d2b79ab448 | 262A3DD8E5FA6492A1EF078B57AC78F0444ACF4630FE9241B2AC48217B8D5834 |
| E02 | 471ede4e-4365-4bab-a2c7-4b66e440ca0c | 302BF71057FEA93DF7B72487D2485F8C691543462910691E24563D0D653746C3 |
| E03 | eb8d7ee6-e33f-44bf-a300-f92e1b5ca873 | 4D0B5111129D04F1E906CFD029B5FC0FF42EFA0CF97C86EEC05E88FBB9BEEE58 |

Thư mục cùng END chứa E01/E02/E03.mp4, contact sheets 16 khung ở 2 fps, lưới cuối 15 khung từ 5,5 giây ở 6 fps, preflight.png, results-flow.png, balance.png. Người điều phối xem đủ các lưới.

- END được thể hiện ở cuối: Đào nhìn ra phía cốc, Khoai giữ nem thấp. Tuy nhiên Đào vẫn nhìn Khoai trong phần gắp trước đó; nhịp lén gắp chưa đúng.
- E01 giữ nem chưa ăn trong ảnh kiểm đoạn cuối, nhưng nâng gần miệng rồi hạ; trạng thái và vị trí bát Khoai thay đổi trong các khung giữa. Chưa qua kiểm liên tục đạo cụ.
- E02 đưa nem vào miệng rõ rồi trở lại END còn nem; không đạt vật lý/liên tục phần nem.
- E03 đưa nem sát miệng và có biểu hiện ăn; chưa chứng nhận không chạm miệng. Bát và quỹ đạo giữa hai khung vẫn không đạt.

**Chưa có bản qua kiểm nội bộ để gửi owner test.** Không gửi các bản lỗi làm ứng viên đạt, không ghép thoại/trao bát/Quality. Một khung cuối đẹp không thay kiểm đường chuyển động. Khung END là thử nghiệm, chưa owner duyệt và chưa sản xuất chính thức.

## Bước tiếp theo và giới hạn

Không lặp prompt-only cùng một chuỗi toàn cảnh. Chuẩn bị cặp khung cho cận cảnh tay/đĩa với một chuyển động gắp; tách cảnh Đào quay lấy cốc và cảnh phát hiện theo kịch bản, kiểm điểm nối trước khi chạy. Giữ các bát/rau/chấm trong inventory dù nằm ngoài crop; không crop chỉ để che lỗi đã có. Đây là đề xuất thử kỹ thuật, không tự đổi kịch bản hay duyệt đạo diễn production.

Ngân sách còn 24 không đủ một batch x3 Lite ở giá hiện tại 30. Dừng gửi generation mới, không lấy Quality hoặc toàn bộ số dư tài khoản làm quyền chi. Cần owner cấp thêm ít nhất 6 credit để có một batch x3, hoặc cho phép x2 trong phần còn lại. Chuẩn bị tài liệu không tiêu credit có thể tiếp tục; không hứa sẽ chạy nền sau khi kết thúc lượt.
