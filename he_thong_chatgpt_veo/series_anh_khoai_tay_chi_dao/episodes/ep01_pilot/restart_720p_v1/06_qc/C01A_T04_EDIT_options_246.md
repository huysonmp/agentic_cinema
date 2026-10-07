# C01A T04 — Lựa chọn dựng và ngoại lệ phải trình owner

**Run:** C01A-T04-EDIT-246. **Role:** EDIT v0.2, maker. **Ngày:** 07/10/2026. **Mode:** bounded local edit planning với sampled native frames. **Disposition hiện hành:** HOLD theo chuẩn trước-contact; không selected range/EDL, không render hoặc generation.

## Đầu vào và capability

Kế thừa hợp đồng PROD7/02, DIRECT01/DIRECT05, AEQ02/SIA10 đã đọc đầy đủ ở run EDIT246 và C01A_EDIT_246; không nhận timing giấy là actual. Lượt này đã đọc toàn `04_requests/C01A_T04_request_246.json`, `04_requests/C01A_T04_prompt_246.txt`, `06_qc/C01A_T04_native_evidence_246.json`, `06_qc/C01A_T04_ASR_raw_246.json`. Thẩm quyền217 chỉ bounded local maker contribution; chỉ viết report được giao, không UI/API/Git/credit/script/media write, không waive canon hoặc duyệt thay owner.

Target native T04: `05_native/EP01_720_C01A_T04_NATIVE.mp4`, hash theo manifest `bbf5c423bff3e30b98aa0ec5b7f56d11b89467456f75dcf1ea2fe3b0829efa43`. Chưa tự tính hash native. Probe của root ghi720×1280,24fps,144frames/video6s/audio6,016s. Không lấy decode sạch thành chất lượng cảnh.

Đã trực tiếp xem owner-QC `C:/Users/PC/Downloads/du_an_nem_bui/ep01_restart_720p_v1/06_qc/C01A_T04_246/overview_1fps_01.jpg`, `mouth_hands_6fps_02.jpg` và các native PNG có zero-based indices76,78,79,80,84,96,108 (filename là index+1). Thời điểm tương ứng3,166667/3,25/3,291667/3,333333/3,5/4/4,5s theo bảng timestamp root. Chưa xem tất cả144frames hoặc continuous AV; chưa nghe native, chưa so actual D06. Không đọc report độc lập T04 đang chạy và không đóng findings của critic.

## Quan sát và giới hạn của cửa sổ dựng

- Trong mẫu76/3,166667s, tay ngoài Đào đã ở vành phải đĩa, không có dải gỗ tách rõ giữa ngón và outline như chuẩn request. Tay trong cũng đã tiến ra trước, thay vì nghỉ suốt lượt. Mẫu78–80 vẫn có tay ngoài sát/chồng vành và tay trong đang rút dần. Đây là sai lệch hình với nhiệm vụ strict, không giải quyết bằng đổi nhãn speaker hoặc trim sau câu.
- So mẫu96/4s và108/4,5s, đĩa đã dịch về phía Đào rõ hơn; phần đuôi này không dùng cho phương án “chạm vành nhưng chưa kéo”. Không gọi entire6s native là usable.
- ASR ghi N01 đúng text, câu cuối kết tại3,22s; root báo ngưỡng tail silence -40dB bắt đầu3,286062s. Đây là **ước tính ASR và detector kỹ thuật**, không proof đã giữ toàn âm “em”/hơi thở, đúng giọng hoặc điểm cắt đã an toàn.
- Vùng xấp xỉ3,25–3,333s là **vùng cần kiểm**, không range selected. Mẫu3,291667/3,333333 có môi khép và outer hand ở vành, nhưng không thể xác nhận đĩa tuyệt đối chưa bắt đầu dịch chỉ từ một số mẫu. Không có first-plate-movement index đã được EDIT xác minh.

