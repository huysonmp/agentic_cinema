# REC321 — Hoàn thiện từ bản dựng REC312, không làm lại cả phim

Ngày 16-10-2026. Owner hỏi bản gần hoàn thiện nhất ở đâu, sau đó trả lời “uh thế làm đi” cho việc kiểm bản nền và phân loại giữ / sửa bằng dựng / cần sửa nguồn hình. **Đây là kết quả kiểm và kế hoạch sửa có phạm vi, chưa phải một video mới hoặc nghiệm thu bản cuối.**

## 1. Bản nền đã tìm lại và bảo toàn

![Bản dựng đầy đủ REC312 — 35 giây, chưa phải bản cuối](C:/Users/PC/Downloads/du_an_nem_bui/312_EP01_ROUGH35_TRIAL/EP01_ROUGH35_TRIAL_v1_NOT_FINAL_312.mp4)

File gốc: `restart_720p_v1/07_edits/EP01_ROUGH35_TRIAL_v1_NOT_FINAL_312.mp4`. SHA256 `44bd2c591a00f085b8d4c4e4e69c5a25fb9d4f4357e7dbc76263ca068fec1e66`. Đọc lại được 840 khung, 24 fps, 720×1280, 35 giây. Đối chiếu hash cả bảy tệp nguồn theo EDL312: đều khớp. Không sửa nguồn, EDL hoặc lời/giọng; không tạo media bằng AI, không tiêu credit.

REC313–320 là nhánh cải thiện hình ảnh sau phản hồi về khung hình/chuyển cảnh/trọng tâm. Không thay thế hoặc xóa bản nền. C02 cận mới REC320 chưa được ghép vào REC312 và chưa được owner duyệt tiếng/diễn. Các ảnh REC318/319 không phải video còn thiếu bắt buộc phải tạo toàn bộ. Approval hướng quay/ảnh cũ vẫn giữ đúng phạm vi, không bị hủy bởi việc quay lại kiểm bản nền.

## 2. Kiểm gì trong vòng này

- Trích mới 142 khung chọn lọc từ chính bản export312: overview mỗi giây, tám khung quanh mỗi cut, toàn bộ giây cuối. Ảnh bằng chứng thu nhỏ 360×640, không chỉnh mặt, món hay đạo cụ.
- Root đã xem 35 ô overview, bốn ô tại mỗi điểm cắt trong 11 điểm, đủ 24 ô giây cuối. Không nhận đã nhìn từng khung trong cả 142 ảnh hoặc xem chuyển động liên tục.
- Xem bổ sung đủ 28 khung native C04 F116–143 và 24 khung C09 F72–95 để kiểm phần nguồn còn chưa dùng.
- Xem lại hai ảnh món thật owner cung cấp. Nem thật có phần sợi và lát mỏng không đều, phủ thính có hạt; không phải tất cả đều là sợi. Không gọi mọi lát mỏng trong phim là sai, nhưng hình trước/sau cut24s khác rõ về cấu trúc và lượng.
- Đọc lại ASR cũ chỉ để định vị sơ bộ lời, không dùng nó làm mốc âm chính xác hoặc nhận diện người nói. Tái đo PCM phần 29,25–35 giây: 552.000 giá trị mẫu, tất cả bằng 0. Câu subscribe trong ASR đuôi là nhận dạng nhầm, không phải tiếng cần xóa.

Bằng chứng: `restart_720p_v1/06_qc/BASELINE312_AUDIT_321_V2/`. Không có báo cáo reviewer độc lập mới hoặc chứng nhận AV trong lượt này.

## 3. Bản đồ giữ / sửa theo đúng timeline hiện tại

Các mốc dưới thuộc **bản35s gốc**, không phải timeline sửa. “Giữ nền” nghĩa là ưu tiên tái sử dụng, không phải duyệt toàn cảnh hoặc mọi điểm nối.

