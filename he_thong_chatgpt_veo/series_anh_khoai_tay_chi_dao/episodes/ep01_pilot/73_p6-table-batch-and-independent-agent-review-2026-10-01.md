# P6 — Loạt bàn ăn và agent review độc lập

Ngày 2026-10-01. Owner yêu cầu “làm cả 1 loạt đi, agent kiểm tra đâu rồi, sao không đề xuất”. Root nhận trách nhiệm các lượt F04/F05/T01 chỉ root QC, không gắn nhãn đã chạy independent agent. Vòng này: một request x3 cho ba candidate cùng brief, không ba thiết kế được nghiệm thu. Không ghép nhân vật, voice/video hoặc close P6.

## Generation register — TABLE-BATCH01

Input theo thứ tự: F05 (asset56d529b7-b789-4988-b83d-95b2a00ec347, approved texture) + ảnh mẹt đã duyệt68 (supports leaves, không món phụ). UI trước submit: Hình ảnh / Nano Banana Pro / 9:16 / x3 / 0 tín dụng. Submit một lần; ba tile0% cùng prompt. Không retry chưa đối soát. Giá UI không billing ledger. IDs T-NB-02A/B/C sẽ gắn theo tile khi download.

## Prompt chung thực chạy

```text
Create a vertical food-table concept for two adult friends sitting side by side along the same near long edge of a rectangular wooden table at a modest tidy Vietnamese sidewalk eatery at dusk. No people yet. Image 1 is the approved Nem Bui texture: preserve the irregular curved strips, small thin slices and fine golden-beige rice powder. Image 2 supports the accompanying fig leaves and dinh lang leafy sprigs only, not its other foods or tray. Use a wider elevated three-quarter camera view. The ENTIRE table surface and all essential objects must fit comfortably inside the image with generous margins on every side, not a food macro. Place one full off-white plate of Nem Bui near the middle, and one smaller plate of la sung and a little la dinh lang behind it. At the near edge place exactly two empty receiving bowls side by side, left and right, at equal distance from the camera for the two adjacent seated friends. Beside each receiving bowl put one small separate bowl of red chili dipping sauce and one pair of wooden chopsticks. Place exactly one clear unbranded glass of water outside the right-hand place setting. Leave an unobstructed space between each bowl and the central dish, enough for hands and bowl transfer later. Show two simple low stools at the same near side. Keep the dish texture natural, the accompanying leaves botanical rather than generic lettuce or mint. Simple blank shop wall, a plain warm lamp and blurred sidewalk in the background. Absolutely no menu boards, food posters, writing, signs, logos, landmarks, branded bottles, alcohol, extra food dishes, people or hands. Keep tableware fully uncropped. Believable natural food materials suitable for a tactile stylized 3D character scene later. Preserve the platform watermark.
```

## Agent dispatch register — trước media review

| Run | Role và input | Output | Status |
|---|---|---|---|
| FOOD-TABLE-BATCH01 | Food/leaf evidence reviewer; actual candidates cold trước references, primary research; không maker prompt/log/QC | agents/visual_experiments/13_food-table-batch-evidence-review-v01.md | COMPLETED; A/B/C REWORK |
| TABLE-BATCH01-STAGING | CONT; contracts Tier1+CONT+VE, candidate cold rồi script32/bộ phục vụ, không maker/report khác | agents/visual_experiments/14_food-table-batch-staging-review-v01.md | COMPLETED; static layout limited pass, action HOLD; watermark exception root below |
| TABLE-BATCH01-SELECTION | VEXP; PROD7+VE, media/log và hai reviewer reports sau độc lập | agents/visual_experiments/15_food-table-batch-selection-v01.md | COMPLETED; C proposed repair base, tests NOT_RUN |

Đây là nhiệm vụ agent contexts Codex, không runner/API/daemon mới. Reviewer không có quyền generate/upload/spend/Git. Root kiểm completeness và commit/push. Cùng nền mô hình vẫn có thiên kiến chung; không khán giả thật hoặc expert field certification.

## Kết quả

