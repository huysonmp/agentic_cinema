# T2 idle-performance — vòng thử có kiểm soát

Ghi chú biên tập ngày 2026-10-02: phần dưới là nhật ký kỹ thuật của các lượt đã chạy. Giữ nguyên prompt tiếng Anh, mã clip, hash, số liệu và các trạng thái tại thời điểm ghi để truy xuất. Phần diễn giải tiếng Việt đã được biên tập tại tài liệu 120; quyết định Quality hiện hành ở tài liệu 122. Không coi nhật ký này là bản văn trình duyệt đã biên tập toàn bộ.

## Trạng thái cuối vòng — 2026-10-02

**10/10 lượt đã tạo, tải và lưu. Không có production PASS. Dừng phát sinh lượt mới.** Kết quả/đề xuất dễ đọc tại [120 — gói kết quả để owner xem](120_t2-idle-round-results-and-next-decision.md). Các dòng REGISTERED/pending bên dưới là nhật ký thời điểm, được thay thế bởi OUTPUT_SAVED tương ứng.

Số dư UI trước vòng1.020 (118), sau vòng920 (119_BALANCE_FINAL.jpg): observed delta100, phù hợp10 lượt quote10. Tổng từ mốc1.050 trướcV01 tới920 là130/200credit; không đổi cap tổng. Đây là đối soát số dư UI, không phải sao kê billing từng giao dịch. Không dùng reserveV02, không nâng Quality.

Root đã xem16 ảnh mẫu/clip (~0.25→7.75s) và full technical decode. Chưa nghe đầy đủ audio, chưa full audiovisual hoặc independent review; không gán agent PASS. R01 giữ tay tốt trong mẫu nhưng thêm mist/steam; R02–R10 có cử chỉ tự phát hoặc mở miệng. Tất cả OVERALL_REWORK. P6/P7 OPEN, không đổi script/canon/recipe approval.

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

R03 OUTPUT_SAVED asset `3e3c5f62-51f6-4469-9a0e-b30f3cb9ebf6`,native `Two_adults_posing_at_table_20261002072511.mp4`3.605.373bytes,projectR03.mp4/owner119_R03.mp4; SHA256 `804AD677BB154F1D268A634B8D23AA32DE760D62DCCBAE828158E819901328C6`. Decode clean,720×1280/24fps/8s/audio stream. Root16samples: Khoai lifts both hands approx0.75s, a hand1.25s; nhiều blink/Đào eyeline-face state changes. Table/framing toàn samples giữ được, steam không thấy. **REWORK gesture**, không kết luận model không thể idle. Screenshot119_R03_RESULT.jpg.

## R04 — endpoint constraint, registered

Giữ exact prompt R03, đổi riêng END từblank thành chính OPEN7 (START=END), để kiểm biên đầu/cuối có giảm spontaneousgesture. Không ảnh endpoint mới, không production canon; không ép endpoint giả cho camera tilt. Chỉ submit nếu vẫn Lite/frames9:16/720p8s/x1 quote10; nếu route/model/giá đổi HOLD. Planned cumulative40/100,đãsubmit3. Chưa chạy.

R04 SUBMITTED sau actual UI vẫnLite/frames9:16/720p8s/x1/quote10, hai thumbnail cùngOPEN7; click một lần, composer reset.119_R04_PRE.jpg. UI balance afterR04submit980 so baseline118=1.020: observed delta40 phù hợp4quotes10. R04 output còn pending; không coi debit=output. Screenshot119_BALANCE_AFTER_R04.jpg local-only accountpanel. P6 trial total balance-delta từmốc1.050 trướcV01 tới980=70, cap200 không bị vượt; không thay billing audit.

R04 OUTPUT_SAVED asset `ea550b0a-495a-40ff-8c5c-4aefd0a71e9f`,native `Adults_posing_at_wooden_table_20261002073036.mp4`1.942.524bytes,projectR04.mp4/owner119_R04.mp4, SHA256 `6EC24F488A5E7C5BBD1B778F0FDCCA89984645B41CCD0BFB3DA4E4C44EA70AE8`. Decode clean/720×1280/24fps/8s/audio stream. Root16samples: Đào opens mouth and lifts bothhands ~1.25–2.75s, Khoai mouthopens~4.75–5.75s. Composition/meal preserved samples. **REWORK**, START=END không đủ khóa chuyển động giữa clip.119_R04_RESULT.jpg.

## R05 — cinemagraph only-eyelids, registered

