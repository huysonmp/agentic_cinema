# REC287 — Chẩn đoán độc lập diễn mặt–thân Khoai, chưa sửa hoặc sinh mới

Ngày 13-10-2026. Reviewer `food_repair_critic_283`, bounded local REC217. Owner nhận xét **“chuyển động của khoai chưa ok đâu”**, sau đó root báo owner chọn ưu tiên **“Diễn mặt–thân người”**. Đây là diagnostics, không quyền sửa, paid retry hoặc thay chỉ đạo nhân vật.

**Scope thực: toàn123 source frames và124 output frames tại board scale, dense source F64–122 qua action boards, critical full-resolution stills. Không continuous playback, nghe thực, phoneme/action alignment hoặc motion/AV PASS.**

## 1. Kết luận trước

Nhận xét owner cần mở **ACT/PERF mặt–thân**, không chỉ lặp lại lỗi yếm/hậu cảnh đã bác286. Qua hai chuỗi ảnh dày, phần lớn nhịp mắt–miệng và hướng tay của Khoai **đã có ở source C05→C06**, bản edit286 có hình thức rất tương tự ở cùng frame index. Vì vậy chưa đủ căn cứ gọi toàn diễn thiếu tự nhiên là lỗi mới do food edit hoặc một câu prompt283 gây ra.

Vấn đề cần kiểm tiếp là **mức đọc được ý định “bị bắt gặp, bình tĩnh chữa cháy” qua phối hợp mắt/mày/đầu/thân**, thay vì chỉ thấy mặt cử động theo nói còn người giữ pose rồi tay đi sang bát. Đây là giả thuyết diễn xuất có evidence ảnh, chưa là kết luận nhịp playback hoặc emotion từ một âm tiết. Owner đã bác chất lượng diễn output hiện tại; giữ NOT_SELECTED, không dùng approval source276 để bác feedback mới.

## 2. Exact inputs và coverage

- Source `C:/Users/PC/Downloads/du_an_nem_bui/276_C05_C06_JOIN/C05_C06_5p125S_JOIN_QC_NOT_FINAL.mp4`, SHA kiểm lại `42d826e1356ce67acc6e1057b4ceefc9703f3e705ffa14ae6c09dea7934b5bdf`,123F/24fps/5,125s.
- Output286 `C:/Users/PC/Downloads/du_an_nem_bui/286_FOOD_EDIT_PROJECT_PROMPT/EP01_720_C05_C06_FOOD_EDIT_T01_NATIVE_286.mp4`, SHA kiểm lại `4703fb9b34abbb63144364cb388aa4d9921e06d7b7c597f2da77d04a7299e583`,124F/24fps/5,166667s video. Không sửa file.
- Trực tiếp xem source eight boards `C:/Users/PC/Downloads/du_an_nem_bui/287_KHOAI_MOTION_QC/source_full16_01.png`…`source_full16_08.png`: consecutiveF0–122, trang cuối11 real +5 black padding. Output eight full16 boards đã xem trong actual286; run287 xem thêm output mouth_hands6fps01–03 cùng source6fps01–02. Source action_all09–16 trực tiếp xem dàyF64–122.
- Fullres xem riêng run287: outputF80/F104/F110/F116/F120; sourceF104/F110/F116/F120. Fullres outputF0/F65/F66/F71/F72/F123 và sourceF0/F65/F66/F72/F122 đã xem actual286.
- Đọc đầy đủ C06 T03 prompt275, run275 và acceptance276. Source join có C05[0,66) + C06 selected prefix[0,57); **không dùng96F full C06 tail đã bị bác sớm thả món** để đánh giá endpoint này.

Các frame đối chiếu cùng index chỉ là **container-start comparison**, không chứng minh alignment từng phoneme/action. Root có tạo silent compare `SOURCE_LEFT_EDIT286_RIGHT_SILENT_COMPARE_QC_NOT_FINAL.mp4`, reviewer kiểm hash `8f8fb12736578f9a26cdc09e37bf8131531b05a9aa7a0f52f1e42f275a017d17` nhưng **chưa phát/xem liên tục clip đó**. Không lấy sự tồn tại MP4 làm actual playback.

