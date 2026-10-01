# P6 — Vòng kiểm visibility tay/đũa

2026-10-01. Owner: “làm tiếp, làm liên tục đi để tôi check xem”. Tiếp nối58: tiến hành image-only probes theo lỗi/evidence từng lượt, giữ version, review trước lượt tiếp. Không tự đổi canon/script, không món retry, không voice/video. Cap200 hiện hành; UI0 không là billing hoặc quyền vô hạn. P6 OPEN.

## T3 — cận tay từ I06

Input: current editor asset `d7f731fc-225c-4020-a940-dff7779b021b`, download read-back hash `05DD189AA31AC32A330C316D4B9068EEFDFB8D76CF0355C43A91E0B8DD44FC8F` bằng local I06. Không dùng tên asset I04 làm version proof. I06 local giữ nguyên.

Hypothesis: đổi framing, không đổi grip, sẽ giúp đọc support/contact rõ hơn. Yếu tố đổi: tight camera framing. Chấp nhận: rõ cả hai que từ handles đến tips, ngón cái/ngón cong/cuff giữ pose, không drift hand/que; nhìn được đủ cấu trúc điểm tựa để review. Generation không là deterministic crop, không xác minh ngược phần bị che của I06 bằng chi tiết AI bịa thêm. Nếu vẫn bị che, xem góc bổ sung hoặc reference thay vì vô hạn yêu cầu nhìn xuyên tay. Không đòi visible mọi ngón mọi contact trong một ảnh.

Settings observed: Nano Banana Pro,9:16, UI0credit, editor một output. Count T3=1 trước review. Lượt kế tiếp nếu cần phải có hypothesis và manifest mới, không repeat mù.

Exact prompt:

```text
Create a tight diagnostic close-up from this exact image, changing only the camera framing. Center the existing raised potato hand, cream shirt cuff, wrist and two wooden chopsticks; include the complete rounded handles on SCREEN LEFT and the complete long tapered tips on SCREEN RIGHT. The hand should occupy most of the frame. Preserve its exact existing thumb, curved finger arrangement, wrist angle, stick separation and hand-to-stick contacts; do not redesign the grip, rotate the hand, mirror the image or add fingers. Keep the same golden potato skin texture, navy sleeve, warm ivory studio background and lighting. No food, extra hands, extra sticks, labels or text. This is a detail view of the same pose, not a new gesture.
```

Run: submit1, 0%→94%→output accessible. Saved `media/raw/ep01_p6_consistency/H-K-I07_v0.1.jpg`, SHA256 `CC0819A1420EEFB2CF6F09FB4AC6191840380E79C459DFE1753401F5325741B8`. Source download `C:/Users/PC/Downloads/dda601fb-671f-4f9b-8361-d7f57b9f1070.jpg`; proof `H-K-I07_flow-proof.png`. Root actual-view: framing cận đạt, thấy hai que tách, thumb và các ngón cong rõ hơn, que dưới có ngón cong phía dưới; điểm tựa thumb-web chưa đọc trọn. Không gọi chi tiết được model dựng thêm là chứng minh pixels I06. CONT review được đăng ký riêng trước dispatch, chưa quyết định thử tiếp khi review chưa về. Food F-NB-02 UNRECONCILED, T2 generic finger-repair HOLD. Không promote hoặc đóng P6.

CONT AP-MEDIA-03 report11 completed: static eating-grip readability `PASS_FOR_NEXT_GATE`, KEEP_FOR_OWNER_REVIEW cho I07 riêng. Upper control/lower support đủ nhận diện, ordinary occlusion không tự là blocker; mechanics phần khuất UNKNOWN và motion NOT_TESTED. Root đồng ý scope; không yêu cầu nhìn xuyên tay hoặc tiếp tục sửa khi chưa có defect.

## T4 — tích hợp grip vào khung nhân vật

Changed factor: framing/context từ closeup sang waist-up. Không finger-repair hoặc đổi action. Target canvas I07; reference explicit **I06** local cùng hash58, upload mới qua composer và chọn exact `H-K-I06_v0.1.jpg`; screenshot thấy thumbnail fullbody Khoai trong composer trước submit. I06 là identity/outfit/pose reference, không thay target. Không attach nguồn món/ảnh người. Current editor Pro9:16, UI0 đã đọc lượt T3; model không đổi. Count1 rồi actual-media review.

Hypothesis: expand có explicit identity reference sẽ giữ upper/lower-support readibility cùng gương mặt/cuff/sleeve trong một ảnh dùng được cho owner xem. Expected: khuôn mặt Khoai theo I06, tay không quá lớn, hai que/thứ tự supports giữ I07, complete sticks in frame, no extra arm. Không coi cùng source là đảm bảo identity. Nếu drift thì không promote; chỉ sửa vùng lỗi cụ thể có rationale mới.

Exact prompt:

```text
Expand this exact hand close-up into a waist-up portrait of the same potato character. Use the attached full-body image ONLY as the reference for his face, potato silhouette, outfit, body proportions and arm placement. Keep the current close-up's raised hand, visible thumb and separate upper-finger control/lower-finger support, cream cuff and two wooden chopsticks as the hand design; do not replace it with a fist grip. Show his complete face, shoulders, torso to the belt and this raised hand at natural scale. Keep the hand on SCREEN LEFT of his body, the short rounded chopstick handles pointing SCREEN LEFT and the complete long tapered empty tips pointing SCREEN RIGHT. Preserve the navy overshirt with chest pocket and cream collared shirt, golden speckled skin, warm ivory studio background and soft lighting. One character, exactly two arms and two chopsticks. No food, bowl, extra hands, extra sticks, mirror reversal, labels or text. The grip is the same static pose; this is framing integration, not a new action.
```

