# REC283 — Maker preflight: sửa chất liệu nem trên bản nối C05→C06

Ngày 13-10-2026. **LOCAL_MAKER_PREFLIGHT / PREPARATION_HOLD / NOT_SUBMITTED.** Vai maker tích hợp DIR, DOP, ACT, EDIT và PROMPT theo quyền local REC217; không là phản biện độc lập, không là media PASS hay quyền chi.

## 1. Phạm vi và bằng chứng thực

Đã đọc đầy đủ REC217, REC281, REC282, brief nhận–bỏ REC281, screening món và root review ảnh REC282, approval ảnh REC283, EDL REC276 và approval bản nối REC277. Đã kiểm SHA-256 của đúng clip local dưới đây; khớp authority. Trực tiếp xem ba ảnh: START v1 REC282, C05 T02 native F32 và C06 prefix F28. Phạm vi xem là **SAMPLED_STILLS**, không xem toàn bộ 123 khung, không nghe thực hoặc xem AV liên tục. Approval nghe/AV có nguồn là owner REC277, không chuyển thành maker đã nghe.

Nguồn đề xuất duy nhất:

- File: `C:/Users/PC/Downloads/du_an_nem_bui/276_C05_C06_JOIN/C05_C06_5p125S_JOIN_QC_NOT_FINAL.mp4`.
- SHA-256: `42d826e1356ce67acc6e1057b4ceefc9703f3e705ffa14ae6c09dea7934b5bdf`.
- 123 khung, 24 fps, 5,125 giây; C05 [0,66), C06 [66,123); điểm cắt F66 / 2,75 giây. C06 chỉ prefix [0,57), không đưa full native với tail bị bác trở lại.
- REC277 duyệt đủ âm cuối N05/N06, thứ tự Đào→Khoai, nhịp thoại và điểm cắt trên exact hash. Không duyệt toàn phim, món sau rework hoặc output sửa mới.

Ingredient hình đề xuất duy nhất:

- `02_refs/RECEIVE_START_food_v1_CHATGPT_FOR_REVIEW_282.png`.
- SHA-256: `491575988bbbea26e16fda3a7f02401b874f9abcc24eda7cdef340764ab232d8`.
- Vai trò **FOOD_MATERIAL_ONLY**, lấy hình thái thịt/bì/thính trên đĩa và phần nhỏ trên đũa. Không lấy tư thế tay, camera, mặt, môi, biểu cảm hoặc bố cục ảnh để thay source clip.
- Owner REC283 duyệt ảnh tham chiếu. Không dùng END v2 vào phép sửa này, vì clip này chưa thực hiện nhịp đưa bát–bỏ nem. END v1 vẫn bị bác.

## 2. Đích nghệ thuật và bất biến theo vai

| Vai | Đích của phép sửa | Không được thay |
| --- | --- | --- |
| DIR | Giữ đối đáp phát hiện–chữa cháy, sửa món để chuyện đọc đúng, không thêm beat | Thứ tự N05→N06; không biến clip thành cảnh nhận/bỏ món, không bỏ C09 hoặc đổi quan hệ hai nhân vật |
| DOP | Đĩa và phần A có hình thái nem đã duyệt, còn đọc rõ hai mặt và vùng tay | Framing, góc máy, ánh sáng, màu da/trang phục, đường nhìn, độ sâu trường ảnh, vật dụng và dấu nền tảng của source |
| ACT | Giữ Đào nói rồi nghe và Khoai nghe rồi chữa cháy; A vẫn được giữ, chưa nhả vào bát | Diễn mặt/mắt, timing, bàn tay/đũa, cốc nâng của Đào, bát riêng và ý định chuyển động |
| EDIT | Sửa đúng một target đã chọn, giữ điểm cắt nội bộ | 123 khung, 24 fps, F66, không nội suy hòa tan cut; không thêm/đảo/cắt lời hoặc co giãn thời gian |
| PROMPT | Chỉ thay hình thái món: không lát đặc đồng dạng, không mì; vật liệu mới bám vật thể cũ | Không prompt dựng lại thoại/miệng, không voice preset mới, không dùng still như frame đích |