| Thời gian | Nội dung | Phân loại và việc làm |
| --- | --- | --- |
| 0–3,375s | Đào “Anh nhìn mãi. Không hợp thì để em.” | **Giữ nền.** Người nói hiện mặt và có ý định đưa tay. Giữ tiếng/diễn; không tạo mở đầu mới chỉ để thay phong cách. |
| 3,375–4,125s | Khoai “Khoan” — cận riêng | **Giữ.** Đã có thay cỡ cảnh có mục đích. Không bỏ cận này chỉ vì muốn thống nhất góc. |
| 4,125–6,208s | Trở về khung đôi, Đào dừng/thu tay | **Sửa bằng dựng nếu tìm được biên an toàn.** Đây là hành động có nguyên nhân, không phải 2,083s “rỗng” có thể xóa hết. Ngoại lệ tay chạm vành đã được duyệt ở258 không bị mở lại. |
| 6,208–12,750s | Khoai kể ký ức | **Giữ nguồn cũ làm nền.** Mặt Khoai nhìn được nhưng vẫn cùng khung đôi nên thiếu tương phản. C02 mới320 chỉ là lựa chọn cải thiện một đoạn; chưa được thay tự động hoặc cần sinh thêm để tiếp tục kiểm bản cũ. |
| 12,750–14,500s | Đào hỏi “Anh chờ ăn à?” | **Giữ nền.** Không có bằng chứng bắt buộc tạo reverse-angle mới. Chỉ chỉnh khoảng nghỉ sau kiểm tiếng/miệng trên bản dựng thử. |
| 14,500–16,583s | Khoai “Chờ mẹ quay lưng” | **Giữ nền.** Có thay đổi mặt/ánh mắt ở cut cùng góc; có thể tìm biên khác, chưa đủ cơ sở gọi bắt buộc thay take. |
| 16,583–21,250s | Đào nhìn sang cốc, Khoai tranh thủ gắp A | **Giữ chuỗi hành động.** Không cắt mất cơ hội gắp để rút thời lượng. Cut hiện ra tại C04 F123; nguồn còn F124–143. Có thể thử lại biên, nhưng thêm20F không tự sửa được mọi lệch mắt/mặt hoặc món. |
| 21,250–24,000s | Đào trêu “Chờ em quay lưng nữa à?” | **Giữ tiếng/diễn làm nền.** Kiểm nhịp phản ứng trước câu và phần đuôi sau câu; không tự xóa đuôi vì ASR báo lời kết thúc sớm hơn. |
| 24,000–29,000s | Khoai chữa cháy → Đào đưa bát | **Giữ block308 làm nền; điểm vào24s cần sửa hình/nguồn.** Nem trên đĩa và phần kẹp đổi rõ giữa F575/F576; còn thay đổi mặt/ánh mắt. Không che bằng dissolve, insert món hoặc crop mất mặt. Nội bộ26s vẫn phải kiểm nhịp/miệng, nhưng chưa thấy reset đạo cụ lớn ở bốn mẫu quanh cut. |
| 29,000–31,667s | A vào bát riêng Đào, đũa rút | **Giữ hành động.** Không cần tạo thêm cận nem cho đẹp; nguồn hiện có đã cho thấy quan hệ đũa–bát. Chưa coi các ảnh mẫu là kiểm mọi tiếp xúc trong chuyển động. |
| 31,667–35,000s | Khoai lấy B mới, hai người nhìn nhau | **Giữ hành động; thử trả phần đuôi còn sẵn.** Range hiện [8,88), nguồn có96F. Thêm F88–95 giúp ánh nhìn cuối từ8F lên16F, tức0,333→0,667s. Không kéo thành1,5s bằng freeze/loop và gọi là diễn tự nhiên. Ngoại lệ đặt cốc/hai tay ôm bát chỉ được duyệt dựng thử, chưa tự trở thành final approval. |

## 4. Mười một điểm cắt: lỗi nào thuộc dựng, lỗi nào thuộc nguồn

| Cut trên bản gốc | Quan sát ảnh trước/sau | Hướng xử lý |
| --- | --- | --- |
| 3,375s / F81 | Khung đôi → cận Khoai, câu “Khoan” có chủ thể rõ | Giữ mục đích cắt; kiểm âm đầu/cuối trên bản thực, không coi đổi cỡ cảnh là lỗi. |
| 4,125s / F99 | Cận → khung đôi; tay Đào vẫn ở khu vực đĩa rồi thu | Giữ phản ứng có nguyên nhân; chỉ tìm lại điểm cắt nếu rõ ràng hơn. |
| 6,208s / F149 | Cùng khung đôi, mặt/ánh mắt thay đổi nhỏ ở biên | Ưu tiên xử lý bằng chọn biên; không mặc định sinh lại C02. |
| 12,750s / F306 | Cùng bố cục; đổi lượt Khoai → Đào | Bảo vệ đối đáp và đủ âm cuối, không thêm cảnh đĩa phủ câu hỏi. |
| 14,500s / F348 | Cùng góc, nét mặt/ánh mắt Khoai đổi | Kiểm biên dựng; không cố làm mượt bằng chuyển cảnh mờ chồng hai mặt. |
| 16,583s / F398 | Cùng bàn nhưng tư thế/mặt đầu chuỗi hành động khác câu đáp | Tìm điểm nối theo ánh nhìn, giữ cốc còn trên bàn trước khi nhấc. |
| 21,250s / F510 | Khoai từ nhìn xuống sang phía Đào; mặt Đào và cốc có thay đổi | Thử biên nativeC04/C05 có sẵn, không mặc định F143 là khung nối hoàn hảo. |
| **24,000s / F576** | **Đĩa và A đổi cấu trúc/lượng rõ rệt, cùng với redraw mặt** | **Chặn khóa hình. Phải sửa/đổi nguồn tại đây hoặc có quyết định chất lượng minh bạch; chỉ cắt không làm hai trạng thái thành cùng món.** |
| 26,000s / F624 | Hai nửa block308, bố cục và trạng thái còn tương ứng ở mẫu | Giữ block đối chứng, kiểm khẩu hình/nhịp trên đoạn xuất thực. Không có lý do tạo lại chỉ từ việc tồn tại cut. |
| 29,000s / F696 | Đào đã đưa bát; đầu chuỗi thả có trạng thái tương ứng | Giữ chuỗi cho–nhận; không lặp hành động thả ở cut. |
| 31,667s / F760 | A trong bát, đũa trống tiếp tục về phía Khoai; có bước đổi góc nhẹ | Giữ pickupB; thử biên trong nguồn trước, không dùng freeze che tay. |

