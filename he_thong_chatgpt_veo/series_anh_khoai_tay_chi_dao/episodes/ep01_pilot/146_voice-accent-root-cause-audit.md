# RCA — Giọng nam Bắc bị sinh thành giọng nam Nam

Ngày 2026-10-02. Owner yêu cầu truy nguyên nhân gốc sau khi loại cả ba mẫu 145, tiếp nối việc loại chín mẫu 142/143. Audit theo learning/02_root-cause-tracing-protocol.md. Không tạo thêm hoặc tiêu credit trong lượt audit.

## Defect và phạm vi kết luận

Expected: nam trưởng thành, miền Bắc; chất Khoai ở 93 không thay yêu cầu vùng giọng. Observed: owner nghe cả 12 mẫu là miền Nam, không đạt. Đây là bằng chứng nghe của owner; root chưa nghe độc lập, không tự mô tả lỗi ngữ âm/timestamp cụ thể. Bộ 145 chuyển OWNER_REJECTED / ACCENT_FAIL; toàn bộ 12 mẫu không dùng làm giọng sản xuất.

Phải tách: nguyên nhân làm model sinh sai accent chưa xác nhận; nguyên nhân quy trình không làm chủ/kiểm sớm accent đã tìm thấy. RCA trạng thái PARTIAL — PROCESS_CAUSES_IDENTIFIED / GENERATION_MECHANISM_UNRESOLVED, không RCA_CLOSED.

## Truy ngược nguồn thực

| Mắt xích | Bằng chứng thực | Kết luận có giới hạn |
|---|---|---|
| Yêu cầu | Owner yêu cầu nam miền Bắc, sau đó loại hai bộ | Không phải owner đổi yêu cầu sau generation |
| Nguồn giọng | Request 142/145 chỉ có START JPEG TABLE08 và prompt chữ; không nạp audio, không chọn voice preset/voice-ID | Không có nguồn giọng Bắc đã tuyển chọn. Đây là giọng do Veo tự sinh, không phải tìm/upload nhầm nguồn giọng miền Nam |
| Điều khiển | 142 viết Northern Vietnamese accent; 145 viết tiếng Việt, Hà Nội/miền Bắc | Yêu cầu có trong prompt nhưng chưa đạt theo owner. Chữ yêu cầu không là cơ chế khóa accent đã kiểm chứng |
| Model/settings | Nhật ký/screenshot thao tác 142/145: Veo 3.1 Lite, Frames, TABLE08, 8s, 720p, 9:16, x3; return-without-audio OFF | Các lượt được chạy bằng cùng route. Chưa có kiểm provider server revision/seed, không suy Lite luôn sai hoặc Quality chắc sửa |
| Asset/map | Các asset trong manifest 143/145 được mở, đọc prompt và tải native; 145 original-download SHA trùng manifest | Không tìm thấy bằng chứng gán lại video cũ vào ba nhãn mới; chỉ kiểm được phạm vi provenance lưu và bytes |
| Bản owner | 12/12 MP4 tại folder owner SHA trùng MP4 artifact tương ứng | Không đổi MP4 khi sao chép bàn giao |
| Trích WAV | 12/12 hash decoded PCM s16le của MP4 bằng hash decoded PCM của WAV tương ứng | Tách WAV không làm thay âm thanh. PCM equality không chứng minh accent đúng |
| QC | Hợp đồng AEQ yêu cầu listening, không suy voice PASS từ ASR/metadata; 142/145 chỉ technical decode và owner nghe | Thiết kế có listening gate nhưng actual reviewer nghe accent chưa chạy trước trình. Không coi thiết kế agent/fixture là kiểm âm thanh production |

Không có bằng chứng âm thanh cũ được nạp lại vào model. JPEG không có track giọng; ảnh có thể ảnh hưởng suy diễn của model là giả thuyết khác, chưa loại hoặc xác nhận. Tên K2/K3/K4 và B-R1 chỉ là nhãn yêu cầu/thử, không chứng nhận vùng giọng.

## Sai sót quy trình đã xác định

1. Chuyển yêu cầu vùng giọng thành mô tả prompt mà chưa xác minh route cung cấp mức điều khiển nào. Không có voice source/preset đạt Bắc hoặc positive baseline.
2. Vòng 142 nhân ba phong cách diễn trước accent baseline, làm chín mẫu cùng chịu một rủi ro nền chưa kiểm chứng.
3. Sau thất bại, 145 đổi cả ngôn ngữ prompt, mức cụ thể địa phương, lượng lời và hướng diễn. Có thể dùng như candidate probe nhưng không phân biệt nguyên nhân riêng từng biến; không là RCA kiểm soát một biến.
4. Agent AV có contract nghe nhưng công cụ/khả năng nghe actual không được đáp ứng; reviewer thực nghe độc lập chưa chạy. Root không báo voice PASS, nhưng chưa tổ chức được bước kiểm accent trước trình và để owner làm người phát hiện lỗi.
5. Trình bộ mẫu dưới tên hướng giọng dễ gây hiểu là đã có nguồn giọng Bắc tuyển chọn. Thực tế chỉ sinh ứng viên. Cần nói rõ nguồn/giọng yêu cầu/giọng nghe đánh giá là ba loại khác nhau.

