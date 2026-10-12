# REC277 — Kiểm C07 T01: maker DIR / DOP / ACT / EDIT / CONT

Ngày 13-10-2026. RUN_ID `REC277_C07_T01_MAKER_ACTUAL`. **SOURCE_REWORK_WRONG_BOWL / ENTRY_CONTINUITY_HOLD / AUDIO_AV_HOLD / NOT_SELECTED / C08_HOLD.** Không có đoạn hoàn thành nhiệm vụ chuẩn bị bát riêng của Đào; cắt đuôi không sửa được việc chọn sai bát. Đây là maker actual, không phải phản biện độc lập. Không tự sinh lại.

## Đối tượng và phạm vi thực kiểm

- Đã đọc đầy đủ final `04_requests/C07_T01_prompt_276.txt`, preparation276, run277 và `00_decisions/C05-C06-join-owner-acceptance-277.json`. Hash final đã tự tính ở preflight: `ff869d873dbad96e81d323d770fb6f656274df691bf0136c1ae2a5f399b5353f`. Authority217, scoped238, plan236 và boundary276 đã được đọc trong chuỗi maker.
- **Tự hash bản gốc** `05_native/EP01_720_C07_T01_NATIVE.mp4`: **`d1ed08ffca20e8bbee1455f14ed672fb4e2f538374a3ba209d6cfe49a195bfc0`**. Folder owner: `C:/Users/PC/Downloads/du_an_nem_bui/277_C07_T01/`.
- Đọc đầy đủ `native_qc/native_evidence.json` và `action_all/manifest.json`. Evidence ghi 720×1280, 24 fps, 144 khung, 6 giây hình; AAC stereo 48 kHz, 6,016 giây container; giải mã toàn bộ thành công. Không tự chạy lại probe/decode. Manifest có cùng hash bản gốc.
- Trực tiếp xem **đủ144 khung F0–143 qua18 bảng ảnh**, thêm ảnh nguyên khung F0/F48/F64/F80/F95/F143 và exact START `02_refs/C07_START_from_C06_T03_selected_F56_276.png`, hash đã kiểm tại preflight `69fb0e62a3a6f138a0eae622603945b248ec8d2809c8cda513dcdfdc33d00863`.
- Root gửi nhận định khi maker đang xem. **Maker tự đối chiếu ảnh và không đọc critic actual277**; findings dựa trên ảnh thực, không nhận độc lập khỏi mọi thông tin root hoặc tự duyệt output mình.
- Capability **ALL_FRAME_STILLS_NOT_AV**. Chưa nghe thực tế hoặc xem chuyển động/AV liên tục; D06/N07/single speaker/sync/thời lượng lời vẫn UNKNOWN/NOT_CERTIFIED. Không suy giọng nam từ miệng mở cuối cảnh. Không script/công cụ mới, ASR, trình duyệt/API/credit/git/render hoặc sửa media.
- Run ghi một output6s giá10, số dư1043→1033, đã dùng197/500, first-pass còn82, reserve đóng. Maker chỉ đọc thông tin nguồn gốc, không chi. Owner277 duyệt **điểm nối C05→C06**, không C07 hoặc C06→C07. F bắt đầu từ0, Fn=n/24 giây.

## Findings actual