## 5. Kết luận về “buộc làm mới”

**Chưa có bằng chứng buộc sản xuất lại toàn tập, cũng chưa chứng minh tất cả lỗi đều sửa được chỉ bằng dựng.** Vị trí chắc chắn cần xử lý hình là cut24s. Trước khi đề xuất sinh mới, cần đối chiếu các takeC06/food-edit đang có; không lấy một take từng bị loại về diễn hoặc thả sai làm đạt chỉ vì món gần hơn. Chưa kiểm lại toàn bộ các take đó trong vòng321, nên chưa chọn thay thế hoặc hứa ghép được tiếng cũ lên miệng mới.

Vấn đề thẩm mỹ món trong các cảnh cũ vẫn mở khi so với ảnh thật; sửa riêng điểm24s không chứng nhận mọi đĩa nem trong phim đúng. Việc ưu tiên hoàn thiện từ312 không phải một waiver chất lượng món hoặc thu hồi phản hồi đạo diễn trước đó.

## 6. Rút về30s: phải thử bằng nguồn thật, chưa được gọi là xong

35→30s cần bỏ120F. Nếu đồng thời trả20F cho cuốiC04 và8F cho kết, cần bù148F/~6,167s ở chỗ khác; không thể coi việc khôi phục các đuôi là miễn thời lượng. Hai handle này chỉ là lựa chọn kiểm, chưa được chèn vào timeline mới.

Ưu tiên khảo sát khoảng nghỉ sau “Khoan”, biên C02/C03 và đuôi C05; bảo vệ đủ lời, thu tay, cơ hội gắp, một lần thảA và pickupB. ASR không là forced alignment: riêng N01 ước lượng còn vắt qua cutF81, nên tuyệt đối không cắt lời theo số ASR một cách máy móc. Chưa có120F được chứng minh an toàn để bỏ; chưa tạo hoặc duyệt EDL30. Không tự đổi mục tiêu final thành35s và không tự tăng tốc lời/hành động.

## 7. Thứ tự sửa tiếp — không mở lại dự án

1. Giữ312 làm bản nền và các tệp nguồn nguyên vẹn; nhánh320 để riêng, không làm gate bắt buộc cho mọi công việc khác.
2. Làm bản thử cắt/điểm nối bằng nguồn có sẵn: mở đầu, C03B→C04→C05 và phần đuôi kết. Mỗi thay đổi phải lưu range, đo đủ lời và kiểm chuyển động thực; không được chỉ dựa board ảnh để báo đã mượt.
3. Đối chiếu các take/food-edit có sẵn tại cut24s. Nếu không có phương án đạt, mới trình đúng đoạn cần sửa và chi phí; không mở lại cả chín nhịp hoặc tiếp tục tạo ảnh hàng loạt.
4. Ghép bản thử toàn phim, kiểm nhịp/miệng/đạo cụ/âm cuối; chỉ chốt30s khi actual export đạt. Nếu giới hạn30s mâu thuẫn với giữ lời/hành động, báo trade-off cụ thể thay vì cắt ép.
5. Sau khóa hình mới làm mix, phụ đề, nhãn món/địa phương và thông tin AI, rồi kiểm finalexport trước bàn giao. Chưa đăng hoặc release.

### Tổng hợp

- **Đã xác định:** bản312 đủ câu chuyện; các nguồn còn nguyên, các điểm cần sửa đã gắn timecode; có20F C04 và8F kết chưa dùng.
- **Quyết định hiện hành:** owner cho kiểm/hoàn thiện từ bản nền, không yêu cầu tạo lại cả phim. Không có approval mới cho nguồn hình, nhịp, tiếng hoặc bản cuối.
- **Giả định làm việc:** giữ phần dùng được giúp giới hạn phạm vi sửa; không phải giả định mọi take cũ đã đạt whole-film quality.
- **Còn mở:** cut24s/chất liệu món, actual motion/AV, nhịp kết, range30s, finishing và finalapproval.
- **Bước tiếp:** bản thử dựng có giới hạn và đối chiếu take sẵn có; không sinh thêm hoặc tiêu credit trong vòng321.

Ngân sách không đổi so sổ320:291/500 đã chi, còn209 = tạo mới66 + tạo lại0 + coverage33 + dự phòng110 đóng. Không refresh số dư Flow trong vòng kiểm local này.

Công cụ: FFmpeg/Pillow/runtime sẵn có, không cài hoặc gọi API. Lệnh trích đầu gặp giới hạn độ sâu biểu thức FFmpeg, dừng trước khi có ảnh; giữ folder dở dang riêng, rút gọn selector rồi chạy thành công vào `_V2`, không sửa file nguồn hoặc ghi đè evidence. Prompt/reference/media cũ không thay đổi.
