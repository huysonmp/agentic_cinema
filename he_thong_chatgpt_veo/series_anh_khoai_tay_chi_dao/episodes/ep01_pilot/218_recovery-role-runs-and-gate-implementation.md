# 218 — Thực chạy vai chuyên môn và chốt chặn local

Authority: owner “1 A; 2 A; 3 A” đối với 217. Bounded local reads, role reports và gate code/tests; không browser/generation/API/credit/cài/publish/git. Không sửa media nguồn hoặc lời duyệt.

## Đăng ký run trước thực thi

| Run | Vai | Mode / phụ thuộc | Report | Trạng thái đăng ký |
|---|---|---|---|---|
| REC218-DIR-R1 | DIR maker | APPROVED_INTENT_RECOVERY_PROPOSAL | evidence/218/01_dir-maker.md | REGISTERED |
| REC218-DOP-R1 | DOP maker | FRAME_EVIDENCE_AND_DESIGN, chờ DIR | evidence/218/02_dop-maker.md | WAIT_DIR |
| REC218-ACT-R1 | ACT maker | FRAME_EVIDENCE_AND_PERFORMANCE_DESIGN, chờ DIR | evidence/218/03_act-maker.md | WAIT_DIR |
| REC218-EDIT-R1 | EDIT maker | SOURCE_RANGE_AND_CUT_PROPOSAL, chờ DIR | evidence/218/04_edit-maker.md | WAIT_DIR |
| REC218-CINE-R1 | CINE-LIGHT reviewer | COLD_FRAME_SCREENING_THEN_CRITERIA | evidence/218/05_cine-review.md | WAIT_MAKERS |
| REC218-PERF-R1 | PERF reviewer | COLD_FRAME_INTERPRETATION_THEN_CRITERIA | evidence/218/06_perf-review.md | WAIT_MAKERS |
| REC218-CONT-R1 | CONT/FOOD reviewer | SOURCE_STATE_AND_CUT_SCREENING | evidence/218/07_cont-review.md | WAIT_MAKERS |
| REC218-SIA-R1 | SIA/AV reviewer | CAPABILITY_AND_PROVENANCE, ear/AV phải có thực | evidence/218/08_sia-review.md | WAIT_MAKERS |

Actual dispatch/completion, context IDs, files thực đọc và scope được ghi bên dưới sau khi có bằng chứng. Bảng trên không nhận đã chạy.

## Target và capability

Current source N02 native hash `72cbaf7d9f66932002dfce1b1a57fa464935c315e84e54ae094fe29aa805a153`, audio202 hash `3c83b7d6188f5b973b0ef5c77ebc1fc16afde7c11827764c5302145741b736d4`; storyboard text214 đã duyệt, không có AV recovery master mới. Source216 có 240 frame và các cut/hints; source215 có bảng sàng lọc 12 ứng viên. Báo cáo trên frame/text không thay kiểm nghe hoặc chuyển động/AV liên tục.

Maker đọc contract, C-v0.6/178, quyết định212–217, media/ref trong allowlist. DOP/ACT/EDIT đọc contribution DIR sau khi có; không đọc contribution nhau trong vòng R1. Reviewer không đọc maker rationale/verdict hoặc root RCA211/216 trước cold phase nếu dispatch yêu cầu; tự quan sát media/frames rồi đối chiếu approved214/178. Không soi từ nhãn speaker để gán observed voice.

## Gate local — đăng ký triển khai

Triển khai validator/wrapper và hooks: frame-bound render mặc định PLANNING, finishing bắt buộc FINISHING evidence trước writes, delivery verification bắt buộc DELIVERY evidence trên đúng export. Kiểm roles/reviewer độc lập, target/input hashes, scope/capability, findings/closure, owner approvals và biến PLANNING thành DELIVERY. Chưa code/test thành công thì không ghi implemented.

Không tự tạo report PASS cho phim. Target thiếu full AV/hearing hoặc critical/major chưa đóng phải bị chặn; fixture PASS chỉ chứng minh validator, không chứng minh media đạt.

## Thực thi — maker contributions đã hoàn tất

Root đã đọc đầy đủ bốn báo cáo, không chỉ dùng final message của agent. Context riêng, DIR trước rồi DOP/ACT/EDIT nhận contribution DIR; ba vai sau không đọc contribution nhau trước R1.

| Run | Context thực | Output thực | Kết quả đúng phạm vi |
|---|---|---|---|
| REC218-DIR-R1 | `/root/rec218_dir` | `evidence/218/01_dir-maker.md` | PROPOSAL_COMPLETE, paper/sampled frames; các media gates HOLD |
| REC218-DOP-R1 | `/root/rec218_dop` | `evidence/218/02_dop-maker.md` | PROPOSAL_COMPLETE, design/sampled frames; chưa continuous visual/AV |
| REC218-ACT-R1 | `/root/rec218_act` | `evidence/218/03_act-maker.md` | PROPOSAL_COMPLETE, performance design/sampled frames; chưa diễn/khẩu hình media PASS |
| REC218-EDIT-R1 | `/root/rec218_edit` | `evidence/218/04_edit-maker.md` | PROPOSAL_COMPLETE, sampled frames + probe/hash/range; chưa render hoặc AV PASS |

