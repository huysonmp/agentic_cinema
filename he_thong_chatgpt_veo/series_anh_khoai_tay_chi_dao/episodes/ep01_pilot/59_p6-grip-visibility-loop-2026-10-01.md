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

T4 PREPARED. Không voice/video/food request mới. Output sẽ là candidate mới, không overwrite local I06/I07 hoặc autoapprove.