| ID / mức độ | Khung / giây | Yêu cầu → quan sát và hệ quả |
|---|---|---|
| BOWL01 / **MAJOR — chọn bát Khoai thay bát Đào** | Tay đi khoảng F49–63 / 2,042–2,625; tiếp xúc bát trái F64–70 / 2,667–2,917; dịch bát F71–93 / 2,958–3,875; trạng thái sai tới F143 | Final: Đào nắm thành ngoài bên trái của **bát riêng ngay trước cô bên phải**, trượt ngắn sang trái dưới A. Actual cô vươn xa sang trái qua tay trong Khoai tới **bát của Khoai bên trái**, nắm phía phải bát ấy và kéo nó sang phải về gần giữa. F64/F80/F95 cho thấy bát trái dịch; bát Đào bên phải giữ nguyên. Không có bát nhận riêng của cô được chuẩn bị. Đây là sai danh tính/đích của đạo cụ, không chỉ ngược hướng hoặc lỗi tay nhỏ. |
| ENTRY01 / **MAJOR — lệch trạng thái vào cần xử lý trước chọn** | START→F0; F0–23 / 0–0,958 | START C06 F56 có tay Khoai đưa ngang trước người, A gần phía trái bát Đào và đang chuyển sang. Native F0 tái dựng tay/đũa/A về phía Khoai rõ rệt; mắt/mày Đào thấp, môi hơi chu khác START. F0–23 tay nâng rồi hạ nhỏ tại phía mình, sau đó mới tiến sang. Không đọc được “tiếp ngắn cùng chuyển động từ F56 rồi giảm tốc”. Đây là reset đầu nguồn, không chỉ khác nụ cười. Chưa kiểm điểm nối AV hoặc chuyển động thực nên không chứng nhận tốc độ đảo; chênh vị trí đã rõ. |
| ACTION01 / A còn kẹp, không thấy thả/ăn | Toàn bộ F0–143; đi sang rõ F24–39, giữ từ khoảng F40+ | Một A còn ở tips của đôi đũa riêng trong tay ngoài trái Khoai, xa miệng; không thấy ăn/thả/rơi/nhân đôi hoặc thêm đôi đũa. Tuy nhiên bát đích không được chuẩn bị đúng, nên đường A riêng không bù BOWL01. |
| GLASS01 / không thấy lỗi cốc vào bát | Toàn bộ F0–143 | Cốc nâng trong tay ngoài phải Đào, tách lòng cả hai bát. Không hạ/đặt/nhấp hoặc đổi tay. Biến thiên nhỏ do tái dựng không phải pose bất biến từng pixel. |
| CONTACT01 / nắm sai bát; chưa khẳng định xuyên vật lý | F64–95, ảnh nguyên F64/F80/F95 | Tay cô nắm vùng vành/thành phải bát Khoai, có ngón chồng hình lên vùng vành/lòng; khác yêu cầu nắm dưới vành bát Đào. Ảnh không đủ chứng minh từng ngón xuyên vật lý. Wrong bowl đã đủ MAJOR; không bịa thêm lỗi tay để tăng mức. |
| MOUTH01 / Đào nói; nam mở miệng cuối cần kiểm | Đào khoảng F50–101 / 2,083–4,208; nam F141–143 / 5,875–5,958 | Đào có chuỗi khẩu hình rõ rồi khép môi. Khoai kín môi phần chính, nhưng mở ở3 khung cuối, trái yêu cầu kín toàn cảnh. Không chứng minh có tiếng nam hoặc nói thay N07; chưa dùng tiếng/ASR. Cắt có thể loại đuôi nếu đoạn đủ nhiệm vụ, nhưng không sửa BOWL01/ENTRY01. |
| ACT01 / hình phần chính phù hợp trêu nhẹ; sắc thái tiếng HOLD | Đào nhìn từ A lên Khoai khoảng F37–40, hình nói F50+ | Đào ngước nhìn anh, mày chuyển, miệng hoạt động và có gesture nói; không thấy nhìn camera, cười lớn hoặc ôm kiểu lãng mạn. Có thêm gesture mở lòng bàn tay kéo dài trước nắm sai bát. Không nhận giọng trưởng thành/sắc thái/nguyên văn N07 đạt chỉ từ hình. Khoai nghe nhẹ, không diễn lại lời chữa cháy phần chính. |
| FOOD/DOP01 / không thấy MAJOR khác | Toàn bộ F0–143 | Hai mặt/tay/A/cốc/bát đọc được; trục, ánh sáng ấm, camera chung giữ. Rau trước trái, hai đồ chấm, nem nguội không khói, watermark giữ. Không cắt/zoom/thêm đạo cụ hoặc thiết kế lại danh tính rõ. |

## DIR / EDIT — thiếu nhiệm vụ, không đề nghị range

Chuỗi actual: reset về phía Khoai → anh đưa A sang/giữ → Đào ngước nhìn → nói và gesture tay → **lấy bát Khoai dịch sang phải** → rút tay về cạnh bát Đào → hai người chờ, Khoai mở môi cuối. Nhiệm vụ “Đào chuẩn bị bát của mình” không xảy ra trong phần nguồn đã xem. Cắt trước tay sai chỉ còn lời/gesture, thiếu chuẩn bị bát; cắt sau vẫn sai bát. Không đề nghị chọn đoạn, không crop/cận món/đổi nhãn bát hoặc tự gộp C08 để gọi C07 đạt.