Quan sát ba still: nguồn C05/C06 có phần gắp đặc, gần chữ nhật; START có phần rời và thính rõ hơn. Tuy nhiên START đặt đũa/tay ở vị trí khác đáng kể, biểu cảm/mặt cũng khác. Đây là nguy cơ **reference pose leakage**, không phải một hình có thể áp nguyên xi lên mọi khung. Chỉ dẫn material-only giảm xung đột về ý đồ, không chứng minh model giữ được những bất biến trên.

Phần A mới cần đọc như một phần gắp nhỏ duy nhất cùng loại với đĩa, không tự phình thành suất lớn hoặc sinh thêm miếng. Không buộc số sợi ảnh START là định lượng vật lý chính xác. Đĩa giữ vị trí, vành và lượng tổng gần nguồn; chất liệu đổi không được làm đĩa mọc thức ăn hoặc rung/hóa lỏng. Không khói/hơi nóng, không nhập món khác từ ảnh thật.

## 3. Prompt đề xuất — chưa nhập UI, chưa trả phí

```text
Make only a local visual correction to the Nem Bui food in this source video: the food on the shared plate and the one small portion already held between Khoai's chopstick tips. Use the attached image ONLY as a reference for the food material, not for character poses, faces, framing, camera or action.

Replace the uniform solid rectangular slices with a loose mixture of irregular thin, softly curved pork-skin ribbons and small meat slivers lightly coated with fine toasted rice powder, matching the approved food reference. Keep the plate outline and position, and keep the held portion small and continuously gripped at the original chopstick tips. No steam, noodles, extra dishes, enlarged portions, extra pickup, release or deposit.

Retain the source video's existing duration, shot sequence and hard cut, framing, camera, lighting, characters, facial performances, lip movements, hands, chopsticks, bowls, raised drinking glass, other table objects and platform watermark. Retain the existing source sound and dialogue without replacement. Do not recreate, add, translate or alter speech. Do not transfer the reference image's pose or expression into the video. Change no other content.
```

Đây là một biến sửa hình thái món ở hai vùng liên quan, không thử đổi model/giọng/camera đồng thời. “Retain” là ý đồ và tiêu chí nghiệm thu, **không cam kết audio bit-exact hoặc khóa mask**. Không gọi thao tác là inpaint/mask nếu UI chỉ có video edit + ingredient và chưa có mask được kiểm.

## 4. Khả thi, giá và cổng trước chạy

Thông tin do root cung cấp trong dispatch: Google hiện công bố video edit tối đa 10 giây, giá 40 credit mọi độ dài/độ phân giải; saved voice chỉ ở Ingredients, không Frames. Maker không tự kiểm browser hoặc coi quote công bố là quote UI của request này. Source 5,125 giây phù hợp trần công bố nhưng chưa chứng minh UI tiếp nhận đúng segment, độ dài hoặc nguyên âm thanh.

**Chưa GO** cho tới khi root hoàn tất các điều kiện:

1. Đúng tài khoản/project, source hash, uploaded card và segment 0→5,125 giây; không tự chấp nhận UI làm tròn 6 giây nếu ảnh hưởng source.
2. Route là sửa **video nguồn** với một ingredient chất liệu, không Frames-to-video hoặc generation từ still. Không saved voice mới; tiếng lấy source. Không yêu cầu chỉnh speech/mouth.
3. Quote UI ghi đúng một lượt, 720p dọc theo source; audio giữ bật/giữ nguồn nếu UI có lựa chọn, Agent tắt. Giữ proof tính năng/cảnh báo/giá; nếu UI không xác nhận thông số thì ghi UNKNOWN, không nhận đã khóa.
4. Independent critic đã đọc/report đúng hash và scope, root tích hợp các bất đồng. Báo cáo maker này không thay critic.
5. Owner phê duyệt riêng **một request sửa, cap 40 credit, không tự retry**, vì vượt max 15 theo REC238. Modal upload chờ quyền phải xử lý tại root; không lặp xin quyền suy diễn hoặc vượt modal.

Sổ do root cung cấp: đã chi 217/500, còn 283; reserve 110 đóng. Một request 40 nếu được owner duyệt và thực debit: đã chi 257, còn 243; không mở reserve. Nếu dùng bucket retake hiện 46 thì còn 6, nhưng việc ghi bucket cần root đối soát và chốt rõ trong request. Không coi còn 173 ngoài reserve là quyền chạy hàng loạt; screening có chín đoạn, chín edits giá 40 là 360 và không phù hợp ngân sách này.

## 5. Checklist sau output và quy tắc STOP

