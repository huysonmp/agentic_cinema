# Hiệu chỉnh: baseline đầy đủ và khám phá Human × AI

- **Ngày:** 2026-09-29
- **Trạng thái:** discovery baseline
- **Thay thế:** mọi đề xuất rút gọn gate hoặc gọi thay đổi quy trình là “cải tiến” trước khi có pilot.

## 1. Sai lệch đã được xác định

Phân tích trước đã đưa ra ba kết luận không có đủ bằng chứng:

1. nhiều gate sẽ tạo gánh nặng human review;
2. giảm còn sáu formal gate sẽ tốt hơn;
3. nên chỉ viết hoặc triển khai một phần quy trình trước.

Hiện chưa có dữ liệu để kết luận như vậy vì:

- chưa chạy episode nào qua P0–P14;
- chưa có defect log, rework log hoặc acceptance data;
- chưa thử agent chuyên biệt ở từng stage;
- chưa biết artifact nào human phải tự tạo và artifact nào agent có thể chuẩn bị/kiểm tra;
- chưa đo chất lượng của mô hình `maker agent → critic agent → human decision`;
- chưa biết gate nào thực sự thừa hoặc thiếu.

Do đó, mọi nhận định về “tối ưu” lúc này chỉ là giả thuyết.

## 2. Baseline mới

### Giữ đầy đủ quy trình

- Giữ P0–P14 như 15 stage độc lập.
- Mỗi stage có input, output, agent support, independent review, human decision và trạng thái riêng.
- Chưa gộp stage, chưa bỏ gate và chưa giảm hồ sơ.
- Không dùng tốc độ, số thao tác hay số agent làm tiêu chí tối ưu ban đầu.
- Chỉ thay đổi quy trình sau khi có bằng chứng từ pilot.

### Mini được hiểu thế nào

`Mini` chỉ giới hạn:

- một series;
- một owner/operator;
- một episode pilot tại một thời điểm;
- Flow thủ công trước API;
- file-based source of truth trước database/cloud workflow engine.

`Mini` không giới hạn:

- số stage kiểm soát chất lượng;
- số agent chuyên biệt hợp lý;
- mức độ review, evidence, versioning và provenance;
- độ đầy đủ của QC và delivery package.

## 3. Mô hình Human × AI cần khám phá

Đơn vị cộng tác cơ bản đề xuất để **thử nghiệm**, chưa phải quyết định cuối:

```text
Orchestrator
  → giao stage cho Maker Agent chuyên biệt
  → Critic/Reviewer Agent kiểm tra độc lập theo rubric
  → Orchestrator tổng hợp khác biệt và evidence
  → Human xem phương án, ngoại lệ và quyết định
  → artifact/version được approve, rework hoặc reject
```

### Vai trò của orchestrator

- giữ workflow state và dependency giữa P0–P14;
- đưa đúng input version cho agent đúng stage;
- không tự thay thế domain agent khi cần chuyên môn;
- thu proposal, critique, open issue và conflict;
- không tự vượt human gate;
- cập nhật decision/change/defect log sau quyết định.

### Vai trò của Maker Agent

- tạo artifact chuyên môn theo stage contract;
- ghi assumptions, evidence, alternatives và confidence;
- tự kiểm completeness trước khi gửi review;
- không tự đánh dấu artifact của mình là accepted.

### Vai trò của Critic Agent

- đọc artifact bằng rubric độc lập;
- tìm omission, contradiction, unsupported claim và downstream risk;
- phân loại defect/severity;
- không sửa âm thầm làm mất dấu proposal gốc;
- đề xuất approve, rework hoặc reject cùng lý do.

### Vai trò của Human

- cung cấp taste, intent, context và authority;
- quyết định khi có trade-off hoặc xung đột giữa agent;
- phê duyệt quyền, chi phí, creative lock, exception và delivery;
- có thể override agent nhưng phải ghi rationale;
- không bị giả định là người trực tiếp soạn mọi artifact hoặc chạy mọi checklist.

