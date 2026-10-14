# EDIT follow-up — C09 actual311 và candidate rough35

**CURRENT DISPOSITION REC312: OWNER_HAND_ROLE_EXCEPTION_ACCEPTED_FOR_ONE_ROUGH_TRIAL. HOLD ở snapshot311 đã được giải quyết riêng cho động tác đặt cốc/đỡ bát bằng hai tay, theo đúng source/hash. Range C09, actual AV, whole rough và final vẫn chưa duyệt. Xem bổ sung312 cuối report; không dùng số học35s làm media PASS.**

Ngày 14-10-2026. `/root/timing_audit_309`. Bounded read/view/hash/ffprobe, chỉ viết report này. **Candidate số học35s có cơ sở để dựng thử; chưa được chọn và chưa chứng minh nhịp AV/đọc kết đạt.** Không sửa media/EDL/Git, không browser/paid/voicechanges, không nghe hoặc xem AV liên tục. Không tự tăng/giảm range để gọi fit.

## Snapshot và actual evidence

Kế thừa inventory/report 309: through C08 conditional 816F/34s; selected encodedblock 308 120F; C08 64F silent còn conditional. Đọc C09 run311/native_evidence/preflight310, parent cập nhật actual 96F. Fresh SHA256 native C09 `d06160b0efbb2ee5e7188d4748ffe3ae915abb0036b31ec12ae52788affd72e3`; ffprobe-count96F,24fps,720×1280,4s. `run311` vẫn ghi WAITING_OUTPUT/actualfalse ở thời điểm đọc là snapshot trước cập nhật, không dùng đó phủ định bytes/probe/frames actual vừa kiểm hoặc gọi owner đã chọn.

Tự xem:

- C04 T02 boards `262_C04/action_all_frames/action_all_15.jpg`–`18.jpg`, đủ F112–143;16/18 đã xem ở audit309,15/17 bổ sung trong follow-up. Full nativeF123/F12/F143 từ `262_C04/native_qc/all_native_frames/00124.png`, `00013.png`, `00144.png`.
- C03B selected exit F49: `259_C03B/native_qc/all_native_frames/00050.png`; C05 T02 entry F0: `265_C05/C05_T02_QC_267/all_native_frames/00001.png`.
- C09 `06_qc/C09_PICK_B_native_311/full16_01.png`,02,04,05,06 = F0–31/F48–95; full F8/F87 (`all_native_frames/00009.png`,00088). Không tự coi đã kiểm F32–47 hoặc full96F từ parent statement. Full C08 encoded exit F63 `C08_PREFIX_SILENT_encoded_309/all_native_frames/00064.png` so C09 F8.

## C04 candidate[12,124) và hai điểm nối

| Target | Quan sát bằng still | Kết luận / gate |
| --- | --- | --- |
| C03B F49→C04 F12 |Hai người mutual gaze/cười nhẹ, môi khép/tay riêng nghỉ, cốc còn bàn phía Đào, hai bát rỗng, đũa Khoai còn trên bàn. Scale/axis/props gần nhau, có sai biệt nhỏ diễn/tái dựng |Không thấy MAJOR reset mới trên cặp full stills. GO để thử encoded seam; không natural rhythm/AV PASS. Lead 12F giữ ít nhất phần idle tới vùngF23 đã xem, không bỏ cue Đào lấy cốc trước pickup |
| C04 F112–123 |A đã kẹp trước Khoai; Đào từ chú ý cốc/môi sang nhìnKhoai khoảng F113–114, sau đó cốc nâng/tay trong nghỉ/bát Đào rỗng. F123 nhìn Khoai, Khoai nhìn A; chưa trao/thả/ăn |End 124 giữ caught gaze trước cut, không bỏ pickup. Khoảng từF114 tớiF123 chỉ10F/~0.417s cho gaze trở lại. Không chứng minh khựng/đọc được ở tốc độ thật |
| C04 F123→C05T02 F0 |CùngA còn kẹp phía Khoai, cốc nângtay ngoài, hai bát/tay tronggiữ. Khoai đổi gaze xuống A → Đào ngay qua cut. Món/tips/pose có sai biệt tái dựng nhẹ |Gaze jump này cũng có F143→C05F0 đã nêu/duyệt269, nhưng approval269 dành exact cut cũ. So fullF123 vớiF143 không thấy pose/props đổi lớn khiến endpoint 123 vô dụng. **Không tự chuyển acceptance 269 sang F123.** Đo/chụp exact encoded seam mới và AV checkpoint vẫn bắt buộc |
| C04 F124–143 bị bỏ |Still giữ caught/A/cốc gần trạng thái F123, có biến đổi nhỏ/chớp mắt |20F/~0.833s là candidate hold trim, không phải safe saving. Shortened hold có thể làm caught beat quá nhanh trước N05, hoặc thay cảm giác ý định→bịthấy |

