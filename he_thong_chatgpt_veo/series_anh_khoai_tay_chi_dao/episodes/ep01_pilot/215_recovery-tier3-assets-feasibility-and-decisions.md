# 215 — Tầng 3: tài nguyên, khả thi và quyết định còn thiếu

Trạng thái: TIER3_OWNER_CHOICES_RECORDED / LOCAL_SCREENING_COMPLETE / NO_PRODUCTION_READINESS_CLAIM. Owner duyệt storyboard 214 sau câu hỏi xác nhận phạm vi; không cấp ngân sách sinh mới. Lượt này không network, không generation, không cài công cụ và không sửa media nguồn.

## Cách kiểm thực tế và giới hạn

Chạy `scripts/inventory_ep01_recovery_assets.py --out C:/Users/PC/Downloads/du_an_nem_bui/215_recovery_asset_screening`.

- Đếm 289 file MP4 và 87 WAV trong folder owner. Không phải 289 take gốc khác nhau; có bản sao, bản dựng thử và các gói bàn giao.
- Probe và trích bảng 12 ảnh/clip từ 12 ứng viên; root đã xem cả 12 bảng, tổng 144 ảnh lấy mẫu. Đây là kiểm sàng lọc bố cục/trạng thái, không phải xem chuyển động hoặc nghe liên tục toàn clip.
- SHA-256 trước/sau mỗi ứng viên khớp; bản audio 202 tồn tại, hash khớp manifest nguồn, probe xác nhận 22,055 giây.
- Xem ảnh tham chiếu `T2-CODEX-OPEN_v0.7.png` và đối chiếu mặt, trang phục, vị trí, rau/chấm/cốc/bát. Ảnh này là tham chiếu diagnostic trong lịch sử, không tự nâng thành canon mới hoặc đủ toàn bộ trạng thái R01–R09.
- Đọc lịch sử 154/169/200/201/202/210, manifest 202, ASR 201 và requirements/công cụ local. Không dùng trạng thái cũ chưa cập nhật trong manifest để phủ định approval audio 203.

Dữ liệu/file paths/probe/hash: `C:/Users/PC/Downloads/du_an_nem_bui/215_recovery_asset_screening/inventory.json`. Không dùng contact sheet để ghi lip-sync, voice hoặc ACT PASS.

## Tài nguyên đã xác minh

### Audio

Ứng viên nguồn chính: `202_dialogue_join_review/EP01_7_LUOT_N02_MOI_REVIEW_NOT_FINAL.wav`.

- SHA-256: `3c83b7d6188f5b973b0ef5c77ebc1fc16afde7c11827764c5302145741b736d4`.
- PCM 16-bit/48 kHz/stereo, 22,055 giây; đủ bảy lượt theo source map. N02 từ nguồn single-speaker 200/201, không dùng lại N02 lỗi trong A03.
- Có lịch sử owner nghe duyệt toàn N02 tại 201 và bản nối bảy lượt tại 203. Root không nhận đã nghe mới trong 215.
- 30 − 22,055 = 7,945 giây ngoài độ dài file audio này. Không coi đó là nhịp hành động đã đạt; action có thể diễn cùng lời, file có khoảng nghỉ/đuôi cần kiểm riêng.
- Audio không tự bảo đảm cảnh hình tương ứng hoặc khẩu hình khớp. Không bắt buộc thu lại chỉ vì sửa dựng.

### Hình tham chiếu

OPEN_v0.7 hiện có mặt hai người, đúng vị trí trái/phải, trang phục và bàn có rau/chấm/bát/cốc. Các cặp tham chiếu 185/187/189 và 195/198/208 cũng tồn tại trong repo; nhiều cặp được chuẩn bị cho cận tay/không mặt, nên sự tồn tại không làm chúng phù hợp storyboard mới. Cần chọn/sửa bộ tham chiếu theo từng trạng thái F0–F4, không tái dùng tất cả mặc định.

## Ma trận sơ bộ theo storyboard

