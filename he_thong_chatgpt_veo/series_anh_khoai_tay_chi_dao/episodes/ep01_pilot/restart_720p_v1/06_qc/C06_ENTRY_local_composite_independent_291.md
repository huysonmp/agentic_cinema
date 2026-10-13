# REC291 — Review độc lập STILL composite entry C06 v3

Ngày 13-10-2026. Reviewer `food_repair_critic_283`, bounded local REC217. **ACTUAL_FULL_STILL + READ_ONLY_DECODED_RGB_CHECK / FOR_OWNER_STILL_REVIEW / NOT_VIDEO.** Owner đã cho local composite food-only, giữ pixel ngoài vùng sửa; approval v3 còn pending. Không browser/generation/paid/git hoặc sửa media. Chỉ viết báo cáo này.

## 1. Kết luận

**V3 đủ trình owner xem đúng phạm vi ảnh entry.** Khác redraw290, mặt/trang phục/bối cảnh/props ngoài mask được giữ bằng pixel nguồn; dấu sao nguồn còn. Món và A đã chuyển sang dạng thịt/bì/thính, phần A nhỏ hơn donor290 và ở đúng tips/phase đầu C06. Không thấy MAJOR mới buộc bác whole still. Có caveat mép/nền vá của A ở crop phóng lớn cần nêu rõ; không dùng outside-mask0 thay thẩm định món/seam hoặc bảo toàn mọi pixel ngoài food về mặt ngữ nghĩa.

Chưa owner-approved, chưa binding/upload ready từ báo cáo này. Không ACT B, motion, voice, sync, hai clip nối hoặc whole-film PASS.

## 2. Artifact đã đọc/xem

Đọc đầy đủ `04_requests/C06_ENTRY_local_composite_v3_291.json` và `C:/Users/PC/Downloads/du_an_nem_bui/291_C06_LOCAL_COMPOSITE/v3/PIXEL_QC.json`. Trực tiếp xem toàn v3, `EDIT_MASK.png`, crop `held_composite_detail.png`, `plate_composite_detail.png`, và `SOURCE_LEFT_COMPOSITE_RIGHT_QC.png`. Source269 và donor290 đã trực tiếp xem full trong review290; không dựa riêng tên prompt.

- Base `02_refs/C06_START_from_C05_T02_selected_F65_269.png`: SHA `f091e35fc7c779591c918c47ba34752a8a2c3b30de507cd99dc0e76143e83196`.
- Donor `02_refs/C06_ENTRY_food_v1_CHATGPT_FOR_REVIEW_290.png`: SHA `40be91b97b873979f09f01d1e530cd9512674dd2b26b1fc339237b0f23f37077`; chỉ vùng món, không mặt/thân/background làm canon.
- Target `C:/Users/PC/Downloads/du_an_nem_bui/291_C06_LOCAL_COMPOSITE/v3/C06_ENTRY_LOCAL_v3_FOR_REVIEW_291.png`: SHA **`7c8023cbe655745b941e1a47dd1df3614ba66fcef512a41c5c4c4048bb33f8cc`**,720×1280.
- Mask SHA **`286f34063e546bc1151a8d4a0ed376191c6bffbf491809c8bb1d843d403118fa`**.
- Config SHA `a64501e0543109d66386e4015023ab5bb85593349bf887444371229b9217b4a8` theo QC/đối soát config hiện hành.

File tương đối tính từ `restart_720p_v1`. Không đọc hoặc cấp scope cho v1/v2; chỉ v3 exact hash.

## 3. Numerical check độc lập thực chạy

System Python không có Pillow; không cài thêm. Dùng runtime Pillow bundled đã có để **chỉ đọc** base/output/mask và recompute RGB differences, không tạo/chỉnh ảnh hoặc script file:

- Base/output/mask cùng720×1280.
- `outside_mask_changed_pixels = 0`.
- `inside_changed_pixels = 36890`.
- `nonzero_mask_pixels = 36892`.
- Nonzero mask bbox `[203,736,550,1084]`, gồm hai vùng rời tại A và đĩa, **không toàn hình chữ nhật bbox**.
- Output/mask hash recompute khớp PIXEL_QC.

