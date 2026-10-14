# REC307 — EDIT/continuity: phạm vi sửa local và nối thử C06→C07

Ngày 14/10/2026. Reviewer độc lập `/root/c07_edit_context_307` chỉ đọc tài liệu, hash và xem ảnh có sẵn; không browser/API/credit/Git, không sửa media hoặc EDL. Đây là **CONTEXT_AND_ACCEPTANCE_CHECKLIST**, chưa phải đánh giá bản sửa chưa được tạo.

## Nguồn và quyền đã kiểm

Đã đọc đầy đủ root305, actual độc lập305, root306, registry305/306, approval tiếng306, root300 và approval range300; EDL cục bộ257/268/276/299 cùng rough35 approval264. Bản REC276 dùng C06_T03 [0,57) là lịch sử, không được lấy lại thay C06_KEEP_A đã chốt tại REC300. EDL299 còn nhãn pending lịch sử; approval300 là quyết định nối tiếp, không sửa hồi tố trạng thái của299. Không tìm thấy một EDL toàn phim mới đã hợp nhất C07 vào production trong tập hồ sơ này.

Tự tính lại SHA-256, khớp:

- Native C06_KEEP_A298: `0174cf58e30699f59e74c1cef1157dd560999802afa751cead5ee41b462ec639`.
- Native C07_TWOREF305: `12a0baa2d7ccedfaa16631b7cddd2c4331480e4fa8784880403eb425a8fb397b`.
- Bản review C07 [0,72) owner nghe: `7a7d2bc4d4fdd7a4ec220daa67477e3063583d1b2f9366a089318b9ab1104e18`.

Approval306 xác nhận đúng một D06, đủ N07 và nhịp ở **đúng bản3s**, không xác nhận hình, range production, lip-sync hay C08. User vừa giao làm bước sửa local và yêu cầu agent kiểm; root cần ghi quyết định mới riêng, không đổi `local_visual_repair_authorized=false` trong snapshot306 thành lịch sử đã duyệt.

## Kiểm đầu và đuôi bằng ảnh thực

Trực tiếp xem full720×1280 C06 native F47/ảnh START300; C07 native F0/F4/F5/F14/F15/F48/F64/F71. Xem năm board full16_01..05, đủ F0–79, gồm toàn range ứng viên F0–71 và biên ngoài. Chỉ **ALL_FRAME_STILLS_IN_CANDIDATE_RANGE**, không nghe hoặc xem AV liên tục.

- C06 F47→C07 F0: cùng trục hai người, mặt/pose, hai bát, cốc nâng, A trên đũa, rau, hai đồ chấm và đũa nghỉ gần khớp; không thấy reset lớn hoặc đổi chủ thể. Nem A/ánh sáng/texture có sai biệt re-encode/sinh mới, không exact-pixel seam PASS. Cần xem actual encoded cut; đây là ứng viên nối hợp lý trên stills.
- F5–14: Khoai có chuỗi mở–khép môi trong khi chỉ Đào nói N07; F4 và F15 là khung ngoài vùng sửa có môi khép. Không chữa bằng trim đầu vì có thể mất đầu “Thế”, không đổi line hay diễn thành ngạc nhiên để miễn lỗi.
- F48/F64/F71: Đào dùng tay trong giữ đúng bát mình, đã rời chỗ cũ; cốc vẫn ở tay ngoài và ngoài bát. A còn kẹp, chưa thả/cho vào miệng/gắp lại. Bát Khoai vẫn trên bàn. Đuôi F71 không thấy bát thứ ba.
- Phần bát nâng và tay đỡ chồng hình trước tay nghỉ Khoai; khoảng hở phía sau bị che. Không thấy xuyên tay rõ trên ảnh đã xem, nhưng **CLEARANCE_NOT_CERTIFIED**. Vùng sửa miệng không được nhận công trạng sửa physics; mọi lỗi props mới vẫn phải đánh giá độc lập.
- F71 Đào đang chớp mắt; endpoint trong range3s là F71, không phải F72/F76/F95. Đây không tự động là frame tốt nhất cho C08. Nếu khảo sát endpoint khác, phải ghi range mới và kiểm nhịp/độ dài; không tự dùng native đuôi lỗi hoặc redraw thay nguồn.

## Chỉ dẫn dựng bản local — acceptance checklist

