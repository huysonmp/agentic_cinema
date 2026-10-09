# C04 T02 — kiểm độc lập native REC262

Kết luận: HOLD / NOT_SELECTED; SAME_MAJOR_GAZE_REPEAT → STOP_FOR_DIAGNOSIS; C05 HOLD. Không có prefix đạt trọn yêu cầu hiện hành được chứng minh.

## Bằng chứng và giới hạn

- Đã tự xem đủ 18 board action_all_01..18, toàn bộ F0..143; xem thêm PNG native F60,90,94,96,104,106,112,113,114,117,120,124. F đánh số zero-based, t=F/24.
- Rehash native `05_native/EP01_720_C04_T02_NATIVE.mp4`: `8ad98f21c0c904b01055d6f579900cd60c107a152a9166a8cfa563165a47a209`.
- Full-read prompt262, rehash: `b96351ef775ee44bcacc2e61875413ed76d9deedd66f3c542bd0966457bd16e3`; run262 ràng buộc đúng START F49, không END/voice, 6s/x1. Reference SHA `c626858d067d2aed3bedec193a1825e3442faf32708cd2643266ed64dc7e6358`.
- native_evidence: H264 720×1280, 24fps, 144 frame/6s, decode đủ; có AAC stereo48k/6.016s dù no-audio ON. Stream tồn tại không chứng minh nghe được hay im lặng. Tôi không nghe, không chứng nhận continuous AV/lip-sync; không kiểm join mới.

## Quan sát thực tế

- F0 giữ hai nhân vật/shot và trạng thái tay nghỉ, hai đôi đũa trên bàn, bát riêng rỗng; không thấy biến đổi lớn so với reference. Camera cố định, không caption/text mới hay steam; native watermark còn.
- F31..39 (1.292..1.625s): Đào quay mắt/đầu xuống phía ly SCREEN-RIGHT; tay ngoài vươn lấy ly. Ly bắt đầu nhấc khoảng F54..60 (2.25..2.5s), đáy tách mặt bàn rõ F60, đưa hơi vào trong nên còn đọc được.
- Khoai bắt đầu tay ngoài tới đôi đũa riêng khoảng F64..70 (2.667..2.917s), sau khi ly đã nhấc; nhấc đôi đũa khoảng F74..80 (3.083..3.333s). Đôi riêng của Đào vẫn nghỉ; không thấy đôi trùng ở vị trí Khoai vừa lấy. Hai tay trong giữ nghỉ bên bát.
- Tips tới near-left đĩa khoảng F100..104 (4.167..4.333s), một lát biểu kiến rời đĩa F105..106 (4.375..4.417s), đi về phía Khoai F108..113 (4.5..4.708s); cuối shot dưới ngực, xa miệng, không thấy ăn/drop/offer. Không coi stills là bằng chứng tracking vật thể hoàn hảo; lát hơi gập, không khẳng định cấu trúc nem tuyệt đối.
- Grip quanh thân đũa, tips hướng đĩa, không thấy fist ở đầu; chưa chứng nhận cơ sinh học từng ngón. Bát/đĩa/chén chấm/rau nhìn ổn định, không thấy prop/camera mutation lớn. Khoai giữ môi đóng trong 144 stills.
- MAJOR mouth/cup: Đào đưa ly tiếp lên sát miệng, không chỉ nhấc nhẹ; khoảng F90 (3.75s) môi bắt đầu hé, F94..106 rim tới vùng môi, F112 (4.667s) môi mở rõ cạnh rim. Đây là cup-to-mouth/sip-like pose và vi phạm closed-mouth/no-drink staging; stills không chứng minh đã nuốt nước, không tuyên bố nghe speech.
- MAJOR gaze lặp: F113 (4.708s) mắt bắt đầu dịch trái, F114 (4.75s) rõ nhìn về Khoai/A, F115..119 đầu/mắt quay trái; F120..143 tiếp tục nhìn Khoai thay vì hấp thụ ở ly SCREEN-RIGHT. Đây là phát hiện sớm thuộc C05, không phải ending C04 yêu cầu.

## Prefix và quyết định

- T02 có cải thiện: A nhấc trước gaze-return; T01 nhìn lại F95..96 trước A nhấc F111..112. Không sao chép lỗi thời điểm T01 sang T02.
- Cắt trước cup/mouth vi phạm (~F90) mất cả pinch/lift A. Cắt trước gaze-return `[0,113)` vẫn chứa cup-to-mouth/môi mở và đoạn đưa A đang di chuyển; không thấy brief stable pause F1 trước ranh này. Pause rõ hơn khoảng F120+ đã nằm trong gaze sai.
- Vì vậy không đề xuất range đạt bằng trim, bỏ đoạn giữa, freeze, tăng tốc hay giả định intention/pause. Native giữ nguyên để diagnosis, không selected, không đóng chuỗi C03B→C04→C05 hoặc thời lượng phim.
- Cùng major “Đào nhìn lại trong pickup/pause” đã lặp T01/T02: dừng chu kỳ retake để chẩn đoán theo scoped238. Prompt hiện đã nêu rõ giữ gaze tới LAST FRAME; output trái prompt không chứng minh nguyên nhân nội bộ model. Các giả thuyết về staging ghép lift-ly với phản ứng nhìn lại chỉ là giả thuyết cần kiểm, không quyền chạy T03/đổi route/chi reserve.
- Run ghi một submit10 credit; không thực hiện thêm hành động trả phí. C05 HOLD cho tới quyết định xử lý blocker; audio/no-audio và AV vẫn cần kiểm riêng, không được nâng thành PASS từ settings/metadata/stills.

## Hai phương án chỉ để owner quyết định, chưa phê duyệt

- Đổi boundary/exception: cho phép Đào đưa ly sát môi như chuẩn bị nhấp (không suy ra nuốt); cho caught-beat xảy ra ở tail T02 SAU A đã nhấc, C05 bắt đầu với gaze đã trở lại để N05, không lặp turn. Trật tự sneak→caught có hỗ trợ từ stills T02 và giảm nhu cầu shot mới, nhưng thay điều kiện closed-mouth/no-drink và boundary C04/C05 đã duyệt; cần owner chấp thuận chính xác exception/range, kiểm AV và join mới. Hiện native vẫn NOT_SELECTED, không coi phương án này là đạt prompt cũ.
- Giữ boundary: prefix F0..75 chứa turn/ly-lift và bắt đầu cầm đũa, chưa có A nhấc; cần shot gắp/pause mới nối đúng trạng thái, Đào tiếp tục gaze-away tới hết. Không thể gọi prefix là C04 hoàn chỉnh. Rủi ro thêm join/identity/chopstick-A continuity, credit và thời lượng; phải có phương án cùng authority mới sau STOP diagnosis, không tự submit hoặc lấy reserve.