Giữ START=END OPEN7, cùng config/quoteexpected10; đổi prompt. Exact:

Create an eight-second locked-off cinemagraph from the supplied image. Animate ONLY the eyelids of the two foreground figures, with one gentle blink. Their lips are sealed in the original closed-mouth smile. Their heads, shoulders, arms, wrists and all four hands are held in the original pose for all eight seconds. The entire tabletop, food, herbs, bowls, sauces, chopsticks and glass are a static still-life layer. Keep the camera, framing, scale, lighting and background fixed. Every object retains its exact original position and size. Clear still air above the table. Silent audio. Preserve the native video watermark.

Chỉ là behavior-control diagnostic, không yêu cầu production clip trở thành cinemagraph. Registerednot submitted; cumulative planned50/100.

R05 SUBMITTED: actualquote10/Lite/frames9:16/720p8s/x1; START=END OPEN7;exactpromptread-back/clickonce/composerreset;119_R05_PRE.jpg. Output pending.

R05 OUTPUT_SAVED asset `2d9e5320-1373-459a-8121-6ef690dbee33`,native `Animate_eyelids_of_two_figures_20261002073653.mp4`1.854.027bytes,projectR05.mp4/owner119_R05.mp4;SHA256 `9F7F6EC007DBA1AE19CC6902FB0E409A190E0AC6C9B3A6969C9066125253DF1B`. Decode clean/720×1280/24fps/8s/audio stream. Root16samples: both handgestures ~0.75–1.25s,Khoai many later gestures, prolonged eyesclosedstates/miệnghá. Table/framing samples preserved. **REWORK**.119_R05_RESULT.jpg.

## Research checkpoint và R06 — motion-only minimal, registered

Google official image-to-video bestpractice đọc2026-10-02: [nguồn](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/best-practice),sectionsPrompt for motion only/Use general terms/Direct camera. Ảnh đã mang character/scene/style, nên prompt chuyển động và tránh mô tả lại. Đây là hướng dẫn GoogleCloud/AgentPlatform, không bảo đảm FlowLite hay controlendpoint; không dùng API negativePrompt giả trong UI. Suy luận cầntest: giảm dư thừa prompt có thể giúp idlecontrol; chưa causalconclusion.

R06: START=END OPEN7 nhưR05, cùngLite/frames9:16/720p8s/x1/expected10, đổi exactprompt:

Locked camera. The subjects hold their exact starting pose for eight seconds, with closed lips and hands resting on the table. Only their eyelids blink gently once. All other scene elements remain still. Silent audio. Preserve the native video watermark.

Plannedcumulative60/100. Chưa submit.

R06 SUBMITTED actualquote10/Lite/frames9:16/720p8s/x1;START=END OPEN7/clickonce/read-back;119_R06_PRE.jpg. Chưa output/delta mới.

R06 OUTPUT_SAVED asset `696aad7c-538b-48dd-a99a-8ca1caa7dcbf`,native `Subjects_holding_pose_at_table_20261002074248.mp4`1.915.584bytes,projectR06.mp4/owner119_R06.mp4;SHA256 `640261F75A723977CA4A4A9B0A7F8ECEFC02E7EA5A7107D843990FDF19E97580`. Decode clean/720×1280/24fps/8s/audio stream. Root16samples: Đào moves ahand~0.75–1.25s,then later hands settled;mouth/head turns early;table/framing preserved. **REWORK**, partial idle usable-looking segment khôngwhole8sPASS.119_R06_RESULT.jpg.

## R07 — motion-only endpoint ablation, registered

Giữ exactpromptR06, STARTOPEN7 nhưngENDblank để so paired vs single reference cùngprompt. Configquoteexpected10/Lite/frames9:16/720p8s/x1 unchanged, cumulativeplanned70/100. Chưa submit. Không mượn frame extracted của failedclip làm canon.

R07 SUBMITTED sau actual read-back cùngconfig/quote10; STARTOPEN7/ENDblank; clickonce/composerreset;119_R07_PRE.jpg. Chưa output/delta.

R07 OUTPUT_SAVED asset `68c8e875-5b3e-4572-8ec5-000a0ab54138`,native `Subjects_holding_starting_pose_20261002074912.mp4`2.213.088bytes,projectR07.mp4/owner119_R07.mp4;SHA256 `7CBCF43DDD3A18CAD03C6479CC69C34C7625D7405687A1E0A537E6B1247BBDDE`. Decode clean/720×1280/24fps/8s/audio stream. Root16samples: bothgestures~0.75–1.25s,Khoai late~7.75s,mouthopen. Frame/meal samples intact. **REWORK**, single-start khôngkhóaidle vớiD.119_R07_RESULT.jpg.