Tên prompt DOP/ACT/EDIT trong brief ban đầu không khớp filename repo; các agent/root tìm và dùng đúng `03_cinematography-designer-prompt.md`, `04_character-performance-director-prompt.md`, `05_creative-edit-upgrade-v0.2.md`. Không bỏ contract vì sai tên.

Reviewer CINE mở cold phase sau DOP/EDIT hoàn tất, khi ACT đang chốt report; phase này chỉ quan sát media, không phụ thuộc contribution ACT. PERF mở sau cả bốn maker hoàn tất. Các context reviewer mới không nhận maker rationale hoặc root RCA, không tự review contribution của mình. Dispatch CONT có lần không được nhận vì runtime báo `agent thread limit reached`; đó là **NOT_STARTED**, không phải có báo cáo hoặc QC đã chạy. Root thực thi tiếp khi có slot, không gán verdict từ lượt dispatch thất bại.

## Mã chốt chặn đã triển khai và kiểm thử

Chi tiết/read-back: `evidence/218/09_gate-code-readback.md`. Validator + hooks ba đường local đã có; 85 test EP01 và 5 test finishing đạt, tổng90/90. Negative command thực chặn finishing thiếu gate trước tạo file; Test-Path output trả False. Những kết quả này là software fixture/integrity evidence, không production media PASS.

Owner approval ghi riêng tại `evidence/218/owner-tier4-approval.json`: scope local implementation/checkpoints, không finishing, delivery, paid generation hay publication. Không dùng approval tầng4 để vượt validator cần approval đúng media/hành động.

Source hash root đọc lại sau maker runs: N02 `72cbaf7d9f66932002dfce1b1a57fa464935c315e84e54ae094fe29aa805a153`, WAV202 `3c83b7d6188f5b973b0ef5c77ebc1fc16afde7c11827764c5302145741b736d4`, giữ nguyên. Không sửa/ghi đè media nguồn.

## Thực thi — reviewer đã hoàn tất, root đã đọc đầy đủ

| Run | Context độc lập với makers | Report | Actual scope / kết quả |
|---|---|---|---|
| REC218-CINE-R1 | `/root/rec218_cine` | `05_cine-review.md` | Cold ảnh trước script/board; sampled composition/light/cut, NEED_MORE_EVIDENCE/HOLD media |
| REC218-PERF-R1 | `/root/rec218_perf` | `06_perf-review.md` | Cold ảnh trước intent; chưa đọc được đủ causal joke từ mẫu, HOLD continuous performance |
| REC218-CONT-R1 | `/root/rec218_cont` | `07_cont-review.md` | Cold đối chiếu identity/table; A03 REWORK nếu nối cùng trạng thái bàn, food/temporal HOLD |
| REC218-SIA-R1 | `/root/rec218_sia` | `08_sia-review.md` | Probe/hash/PCM/provenance + phản biện code; giữ audio approvals201/203, hearing/reference/full AV HOLD |

CONT đã thực chạy sau slot được giải phóng, không dùng dispatch lỗi như run thành công. SIA đọc evaluator hiện có sau root mở rộng allowlist read-only để kiểm bridge; không đọc maker hoặc reviewer khác. Root đã đọc lại bản cuối của cả tám báo cáo. Reviewer không tự sửa media, approve take hay ghi PASS giả.

SIA chỉ ra thiếu binding từng lượt/reference và scope/capability đóng lỗi trong snapshot mã đầu; root bổ sung cầu nối evaluator SIA, closure checks. SIA phát hiện thêm offscreen approval cũ có thể được nhận chỉ bằng file/hash; gate recovery hiện chặn offscreen toàn lượt, không tái dùng203 thay214. SIA đọc lại đúng snapshot cuối và ghi MITIGATED_CODE_INSPECTION_NOT_TESTED, không tự nhận đã chạy unit tests hoặc nghe phim. Root regression sau sửa: **91 tests EP01 + 5 finishing, tổng96/96 OK**. Log96 thay summary90 về phiên bản hiện hành, không xóa các vòng kiểm trước.

Snapshot mã cuối: recovery gate `dba5141217112df41825ef9be32f5674e286e3b1e9fa50e7e0cb8047ae4f816e`; tests `1d191a2f311929396ddba262a3fe6179fa887e69aeb31266cc08aaa209f8bfc2`; finisher `b97351f00f2214f44da7c5d80197e9d464cb22cb87849a61343a6dbca0995aec`; verifier `640ee9db2d32f324cf8f66754b05b484cf2df6f245ad8f0c75934a9f8fdf4d60`. SIA report cuối `85e68cdba6807b25e1d5d2c5dacc9d5765b2c943fb895edd4ba82e57acd0a666`. Checksum này là đối soát hồ sơ, không đóng media findings.

## Kết quả lượt triển khai và bước tiếp

Hoàn tất bounded local role execution và gate implementation/tests theo approval tầng4. **Chưa hoàn tất recovery phim**: không có G1 animatic đủ chín nhiệm vụ, N02 proof hoặc full recovery AV mới; không mở finishing. Không paid generation/browser/API/cài mới/git/publication. Báo cáo ngắn cho owner và gap map G1 tại `219_recovery-execution-readback-and-g1-gap-map.md`.