Native6s không phải selected6s. Còn151 khung =6,291667s cho C07–09; giữ full C07 sẽ chỉ còn7 khung =0,291667s cho hai cảnh cuối, không đủ nhiệm vụ theo thiết kế. Chưa có range đạt nên chưa đo thời lượng chọn thực. Không bỏ nhận/thả/kết B hoặc cắt âm N07 để vừa35. C08 HOLD vì source/range/bát nhận/điểm nối chưa đạt, dù A còn kẹp và cốc đúng.

## Chẩn đoán nguồn → prompt → kiểm đầu vào

**Đã quan sát:** native chọn sai bát dù final đã nói “her OWN EMPTY beige bowl”. START có hai bát gần giống, cùng màu/chất liệu/trạng thái rỗng; model chưa giữ đúng quan hệ sở hữu. Reset đầu cảnh là tái dựng nguồn; chưa chứng minh Ingredients là nguyên nhân duy nhất hoặc cấu hình/giá sai.

**Khe hở thiết kế/kiểm giấy:** “inner LEFT-screen hand”, “OUTSIDE LEFT wall”, “slide ... screen-left” dùng LEFT cho tay, grip và hướng dịch nhưng chưa neo độc nhất bát Đào bằng quan hệ vị trí. Bát Khoai cũng rỗng/beige, ở bên trái. Prompt cấm bát mới nhưng chưa khóa bát Khoai đứng yên/Đào không chạm. Maker đã kiểm đường tay nhưng **chưa coi phân biệt hai bát giống nhau là rủi ro cụ thể đủ mạnh**. Cần kiểm identity-before-motion, không chỉ action cuối; preflight không bảo đảm output.

**Giả thuyết, chưa chứng minh nhân quả:** model có thể ưu tiên LEFT và lấy bát trái, rồi kéo vào giữa để “chuẩn bị nhận”. Không có thử nghiệm chỉ thay wording nên không kết luận duy nhất; voice/nụ cười/gesture cũng chưa được chứng minh gây sai bát. Không đổi D06/N07/camera/set/route từ lỗi này.

## Can thiệp giấy cho targeted retake — chưa final / chưa GO

1. Neo bát Đào là **bát screen-right ngay trước cô, ngay bên phải tay trong đang nghỉ, bên trái đôi đũa nghỉ ngoài phải, dưới và bên trái cốc nâng**. Đây là quan hệ trên ảnh, không dời props/canon. Bát Khoai ở trái trước anh phải đứng yên; cô không chạm hoặc vươn qua tay nghỉ của anh tới đó.
2. Tách hai hướng: tay cô từ vị trí nghỉ đi ngắn **sang phải** để nắm thành ngoài bên trái **bát ngay trước cô**, ngón dưới vành. Sau khi nắm đúng mới trượt cùng bát ngắn **sang trái** dưới A. Không gom thành vươn xa sang trái. Đáy bát trên bàn, A/tips cách vành; cốc giữ nâng trong tay ngoài phải. Không thêm gesture mở lòng bàn tay trước nắm.
3. Neo entry từ exact F56: A đã gần bát Đào, tay ngoài trái Khoai đã duỗi. Chỉ tiến rất ngắn rồi giảm tốc/giữ; không quay A/tay về bát Khoai hoặc nâng đũa lên diễn mời lại. Không thêm lời hoặc nhịp cảm xúc.

Có thể chuẩn bị retake trong scope238 sau root/critic đối chiếu actual, khóa final/hash mới và live gates; **report này không cấp paid GO hoặc retry tự động**. Đây là một output C07 đầu sai bát, chưa phải hai C07 take cùng lỗi. Nếu lượt sửa lại sai cùng MAJOR bát thì STOP_FOR_DIAGNOSIS. Không lấy lỗi C06 khác shot để đổi counter, cũng không dùng ngân sách còn lại để chạy mò.

## Đọc draft T02 — chưa current-final GO