## Giả thuyết / điều cần kiểm chứng

| H | Hiện trạng | Kiểm phân biệt cần thiết, chưa thực hiện |
|---|---|---|
| H1 — route/model đáp ứng accent không đáng tin trong cấu hình này | SUPPORTED trong 12 mẫu owner loại; không chứng minh giới hạn phổ quát | Kiểm capability thực về voice selector/reference; positive control cùng câu với nguồn hoặc voice đã nghe đạt Bắc |
| H2 — ảnh/bối cảnh/khối mô tả khác chi phối giọng | UNRESOLVED | Thử cùng câu/accent/model, chỉ đổi hoặc bỏ image/context; route thay đổi phải ghi confound |
| H3 — ngôn ngữ hoặc phrasing của prompt | Đổi tiếng Anh sang tiếng Việt vẫn thất bại theo owner | Không coi chỉ đổi ngôn ngữ là fix; nếu nghiên cứu tiếp phải giữ phần còn lại cố định |
| H4 — lỗi trích/sao chép audio | Không được hỗ trợ: PCM equality 12/12, owner MP4 SHA equality 12/12 | Đã kiểm kỹ thuật local, không cần generation để kiểm nhánh này |
| H5 — tài liệu/khả năng voice của model khác bị suy sang Veo | Rủi ro capability conflation có trong nghiên cứu chung về Flow | Kiểm theo model và tính năng actual; không mặc định tài liệu Flow chung là route Veo Lite hỗ trợ voice lock |

## Đối chiếu tài liệu chính thức

Đọc lại ngày 2026-10-02: [Google Flow model features](https://support.google.com/flow/answer/16352836?hl=en) đặt preset/custom voice trong phần Gemini Omni; không xác nhận preset nam Bắc hoặc điều khiển accent tương đương cho Veo Lite. [DeepMind Veo prompt guide](https://deepmind.google/models/veo/prompt-guide/) hướng dẫn mô tả voice/dialogue qua prompt, không cung cấp bảo đảm giọng Bắc cho phép thử này. Không dùng việc docs không nói để kết luận Veo tuyệt đối không hỗ trợ accent.

Các tài liệu agents/06-quality-agent-expansion-research-v0.1.md đã phân biệt voice references cho supported Omni, nhưng mô tả chung Flow và câu hỏi khả năng voice không thay actual capability test theo model. Đây không là nguồn audio đã được dùng.

## Bằng chứng kỹ thuật mới

FFmpeg verified 9.0.2 read-only: `-map 0:a:0 -c:a pcm_s16le -f hash -` trên cả MP4 và WAV. Mỗi cặp khớp SHA256, không tạo file mới. Các PCM hash của 12 MP4 khác nhau; không cùng audio bytes gán 12 tên. WAV của ba mẫu mới:

```text
B-R1-01 48f6c6a540e2ec621a7e82268134b3254660a90e2c01e8be02abdff010207a4b
B-R1-02 3f8e9b0fbec41ec835f822824a8a5049f7f8509f4ba45311085da85117353a55
B-R1-03 4267e925c8a862b0715906e306f6d18de372267638afa63810040e488a7468da
```

Original downloads của ba mẫu 145 SHA đúng như manifest; 12 bản owner MP4 đúng artifact. Không kiểm lại âm thanh server bằng nghe hoặc signed URL trong lượt này; không lưu URL nhạy cảm. Không ASR accent: transcript không thay ngữ âm/nghe.

## Quyết định, giả định, còn mở, bước tiếp

- Đã xác định: không dùng nguồn giọng Bắc, chỉ prompt; lỗi accent theo owner ở cả hai bộ; không do bước trích WAV/sao chép local trong phạm vi kiểm.
- Đã chốt: loại cả 12, không generation trong audit; nam Bắc và chất Khoai vẫn giữ. Số dư lần kiểm 145 là 620; khoản mới 200 còn 170, không tiêu trong audit, không dùng Quality.
- Giả định: chưa route nào có baseline giọng Bắc đạt; không mặc định Hà Nội là canon hoặc preset trên Omni có sẵn/đạt.
- Còn mở: cơ chế sinh accent sai, nguồn/voice identity đạt, route khả dụng, actual nghe độc lập và khả năng giữ giọng/lip-sync.
- Bước tiếp đề xuất: kiểm khả năng chọn/reference giọng trên route cụ thể trước tạo tiếp; tìm hoặc tạo baseline giọng Bắc có provenance và quyền phù hợp, nghe xác nhận; chỉ sau đó so cùng câu và duyệt cách tích hợp. Nếu Veo route không khóa được giọng thì trình phương án voice riêng/ghép, không tự đổi pipeline. Không sửa prompt mò hoặc chạy thêm hàng loạt để coi là RCA.