Điều kiện một window dùng được cho optionB là đồng thời: sau toàn lời/breath cần giữ, trước frame đầu đĩa dịch hoặc thao tác lấy/ăn, pose tay/mắt có thể nối C01B, không phát sinh lỗi mặt/giọng. Nếu không có khoảng đáp ứng giao này, **B không khả thi trên take hiện tại**, dù owner muốn chấp nhận rim-touch. Không cắt mất “em”, đặt tiếng lên hình khác hoặc freeze để tạo một window giả.

## Hai lựa chọn phải phân biệt

| Lựa chọn | Giữ/đổi điều gì | Hệ quả và điều kiện |
| --- | --- | --- |
| **A — Giữ strict trước-contact** | Giữ tay ngoài chưa chạm và tay trong nghỉ; không ngoại lệ tự động | T04 HOLD/không dùng làm selected C01A. Cần re-stage/reroute sản xuất có mục tiêu sau diagnosis và quyền root/owner hiện hành, không EDIT cấp retry hoặc chỉ sửa chữ rồi chạy tiếp. Đổi staging phải có input/prompt/preflight mới và kiểm lại cả tay/mặt/voice/props |
| **B — Trình ngoại lệ chạm vành hạn chế** | Owner cho phép tay ngoài chạm vành **nhưng đĩa chưa dịch**, chưa lấy/ăn; đồng thời cho phép chuyển động tay trong như một gesture phụ | Chỉ giữ prefix đến verified window. C01B phải kế thừa exactpose và Khoai “Khoan” khiến cô dừng, thả và thu tay. Không hứa phí/tiết kiệm hay thành công. Requires owner decision với exact target/candidate cut và phạm vi ngoại lệ; critic vẫn review actual cut và join |

**Khuyến nghị hiện hành:** A là đường duy nhất giữ nguyên chuẩn đang khóa. Có thể trình B như lựa chọn vật liệu cụ thể sau khi xác minh tồn tại window và cho owner thấy đầy đủ hai sai lệch; không mô tả B là “sửa xong bằng cắt đuôi”. Nếu owner không chấp nhận cả rim-touch lẫn inner-hand gesture, B không được triển khai từ T04 này. Không biến inner-hand retract trước “Khoan” thành phản ứng do câu Khoai gây ra: đó phải được hiểu là gesture phụ đã cho phép; phản ứng chính vẫn nằm ở tay ngoài release sau cue.

## Cách B có thể giữ nghĩa, nếu được duyệt và đủ evidence

Trong chuyện đời thường, “Không hợp thì để em” + tay chạm vành đĩa nhưng chưa kéo vẫn có thể biểu hiện ý định lấy; “Khoan” ngắt ở ngưỡng ấy. Đây là **phán đoán creative paper**, không phản ứng khán giả đã đo. Đào vẫn là người cởi mở trêu thân mật, không tranh giành/giám sát; Khoai ngắt nhẹ để kể ký ức, không quát. Hai người là bạn.

Thứ tự không đổi:

1. C01A nguyên N01 do Đào nói, tay ngoài tới vành; không ăn/lấy món hoặc kéo đĩa.
2. C01B nguyên “Khoan” do Khoai nói; tay ngoài đang ở đúng pose chạm, Đào nghe → ngừng ý định → thả và thu. Tay trong ở pose tương ứng actual endpoint, không reset một bàn tay còn giữa chuyển động.
3. C02 exact selected export đã owner246 duyệt, tay nghỉ và nem/bát/đũa/rau/chấm/cốc không reset. Không thêm “Khoan” lần nữa, không dùng đuôi nativeC02 unselected để vá.

C01B Ingredients không bảo đảm start/end lock. Một ảnh exact endpoint giúp tham chiếu nhưng phải kiểm media tạo ra: không bàn tay bỗng lơ lửng cách đĩa trước cue, không đĩa trả ngược lại vì T04 đã kéo trước cut, không hidden cut làm mất release. Nếu C01B không match/không stop-release đọc được thì REWORK source/shot/join, không che bằng cận nem hoặc audio-only.

## Timing và nghiệm chứng trước chọn range

