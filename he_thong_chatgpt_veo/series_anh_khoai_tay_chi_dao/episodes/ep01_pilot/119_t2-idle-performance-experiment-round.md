# T2 idle-performance — vòng thử có kiểm soát

2026-10-02. Owner “cứ thử đi, tầm10lần cũngdc”: cho thử tối đa10 lượt Lite mới, dự trù quote10/lượt → cap100credit cho vòng119. Thay trần dưới50 của vòng camera trước trong phạm vi này, không nâng Quality/Extend/API/voice. Không thay script32/identity canon/recipe approval. START OPEN7 cùng SHA116/118, END trống,9:16/720p/8s/x1; read-back quote/model trước mỗi submit. Nếu giá>10 hoặc scope khác HOLD. Cumulative trial cap200 theo41 không bị xóa; vòng này không tự cho phép vượt cap tổng.

Outcome: tìm prompt giữ idle performance (tay/miệng) và whole-serving, rồi thử camera nếu idle đạt. Tối đa10 không là phải dùng hết; dừng sớm nếu có candidate lặp lại hoặc thử tiếp không tạo thêm bằng chứng hữu ích. Mỗi condition stochastic, không fixed seed: không kết luận causal proof hoặc mọi clip Lite/Quality sẽ như vậy.

QC: full technical decode + root bounded samples ghi mốc; không giả đã nghe/ASR/full audiovisual/independent review. Nếu mẫu phát hiện gesture/margin defect thì REWORK đủ bằng chứng. Mẫu không lỗi chỉ SAMPLE_CANDIDATE, chưa production PASS. File/hash/settings/prompt/UIbalance ghi actual liên tục, media local gitignored. Không tự chọn production winner.

## R01 — positive idle, registered before submit

Giữ camera tĩnh; rút gọn nhiều phủ định, mô tả vị trí và hành vi tích cực. Đây là thay một nhóm prompt, không isolated từng từ. Plan10credit, balance last observed1.020 (118), current reconcile sau actual.

Exact prompt:

Animate this reference image as a quiet eight-second waiting moment. The adult potato man on the left and adult peach woman on the right sit peacefully, looking down at the shared meal with their lips gently closed. Each character keeps both hands resting in exactly their original positions on the tabletop throughout the entire eight seconds. Only subtle breathing and a single gentle blink bring them to life. Their shoulders, elbows and wrists remain settled. This is a silent pause, not a conversation. A locked-off tripod camera holds exactly the starting composition and scale for the whole shot. Keep both full faces, the entire Nem Bui plate, herb plate, both sauce bowls, both eating bowls, chopsticks and water glass inside the frame with the original margins. Preserve the reference identities, clothing, table layout, food appearance and warm street-side lighting. Quiet background street ambience only. No speech or music. Keep the native video watermark intact.

Status REGISTERED_NOT_SUBMITTED. Actual updates below.

R01 SUBMITTED: actual UI quote10/Lite/frames9:16/720p8s/x1, START OPEN7/ENDblank; prompt read-back đúng. Click generate đúng một lần, composer reset/newtile. Evidence `119_R01_PRE.jpg` owner folder. Chưa costdelta/output/PASS.

R01 OUTPUT_SAVED: asset `3ad6e97f-56aa-4ee8-b575-5b8fa89ee45b`,native Downloads `Characters_sitting_quietly_at_table_20261002071915.mp4`3.182.913bytes, project `media/raw/ep01_t2_idle119/R01.mp4`,owner119_R01.mp4. SHA256 `1E829FD8CB8031844C8A1D35260D91D2D638EB8AF0A21C3D5C99C27A04F6F463`. ffprobe720×1280/24fps/8s/audio stream, full decode clean. Root xem contact sheet16sample ởfps2 (xấp xỉ0.25→7.75s, không fullplayback). Hands/whole-serving/frame scale ổn trong samples, blink nhiều hơn một, miệng không thấy há như gesturecontrol; thêm steam/mist phía bàn khoảng1.75→3.75s → IDLE_SAMPLE_CANDIDATE / OVERALL_REWORK do hiệu ứng không có trong reference. Audio UNKNOWN. Evidence119_R01_RESULT.jpg, không production PASS.

## R02 — repeatability control, registered

Exact prompt giống R01 toàn bộ (không sửa), cùng START OPEN7/ENDblank/Lite/frames9:16/720p8s/x1, expected10. Kiểm lặp lại idle và steam trước thay prompt. Không submit cho đến actual quote check; cộng round planned20/100credit. Chưa output/costdelta.

R02 actual submit một lần sau quote10/settings read-back nhưR01. OUTPUT_SAVED asset `4302166e-2e64-42e7-bf65-96a6cbc44a73`,native `Potato_and_peach_characters_sitting_20261002072204.mp4`,3.616.057bytes;projectR02.mp4/owner119_R02.mp4, SHA256 `46E303CBE8F2C073B3CA73EC815E700A53DF61AB9769AD6A5107FF7AEED0F71B`. Decode clean,720×1280/24fps/8s/audio stream. Root16sample: Khoai gestures approx1.25–2.25/7.75s,miệng há; đĩa rau giảm/di chuyển và món dịch chuyển. **REWORK, R01 idle improvement không repeatable n=2**. Steam không rõ nhưR01, không generalize. Screenshot119_R02_PRE/RESULT.jpg. Audio UNKNOWN,actual delta chưa read-back riêng.

## R03 — living portrait / minimal prompt, registered

Plan Lite10 như trước, chỉ đổi promptgroup, START OPEN7/ENDblank. Exact prompt:

A living photograph of the supplied reference, held for eight seconds. Both adult characters retain exactly their initial pose and initial gaze. Their four hands stay planted in the same spots on the wooden tabletop. Their lips stay completely closed and their shoulders, arms and wrists remain motionless. The only character animation is one slow natural blink. Locked tripod camera: the composition, perspective, scale and image borders stay fixed. Every plate, leaf, sauce bowl, eating bowl, chopstick and water glass stays exactly as photographed, with all original margins intact. Maintain the original faces, clothing, food quantity, background and warm light. The air above the food is clear and still. Silent soundtrack. Preserve the native video watermark.

Chưa submit tại đăng ký. Giữ source/current mouthpose tốt hơn instruction nhìn xuống; body heldpose chặt hơn, không suy sẽ thành công trước thử.

R03 SUBMITTED actual10/Lite/frames9:16/720p8s/x1, START OPEN7/ENDblank; click một lần sau exactprompt/read-back;119_R03_PRE.jpg. Chưa output/costdelta. Current round3 submitted/2saved; quotes30credit, actual balance phải đối soát.