SUBMITTED_ONCE / THREE_OUTPUTS_DOWNLOADED / THREE_AGENT_REPORTS_COMPLETED / REWORK. Giữ reference/script/serving approval71–72. Cả ba JPEG768×1376 (UI9:16, file không đúng tỉ lệ toán học9:16), đã root actual view. Bản owner tại `C:\Users\PC\Downloads\du_an_nem_bui\`, bản project tại `media/raw/ep01_p6_food/`, filenames dưới đây.

| Candidate | File | Flow asset ID | SHA256 |
|---|---|---|---|
| A | T-NB-02A_v0.1.jpg | 3d9bd3f7-75be-4fd1-9184-4cf972f56c03 | 4AF26D3F4B39D3E0E5230DE9DC561349215B7DC05DE123B5958171447862004A |
| B | T-NB-02B_v0.1.jpg | cad84335-9edf-4d14-b177-001d2483660d | 0BE6242BA0233F179B157B7BA7FD2F83E2F4DC92FABD5431B60D0F186F634E85 |
| C | T-NB-02C_v0.1.jpg | 55cc8bc8-fecf-4183-a506-f05fc62c940c | 1C9B0128CA397F984E5081566C93751A878E5FB55F9809B794E435D44D92223F |

Editor download gốc lần lượt `b023b97f-d14f-4678-ac74-4ac46d736126.jpg`, `c53b2a7a-6236-4ca7-a274-91330d861e55.jpg`, `4be6c248-57aa-439d-aac7-6a858475a471.jpg` trong Downloads. Proof mỗi candidate `T-NB-02A_flow-proof.png`/B/C cùng project media folder, lưu screenshot actual editor. Không overwrite T01/F05 hoặc reference.

## Đối soát review và root disposition

Food reviewer13 và CONT14 đã hoàn tất actual media review trong contexts riêng. Food xem A/B/C cold rồi ba reference; CONT xem A/B/C cold rồi script32, không maker prompt hoặc food report. Không gọi các context cùng nền mô hình là expert xác thực ngoài đời.

- A/B/C: REWORK về food/leaf fidelity. Cả ba lá bản rộng có thùy sâu, trái silhouette lá sung không thùy trong ảnh được duyệt và nguồn VNUF; không chứng nhận loài của lá AI. Sprigs đinh lăng UNKNOWN. Sợi nem quá thiên về dây tròn dày so với dải/lát mỏng đa dạng của F05 và ảnh thật.
- Static count/layout: đủ đĩa món, đĩa lá, hai bát, hai chén chấm, hai đôi đũa, một cốc ngoài phải. Đây không phải chứng minh reach hoặc chuỗi gắp/đổi hướng/nhận bát; cần composite rồi action states/video.
- Root correction TST-01: dấu sao nền tảng đã được brief yêu cầu giữ. Cold observation đúng, nhưng yêu cầu clean/remove bị rút khi cấp exception; không xóa/crop watermark, không gộp watermark với nhãn hàng bị cấm.
- UI9:16 không bảo đảm tỉ lệ pixel actual; khâu bàn giao dọc cần xử lý canvas riêng mà không crop mất props.

Đã xác định: batch đã có ba output và independent findings. Quyết định đã chốt: không đổi F05/primary/script; không promote A/B/C thành approved reference. Giả định: hai ghế cạnh gần intended cho hai bạn, vẫn cần kiểm khi ghép. Còn mở: sửa lá/texture, chọn layout cuối, placement và action. Bước tiếp theo: VEXP chọn base sửa và test cô lập; chỉ candidate đạt re-review mới trình owner duyệt reference.

## Quy trình batch đề xuất dùng tiếp

Maker đăng ký brief/input/version và chạy batch → Food/Source + CONT review actual pixels độc lập → VEXP tổng hợp defect/đề xuất test → root đối soát ngoại lệ/closure → owner duyệt asset ở gate. Không bắt owner duyệt mỗi mẫu lỗi; không gán maker tự kiểm là independent review. Vòng này là ba sampling variations cùng prompt, chưa phải ba thử nghiệm một-yếu-tố.

VEXP15 final được root đọc đầy đủ: đề xuất C làm base sửa, A dự phòng; B thêm kê đũa tạo dependency. Root đồng ý đây là đề xuất hợp lý về base, không owner selection hoặc chứng minh appeal. Hai test tuần tự NOT_RUN: L01 chỉ sửa hình thái/binding lá bằng reference đã được phép; F01 chỉ sửa geometry nem sau khi revision lá dùng được. Giữ bố cục/count/light/watermark, re-review actual output và kiểm regression. Không gọi test proposal là đã triển khai.