1. **Phạm vi:** sửa duy nhất vùng miệng Khoai trên native F5–14 (10F), lấy môi khép từ chính native305 và tracking phù hợp từng frame. Không thay mắt/mày/gương mặt toàn bộ, không sửa Đào, tay, bát/cốc/đũa/A/món, background, watermark; không thêm credit hoặc sinh lại voice.
2. **Ngoài vùng sửa:** giữ pixel nguyên trước encode trong mọi vùng ngoài mask và mọi frame ngoài F5–14. Ghi ROI/mask/frame list và pixel-diff evidence; bản H.264 re-encode có sai biệt nén toàn khung nên không tuyên bố pixel-exact trên output lossy. Lưu bản trung gian/evidence đủ để tách sửa chủ ý khỏi sai số codec.
3. **Biên sửa:** kiểm full/crop từng F4–15, đặc biệt transition F4→5 và F14→15; không môi kép, răng còn sót, viền sáng/tối, texture bị đứng, miệng trượt, ánh sáng nhảy hoặc freeze toàn đầu. Reviewer nhìn bảng toàn72F và full critical để bắt lỗi ngoài vùng.
4. **Tiếng:** remux nguyên track AAC từ **bản3s được owner nghe**, không từ native4s rồi trim lại tùy ý. Không revoice/re-encode/đổi gain/pitch/speed/cắt đầu/dời tiếng/crossfade. Chứng minh compressed audio packet payload hoặc decoded PCM và timestamp/codec/duration khớp bản approved; file hash đổi do hình sửa không làm mất provenance tiếng nếu chứng minh được stream giữ nguyên. Remux không tự chứng nhận lip-sync/AV của bản mới.
5. **Range/timing:** output vẫn72F/24fps,720×1280,3s; đủ trọn N07 đã chốt, không lấy phần bát nhân đôi F77+. Không padding/freeze/đổi tốc độ để cứu timing. Full decode, probe, stream comparison và hash trước/sau bắt buộc.
6. **Nối thử:** C06native298 [0,48) + bản sửa C07 [0,72), tổng120F/5s; cut ởF48/2s. Kiểm encoded F40–55 cùng full F47/F48; correct speaker owner N06=Khoai/K20 rồi N07=Đào/D06, hai mặt nhìn thấy, người nghe không phát âm. Check không click/pop, mất đuôi “mà”, nuốt đầu “Thế”, chồng tiếng hoặc môi–tiếng lệch. Bản nối là review-only, không sửa EDL production. Nếu audio của join phải AAC encode mới do concat, ghi rõ không bit-exact và đừng đánh đồng với remux của bản3s.
7. **Đuôi/ownership:** C07 [0,72) vẫn hai bát, inner Dao=bát riêng, outer Dao=cốc, outer Khoai=đũa cùng A, inner Khoai=tay nghỉ. Chưa thả A và chưa ăn. Kiểm clearance thực không giấu bằng crop; nếu không thể đọc vì occlusion thì ghi hạn chế, không bịa collision hoặc physics PASS.

## Timing toàn tập — không quên phần kết

Mốc hiện hành từ hồ sơ268/300: qua C05=632F/26,333333s; thêm C06[0,48) thành680F/28,333333s. Nếu C07 đủ72F sau sửa được chọn, qua C07=752F/31,333333s.

| Ngưỡng | Phần còn lại sau C07 ứng viên3s | Ý nghĩa |
| --- | --- | --- |
| Final30 =720F | **−32F / −1,333333s** | Đã quá30 trước thả/C09; chưa đạt final30. |
| Rough35 =840F | **88F /3,666667s** | Chỉ khoảng còn cho nhịp thả/thu đũa và C09; chưa có actual chứng minh đủ. |

Rough35 được REC264 cho phép để giữ trọn lời và nhịp, không phải chốt final35. Không bỏ C09, cắt từ, tăng tốc hoặc ngụy trang số học như phần còn lại đã làm xong. Food/A seam C05→C06 còn blocker production riêng, không được sửa miệng C07 rồi ghi toàn phim đạt.

## Kết luận cho root

**Có thể làm thử local và nối review-only theo checklist; chưa production PASS.** Không cần hỏi owner lại các thao tác tracking/mask/remux/hash/đọc frame trong phạm vi vừa giao. Root và reviewer tự chọn/loại draft kỹ thuật, trình một gói đã kiểm thay vì từng thao tác nhỏ.

Blockers trước promotion: (1) bản sửa thực phải qua pixel-scope/biên/nhịp mặt; (2) preserved audio và encoded cut attribution/lip-sync cần evidence; (3) clearance/endpoint C08 chưa chốt; (4) food seam C05→C06; (5) actual thả/C09 và final30 chưa có phương án đã chứng minh. Không đề nghị paid retry, ngân sách mới hoặc bỏ lời ở report này. Reviewer không nghe, không cấp FULL_AV_PASS hoặc C08 authorization.
