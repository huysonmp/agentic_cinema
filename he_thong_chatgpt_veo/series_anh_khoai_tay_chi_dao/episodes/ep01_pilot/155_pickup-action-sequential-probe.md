# Thử tuần tự động tác gắp — nhịp đầu

Owner yêu cầu làm tuần tự và tiếp tục. Đối chiếu kịch bản32: Đào quay sang lấy cốc, không nhìn phố như root diễn giải nhầm trước đó. Chuỗi đầy đủ: gắp về miệng → bị nhìn thấy → đổi hướng → nhận bằng bát → đặt nem vào bát. Không đút ăn/romance, không miếng đã chạm miệng.

Lượt này chỉ nhịp đầu, chưa chuyển bát/thoại. Đã đọc quyết định62 và xem I03/I05 local; dáng/hướng grip owner chọn giữ làm mốc review, không áp yêu cầu phải lộ ngón cái. Không gắn hai ảnh studio vào Frames vì chúng không phải cảnh bàn ăn; không tuyên bố model đã nhận các ảnh grip. Dùng OPEN7 đã có làm START; END trống. Preset K20/D06 giữ quyết định nhưng không dùng cho test không thoại. Không tự duyệt voice hoặc đổi pipeline production.

Veo3.1 Lite, Frames,9:16,720p,8s,x3, quote30. Ngân sách bổ sung còn134 trước thử; Quality riêng chưa dùng. Chỉ một batch; đánh giá trước nhịp trao món. Skill computer-use cho thao tác UI; browser cũ không còn, khôi phục tab cùng project trên IAB hiện hành5.

## Prompt actual

```text
Use the supplied starting frame for an eight-second physical action test, one locked tripod shot. Keep the exact adult 3D anthropomorphic potato Khoai on screen left and adult 3D anthropomorphic peach fruit Dao on screen right, original faces, clothes, lighting, street-side eatery and complete table layout. The central plate holds a cool loose mound of irregular short pork and pork-skin strips coated with roasted rice powder.

First Dao turns toward the water glass on her outside right and reaches her right hand to grasp that glass, briefly looking away from Khoai. While she is looking at the glass, Khoai uses his anatomical RIGHT hand, on screen left, to pick up HIS existing pair of wooden chopsticks from beside his bowl. He holds their thicker blunt handles; the long narrow eating tips extend beyond his fingers toward the food. The lower stick stays supported while the upper stick closes to pinch ONE small irregular tuft of nem from the central plate. Show contact with the food, then lift that same tuft clear of the plate. Khoai brings it toward his own mouth. Dao turns her face back toward Khoai, still holding her own glass. When their eyes meet, Khoai pauses with that same tuft suspended short of his closed mouth, giving a tiny caught-in-the-act look. End there.

This tests only the first action beat; no dialogue or mouth contact, no eating, no feeding or transfer yet. Keep the tuft visibly held between the two eating tips, not stuck to fingers or floating. Both wooden sticks remain continuous, proportional and connected to the same hand. His left hand rests beside his bowl. Other food, leaf plate, dipping saucers, bowls and chopsticks remain on the table in their original places. Clear restrained facial reactions, not exaggerated panic. Quiet street ambience only, no music, speech, captions or camera movement. Preserve the native watermark.
```

## Gate

Kiểm thời gian/quỹ đạo: cốc đúng của Đào; đúng tay, hai đũa hướng đầu ăn; tiếp xúc/nâng cùng phần nem; dừng trước miệng; gặp ánh mắt. Không kết luận toàn cảnh đạt từ một động tác tốt. Người điều phối tự kiểm ảnh mẫu; chưa có reviewer độc lập hoặc nghiệm thu của owner.

## Kết quả thực tế — 2026-10-02

Một batch yêu cầu ba đầu ra: hai video thành công, một lỗi tạo âm thanh; Flow thông báo không tính phí đầu ra lỗi. Không thử lại. Số dư 634 → 614, ròng 20 credit; khoản thử bổ sung 200 còn 114. Quality riêng chưa dùng.

| Mã | Asset Flow | SHA-256 file MP4 |
| --- | --- | --- |
| A01 | f4f24738-fe70-4bd5-836c-87f57113616e | EA8D6469C83BFEEDC22786B1F88DDEAACE1673457F1BF9B97344012CE0910399 |
| A02 | b08eed12-0a8b-4112-8d4f-ceca2c348f92 | 058F9CE631F2584E001892521C32E8DCB1FC1FA2EAD20CA5AEFF3D01AB196255 |

Thư mục `C:/Users/PC/Downloads/du_an_nem_bui/155_pickup_action`: `A01.mp4`, `A02.mp4`, `preflight.png`, `results-flow.png`. Tải qua menu 720p kích thước gốc. Cả hai H.264 720×1280, 24 fps, 8 giây, stream AAC; giải mã toàn file không lỗi. Chưa nghe audio, không chứng nhận không có lời từ metadata.

Kiểm từng clip qua 16 khung cách 0,5 giây (`A01-contact.jpg`, `A02-contact.jpg`), bổ sung 15 khung cuối từ 5,5 giây ở 6 fps (`A01-end.jpg`, `A02-end.jpg`).

- Cả hai có Khoai lấy đũa, tiếp xúc đĩa, nâng nem. Chưa thấy cầm đảo đầu ăn rõ ràng trong ảnh kiểm; chưa chứng nhận grip hoặc hình món đạt toàn bộ.
- A01: phần nem biến mất sát miệng ở đoạn cuối, có biểu hiện ăn và hạ đũa rỗng. **Không đạt trạng thái kết thúc giữ nem trước miệng.**
- A02: mở miệng, đưa nem vào miệng rồi rút đũa. **Không đạt điều kiện chưa chạm miệng.**
- Đào dùng tay trái theo giải phẫu (phía phải màn hình), không phải tay phải ghi trong prompt. Prompt lẫn hướng màn hình và tay giải phẫu: cốc ở ngoài bên phải màn hình, gần tay trái Đào. Đây là lỗi lập kế hoạch đầu vào; kịch bản chưa khóa tay lấy cốc.
- Đào chưa quay đi đủ rõ, nhịp lén gắp/bị bắt gặp còn yếu. Giữ được nhân vật rau quả trong ảnh kiểm không thay kiểm mặt, trang phục, món và continuity chi tiết.

**Chưa có take đạt để chuyển sang trao nem vào bát, ghép thoại hoặc Quality.** Không dùng khung cuối đã ăn làm nguồn cho động tác gắp cho Đào. OPEN7 vẫn là nguồn thử, không tự thành nguồn production hoặc nối được với bàn T-NB03 v0.8.

## Truy nguyên nhân và bước kế tiếp

Đã xác định lỗi chỉ định tay lấy cốc trong prompt và kết quả vượt điểm dừng. Giả thuyết cần thử: hướng chuyển động “toward his own mouth” trong chuỗi nhiều hành động khiến Veo hoàn tất động tác ăn dù có câu cấm. Hai mẫu chưa xác nhận cơ chế hoặc từ gây lỗi.

Tiếp theo thử riêng nhấc nem lên ngang ngực và giữ nguyên phần nem; sửa tay Đào theo vị trí cốc, làm rõ ánh mắt quay đi. Đây là chia nhỏ phép thử, không đổi kịch bản đã duyệt. Khi giữ vật/điểm dừng đạt mới thử gần miệng/bị phát hiện, rồi chuyển vào bát; thoại K20/D06 tích hợp sau. Bộ sửa chưa gửi trong hồ sơ này.
