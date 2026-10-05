# EP01 — Kiểm nối cận tay và chuẩn bị chuyển nem vào bát Đào

Ngày 2026-10-05. Chủ dự án đồng ý tiếp tục theo bước đã trình tại 185: làm local, đối soát điểm nối và chuẩn bị khung chuyển–nhận. Không suy “ok làm đi” thành quyền chi thêm hoặc nghiệm thu media.

## 1. Đầu vào hiện hành

- Nội dung C-v0.6 và K20/D06 giữ nguyên; kiểm speaker identity được hoãn, SIA-01 vẫn **HOLD**.
- Bàn ăn T-NB-03_v0.8.jpg được duyệt tại 78 là nguồn vị trí món, rau, hai chấm, hai bát và cốc.
- C01 chỉ được chấp nhận về động tác gắp; chưa duyệt continuity món/điểm nối. Phạm vi dùng trong bản thử: 2,750–5,250 giây.
- V02 của 185 vẫn REWORK toàn take. Đoạn 0–1,750 giây là ứng viên nâng ngắn đã ghi ở 185, không tự chuyển thành PASS.
- Hai ảnh phản ứng Đào của 185 là ảnh tạm, chưa có diễn quay lấy cốc/quay lại.
- Ngân sách theo sổ: đã dùng 232/255, còn **23 credit**. Không đọc Flow live trong lượt này; số dư 194 và giá bộ ba 30 là quan sát trước đó, không phải báo giá mới.

## 2. Đã dựng bản kiểm nối 8 giây

File local: `C:/Users/PC/Downloads/du_an_nem_bui/186_continuity_planning/render_v0.2/EP01_ACTION_JOIN_8s_PLANNING_v0.2.mp4`.

Đây là **JOIN_PROBE_NOT_DELIVERY**, không tiếng, không dùng hoặc sửa audio A03/R01. Không thay bản 30 giây tại 182, không kiểm lại giọng hoặc đổi kịch bản.

| Khoảng trong bản thử | Nguồn / trạng thái |
| --- | --- |
| 0–1,25 giây | Ảnh tạm Đào nhìn cốc; chưa có chuyển động quay đi. |
| 1,25–3,75 giây | C01: đoạn gắp 2,750–5,250 giây, chưa duyệt nối. |
| 3,75–4,50 giây | Thẻ **THIẾU** nhịp đưa nem từ trên đĩa chung về vùng trước bát Khoai. |
| 4,50–6,25 giây | Ứng viên nâng tay V02, không đổi tốc độ. |
| 6,25–7,50 giây | Ảnh tạm Đào nhìn Khoai; chưa có chuyển động bắt gặp. |
| 7,50–8,00 giây | Giữ frame cuối ứng viên V02, chỉ ảnh tạm tay khựng. |

Có 4,25 giây video ứng viên, 3 giây ảnh giữ chỗ và 0,75 giây thẻ thiếu. **Không cộng những con số này thành coverage đã nghiệm thu.** Bản thử chỉ cho xem thứ tự/mạch và các lỗ hổng.

Root đã xem grid 16 khung, khung điểm nối và nhãn ở độ phân giải đầy đủ. Probe: 720×1280, 24 fps, 192 frame, đúng 8 giây, không audio stream; giải mã sạch. Hash hiện hành: `996f250d9e34ac05520495d308678475fba397d4172901f7fde517d9d400965e`. Metadata và nguồn/range tại [manifest v0.2](evidence/186/manifest-v0.2.json).

Bản local v0.1 vẫn giữ nguyên. Khi xem bản đầu, nhận ra dải nhãn đè lên vùng tay của C01; v0.2 thu toàn bộ hình xuống dưới dải nhãn, không che grip hoặc watermark. Đây là sửa layout của bản kiểm, không phải sửa lỗi diễn hoặc làm ảnh mới. [Kiểm layout](evidence/186/label-layout-check-v0.2.png).

Script `scripts/render_ep01_action_join_probe.py` kiểm hash hai video đầu vào, range không vượt source duration, timeline, output và cấm ghi đè thư mục render đã có nội dung. Đã render thực tế, qua py_compile; thử chạy lại vào thư mục v0.2 bị từ chối với exit 2 và hash output không đổi. Đây là kiểm kỹ thuật, không phải agent creative PASS.

## 3. Kết quả đối soát điểm nối

| Điểm nối | Quan sát | Kết luận |
| --- | --- | --- |
| C01 → V02 | C01 kết thúc khi nem còn trên đĩa chung; V02 bắt đầu trên bát Khoai. Góc đũa và kích thước/chi tiết phần nem thay đổi. | Chưa match-on-action; cần nhịp trung gian hoặc nguồn liên tục thống nhất. Không che khoảng thiếu bằng gọi cut đã đạt. |
| V02 → Đào | Hướng nhìn cuối của Đào là sang trái về Khoai, phù hợp trục làm việc. Chưa có động tác quay lại hoặc phản ứng tay của Khoai thật. | Mạch dự kiến đọc được trên ảnh, chưa nghiệm thu diễn. |
| V02 → chuyển–nhận | Nem đang trước áo Khoai; START mới ở trên bát Đào. | Chưa có đường đổi hướng sang bát Đào. Khung mới không tự lấp phần này. |