Candidate C04[12,124) có112F/4.666667s, giảm32F/1.333333s từ144F. Bỏlead12 vàtail20 là hai lựa chọn biên tập khác nhau; endpoint đổi 123 thay 143 ảnh hưởng seam C05. Không chọn chỉ vì nó cung cấp đúng số32.

## C09 candidate[8,88)

NativeC09 actual 96F, chưa source/range AV acceptance. Candidate 80F/3.333333s bỏ F0–7 vàF88–95.

- EntryF8: tips rỗng, A trong bát Đào đang cầm, cốc tay ngoài còn nâng, bát Khoai ở bàn; hai mặt môi khép. So C08 encoded F63, bát Đào hơi hạ/mặt nhìn thay nhẹ nhưng không thấy pickupB xảyra trước cut hoặc A biến mất/đổi đích. C09 lead 0–8 còn gần state đầu nên không thấy MAJOR state jump từ việc bỏ 8F; actual encoded C08 → C09 seam cần kiểm. Việc root lấy C08 F63 làm input không bảo đảm F8 pixel match.
- Khoai đưa đũa rỗng về đĩa, nativeF57–65 vùng pickup rồiB nâng; đã xem F48–79 đầy đủ qua boards 04/05. Candidate range giữ vùng này. Không cắt B, không dùng B thay A, không đảo causality. Mặt/hai bát vẫn đọc; clearance quanh rim/tay không được chứng nhận 3D từ still.
- Ending: Khoai blink F74–76, Đào blink F75–79; **mutual gaze với hai mắt mở rõ F80–87** trong candidate =8F/0.333333s. F79 Đào còn blink, không cộng nó thành8+1 frame đã mở. B trên đũa về Khoai, A vẫn trongbát Đào; full F87 hợp endpoint về state.
- F88–95 bịbỏ vẫn cùng nét cười/mutual gaze; đó là 0.333333s thêm để khán giả đọc kết. Candidate[8,88) giữ hành động nhưng **có rủi ro ending quá hụt**, không tự gọi8 frame cười là đủ R09. Actual playback/ownerrough cần xác nhận cảm giác hai người cùnghiểu. Nếu cần giữ đủ tail F95 thì C09[8,96)=88F, rough candidate bên dưới thành35.333333s và không fit; báo đúng, không tự cắt thêm C02/C04 để bù.

## Số học candidate — không acceptance

| Thành phần | Count hiện hành | Candidate | Saving giả định |
| --- | --- | --- | --- |
| C02 export |181F [0,181)|157F [16,173)|24F; speech/biên AV vẫn pending nhưreport 309 |
| C04 native |144F [0,144)|112F [12,124)|32F; caught/seam mới pending |
| C09 native mới |96F [0,96)|80F [8,88)|16F; ending-readability pending |
| Tổng hiện hành gồmfullC09 |912F/38s|840F/35s|72F/3s tổng;24+32 trướcC09=56F |

Đối soát theo yêu cầu: 816+80−(24+32)=840F/35s. Điểm C02 end 173 cùng lead 16 giữ đúng giả địnhreport 309, không phải thuật ngữ approved range. C06+C07block 308 120F/C08 64F và mọi lời/voice/speed giữ nguyên trong scenario. Mục tiêu 30 còn thiếu 120F/5s trên candidate 35 này; không có bằng chứng để reclaim thêm 120F an toàn.

**GO_FOR_ONE_LOCAL_TRIAL_AND_BOUNDED_ENCODED_REVIEW, NOT_SELECTED_OR_AV_PASS.** Về stills không thấy MAJOR entry/state blocker mới làm3 range đề nghị vô dụng; perceivedcaught pause và chỉ8F ending là hai risk thực phải kiểm; paperwork chưa đủ để đóng. Chưa có actual encoded candidate 35 hoặc audio đã nghe. Savings đã safe/accepted trong audit=0.

Bước tiếp scoped ở snapshot đầu: dựng đúng candidate 840F với EDL trial/hash, không ghi đè source/EDL approved; kiểm new seams BR→C02/C02→C03A/C03B→C04/C04→C05/C08→C09 và ending F80–87 ở export. Source C05 → C06 food seam vẫn riêng OPEN. Exact candidate toàn rough cần nghe/xem continuous AV để chốt âm đầu/cuối N02, không giọng lạ/nhạc, caught/rhythm/ending. Nếu ending cần tail dài hơn thì ghi actual duration vượt 35 và trình phân bố lại; không bỏ B/tăng speed/voice remake hoặc retro approve final 35. **Bước dựng này bị thay bằng HOLD trong bổ sung sau; không thực hiện trước disposition của owner về lỗi tay/cốc.**

