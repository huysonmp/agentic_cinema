# REC264 — C05 T01 independent actual QC

Kết luận: HOLD / NOT_SELECTED vì MAJOR continuity ly/bát Đào; C06 HOLD cho tới disposition nguồn/điểm nối. Không final/voice/sync PASS, không quyền retry.

## Target, bằng chứng và khả năng

- Full-read run264, rough35 decision264, final prompt263 và acceptance263; không đọc maker report. Rehash native `05_native/EP01_720_C05_T01_NATIVE.mp4` khớp `82478230b9a4c298f3a28f4432474822e406586693c0a49381278cd3d7d1f648`.
- Tự xem toàn bộ 12 board `action_all_01..12.jpg`: đủ96 frame F0..95, full/both-face/table; thêm PNG native F0,28,29,61,62,63,64,67,68,95 và actual START C04 F143. F zero-based, t=F/24. Đã đọc đầy đủ native_evidence.
- H264720×1280/24fps/96 frame/4s; AAC stereo48k/4.010s, decode đủ/source unchanged theo evidence. Đây là stills/metadata, không playback continuous AV; tôi không nghe, không chứng nhận đúng D06/lời/sync/single female audio bằng preset hoặc ASR.
- Nguồn vào F143 SHA `2e4f4a5fbf0d5f310010762d26d0c74f08bfb2da3eab792f69a3be568b94c2db`, C04 SHA `8ad98f21c0c904b01055d6f579900cd60c107a152a9166a8cfa563165a47a209`; final prompt `16a76e4826fb8d1cdc23b4acf245d04b7c0d3a0cb60c3ad47c76fd933281b679` đúng run. Ingredients không khóa pixel, nhưng lệch actual vẫn phải QC.

## Phát hiện từng trạng thái

- MAJOR F0/0s → toàn F95: START có ly nâng ngang ngực dưới mặt Đào; native F0 đã ở độ cao mặt bàn, đáy sát bàn và tay ngoài đổi xuống theo. Trong96 stills không có động tác hạ ly nối từ trạng thái accepted; đây là reset tại entry, không chuyển động được chứng minh qua cut.
- MAJOR F0..95: bát cá nhân Đào nhìn rõ ở START nay không hiện trong vùng trước cô; chỉ bát Khoai còn rõ. Full F0/28/61/68/95 không cung cấp bằng chứng bát Đào vẫn nguyên nhưng bị ly che. Không chứng nhận “hai bát rỗng” hoặc bịa đường bát ra ngoài khung; tối thiểu bát bắt buộc phải đọc được đã mất khỏi hình, ảnh hưởng C07 nhận bát/C08 thả A.
- A vẫn biểu kiến kẹp ở tips đôi Khoai trong tay ngoài SCREEN-LEFT, phía mình dưới ngực xa môi trong cả96 frame; chuyển tay nhỏ đầu shot rồi giữ, không thấy gắp lần hai/ăn/offer/transfer/drop/A biến mất. Shape có nếp gập, không dùng stills chứng minh identity từng pixel hay khẳng định nhiều miếng khi chưa đủ bằng chứng. Không thấy đôi Khoai trùng nghỉ trên bàn; đôi Đào còn nghỉ.
- Hai tay trong nghỉ; không thấy bowl-lift hoặc reach món. Đĩa/chấm/rau front-left ổn định, nem không steam/smoke, không caption/text mới; native watermark còn. Camera/axis giữ Khoai LEFT–Đào RIGHT và cố định trong native; không có cut nội bộ thấy được, không gọi seam với nguồn là exact-lock.
- Đào vào đã nhìn Khoai, không quay về ly rồi quay lại/diễn discovery lần hai. Khoai từ mắt thấp về A chuyển sang cô khoảng F9..17 (0.375..0.708s), blink F12..14, nét ngượng kín/tay khựng nhẹ hỗ trợ caught-response; không broad laugh/scolding rõ. Confirming glance xuống A không nổi bật, không coi là lỗi major thêm.
- Mouth attribution: Khoai môi giữ cùng nhau ở96 stills, không thấy speech-shaped opening. Đào bắt đầu hé khoảng F29/1.208s, rõ open/speech-shapes F30..62 (1.25..2.583s), có closure nội bộ F38..39; F63/2.625s khép lại và F63..95 giữ closed-lip smile. Không suy ra word boundaries/số câu nghe được từ các shape này.
- F63..67 blink/khép mắt sau khẩu hình; F68..88 (2.833..3.667s) hai mắt đọc được, Đào closed-lip smile, Khoai nhìn cô/giữ A; F89..95 Khoai blink/mắt về thấp. Không thấy sip mới hoặc mở miệng người nghe ở tail.

## Range, owner checkpoint và gate tiếp