T4 submit1, 0%→output accessible. Saved `H-K-I08_v0.1.jpg` raw consistency; SHA256 `D3DA6BA6A591BCF24159E521E3B24BFB30ACE1268C9B36F750B09E49C6724900`; download `C:/Users/PC/Downloads/58873d57-212c-4d08-b7ab-014847039557.jpg`; proof `H-K-I08_flow-proof.png`. Root actual-view: identity/pose nhận diện được nhưng **framing DEFECT: fullbody, không waist-up**. Grip nhỏ lại, output giống I06 về bố cục; không chứng minh model đã dùng detail I07 theo intent. T4 NOT_MET cho target integration-readability. Không autoapprove.

## T5 — diagnostic aspect/framing

Root inference: hand dang bên + trọn đũa rộng làm tight waist-up9:16 khó với pose bất biến; attachment fullbody có thể neo composition. Đây là hypothesis, chưa causal proof. Target current I08, local phiên bản giữ nguyên. Không attachment ở composer sauT4 (submit cleared). Thay khung kiểm từ9:16 sang3:4 và yêu cầu tight waist-up: một can thiệp framing bundle, **không controlled single-variable aspect experiment** vì target và reference configuration khác T4. Không đổi TikTok delivery9:16 hoặc body pose. Count1, no food/no video. ModelPro giữ nguyên, đọc UIcost lại.

Exact prompt:

```text
Reframe this exact image as a tight waist-up diagnostic portrait in the selected 3:4 frame. The frame must contain the complete potato face, raised hand and both complete chopsticks, shoulders and torso ending at the belt. Exclude legs, shoes and the floor; keep only a small margin above the head. Preserve this character's exact face, body shape, navy overshirt, cream collared shirt, natural hand size, thumb and curved fingers, wrist angle, two separated wooden sticks and current arm pose. Rounded short handles stay SCREEN LEFT and tapered long tips SCREEN RIGHT. Do not redesign the grip or move the arm; change framing only. Same warm ivory background and soft light. No food, bowl, extra hands, extra sticks, labels or text.
```

T5 settings verified Pro3:4/UI0, submit1→0%→output accessible. Saved `H-K-I09_v0.1.jpg`, SHA256 `2522CBB562EB8EA59DE2749EBD022BDFEF02C834B739237C74F9B3FF4717D2DA`; download `C:/Users/PC/Downloads/1be43e45-ffe3-422c-b0c1-cd0749fed18e.jpg`; proof `H-K-I09_flow-proof.png`. Actual System.Drawing metadata **896×1200** (gần3:4, không exact ratio); I07/I08 actual768×1376. Root xem actual I09: waist-up, không chân/sàn; mặt Khoai và tay/đũa đủ khung, two-stick/tipsright giữ, upper-control/lower-support nhìn rõ hơn fullbody; nhận diện mặt/outfit giữ. Headroom còn rộng hơn “small margin”, không gọi exact framing prompt perfect. AP-MEDIA-04 đăng ký04 trước dispatch, báo cáo độc lập12 trước promote. Không cần crop9:16 ảnh diagnostic bằng cách cắt mất tay. Không voice/video/food request mới. Tổng vòng này3 submits/3 outputs actual; chưa đối soát ledger billing, UI0 không là khẳng định free.

Đã rename current Flow asset thành `Khoai grip I09 - diagnostic 3x4`, read-back name verified; proof bổ sung `H-K-I09_owner-review-proof.png`. AssetID/versions history giữ nguyên. I06 upload làm support là thẻ riêng; không xóa ảnh hoặc restore old version. Editor aspect hiện3:4 cho diagnostic; trước request video/future9:16 phải đặt/verify lại, không mặc định.

CONT AP-MEDIA-04 report12 hoàn tất actual4JPEG: I09 bounded static recognizable identity + grip-readability PASS_FOR_NEXT_GATE / KEEP_FOR_OWNER_REVIEW. Root đọc fullreport và đồng ý phạm vi, không coi headroom là exact framing target đã đạt. Không thêm generation khi không có defect trọng yếu trong scope; refs chờ ownerselection ở60, không autoassetapproval. Reviewer có retained history, không freshblind.

## Tổng hợp vòng

Đã xác định: I07 readable handdetail; I08 giữ identity nhưng fail framing; I09 có mặt/tay/đũa đọc được trong một portrait, reports11/12 xác nhận bounded static scope. Quyết định đã chốt: tiếp tục có logs+versions, không retry mù, không tự promote hoặc chuyển video; đề nghị owner xem cặp I07/I09. Giả định: ordinary occlusion không phải lỗi nếu đủ nhận diện supports; still không chứng minh chuyển động. Vấn đề mở: owner chọn ref, hidden mechanical certainty ngoài static scope, motion/action, food unreconciled và các gap P6 khác. Tiếp theo: ownercheck cặp ref; lập action/shot probe theo exact script và food input khi các gate sẵn sàng, không ép3:4 diagnostic thành final9:16 hoặc tự đóng P6.
