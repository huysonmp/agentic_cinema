# REC263 — acceptance C04, continuity và gate thời lượng C05

Kết luận: GO_C05_INPUT_PREPARATION_ONLY; HOLD_PAID_C05_WHILE_TIMING_TARGET_UNRESOLVED. Nguồn C04 đã được owner chọn dưới exception A; không phải PASS prompt262 cũ, join/audio hoặc toàn phim.

## Phạm vi kiểm và acceptance

- Đã full-read decision263, scoped238 JSON/hồ sơ, plan236, các hồ sơ selected-opening258–261, bindings238, derivative measurements258/259; đọc draft/preparation C05 hiện hành. Chỉ kiểm hồ sơ và ảnh native; không nghe audio hoặc xem continuous AV trong lượt này.
- Decision263 chọn đúng native C04 T02 SHA `8ad98f21c0c904b01055d6f579900cd60c107a152a9166a8cfa563165a47a209`, `[0,144)`/24fps/6s: owner chấp nhận cup gần môi/môi hé và gaze-return SAU A nhấc. Report262 HOLD theo điều kiện cũ giữ nguyên lịch sử, không sửa thành PASS.
- STOP cùng major đã được xử lý bằng owner chấp nhận staging cụ thể, không bằng quyền retry. C04 production đóng; không suy approval sang nuốt nước, silence, C05, full opening/C03B→C04 join, 30s final hoặc gia hạn runtime.
- Đã xem START C05 actual F143 và rehash PNG: `2e4f4a5fbf0d5f310010762d26d0c74f08bfb2da3eab792f69a3be568b94c2db`. Nguồn/hash/F143 đúng preparation; ảnh không là chứng minh Ingredients khóa pixel/motion.

## Trạng thái và ranh giới phải giữ

- Ảnh F143: Khoai LEFT, A còn ở tips đôi đũa riêng trong tay ngoài SCREEN-LEFT, phía mình dưới ngực/xa miệng; Đào RIGHT đã nhìn về anh, ly giữ bằng tay ngoài SCREEN-RIGHT dưới miệng; hai môi khép, tay trong nghỉ, hai bát rỗng, đôi Đào nghỉ. Không reset A/đũa/ly hoặc lấy lại từ đĩa.
- C05 bắt đầu với gaze đã trở lại, không quay về ly rồi quay lại, không diễn phát hiện lần hai. Có thể đọc A→mắt Khoai như tiếp nối phản ứng, không một discovery mới; Khoai nhận ra bị bắt gặp, khựng và giữ SAME A trước lời chữa cháy C06.
- C05 chỉ Đào/N05 “Chờ em quay lưng nữa à?”, D06 ID `6dadc0b1-00c3-493c-943d-f4a1e4a88feb`; không K20 voice, không N06 sớm. Preset owner-approved không chứng minh waveform mới/word/sync; output cần actual nghe và kiểm mặt nói–mặt nghe.
- C06 mới đổi hướng cùng A về Đào; C07 lời nhận/đưa bát còn rỗng; C08 thả SAME A một lần; C09 mới gắp B khác, A phải còn trong bát Đào. Không ăn A/nhân đôi/biến mất, không freeze frame để thay pause sống, không bỏ đường causal để tiết kiệm giây.
- Draft C05 hash `bbcb5388bcab46aa3caa3a47bce65bb3fe20003d039e95828521b5af66040db7` khớp rehash: đã bỏ duplicate turn, giữ A/ly/tay/bát đúng. Không thấy mâu thuẫn giấy thiết yếu mới; đề xuất sinh4s không là selected runtime và không chứng minh câu/hành vi sẽ vừa4s. Live binding/quote còn chưa kiểm.

## Số đo hiện có và điều chưa biết