- Không có range cắt nào tự khôi phục bát Đào hoặc ly lifted-entry: sai lệch nằm ngay F0 và còn toàn clip. Cắt đầu/đuôi chỉ đổi nhịp, không repair continuity; không crop/insert/freeze để che mất bát hoặc gọi giữ A là toàn boundary PASS.
- Nếu nguồn/exception được xử lý riêng, endpoint F68..75 là vùng hình có closure + eyes readable + A vẫn giữ, đáng kiểm làm candidate ngắn. Chưa chọn range/khẳng định trọn N05 vì chưa nghe; không cắt theo ASR1.1–2.44s mà thiếu âm cuối/response. Full4s cũng chưa selected.
- Owner cần nghe đúng “Chờ em quay lưng nữa à?” một lần, D06 trưởng thành Bắc, không male/extra words, nhẹ “nữa à”, trọn âm cuối và sync; xem caught-response tự nhiên. Kèm actual encoded C04→C05 seam để quyết định riêng ly thấp/bát không hiện, không lấy exception C04 gần môi làm blanket exception C05.
- Trước C06: cần quyết định nguồn repair/new take hoặc owner chấp thuận một boundary/prop disposition cụ thể với downstream plan khôi phục/đưa bát có causal rõ; lời chấp nhận clip/voice riêng không tự sửa vật thể. Không tự dựng bát xuất hiện lại C07, không tự paid retry; native/prompt giữ nguyên.
- Owner264 chỉ mở rough cap35s, vẫn giữ lời/nhịp và prefer30 nếu trim an toàn; không final35s PASS. Nếu dùng đủ C05 4s, tổng range hiện27.583333s, còn7.416667s tới35 cho C06–09; future source timing chưa đo, không lời hứa đủ. C05 range chưa chọn nên đây chỉ là phép tính điều kiện.
- Run ghi một submit7 credit934→927, project156/500 còn344, reserve110 CLOSED. Trạng thái run “output pending” là snapshot giấy; native thật đã tồn tại và được review đây, không lý do submit lại. Không thực hiện spending hay approval mới trong lượt kiểm này.

## T02 — paper preflight riêng, không sửa actual verdict T01

- Đã FULLREAD draft/preparation T02 và rehash draft `e3e5f9cda64362eab52a9f6f644f9952119934b859611a2d138f0ff9ba5ab69a`; T02 NOT_SUBMITTED, live quote null. Không đọc maker report; đánh giá độc lập trên source/actual T01/draft.
- Hai sửa có căn cứ: giữ ly/holding-hand raised trên bàn xuyên shot; neo riêng bát ceramic Đào với rim/interior readable, không để glass thay bowl. Không đổi canon/N05/D06/model/route; SAME A/đôi đũa/bát Khoai/mặt cả hai/cold-food tiếp tục là hồi quy bắt buộc. Đây là kiểm chứng sửa có mục tiêu, không proven fix hoặc backend pixel-lock.
- “No sip”, returned gaze/no repeat discovery và Khoai closed lips phù hợp accepted START; Đào chỉ nói N05 rồi khép. Nên khóa rõ một câu ở final: hai môi khép tại START, chỉ Đào mở cho N05 (không cấm môi Đào trong thoại). Draft hiện không nêu riêng môi Đào khép trước câu; đây là clarification để tránh mouth lead-in, không bằng chứng output lỗi mới.
- Neo độ cao bằng actual reference; “rim just below her chin” không nên làm model tự dịch rim theo giải phẫu thay vì giữ đúng pose ảnh, trong ảnh rim dưới mouth/ở vùng chin-neck. Ưu tiên “at the inherited height/position in reference, below her mouth, raised above her visible bowl”; không nâng/hạ thêm để hợp từ shoulder/chin.
- GO_T02_TARGETED_INPUT_PREPARATION_AND_FINAL_VERSION_GATE_ONLY: đóng clarification hiện hành, maker/current independent/root full-read, live lại exact image+D06-only/audioON/config/quote≤15/x1/AgentOFF trước bất kỳ submit. Không dùng draft paper làm paid GO. Actual T01 vẫn HOLD, C06 HOLD; nếu ly/bát major lặp ở actual T02 thì STOP diagnosis, không T03 tự động. Không cert voice/motion/sync/35s feasibility từ wording.

## Amendment — current final T02 paper check

- Đã FULLREAD riêng final `04_requests/C05_T02_prompt_264.txt`; rehash khớp `33d87040e8fe90ddb69fca46f2942e62f56d685c40248ac6f78173e55056c3c3`. Draft `e3e5...` giữ lịch sử, không target current-final.
- Hai clarification đã giải quyết: exact inherited height/position thay forced shoulder/chin; cấm raise/lower/reposition nên không cho lateral relocation để né bát. Ly phải giữ phía tay ngoài, không thế chỗ hoặc che empty interior; bát riêng vẫn readable tại vị trí source. Không thấy mâu thuẫn giấy mới giữa hai neo này và ảnh accepted F143.
- Both closed lips tại entry, chỉ Đào mở cho single N05 rồi khép; Khoai closed xuyên shot, returned gaze/confirming glance không discovery lại. N05/D06/SAME A/own pair/empty bowls/cold food/no sip–transfer–drop–eat giữ nguyên; tiny arrested hand movement chỉ khựng trong pose, không hành động lift mới.
- GO_CURRENT_FINAL_PAPER_TO_INPUT_AND_LATER_LIVE_GATE_ONLY; clarification draft đã đóng. Không submit/live proof/credit hoặc media PASS trong lượt này; root phải full-read amendment và kiểm request/input/quote/config hiện hành trước paid action. T01 actual HOLD, C06 HOLD và same-major-repeat STOP/no automatic T03 không đổi; wording mạnh hơn không bảo đảm backend/state/motion/voice/sync.
