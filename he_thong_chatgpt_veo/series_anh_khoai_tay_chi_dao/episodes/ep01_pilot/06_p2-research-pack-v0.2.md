# EP01/P2 — Research pack Nem Bùi v0.2, đề nghị owner gate

- **Version:** `EP01-P2-v0.2`; thay thế v0.1 *khi* được owner duyệt, chưa tự approved.
- **Status:** `READY_FOR_OWNER_REVIEW`, P2 gate pending.
- **Rework date:** 2026-09-30 (Asia/Saigon).
- **Upstream:** P0-v1, P1-Bible-v0.9 approved; owner accepted claim boundaries 2026-09-29; Fact & Source Auditor report `EP01-P2-AUD-20260929` recommends evidence-map rework.
- **Purpose:** cung cấp baseline nghiên cứu cho P3 brief, không chọn concept/script. `F01` và `F02` là hai claim *ứng viên* được ưu tiên vì Script Lab đã dùng chúng; chọn làm nền nghiên cứu **không** duyệt câu thoại hoặc hình cụ thể.

## 1. Nguồn đã tái kiểm và provenance

| ID | URL / thời điểm đăng | Truy cập 2026-09-30 | Vai trò và giới hạn |
|---|---|---|---|
| R2 | [VOV5 — Nem Bùi, món ngon dân dã xứ Kinh Bắc](https://vovworld.vn/vi-VN/xa-hoi-doi-song/nem-bui-mon-ngon-dan-da-xu-kinh-bac-2206831.vov5); ngày đăng không xác định từ trang trích xuất | **Mở full text**; các đoạn liên quan ở dòng web 73–80, 86 | Tường thuật có phỏng vấn người sản xuất; hỗ trợ Bùi Xá/thính. Trang có lỗi gọi “huyện Ninh Xá”, nên không dùng để xác định cấp hành chính. Tuyên bố đãi khách là lời tường thuật ở phạm vi địa phương, không là khảo sát đại diện Kinh Bắc. |
| R4 | [VietnamPlus/TTXVN — nghề nem thính Bùi Xá](https://www.vietnamplus.vn/hoc-trom-nghe-lam-nem-thinh-bui-xa-dung-chat-o-bac-ninh-post294563.amp), 03/12/2014 | **Mở full text**; đoạn liên quan dòng 72–94 | Phóng sự về làng/nghề và công đoạn làm thính; niên đại “hàng trăm năm” được gắn với lời kể cao niên, không là tài liệu xác lập năm hình thành. Công thức/cách rang trong bài là cách làm được mô tả, không chứng minh mọi hộ giống nhau. |
| S5 | [Trang Thương mại biên giới của Bộ Công Thương — Nem Bùi](https://thuongmaibiengioimiennui.gov.vn/dac-san-vung-mien/2023/2/nem-bui), 08/02/2023 | **Mở full text**; dòng 15–19, 23 | Bài ghi rõ nguồn Hà Nội Mới ở dòng 23; là bài đăng lại, **không** phải một cuộc điều tra độc lập của Bộ. Hỗ trợ cách diễn đạt hẹp về Bùi Xá, gạo rang làm thính, làm quà; không dùng tính từ/tuổi nghề tuyệt đối làm fact. |
| R3 | [Cổng du lịch — Một số ẩm thực tiêu biểu Bắc Ninh](https://dulichbacninh.gov.vn/kham-pha/mot-so-am-thuc-tieu-bieu-bac-ninh-c1060.html); ngày đăng không xác định từ đoạn trích | **Mở full text**; mục Nem Bùi dòng 130–135 | Bài tổng hợp, không cung cấp nguồn gốc cho từng nhận định về tục lệ; chỉ là chứng cứ có một cách kể về đãi khách quý, không là xác nhận tập quán toàn vùng. Địa danh phường cũng không được dùng khi còn bất nhất. |
| S1 | [Cổng phường Ninh Xá — làng nghề Nem Bùi](https://ninhxa.bacninh.gov.vn/news/-/details/76641/lang-nghe-nem-bui-di-san-am-thuc-kinh-bac-86668605), 24/01/2026 theo trang tìm kiếm | **Không mở được full text trong lượt này**; bản print chính quyền cũng timeout; chỉ thấy bản tìm kiếm | Maker v0.1 ghi HTTP 200 trong lượt trước; timeout hiện tại không phủ định lượt đó. Không dùng snippet làm đoạn chứng cứ chính cho F01/F02 ở v0.2. |
| S2–S3, S6 | URL như source register v0.1 | **Không tái mở trong lượt này** | Không cần để hỗ trợ F01/F02 đã chọn; giữ như hồ sơ nguồn cũ và xung đột niên đại/địa giới, không dùng làm proof mới ở v0.2. |

**Log truy vấn/truy cập:** mở URL trực tiếp R2/R4/S5/R3; lần mở thẳng URL đầu bị công cụ từ chối, sau đó tìm đúng URL qua chỉ mục rồi mở kết quả; trang R2, R4, S5, R3 đã trả full text. Tìm bản print S1 qua `site:bacninh.gov.vn "nem Bùi" "thính gạo" Bùi Xá`, nhưng mở bản print timeout. Độ truy cập không ổn định được ghi thay vì khẳng định nguồn luôn sẵn.

## 2. Claim–source evidence map có thể tái kiểm

| Claim ID / câu được phép phát triển | Đoạn kiểm trực tiếp (vị trí + đoạn ngắn) | Vì sao đoạn nguồn hỗ trợ đúng mức | Không được suy rộng |
|---|---|---|---|
| `F01`: “Nem Bùi gắn với Bùi Xá, Bắc Ninh.” | R4 dòng 79 nêu nghề nem Bùi Xá tại Bắc Ninh; R2 dòng 74–76 nhắc làng Bùi Xá và tên nem; S5 dòng 15 nêu làng Bùi Xá, Bắc Ninh (bài đăng lại). | Hai nguồn tường thuật khác thời điểm + một bản đăng lại đều nối món/nghề với Bùi Xá; đủ cho quan hệ *gắn với*, không cần xác quyết địa chỉ hành chính hiện tại. | Không dùng “mọi hộp nem trên hình đều được làm ở Bùi Xá”, “chỉ có ở Bùi Xá”, hoặc tên phường khi chưa kiểm văn bản hiệu lực. Thoại “từ Bùi Xá” cho một hộp hư cấu cần sửa thành câu F01. |
| `F02`: “Thính gạo rang góp phần tạo mùi/vị của Nem Bùi.” | R2 dòng 79 mô tả gạo được rang, dậy mùi rồi nghiền làm thính; R4 dòng 86–94 mô tả rang gạo và vị thơm của thính; S5 dòng 16 và 19 nêu gạo rang thành thính và mùi thơm (đăng lại). | Chứng cứ trực tiếp về *công đoạn rang gạo*, *thính* và *mùi thơm* trong các cách làm được mô tả. Dùng “góp phần” vừa mức hơn “linh hồn duy nhất”. | Không suy công thức chuẩn, một loại gạo/tỷ lệ bắt buộc, thính luôn bám ngoài bề mặt, hoặc một người trong cảnh có thể nhận đúng nguyên liệu chỉ nhờ ngửi. Hình phải kiểm ở P6. |

**Source independence:** R2 là bài có phỏng vấn, R4 là phóng sự TTXVN năm 2014; không thấy bằng chứng trong các đoạn đọc rằng hai bài đăng lại nhau, nhưng không thể chứng minh hoàn toàn độc lập thông tin lịch sử. S5 tự ghi là bài Hà Nội Mới đăng lại và không được tính như xác nhận thứ ba độc lập. R3 là bài tổng hợp, không tăng số nguồn gốc cho F01/F02.

## 3. Claim register còn lại / phản chứng phải giữ

| ID | Disposition P2 v0.2 | Evidence và điều kiện nếu muốn mở lại |
|---|---|---|
| `F03` thành phần/lá | `SUPPORTED_WITH_QUALIFIER`, không là trục đang chọn. S5 dòng 16–19; R4 dòng 91–94. Khi chọn hình/câu cụ thể, kiểm đúng kiểu nem được minh họa, không nói “luôn luôn”. |
| `F04` nghề truyền thống | `SUPPORTED_FOR_REPORTED_EVENT`, không chọn. S4/R5 trong audit tường thuật lễ công nhận *nghề*. Nếu dùng như claim chính, tìm quyết định ký và đúng tên pháp lý trước script lock; không đồng nhất món với di sản được ghi danh. |
| `F05` làm quà | `SUPPORTED_WITH_QUALIFIER`, không chọn. S5 dòng 19 và R3 dòng 135 ghi có thể dùng làm quà; không suy tập quán thường đãi khách. |
| `F06` người Kinh Bắc thường đãi khách | `NOT_SUPPORTED_AS_WRITTEN — EXCLUDE`. R2 dòng 86 nêu nem thường được chuẩn bị đãi khách ở tường thuật địa phương; R3 dòng 132 kể chuyện “đãi khách quý” như truyền thống. **Bổ sung so với v0.1:** có evidence cho cách nói *hẹp/được thuật lại*, nhưng không có dữ liệu đại diện cho mọi người Kinh Bắc hoặc tần suất toàn vùng. Nếu định dùng, mở nghiên cứu và cultural reviewer; pilot hiện bỏ. |
| `F07` tuổi nghề chính xác | `CONFLICTED/UNVERIFIABLE — EXCLUDE`. S5 dòng 15 nói gần 100 năm; R4 dòng 79 thuật lại hàng trăm năm theo lời cao niên. Hai cách kể không cho phép chọn một mốc năm. S2 trong v0.1 cũng nêu hàng trăm năm nhưng không tái mở được. |
| `F08` phường Trí Quả hiện tại | `CONFLICTED — EXCLUDE`. S3 v0.1/index nêu Trí Quả, nguồn khác gắn Ninh Xá; không có văn bản hành chính hiệu lực được đọc đầy đủ ở pack này. Chỉ ghi **Bùi Xá, Bắc Ninh**. |
| `H01` chơi chữ “thả thính” | `HUMOR_NOT_FACT`; có thể thử ở P4 nhưng không tự duyệt và không ngụ ý F06. |
| `O01` khẩu vị Khoai | `OPINION`; gắn với cá nhân, không là đánh giá phổ quát về món/địa phương. |

## 4. Rights, image và creative handoff

- Trang nguồn/ảnh phóng sự chỉ được dùng để nghiên cứu, **không tự cấp quyền dùng ảnh, video, nhãn hàng, cơ sở hoặc nhân vật có thật** trong clip. P6 lập reference/asset register; người thật/địa điểm thật phải xác minh riêng nếu xuất hiện.
- Hình món cần đối chiếu phiên bản tham chiếu được phép sử dụng. Không để AI vẽ một lớp thính/kiểu gói rồi tuyên bố đó là cách duy nhất hoặc “chính xác truyền thống”.
- P3 có thể chọn câu hỏi tập dựa trên F01/F02 sau khi owner duyệt pack này; P3 không bắt buộc chọn một trong các concept Script Lab. Các script thử trong `script_lab/` vẫn `NON-FINAL`.
- Nếu script cuối thêm claim mới, phải quay lại P2 để gắn source span và auditor check phần thay đổi.

## 5. Disposition và gate request

**Maker rework disposition:** F01/F02 có các đoạn nguồn trực tiếp, vị trí, provenance và giới hạn diễn đạt đủ để **trình owner xem xét P2**; các claim có mâu thuẫn/không cần thiết tiếp tục bị loại. D01 (evidence đãi khách phạm vi hẹp) và D04 (lời kể niên đại) đã được ghi; D02 được xử bằng R2/R4/S5 mở trực tiếp thay cho việc phụ thuộc S1–S3. D05 giữ phạm vi Bùi Xá/Bắc Ninh. Không tuyên bố đã giải quyết lịch sử/phường/rights chưa dùng.

**Gate decision chỉ owner ghi:** `APPROVED` / `REWORK` / `BLOCKED` cho `EP01-P2-v0.2`, kèm điều kiện/ngoại lệ. Report Auditor v0.1 không tự đổi thành phê duyệt v0.2; nếu owner muốn tái-review độc lập đúng v0.2, thực hiện trước gate. Chưa mở P3 chính thức cho tới khi có quyết định này.