## Bổ sung actual — tay ngoài đổi vai và cốc đã đặt xuống, không trim-away

Sau khi root đọc report, root gửi finding từ reviewer actual và full F40/F56: Đào đặt cốc lên bàn, tay ngoài rời cốc và chuyển sang đỡ phía phải bát. Đây là thay đổi hành động/vai tay, không chỉ hạ độ cao bát/cốc. Reviewer timing đã bổ sung đọc **toàn FINAL311** và tự xem full native F40/F56 (`all_native_frames/00041.png`, `00057.png`). Xác nhận hai tay Đào đang đỡ bát, cốc nằm trên bàn phía sau bát/tay; tay ngoài không giữ cốc như entry. Finding này đã có trong các boards/full F87 đã xem trước nhưng audit timing đầu chưa đối chiếu nó với contract FINAL — phạm vi GO ban đầu vì vậy không đủ làm source suitability verdict.

FINAL311 yêu cầu A ở bát do tay trong đỡ, tay ngoài tiếp tục giữ cốc nâng ngoài bát; cụ thể: **“Do not put Dao's bowl or glass down or invent a spare bowl.”** Props có đủ số lượng không đóng được lỗi hand-role/staging này. Candidate [8,88) vẫn chứa thao tác đặt cốc/đổi tay và trạng thái sai trước pickup B khoảng F57–65; cắt head/tail không loại được vi phạm mà vẫn giữ nguyên pickup/kết R09. Không bỏ F40–56, che tay hoặc tua qua để gọi đúng contract.

**C09 SOURCE NOT_SELECTED; owner hand-role/staging exception NOT_GRANTED. Timing35 chỉ khả thi theo số học và một số biên still; chưa có contract PASS, chưa phải chỉ còn AV checkpoint.** Kết luận `GO_FOR_ONE_LOCAL_TRIAL_AND_BOUNDED_ENCODED_REVIEW` phía trên được giới hạn/supersede ở bước thực thi: root giữ HOLD, **không dựng rough35 lúc này**. Cần trình đúng native/silent source và thay đổi cụ thể để owner quyết định ngoại lệ có chấp nhận được không; không mặc định owner đã đồng ý hoặc xin lại từng thao tác kỹ thuật. Không có retry mới hoặc quyền đổi voice từ report.

Run311 hiện đã ghi debit thực7, project spent279/500, remain221; reserve110 đóng. Snapshot WAITING_OUTPUT/actualfalse ghi ở đầu report là lịch sử lúc đầu đọc, không trạng thái current sau bổ sung này. Current source disposition và quyền chi không được thay bằng phép tính840F.

## Bổ sung REC312 — ngoại lệ đã được owner chấp nhận, mở đúng một rough trial

Reviewer đã đọc toàn `00_decisions/C09-hand-role-exception-for-rough-312.json`. Owner trả lời nguyên văn: **“A — Chấp nhận động tác mới, tiếp tục dựng thử (khuyến nghị)”**. Target đúng native311 SHA `d06160b0efbb2ee5e7188d4748ffe3ae915abb0036b31ec12ae52788affd72e3`, silent review SHA `68589b58fcc342fc1d72c111828c9bf430d4713a2ba9ee78ed60f57bc09f5958`. Ngoại lệ cho phép Đào đặt cốc xuống bàn và tay ngoài cùng tay trong đỡ bát riêng trong **rough trial**. A phải tiếp tục ở bát Đào; B vẫn là phần mới từ đĩa về Khoai.

HOLD311 vì thiếu quyền ngoại lệ này được supersede **theo scope trên**, không hồi tố source thành đúng FINAL311. Decision312 ghi rõ `C09_conforming_to_original_prompt=false`, `C09_range_approved=false`, `whole_episode_approved=false`, `new_generation_authorized=false`, `release_authorized=false` và giữ owner full rough/final checkpoints. Không chi mới; không retry/sinh voice hoặc media mới từ ngoại lệ.

Root được mở **một local rough35 candidate** với trial ranges công khai: C02[16,173), C04[12,124), C09[8,88), giữ exact selected encoded block308120F/C08candidate64F, lời/voices/tốc độ. Tổng kỳ vọng840F/35s vẫn chỉ là phép tính; các biên mới/âm đầu-cuốiN02/caught beat/ending8F và C05→C06 food seam phải kiểm trên exact encoded file/QC. Reviewer chưa nhận hoặc kiểm encoded rough mới tại thời điểm bổ sung312; không ghi report actual PASS từ việc root chuẩn bị dựng. Sau khi có file/hash/QC mới sẽ bounded timing/transition review, giữ gate nghe/xem continuous AV và owner rough/final acceptance.
