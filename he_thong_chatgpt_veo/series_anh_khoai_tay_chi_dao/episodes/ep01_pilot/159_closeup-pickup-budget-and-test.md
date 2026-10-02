# Cận cảnh gắp — quyền thử bổ sung và kiểm một chuyển động

## Quyết định của owner

Sau khi được trình C01 kèm giới hạn riêng động tác gắp, owner trả lời “ok”. Ghi nhận chấp nhận C01 cho phạm vi này; chưa duyệt toàn tập, continuity, voice hoặc Quality. Tiếp nối ở hồ sơ 160.

Owner cấp tiếp 200 credit để test. Cộng 24 còn từ 158: **224 credit được phép dùng**, không phải toàn bộ số dư tài khoản. Giữ bộ ba Lite theo quyết định trước; Quality riêng chưa dùng. Chỉ trình owner bản đã qua kiểm nội bộ, không tự duyệt tập hoàn chỉnh.

## Hướng thử tiếp

Tách cận cảnh tay/đĩa với một chuyển động kẹp và nhấc nem. Đây là thử kỹ thuật cho insert thuộc nhịp gắp trong kịch bản 32, không thay nội dung câu chuyện hoặc tự khóa phương án đạo diễn. Không crop video lỗi để che bát biến mất. Chuẩn bị khung mới từ nguồn bàn OPEN7 và dáng/hướng grip I05 đã được owner chỉ định ở 62. Không dùng I07/I09 hoặc yêu cầu phải lộ ngón cái. Chưa tích hợp giọng K20/D06.

Ảnh START: đầu đũa ở hai bên một phần nem nhỏ trên ụ nem, chưa nhấc. Ảnh END sẽ chỉ đổi trạng thái kẹp/nhấc, giữ camera và đạo cụ. Hai bát, rau, hai chấm vẫn trong inventory; đầu/miệng ở ngoài khung cận để phép thử chỉ kiểm tay/món. Đường nối với toàn cảnh phải kiểm sau, không mặc định khớp.

Skill imagegen dùng built-in image tool để tạo hai khung có nguồn, skill computer-use dùng UI Flow. Không Gemini API/CLI. Nguồn gốc không ghi đè, không tuyên bố phí ảnh built-in bằng không.

## Tiêu chí kiểm

Một cặp đũa liên tục; giữ phía cán, đầu ăn kẹp phần nem; nem cùng một phần từ tiếp xúc đến nhấc; không biến dạng thành mì/cuộn; không vật lơ lửng/xuyên tay; ánh sáng và vật dụng không đổi; không hơi/chữ thừa. Kiểm native download/decode, toàn chuỗi và dày đoạn gắp. Chưa nghe thì không chứng nhận audio. Người điều phối tự kiểm, không giả nhận agent độc lập đã chạy.

## Kết quả

Đã gửi một bộ x3 Veo 3.1 - Lite, Frames, dọc 9:16, 720p/8 giây. Giá hiển thị trước gửi: 30 credit. Khoản được phép thử đầu lượt: 224 = 24 còn lại + 200 owner cấp thêm; Quality riêng không sử dụng.

### Đối soát và review actual

- Kết quả: một thành công, hai lỗi tạo âm thanh; UI nói hai lỗi không tính phí. Không có đủ ba file để so sánh; không retry mù.
- Số dư actual screenshot: **514**, lần trước 524. Ròng **10 credit**, trial còn **214**, Quality riêng chưa dùng. Owner cấp quyền tiêu thêm, không phải xác nhận tài khoản được nạp thêm.
- C01 Flow ID `9fe75de1-947d-4c2a-bcf7-ca16287426bf`. Native download `C:/Users/PC/Downloads/Hand_lifting_food_with_chopsticks_20261002223354.mp4`; bản lưu `C:/Users/PC/Downloads/du_an_nem_bui/159_closeup_pickup/C01.mp4`.
- ffprobe: H264, 720x1280, 24fps, 8s, AAC. Giải mã toàn bộ sạch. Chưa nghe/nghiệm thu ambience; probe không có thoại.
- Kiểm ảnh mỗi 0,5s toàn clip và 6fps từ 2,5–5s: đầu đũa kẹp nem ở ụ, nhấc phần nhỏ rồi giữ. Hai bát, hai chấm, rau, cốc còn trong khung kiểm; chưa thấy khói/chữ thừa. Không khẳng định kiểm từng frame 24fps. Không có đầu/miệng trong khung, do đó không chứng minh khả năng dừng trước miệng.
- **Ứng viên đạt kiểm hình sơ bộ cho riêng cơ học gắp**; chưa production PASS, chưa canon camera, chưa tái lập trên ba thành công. Gần 3s mới nhấc; nhịp dựng còn phải xử lý.
- Proof `results-flow.png`, `balance-after.png`; QC `C01-grid.png`, `C01-pickup-dense.png`, cùng folder 159.
- Tiếp: kiểm nối insert với cảnh rộng Đào lấy cốc, Khoai gần miệng nhưng chưa ăn rồi chuyển vào bát. Giữ trục máy/đạo cụ. Tiếp tục bộ x3 Lite và phí actual; chưa chuyển Quality.

