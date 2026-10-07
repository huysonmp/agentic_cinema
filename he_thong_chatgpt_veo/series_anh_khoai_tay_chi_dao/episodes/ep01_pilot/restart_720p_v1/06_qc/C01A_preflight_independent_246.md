# C01A — Preflight độc lập REC246

Run **C01A-CRITIC-246**, ngày 07/10/2026. **Verdict: PASS_PAPER_WITH_ACTUAL_OUTPUT_GATES.** Không phát hiện mâu thuẫn chặn trong prompt/request tích hợp đã đọc. Không phải motion/audio/native PASS hoặc quyền retry; root chịu trách nhiệm live submission trong scoped238.

## Phạm vi và provenance thực

Đọc đầy đủ current kế hoạch236, scoped238, `00_decisions/C02-export-approval-246.json`, C01A DOP/ACT/EDIT246, exact prompt/request246 và bindings238. Contracts PROD7/DIRECT/217, canon178/storyboard214 đã đọc đầy đủ ở các run trước trong cùng context. Đã xem toàn actual `02_refs/C01A_F0_from_C02_T02_v1.png`. Không lấy tên vai hoặc paper maker làm bằng chứng output đạt. Không UI/API/Git/credit/generation, không chỉnh input/media.

Hash thực bằng PowerShell:

- Ảnh F0: **`c59ad1e436ad42e7525c564a883269ef9f80288f4c76b675e64bba1798500cad`**; trùng hash owner QC `C02_T02_FLOW_245/all_native_frames/00001.png`, nên byte-identical với frame0 export đã kiểm, không ảnh tái tạo giả endpoint.
- Prompt246: **`357bbde54332da9b20bed7cc222ae2ab81b8a116a105ac3c873ab83fe984e990`**; khớp request.

Owner246 đã chấp nhận exact C02 export hash `d151eb1d…`, không native tail/cảnh tương lai/toàn phim. Đây đóng dependency C02 cho chuẩn bị C01A, không chứng nhận D06 trên C01A. Ảnh lấy từ tài khoản mới, không dùng footage nick cũ.

## Actual still và kiểm tích hợp

| Tiêu chí | Quan sát / đối soát | Kết luận và giới hạn |
| --- | --- | --- |
| Identity/set/coverage | Actual ảnh giữ Khoai trái, Đào phải, adult clothes/style; hai mặt/mắt/miệng rõ. Quán phố mở/đèn lồng/mái bạt phải, sáng ấm mềm. | STILL_MET. Mặt/tay/vùng đĩa cùng coverage. Không chứng minh model giữ geometry/camera qua motion. |
| F0 | Bốn tay nghỉ riêng, môi khép, hai bát riêng trống, hai đôi đũa trên bàn; nem giữa, rau trước-trái, hai chấm/cốc ngoài-phải. Không visible steam. Serving ngoại vi bị crop một phần như source đã chốt. | STILL_MET, không đổi geography để né tay. F0 food không có nghĩa cuối C01A bốn tay vẫn nghỉ. |
| Speaker/voice/lời | Prompt/request chỉ Đào D06 `6dadc0b1-00c3-493c-943d-f4a1e4a88feb`, khớp bindings. Lời nguyên văn đúng một lượt: “Anh nhìn mãi. Không hợp thì để em.” Khoai listener im/môi khép/tay nghỉ. “Khoan” chỉ xuất hiện trong lệnh cấm, không được đưa vào spoken text. | PAPER_MET. Không leak K20 hoặc audition. Actual female Northern D06, phát âm, lời, speaker/mouth và nhịp vẫn UNKNOWN. |
| Route tay | Đúng tay ngoài screen-right, lúc nghỉ ở ngoài bát gần cốc/đũa. Prompt cho nhấc và đi chéo vào trong, xa cốc, phía trên đũa tới mép trên-phải đĩa; tay trong nghỉ. | PAPER_COHERENT nhưng bàn chật; 2D không đo clearance. Cần actual trajectory tránh bát/đũa/chấm/cốc, ngón không deform/nhân đôi. Không được chỉ xem đầu/cuối để PASS path. |
| Diễn/nhịp | Câu đầu nhìn Khoai/nét cười nhỏ; câu sau mới nhìn đĩa/vươn; sau “em” môi khép và tay còn định lấy. Khoai chú ý bằng mắt, không giành lượt. | DOP/ACT/EDIT ý định tương thích, không biến thành review/MC/trẻ em/cặp đôi. No-startle/no-withdrawal trong C01A giữ cause→“Khoan” ở C01B. |
| Contact/next cue | Khoảng hở nhìn thấy, không contact/chạm/kéo/ăn; no early retract. C01B chưa có endpoint; phải dùng state ra actual C01A, rồi Khoai ngắt→Đào dừng/thu→F0 nối C02. | PAPER_MET. “Near rim” không thành contact allowance; không claim Ingredients khóa start/end. Nếu không có range vừa đủ lời vừa reach trước-contact thì HOLD endpoint, không cứu bằng cận món/cắt âm “em”. |
| Timing/finishing | Native6s; camera fixed two-shot; không cutaway/zoom, speech mặt rõ. Giữ watermark; không thêm chữ/nhạc/brand, ambience dưới thoại. | Native6s không chứng minh opening4,5s hoặc toàn phim30s. Ambience là thiết kế, cần nghe không thêm giọng nền. Không hứa stem/mix/tool controls chưa kiểm. |

