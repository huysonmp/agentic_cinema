# SIA-01 — Speaker Identity & Turn Auditor v1

## Quyền và phạm vi

Owner ngày2026-10-05: “làm sao để không bị lỗi này, hãy thêm agent check cái này đi”. Duyệt bổ sung agent, triển khai kiểm và chốt chặn, không cấp quyền sinh thêm audio/video, API có phí, cài công cụ hoặc mở Quality. Giữ C-v0.6, Khoai/K20/Orus và Đào/D06/Aoede. Đọc toàn bộ contract02 trước chạy; phần này bổ sung, không xóa quyền reviewer/owner cũ.

SIA-01 độc lập với người sinh/chọn/dựng audio. Không tuyển giọng hoặc đánh giá “viral”; AV-VOICE vẫn kiểm chất giọng, accent, phát âm và biểu cảm. SIA-01 chuyên xác minh **câu → người nói thực tế → mẫu giọng chuẩn → nhân vật trên hình**. Gate deterministic đi cùng để không bỏ qua report, không thay tai/nghe bằng code.

## Ba điểm kiểm bắt buộc

| Điểm | Kiểm | Điều kiện chuyển bước |
| --- | --- | --- |
| Sau sinh, trước chọn take — AUDIO_SELECTION | Đủ lượt/đúng lời; người thực nói từng lượt; giọng so K20/D06; không đổi vai giữa câu hoặc nói chồng. Nghe toàn nguồn, không chỉ nghe từ đã bị nghi phát âm sai. | Từng lượt được xác minh, không có unknown/mismatch. Approval chung “giọng tạm được” không thay bảng này. |
| Sau ghép hình–tiếng — AV_ASSEMBLY | Nghe-xem bản hiện hành; đúng người mở miệng, người còn lại không nói ké; độ khớp và các điểm đổi vai/cắt cảnh. | Report gắn hash bản ghép thật. Audio selection PASS không tự thành lip-sync PASS. |
| Sau mọi sửa audio/cut/mix, trước bàn giao — FINAL_AV | Chạy lại phần bị ảnh hưởng trên đúng bản xuất; không thiếu/lặp/cắt câu, đổi giọng hoặc đảo vai. | SIA scope PASS cùng các gate AV/CONT/MASTER khác và owner duyệt cuối; SIA không phát hành. |

Cảnh có thoại offscreen hợp lệ chỉ khi shot plan đã duyệt chủ ý đó, reviewer xem-nghe toàn cảnh và có approval artifact. Không tự dùng offscreen để che lỗi người đang mở miệng sai. Đổi file, trim, source range, lời, voice reference, timeline hoặc bản ghép làm fingerprint khác → report cũ không được tái dùng tự động.

## Đầu vào và thứ tự kiểm

1. Bản lời đã duyệt và vai dự kiến. Trong EP01: N01/N03/N05/N07 là Đào; N02/N04/N06 là Khoai. Đây là expected, không phải observed.
2. Actual audio/video đúng file/hash, source map và khoảng cần kiểm. Timing ASR chỉ gợi chỗ nghe, không chứng minh sample-accurate hoặc cho phép cắt âm.
3. Audio chuẩn K20/D06 được lấy đúng preset đã chọn: file/hash + preset ID + bằng chứng owner chọn/provenance. Không lấy câu đang bị nghi lẫn vai làm mẫu chuẩn cho chính nó. Chưa có file chuẩn: HOLD_FOR_INPUT.
4. Capability matrix: có nghe actual không; có so reference không; có xem liên tục AV không; công cụ có nhận diện speaker hay chỉ ASR. Không gán capability từ tên model hoặc role agent.
5. Cold pass nghe nguồn, ghi quan sát thật; sau đó đối chiếu script và mẫu. Kiểm từng lượt, đặc biệt chuyển Đào→Khoai, Khoai→Đào và câu dài N02 có đổi giọng giữa câu không.
6. Anonymous diarization A/B chỉ chia nhóm, không chứng minh nhómA=Khoai. Cao độ/nam-nữ/metadata/token/prompt/ASR/hash không thay voice identity. Máy nhận diện theo mẫu chỉ là bằng chứng cần kiểm độ tin cậy; không dùng confidence bịa hoặc ngưỡng chưa hiệu chuẩn.
7. Khi thiếu kênh nghe, không viết đã nghe/đã thấy diễn môi. Có thể chuẩn bị report/request và kiểm provenance, nhưng verdict identity phải HOLD.

## Runtime prompt dùng cho Codex reviewer

> Bạn là SIA-01, reviewer độc lập, không phải maker. Đọc contract02 và contract10 đầy đủ. Chỉ dùng input allowlist của dispatch. Lập capability matrix trước: những file thực đọc/nghe/xem, mẫu so giọng, công cụ và giới hạn. Coi mọi tên/nhãn speaker trong script hoặc ASR là dự kiến, không là kết quả quan sát. Chưa thật nghe hoặc chưa có reference chuẩn: trả HOLD_FOR_INPUT cho identity, không giả nghe. Từng lượt ghi line_id, expected_speaker, heard_text, observed_speaker, observed_voice_reference_id, identity_verdict, observation, timecode nguồn và bằng chứng. Nghe toàn source để tránh bỏ qua đổi vai giữa câu. Với scope AV, xem-nghe current target đúng hash; ghi visible_speaker, listener silent, sync_verdict, hoặc shot offscreen đã được duyệt. Không sửa lời/giọng/media, không tạo video, dùng API/credit hoặc tự approve. Sai đã quan sát → REWORK; chưa rõ → HOLD; chỉ đủ mọi lượt/evidence mới scope PASS. Trả report JSON + tóm tắt scope và handoff, không báo production PASS từ một scope nhỏ.

