# Roles and Approval Matrix

- **Version:** P0-v1
- **Status:** proposed

| Vai trò | Trách nhiệm | Quyền quyết định |
|---|---|---|
| Owner | creative intent, risk tolerance, exception, final acceptance | cuối cùng ở mọi stage |
| Codex Orchestrator | state, dependency, version, register, tổng hợp conflict | không tự approve |
| Maker Agent | tạo artifact theo stage contract, nêu assumption/evidence | proposal only |
| Critic Agent | review độc lập, defect/severity, đề xuất disposition | recommendation only |
| Specialist Reviewer | review văn hóa/chuyên môn khi nguồn mâu thuẫn hoặc nhạy cảm | advisory; owner quyết định |
| Flow Operator | owner trực tiếp thao tác request đã duyệt | không tự đổi request thiếu log |

## Trạng thái quyết định

- `APPROVED`: đúng version và được phép sang stage sau.
- `REWORK`: trả lại với defect/rationale.
- `REJECTED`: phương án không tiếp tục, vẫn giữ hồ sơ.
- `BLOCKED`: thiếu authority/evidence/input bắt buộc.
- `SUPERSEDED`: có revision mới thay thế.

Owner có thể override recommendation của agent nhưng override phải có rationale.