## Live/config và hồ sơ

Current request đọc lại sau parent cập nhật: Ingredients / Omni1.1Flash / 720p / 9:16 / 6s / x1 / Agent OFF; một image UUID `4c83356f-ac72-437b-8dd7-f8534b61103a`, một D06; full prompt readback true, full-input quote **10 ≤15**, submit_count0. Screenshot được root ghi `246_C01A/C01A_FULL_INPUT_QUOTE10.png`. **Đây là live checks root-reported, không critic trực tiếp kiểm UI.** Root giữ cổng screenshot/readback cuối sau mọi sửa; report paper không giữ hiệu lực nếu inputs/hash/config đổi.

Request `status` còn tên pending independent/live dù các fields live đã có: cập nhật trạng thái sau root đọc full report, không giả đã submit. Balance tab mới1050 khác tab generation1020 đã được ghi riêng; không mặc định refund hoặc tăng quyền chi. Project spent bảo thủ30/remaining470; first-pass150 và retake165 chưa tự cộng reserve110. Không blocker paper từ số dư khi quote/quyền vẫn rõ, nhưng ledger cần đối soát sau lượt.

## Actual gate sau một output

1. Giữ native/hash/request/config/phí thực; probe/decode và frame evidence theo FPS thật. Không faked source timing.
2. Kiểm đủ dày **toàn path** tay ngoài và cuối lời: tay rời nghỉ trong câu sau, không va props/contact/retract; Khoai không nói miệng thay, không có steam/set/camera regression. Frame đầu/cuối đẹp không chứng minh trajectory.
3. Owner/SIA nghe exact C01A để xác nhận D06 nữ Bắc trưởng thành, đúng nguyên văn/nhịp/âm cuối, không male/additional voice; kiểm actualAV/sync theo khả năng. **Checkpoint D06 bắt buộc trước mở thêm thoại Đào**, preview239 và C02 approval246 không thay.
4. EDIT chọn range measured sau trọn “em”, tay vẫn trước-contact; extract exact endpoint làm nguồn C01B. C01B/C02 joins phải kiểm riêng, không gọi approved C02 = approved assembly. 4,5s vẫn target cần đo/phân bổ, không tăng tốc/pitch hay bỏ reaction.
5. Nếu cùng MAJOR C01A lặp hai output liên tiếp: STOP chẩn đoán theo238, không autorun hoặc test tay riêng. Chưa có output nên rủi ro path/timing chỉ là UNKNOWN cần kiểm, không defect media đã xảy ra.

**Đã xác định:** F0 exact/hash, canon N01, một D06 và paper integration nhất quán. **Quyết định reviewer:** PASS_PAPER, không chọn take/EDL/approval thay owner. **Giả định làm việc:** reach nâng trên đũa khả thi và6s đủ để lấy range; chưa bằng chứng chuyển động/thời lượng lời. **Còn mở:** actual D06/AV/path/endpoint/joins. **Bước tiếp:** root đọc full report, khóa live final checks rồi một lượt trong238; QC và trình mốc nghe Đào trước chuỗi phụ thuộc.