| Khung | Ứng viên và bằng chứng đã kiểm | Kết luận sàng lọc / khoảng thiếu |
|---|---|---|
| R01 | 180 A01/A02/A03 có hai mặt; A03 là nguồn audio N01 | A01 biến hình món; A03 thiếu các đạo cụ bàn và có chữ trong một số mẫu; A02 gần bố cục bàn hơn. Chưa chứng minh động tác kéo–dừng đĩa và đúng miệng/câu. Không có clip R01 được nghiệm thu mới. |
| R02 | 200 N02_NATIVE có khung hai mặt và cận Khoai nói; audio chính là nguồn N02 đã duyệt | Có tiềm năng tái dùng một phần. Nhưng clip tự chuyển sang món khoảng vùng mẫu 6,67–7,50 giây rồi trở lại hai người; không đáp ứng trọn cận Khoai theo R02. Chưa đo điểm cắt hoặc lip-sync từng từ, không ghép toàn clip mặc định. |
| R03 | 180 A01/A02/A03 chứa hai mặt; audio N03/N04 đã trích từ A03 | Kiểm theo đúng hai lượt, không dùng N02 lỗi nằm trước đó. Sàng lọc cho thấy các vấn đề món/đạo cụ/chữ và người mở miệng cần đối chiếu. 175 B03 đổi trang phục Khoai và có món/đạo cụ khác, không dùng nguyên cảnh. |
| R04 | 160 N01/N02/N03 và 163 R02 có mặt, nem trên đũa hướng về Khoai | Mẫu bắt đầu đã có A trên đũa; chưa chứng minh gắp từ P, Đào quay lấy cốc rồi bắt gặp đúng thứ tự. Một số mẫu có miệng mở gần A và Đào chưa quay đi rõ. Không gọi nguồn trọn R04 hoặc khẳng định tiếp xúc miệng chỉ từ ảnh mẫu. |
| R05 | 194 R203 có cận Đào và cốc; 163 R02 có hai người với A | Không một mẫu sàng lọc nào chứng minh đủ A → ánh nhìn bắt gặp → Khoai khựng và N05 đúng miệng. R203 có các mẫu miệng mở trong đoạn dự kiến im lặng; chưa hợp lệ khi phủ audio khác. Phản ứng riêng không thay toàn cảnh bị phát hiện. |
| R06/R07 | 154 R01 có mặt hai người và nguồn ba câu cuối đã duyệt | Trong 12 ảnh, tay nghỉ trên bàn; không có trạng thái A trên đũa/đổi hướng/Đào đưa bát nhận như storyboard. Có thể nghiên cứu tái dùng lời/biểu cảm, chưa đủ nhiệm vụ hành động. Các đoạn U04/U06/U07 bản 209 không mặt nên không thay cảnh nói thấy mặt. |
| R08 | 207 U07 có lịch sử clip đặt nem trong timeline 209 | 215 chưa kiểm mới clip này; lịch sử có bát xê dịch. Chỉ là ứng viên insert theo continuity, không nhận PASS mới hoặc dùng để bỏ cảnh chữa cháy có mặt. |
| R09 | 209 U08_NATIVE có hai mặt, bát Đào có món và Khoai gắp | 12 mẫu cho thấy bát có món và đường đũa hướng về đĩa/rồi nâng; có tiềm năng dùng đoạn kết. Chưa chốt range/join với A thả ở R08; không dùng nguyên 8 giây hoặc mặc định đoạn 209 cũ là đúng nối mới. |

Kết luận đúng phạm vi: chưa có bộ footage được chứng minh đáp ứng toàn bộ R01–R09. Điều đó không đồng nghĩa đã xem và loại mọi file trong 289 MP4. Phần cần làm mới chỉ được chốt sau kiểm đoạn ứng viên sâu hơn và bản dựng thử.

## Điểm nghẽn cần phép chứng minh, không chỉ sửa prompt