Không làm một động tác đưa đồ ăn tới miệng ngoài khung rồi lấy phần sau để chữa cháy. Không tua nhanh/crop lỗi hoặc đổi miếng nem đã ăn thành miếng chưa ăn. Không kết luận khác biệt mọi vị trí pixel là lỗi: góc máy thay đổi có thể hợp lý; nhưng sự thay đổi trạng thái món phải có cầu nối được kiểm.

Lưu ý dữ liệu tay: prompt phản ứng 185 gọi tay giữ cốc là “right hand”, nhưng ảnh front-view đặt tay đó ở bên phải khung. Không dùng chữ trong prompt để chứng nhận giải phẫu tay. Gói mới khóa vị trí theo ảnh: tay Khoai cầm đũa ở bên trái khung; tay Đào giữ bát ở bên phải khung. Tay giữ cốc phải rời cốc trước lúc giữ bát; nhịp này chưa có video, không đánh dấu đã hoàn tất.

## 4. Cặp khung chuyển–nhận mới

Dùng skill imagegen tích hợp: ảnh bàn ăn đã duyệt làm nguồn chính, frame V02 thực tế ở 1,708333 giây chỉ hỗ trợ grip/phần nem. END chỉnh từ chính START mới. Giữ mọi bản gốc, lưu asset mới vào workspace và folder của owner.

- [START](../../assets/references/186/START_handoff_v0.1.png): Khoai giữ một phần nem nhỏ trên vùng trong bát Đào; Đào giữ bát, mặt/miệng ngoài khuôn hình.
- [END](../../assets/references/186/END_handoff_v0.1.png): nem nằm trong bát Đào, đầu đũa đã rời món; chưa gắp miếng khác.
- Rau phía trước-trái, đĩa chung ở giữa, hai chấm và cốc vẫn nằm trong bối cảnh bàn ăn. Không tự dọn rau/chấm sang một chỗ khác để tiện diễn.
- Root đã xem actual hai ảnh: đầu to của đũa ở tay, đầu nhỏ hướng bát nhận; không thấy hơi/chữ/miệng hoặc bàn giao vào miệng.
- Đây là **khung đầu vào**, chưa owner canon approval, FOOD/continuity hoặc independent reviewer PASS. Hai ảnh không chứng minh chuyển động release, bảo toàn miếng nem hoặc dynamic anatomy.
- Cặp này chỉ chuẩn bị nhịp **đặt nem xuống bát**, không gồm đường đổi hướng từ mình sang Đào, bát đưa nhận, câu N06/N07, nụ cười hoặc gắp miếng tiếp.

[Prompt ảnh](evidence/186/image-prompts.txt), [prompt video draft chưa gửi](evidence/186/prompt-deposit-DRAFT-NOT-SUBMITTED.txt), [preflight/hash/gate](evidence/186/deposit-input-preflight.json). Không khẳng định giá của imagegen; chi Flow trong lượt này bằng 0.

## 5. Trình tự tiếp tục và điểm cần quyền mới

1. So sánh cảnh gắp/nâng mới với bàn ăn đã duyệt; chọn cầu nối và thống nhất phần nem. Chưa mở Quality.
2. Hoàn thiện chuyển động Đào quay lại và Khoai khựng trên cùng trục; ảnh hiện tại chỉ làm đầu vào.
3. Hoàn thiện đổi hướng → bát nhận → đặt nem, rồi cảnh kết; không biến nhịp đặt nem thành toàn bộ hành động.
4. Đưa coverage đã qua kiểm vào bản planning C-v0.6; khi owner muốn kiểm giọng lại, chạy SIA trên nguồn thật và bản ráp. Trước bàn giao vẫn phải kiểm thoại/môi, diễn, hình/đạo cụ, chữ/nhãn AI và âm thanh.

Còn 23 credit. Nếu giá live vẫn là 30 cho bộ ba Lite, riêng một batch mới cần bổ sung ít nhất 7; **chưa yêu cầu thực thi hoặc tự cấp khoản đó**, và không cam kết một batch đủ hoàn tất mọi cảnh. “Ok” lần này chỉ cho làm bước local/khung tham chiếu đã trình, không tăng trần hoặc giảm số lượt thử.

## Tổng kết vòng

- **Đã xác định:** bản kiểm nối 8 giây có nhãn rõ; điểm nối C01–V02 còn thiếu; hai khung đặt nem xuống bát đã tạo và lưu.
- **Quyết định thực thi:** giữ source/script/giọng, dùng bản planning không tiếng, không che lỗi hoặc gửi thêm paid batch.
- **Giả định:** cận tay và cận phản ứng có thể giữ nhịp bị bắt gặp; đây là hướng làm việc chưa được kiểm bằng diễn liên tục.
- **Còn mở:** nguồn món thống nhất, cầu nối gắp–nâng, phản ứng động, đổi hướng–đưa bát–release, speaker identity và các cảnh thoại/kết.
- **Bước tiếp theo:** chuẩn bị và duyệt gói chuyển động ưu tiên sau đối soát continuity; đọc giá live/kiểm quyền chi trước generation. Ngân sách vẫn 23, chưa Quality/master/publish.
