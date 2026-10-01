# EP01 — Duyệt hướng giọng và vòng kiểm tổng thể

2026-10-01, Asia/Saigon. Owner: “hướng ‘trầm ấm, kể thân mật, ký ức có nét cười kín’ này đúng chất Khoai; duyệt bổ sung agent phản biện quay phim–ánh sáng và chạy vòng kiểm tổng thể nữa”.

## Decision lock

- Hướng diễn xuất giọng Khoai trong 92 được duyệt: trầm ấm, thân mật, ký ức có nét cười kín. Không đồng nghĩa V01 được chấp nhận hoặc voice identity đã khóa.
- Duyệt thiết kế CINE-LIGHT và chạy review actual V01/reference cùng hồ sơ script/shot/context. Role contract: agents/audio_edit_quality/09_cinematography-lighting-critic-contract.md.
- Root tổng hợp cinematography/light + directing/performance/context + transition/technical/voice evidence; thiếu nghe/full playback/cảnh khác nhau phải giữ UNKNOWN. Không gọi một reviewer là toàn bộ quality panel đã chạy.
- Không cấp quyền thử lại V01, chạy V02, Quality, API hoặc credit mới. V02 giữ HOLD theo 92/88. Approval agent không là approval generation.

## Thực thi

Run EP01-CINE-R1: subagent độc lập đọc contract và visual evidence trước đối chiếu SoT; không đọc root visual verdict/owner preference feedback trước first pass. Report riêng tại agents/audio_edit_quality/reports/06_cine-light-v01-r1.md. Root aggregate tại 94; completion ghi sau khi report thực có và kiểm lại.

Execution complete: report06 thực đã lưu, root đọc toàn bộ và adjudicate nguồn chữ/constraint gesture trong94. Review hoàn tất trong phạm vi still/sample + paper/context; không full playback/hearing hoặc production pass. Role chưa independent fixture-qualified. Request95 đã soạn nhưng chưa submit, không credit.

Đã xác định: hướng giọng mong muốn và quyền review. Đã chốt: hai approval trên. Giả định: dùng V01 hiện hành và table v0.8 làm phạm vi vòng đầu. Còn mở: candidate giọng mới, actual full motion/listening và transition giữa cảnh. Bước tiếp: chạy review, trình các sửa cụ thể và chuẩn bị request voice mới, chưa submit.