SHA256 START: `F36E0DFDDEA3F46F7513D43B1DF40F9DE6C02535999BA26BE2EFB9E19B66560D`.
SHA256 END: `0A69E0A66F174177D3549FA1BDC2AC5F55BA729FE7DFD81910327A6B413EEA88`.
Proof settings: `C:/Users/PC/Downloads/du_an_nem_bui/159_closeup_pickup/preflight.png`.

### Prompt video thực tế

```text
Locked tripod close-up insert of the supplied table and potato-textured right hand. Match the supplied first and last frames. The two wooden chopsticks close their narrow eating tips around one small loose tuft of cool nem from the top of the mound, then the hand gently lifts that same tuft just clear of the mound and holds it steadily at the final-frame height. This is one continuous small pickup movement. Preserve the same grip, two continuous wooden sticks and visible contact with the same tuft throughout. The plate, remainder of the mound, two bowls, two dipping saucers, leaf plate and glass stay fixed in their original positions. Preserve the warm light, camera, crop and short irregular rice-powder-coated pork and pork-skin strips. Only the hand, chopsticks and pinched tuft move; hold the resulting pose through the end. Soft street ambience; no dialogue, graphics or camera motion. Preserve native watermark.
```

## Prompt ảnh START thực tế

```text
Use case: precise-object-edit / identity-preserve. Asset: 9:16 close-up insert START frame for the approved food story. Image 1 is the scene and table source; Image 2 is ONLY the approved direction/shape of Khoai's right-hand chopstick grip, not a scene or outfit replacement. Make a new camera insert closer to the original plate from the same front side of the table, camera looking slightly down. Keep the exact cool nem Bui short irregular pork/pork-skin strips coated with rice powder from Image 1, same round off-white plate, wooden tabletop, warm street lighting, leafy plate on screen left, dipping dishes left/rear and right/front and BOTH personal ceramic bowls at the rear. Show only Khoai's right golden potato-textured hand and dark cuff entering from upper-left, holding his existing two reddish wooden chopsticks at their thicker blunt handles, the long tapered eating ends extending toward the center of the nem. Use the general back-of-fingers visible grip direction of Image 2; do not require the thumb to face the camera. At this START pose the two tips are slightly apart and touch either side of a SMALL loose tuft at the TOP of the mound. No food lifted yet. Hands and sticks clearly readable with natural proportions, continuous wood. Heads and mouths entirely outside the framing, no other hands in frame. Do not move, remove or duplicate table objects; match their relative arrangement. Scene is a new insert, not a crop hiding a faulty video frame. Single portrait still, no labels or text, no vapor, no overlays, no montage.
```

## Prompt ảnh END thực tế

```text
Use case: precise-object-edit. Supplied image is the exact START frame and edit target. Create its END frame by changing ONLY the hand/chopstick/one-small-tuft state. Keep the camera, crop, lighting, background blur, wood grain, plate, food mound, leaves, BOTH ceramic bowls, TWO dipping saucers and water glass in exactly the same places and shapes. The same right potato-textured hand maintains the same grip on the two reddish wooden chopsticks. Close the narrow eating tips around ONE SMALL loose irregular tuft from the very top of the nem mound and lift that tuft just clear of the mound, leaving a small visible air gap beneath it. Raise the hand slightly while keeping its orientation, anatomy and dark jacket cuff unchanged. The two eating tips pinch the same short irregular rice-powder-coated strips, never a noodle bundle or a neat roll; the tuft is suspended between the two tips, not glued to fingers. No mouth/head in frame; all other elements untouched. No text, measurements, diagrams, vapor, overlay or montage. Single portrait frame with exact original aspect ratio.
```

Hai ảnh local: `C:/Users/PC/Downloads/du_an_nem_bui/159_closeup_pickup/START_contact_v0.1.png`, `END_lift_v0.1.png`. Người điều phối đã xem actual: cùng bố cục, đủ hai bát/hai chấm/cốc/rau, đúng hướng đũa và phần nem nhỏ nhấc khỏi ụ. Chưa canon hoặc nghiệm thu owner; grip cơ học trong chuyển động vẫn phải thử. Không nạp ảnh studio grip vào Veo: ảnh đó chỉ nạp vào bước dựng START bằng imagegen.
