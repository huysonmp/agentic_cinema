# REC311 — C09 PICK B actual review độc lập

**BLOCKED_AS_BRIEF_CONFORMING / ROUGH_REVIEW_CANDIDATE_WITH_UNAPPROVED_PROP_EXCEPTION.** Nhìn thấy đúng nhiệm vụ B mới từ đĩa về Khoai, A ở bát Đào và ending hai người hiểu nhau. Tuy nhiên Đào hạ bát/cốc rồi **tay ngoài rời cốc, chuyển sang đỡ bát**, trái FINAL311. Không tự waive thành MINOR/PASS. Có thể giữ clip làm candidate để trình rough với sai lệch được công khai; muốn chọn giữ hành vi này phải chốt ngoại lệ và kiểm bản ghép thực, chưa có owner acceptance.

## Target, năng lực và kỹ thuật tự kiểm

- Target `05_native/EP01_720_C09_PICK_B_T01_NATIVE_311.mp4`; tự hash trước/sau kiểm: `d06160b0efbb2ee5e7188d4748ffe3ae915abb0036b31ec12ae52788affd72e3`, khớp evidence. Native được giữ nguyên.
- Tự chạy read-only ffprobe/count_frames: H264/720x1280/24fps/96F/video4,000s; có AAC48kHz/stereo4,010s, container4,010s/853335bytes. Tự full decode ffmpeg ra null, exit0, không lỗi. Binary đã có trong `.local-tools/ffmpeg/verified-9.0.2/ffmpeg-9.0.2-essentials_build/bin`. Không tạo/chỉnh media hoặc chạy paid.
- Đọc FINAL311/current preflight310/run311/native_evidence; tự FINALhash `5c853a7e0336a761e61166f3e5d01f3775cfe67b8805f1ac337282400cde90fa`, STARThash `e7dd6c786fd9c8d0982d9a4a67e2820aa66992ca4dcf4ce9bb1a7578f408f321`, khớp đã xem exact encodedC08F63. Run lúc đọc còn trạng thái submitted/waiting và chưa ghi debit/output; không suy đó là chưa có native khi file thực đã xác minh.
- Trực tiếp xem **đủ sáu full16 boards, mọi F0–95**, đếm96PNG. Mở riêng full720 native **F0,13,16,20,24,28,31,32,34,36,38,40,56–65(từng frame),68,72,79,80,84,95**. F là0-based; PNG file làF+1. Đây là all-frame still review và full critical samples; **không phát liên tục hoặc nghe**.

## Findings actual

| Frame | Quan sát độc lập |
| --- | --- |
| F0–12 | Kế thừa START: tips trống phíaKhoai, A trong bát Đào cầm tay trong, cốc nâng tay ngoài, bát riêng Khoai/tay nghỉ/props đúng. Không entry face/pose reset rõ. |
| F13–24 | Đào hạ và dời bát sang phải về gần bàn, hạ cốc; blink tự nhiên, miệng vẫn khép. F24 còn tay ngoài ôm cốc. **Sai giữ height đã xuất hiện trước B.** |
| F28–34 | Bát/cốc xuống sát tabletop; A vẫn thấy trong bát. Tay trong vẫn tiếp xúc bát; không kết luận bát đã hoàn toàn thả khỏi tay. Tay ngoài còn ở cốcF31–34; trạng thái raised glass đã mất. |
| F36–40 | Tay ngoài rời grip cốc và chuyển về mép phải bát. F40 thấy cốc đứng sau bát, hai tay Đào ở hai bên bát. **Visible hand-role change / glass set-down**, không còn outerhandholdingraisedglass của FINAL. Không fake pass dưới nhãn chỉ lowering. |
| F24–55 | Empty tips Khoai đi về plate, tiếp cận nem; không lấy lại A. F31–40 đọc được đũa tới phần đĩa phía gần/trái, sau đó ngậm một phần nem. Không thấy xuyênrim rõ, nhưng overlap chiếu2D gần resting hand không chứng nhận khoảng hở3D. |
| F56–65 | Một cụm B được nhấc từ plate; ribbon dài còn trên vùng đĩa lúc đầu, tớiF63–65 cụm đi tách lên về Khoai. A vẫn trong bátĐào, không clone/repeatedgift hoặc pickup thứ hai nhìn thấy. Phần B khá bung sợi, exact mass/từng sợi không thể bảo toàn-certify qua still. |
| F68–72 | B trên tips ở phíaKhoai, phía trên bát riêng, chưa mouth-contact; không thảB vào bát, ăn hoặc đổi người cầm. Dao outerhand tiếp tục đỡ bát, glass đứng thấp sau bát. |
| F73–79 | Blink và chuyển gaze từ món lên nhau; F79 Đào đang mở lại mắt, Khoai nhìnĐào, không speech mouth. |
| F80–95 | Hai người gặp mắt/nụ cười nhỏ; B vẫn trên đũa phíaKhoai, A trong bátĐào. Đúng ending bạn bè ăn ý, không surprise/triumph/review món. **Props sai brief vẫn tồn tại đến exitF95.** |