## 4. Bản đồ agent chuyên biệt theo 15 stage để nghiên cứu

Đây là catalog ứng viên, chưa quyết định mỗi dòng phải là một process/model riêng.

| Stage | Maker Agent ứng viên | Critic/Reviewer ứng viên | Human quyết định gì |
|---|---|---|---|
| P0 Project setup | Project Governance Agent | Scope & Risk Reviewer | mục tiêu, authority, delivery, risk tolerance |
| P1 Series foundation | Series Strategy Agent | Positioning/Coherence Critic | audience, promise, taste, boundaries |
| P2 Research & evidence | Research/Evidence Agent | Fact & Source Auditor | chấp nhận nguồn, uncertainty, expert escalation |
| P3 Episode brief | Editorial Brief Agent | Brief Alignment Critic | message, hook promise, desired outcome |
| P4 Concept development | Concept Agents theo nhiều creative lens | Concept Evaluation Panel | chọn concept/trade-off, không chỉ chọn điểm trung bình cao nhất |
| P5 Script & narrative | Script Agent | Narrative + Factual Critics | voice, meaning, emotional intent, script lock |
| P6 Visual development | Visual Direction Agent | Style/Identity/Continuity Critic | visual taste, canonical identity, allowed variation |
| P7 Shot design | Shot Planning Agent | Coverage & Editability Critic | coverage, shot intent, fallback strategy |
| P8 Generation planning | Veo Prompt/Generation Planner | Feasibility, Rights & Cost Reviewer | request, references, experiment design, spend |
| P9 Veo generation | Generation Session Assistant | Output Triage/Provenance Critic | thao tác Flow, deviation, accept/retry/stop |
| P10 Selection & assembly | Edit Assembly Agent | Sequence/Narrative/Continuity Critics | selects, rhythm, pickup decision |
| P11 Post-production | Post Supervisor Agent | Audio/Text/Visual Finishing Critics | picture/audio/text lock và artistic exceptions |
| P12 Master QC | QC Orchestrator | các reviewer factual, visual, audio, technical, rights độc lập | waive/reject/approve defect |
| P13 Delivery | Delivery Manager Agent | Package/Manifest Read-back Auditor | acceptance và quyền release/publish |
| P14 Retrospective | Process Learning Agent | Causal Analysis Critic | thay đổi process nào được áp dụng từ version nào |

Một stage có thể cần nhiều agent song song về góc nhìn, nhưng không vì vậy mà tự động lấy majority vote. Human cần thấy disagreement và evidence.

## 5. Những câu hỏi phải test thay vì đoán

### Agent granularity

- Một agent theo stage tốt hơn hay một agent theo discipline dùng qua nhiều stage?
- Critic có thực sự độc lập nếu dùng cùng context/prompt/model với Maker?
- Stage nào cần nhiều creative agents để tạo diversity?
- Stage nào cần deterministic validator thay vì thêm agent?

### Human control

- Human cần xem toàn artifact hay chỉ change/diff, exception và disagreement?
- Human override agent ở loại quyết định nào?
- Gate nào tạo ra quyết định thực, gate nào chỉ xác nhận hình thức?
- Khi agent đồng thuận sai, cơ chế nào phát hiện?

### Quality

- Agent nào phát hiện lỗi sớm nhất và loại lỗi gì?
- Lỗi nào lọt qua nhiều stage?
- Reviewer nào có false-positive cao?
- Artifact nào đạt hình thức nhưng không giúp downstream?
- Độ nhất quán của series cải thiện hay giảm khi thêm agent chuyên biệt?

### Operational integrity

- Provenance có được duy trì đầy đủ khi qua nhiều agent?
- Version nào bị nhầm hoặc dùng sai?
- Tool/Flow action có bám đúng generation manifest?
- Agent có tự làm mờ uncertainty hoặc hợp lý hóa output Veo kém không?

## 6. Thiết kế pilot để tạo bằng chứng

### Pilot 0 — Dry run không tiêu credit

