# C02 — Review ảnh tham chiếu cận vừa độc lập, REC244

Run **C02-MEDIUM-REF-CRITIC-244**, ngày07/10/2026. Mode **COLD_STATIC_REFERENCE_COMPARISON_THEN_REQUEST_CHECK**. **Disposition: PASS_FOR_HANDOFF_STATIC / NOT_VIDEO_PASS.** Không thấy MAJOR trong phần ảnh tĩnh được xem; đây là reference riêng của shot, không master thay thế hoặc quyền chạy lại.

## Input và phạm vi

Cold xem toàn actual approved masterv5 rồi toàn ảnh cận mới, so identity/framing/background/F0 trước đọc prompt và rationale. Sau đó đọc đầy đủ `02_refs/C02_medium_reference_244.txt`, promptC02/242, reportnative243, quyết định audio244 và registry244. Contracts PROD7/02, DIRECT01,217/236/238 và masterapproval242 đã đọc đầy đủ ở các run trước, giữ cùng giới hạn reviewer local. Không coi tên role hoặc lời prompt là evidence ảnh đạt.

Hash tính lại bằng PowerShell:

| Ảnh | SHA256 |
| --- | --- |
| `MASTER01_v5_CHATGPT_NATIVE.png` | `ab31c41ec168aea7fff2206d1536c9ff61c763c3da175defe7cc4bd14649bf96` |
| `C02_MEDIUM_v1_CHATGPT_NATIVE.png` | `c0ec77283233b4b4f49c172697f8c7b42fd2a7cc4bf3960670723b1a871fd0a7` |

Ảnh cận PNG IHDR thực941×1672; ratio gần9:16, không video720p. Chỉ xem ảnh tĩnh và đọc nguồn, không UI/API/Git/credit/generation hoặc sửa inputs. Không nghe/xem AV, không lip-sync/motion pass. Root chưa sinh video thứ hai theo registry.

## Actual findings

| Rule / disposition | Expected → observed | Mức / handoff và giới hạn |
| --- | --- | --- |
| REF244-FACE / MET static | Cận vừa hai người thấy mắt/miệng → hai mặt lớn, rõ, không legs/shoes/tablelegs; shoulders/torso/hands/bowls có trong khung. | Camera intent hiện có ngay trong source, giảm yêu cầu model tự thiết kế từ master rộng. Chưa chứng minh video giữ đúng cỡ hoặc có sức diễn. |
| REF244-ID / MET trong visible scope | Giữ Khoai/Đào và scale tương đối → Khoai trái vàng lấm tấm/mày dày/mắt nâu; Đào phải cuống/lá/rãnh đào/lông mi, mặt 3D cùng style. Jacket tối/sơmi kem và blouse kem/nơ dusty-pink/váy sage giữ. | Không thấy MAJOR redesign; không pixel-identical. Lens/camera mới có biến đổi tỉ lệ nhìn thấy, chưa continuity đa góc trên chuyển động. |
| REF244-GEO / MET static | Cùng phố/quán → vẫn openstreetperspective, đèn lồng/stringlights, awningcamđỏ bên phải, xe/quầy mờ. Không tường phẳng/cửa cuốn/quạt/bảng “NEM BÙI” như take243. | Giữ recognizable set, không tuyên bố mọi backgroundpixel trùng. Lỗi GEO243 vẫn mở trên native243; reference mới chỉ xử lý đầu vào, chưa đóng bằng take sửa. |
| REF244-F0 / MET static | Môi khép,4tay nghỉ riêng, bát trống → actual đúng; đũa không được cầm, không chắp tay/trướcngực. | Head-state có cue rõ hơn243. Không chứng minh model sẽ không tạo cử chỉ hoặc Đào speechmouth. |
| REF244-TABLE / MET visible, peripheral partial | Giữ nem giữa/rau trái/chấm trái&trướcphải/bát/đũa/cốcphải → positions tương đối nhất quán; rau/cốc bị crop ở ngoại vi vì cận hơn. | Phù hợp236/packet coverage riêngC02, không phải dời rau hoặc xóa cốc. Không báo toàn bộ props ngoài coverage đã kiểm. Masterv5 vẫn là chuẩn fulltable. |
| REF244-FOOD / MET morphology visible | Coldnem miếng/dải dẹt phủ bột → material giữ, không thấy steam/noodle-substitution rõ. | Không xác nhận công thức/claim. Đĩa món còn khá lớn ở nửa dưới nhưng hai mặt vẫn chủ đạo; không blocker “toàn bát nem”. Kiểm camera attention thực khi sinh. |
| REF244-LIGHT / MET static | Warm/readableeyes/mouths → mặt và bàn sáng mềm, nền mềm phụ trợ. | Không nhận continuous flicker/exposure/motion pass. |
| REF244-MARGIN / MINOR_LIMIT | Fullfaces → mắt/miệng/mặt đầy đủ, nhưng silhouette tayáo phía trái và cuống/lá/phần ngoại vi phía phải sát hoặc ra biên. | Không thấy crop mặt/miệng; chưa blocker static. Video cần tránh model làm headturn mất mặt hoặc thêm crop. Không yêu cầu mọi servingfull trongcận như master. |
| REF244-FORMAT / MINOR_LIMIT | Referenceportrait →941×1672 hơi lệch9:16 (~0,053%). | Không miễn tiêu chuẩn nativevideo/export720×1280. Không kéo giãn/đổi nhãn file thành720p. |

## Paper request và next gate

Reference prompt244 không mâu thuẫn giữa giữ scene geography và crop ngoại vi; nó giữ camera riêngC02 trong direction236, không thay toàn bộ phim/canon. C02 draft242 vẫn gọi “attachedMASTER01v5”: trước rerun phải lập phiên bản request/prompt mới chỉ đúng shot-specific reference/hash/cloudbinding, không im lặng giữ tên master hoặc đính hai framing đối nghịch. Giữ exact phầnN02 và mộtK20; không thêm “Khoan”, voiceĐào hoặc lời audition.

Owner đã chấp nhận **audio native243 đúng hash5ba2878f…**: “Đúng K20, lời và nhịp chấp nhận được” theo244. Tôi không nghe và không chuyển acceptance đó thành tiếng take mới. Native243 vẫn REWORK hình; lipsync/fullAV chưa được duyệt.

**Bước tiếp:** root đọc report, khóa shotreference như cụ thể hóa direction đã có hoặc trình owner nếu framing/identity/canon vượt scope; không suy owner đã xem/duyệt ảnh mới từ approval master/audio. Request rerun cần exactsource/config/quote/quyền238 và kiểm gate còn mở. Sau take mới kiểm nền/cận mặt/F0 suốt range, nghe/lipsync lại và checkpointC02 riêng. Nếu cùngMAJOR tiếp tục lặp thì dừng chẩn đoán, không lấy still này làm cam kết fix hoặc quyền autorun.

Đã xác định: staticref mới đáp ứng camera/identity/F0/geography nhìn thấy. Đã chốt trong review: handoffstatic có giới hạn, không approval thay owner. Giả định: source gần đúng camera có thể giữ ý đồ tốt hơn, chưa proof. Còn mở: livebinding/request/quote và actualvideo/voice/AV/joins. Không xác suất thành công, không releasePASS.