- Các range đã chọn: opening tới C03B 422 frame/17.583333s, cộng C04 144 frame/6s =566 frame/23.583333s. Target30s/720 frame còn154 frame/6.416667s cho C05–C09.
- Đây là tổng range lựa chọn, không acceptance của toàn export23.583s chưa dựng/kiểm. Entire17.583s export không được owner explicit AV approve trong261; owner đã nhận C03B short riêng. C03B→C04 và C04→C05 vẫn phải actual encoded join QC.
- Plan236 dành C05–C09 tổng11s (2.5+2+2.5+1.5+2.5), chênh4.583333s/110 frame so quỹ hiện có. 11s là phân bổ giấy, không minimum đã đo; chưa có duration thoại/hành động native C05–C09 nên không kết luận chắc chắn30s bất khả thi.
- C03A đã cắt1.75s trước Khoai mở môi, N03 ASR kết1.36s; phần chênh0.39s chứa closure/response. C03B2.083333s, ASR N04 kết1.24s; chênh0.843333s chứa phản ứng/closure. Không coi các chênh ASR này là số giây reclaim an toàn; ASR không thay nghe âm cuối/nhịp và seam.
- T02 còn mutual-gaze idle đầu khoảng1s và tail caught/pause khoảngF120..143/1s; đó chỉ là vùng có thể audit, không khoản tiết kiệm được chứng minh. Trim đầu đổi entry từ C03B; trim tail đổi source endpoint F143/C05 dependency và độ đọc caught beat. BR đã cắt xuống50 frame, release/retract phải đủ; không lấy silent bằng chứng thành redundant.
- Hồ sơ hiện không có EDL mới + nghe/nhìn actual chứng minh reclaim an toàn đủ110 frame. Không cộng nhẩm mọi silence/rest rồi cam kết30s; không cắt lời, tăng speed/pitch, bỏ beat hoặc tái sinh các clip accepted để chữa bảng thời gian.

## Quyết định cần đóng trước paid C05

- Giữ30s: làm audit/re-edit có bằng chứng trên rests/transitions của nguồn accepted, bảo toàn lời/mặt/causality; trình range/EDL/candidate và re-QC join/AV đúng version. Chỉ số đo hiện tại chưa đủ thông qua tuyến này; future speech vẫn UNKNOWN.
- Owner cho phép target dài hơn, ví dụ trần35–38s: giữ accepted footage/core không speed; ở35s còn11.416667s, ở38s còn14.416667s cho C05–C09. Đây là quỹ tính toán, không lời hứa35s hoặc38s chắc chắn chứa đủ footage chưa sinh. Cần owner chốt một target/trần cụ thể; câu acceptance C04 chưa cấp quyền này.
- Khuyến nghị: trình timing decision ngay, không paid C05 khi vẫn mặc định30s mà chưa có disposition/risk-plan được chấp thuận. Có thể chuẩn bị draft/ref/maker review, nhưng report này không GO submit. Sau chốt target phải có request/prompt hiện hành, live D06-only/config/quote≤15/x1/AgentOFF/audio-enabled và root full-read; output thực vẫn qua word/voice/AV/A/joins gate.
- Quyền238 không mở rộng: project149/500 còn351 theo decision/preparation; first109, retake87, post45, reserve110 CLOSED. Không cấp ngân sách/tool/voice mới; báo cáo không tự phê duyệt generation hoặc toàn phim.

## Amendment — current final paper preflight REC263

- Đã full-read lại `C05_T01_prompt_263.txt`, preparation263 hiện hành và toàn maker `C05_DIR_DOP_ACT_EDIT_input_263.md`; rehash final khớp `16a76e4826fb8d1cdc23b4acf245d04b7c0d3a0cb60c3ad47c76fd933281b679`. Draft `bbcb...` phía trên chỉ là lịch sử, không target preflight final.
- Sửa hẹp “Already aware... brief confirming glance” đã tích hợp đúng khuyến nghị maker, loại ambiguity “notices” có thể diễn discovery lại. Không đổi N05/D06, source F143, ly, SAME A, hai bát trống, no-transfer/no-eat và listener closed lips; không thấy contradiction giấy thiết yếu mới. Tiny arrested movement phải là khựng trong tư thế hiện có, không lift/transfer mới.
- GO_CURRENT_FINAL_INPUT_PREPARATION_AND_LATER_LIVE_GATE_ONLY. HOLD_PAID_C05_WHILE_TIMING_TARGET_UNRESOLVED giữ nguyên: owner chưa trả lời35s rough-cap hay giữ30s/re-edit, chưa có live quote/input proof. Final prompt/readback đúng không chứng minh backend binding, motion, voice/sync, full joins hoặc thời lượng phim; root cần full-read amendment trước gate tiếp theo.
