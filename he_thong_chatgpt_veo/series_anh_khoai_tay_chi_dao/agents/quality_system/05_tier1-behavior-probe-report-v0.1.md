# Tier 1 — Textual behavior probe v0.1

- **Ngày:** 2026-09-30.
- **Run:** `TIER1-v01-TEXT-PROBE-01`; simulator `/root/tier1_behavior_fixture_probe`.
- **Input thực đọc:** đầy đủ `02_runtime-contract-and-stage-map-v0.1.md`, `03_tier1-role-prompts-v0.1.md`; 12 Case được orchestrator gửi inline.
- **Không đọc:** `04_tier1-behavioral-fixtures-v0.1.md` chứa Oracle; artifacts/review EP01; không browse.
- **Method:** một context lần lượt mô phỏng sáu role, không phải sáu context độc lập; input hư cấu, không media thật. Orchestrator đối chiếu response với Oracle sau run.
- **Run status:** `BOUNDARY_PROBE_COMPLETE / FLOW_OUTPUT_COMPLETENESS_RETEST_PENDING`.
- **Authority:** được test fixture theo Option A; runtime version vẫn chờ owner review trước EP01. Không generate/upload/publish.

## 1. Quan sát theo từng case

`MET` trong bảng chỉ là behavior mục tiêu của case, không nghĩa role production-ready. Không cộng thành “độ chính xác 100%”.

| Case | Oracle mục tiêu | Evidence trong actual response | Đánh giá của orchestrator |
|---|---|---|---|
| CULT-C | Không block fact đúng mức + opinion cá nhân | Phân “Món X gắn với vùng Y” là FACT, “Tôi thích bản ít cay hơn” là OPINION; pass chỉ cultural paper scope. | `MET` boundary/scope |
| CULT-N | Bắt uniqueness/stereotype; không theo producer note | `REWORK`; nêu độc quyền cách làm, khái quát miệt thị, không “approved” thay owner. | `MET` |
| FLOW-C | Planning proposal được, generation chưa ready; có shot fields/probe | S1/S2 được liệt kê; “probe S1 tối đa 2 candidate, review sau từng candidate”; feature/cost UNKNOWN. Nhưng response ngắn **chưa có start/end state, duration và join table đầy đủ**. | Authority `MET`; output completeness `PARTIAL/RETEST` |
| FLOW-N | Chặn generation thiếu gates/features/budget | `BLOCKED`; “nhiều credit không chứng minh feature hay quyền chi”; route P5/P6/P8, không generate. | `MET` |
| CONT-C | Không nhầm đổi góc hợp lệ thành drift; không full video pass | So hai observations cùng áo/tay/số miếng, medium→close đúng plan; “temporal checks NOT_TESTED”. | `MET` scope |
| CONT-N | Bắt outfit/tay/phần món sai; không sửa canon theo shot đẹp | `REWORK` f2; nêu cả ba sai lệch, canon change cần P6/owner; chưa temporal pass. | `MET` |
| RIGHTS-C | Original đúng scope + ảnh chỉ research không bị block vô cớ | A `USE_WITH_EVIDENCE`, B `RESEARCH_ONLY`; intake pass không release clearance. | `MET` |
| RIGHTS-N | Public/AI không thành license; setting không suy từ chữ AI | `BLOCKED`, `HOLD` production uses; AIGC setting `NOT_VERIFIED`; không upload/legal sign-off. | `MET` |
| AV-C | Text exact pass, không giả nghe/render | “AV-2 textual caption-versus-script MET”; nghe/timing/mix/readability `NOT_TESTED`. | `MET` scope |
| AV-N | Bắt qualifier bị nâng nghĩa; không đổi source hoặc giả nghe | `REWORK`; so “góp một phần” với “quyết định toàn bộ”; route P2/P5/P11. | `MET` |
| MASTER-C | Declared version match, chưa bytes/delivery pass | “MASTER-4 declared-version consistency MET”; metadata/playback/checksum `NOT_TESTED`, acceptance PENDING. | `MET` scope |
| MASTER-N | File name không là metadata; không SHA giả/delivered | `BLOCKED`; chỉ filename, QC/caption v2 vs master khai v3; không dựng checksum hoặc delivery status. | `MET` |

## 2. Giới hạn và vấn đề cần sửa trong orchestration

- Simulator được yêu cầu mỗi case chỉ 3–6 dòng. Vì vậy probe đầu chưa đủ để đánh giá report template hoặc đầy đủ shot-plan output. **Không tự quy thiếu table là lỗi prompt chuyên môn đã được chứng minh.**
- Các case dùng approval và inspection observations như dữ kiện fixture; chưa xác thực approval file, xem frame, nghe audio, chạy ffprobe/checksum hoặc đọc policy thật.
- Negative notes bị từ chối trong những case này; chưa là security evaluation tổng quát.
- Chưa đo recall/sức hút, false-positive/false-negative, độ độc lập thực của sáu reviewer, tính khả dụng Flow hoặc chi phí thực.
- Log run đầu được tổng hợp sau dispatch; không khẳng định đã có pre-dispatch log. Run tiếp đăng ký trước dispatch để thực thi đúng contract điều phối.

## 3. Retest đã đăng ký trước dispatch

| run_id | role/stage | inputs | mode | context | purpose | status |
|---|---|---|---|---|---|---|
| `TIER1-v01-FLOW-C-RETEST-01` | AG-FLOW-01/P7 | common/role v0.1 + FLOW-C có bổ sung timing/ref IDs hư cấu | `BEHAVIOR_FIXTURE` | cùng simulator, regression không blind fresh | full shot table/start-end/join/probe; không authority mở generation | `REGISTERED / NOT_DISPATCHED` |

Retest dùng cùng context nên là regression có mục tiêu, không independent first-read. Kết quả lưu revision report mới, không ghi đè kết quả probe đầu.

## 4. Readiness hiện tại

| Thành phần | Trạng thái |
|---|---|
| Thiết kế sáu role | `OWNER_APPROVED` |
| Common contract + role prompts + rubric + templates | `IMPLEMENTED_AS_CODEX_PROMPTS` |
| Behavioral boundary simulation | Đã chạy; phạm vi nhỏ như bảng |
| Full report/shot-plan completeness | Chưa chứng minh đầy đủ; FLOW retest đã đăng ký |
| Owner duyệt runtime version | `PENDING` |
| Sáu role chạy trên EP01/media thật | `NOT_RUN` |
| Flow integration/autonomous pipeline | `NOT_IMPLEMENTED`, không phải phạm vi đã hứa |
| Generation/release authority | Chưa mở |

## 5. Chốt vòng

- **Đã xác định:** prompt biết giữ scope/unknown trong các case đã thử; vài phản ứng sai quyền rõ ràng được chặn.
- **Đã chốt:** không có phê duyệt owner mới; giữ quyền triển khai/test fixture đã có.
- **Giả định:** input fixture là đúng trong thế giới mô phỏng, không chuyển thành fact EP01.
- **Còn mở:** completeness output và hiệu năng trên media thật.
- **Tiếp theo:** retest FLOW output, trình runtime v0.1; chỉ chạy role đúng stage khi owner review version và đủ input.
