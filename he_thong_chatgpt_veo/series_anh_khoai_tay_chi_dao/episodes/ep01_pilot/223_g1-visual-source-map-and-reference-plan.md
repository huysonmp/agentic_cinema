# 223 — Chuẩn hình EP01 và bộ khung R01–R09

Ngày 2026-10-07. `ANCHOR_A_APPROVED / G1_SOURCE_SCREENING_COMPLETE / REFERENCE_FRAMES_PENDING / NOT_RELEASE`.

## 1. Quyết định A đã khóa

Owner trả lời **“a”** cho lựa chọn tại222: lấy đúng N02 B làm chuẩn hình nhân vật/ánh sáng/nền quán/hình thái ụ món cho riêng EP01. Không đổi canon toàn series, giọng K20/D06, lời C-v0.6, storyboard214, quan hệ bạn bè hoặc đường hành động. [Hồ sơ quyết định](evidence/223/anchor-decision.json) gắn exact native SHA256 `660f1757…7f31a535`.

Giữ bộ phục vụ: rau trước-trái, hai đĩa chấm, hai bát cá nhân, đũa nghỉ trước khi gắp, cốc ngoài phải Đào. Khi Khoai cầm đũa, đôi đũa ấy không còn nằm trên bàn; đó là đổi trạng thái có nguyên nhân, không phải vật biến mất. Món nguội, không khói. A là miếng đầu cho vào bát Đào; B là miếng khác Khoai tự gắp sau đó. **B của tên video N02 khác B của miếng nem.**

N02 B đã được owner chấp nhận về tiếng/lời/nhịp/khẩu hình và return7s tại222. Không hỏi lại các quyết định này hoặc giữ câu hỏi variation B–TABLE08 cũ làm blocker. Các cảnh và điểm nối khác vẫn cần kiểm riêng.

## 2. Đã kiểm dữ liệu và chuẩn bị hình thật

Root chạy `scripts/prepare_ep01_g1_visual_evidence.py`: rehash/probe8native, trích **96 ảnh đúng nativeframe n/24**, không resample thời gian. Đã trực tiếp xem cả8boards; nguồn trước/sau không đổi. Bao gồm clip thả207 chưa được kiểm mới ở215. Không dùng lại timestamp board215 làm range dựng.

- Folder nguồn/ảnh: `C:/Users/PC/Downloads/du_an_nem_bui/223_g1_source_frames/`.
- [Manifest nguồn](evidence/223/source-frames.json):8hashes,96ảnh/hash/nativeframe/PTS/probe.
- Folder9thẻ: `C:/Users/PC/Downloads/du_an_nem_bui/223_g1_nine_cards_v02/`.
- [Manifest thẻ v0.1](evidence/223/card-manifest.json) giữ lịch sử bản nhãn đầu; [v0.2](evidence/223/card-manifest-v02.json) chỉnh nhãn tiếng Việt/thời gian, cùng 9 native frames, không sửa nội dung nguồn.

Bộ ảnh dưới là **bản rà soát nguồn**, không phải9ảnh sản xuất đã duyệt. Nhãn thoại là nhiệm vụ mong muốn, không xác nhận lời thực sự đang được nói ở ảnh đó. F0–F4 là trạng thái cần có của khung; các thẻ đỏ cố ý chỉ ra ảnh hiện có **chưa đáp ứng** trạng thái ấy.

- Xanh: N02 được owner chấp nhận đúng phạm vi, không full-film PASS.
- Vàng: ảnh ứng viên/tham khảo, chưa footage đạt hoặc head/tail được chọn.
- Đỏ: thiếu trạng thái/hành động cần thiết, không đưa nguyên ảnh vào sản xuất.

![R01–R09 — nguồn thật và phần thiếu, chưa là storyboard production](C:/Users/PC/Downloads/du_an_nem_bui/223_g1_nine_cards_v02/G1_NINE_CARDS_DIAGNOSTIC_NOT_APPROVED.png)

