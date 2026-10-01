# EP01 — Kết quả thử bốn agent voice và dựng

2026-10-01, Asia/Saigon. Owner duyệt: `chấp thuận, chạy thử đi xem nào`.

## Kết quả để owner xem

Đã xây contract và chạy bốn vai trò trong các context Codex riêng. Một lỗi của agent ghép lời được root phát hiện, yêu cầu sửa và kiểm lại; không báo đạt ngay lượt đầu. Không gọi Gemini/API, không tạo hoặc ráp/export mới trên Flow, không tiêu credit. Media gốc V01 giữ nguyên.

| Vai trò | Đã thử | Kết quả và giới hạn |
|---|---|---|
| Voice Quality Auditor | V01 JSON/ASR/log thực + 3 fixture | Ghi hai nghi vấn hồi/hội và rang/răng; không quy ASR thành phát âm sai. Có listening tickets kèm timecode. Chưa nghe, chưa xác nhận voice/lip-sync. |
| Dialogue Assembly Editor | 3 fixture + một lượt kiểm lại | Bác cut trong từ “mà”; giữ lời và native audio. R1 tự chia 30 giây cho ba câu không căn cứ → root yêu cầu sửa; R2 bỏ allocation, ghi timing UNKNOWN. |
| Scene Assembly Editor | 3 fixture/paper EDL | Phát hiện thiếu ý định ăn, phát hiện và đổi hướng; không cứu joke bằng thêm câu. Lập hai phương án cut giữ các beat, chưa kiểm media hoặc chọn take production. |
| AV Sync & Cut Auditor | 4 fixture + diagnostic/probe/hash/ASR thực | Nhận ra duplicate B và thời lượng 13,5 giây thay vì 8 giây; bác dùng QC bản cũ cho bản mới. Control đạt kiểm nối kỹ thuật giới hạn, không xác nhận continuity, voice hoặc production. |

Root review: 13 tình huống hành vi xử lý phù hợp sau một lượt kiểm lại; 5 unit tests mapping đạt (control, repeat, reorder, thay version, thay trim). Đây là tập thử nhỏ, không bằng chứng agent đủ nhạy với mọi lỗi production hoặc phản ứng khán giả.

## Hai media diagnostic thật — không phải clip final

Root chia V01 thành A[0–2,5 giây] và B[2,5–8 giây], rồi dùng FFmpeg nối trên bản sao. Không có clip cảnh khác hoặc duyệt safe-cut ở 2,5 giây bằng nghe. Cả hai được encode lại: H264 720×1280/24fps, AAC 48kHz stereo.

- `control.mp4`: A→B, thời lượng đo 8,000 giây. SHA256: `088d4ac5005e03343016cd4388d08a58d3fcb832a08bcd29121e3b51184709e0`.
- `repeat.mp4`: A→B→B, thời lượng đo 13,500 giây. SHA256: `2638598b2017c181768ea79222ebb812a8f5ec6eb59f87be3f9d59ce244176d9`. Có lỗi chủ đích để thử reviewer, không sửa hoặc đưa vào sản xuất.

ASR nhận lặp:

- “Bếp nhà anh, hội bé.” tại khoảng 2,44–4,16 giây và 7,92–9,66 giây.
- “Mẹ rang gạo, anh đứng chờ.” tại khoảng 4,78–6,86 giây và 10,18–12,36 giây.

Đây là timestamp ước lượng ASR, không phải acoustic boundary. “rang” nhận đúng ở bản repeat nhưng thành “răng” ở lần ASR V01 trước: không lấy một transcript để kết luận chất lượng phát âm.

Owner files: `C:/Users/PC/Downloads/du_an_nem_bui/AEQ_agent_test_r1/`, gồm media, manifest, ASR, text, bản tổng hợp và report copies. Project diagnostic: `artifacts/voice-assembly/aeq-r1/`; repeat ASR: `artifacts/voice-assembly/aeq-repeat-asr-r1/`. Generated media/caches không commit.

## Hồ sơ triển khai

[Approval/log](../../agents/audio_edit_quality/01_owner-approval-and-run-log.md), [contract/roles](../../agents/audio_edit_quality/02_contract-and-role-prompts.md), [root verification](../../agents/audio_edit_quality/08_oracle-and-root-verification.md).

Reports: [voice R1](../../agents/audio_edit_quality/reports/01_voice-r1.md), [dialogue R1 giữ lịch sử](../../agents/audio_edit_quality/reports/02_dialogue-r1.md), [dialogue R2 hiện hành](../../agents/audio_edit_quality/reports/02_dialogue-r2.md), [scene R1](../../agents/audio_edit_quality/reports/03_scene-r1.md), [cut-audit R1](../../agents/audio_edit_quality/reports/04_cut-audit-r1.md).

## Readiness và bước tiếp

- Đã xác định: bốn role có contract/report/test thật; bản ghép lỗi được phát hiện; một lỗi maker được kiểm lại và sửa. Không tự đổi script.
- Quyết định: approval cho agent test, local tooling và ưu tiên Flow ghép theo 89. Giữ native audio, không rephrase, không tự generation/credit/release.
- Giả định: fixture không phải production; map được render log/manifest/probe/ASR hỗ trợ, chưa có full playback review. Khả năng nghe của công cụ chưa thay đổi.
- Còn mở: owner nghe V01 và đánh giá giọng; lip-sync; V02 chưa chạy; multi-scene joins, choreography, caption và master chưa thử. Không coi 13/13 behavior cases đạt là quality approval.
- Bước tiếp: owner nghe V01, ưu tiên hai nghi vấn theo voice R1; đủ listening gate 88 mới chạy V02 Lite trong ngân sách còn 10 credit. Khi đủ production takes đã chọn, maker lập source/line/cut map thực và ráp Flow; AV/CONT/PERF kiểm độc lập bản export rồi MASTER/owner duyệt.

Các số 37 giây/30 giây trong fixture chỉ là dữ liệu giả để kiểm hành vi, không phải constraints mới của EP01 và không cần owner chốt chúng.
