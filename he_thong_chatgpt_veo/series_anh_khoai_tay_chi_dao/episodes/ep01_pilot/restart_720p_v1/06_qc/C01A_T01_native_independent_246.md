# C01A T01 — Review native độc lập REC246

Run **C01A-NATIVE-CRITIC-246**, ngày 07/10/2026. **Disposition: HOLD_C01B_ENDPOINT / REWORK_VISUAL_BOUNDARY.** Chưa tìm được endpoint đã kiểm đáp ứng đồng thời trọn lời + tay còn định lấy + khoảng hở trước mọi tiếp xúc nhìn thấy. Không dùng nguyên native6s, không tự retry hoặc duyệt thay owner.

## Target, phương pháp và giới hạn

Repo native `05_native/EP01_720_C01A_T01_NATIVE.mp4`, SHA256 thực PowerShell **`0c42df876e8d3b7b46fe1b7930f3fc33ecf1e462f6c3f66ddabf677efb6c67d4`**, khớp dispatch/current request. Đọc full owner `C01A_T01_246/native_evidence.json`, unprompted `C01A_T01_246_ASR/asr.json`, audio-diagnostics log và current request246 sau visual phase. Exact prompt/F0,236/238/246, DOP/ACT/EDIT và preflight246 đã đọc đầy đủ ở run trước. Không UI/API/Git/credit/generation hoặc sửa media.

Đã xem actual owner QC ở `C:/Users/PC/Downloads/du_an_nem_bui/ep01_restart_720p_v1/06_qc/C01A_T01_246/`:

- Overview1fps:6 samples zero frames0,24,…120.
- Toàn ba boards6fps:36 samples zero frames0,4,…140.
- Full-resolution PNG: frames **64,72,80,84–101 liên tiếp,104,108,141,142,143**. Trong đó frame88 = `00089.png` /3,666667s; frame96 = `00097.png` /4s. Tổng **52 unique frame samples**; không xem đủ144 frames hoặc continuous AV. Đoạn84–101 /3,5–4,208333s được kiểm từng frame dưới dạng still, không playback.

Probe/decode root:720×1280/24fps/144frames, video6s/audio6,016s, decode thành công. Reviewer đọc evidence, không tự chạy lại probe. **Không actual listening, voice identity/speaker/lip-sync PASS.** ASR/toggle/preset không thay nghe.

## Cold actual interpretation

Đào nói bằng các poses miệng hướng về Khoai; tay ngoài screen-right nhấc lên khoảng2,667s rồi vươn về đĩa, tay trong nghỉ. Khoai chú ý bằng mắt/môi chủ yếu khép trong lượt lời sampled. Hai mặt đọc rõ, camera/nền/phục vụ tương thích source; không bị phủ bằng cảnh món.

Nhưng tay Đào hạ rất sát sau mép trên-phải đĩa. Từ fullframe80/3,333s và đặc biệt84–97/3,5–4,041667s, đầu ngón bị mép đĩa che/chồng lên mép; **không thấy air gap liên tục cần thiết**. Đây không phải bằng chứng chắc chắn lực chạm vật lý, nhưng cũng không đủ báo before-contact đạt. Tay tự rời vùng đĩa/thu trước bất kỳ “Khoan” nào: fullframe98–101/4,083333–4,208333s cho thấy rút lên về bát/thân; frame104/4,333333s đã gần thân, frame120/5s về nghỉ. Không được chỉ lấy pose giữ gần đĩa làm proof clip đáp ứng.

## Findings / correction layer