Root tạo và xem lại v0.1/v0.2; v0.2 có nhãn tiếng Việt và nativeframe/time. Hai bản được giữ riêng, không ghi đè evidence. Không sinh ảnh AI/video, không chi credit, không chỉnh hoặc xóa nguồn.

## 3. Bảng thiết kế khung cần đạt — không đổi câu chuyện214

| Khung | Nội dung và người nói | Đầu → cuối cần thấy | Nguồn đã kiểm / việc còn thiếu |
|---|---|---|---|
| R01 | Đào: “Anh nhìn mãi. Không hợp thì để em.”; Khoai: “Khoan.” | Hai mặt/F0 → tay Đào định kéo đĩa, nghe Khoai và dừng; đĩa/món chưa bị thay vị trí khi vào N02 | A02f12 có hai mặt/bộ bàn gần B, nhưng chỉ tay nghỉ. Cần ảnh/tư thế và footage cho định kéo–dừng; không lấy đầu N02 làm giả Đào nói |
| R02 | Khoai: “Mùi này làm anh nhớ đến bếp nhà anh. Hồi bé, mẹ rang gạo, anh đứng chờ.” | F0, mặt/miệng Khoai, Đào nghe → trở về hai người; cùng bàn, chưa gắp | N02 B nguyên bản đã chọn; thẻf120/5s chỉ minh họa cận. Không coi5s là điểm đầu câu hoặc tự cắt tiếng. Gaze và điểm nối N01/N03 còn kiểm khi ghép |
| R03 | Đào: “Anh chờ ăn à?”; Khoai: “Chờ mẹ quay lưng.” | F0 sau ký ức → hỏi/đáp và nhịp cô hiểu, chưa lấy cốc/gắp | A02f144 có pose gần B; A03 là nguồn tiếng N03/N04 trong202 nhưng hình thiếu bộ phục vụ/có chữ. Cần đối soát hoặc làm hình đúng B; không overlay tiếng lên mouth chưa kiểm |
| R04 | Không thêm lời; Đào lấy cốc, Khoai tranh thủ | Cô chuyển chú ý → A rời đĩa → về phía miệng Khoai, chưa chạm |163f24 cho pose cốc/A gần miệng; mẫu đầu đã giữ A. Thiếu chứng minh lấy từ đĩa và thứ tự cô quay đi trước. Cần khung chung đủ mặt/cốc/đường A |
| R05 | Đào: “Chờ em quay lưng nữa à?” | A còn kẹp → cô nhìn A rồi anh → anh biết bị thấy và khựng |163f96 là ứng viên low-hold, không đủ chuỗi caught;194 chỉ cận Đào/cốc, không thấy A/mặt Khoai. Cần pose và chuyển động có quan hệ hai người, đúng miệng Đào |
| R06 | Khoai: “Anh gắp cho em mà.” | F2 A còn kẹp sau bị thấy → đổi hướng về bát Đào |154f72 có mặt Khoai nhưng tay nghỉ/F0, không có A. Phải có cả mặt nói và đường đổi hướng; không lấy cận tay207 phủ toàn câu |
| R07 | Đào: “Thế em quay lại đúng lúc rồi.” | F3 cô nhìn A/anh, hiểu → đưa bát trống nhận, A vẫn kẹp |154f120 chỉ nói/nhìn nhau, không A/bát nhận.209 bát đã có món là F4, không dùng làm đầu R07. Cần tư thế nhận với mặt Đào/miệng đúng lời |
| R08 | Không thêm lời; A vào bát | A còn trên đũa trên bát → thả đúng một lần → đũa rời, A trong bát |207f0/48/96 là chuỗi pose trước/trong/sau đặt. Chỉ ứng viên insert cho R08, không proof chuyển động hoặc cùng A qua join; bát/tay/ánh sáng khác B cần match. Gộp vào R07 nếu khung chung làm rõ đủ |
| R09 | Không thêm lời; hai người cùng hiểu, Khoai gắp B | A vẫn ở bát Đào → B mới rời đĩa về phía Khoai, không quay sang cho Đào lần nữa |209f48 minh họa gắp từ đĩa; các mẫu cuối hướng miếng về phía Đào, chưa đạt tự gắp cho mình. Cần nguồn/pose đường B đúng; không dùng154 với hai bát trống để reset kết |