1. Cảnh nói thấy mặt phải giữ đúng giọng/lời/khẩu hình với N02 dài; nguồn 200 cho thấy làm được một phần trên hình, chưa chứng minh trọn cảnh theo storyboard.
2. Chuỗi nhiều trạng thái mặt–tay–đũa–A–bát: cần chứng minh ý định, phát hiện, đổi hướng và thả. Không có căn cứ một clip nhiều hành động sẽ làm đúng toàn bộ hoặc một loạt insert sẽ giữ liên tục.
3. Giữ bản thoại/giọng được duyệt và cảnh đẹp cùng lúc. Tuyến trong hồ sơ 200/154 là Omni 1.1 Flash với voice tùy chỉnh; các cảnh tay dùng Veo Lite. Không gọi tất cả là một tuyến Veo đã chứng minh gắn voice/khẩu hình. Tính năng và giá hiện tại chưa được kiểm live.

## Bộ công cụ hiện có và phần thiếu

- FFmpeg/FFprobe verified 9.0.2 đang chạy được: đọc metadata/hash, trích ảnh, tách âm, dựng thử/cắt frame và đo âm lượng. Đây là kiểm kỹ thuật, không phải hiểu diễn xuất.
- Venv có numpy, faster_whisper, av, onnxruntime; script ASR local không prompt mồi, hỗ trợ cache offline. Lượt 215 chỉ kiểm module tồn tại và đọc ASR cũ; không báo một lần ASR/kiểm nghe mới đã chạy.
- Root xem được ảnh local. Chưa chứng minh khả năng nghe giọng/diễn xuất trực tiếp hoặc xem video liên tục trong lượt này. Muốn nghiệm thu giọng/khẩu hình cần bố trí kênh kiểm thực, không ghi agent đã nghe chỉ vì có transcript.
- Chưa kiểm được một tuyến lip-sync độc lập nhận WAV duyệt và bảo toàn hai tạo hình/biểu cảm. Không hứa pipeline này đã có, không cài/upload/API mới trong lượt này.
- Bộ công cụ chưa đủ để gọi production ready. Tầng 4 phải phân quyền kiểm thực, reviewer và bằng chứng theo phiên bản.

## Ngân sách: số dư không đồng nghĩa quyền chi

210 ghi sổ chi 419/422, còn 3 credit được phép, số dư tài khoản Flow 57 từ lần kiểm 209. Đây là ghi chú lịch sử, không xác nhận số dư live hiện tại. 215 không kiểm UI/account hoặc quote; không lấy 57 làm ngân sách được phép và không dùng cap cũ 200/100 như khoản mới.

Một phép thử mới cần đọc quote hiện hành và quyền chi rõ. Các quyết định 212–214 chỉ mở discovery/storyboard, không cấp paid generation. Không xin một con số dự toán tổng khi số clip thiếu/route chưa được chứng minh.

## Tầng 3 — bốn câu hỏi cần owner chốt

### Q1. Tái dùng hình tới mức nào?

- A: tái dùng chọn lọc nếu qua kiểm đúng nhiệm vụ cảnh, continuity và thoại–miệng; phần thiếu mới làm. Khuyến nghị sơ bộ; tiết kiệm công nhưng không được giữ clip chỉ vì đã tốn credit.
- B: làm mới phần hình R01–R09 từ bộ tham chiếu thống nhất; giữ audio nếu phù hợp. Đồng nhất tốt hơn về mặt kế hoạch, nhưng tốn thêm và không bảo đảm công cụ sẽ đạt nếu chưa có phép chứng minh.

### Q2. Chứng minh điểm nghẽn nào trước?

- A: trọn N02 đúng giọng Khoai, thấy mặt, diễn ký ức và khẩu hình phù hợp. Khuyến nghị sơ bộ: xác nhận lời–giọng–mặt trước khi sản xuất cả tập; nguồn 200 có ứng viên để kiểm local trước khi đề xuất sinh.
- B: chuỗi im lặng R04–R06, chứng minh ý định ăn → bị thấy → đổi hướng vào bát. Ưu tiên cơ thể/hành động; vấn đề voice–miệng vẫn phải kiểm trước toàn tập, không bỏ.

