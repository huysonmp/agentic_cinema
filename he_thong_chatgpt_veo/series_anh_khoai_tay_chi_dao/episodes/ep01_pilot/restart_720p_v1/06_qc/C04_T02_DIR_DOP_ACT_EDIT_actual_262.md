# REC262 — C04 T02 actual DIR/DOP/ACT/EDIT maker diagnosis

Target native SHA `8ad98f21c0c904b01055d6f579900cd60c107a152a9166a8cfa563165a47a209`, 720×1280/24fps/F0–143/6s. Đã xem đủ18 action boards chứa144 khung, thêm PNG nguyên khung F60/F75/F95/F99/F104/F107/F112/F114/F120; frame đánh số từ0, PNG số file=F+1.

Ghi chú biên tập của root: thống nhất nhãn với báo cáo trình owner — A điều chỉnh ranh giới C04/C05; B tách C04, giữ ranh giới cũ. Chỉ sửa nhãn, không đổi kết luận hoặc quan sát của maker.
Khả năng: đối chiếu từng khung, không playback/nghe thực; không chứng nhận silence/AV/lip-sync. Đây là chẩn đoán maker, không review độc lập.
Kết luận: NOT_SELECTED; chưa có prefix liên tục hoàn thành C04 đúng mọi điều kiện. C05 HOLD; cùng major giữ gaze-away tới endpoint lặp từ T01 → STOP, không tự T03.

| Native frame / thời điểm | Quan sát và hệ quả |
| --- | --- |
| F31–47 /1,292–1,958s | Đào đổi mắt/head sang cốc và với tay ngoài; Khoai chưa cầm đũa. Cue nguyên nhân có thực hiện. |
| F60–64 /2,500–2,667s | Cốc bắt đầu rời bàn/nâng rõ; tay ngoài Khoai bắt đầu rời tư thế nghỉ sau đó. Không thấy lỗi anh lấy trước cue cô nâng. |
| F71–81 /2,958–3,375s | Khoai chạm/nắm đúng đôi ngoài trái rồi nhấc rõ ở khoảng F77–81; đầu nhỏ quay về đĩa. Đôi Đào còn nằm bàn, tay trong nghỉ. Không cần kết luận grip giải phẫu hoàn hảo từ ảnh. |
| F95–99 /3,958–4,125s | Đào đưa vành cốc sát môi, môi hé thành khe rõ nguyên khung F99; vượt hành động chỉ nâng nhẹ/môi khép. Hình gợi ý chuẩn bị uống; không chứng minh đã nuốt nước hoặc có tiếng uống. |
| F99–104 /4,125–4,333s | Hai đầu đũa tới/kẹp lát ở mép gần-trái. Phân biệt kẹp trong đống món với lát đã rời đĩa; không gọi đây là pause hoàn tất. |
| F105–107 /4,375–4,458s | Một lát bắt đầu tách/nâng, F107 thấy rõ lát rời đĩa đi về phía Khoai; chưa ăn/chưa chuyển bát Đào. Đào đã có lỗi môi/cốc trước thời điểm này. |
| F112 /4,667s | A đi qua phía bát Khoai, vẫn trên tips, chưa thả; gaze Đào còn hướng trước/cốc. Chưa có endpoint đã giữ yên đủ để dùng làm kết C04, và lỗi môi trước vẫn nằm trong prefix. |
| F113–120 /4,708–5,000s | Mắt Đào bắt đầu về trái rồi nhìn rõ phía Khoai/A; F120 mặt quay theo, cốc hạ khỏi sát môi. Bắt gặp đã lọt vào C04. Khác T01: lần này gaze trở lại sau A rời đĩa, không trước nâng A. |
| F124–143 /5,167–5,958s | A được giữ thấp dưới ngực về phía Khoai, xa miệng; pause cuối đọc được nhưng Đào nhìn anh, không nhìn cốc. Khoai giữ môi khép ở các khung đã xem, khác lỗi miệng mở đuôi T01; không bù được lỗi Đào. |

