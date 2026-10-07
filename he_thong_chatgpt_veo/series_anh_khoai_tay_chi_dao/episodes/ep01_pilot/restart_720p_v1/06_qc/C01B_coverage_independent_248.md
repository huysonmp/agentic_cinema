# C01B coverage A — phản biện thiết kế và still độc lập REC248

Ngày 08/10/2026. Reviewer không phải maker DIR/DOP/ACT/EDIT hoặc root producer. **DESIGN_STILL_CONDITIONAL_HANDOFF / PRODUCTION_HOLD**. Có thể trình owner đúng gói BM cận Khoai → BR khung gốc và ảnh BM v1, không thấy lỗi still buộc tạo lại trước trình. Đây không phải approval ảnh, motion, voice, lip-sync, media, rights hoặc chi credit; STOP T01/T02 vẫn giữ.

## Nguồn và capability

Đọc đầy đủ direction248, production brief248/v1 hiện hành, cả4 report DIR/ACT/DOP/EDIT248 (đọc lại riêng khi output tổng bị cắt),217,236 và scoped238. Đọc thêm exact image prompt248 để đối soát provenance/intention. Trực tiếp xem **đủ3 ảnh local** bằng view_image, tính lại SHA256 PowerShell:

| Ảnh dưới `02_refs/` | SHA256 thực |
| --- | --- |
| `C01B_START_from_C01A_T04_FLOW_v1.png` — A80 | `0cf422f2b28dae631785af6ec19fc7488800c0cf8d22bb95dddd04e1b7ae2acb` |
| `C01A_F0_from_C02_T02_v1.png` — C02F0 | `c59ad1e436ad42e7525c564a883269ef9f80288f4c76b675e64bba1798500cad` |
| `C01B_BM_START_v1_CHATGPT_FOR_REVIEW_248.png` | `8ecb1105de2b8a0b786c05ad38e4965206d62a7629741a7863e8fcb77f7bad03` |

BM941×1672 theo current input record; hai endpoints720×1280. Không xem lại old natives, không continuous video/AV/actual hearing, không feature/quote UI, không generate/edit/crop media. Still có thể kiểm framing/state thấy được; không chứng minh state ngoài khung/path/speech.

## Findings thiết kế/still

| Scope / severity | Expected / actual | Closure cần có |
| --- | --- | --- |
| **BM speaker framing / thuận lợi** | Actual BM có toàn đầu, mắt/mày/miệng Khoai, lớn hơn A80 rõ; tay anh nghỉ, áo navy/cream và palette quán tương thích. Anh trái, Đào một phần bên phải; không reverse axis/MC nhìn trực diện. Môi cả hai khép trong still, mắt thấp. | Hợp nhiệm vụ người ngắt, không ảnh master đủ hai mặt. Chưa chứng minh anh sẽ nhìn bạn/phát nguyên Khoan/K20 trong video. Owner duyệt coverage/ảnh mới, native phải kiểm riêng. |
| **BM inner hand / outer UNKNOWN** | Tay trong Đào còn visible cong gần thân/bát, không hiện một grip vành trái như take lỗi. Tay ngoài/contact phải, cốc và phần bàn ngoài khung không thấy. Mặt Đào bị cắt ở mép phải đúng framing bất đối xứng. | Không blocker tự động chỉ vì BM không thấy toàn contact. Không gọi offscreen là contact preserved hoặc cho phép reset. BR phải mở đúng A80 và chứng minh toàn release/return; sai lộ ở BM/BR vẫn REWORK. |
| **Identity/set/food projection / conditional** | Nhận diện Khoai/Đào, clothes và phố mở/đèn/mái bạt giữ nét chính; BM đổi cỡ nhìn có động cơ rõ. Một phần nem/chấm/đũa/bát/rau còn, không steam nhìn thấy. Projection/từng miếng có khác trong ảnh tái dựng; full plate và props bên phải không đủ để so. | Không khẳng định same3D camera hoặc toàn bộ món không redraw/relocate. Không observed gross scene reset trong3still, nhưng continuity hình/món/bàn là gate actual joins, không no-steam thay food PASS. |
| **BR endpoints / đủ phạm vi hình** | A80 hiện đủ hai mặt, outer fingers tại vành phải, inner hover gần bát; C02F0 hai tay Đào nghỉ quanh bát, Khoai nghỉ. Cùng trục/camera/nem nguội/bát trống/phục vụ. Mắt C02F0 thấp, không eye-contact endpoint. | Đủ reference chức năng contact→rest và vùng kiểm mặt/tay. Không proof path. BR cần mắt lên nhận cue rồi có thể về thấp tự nhiên trước endpoint, không ép eye-lift/eye-lower/return vào timestamp giấy hoặc teleport. |
| **BM→BR causal state / gate chính** | Integrated brief/EDIT yêu cầu BM chưa release hoặc quay mắt rõ; BR bắt A80 mắt thấp rồi mới phản ứng với trọn Khoan vừa nghe. Đây là một reaction sau cue, không phát lại reach. | Coherent paper nếu BM actual giữ điều kiện. Nếu BM đã nâng mắt/thu rồi BR reset A80, HOLD dependency; không tạo BR dựa endpoint thuận tiện hoặc cắt lại oldnative để che. Chọn BM range chỉ sau giữ trọn âm/miệng actual; không hứa dùng earlytrim chắc cứu được. |
| **DIR stale visibility/beat / harmonize trước request** | DIR mục beat map và camera vẫn đòi B-K đủ trạng thái hai tay/mặt Đào, cut khi attention đã bắt đầu, BR medium. DOP hiện hành và EDIT/brief248/v1 đã chuyển BM outer-offscreen UNKNOWN, BR original-wide, reaction chỉ ở BR. | Đây là **xung đột maker proposal lịch sử**, không blocker integrated design đã nêu rõ lựa chọn. Root cần ghi version/precedence brief248/v1 và không chép những câu DIR cũ vào BM/BR prompts. Root báo đã yêu cầu DIR amendment, critic chưa đọc amendment đó; root phải đối soát closure trước request. Nếu vẫn yêu cầu hai specs cùng lúc thì trở thành blocker request. Không coi mọi report đã đồng thuận từng câu. |
| **Aspect / format / gate kỹ thuật** | BM941×1672 gần9:16, không native720×1280 và không exact9:16. Full đầu Khoai hiện có margin; Đào cắt biên có chủ đích. | Không tự crop/resize gọi approved720. Trước submit kiểm UI xử lý input không làm mất speaker coverage; native/export probe thực. Sai raster reference nhỏ chưa buộc remake nghệ thuật, nhưng livevideoformat vẫn HOLD. |
| **Watermark/provenance / conditional** | A80/C02F0 thấy symbol4điểm dưới-phải; BM không thấy. Exact image prompt yêu cầu preserve any existing visible watermark, không chỉ dẫn xóa dấu. Brief mô tả new generated coverage reference, không cleanup/cropnative và giữsource nguyên. | Không có evidence thao tác removal trên native; cũng không suy watermark vắng=rightsPASS hoặc hợp lệ mọi cách xử lý. Root đối soát input/tool/output provenance và policy scope trước upload; native/export giữmark. Không bịa quyền bản quyền hoặc cam kết kết quả model. |

