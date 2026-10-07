# C01A T02 — Preflight phản biện độc lập REC246

Run **C01A-T02-PREFLIGHT-246**, ngày 07/10/2026. **Verdict: PASS_PAPER_WITH_ACTUAL_BOUNDARY_AND_INTENT_GATES.** Không có blocker mâu thuẫn rõ trên giấy. Không media/voice/motion PASS hoặc quyền tự chạy T03.

## Exact input và phạm vi

Đọc full latest `04_requests/C01A_T02_prompt_246.txt`, requestT02, ACTT02 và report nativeT01 của reviewer; kế thừa contracts/236/238/246 đã đọc full trong run trước. Xem lại actual sourceF0. Chỉ local read/view + report này; không UI/API/Git/credit/generation.

Hash tính thật bằng PowerShell:

- PromptT02 **`1b6046bff3644f7a1d14766886da54db209e2cd6e39d78d98211d58d196ac256`**, khớp exact request/dispatch.
- F0 **`c59ad1e436ad42e7525c564a883269ef9f80288f4c76b675e64bba1798500cad`**, không đổi source. Actual ảnh vẫn hai mặt rõ/Khoai trái/Đào phải, bốn tay nghỉ, hai bát trống/đũa bàn, nem nguội/phục vụ đúng set. Source không chứng minh T02 endpoint/motion.

## Kiểm sửa có mục tiêu

| Rule | Latest paper → đánh giá độc lập | Gate actual |
| --- | --- | --- |
| GAP | Đích tay đổi khỏi sát rim thành cao trên vùng trống giữa bát–đĩa; yêu cầu band khoảng hở ít nhất bề rộng bàn tay biểu kiến, đầu ngón không overlap/disappear sau outline đĩa. | Xử lý trực tiếp failure nhìn thấy củaT01. Khoảng cách là tiêu chí ảnh, không cm/clearance đo hoặc lời bảo đảm model. Vùng giữa bát–đĩa chật, nhưng prompt yêu cầu **ở trên** vùng ấy, không bắt bàn tay nằm lọt trên mặt bàn. Không thấy mâu thuẫn hình học giấy chắc chắn. Kiểm depth/path thật. |
| INTENT | Cẳng tay tiến chéo vào trong về đĩa; bàn tay thả lỏng/thẳng theo reach, không open-palm trình bày món. Ngón hướng về đĩa; ý định vẫn lấy, chưa contact. | Bổ sung ACT đã tích hợp. **Không đổi canon** sang review/giới thiệu món trên giấy. Nếu actual thành “mời xem món” hoặc bàn tay nâng đứng yên không reach đọc được, vẫn REWORK dù gap đẹp. |
| HOLD | Một reach chưa hoàn tất; sau trọn “em” khép môi, giữ pose cao tới cuối, không lowering/contact/retract/reset; interruption ở shot sau. | Xử lý premature return T01. Hold là buffer native, không buộc dùng toàn6s. Chọn range ngắn giữ speech+ý định; không framefreeze/một hold dài làm mất nghĩa bị ngắt. |
| CANON/VOICE | Chỉ mộtD06 đúng `6dadc0b1-00c3-493c-943d-f4a1e4a88feb`; N01 nguyên văn “Anh nhìn mãi. Không hợp thì để em.” một lần. Khoai im/môi khép/tay nghỉ; khôngKhoan trong spoken text. | Giữ speaker và cặp bạn trưởng thành. ProductionD06 vẫn cần owner nghe trên exact take mới; tên/ID hoặc ASR không PASS giọng/lip-sync. |
| SET/F0/CAMERA | Cùng source, fixed two-shot đủ cả hai mặt/tay/đĩa; đũa/bát/rau/chấm/cốc giữ, không steam/món dịch, không thêm chữ/voice/nhạc. | Regression check đầy đủ, không dời props để giảm lỗi. “Behind the rim” đọc là phía sâu hơn trong scene **vẫn thấy cả tay và band trống**, không cho phép tay bị đĩa che vì clause kế đã cấm occlusion. |
| NEXTCUE | C01B còn pending, phải derive từ endpoint C01A actual trước-contact rồi Khoan→dừng/thu; C02 accepted riêng. | Không tự C01B từ endpoint giấy hoặc F0 nghỉ. Không khóa EDL/30s hay thời điểm speech từT01 choT02. |

T02 đổi endpoint/hold và rephrase toàn prompt: **không phải thí nghiệm đơn biến**. Giả thuyết near-rim conditioning/gesture completion chưa causal proof. PASS_PAPER chỉ xác nhận yêu cầu coherent và sửa đúng failure mục tiêu, không forecast xác suất hoặc guarantee.

## Live và handoff

Current request + parent message ghi root đã kiểm new-generation overview composer, **không video-edit**; một ảnhUUID `4c83356f-ac72-437b-8dd7-f8534b61103a`, một exactD06/performance; fullreadbacktrue, Omni1.1Flash/Ingredients/720p/9:16/6s/x1/AgentOFF, fullquote10≤15, screenshot `246_C01A/C01A_T02_FULL_INPUT_QUOTE10.png`, same-tab balance1040, submit_count0. **Root-reported UI checks**, reviewer không trực tiếp kiểm UI. Root phải đóng trạng thái/gate sau đọc full report và giữ readback cuối; input đổi phải recheck, không dùng report hash này cho prompt khác.

Budget quyền238: targeted retake, conservative spent40/remaining460, retake165, reserve110 không tự dùng. Sau một output: hash/probe/decode, kiểm đủ dày whole handpath và đoạn speech-end actual; ngheD06/lời/AV; chọn endpoint trọn lời+visiblegap+unfinishedreach rồi mớiC01B. Không PASS chỉ từ ảnh cuối.

**Same MAJOR boundary/no-gap hoặc premature-return tiếp tục ở output C01A thứ hai ⇒ STOP chẩn đoán, không automaticT03.** Failure mới về presenting intent cũng phải giữ dependency nếu không có range đạt, không gọi sửa được lỗi cũ là xong cảnh.

Đã xác định: exactsameF0/voice/N01, paper treatment rõ hai failure và anti-presentation. Quyết địnhreview: PASS_PAPER có actualgates, không ownerapprovaltake. Giả định: elevated unfinishedreach có thể diễn tự nhiên, chưa evidence. Còn mở: actualgap/path/intent/voice/endpoint/joins. Bước tiếp: root đóng live/gate rồi một targeted retake trong238; nếu lỗi lặp thì trình chẩn đoán, không tiếp chuỗi.
