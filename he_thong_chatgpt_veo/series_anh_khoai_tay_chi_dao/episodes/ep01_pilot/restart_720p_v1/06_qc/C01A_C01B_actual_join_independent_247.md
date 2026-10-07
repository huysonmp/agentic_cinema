# C01A → C01B T01 — kiểm đoạn nối actual độc lập REC247

Ngày 07/10/2026. Reviewer độc lập, không maker/producer. **JOIN_REWORK / SOURCE_C01B_HOLD**: đoạn nối actual xác nhận đứt liên tục động tác tay ở A→B; không phải chỉ khác vài chi tiết hình giữa hai shot. Chưa chọn C01B T01 cho bản phim. Báo cáo không cấp quyền retake, không release và không chứng nhận AV.

## Target và phạm vi bằng chứng

SHA256 tính lại bằng PowerShell trên cả ba media:

- Join `07_edits/C01A_C01B_T01_FLOW_JOIN_QC_247.mp4`: `4f92cfd00ddf51b30dd99ec1d779fc703d22ea4fec0a51fd83ec8f0f4322a58d`.
- Selected A `07_edits/C01A_T04_FLOW_0_3p333S_FOR_APPROVAL.mp4`: `e22c113204c404e928683c69465237921f601f2b33a3eb9a9187eb0648f4b803`.
- Native B `05_native/EP01_720_C01B_T01_NATIVE.mp4`: `f7321e72c952cf849f9b5febede7fb08951c997970de82e6f8d424f54415089b`.

Đọc đầy đủ `C01B_T01_native_independent_246.md`, DOP/ACT diagnosis246, C01A exact-prefix selection246, owner confirmation247 và join `native_evidence.json`. Đọc T02 draft247 chỉ để nêu đích sửa tối thiểu; **không phải preflight T02**.

Trực tiếp xem join: overview1fps; cả ba boards6fps (zero-index **0,4,…172**); full frames **65–105 liên tiếp** và **176**. Tổng **76 unique join frames**, không toàn bộ177 frame/continuous playback. Xem lại actual A frame80 (`C01A_T04_FLOW_246/all_native_frames/00081.png`), native B0 và B16 (`C01B_T01_NATIVE_246/all_native_frames/00001.png`, `00017.png`), không chỉ dựa trên ảnh reference. Join full images1280×2274 được công cụ hiển thị1153×2048; không đo pixel hoặc lực/chạm3D từ chúng.

Technical extraction của root: join **1280×2274**,177frames,VFR average `2718720/113357`,video7,380013s/audio7,36s,decode good. Reviewer tính hash nhưng không probe/decode lại. Native A/B là720×1280/24fps. Join này **không phải native720p/CFR24 deliverable**. Mốc dùng PTS có sẵn, không lấy index/averageFPS. File PNG=index+1.

## Findings và mức độ

| Finding | Actual index / PTS và quan sát | Severity / lớp cần sửa |
| --- | --- | --- |
| **J-START-HAND** | A cuối: join80 / **3,333333s** là trạng thái tay trong gần bát riêng, tay ngoài tại vành phải. Ngay B đầu: join81 / **3,380013s**, tay trong đã vươn chéo trái-xuống tới gần vành trái; tay ngoài mở cong/rời cách ôm vành nguồn. Mismatch tương tự có ngay ở actual nativeB0 so actualA80. | **MAJOR causal continuity**. Không đòi pixel-identical toàn cảnh; vấn đề là vị trí và chức năng hai tay đổi tại một cut tiếp nối cùng hành động/camera. Ngoại lệ owner cho chạm vành + inner gesture ở A không cho phép tự đổi thành một lượt tiến hai tay mới ở B. Sửa staging/take B, không đổi cut để giấu. |
| **J-RENEWED-REACH** | Dense81–105 / **3,380013–4,380013s**: từ bàn tay mở gần đĩa, cả hai tay lại tới hai phía vành; Khoai có mouth event rõ ở các mẫu85–101. Boards108–116 /4,505013–4,838346s vẫn có tay ở vùng vành. Không phải chỉ một ảnh B0 khác A rồi lập tức thả/thu. | **MAJOR continuation/action**. Hướng mong đợi: giữ contact đang có → nghe → thả → thu; quan sát lại cho một đoạn tiếp tục tiến/đặt hai tay tại đĩa rồi mới rút. Mouth event không chứng minh cue âm chính xác, nhưng không xóa được lỗi hình. |
| **J-FOOD-POP** |80→81: contour phía trên khối nem và cách xếp các miếng thay đổi; outline đĩa/đầu nhân vật cũng drift. So actualA80/nativeB0 có cùng kiểu thay đổi. Qua đầu B có biến hình nhẹ của outline/pile. | **Continuity defect**, góp phần làm cut lộ; không suy thành lấy món, đổi khối lượng hoặc kéo đĩa vật lý. Đích sửa giữ silhouette/arrangement đĩa và món, không chỉ giữ tên Nem Bùi/no-steam. |
| J-LATE-RELEASE |Boards124–136 /5,171680–5,671680s thấy rời vành/thu;148–152 /6,171680–6,338346s gần trạng thái nghỉ;176 /7,338346s hai tay quanh bát, hai mặt rõ, Đào nhìn Khoai. | Release/rest có trong mẫu; không cứu opening mismatch. Không thấy gross kéo/nhấc đĩa/lấy/ăn kiểu tailA-T04 trong phạm vi đã xem. Không chứng minh stationary3D hoặc fluidity mọi frame. |
| J-COVERAGE/SET |Hai mặt vẫn nhìn rõ; Đào môi khép trong mẫu B được xem. Bát, rau trước-trái, hai đồ chấm, đũa nghỉ, cốc ngoài phải và phố mở còn. Không thấy chữ mới/steam trong76samples. | Quan sát thuận lợi có giới hạn. Không dùng no-steam/face coverage để PASS tay hoặc toàn join. Không chứng nhận only speaker/lip-sync bằng still. |
| J-FORMAT |Join export tăng raster lên1280×2274 và VFR, PTS81 không đúng81/24. Gap80→81≈0,046680s. | Cần root xử lý export-format gate trước delivery. Re-encode/timestamp khác nhỏ không giải thích việc tay/food đổi pose, và không phải lý do tạo lại native. |