## 3. Chuỗi diễn mặt–thân quan sát được

| Range source/output gần cùng index | Quan sát từ chuỗi dày | Ý nghĩa và giới hạn |
| --- | --- | --- |
| F0–47 | Khoai giữ tay/đũa trước mình, mắt hướng Đào; đầu và thân khá yên trong khi Đào có mouth activity. Source/output cùng kiểu giữ pose. | Stillness khi nghe không tự là lỗi; chưa thấy evidence edit tạo mới toàn sự cứng. Cần đọc áp lực “bị bắt” khi phát, không thêm head bob chỉ cho có chuyển động. |
| F48–55 | Khoai hạ mí/chớp, rồi mở lại; xảy ra ở cả source/output trước N06. | Có reaction bằng mắt nhưng chưa chứng minh một beat quyết định rõ hoặc timing với câu Đào nếu chưa nghe. |
| F64–77 | Face caught/khép môi chuyển vào articulation; hand còn ở vị trí cũ. Source cut tại66, output có thay hậu cảnh lớn tại72. | Trạng thái chuyển lượt có trong nguồn; backdrop edit làm discontinuity riêng. Không quy mọi cảm giác giật mặt vào cut này nếu chưa playback. |
| F78–85 | Mí Khoai có pha đóng/hạ và miệng mở rộng/lộ răng; sau đó mắt mở. Pattern cũng hiện rõ trên source dense boards10–11. | **Không gọi miệng mở là cười vui**: có thể phonetic articulation. Cần xem/nghe cả câu để phân biệt “nói” với grin/diễn quá vui. Không sửa bằng cấm răng hoặc freeze lips. |
| F86–103 | Miệng khép rồi mở lại theo nhiều shape; tại cuối range chuyển dần về nét khép miệng/mỉm nhẹ. Đầu/torso còn khá cố định. Source/output pattern tương tự. | Không đủ ASR hay stills để gắn mỗi shape với từ. “Mỉm nhẹ” mô tả hình, chưa chứng minh tâm trạng đắc ý; cần xét mày/mắt/thân đi cùng. |
| F104–123 | Miệng khép/mỉm nhẹ, gaze thay từ Đào sang vùng món/bát; cánh tay/đũa di chuyển sang phải. Source cũng có pha này và selected exit đang chuyển động. | Hành động đi sau articulation về mặt hình là hướng đã thiết kế, không tự gọi chậm doedit. Coupling mặt–thân với ý “chữa cháy” còn cần human playback; không bắt endpoint đứng yên theo brief cũ đã được owner thay. |

Điểm cần kiểm nghệ thuật: khuôn mặt có thể đọc như **một vòng articulation khá rộng rồi mỉm nhẹ**, trong khi đầu/thân ít góp ý định và tay mới thực hiện redirect cuối. Nếu khi phát owner thấy giống “vui vẻ đưa món” hoặc “mặt diễn máy”, phải đổi thiết kế/performance có chủ đích; không thêm số tính từ “tự nhiên” vào food-only prompt và hy vọng tự sửa.

Đây là **interpretation cần xác minh**, không chắc chắn Khoai cười sai ở F80. Một actor cũng có thể gần bất động để giữ bình tĩnh; cái cần đạt là intent, không bắt buộc nhiều chuyển động hoặc chuỗi cảm xúc phức tạp trong vài giây.

## 4. Tay/đũa/A — scope phụ, không che mất trọng tâm owner

F104→110→116→120 và exit thể hiện cánh tay đưa tips/A từ phía bát riêng Khoai sang hướng bát Đào, tay trong vẫn nghỉ; không vào miệng, không pickup mới hoặc thả ở đoạn được kiểm. Output có nhúm dải rủ dài hơn lát A nguồn, làm silhouette/occlusion khác. Tại fullres không thấy joint bị đứt hoặc đổi tay rõ; **không đủ để chứng nhận grip/contact/physics hoặc chuyển động tự nhiên** từ ảnh tĩnh.

