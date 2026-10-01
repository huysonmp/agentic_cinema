# P6 — T1: đổi hướng đũa, giữ nguyên tay

Ngày 2026-10-01. Owner: “làm tiếp đi”, tiếp nối preflight57. Scope: upload I04 riêng, một T1 image edit; không retry món, không T2, không voice/video. P6 OPEN.

## Input và preflight

- Local control: `media/raw/ep01_p6_consistency/H-K-I04_v0.1.jpg`, SHA256 `412367B419CD3EEADD65390BD853A790776FFC7E354B6ACFB1F1970A74C93557`.
- Upload thành asset mới `d7f731fc-225c-4020-a940-dff7779b021b`; không ghi đè asset I05 `ef5c30f0-736b-4d59-999f-6ddca114e77b`.
- URL: https://flow.google.com/u/1/project/9276788e-9781-44fb-ba5b-083006667374/edit/d7f731fc-225c-4020-a940-dff7779b021b
- Download canvas sau upload: `C:/Users/PC/Downloads/12b8e83b-2006-4351-a670-be12e4a751c6.jpg`, SHA256 `185677A1839515FB36E4E2372A296C0D373FC8DFC01DE83BB7A3A19CB3B00D4B`. Hash KHÔNG bằng local control. Đã xem cả hai ảnh: hình tương ứng I04, đủ full-body, lòng bàn tay/ngón cái thấy rõ, đũa hướng trái. Không khẳng định byte-equivalence hoặc pixel-equivalence; dùng bản upload-render của I04 làm input, ghi nhận khác biệt encoding chưa kiểm chứng nguyên nhân.
- Editor chọn explicit Nano Banana Pro, 9:16. UI giá 0 tín dụng tại preflight; không phải đối soát billing. Một submit editor; không batch.

## Exact prompt T1

```text
Edit this exact potato image. Change only the orientation of the two wooden chopsticks along their existing axes: place their long tapered empty tips to SCREEN RIGHT and their shorter rounded handles to SCREEN LEFT. Keep the existing hand, visible thumb, curved fingers, wrist and forearm pose unchanged; do not rotate or mirror the hand or the image. Keep exactly two separate sticks, with plausible hand contacts. Preserve this exact character face, potato silhouette, clothing, body proportions, other arm, framing, light, ivory background and platform watermark. No food, new hands, additional sticks or text.
```

## Run / QC

Đã submit **1** lần trên editor asset mới; UI 0% → 67% → ảnh hiện ra (không terminal lỗi). Download actual JPEG vào `media/raw/ep01_p6_consistency/H-K-I06_v0.1.jpg`. SHA256 `05DD189AA31AC32A330C316D4B9068EEFDFB8D76CF0355C43A91E0B8DD44FC8F`. Download gốc `C:/Users/PC/Downloads/1a10fcac-4a4d-49e7-b549-a71a644ec115.jpg`. Proof `media/raw/ep01_p6_consistency/H-K-I06_flow-proof.png`. Input/output/proof là local gitignored media, không được push binary vào GitHub. Chưa đối soát ledger credit.

Root đã mở ảnh output thực: hai que tách biệt bên ngoài tay; đầu dài thon hướng phải, đầu ngắn tròn hướng trái. Ngón cái, ngón cong, lòng bàn tay/cổ tay và vị trí cẳng tay giữ cấu trúc nhìn thấy của I04; không thấy regression thành grip nắm đấm của I05. Mặt, silhouette, trang phục và full-body framing nhận diện được giữ lại. Đây là kiểm nhìn trực tiếp, không đo pixel hoặc chứng nhận mọi contact bị che.

**T1: OUTPUT_AVAILABLE / direction + visible-pose hypothesis supported.** Chưa PASS grip: điểm tựa que dưới và đường que bên trong tay vẫn không đọc đủ. Agent CONT-AP AP-MEDIA-02 được đăng ký trước dispatch ở VE04, đọc lạnh output rồi mới control/primary; report10 riêng, không đọc maker prompt/log/root QC. Chưa thêm lượt tạo khác.

Output metadata thực đọc bằng System.Drawing: 768×1376; đây là kích thước file, không khẳng định exact 9:16 mặc dù UI chọn9:16. Chưa là master/export TikTok spec.

CONT-AP đã hoàn tất [report10](../../agents/visual_experiments/10_cont-i06-static-review-v01.md): actual3JPEG, hướng/visible pose/recognizable identity MET; complete grip readiness BLOCKED, disposition HOLD do hidden contact/supports, không khẳng định xuyên da hoặc thiếu ngón. Root đọc và đồng ý phạm vi kết luận. Context đã từng xem I04 ở run trước nên đây không fresh-context blind evaluation, dù lượt này không nhận maker rationale và đã ghi observation I06 trước mở control/primary.

Gate: hướng tips phải; tay/cổ tay giữ cấu trúc I04; đúng hai que; không mất nhận diện. Hướng đúng riêng lẻ không đủ PASS grip. Tiếp xúc bị che UNKNOWN, chuyển động NOT_TESTED. F-NB-02 giữ UNRECONCILED, T2 HOLD.

## Tổng hợp vòng

Đã xác định: input upload đúng hình I04 trong asset riêng; T1 có output và đổi đúng hướng mà giữ cấu trúc tay thấy được; CONT review cùng xác nhận giới hạn này. Quyết định đã chốt: không ghi đè I05, không retry món, chỉ một T1; giữ I06 làm candidate/evidence, chưa promote output. Giả định đang dùng: visual comparison đủ nhận diện bản upload I04 nhưng không chứng minh exact byte/pixel equivalence. Còn mở: lower support/contact, F-NB-02 terminal outcome, motion. Bước tiếp theo đề xuất: probe close-view/contact có góc nhìn/reference cụ thể để đọc upper control và lower support; request phải chỉ rõ input I06, thay đổi visibility nào, tiêu chí và count trước submit; không lặp generic finger-repair T2. Không generate probe mới trong vòng này.