So sánh đếm pixel RGB khác ở nơi mask=0/khác0, không lấy độ sáng trung bình để làm mất khác biệt một kênh. Đây xác nhận **ngoài saved mask** giữ exact decoded RGB; không chứng minh saved mask là semantic segmentation thuần food. Mask gồm silhouette/shadow cũ, biên blend và vùng áo lộ ra phải phục hồi; toàn pixel áo nằm trong mask không được gọi là giữ tuyệt đối.

## 4. Findings actual visual

| Scope | Quan sát và disposition |
| --- | --- |
| **Plate** | Thịt nâu hồng, bì rời và thính giống hướng hai ảnh thật đã duyệt hơn slabs cũ; không nhập món khác/khói. Plate rim còn từ source; crop có biên chuyển khá liền, không thấy miếng cũ đặc lộ lớn. Độ sắc/texture món khác ảnh nguồn và có màu ấm hơn, chưa recipe hoặc owner FOOD approval. |
| **Held A/amount** | Nhúm nhỏ tập trung ở cùng tips; không dangling serving lớn như donor290. Tại full frame đọc là một phần nhỏ đang cầm, chưa sang miệng/thả hoặc nhận. Không chứng minh lượng vật lý/mass bằng pixel; shape và vật liệu được thay là chủ đích. |
| **A seam/background** | Crop phóng lớn thấy vùng nền áo phục hồi có chuyển sắc khá phẳng theo vùng vá dưới/trái A; mép thính có cạnh hơi cứng hơn source mờ. Ở full720 chưa thấy ghost slab lớn hoặc MAJOR viền bật; giữ **MINOR/CAVEAT** để owner xem ở kích thước thật, không tuyên bố patch vô hình. |
| **Chopsticks/contact** | Hai thanh vẫn liên tục đến vùng nhúm; phần protected polygons được cấu hình phục hồi từ nguồn. Crop không thấy đôi đũa mới/đứt hoặc đầu thanh tách rõ khỏi A. Contact physics/grip trên chuyển động chưa kiểm; numerical zero ngoài mask không chấm mọi vùng tip trong mask. |
| **Face/props/source continuity** | Mặt và trạng thái môi khép/gaze nguồn giữ, blouse Đào trắng, Khoai vest tối; hai bát rỗng/cốc nâng tay ngoài và ngoài bát, tay rảnh chưa nhận. So source-left/v3-right không thấy đổi bố cục/ánh sáng/background như290/286. Pixel ngoài mask0 củng cố các vùng đó, không actual seam video hoặc diễn B. |
| **Provenance mark** | Dấu sao Flow ở đáy phải được giữ từ base, ngoài mask; source không bị chỉnh. V3 là **local composite từ native frame + donor ChatGPT**, không native Flow output mới, không video đã sửa. Không watermark removal hoặc watermark giả. |

## 5. Gate và bước tiếp

Owner cần chốt **exact v3 entry still, món/nhúm và mức chấp nhận seam**; source approval269/276 hay approval donor không tự truyền. Nếu v3 được chốt, chỉ đóng input still scope, không hứa Ingredients khóa F0 hoặc sinh giữ pixel đó.

Root giữ source/donor/config/mask/hash/phiên bản để truy. C05 còn món cũ là dependency riêng; thay entry C06 không sửa C05 hoặc tự nghiệm thu toàn chuỗi. Gói C06 ACT B tiếp theo phải kiểm source role, voice/config/quote live và xin quyền request; không tự paid hoặc EDL edit từ report.

**FINAL: OUTSIDE_SAVED_MASK_RGB_EXACT_RECOMPUTED / V3_STILL_REVIEWABLE_WITH_MINOR_A_SEAM_CAVEAT / OWNER_APPROVAL_PENDING / NO_MEDIA_PERFORMANCE_OR_PAID_GO.**
