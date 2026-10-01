# AEQ-v0.1 — Approval và đăng ký chạy thử

2026-10-01 Asia/Saigon. Owner trực tiếp trả lời `chấp thuận, chạy thử đi xem nào` sau đề xuất bốn vị trí voice/ghép lời/ghép cảnh/kiểm bản ráp.

APPROVED: xây contract, fixture và chạy bốn vai trò trong Codex; V01 có thật và diagnostic local dùng bản sao nếu cần. Không đổi script/canon, không Gemini/API, upload, generation, credit, Quality, release hoặc thay final owner acceptance. Flow là ưu tiên ráp production sau khi đủ clip đạt gate. Bài thử paper/diagnostic không thay P6/P9/P10/P12 approval.

| Run | Role | Scope | Registration |
|---|---|---|---|
| AEQ-V01-R1 | AV-VOICE | V01 evidence + voice fixtures | REGISTERED, chưa dispatch tại mốc này |
| AEQ-DLG-R1 | DLG-EDIT | bảng dựng lời + fixtures | REGISTERED, chưa dispatch tại mốc này |
| AEQ-EDIT-R1 | EDIT | bảng dựng cảnh + fixtures | REGISTERED, chưa dispatch tại mốc này |
| AEQ-CUT-R1 | AV-CUT | kiểm độc lập fixture điểm nối + local diagnostic | REGISTERED, chạy sau khi có diagnostic evidence |

Context từng vai trò mới, không nhận đáp án `08_oracle-and-root-verification.md` hoặc report khác ở lượt đầu. Orchestrator đối chiếu oracle sau run; output tại `reports/` đúng role. Đây là prompt agents, không daemon hoặc agent tự vận hành Flow.

## Dispatch và actual completion log

| Run | Context | Actual input/access | Outcome |
|---|---|---|---|
| AEQ-V01-R1 | /root/aeq_voice_test | contract + V fixtures + V01 JSON/log/request85/run88, không hearing/playback | reports/01_voice-r1.md; fixture responses complete, actual OWNER_LISTENING_REQUIRED |
| AEQ-DLG-R1 | /root/aeq_dialogue_test | contract + D fixtures, paper only | reports/02_dialogue-r1.md; root phát hiện D-A tự gán30s, REWORK |
| AEQ-EDIT-R1 | /root/aeq_scene_test | contract + E fixtures, paper only | reports/03_scene-r1.md; root kiểm fixture behavior, không production edit |
| AEQ-DLG-R2 | /root/aeq_dialogue_test | đăng ký trước followup; cùng allowlist + root finding DLG-ROOT-01 | RETEST_REQUESTED; giữR1, output02_dialogue-r2.md |
| AEQ-CUT-R1 | /root/aeq_cut_audit_test | đăng ký trước dispatch; contract/C fixtures/07 actual diagnostic + raw manifest/ASR/file + probe read-only | DISPATCHED; output04_cut-audit-r1.md chờ root đọc |

### Completion ưu tiên hơn các checkpoint phía trên

AEQ-DLG-R2 COMPLETE: report02_dialogue-r2.md; root xác nhận closureDLG-ROOT-01, không numerical30sallocation thiếuinput. AEQ-CUT-R1 COMPLETE: report04_cut-audit-r1.md; independentprobe/hash actualcontrol8s/repeat13.5s, duplicateB detection vàscope limits đúng. Root verification08:13/13behaviorcases afterretest,5/5unit tests; không production/audio/lip-syncpass. Bốn vai trò đã thực chạy; không suy promptfileexistence làrun.
