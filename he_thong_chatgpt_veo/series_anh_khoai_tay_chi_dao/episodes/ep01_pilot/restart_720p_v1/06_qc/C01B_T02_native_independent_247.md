# C01B T02 — xác nhận actual độc lập REC247

Review ngày 08/10/2026. **REWORK / SAME_MAJOR_START_POSE_CONFIRMED / STOP_FOR_DIAGNOSIS**. T02 thu tay sớm hơn T01 trong mẫu, nhưng actual start vẫn biến inner gesture gần bát thành hai tay ở hai phía đĩa. Không selected/release, không automaticT03 hoặc mở phụ thuộc C03A.

## Exact target và scope

SHA256 PowerShell thực:

- `05_native/EP01_720_C01B_T02_NATIVE.mp4`: **`b2203e0e3572b997f3f58959acb60aacd343d353a775347e0c49c90066b78f5d`**.
- Exact A80 source `02_refs/C01B_START_from_C01A_T04_FLOW_v1.png`: `0cf422f2b28dae631785af6ec19fc7488800c0cf8d22bb95dddd04e1b7ae2acb`.

Đọc full T02 request247/native_evidence; criteria từ T02 preflight và actual join247 vừa review. Root technical evidence720×1280/24fps/96frames/video4s/audio4,01s/decode good; reviewer tính hash, không probe/decode lại hoặc coi format là quality PASS. Live inputs/readback/quote7/debit7 là record của root, không UI do critic kiểm.

**Trực tiếp xem:** exact A80 reference; cả hai mouth_hands6fps boards (**0,4,…92**); fullframes **0,4,12,28,44,52,95**. Tổng **25 unique T02 frames**, không96frames/continuousAV. Zero-index/PTS=index÷24; PNG=index+1. Không ASR, không actual nghe, không lip-sync certification. Phạm vi đủ xác nhận mismatch first-frame và diễn biến mẫu, không phải toàn take certificate.

## Findings

| Finding | Expected / actual và mốc | Severity / disposition |
| --- | --- | --- |
| **B-T02-START-POSE** | A80: inner hand hover gần cạnh trong bát riêng, outer fingers tại vành phải. **T02 frame0/0s**: inner arm đã duỗi trái-xuống, fingertips ở vùng vành trái; outer hand ở vành phải. Full4/0,166667s và12/0,5s giữ hai tay tại hai phía đĩa. Không phải pose A rồi chỉ khép inner gesture INWARD. | **MAJOR lặp đúng source-pose blocker T01** đã xác nhận trên actual join247. Không cần pixel-identical toàn mặt/nền; vị trí/chức năng tay đã đổi làm action continuation sai. Không phải lỗi mới chỉ vì cả T01/T02 fail. |
| B-T02-RELEASE-TIMING |Full28/1,166667s mắt Đào lên Khoai, fingers bắt đầu rời vùng vành; boards36–44/1,5–1,833333s thu tay; full44 tay đã gần bát, full52/2,166667s inner hand nghỉ còn outer hand trên vùng bát.56–60/2,333333–2,5s settle, giữ tới95/3,958333s. | **Cải thiện sampled timing** so T01 nghỉ khoảng2,833333–3s. Không thấy cùng đoạn new approach dài như T01; không đánh đồng toàn renewed-reach. Tuy nhiên release từ pose sai không sửa lỗi start. Không chứng nhận nghe cue đúng từ still. |
| B-T02-KHOAI-HAND |Prompt giữ hai tay Khoai resting. Boards8–20/0,333333–0,833333s và **full12/0,5s** có hai bàn tay nâng lên khỏi bàn trong mouth event; về vùng nghỉ khoảng28–32. | **Deviation mới**, không dùng để đếm SAME MAJOR. Thêm gesture không được yêu cầu; nếu staging sau thay đổi phải có disposition, không silently waive. |
| B-T02-FOOD/PLATE |So sourceA80 với fullT02-0: đĩa/khối nem contour và arrangement khác, tương tự loại redraw T01. Trong mẫu không thấy gross pull/lift/take/eat; head/outline drift nhỏ tiếp tục. | Food continuity chưa đóng. Không kết luận lượng món đổi hoặc chuyển động đĩa vật lý3D từ outline. No gross pull không bằng “exactly stationary PASS”. |
| B-T02-COVERAGE/SET |Hai mặt/tay/đĩa rõ; Đào môi khép trong25samples, Khoai mouth event đầu. Phố mở, rau trước-trái, chấm, bát trống, đũa nghỉ/cốc và symbol giữ; không thấy chữ mới/steam trong mẫu. | Thuận lợi có giới hạn, không PASS voice/speaker/AV hoặc bù cho source mismatch. |

## Kết luận chẩn đoán và bước tiếp

1. **Ủng hộ STOP của root:** T01 và T02 là hai actual generated outputs liên tiếp cùng MAJOR source-pose mismatch. Join T01 re-export không tính thêm output; cải thiện thời gian thu tay T02 không reset blocker đầu cảnh. Không automaticT03/paid loop hoặc selected B từ no-steam/voice ID.
2. Lỗi nằm ở **actual take B so với selected A-end**, có ngay frame0 trước assembly. Không bằng chứng upload nhầm, source PNG sai, hoặc cơ chế model/prompt riêng đã được chứng minh. Ràng buộc Inputs/Ingredients exact chip đã ghi không bảo đảm start-frame adherence. Phrase sửa thất bại trong giữ pose, không chứng minh mọi prompt tương lai bất khả thi.
3. Tối thiểu cần chẩn đoán lại cơ chế nối/staging trước đề xuất triển khai: giữ A-end actual/food arrangement; B phải tiếp đúng contact nguồn và inner hand **chỉ về thân/bát**, Khoai tay nghỉ, sau interruption outer release→rest. Nếu đổi công cụ/mode hoặc thay staging/canon để tránh yêu cầu khó, trình rõ tradeoff và authority cần bổ sung; **không** tự đổi model, overlay âm, offset bỏ Khoan, crop/foodcover/freeze hoặc duyệt lại A để hợp thức B.
4. T02 audio là waveform mới `b220…`, **chưa approved**; T01 exact audio acceptance không chuyển sang T02. Reviewer không nghe/ASR-certify Khoan/K20/sync. Không cần thêm full96scan hay nghe để quyết định STOP source mismatch đã thấy; hearing/join gates chỉ xử lý khi có phương án/source được chọn hợp lệ.

**Đã xác định:**25samples và hash, MAJOR start-pose lặp; release/rest sớm hơn; Khoai lift gesture mới. **Quyết định review:**REWORK + STOP_FOR_DIAGNOSIS, không production/release. **Giả thuyết:**reference adherence và action staging vẫn chưa đủ; chưa causal proof. **Còn mở:**phương án sửa cơ chế nối, audio T02 và toànAV. **Bước tiếp:**root đọc đầy đủ, đóng STOP và đề xuất xử lý có quyền; giữ A/C02/media nguyên, không tốn thêm lượt từ báo cáo này.