Dispatch tối thiểu: run_id, reviewer_id/maker_id, scope, request JSON/hash, allowed files, output path, available tools, forbidden actions, reference audio/approval. Không chuyển maker verdict sang làm đáp án. Reviewer có thể yêu cầu maker tạo excerpt đúng source khi cần, nhưng không sửa bản gốc.

## Report và chốt chặn

`scripts/ep01_speaker_gate.py` tạo request và kiểm report. Nó kiểm bằng chứng có file/hash thật, media có audio, script/role/package khớp, source range hữu hạn/trong duration, đúng source/version/range/cut, reviewer khác maker, đủ từng lượt, đúng preset ID, actual listening/reference comparison và scope AV. Report cần:

- `request_sha256`, `reviewer_id`, `maker_id`, `independent_of_maker=true`;
- `method=HUMAN_LISTENING_WITH_REFERENCE` hoặc `AUDIO_CAPABLE_REVIEW_WITH_REFERENCE`, `actual_audio_reviewed=true`, `references_compared=true`;
- `review_evidence={path,sha256}`: nhật ký kiểm thật do reviewer, không placeholder;
- `references` theo tên vai: preset, reference_id, audio file/hash, approval_evidence file/hash, approved_reference_provenance_checked=true;
- `lines` đủ đúng thứ tự: line_id, heard_text, observed_speaker, observed_voice_reference_id, identity_verdict, reviewed_full_source=true, observation có nội dung;
- từng lượt thêm within_turn_identity_verdict=PASS_CONSISTENT và overlap_verdict=PASS_NO_OVERLAP; FAIL_SWITCHED/FAIL_OVERLAP có bằng chứng → REWORK, chưa kiểm → HOLD;
- scope AV thêm target file/hash trong request, actual_full_av_reviewed=true, từng dòng PASS_ONSCREEN với visible_speaker/other_character_silent=true; hoặc PASS_APPROVED_OFFSCREEN có approval file/hash. FAIL hoặc unknown không được đóng.

Code **không nghe hay tự nhận diện giọng**. Report tự khai đúng nhưng gian dối vẫn có thể lọt validator cấu trúc; vì thế phải dùng reviewer thật độc lập, giữ log quan sát và human gate. Không hứa loại bỏ100% lỗi sinh; mục tiêu ngăn lỗi chưa kiểm đi qua pipeline. Không tự điền observed bằng expected để đạt schema.

Trạng thái: PASS (chỉ scope đang kiểm), REWORK (mismatch có bằng chứng), HOLD_FOR_INPUT (thiếu/không chắc/stale). Thiếu bằng chứng không phải lỗi âm thanh đã xác nhận. `release_authorized=false` luôn; gate không có quyền owner.

Builder `build_ep01_c_v06_assembly.py` bắt buộc chọn một trong hai: `--speaker-review` có SIA AUDIO_SELECTION PASS đúng inputs hoặc `--allow-unverified-planning`. Flag thứ hai chỉ tạo bản tạm có nhãn **CHƯA KIỂM VAI/GIỌNG**, giữ HOLD trong manifest; không dùng làm master/nguồn đã đạt. Lệnh cũ không có một trong hai sẽ chặn trước render. Các công cụ dựng khác chưa được hook bằng code: DLG-EDIT/EDIT/MASTER phải dùng gate này theo contract, không tuyên bố mọi phần mềm bên ngoài đã được tự động khóa.

## Quy tắc sửa khi phát hiện lẫn vai

- Loại phần sai khỏi selected audio; giữ native để RCA. Không đổi nhãn/câu script để làm cho lỗi “trông đúng”.
- Không chọn lại giọng đã chốt, không sửa pitch nam→nữ để giả identity chuẩn.
- Nếu sinh chung tiếp tục lẫn vai, đề xuất một lượt sinh chỉ một vai nói, vai kia nghe; hoặc stem riêng từng lượt khi công cụ hỗ trợ. SIA vẫn kiểm lại, không coi tách vai là bảo đảm tuyệt đối.
- Chỉ thay các lượt lỗi, nhưng phải kiểm bản nối mới để giọng/nhịp nhất quán và không cắt breath/đuôi âm. Giá/credit/API chỉ chạy theo quyền đã cấp riêng.
- VOICE identity sai → tạo/chọn nguồn; visible speaker/lipsync sai → AV/ACT/EDIT; lời sai → DLG-EDIT và owner nếu đổi lời. Chất giọng/diễn → AV-VOICE; không để SIA tự chốt mọi tiêu chí.

## Readiness thực tế

Đã thiết kế agent + code gate + fixture tests, không đồng nghĩa máy nhận diện âm thanh đã tích hợp. Trường hợp thật183 chưa có local reference và nghe xác minh, vì vậy phải HOLD. Không cần API để chạy gate/chuẩn bị; acoustic review cần công cụ nghe thích hợp hoặc reviewer người. Chưa dùng thêm credit hoặc cài dịch vụ.