Cả hai đều cần giải quyết; lựa chọn chỉ là thứ tự. Kiểm local trước, không suy lựa chọn A/B là quyền paid generation.

### Q3. Phạm vi công cụ nếu tuyến hiện tại không đạt?

- A: tiếp tục giới hạn Flow và bộ local đã có; nếu không đạt, dừng và trình lại, không thay bằng cảnh không mặt. Phù hợp giới hạn công cụ cũ nhưng có thể chưa hoàn thành mục tiêu nếu tính khả thi không được chứng minh.
- B: cho nghiên cứu thêm tuyến/công cụ đồng bộ thoại–miệng nếu kiểm cho thấy cần. Khuyến nghị sơ bộ ở mức nghiên cứu: chưa chọn vendor, không cài/mua/upload hoặc kết nối API trước duyệt riêng; không tự từ bỏ Flow/Veo.

### Q4. Cơ chế duyệt chi thử mới?

- A: trình đúng phép thử, quote live, số output và tiêu chí đạt/dừng, owner duyệt khoản đó trước chạy. Khuyến nghị sơ bộ trong giai đoạn khắc phục; chưa cấp credit mới.
- B: cấp trần thử mới, owner nêu số credit; root vẫn phải trình kế hoạch phân bổ và đọc quote, không dùng toàn trần để thử không điều kiện.

Quy tắc thử 3 lượt Lite trước đây là lịch sử cần đối chiếu tuyến/giá và quyền chi; không tự coi nó cho phép vượt 3 credit còn lại hoặc áp model Lite cho tuyến voice khác. Số output phép thử mới sẽ được trình cụ thể sau lựa chọn/quote.

## Tổng hợp vòng

- Đã chốt: storyboard text R1 được owner duyệt, mở tier3 local inventory.
- Đã kiểm: file inventory, 12 ứng viên/144 ảnh mẫu, reference OPEN7, hash/probe audio 202, công cụ local/module tồn tại và lịch sử tuyến/approval.
- Giả định: audio 202 là ứng viên chính và footage có thể tái dùng một phần; chưa chốt đoạn nào là final.
- Còn mở: Q1–Q4, voice/lip-sync/continuous performance, đoạn reuse sâu, dựng thử bằng ảnh, quote live và reviewer thực.
- Tiếp: owner trả lời; root lập kiểm đoạn cụ thể/thử khả thi có giới hạn và kiểm công cụ theo phạm vi được chọn, không nhảy sang sản xuất cả tập.

## Owner chốt tầng 3 và cập nhật kiểm sâu

Owner trả lời nguyên văn: “1. a; 2 a; 3a; 4a”. Ghi nhận Q1-A/Q2-A/Q3-A/Q4-A: tái dùng chọn lọc, N02 trước, chỉ Flow/bộ local hiện có, trình từng phép thử/quote/output/tiêu chí đạt–dừng và duyệt riêng trước chi.

Không chọn Q3-B: không tự nghiên cứu/chuyển sang vendor lip-sync khác, mở API hoặc cài công cụ mới. Không chọn Q4-B: chưa cấp trần thử mới.

Kiểm sâu 216 xác nhận cut chính xác của N02: khung chung 0–3,000 giây; cận Khoai 3,000–6,833333; cận món 6,833333–8,375; trở lại hai người 8,375–10,000 video. Lượt 215 chỉ nêu vùng theo ảnh lấy mẫu; nhãn thời gian của contact `fps` không thay timestamp frame native. Dùng 216 khi cần quyết định source range. Không viết lại các ghi chú lịch sử như thể đã biết mốc chính xác ở 215.

Tầng 4 đề xuất tại `217_recovery-tier4-runtime-gates-and-questions.md`; chưa dispatch vai độc lập hoặc chi thử từ việc ghi nhận quyết định này.
