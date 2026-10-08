# REC249 — Review hình native độc lập BM T01

- Kết luận: HOLD / BLOCK dependency BM→BR theo coverage đã duyệt; chưa chọn range BM, không tự retake.
- Đã đối chiếu ảnh reference `C01B_BM_START_v1_CHATGPT_FOR_REVIEW_248.png`, hai board 6fps và PNG native F0/F12/F36/F40/F60.
- Quy ước: F là chỉ số bắt đầu từ 0; file PNG bắt đầu từ 00001. Review này là hình lấy mẫu, không phải xem/nghe AV liên tục.
- Nguồn: `EP01_720_C01B_BM_T01_NATIVE.mp4`; asset `d9b0f984-2153-4a78-81e9-db73a50bf160` theo bàn giao root.
- SHA-256 từ `native_evidence.json`: `33ccb60ce91eac26620040944811d16e6f566ee3110aef2a15d5b5f4d880f60a`.
- Evidence ghi 720×1280, 24fps, 96 frame/4s, full decode thành công và nguồn không đổi; đây chỉ là bằng chứng kỹ thuật.

## Blocker quan sát trực tiếp

- Chữ “Khoan” trắng viền đen xuất hiện ngay trong PNG nguồn, ở vùng bát/tay Khoai: F12/0,500s và F36/1,500s xác nhận rõ; board có chữ tại mọi mẫu F12–F36.
- F8/0,333s chưa có chữ, F40/1,667s đã hết chữ; chưa đo biên xuất hiện/biến mất chính xác từng frame.
- Đây là chữ nằm trong hình native, trái yêu cầu không caption/lettering; flag caption stream trong probe không phủ định chữ burn-in.
- Reference cho thấy Đào nhìn xuống vùng bàn/món; F0 native đã hướng mắt lên/trái về Khoai, không giữ trạng thái mắt hạ của reference.
- Đào sau đó hạ mắt (F32–F40), rồi hướng mắt về Khoai lại ở F60/2,500s và các mẫu cuối. Không đáp ứng “mắt hạ suốt BM”, đã có chuyển hướng phản ứng trong BM.
- Tay trong khung của Đào ở reference/F0 cong và hover; F36/F40 cho thấy tay hạ, ngón khép hơn và đặt sát mặt bàn. Không giữ nguyên hover như yêu cầu.
- Không suy chuyển động tay trong khung thành “đã buông contact mép phải”; tay ngoài khung vẫn UNKNOWN.

## Range và lời trọn

- Mặt và khẩu hình Khoai rõ; board có mở miệng ở F8/F12/F16, sau đó khép lại. Chỉ quan sát được chuỗi hình, không xác nhận lời “Khoan” trọn hoặc lip-sync.
- Khoảng khẩu hình mở quan sát được chồng với chữ burn-in. Cắt bỏ toàn đoạn có chữ sẽ bỏ một phần chuỗi khẩu hình; chưa có bằng chứng về range sạch chữ chứa lời trọn.
- Các mẫu F40 trở đi không có chữ nhưng Khoai đã khép miệng, Đào đã đổi trạng thái; không thể dùng đuôi này để tự chứng nhận BM nói trọn “Khoan”.
- Ngay cả nếu tiếng sau này đạt, blocker chữ và trạng thái vẫn chặn chọn BM theo brief hiện hành; không mở BR từ take này.

## Điểm đạt trong mẫu và giới hạn

- Camera giữ bố cục ổn định trong các mẫu; hai tay Khoai vẫn nghỉ trên bàn, mặt rõ, không thấy reach/ăn/uống hoặc di chuyển đĩa trong mẫu.
- Không chứng nhận mọi frame, continuity ngoài khung, điểm nối với C01A/BR/C02 hay chất lượng phim đầy đủ.
- `native_evidence.json` ghi `actual_listening=NOT_PERFORMED`, `lip_sync=NOT_CERTIFIED`; có audio stream không phải bằng chứng đúng K20/đúng từ/không lời thừa.
- Không nghe, chép tiếng, sửa media, tạo mới hay chi credit. Giữ nguồn; root cần báo blocker và chốt hướng xử lý trong quyền hiện có trước bước sản xuất tiếp.