## Authority, timing và production readiness tách riêng

Owner248 chọn A là **design authorized**, chưa duyệt actual BM v1 hoặc hai request/chi. 217 cho chuyên biệt + critic độc lập; 236/238 giữ voices/canon/native720/quote≤15/x1, các owner checkpoints và reserve110. Khảo sát Frames không lời cùng công cụ hiện có phù hợp tuyến236 dự kiến; feature START+END/720/no speech vẫn **unchecked**, không đồng nghĩa có thể submit hoặc tự fallback/new tool/model.

Giữ selected A 3,375s và C02 7,541667s, tổng 10,916667s. B selected 2–3s chỉ working hypothesis; còn 19,083333−B cho phần sau. Không EDL/range/measured cue mới, không guarantee 30s hoặc probability thành công. Không bỏ lời/âm cuối/release, speed/freeze/food cover/audio-overlay để đạt target. Một BM speech và một BR silent là tách nhiệm vụ hợp lý trên giấy, **không bằng chứng giảm lỗi đã được kiểm nghiệm**.

Proposal 2 outputs × ≤15 = ≤30 chỉ là trần cần owner chốt, không live quote/new approval. STOP tuyến cũ chưa tự đóng bằng đổi tên BM/BR. Snapshot 74 spent/426 remain là hồ sơ247, không live balance mới; reserve110 không dùng. Audio T01 không transfer sang BM; BR không lời phải kiểm actual lips/ambient, không mute lỗi để gọi im đạt.

## Các gate cần đóng theo thứ tự

1. Root version-lock integrated brief248/v1 (BM coverage bất đối xứng; BR wide; reaction chỉ ở BR), nêu tradeoffs offscreen/contact UNKNOWN và provenance, trình owner duyệt **đúng 3 refs/coverage và production scope ≤30** nếu muốn mở chi. Không hỏi lại lựa chọn A/B.
2. CTD/FLOW xác minh route/features/config/quote trong phạm vi duyệt; BM đúng một K20, BR không voice/hai endpoint khi composer thực hỗ trợ; prompt readback/source hash/cloud ID/Agent OFF. Nếu thiếu route hoặc auto-fallback, HOLD/trình khoảng thiếu, không “exact” từ Ingredients.
3. BM mới: whole Khoan trên mặt Khoai, tay nghỉ; Đào chưa reaction/reset; nghe exact new artifact bằng capability/owner và kiểm actual source exit. Không chạy BR trước BM dependency closure.
4. BR mới: actual START/path/END, face/eyes/outer contact→release→return và inner inward, no food/table reset/pull/extra reach. Full-frame/dense QC được ghi đúng scope, endpoints không chứng nhận mọi motion.
5. Dựng actual A/BM/BR/C02: kiểm 3 joins, đúng waveform/nhịp/speaker, raster/FPS/ranges/duration/duplicate instances và measured 30s. Review source riêng không thay target export; chưa đạt chưa C03A/finishing/release.

**Đã xác định:** hash 3 still, framing BM phục vụ speaker, BR endpoints đủ vùng nhìn; stale DIR proposal được integrated brief thay rõ. **Quyết định review:** conditional design/still handoff, không blocker buộc remake trước owner review; PRODUCTION_HOLD. **Giả định:** tách speech/reaction giúp kiểm nhiệm vụ, chưa test. **Còn mở:** owner đúng scope, provenance/feature/quote, BM dependency/path/new audio/actual joins/timing. **Bước tiếp:** root đọc đầy đủ/chốt precedence rồi trình gói248, không trả phí hoặc gọi media PASS từ report này.