| ID | Expected → observed, time/frame | Mức / xử lý và closure |
| --- | --- | --- |
| C01A246-GAP-01 | Tay gần rim nhưng **có khoảng hở nhìn thấy**, chưa contact → frame80/3,333s, toàn84–97/3,5–4,041667s đầu ngón chồng/ẩn ở mép đĩa; khoảng hở không xác nhận được. | **MAJOR blocking acceptance/endpoint**, không kết luận chắc đã chạm/nắm đĩa. DOP/ACT/CTD xử lý tầng clearance/đường tay/pose và điều kiện trước-contact trên actual output. Closure phải thấy gap thật ở interval giữ đủ lời; không chỉ chữ “air gap” hoặc still endpoint đẹp. |
| C01A246-RETRACT-02 | Ý định còn vươn, chỉ dừng/thu sau Khoan ởC01B → fullframe98–101/4,083333–4,208333s tay đã rút lên;104/4,333s thu gần thân;120/5s nghỉ. | **MAJOR nếu giữ nguyên shot6s**: làm ngắt không còn nguyên nhân. Tail có thể loại bằng EDIT **nếu** đoạn trước đạt gap+lời; hiện GAP-01 chưa đóng nên trim riêng không cứu đủ nhiệm vụ. Không reset state C01B hoặc viết lại cause. |
| C01A246-ENDPOINT-03 | Endpoint sau đủ “em”, chưa contact và chưa retract → ASR “em”3,44–3,66s; detector -40dB silence từ3,747604s; các fullframes88–97 sau mốc này còn occluded gap, rồi98 bắt đầu rút. | **HOLD_C01B_INPUT**: không có candidate đã kiểm đủ ba điều kiện. Range trước3,333s giữ gap tốt hơn nhưng nằm trước âm cuối theo ASR; không cắt mất “em”. Range3,75–4,0s giữ speech theo offline nhưng không chứng minh no-contact. Actual hearing vẫn bắt buộc, không tự khóa timestamp/EDL từ ASR. |
| C01A246-LISTENER-TAIL-04 | Khoai môi khép/listener → board140/5,833s gần khép; full141–143/5,875–5,958333s anh nhắm mắt/cười mở môi thấy răng. | **MINOR_LOCALIZED visual instruction mismatch** ngoài đoạn thoại ASR; không chứng minh anh nói/cười thành tiếng. Có thể bỏ tail khi chọn range đạt, không tự voice reroll hoặc gọi sai speaker từ still. |
| C01A246-HAND-ID | Chỉ tay ngoài Đào vươn → đúng tay screen-right, phía ngoài bát ban đầu; tay trong và hai tay Khoai nghỉ trong samples. | SAMPLED_MET về hand identity, không toàn path collision PASS. Không thấy nhấc đũa/cốc hoặc added hand rõ; ảnh sampled không chứng minh clearance độ sâu ở bát/đũa. |
| C01A246-FACE-SET | Hai mặt/miệng rõ, cùng phố/khung/identity/warmth → giữ trong52samples; không đổi tường/quạt, không legs/fullbodywide hoặc food cutaway. | SAMPLED_MET. Mặt còn đủ dù Đào head/eyes chuyển nhẹ. Không continuous flicker/motion/sync certification. |
| C01A246-F0-FOOD | Nem nguội, hai bát trống, đũa nghỉ, serving giữ → sampled đĩa/rau/hai chấm/cốc/bát không bị kéo/gắp; không visible steam. | SAMPLED_MET về food/geography. Đĩa không dịch **không chứng minh** ngón không contact; không hợp thức GAP-01 bằng F0 món còn nguyên. |
| C01A246-VOICE | Một D06/exact N01 → input request đúng ID/name; ASR từ native nhận đủ đúng từ. | **ACTUAL_D06_PENDING**. Không certify nữ Bắc/D06/nhịp hoặc audio only-Dao. Owner/SIA nghe exactnative riêng; preview239 và C02approval246 không chuyển. |

## Đối soát request và nguyên nhân

Current request ghi một submit/Original720p, native hash đúng, fullinputquote10, mộtD06/ảnhF0, readback đúng, Omni1.1Flash/Ingredients/720p9:16/6s/x1/AgentOFF. Tôi không kiểm UI lại. Root debit10, project conservative spent40/remaining460, reserve110 chưa quyền. Thất bại boundary không có evidence buộc đổi voice, Quality hoặc công cụ.

**Observed:** lời/gesture gần nhau, tay xuống thấp ở vùng rim trước speech-end offline, rồi tự thu. **Hypotheses:** endpoint-hold chưa được model giữ; semantic “take the plate” có thể kéo pose chạm rim hoặc diễn gesture đầy đủ; 2D clearance/camera không làm khoảng hở đủ đọc. Chưa chứng minh cơ chế model hay một nguyên nhân duy nhất. Prompt đã cấm contact/retract nhưng output không đạt điều kiện nghiệm thu; không gọi prompt đúng = video đạt.

Nếu root đề xuất sửa, giữ source/canon/voice và mục tiêu một lượt; dàn pose tay **còn tách rõ khỏi rim trong hình**, hold trước-contact tới điểm ra sau trọn lời và không tự thu. Đây là đề xuất cần tích hợp/chẩn đoán, không garanti fix hoặc authority chạy. Không crop tay, phủ món, freeze, ghép tiếng lên môi khép hoặc cắt trước cuối lời để báo hoàn tất.

## Handoff năm mục

1. **Đã xác định:** native/hash thật, Đào đúng tay có reach; faces/set/F0/no-steam sampled giữ; có gap chưa xác nhận, tự retract và listener-tail open-mouth.
2. **Quyết định review:** HOLD endpointC01B / REWORK visual boundary, không retain-as-approved toàn6s. Không candidate trim-certified trong phần đã xem.
3. **Giả định:** speech-end theo ASR/silence khoảng3,66–3,75s; không human hearing/word-cut certification. Contact vật lý chưa xác quyết, visible-gap criterion đã không chứng minh được.
4. **Còn mở:** actual D06/audio/AV và phương án sửa boundary. Đây là output C01A đầu tiên; chưa cùng MAJOR haiC01A liên tiếp để tự kích STOP, nhưng không mở dependency khi blocker chưa đóng.
5. **Bước tiếp:** root đọc full report, đối soát dense interval/intent với DOP/ACT/EDIT, trình rõ HOLD/route sửa và nghe mốc D06 riêng nếu phù hợp; chưa làm C01B từ rim-occluded pose. Mọi retry theo scoped238, không auto từ report; nếu output kế lặp cùngMAJOR thì STOP chẩn đoán.