Toàn boards giữ Khoai trái/Đào phải trưởng thành/cùng đầu khoai–đào/cuống/lá và áo, hai bát cá nhân ngoài hai chén chấm, một glass, đĩa/rau/đũa nghỉ phải, watermark native. Không thấy spare bowl, A biến mất hoặc về đĩa, B hướng miệng, camera cut/zoom/reset, steam, mouth mở thành phát âm. Cốc/bát dịch chuyển là hành động thấy rõ, không thể gọi props completely preserved. Chất nem vẫn dạng sợi/mảnh; nhiệt độ/nguyên liệu thật không được xác thực từ hình.

## Mức độ, dựng được gì và quyết định còn thiếu

- **Sai lệch đáng kể ở take, không phải input/prompt thiếu guard:** FINAL nói “Her outer hand still holds the raised water glass” và “Do not put Dao's bowl or glass down”; hiện glass thấp/đứng trên bàn và outerhand chuyển sang bát. No put-down/hand-role giữ suốt clip không đạt. Đây là blocker để báo **conforming C09 PASS**, chưa đủ căn cứ gọi toàn chuyện A/B hỏng hoặc tự bắt buộc tạo lại trả phí.
- Core story giữ được A đã trao→B mới vềKhoai→nét hiểu nhau. Vì hạcốc diễn liên tục khi anh reach, về nghệ thuật có thể là hành vi đặt cốc sau khi nhận A rồi chuẩn bị ăn. **Đây chỉ là lựa chọn ngoại lệ đề xuất**, không retroactive approval. Nếu muốn giữ candidate, trình đúng đoạn hạ/đổi tay trong rough, xin chốt giữ hành vi thực hoặc xử lý; owner chưa chọn.
- Không sửa bằng tailtrim đơn giản: sai đã từF13–40, B chỉ nhấcF56–65, gazeendingF80+. Cắt trước sai thì chưa cóB; giữ đoạnB/cuối đơn lẻ làm jump height/hand/glass qua cut vớiC08F63. Không chọn “đoạn cuối đẹp” để giả toàn nhiệm vụ/range conforming. Không dựng/crop/speedup/EDL trong review này.
- Candidate có thể khảo sát **native `[0,96)`** cho rough review toàn hành vi, kèm nhãn exception pending; chưa selected/approved range. Nếu cần ngắn hơn phải audit timing/join/gaze trên bản encode mới. Việc lấy `[0,84)` sẽ tới nét gặp mắt nhưng vẫn mang toàn sai lệch, không đóng lỗi.
- ThroughC08candidate=816F/34s. Thêm full96F→912F/38s, vượtrough35=72F/3s; `[0,84)` cũng37,5s/vượt60F. Không đủ24F còn lại để giữ entry→pickup→ending thực. Cần audit earlier margins bằng nguồn/range/lời thực; không tự đổi cut đã duyệt, bỏB hoặc chốtfinal30.
- Native có AAC dù UI no-audioTRUE; presence không cho biết voiced/noisy/silent. Chưa measure/listen C09, không ASR-as-listening, không AV/lipsync PASS. Silent derivative nếu làm phải giữnative/provenance và không làm mất visible hand-role violation.
- C08native cũng có unrequestedlowering ở tail, đã loại khỏi candidate; C09 lần này sai trướcB nên không cùng khả năng trim. Không tự suy thành quyền paid retry. Retake0/reserve110CLOSED; nếu root phân loại là cùngMAJOR hai output theo238 thì STOP_FOR_DIAGNOSIS bắt buộc, không chạy thử tiếp. Report không tạo ledger debit mới, chuyểnbucket hoặc mở reserve.