Đã đọc đầy đủ `04_requests/C07_T02_prompt_DRAFT_277.txt`, tự hash `6014f1c07324b7937d18cbb3f657c7d8c15363156f5fae34fdce670ccc5aa5b7`. Draft neo bát nhận bằng các quan hệ đúng trên ảnh; bát Khoai đứng yên, không vươn qua tay anh. Đúng thứ tự tay đi phải nắm bát Đào rồi trượt bát trái; A ở gần cẳng tay trong Đào/trên mép trái bát cô, không quay về Khoai hoặc nâng lại lên ngực. Không đổi N07/D06/set/camera/C07–08.

Draft xử lý đúng khe hở phân biệt đích và entry pose đã quan sát; **không chứng minh đó là nguyên nhân duy nhất hoặc bảo đảm take mới đạt**. Chưa thấy conflict giấy mới. Rủi ro còn: grip dưới vành bị tái dựng sai; hai bát vẫn giống nhau; A tự hạ/thả khi bát tới; Ingredients không khóa vận tốc chính xác. Không chỉ kiểm end frame.

Root phải đọc actual/diagnosis, tích hợp critic, khóa final/hash mới rồi maker đọc lại trước live. Draft chưa paid permission/current-final PASS/actual PASS; chưa T02, không tự retry hoặc mở C08.

## Kết luận

**C07 T01 SOURCE_REWORK / NOT_SELECTED; không range hoàn thành nhiệm vụ.** MAJOR bát Khoai và reset entry; D06/N07/sync chưa kiểm. Cốc/A còn kẹp/bố cục món đúng không bù đích bát. Root đọc actual độc lập và report này, khóa can thiệp neo vị trí độc nhất + tay đi phải/bát trượt trái trước final/live gates nếu mở retake hợp lệ. C08 và C06→C07 seam HOLD; không cắt che lỗi hoặc giao owner audit lỗi rõ thay root.

## Refresh final T02 — current-final maker preflight

Sau proofread báo cáo này, maker đã **đọc đầy đủ** `04_requests/C07_T02_prompt_277.txt` và `04_requests/C07_T02_preparation_277.json`; tự hash final **`ae636235971fb36f5a31234dcb294cb91ea5d12c9231c8b046b797b8ad756ef4`**. Draft và hash ở trên chỉ là lịch sử; kết luận preflight mới áp đúng final này.

Final sửa neo A từ “above LEFT edge” thành **“just LEFT of HER RIGHT-SCREEN bowl and visibly above its rim height”**. Điều này sát START hơn: A đang ở cạnh cẳng tay trong Đào, hơi trái bát và cao hơn vành, không đã nằm trên tâm lòng bát. Giữ đầu đũa/tay ở đúng trạng thái, tiếp rất ngắn rồi giảm tốc; không rút về Khoai hoặc nâng lên ngực. Khóa bát Đào độc nhất bằng tay nghỉ/cốc/đũa; chỉ nó được cô chạm. Tay đi phải một đoạn ngắn nắm thành trái, rồi bát trượt trái ít trên bàn. Bát Khoai đứng yên, không vươn qua tay anh; cùng A còn kẹp, cốc nâng và chỉ D06/N07 giữ nguyên.

**Không thấy blocker giấy mới hoặc thay đổi ranh giới kể chuyện.** Hai họ can thiệp sửa đúng finding T01: nhận dạng bát và kế thừa entry pose. Không đổi giọng, shot, đạo cụ, route hay nhiệm vụ. Geometry vẫn cần actual kiểm: ngón nắm dưới vành, tay không xuyên A/tips, bát đúng không dịch quá chỗ Đào, gap còn rõ và không thả ở cuối. Không khẳng định thêm quan hệ vị trí là nguyên nhân gốc duy nhất hoặc bảo đảm take sửa đạt.

**CURRENT_FINAL_PAPER_INPUT_READY_FOR_INDEPENDENT_AND_LIVE_GATES.** Root phải đọc phiên bản báo cáo hoàn chỉnh, đối chiếu critic current-final, kiểm exact reference/D06/prompt/config/quote≤15/ngân sách retake trước nếu quyết định một lượt sửa trong238. Giá10 chỉ lịch sử; chưa submit. T01 chưa audio approval, không chuyển sang T02; output/sync/seam/timing35 chưa được bảo đảm. Nếu T02 lại sai cùng bát hoặc entry MAJOR lặp, **STOP_FOR_DIAGNOSIS, không tự T03/C08**.