Số lượng A: nguyên khung cho thấy một lát cong/không đều tại tips; chưa có bằng chứng chắc chắn hai lát hay nhân đôi, nên không thêm major giả. Hướng về mình và không ăn có thể đọc, không phải toàn hành động đều thất bại. Camera chung giữ mặt/đũa/A/bát/cốc đọc được; có nền phố chuyển động, không thấy lý do cứu bằng thay máy/cận món.
EDIT: cắt trước F95 tránh môi/cốc nhưng chưa hoàn thành lấy A; cắt trước F113 có phần nâng A nhưng chứa môi hé từ F95–99 và chưa có pause hợp lệ. Lấy riêng đuôi bỏ nguyên nhân/cue và đã có gaze quay lại. Không crop/freeze/che Đào hoặc bỏ tiếng để ghi PASS hình.
Opening17,583333s còn12,416667s cho C04–09; nguồn6s không mặc định dùng hết. Khi chưa có range hợp lệ, không dùng phép cộng30s hoặc speed để hợp thức hóa T02.
Chẩn đoán hẹp: prompt262 đã viết giữ gaze tới VERY LAST FRAME/no drink/môi khép; lỗi là output không giữ trạng thái xuyên chuỗi, không phải thiếu yêu cầu. Giả thuyết model gắn cốc với uống và gắn tương tác hai người với quay lại còn cần kiểm chứng, không tuyên bố nguyên nhân nội bộ.
Bước tiếp chỉ trình chẩn đoán và phương án dàn cảnh/tuyến sau ngưỡng lặp; chưa có shot mới, script mới hoặc thay voice được duyệt. Giữ cả hai natives và bằng chứng; không lấy endpoint T02 làm ref C05 đã đạt.
Phương án hẹp để owner quyết định: tách C04, cân nhắc prefix T02 `[0,76)` =F0–75/3,166667s làm đổi chú ý–nâng cốc–chuẩn bị lấy đũa trước cốc sát môi; đây là đoạn bộ phận, không C04 PASS. Cảnh tiếp lấy exact F75 làm trạng thái vào để hoàn tất cùng đôi đũa → một A → pause, Đào đã chú ý cốc và phải giữ môi khép/gaze-away. Không reset đũa về bàn hoặc đổi tay để sửa ảnh; hướng mắt/cốc trong F75 vẫn phải review làm input mới.
Tách giảm nhiệm vụ khởi động gaze/cốc trong cảnh gắp, nhưng chưa chứng minh model giữ trạng thái; tăng điểm nối phải kiểm và có thể vẫn lỗi uống/quay lại. Timing:17,583333+3,166667=20,75s, chỉ còn9,25s cho range gắp mới và C05–09; các range chưa biết nên không cam kết30s. Chưa tạo clip/ảnh/prompt mới, chưa mở paid; đây là đề xuất chờ owner, không T03 tự động.
Phương án nghệ thuật A, cũng chỉ đề xuất: owner có thể cho phép Đào đưa cốc gần môi/ý định nhấp (không khẳng định đã uống/nuốt), nhận nhịp bắt gặp bằng gaze trong đuôi T02 **sau** A đã nâng. C05 vào từ gaze đã trở lại, tiếp tục Đào nhìn A→anh và nói N05, không diễn lại lượt quay đầu; Khoai phải nhận ra bị thấy/khựng trước chữa cháy. T02 cuối chưa tự chứng minh nhịp khựng của Khoai, nên không bỏ nhiệm vụ này ở C05.
Tradeoff A: giữ nguyên nhân cô phân tâm trước gắp và chuỗi tranh thủ→bắt gặp→chữa cháy, tận dụng footage, không cần credit C04 mới; đổi boundary bắt gặp từ C05 sang C04, cho ngoại lệ cốc gần môi/môi hé so với spec đã duyệt. Có nguy cơ ánh nhìn đuôi đọc như chỉ nhìn bạn hơn là phát hiện A; cần owner xem chuyển động thực và reviewer kiểm gaze/A rồi điểm nối C05, không suy từ still thành chắc chắn.
So với split giữ spec nhưng thêm nguồn/điểm nối/chi phí và timing chưa biết, A đáng trình trước nếu owner ưu tiên nét hài tự nhiên và tiết kiệm nguồn: A đã rời đĩa trước gaze trở lại nên chưa mất nguyên nhân lõi như T01. Tuy nhiên chỉ hợp lệ sau owner quyết định rõ ba ngoại lệ boundary/cốc/môi và chấp nhận diễn thực; không tự gọi lỗi đạt. Native vẫn NOT_SELECTED, C05 HOLD, timing/range/AV chưa nghiệm thu; không có bảo đảm30s hoặc phép nghe từ báo cáo khung.