**Disposition:** giữ native và evidence; C09 có giá trị **ROUGH CANDIDATE ONLY WITH EXPLICIT UNAPPROVED PROP/HAND EXCEPTION**, chưa conforming/ownerapproved/source-selected/AVpass. Root có thể tích hợp findings vào phương án rough cụ thể để review, nhưng không tự miễn sai lệch hoặc gọi các gate fullrough/final đã đóng. Phần khuất/continuous clearance, nghe/AV, timing và food seamC05→C06 cònOPEN.

## Bổ sung superseding scope REC312 — ngoại lệ owner cho dựng thử

- Đã đọc đủ `00_decisions/C09-hand-role-exception-for-rough-312.json`. Owner trả lời nguyên văn: “A — Chấp nhận động tác mới, tiếp tục dựng thử (khuyến nghị)”. Target native311 SHA `d06160b0efbb2ee5e7188d4748ffe3ae915abb0036b31ec12ae52788affd72e3` khớp nguồn reviewer đã tự kiểm; decision ghi review-video SHA `68589b58fcc342fc1d72c111828c9bf430d4713a2ba9ee78ed60f57bc09f5958`, reviewer chưa tự xem/hash review derivative ấy trong bước bổ sung này.
- **DAO_GLASS_SET_DOWN_OUTER_HAND_JOINS_BOWL_SUPPORT_ALLOWED_FOR_ROUGH_TRIAL:** owner cho phép Đào đặt cốc xuống bàn và tay ngoài chuyển sang cùng tay trong đỡ bát, chỉ để một local rough trial. Trạng thái “ngoại lệ chưa duyệt” trong kết luận cũ ở trên **được supersede đúng phạm vi hành vi này**; findings F13–40/exit vẫn đúng, original FINAL311 vẫn không conforming. Không sửa lịch sử thành đã đạt brief.
- A ở bát Đào/B mới từ đĩa vẫn bắt buộc; không miễn clone/contact/continuity/AV. Decision ghi rõ C09_range_approved=false, whole_episode_approved=false, new_generation_authorized=false, credit_spent=0, release=false và giữ owner fullrough/final checkpoints.
- **Current disposition: C09_ROUGH_TRIAL_ALLOWED_WITH_OWNER_SCOPED_PROP_HAND_EXCEPTION312 / NOT_ORIGINAL_BRIEF_PASS.** Có thể đưa take311 vào đúng một rough candidate local theo312 mà không mở lại microapproval; source-range/join/timing/encode/miệng/lời/giọng và bản toàn phim vẫn phải QC actual trước trình nghiệm thu.
- Root dự kiến trial840F/35s, C02`[16,173)`, C04`[12,124)`, C09`[8,88)`, giữ exactblock308120F/C0864F/lời/voice/speed. Đây là **proposed trial ranges**, chưa reviewer kiểm encoded rough/range acceptance. Khi có file/hash phải đối soát nguồn→frameboundaries→duration, đoạn gắpA trướcC04exit, pickupB và gaze trongC09range, C08→C09entry, approvedblock308, audio ends/cuts và continuity toàn chuỗi. Không lấy đủ840F hoặc ledger làm qualityPASS.
- Reviewer chỉ cập nhật report; chưa tạo/chỉnh media/EDL/browser/paid/Git. Chờ exact encoded rough path/hash để kiểm file thực. Continuous AV/listening/clearance khuất và food seamC05→C06 cònOPEN.