Chạy P0–P8 bằng một episode giả định hoặc episode thật chưa generate:

- mỗi stage dùng Maker + Critic;
- human quyết định sau khi xem proposal, critique và disagreement;
- ghi time chỉ để biết, không dùng làm mục tiêu;
- đo completeness, defect, rework, override và provenance;
- kiểm tra generation packet có đủ để người dùng thao tác Flow mà không phải tự suy diễn lại.

**Mục tiêu:** kiểm chứng process/agent collaboration trước khi credit bị tiêu.

### Pilot 1 — Một episode end-to-end

Chạy đủ P0–P14 với Flow thủ công:

- không bỏ gate;
- ghi mọi generation và raw candidate;
- QC theo nhiều reviewer chuyên biệt;
- delivery read-back;
- retrospective truy defect về stage nguồn.

**Mục tiêu:** tạo baseline chất lượng và defect leakage đầu tiên.

### Pilot 2 — Lặp lại có kiểm soát

Dùng episode thứ hai với cùng process version:

- không thay nhiều biến cùng lúc;
- kiểm tra lỗi nào tái diễn;
- chỉ thử một thay đổi process/agent configuration đã được Pilot 1 chỉ ra;
- so với baseline, không tuyên bố cải tiến từ cảm giác.

## 7. Evidence cần thu cho từng stage

```text
artifact version
maker agent + configuration
critic agent + rubric version
issues found by maker self-check
issues found by critic
human decision / override / rationale
rework count and origin
downstream defects traced back to this stage
provenance completeness
stage-specific quality score
```

Không dùng latency hoặc số bước làm metric chất lượng chính. Chúng chỉ là quan sát vận hành.

## 8. Khi nào mới được gọi là cải tiến

Một thay đổi chỉ được gọi là cải tiến nếu:

1. có baseline trước thay đổi;
2. nêu rõ metric chất lượng muốn cải thiện;
3. chỉ ra cơ chế vì sao thay đổi có thể tác động metric;
4. thử trên artifact/case tương đương;
5. không làm giảm quyền kiểm soát, provenance hoặc chất lượng khác ngoài ngưỡng;
6. human owner chấp nhận trade-off;
7. thay đổi được version và có đường rollback.

Nếu chưa đủ điều kiện, tên đúng là `hypothesis`, `candidate practice` hoặc `experiment`.

## 9. Điều đã xác định

- Yêu cầu là full-process, quality-first, Human × AI; không phải human-heavy hay automation-first.
- Agent chuyên biệt là một phần cần được khám phá và test nghiêm túc.
- Không có cơ sở hiện tại để rút gọn 15 stage hoặc gate.
- Chưa có cơ sở gọi các thay đổi được nêu trước là cải tiến.

## 10. Quyết định đã chốt

- Khôi phục P0–P14 làm baseline đầy đủ.
- Chưa gộp stage, giảm gate hoặc giới hạn số agent.
- Thử Maker + Critic + Human decision làm cấu hình nghiên cứu ban đầu.
- Chỉ thay đổi process từ evidence sau pilot.

## 11. Giả định đang sử dụng

- Codex là môi trường orchestrate agent và duy trì artifact.
- Người dùng trực tiếp thao tác Google Flow ở P9.
- Mọi agent output là proposal, không phải quyết định cuối.
- File-based source of truth đủ cho pilot, nhưng phải version/provenance đầy đủ.

## 12. Vấn đề còn mở

- Agent granularity và mức độc lập giữa Maker/Critic.
- Stage contract/rubric cho từng P0–P14.
- Cách tổ chức multi-agent trong Codex mà vẫn giữ context và version đúng.
- Delivery consumer, factual risk class và retention level.
- Episode/chủ đề dùng cho Pilot 0 và Pilot 1.

## 13. Bước tiếp theo đề xuất

Không tối ưu thêm. Trước hết thiết kế **experiment protocol cho Pilot 0**, rồi lần lượt tạo stage contract P0–P14 và chạy dry run để lấy baseline.