Các frame/time trên là tọa độ **nguồn**, không thời gian trong phim30s. Chín nhiệm vụ không mặc định chín video sinh mới. Không dùng ảnh sai trạng thái ở thẻ đỏ làm head/tail chỉ để đủ bộ.

## 4. Phản biện và thứ tự xử lý

[CONT độc lập](evidence/223/02_g1-cont-source-review.md) đã thực xem96mẫu+22fullframes và rehash8native/96JPEG; root đọc toàn bộ. Kết luận khớp phạm vi:

- A02 gần chuẩn B hơn về F0; chưa có kéo–dừng hoặc đối soát lời–miệng/range.
- A03 không tái dùng nguyên hình do thiếu serving set/garnish/outfit/chữ; nguồn tiếng vẫn xét riêng theo provenance202/owner203.
-163/194 chỉ tham khảo pose, chưa chứng minh toàn chuỗi ăn vụng/bị thấy.
-154 là F0, không thay trạng thái A đang kẹp hoặc bát đã nhận A.
-207 chỉ có tiềm năng insert R08; không dùng để bỏ mặt trong R06/R07. Bát lốm đốm/tay/texture cần match chuẩn B.
-209 có pose sau trao/gắp mới, nhưng đường B về Khoai chưa chứng minh; không nhận trọn8s là kết đạt.

[Maker EDIT/DLG](evidence/223/01_g1-shot-plan-maker.md) đã lập bản đồ 9 nhiệm vụ, đầu/cuối khung và thứ tự phụ thuộc; root đã đọc đầy đủ bản cuối sau correction C1. Maker ban đầu ghi frame0 của209 có miếng trên đũa. Root mở ảnh full-size, yêu cầu kiểm lại; maker xác nhận **đũa trông trống, bát Đào có nem**, phù hợp CONT. Đã sửa mô tả ảnh; vẫn chưa đóng đường A/B qua join hoặc chuyển động. Hai context maker/reviewer độc lập, không biến báo cáo giấy hoặc ảnh mẫu thành nghe/xem liên tục. Bộ G1 hoàn chỉnh còn thiếu ảnh đúng nhiệm vụ và bản dựng thử; đây chưa là checkpoint để owner duyệt production.

Thứ tự: **khóa bộ mở R01 → N02 B → R03**, sau đó khung chung R04–R07, điểm thả R08 và kết R09. Các nguồn hành động có thể được kiểm thiết kế song song; không sản xuất hàng loạt trước khi đủ đầu vào. Face, tay, cốc và A/bát phải được kiểm cùng cảnh, không sửa từng đạo cụ rời.

## 5. Gói khung mới đầu tiên — đề xuất, chưa chạy

Đề xuất chuẩn bị **4 ảnh tham chiếu mở cảnh** trong Flow, cùng bố cục hai người của B:

| Mã ảnh | Trạng thái cần tạo | Vai trò / không được suy thành |
|---|---|---|
| REF01-S | Hai người/F0, Đào muốn ăn, hai tay ở vị trí nghỉ; môi khép | Khung mở R01; không có thoại/khẩu hình đã nghiệm thu |
| REF01-M | Đào đưa một tay về gần mép đĩa, ý định định kéo; Khoai nhìn cô | Pose giữa R01; đĩa còn đúng vị trí, không tự thêm gắp hoặc ăn |
| REF01-E | Đào đã dừng ý định, tay trở về vị trí khớp đầu N02 B; hai người/F0 | Neo nối N02; ảnh riêng không chứng minh cô đã nghe “Khoan” hoặc chuyển tay mượt |
| REF03-S | Sau ý ký ức, Đào nhìn Khoai tò mò; hai tay nghỉ, chưa chạm cốc; F0 | Neo R03 hỏi/đáp; không dùng bát đã nhận nem hoặc cốc đang cầm |