**G0 — Nhận nguồn:** tải exact output, hash, native resolution/fps/duration/frame count, full decode. Giữ nguồn cũ, không ghi đè. Lưu request/output/quote/debit thật. UI success hoặc technical decode không là quality PASS.

**G1 — Hình và hành động:** trích toàn bộ khung với công cụ đã được phép, so đủ 123 khung và xem liên tục nếu có capability. So face/mouth/tay/đũa/cốc/bát/phông với source; A liên tục ở tips, không rơi/nhả/gắp lại hoặc vào miệng. So món trên đĩa và A với appearance approval, không chỉ hỏi “có khói không”. Kiểm cả khung bị che và khi vật thể xuất hiện lại, không chỉ F0/end.

**G2 — Cắt và lượng:** so F62–70 quanh cut F66; không morph hai lượt, reset pose, đổi lượng A hoặc đổi outline đĩa. So F0–4 và F118–122 để kiểm seam ngoài; source trước/sau hiện còn food rework, nên cải thiện nội bộ không đóng được toàn-film seam. Không tự mở nhịp nhận–bỏ trên endpoint mới nếu chưa đối soát hình thái/geometry.

**G3 — Tiếng và khẩu hình:** đo offset/duration/audio provenance và so waveform/PCM nếu công cụ có sẵn; kiểm thực N05/N06 đúng giọng–speaker–âm cuối–nhịp và miệng trên output. Owner REC277 duyệt nguồn không tự chuyển qua output. Nếu AI chưa nghe được, ghi HOLD và trình owner exact candidate; không dùng ASR thay heard_text. Nếu audio thay đổi, không tự chép audio cũ lên: chỉ cân nhắc sau khi chứng minh mouth/timing giữ và có AV review/authority phù hợp.

**G4 — Tích hợp:** critic độc lập ghi expected/observed theo frame/timecode; root read-back. Candidate chỉ được đề xuất thay range nếu food, visual invariants, acting, audio/sync và cut đủ bằng chứng. Không thay EDL bằng approval giấy hoặc gọi output này final.

STOP trước sinh nếu source/ingredient/route/quote không đúng, không edit được exact segment, xuất cảnh báo speech edit, cap vượt hoặc thiếu owner. STOP sau một lượt nếu MAJOR về mặt/miệng/voice/speaker, cut mất, A thả sớm, món sai hoặc quantity jump; giữ evidence và bóc layer, không tự retry. Nếu cùng MAJOR đã lặp hai lần theo REC238 thì đóng route/rework decision, không “thử thêm một lượt cho chắc”. Lỗi food-only không được xử bằng che mặt, cận đĩa chạy cả câu, mute/revoice hoặc bỏ beat không có authority.

## 6. Khuyến nghị maker và phần còn mở

**Khuyến nghị có điều kiện:** C05→C06 exact join là phạm vi sửa đầu tiên hợp lý vì vừa chứa plate + A, hai speaker và một cut đã duyệt; giữ thành công những bất biến này sẽ là bằng chứng hữu ích cho route. Độ khó cao hơn clip đơn: edit có thể làm mượt cut hoặc kéo pose từ START. Chưa có dữ liệu cho tỷ lệ thành công; không dự báo phần trăm đạt hoặc coi một lượt đạt sẽ chứng minh các cảnh khác.

Nếu output chỉ đúng món nhưng mất diễn/miệng/cut thì không chọn. Nếu UI không bảo toàn segment/cut, trình owner phương án chia nguồn và tổng giá mới trước chạy, không tự dùng full C06 bị bác. Sửa local/composite thức ăn động chưa nằm trong bằng chứng sửa vùng áo tĩnh; không dùng tiền lệ đó để hứa giữ chất lượng.

Đã chốt: reference appearance, source/range và scope ý đồ. Đang giả định: video edit có thể giữ các thành phần không được yêu cầu đổi; điều này bắt buộc kiểm trên output thật. Còn mở: upload permission, quote/config live, audio/cut preservation, independent critic, owner cap 40 và kế hoạch food dependencies các cảnh khác. Bước tiếp theo là hoàn tất preflight UI + critic rồi trình **một request cụ thể**, chưa sinh video hoặc mở tiếp nhịp nhận–bỏ.

Chi credit bởi maker: **0**. Không browser/API/cài công cụ/media edit/git. Báo cáo này là thiết kế phép sửa và sàng lọc input, không kết quả chạy.