Opening khoảng4,5s theo236 là TARGET. Nếu giữ prefix T04 khoảng3,3s thì ngân sách giấy còn khoảng1,2s cho “Khoan” + stop/release/retract trước C02; **không chứng minh các động tác đủ nhịp hoặc đã vừa**. NativeC01B dự kiến4s không bắt buộc dùng toàn bộ, nhưng không tự cắt phản ứng để giữ4,5s. C02 selected video7,541667s giữ nguyên; phần chênh so slot8,5s giấy có thể được xem xét phân bổ lại sau đo toàn sequence, không slack chắc chắn đã dư hoặc quyền đổi30s.

Root/reviewer cần:

- Xem dense native frames quanh hoàn lời và first plate movement, đối chiếu outline/tâm đĩa với props cố định; motion/full playback khi capability cho phép. Ghi exact first-displacement finding và uncertainty; mẫu -40dB hoặc ASR không cấp cut certificate.
- Nghe trọn N01 và quanh dự kiến cut để xác nhận “em”, breath tail, không thêm lời, đúngD06; listener mouth và lip-sync actual vẫn phải kiểm. T02 audio được owner duyệt không tự chứng nhận T04 audio.
- Chỉ khi có window hợp lệ và owner duyệt B: lập **candidate** cut mới với exact source/range/hash, giữ native nguyên. Sau cắt kiểm output actual; không lấy phần waveform “im” làm chứng nhận không pop/không mất đuôi âm.
- C01B từ state pose candidate sau khi cut verified, rồi audit join trên rough mới: tay/đĩa/eyeline/camera/light/speaker/audio. Một source được chấp nhận không bằng hai nguồn nối đạt.
- Nếu window không tồn tại: báo B unavailable; không thử nối để lấp giả nhiệm vụ hoặc xin owner waive cả platepull ngoài phạm vi này.

## Findings và trạng thái

| Rule | Status hiện tại | Impact / route / closure |
| --- | --- | --- |
| EDIT246-T04-CONTACT | DEFECT với strict design trên sampledframes76–80 | MAJOR cho approved endpoint; A re-stage hoặc owner B exact waiver, không maker tự đóng |
| EDIT246-T04-INNERHAND | DEFECT theo rule tay trong nghỉ; observed gesture | B cần owner cho phép riêng; nếu không, giữ HOLD dù tailtrim |
| EDIT246-T04-PLATE | Tail displacement observed sampled96/108; onsetUNKNOWN | No pull trong B; dense review xác định onset và verified prefix, không toàn native |
| EDIT246-T04-WINDOW | UNKNOWN | Actual listening + dense movement review, cut actual/version/hash; không ASR-certification |
| EDIT246-T04-C01B | MISSING_SOURCE/MATCH_NOT_TESTED | Thực C01B stop-release-retract và rough join; không pointstill PASS |
| EDIT246-T04-VOICE | NOT_LISTENED_BY_EDIT / T04_OWNER_PENDING | SIA/AV-VOICE và checkpoint actualD06; không expected→observed |

## Handoff năm mục

1. **Đã xác định:** T04 hình mẫu vi phạm strict gap/tay trong nghỉ và có platepull ở tail; ASR/silence không xác minh boundary an toàn.
2. **Quyết định đã chốt:** none mới; giữ strict HOLD. A giữ chuẩn; B là material-owner option có hai ngoại lệ rõ và điều kiện window, chưa approved.
3. **Giả định:** có thể tồn tại prefix sau lời trước dịch đĩa; chưa được chứng minh. “Rimtouch rồi ngắt” có thể giữ nguyên động cơ câu chuyện nếu actual nối đọc được, không bảo đảm.
4. **Còn mở:** exact movement onset/fullword tail, owner chọn A/B, actualD06, endpoint/candidatecut/C01B và timing toàn mở.
5. **Bước tiếp:** root đọc critic độc lập và evidence actual, xác định window; hỏi owner lựa chọn với target/sai lệch đầy đủ. Không tự render/submit; nếu B không tồn tại hoặc không duyệt thì giữ nguồn lỗi choRCA và re-stage theo quyền sau diagnosis.

**Change log:** report mới chỉ planning; không source/media/EDL/approval/credit mutation. Không claim các frame đã xem là continuous AV hoặc frame range đã certified.