Hướng redirect nguồn và output có cùng cấu trúc tổng quát. Không đo vận tốc/gia tốc hoặc depth/clearance bằng pixel trong run này; không gán số “tay quá nhanh/chậm” hoặc food height nếu chưa dữ liệu. Không áp fullnative275 early-release lên prefix source hoặc kết luận cầm đũa ngược khi không quan sát được lỗi đó.

## 5. Prompt, source và lỗi kiểm trước

C06 prompt275 yêu cầu caught-and-composed, không presenting/celebrating; articulation tự nhiên/răng được phép; sentence trước hand movement, cùng A giữ trên tips. Nhưng acceptance276 đã chốt **slightly embarrassed acting trên exact prefix57 và cut-on-motion**, thay endpoint stop/hold cũ. Phải ưu tiên actual selected range và decision mới, không đánh giá prefix như clip4s buộc dừng hoàn toàn.

Prompt283/286 chỉ sửa món và yêu cầu preserve source expressions/motion; nó **không thiết kế lại diễn mặt–thân**. Khi khuynh hướng diễn hiện trong nguồn, cố giữ nguồn sẽ không tự tạo performance mới hơn. Source đã từng owner chấp nhận không có nghĩa review286 được bỏ ACT/PERF hoặc feedback287 vô hiệu; quyết định cần làm rõ là cải thiện performance source-derived, không sửa món đơn thuần.

Report286 ghi `PARTIAL_VISUAL_ONLY` và `LIMITED_VISUAL`, không motion/performance PASS, đã NOT_SELECTED vì MAJOR khác. Vì vậy **không có motion PASS thật để thu hồi**. Tuy nhiên phát hiện owner cho thấy phần review diễn trước chưa diễn giải đủ **intent và coupling mặt–thân theo chuỗi**, chỉ nói thứ tự mouth activity/props. Cần bổ sung finding/validation này vào gate ACT/PERF; không đủ chỉ viện caveat “chưa continuous AV” để hết trách nhiệm sàng lọc/đặt kiểm tiếp.

Maker287 root báo thất bại capacity trước final report; không gọi maker đã hoàn tất/chứng nhận diễn. Báo cáo này là independent actual read/view, không tổng hợp paper roles như actual quality PASS.

## 6. Bước xác minh tiếp — không paid/fix trong chẩn đoán

1. Root trình owner source và edit cùng sequence để phân biệt **source-derived diễn** với edit-induced drift; dùng silent compare như diagnostic có nhãn alignment container-start, không production. Owner đã chọn mặt–thân, không hỏi lại tay/mặt/both.
2. Human playback cả chuỗi: có thấy Khoai bị bắt và đang giữ bình tĩnh khi bịa cớ, hay đọc vui vẻ/thản nhiên/robotic? Gắn finding bằng moment cụ thể; khi xét lời phải dùng bản có tiếng đúng nguồn, silent compare không chứng minh voice/sync hoặc phoneme-to-eye timing.
3. Trước sửa, lập một beat-level acting brief **đề xuất**: trạng thái khi nghe → quyết định chữa cháy → nói với articulation bình thường, mày/mắt/thân cùng intent → kết câu chuyển A; phân biệt bất biến/được đổi. Owner chọn direction/mức restraint, không giao họ tự viết prompt kỹ thuật.
4. Nếu mục tiêu thực sự đổi performance, trình scope ngoài food-only/source preservation, ảnh hưởng audio/khẩu hình/cut/resources và cap trước action. Không tự sửa285prompt, chọn sourcefailedtail, freeze/speed/overdub hoặc sinh retry; không phản xạ thêm agent mới khi vai ACT/PERF đã có.

**Disposition: OWNER_REPORTED_ACT_PERF_REWORK_OPEN / SOURCE_DERIVED_PATTERN_OBSERVED / CONTINUOUS_PERFORMANCE_VALIDATION_PENDING / NO_RETRY_OR_FIX_AUTHORITY.** Clip286 vẫn NOT_SELECTED vì MAJOR visual drift; không audio/speaker/sync PASS, không nguyên nhân duy nhất đã cô lập hoặc cam kết phương án sửa đạt.