## 7. Cập nhật live do root chuyển — supersedes dự toán 40 và upload HOLD ở trên

Root đã hoàn tất upload exact join, mở editor `/edit/a9912c46-8593-41d0-8d0c-1fe4894169d6`. Theo evidence root chuyển: UI có “Mô tả cách chỉnh sửa video này”, total `00:05:03`, một clip được chọn với outline trắng, model Omni 1.1 Flash; một ảnh START đã gắn, image ID `ff0578c3-808f-4504-bd5f-4b294b1c1906`; không END hoặc saved voice. Draft root đã dán/read-back. Tooltip nút Generate đang báo **12 credit**, có screenshot lưu tại folder owner REC283. **Chưa submit.** Maker không truy cập browser hoặc trực tiếp thấy screenshot này; các chi tiết live là evidence do root báo, không là tự kiểm của maker.

**Sửa cách hiểu ngân sách hiện hành:** 40 ở phần 4 là giá công bố được cung cấp lúc lập bản đầu, không phải quote UI cuối. Quote quan sát mới là 12, khác giá công bố; không tự giải thích nguyên nhân, không gọi 40 là giá chắc sẽ bị debit. Nếu owner duyệt một request ở quote 12 và thực debit đúng 12: tổng chi 229/500, còn 271; retake 46→34 nếu root chốt dùng bucket đó, reserve 110 giữ đóng. Đây vẫn chỉ là điều kiện tính, chưa có debit. Không xin cap 40 dựa trên dự toán cũ trong khi quote hiện báo 12; nếu quote đổi, phải trình/cập nhật riêng trước paid action.

**PREPARATION_HOLD vẫn giữ:** editor chưa hiện cấu hình rõ resolution, x1 và giữ audio; không có metadata video DOM, preview là image/canvas. Tổng `00:05:03` có vẻ phù hợp độ dài nguồn 5 giây 3 khung nhưng maker không kết luận đó là frame notation hay chứng minh output chính xác 123 khung. UI one-clip selection không chứng minh hard cut F66 và timing audio sẽ giữ. Root cần làm rõ phạm vi request/config bằng đúng UI có sẵn; những trường không kiểm được phải ghi UNKNOWN trong package, không gọi 720p/audio-keep/x1 đã khóa.

Giá 12 nằm dưới max15 không tự mở GO: đây là route sửa mới sau STOP280 và còn config uncertainty. Owner approval ảnh hoặc “tiếp tục” không là approval riêng cho request trả phí. Trước chạy cần critic, root tích hợp, owner chốt exact request/cap theo quote hiện hành và các unknown được nêu. Nếu UI không cho xác nhận một bất biến thiết yếu, trình hạn chế/đề xuất bounded action cho owner thay vì suy diễn.

### Đối chiếu exact draft root

Maker đã đọc đầy đủ `04_requests/C05_C06_food_only_edit_DRAFT_283.txt`, là prompt root nhập, **không thay bằng đoạn đề xuất ở phần 3**. Draft giữ đúng đích food-material-only, không sao chép pose/expression/light/composition/quantity/endpoint; giữ phần A nhỏ theo vị trí/trajectory/size; ngăn release/feeding/new pickup/steam; giữ hai-shot cut, duration, source audio/dialogue và platform markings. Không yêu cầu tái tạo speech/mouth. Đây là brief phù hợp về nội dung; chưa có substantive gap buộc viết lại prompt nghệ thuật trước khi làm rõ route/config.

Hai điểm tinh chỉnh tùy chọn, không lý do tự sinh thêm: (1) thêm “not noodles” nếu cần ngăn toàn bộ món thành sợi mì; (2) thêm source cut at 2.75 s / frame 66 và total 5.125 s nếu editor/model chấp nhận chỉ dẫn frame/time chính xác. Các số liệu này cần tương ứng source thật và không làm UI re-time clip. Việc không ghi chúng không được xem là bằng chứng sai đã xảy ra; output vẫn phải kiểm full duration/frame/cut.

Kết luận cập nhật: **đã chuẩn source + ingredient + draft trong live editor; chưa GO, chưa output, chưa chất lượng PASS**. Phần còn mở là quote discrepancy, config/segment bảo toàn, critic và paid approval mới. Maker không chi credit hoặc thay đổi media.