## Nguồn lỗi, khả năng offset và ranh giới quyết định

**Nguồn quan sát được:** mismatch đã có ở nativeB0; join giữ đúng kiểu A-end/B-start đó. Không có bằng chứng assembler dùng nhầm A-tail kéo đĩa, đảo thứ tự hoặc tự tạo một tay mới. Flow assembly/re-encode làm raster/PTS khác; **không phải nguồn chính của lỗi động tác này**. Đây là phân loại lớp lỗi bằng đối soát media, không kết luận cơ chế nội bộ model hay nguyên nhân upload/prompt đã được chứng minh.

Không tìm được **honest B offset** đáp ứng cả giữ nguyên từ “Khoan” thực, giữ nguyên nhân→phản ứng và khép đúng động tác A. Vùng B đầu đến quanh mouth event vẫn chứa tiến hai tay; bỏ vài frame đầu không trả tay trong về pose A. Chọn sau khoảngB1s bỏ vùng lời ngắn theo ASR đã có; chọn vùng thu/rest sauB2s bỏ interruption/cause. Reviewer không nghe nên không chứng nhận phonetic onset hoặc mọi offset có thể có; kết luận là **chưa có range hợp lệ có bằng chứng để chọn**, không được tự khóa EDL. Không dùng overlay âm, crop, speed, cover món, freeze/dissolve để hợp thức.

Owner confirmation247 chốt **exact nativeB audio f732…** và một lần quyền reimportA, rõ ràng không picture/join/future voice. Audio gate này đã đóng bằng human evidence, reviewer không nghe; approval không tự chuyển thành join AV/lip-sync PASS. C01A source selection246 vẫn chỉ81-frame cut dưới ngoại lệ đã chốt, không whole-native/whole-film approval. Giữ source HOLD của root là phù hợp mức MAJOR quan sát ở actual cut; không cần tự thêm một approval mỗi clip.

Join là export lại **cùng T01**, không output generation thứ hai. Không đếm việc xem native rồi xem join thành hai lần SAME MAJOR để bắt buộc STOP. Một take mới nếu lặp đúng start/renewed-reach MAJOR phải xử lý quy tắc STOP theo authority238; báo cáo này không tự cho phép chạy take đó.

## Đích khắc phục tối thiểu / bước tiếp

1. Giữ exact A-end nguồn, canon, shot, K20 và lời một “Khoan”; chỉ sửa B: **không new approach**. Tay ngoài giữ contact nguồn rồi nới/rời vành; tay trong chỉ khép gesture **về phía thân/bát riêng**, không đến vành trái. Sau interruption mới release/retract; đĩa/món không đi theo tay.
2. T02 draft247 đã diễn đạt các đích này và preservation food rõ hơn; đó mới là đề xuất paper, không bằng chứng image-conditioning khóa được first frame hoặc motion. Root cần preflight riêng + live source/voice/readback/config/quote trước quyết định paid output trong quyền hiện có.
3. Take sửa phải kiểm **actual A→B boundary và wholeword→release→rest**, rồi B→C02 và nhịp rough. Không chỉ kiểm B tách lẻ hoặc lấy đúng chip/hash làm start-geometry PASS. Export format cần kiểm riêng.

**Đã xác định:**76samples/actual boundary, lỗi nguồnB về tay và food continuity; late release/rest quan sát được. **Quyết định review:**JOIN_REWORK/SOURCE_C01B_HOLD, không selected/release. **Giả thuyết:**staging câu tiếp tục ý định lấy món có thể kích hoạt lượt reach mới; chưa causal proof. **Còn mở:**continuous AV/phonetics/fluidity, take sửa, B→C02 và delivery format. **Bước tiếp:**root tích hợp chẩn đoán/preflight đích sửa; không auto-retry từ báo cáo này.