## R08 — zero-motion control, registered

STARTOPEN7/ENDblank,cùngLite/frames9:16/720p8s/x1/expected10;prompt chỉfreezehold, bỏ cảblink để phân biệt blinkinstruction vs mặcđịnh motion. Khônglà production direction. Exact:

An eight-second static freeze-frame hold of the supplied image. The entire image remains completely motionless and unchanged throughout: subjects, faces, mouths, hands, objects and background. Fixed camera and identical composition from beginning to end. Silent audio. Preserve the native video watermark.

Plannedround80/100, chưa submit.

R08 SUBMITTED actualread-back10/Lite/frames9:16/720p8s/x1;STARTOPEN7/ENDblank/clickonce/composerreset;119_R08_PRE.jpg. Output pending. Round8submitted7saved, no production winner.

R08 OUTPUT_SAVED asset `c678e028-3e9e-40cb-af5f-75f41ed20f25`,native `Video_freeze_frame_hold_20261002075540.mp4`2.364.694bytes,projectR08.mp4/owner119_R08.mp4;SHA256 `70CD9D0C4C15CE336CBFB08E82A7BB55DEA3983A8CF12FE4FA04270CA255301B`. Decode clean/720×1280/24fps/8s/audio stream. Root16samples: hai nhân vật vẫn gestures/headturn/mouthmovement đầu,giữa,cuối;table/framing preserved. **REWORK**, zero-motiontext không đủ khóa trong lượt này. Không suy API/modelQuality khác cũngfail.119_R08_RESULT.jpg.

## R09 — zero-motion with endpoint, registered

Giữ exactpromptR08, đổi ENDblank→OPEN7,STARTOPEN7; cùngLite/frames9:16/720p8s/x1/expected10. Cumulativeplanned90/100. Xác nhận zero-motion failure có/không endpoint cùngprompt, chưa submit.

R09 SUBMITTED actualsameconfig/quote10/read-back;START=ENDOPEN7/clickonce/composerreset;119_R09_PRE.jpg. Output pending.

R09 OUTPUT_SAVED asset `11a4332e-4ec8-4343-8ba3-bd704716054d`, native `Static_video_freeze_frame_hold_20261002080241.mp4`, 1.917.237 bytes; project R09.mp4 / owner119_R09.mp4. SHA256 `F0F855E9B4D0147BA19BFC8F1D643C77DED2792CA338D8D93427FE7650121BCC`. Decode clean / 720×1280 / 24fps / 8s / audio stream. Root16samples: Khoai lifts a hand around1.25s and opens mouth in multiple samples; meal/framing preserved. **REWORK**, paired endpoints do not freeze intermediate motion in this trial.119_R09_RESULT.jpg.

## R10 — exact repeat A, registered

Repeat the exact prompt A recorded for R01/R02, START OPEN7 / END blank. Same Lite / Frames / 9:16 / 720p / 8s / x1, submit only if actual quote remains10. This is the third sample of A, not a revised prompt or steam fix. Planned round100/100, final authorized trial; no eleventh generation. Not submitted yet.

R10 SUBMITTED: actual UI read-back Video / Frames / 9:16 / 720p / 8s / x1, quote10, START OPEN7 / END blank; exact A; single generate click followed by composer reset. Screenshot119_R10_PRE.jpg. Output pending, ten submissions reached: stop generation.

R10 OUTPUT_SAVED asset `61a72a51-acbd-4830-8060-4b2688a504a9`, native `Potato_and_peach_characters_waiting_20261002080950.mp4`, 3.367.605bytes; projectR10.mp4 / owner119_R10.mp4. SHA256 `C0AECD878B7F1B761954ECABC22CB3EE35BD8315108FB12B82BD8DC3AD2207DA`. Full decode clean,720×1280/24fps/8s/audio stream. Root16samples: Khoai lifts both hands around0.75–3.25s; mouths/head directions change; table/framing mostly preserved. **REWORK**, A now three samples, no repeatable whole-shot success.119_R10_RESULT.jpg. Audio UNKNOWN.

Final UI balance920 verified in accountpanel, screenshot119_BALANCE_FINAL.jpg saved local only. No eleventh generation, Quality, Extend, upload, voice change, canon change or production selection in this round. Outputs and screenshots local/gitignored; manifest and review documents version-controlled.