Nguồn dự kiến tải lên đúng project Flow `9276788e-9781-44fb-ba5b-083006667374`: JPEG trích **ANCHOR_Bf175/7,291667s** trong gói223 (hai mặt/miệng khép), chỉ dùng nhận diện/bàn/nền. Pose môi khép này không xác nhận speech-end. Không đưa các hình nền/bát khác nhau A03/163/207 vào cùng request để model trộn chuẩn. Mỗi ảnh có brief riêng, không prompt gộp cả chuỗi nhiều hành động.

Phạm vi đề xuất xin duyệt: tối đa4ảnh, một lượt/ảnh, chỉ tạo ảnh và review; **trần chi0credit**. Root phải kiểm UI/route/giá hiện hành trước gửi từng request. Nếu không xác nhận được0credit hoặc giá>0: dừng trước submit, trình lại. Không tạo video/Quality/voice mới hoặc tự retry. Approval nếu có là quyền tạo ảnh ứng viên, không duyệt đầu ra.

Gói này chưa được chạy/kiểm quote trong 223; [request draft](evidence/223/reference-request-draft.json) ghi nguồn exact hash và điều kiện dừng. Không tuyên bố ảnh Flow hiện miễn phí từ lịch sử trước. Sau ảnh đạt kiểm hình B/bộ phục vụ/tư thế, tích hợp vào G1 và tiếp khung hành động; production video vẫn phải có brief/quote/approval riêng.

Đã viết bốn prompt DRAFT theo từng tư thế: [REF01-S](evidence/223/REF01-S.prompt-DRAFT.txt), [REF01-M](evidence/223/REF01-M.prompt-DRAFT.txt), [REF01-E](evidence/223/REF01-E.prompt-DRAFT.txt), [REF03-S](evidence/223/REF03-S.prompt-DRAFT.txt). Dùng cùng nguồn Bf175; không thêm voice, chữ hoặc ảnh chuẩn mâu thuẫn. Prompt giữ plate tại chỗ, miệng khép, tay/người nghe đúng state. Các ảnh sẽ chỉ là ứng viên pose, không thay actual diễn/kéo–dừng/khẩu hình.

## 6. Thời gian và tiếng: chưa dựng master

WAV202 vẫn giữ tiếngN02 cũ200, không tự trở thành soundtrack của N02B mới. Khi đề xuất thay phải lấy đúng audio giải mã từ B và đối soát lại bản nối, không giả waveform200=221B. N01/N03/N04/cụmN05–N07 vẫn theo nguồn202/approval203 trong phạm vi source; các source hình còn phải kiểm khác.

Metadata cũ202 là22,055s, B audio221 là10,005s. Dù số giây N02 cũ/mới bằng nhau, chưa chứng minh điểm cắt, khoảng nghỉ hoặc toàn30s vừa hành động. Không dùng7,945s còn lại làm vùng im lặng cố định, không bịa mốc N05/N06/N07 riêng, không time-stretch để vừa. Không tạo bản ghép audio/video mới trong223.

## 7. Tổng hợp vòng

- **Đã xác định:** chuẩn B đã được owner chọn cho EP01; 8 nguồn/96 ảnh exact được kiểm, 9 thẻ nguồn thật dựng và xem lại; đã đọc maker EDIT bản cuối và CONT độc lập. Đã sửa mô tả sai frame đầu209 trong báo cáo maker.
- **Đã chốt:** A tại222, B cho N02, thoại/giọng/quan hệ/F0–F4/đường A→bát→B giữ. Không có quyền chi/generation mới.
- **Giả định làm việc:** ảnh nguồn dùng để sàng lọc/thiết kế, không giả cảnh đã diễn;4ảnh đầu là đơn vị đề xuất để khóa phần mở trước.
- **Còn mở:** quyền gói4ảnh, quote0 thực, ảnh head/mid/tail đúng B, actual lời–hình các lượt còn lại, causal motion, joins và30s.
- **Tiếp:** hoàn tất maker read-back; owner duyệt hoặc sửa gói4ảnh → root kiểm Flow trước gửi. Không yêu cầu owner tự chuẩn bị khung và không xin duyệt các thẻ đỏ như ảnh đã đạt.
