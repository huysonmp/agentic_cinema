# REC252 — Giữ hình sạch chữ, trình tuyến sửa trực tiếp

Ngày 08/10/2026. Owner chọn **B** của vòng251: không chấp nhận chữ thoại tự sinh, chuẩn bị hướng sửa khác có evidence trước xin sinh thêm. Chỉ là quyền chuẩn bị; REC252 submit0, chi0. T02 chưa được chọn, BR/C03A/finishing vẫn HOLD.

## Cơ sở và chẩn đoán

Hai nguồn BM249/251 cùng loại burn-in, dù thay ảnh sang solo và diễn đạt thoại chỉ là audio. Reference v2 sạch chữ; prompt gửi có ràng buộc không lettering và live readback bằng file. Chữ có ngay trong native, không phải caption track hoặc do dựng. Tầng lỗi là generation; chưa cô lập được một cụm prompt/preset hoặc cơ chế backend là nguyên nhân duy nhất. Không có căn cứ chạy lại cùng tuyến chỉ bằng thêm “no subtitles”.

Giữ đúng Khoai/K20, một “Khoan.”, mặt rõ, camera solo, món nguội và canon. Chưa thực nghe hoặc chứng nhận khẩu hình T02; chỉnh chữ không tự đóng các scope đó.

## Nghiên cứu công cụ chính thức và live

Tra cứu ngày08/10/2026:

1. [Google Flow: Edit videos & build scenes](https://support.google.com/flow/answer/16935718?hl=en): Omni Flash hỗ trợ chỉnh video bằng prompt, chọn đoạn tối đa10s, giữ lịch sử bản trước. Tài liệu này không bảo đảm xóa chữ chính xác hoặc giữ audio bất biến.
2. [Google Flow: models & features](https://support.google.com/flow/answer/16352836?hl=en): Omni Flash1.1 có video-to-video; các Veo3.1 Lite/Fast/Quality không hỗ trợ video-to-video theo bảng hiện hành. Không suy demo “remove object” là một nút chuyên dụng đã có trên account này.
3. [Google Flow: create videos](https://support.google.com/flow/answer/16353334?hl=en): voice references áp dụng cho Ingredients; không tự chuyển Frames/Veo và tuyên bố vẫn bind đúng saved custom K20.

Live: project/account đúng, mở asset `cae2fca6-bd20-4251-92e9-385c4a638f49`; direct editor nhận draft nhưng không hiện quote ở mặt giao diện đã kiểm. Vì vậy quay về composer và chọn đúng video “Potato man speaking at table”, toàn0–4s. Chip video cloud `fd1953fa-5f7d-4d73-84e5-ead858bbb01b`; đây là ID representation trong chip, không đổi asset editor ID. Chỉ một video ingredient, không thêm image/voice mới; nguồn đã chứa tiếng từ savedK20, chưa nghiệm thu tiếng thực.

Draft: `04_requests/C01B_BM_T02_REMOVE_TEXT_DRAFT_252.txt`, hash `2370455ce81b59aa39ed717e5b1354eda7ee75348d6c059ab0aa29a65c421559`, readback bằng file sau trim. UI xác nhận Omni1.1Flash / Ingredients / 720p / 9:16 / độ dài dựa trên nguồn4s / x1 / AgentOFF, **quote20**. Screenshot `C:/Users/PC/Downloads/du_an_nem_bui/252_BM_REPAIR_PLAN/video_edit_quote20_252.png`. Không click Generate; sau kiểm đã xóa prompt/ingredient khỏi composer, nút tạo disabled, livebalance vẫn992. Giao diện nhận prompt/quote không chứng minh backend sẽ nhận request hoặc output đạt.

## Lựa chọn và khuyến nghị sơ bộ

| Hướng | Hệ quả và giới hạn |
|---|---|
| **Sửa trực tiếp T02, chỉ phục hồi áo dưới chữ — khuyến nghị xin một lượt** | Nhiệm vụ khác sinh lại ảnh+thoại; tận dụng motion có sẵn. Quote20. Có nguy cơ áo rung/đổi mặt–miệng/đổi tiếng hoặc bị từ chối; chưa có tỷ lệ thành công kiểm chứng. |
| Sinh lại từ ảnh v2 bằng biến thể prompt | Đã lặp burn-in; chưa có giả thuyết cô lập đủ mạnh. Không khuyến nghị thêm lượt cùng route hiện tại. |
| Chuyển model/Frames hoặc công cụ inpainting ngoài | Chưa chứng minh giữ savedK20/khẩu hình/720p và khả năng truy nguyên nguồn; cần research, authority mới. Không tự mở API, cài tool hoặc chuyển model. |

REC232 từng bị tuyến edit từ chối “không thể chỉnh sửa lời nói” khi request có mouth/speaker reconstruction. Draft252 **không** yêu cầu sửa lời/miệng, chỉ phục hồi áo; khác nhiệm vụ nhưng không thể suy sẽ chắc được nhận. Nếu bị từ chối, dừng, ghi số dư thực; không tự retry hoặc né guardrail.

## Quyền chi cần owner bổ sung trước submit

Đề nghị **đúng một video-edit20credit**, không batch/retry, từ allocation tạo lại124 hiện còn, không mở reserve110. Ngoại lệ này vượt trần15/request và đưa cả đợt coverage từ14 lên34, vì vậy cần owner duyệt tăng trần đợt ít nhất34. Output cleanup sẽ là đầu ra thứ3 trong đợt; không tự dùng authority slot BR cũ làm cleanup. **BR vẫn chưa có quyền chi kế tiếp** dưới trần mới34; sau khi BM đạt phải trình lại quote/cap/output tương ứng, không tự cộng thêm.

Nếu chi đủ20: tổng episode108/500, còn392; tạo lại104, lượt đầu133, sau rough45, reserve110 đóng. Đây là dự tính, không thực chi. Số dư992 đã kiểm lại sau preparation252; vẫn phải kiểm live trước submit. OwnerB không phê duyệt ngoại lệ20 hoặc trần34.

## Kế hoạch kiểm sau một output, không hạ tiêu chuẩn

1. Tải native riêng, giữ originals; hash, 720×1280, frame count/timestamps, full decode và PCM.
2. Kiểm toàn bộ vùng chữ qua mọi frame; đặc biệt biênF22/23 vàF57/58 và vùng áo phục hồi. Nếu đổi timing phải map time lại, không áp biên cũ mù quáng.
3. Đối soát mặt/mắt/miệng/tay/đạo cụ, bối cảnh và nhịp với T02 theo frame tương ứng; không dùng đầu/đuôi môi khép làm proof wholeword.
4. Kiểm audio correspondence bằng PCM/timing; số tương quan hoặc hash không thay thực nghe. Nếu tiếng thay đổi không gọi original-preserved; giữ HOLD và trình tình trạng, không tự mux để lờ lỗi. Dù giữ source audio, originalT02 chưa được nghe/duyệt.
5. Reviewer khác maker kiểm nguồn/range; root đọc toàn báo cáo. Nếu hình sạch thì gửi actual media cho owner nghe riêng “Khoan”/K20/sắc thái và xem sync; thiếu actual AV evidence vẫn ghi UNKNOWN/HOLD.
6. Chỉ khi BM đủ nguồn/range/tiếng mới chuẩn bị BR từA80→C02F0. Các join A→BM→BR→C02 kiểm thật; chưa chốt EDL hoặc thời lượng BM từ native4s.

Nếu cleanup thất bại hoặc lỗi lớn mới, **STOP**, không tự thêm output. Chưa có dự báo xác suất số; chỉ xác định đây là nhiệm vụ hẹp hơn và tuyến được tài liệu/UI hỗ trợ, không tuyên bố chất lượng đã tăng.

## Tổng hợp vòng

Đã xác định: chữ thuộc native và owner không chấp nhận. Đã chốt: hình sạch, lời/giọng/canon giữ. Giả định cần kiểm: video-edit phục hồi áo mà giữ performance. Còn mở: ngoại lệ 20/trần 34, output sạch, audio/sync/cut. Phản biện độc lập `06_qc/C01B_clean_picture_repair_independent_252.md` đã hoàn tất, root đọc đầy đủ: đủ trình owner, không phải quyền submit hoặc nghiệm thu media. Bước tiếp: owner chốt quyền đúng một lượt; chưa submit.
