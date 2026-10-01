# T2-CAM-01 v0.1 — Thử món→mắt Khoai

2026-10-01. Root / P7–P8 PAPER_REQUEST. DRAFT / INPUT_BLOCKED / NOT_SUBMITTED. Authority100 chỉ chuẩn bị; không execution/spend. Đây thử camera, không production take hoặc thử hấp dẫn cả tập.

## Câu hỏi thử duy nhất

Một chuyển hướng máy nhẹ có dẫn chú ý từ bữa ăn lên mắt Khoai, vẫn giữ Đào và toàn bộ phục vụ, mà không biến dạng/đổi identity/geography? Đây camera tilt, không nhân vật đổi chỗ, POV đối diện hoặc đổi trục. Hai still tốt không trả lời được câu hỏi motion.

## Request envelope

| Trường | Giá trị / trạng thái |
|---|---|
| Inputs | T2-R-OPEN-v0.1 / T2-R-END-v0.1 theo101; PLANNED_NOT_CREATED, chưa IDs/hash/approval actual |
| Mode dự kiến | Frames start/end; Veo Lite, vertical9:16, x1; chỉ proposal, phải verify khả dụng trên UI |
| Duration dự kiến | 4s native diagnostic, không thời lượng đo S01 hoặc30s tập; account support UNKNOWN |
| Số lượt đề xuất | 1 clip đầu; không tự retry, không Extend, không Quality upgrade |
| Price/cap | UNKNOWN; không reuse10credit V02; exact spend cần UI read-back và owner approval trước submit |
| Voice/music | Không thoại, hát, VO hoặc nhạc; không thử giọng Khoai/Đào. Model có thể sinh âm ngoài ý muốn: ghi nhận và reject theo scope, không hứa mute/stems riêng. |
| State | Hai người/tay nghỉ, cốc/đũa trên bàn, nem nguyên; không hành động món hoặc mouth performance |
| Cues | Không burn-in F01/F02/nhãn/tên mới; tách khỏi thử motion. Nhãn AI vẫn bắt buộc bản bàn giao/phát hành, không xóa watermark native. Probe gắn nhãn AI trong manifest và owner review. |
| Account/project | Flow project9276788e-9781-44fb-ba5b-083006667374 trong hồ sơ; login/current model/control/giá chưa kiểm vòng này |

Không nhập duration/mode từ API documentation vào UI. Nếu 4s/start-end/Lite không hiện: HOLD, read-back options và trình sửa request; không âm thầm đổi model/count/duration. Unknown giá không bằng miễn phí.

## Exact prompt dự thảo

> A vertical diagnostic camera shot between the supplied approved start and end frames. The two adult stylized characters sit at the same side of a small tidy street-side eatery table: potato man screen left, peach woman screen right. Start with visual attention on the complete Nem Bui meal in the lower centre. Make one small, smooth upward camera tilt toward the potato character's eyes and settle at the supplied end composition. No push-in, orbit, axis reversal, rack-focus blur, cuts or shaking. Keep both faces and the entire meal with the same herbs, dipping dishes, two bowls, resting chopsticks and water glass visible throughout. Preserve identity, clothing, food quantity, hand positions, object placement, warm lighting and provenance. Both characters remain quietly seated with natural minimal breathing only; no gestures, plate pulling, utensil use, eating, drinking or speaking. No dialogue, voice-over, singing, music, added writing, names or signs. Do not remove source or native watermarks. This tests camera movement only, not the scene's acting or voice.

## Trình tự và điều kiện dừng

1. Hai ảnh thực được reviewer kiểm và owner chọn; lưu bytes/hash, không chỉ link thumbnail. Mismatch đầu/cuối phải sửa ảnh trước, không trông chờ video chữa.
2. Kiểm account UI route/settings/price, source usage provenance và exact inputs đã gắn. Ghi snapshot trước submit; owner approve request/count/spend riêng.
3. Khi được phép mới submit một lần; lưu actual prompt/settings/jobID/giá báo trước/balance nếu có, file và hash. Không tự báo completed trước output thực.
4. Review full playback và đầu/giữa/cuối, thêm frame tại lỗi; ghi khả năng nghe thực. Nếu không xem được playback, motion UNKNOWN, không lấy vài still thay pass.
5. Fail một criterion chính hoặc cần đổi prompt/reference: HOLD, lưu defect và đề xuất bounded revision để duyệt, không retry tự động.

## Rubric và handoff

| Check | Evidence phải có / fail |
|---|---|
| CAM-1 Attention | Full playback: món mở và mắt Khoai cuối đọc được; không food→face bằng cut/zoom thay tilt. Reviewer mô tả điểm chú ý trước đọc intent; đây phản biện AI, không audience test. |
| CAM-2 Composition | Cả hai mặt, toàn đĩa nem, lá/chấm/bát/đũa/cốc thấy suốt; không out-of-frame hoặc rack focus che món. |
| CAM-3 Continuity | No axis/face/wardrobe/food-quantity/object-position change, tay không tự hành động; actual start/end matching. |
| CAM-4 Craft | Không warp/flicker/giật máy; ấm và mắt/món phân biệt, không suy CCT/lens thật từ prompt. |
| CAM-5 Isolation | Không transfer/cốc nhấc/mouth acting/thoại/tên mới; audio capability nếu không nghe được ghi UNKNOWN. Watermark không xóa. |

Reviewer CINE-LIGHT kiểm camera/light; route identity/props findings sang CONT, actual semantics sang PERF và audio sang AV nếu cần. Gói giấy không thay independent media review. Không gọi tất cả agent đã chạy chỉ vì rubric ghi role.

Khi probe đạt và owner chọn: tiếp tục action-specific S01/S02 refs và thử diễn/voice có kiểm soát; motion pass không đủ handoff S04/A hoặc final generation. Nếu không đạt, báo chính xác lỗi trước đề xuất kỹ thuật mới; không thu hẹp sáng tạo chỉ vì chưa test.

Đã xác định câu hỏi/controls; đã chốt camera intent100; giả định small tilt giữa approved frames khả thi; còn mở refs/account/price/request approval/media; tiếp theo paper review, owner xem gói, chưa chạy.
