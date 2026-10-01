# Episode Context Gate — đề xuất bổ sung, chờ owner duyệt

2026-10-01. PROPOSAL_ONLY / NOT_IMPLEMENTED_AS_NEW_AGENT / NOT_BEHAVIOR_TESTED. Owner hỏi có cần agent nhắc bối cảnh vì các phần sản xuất bị rời rạc. Không lấy câu hỏi này làm approval agent mới.

## Chẩn đoán có bằng chứng

PROD7 contract02 đã yêu cầu exact script/authority/inputs; CTD giữ story intent, ART nhận script/shot needs, PROMPT phải trace request→script. Tuy nhiên batch73 phân dispatch food và count/layout, không có context preflight hoàn chỉnh trước maker prompt; chưa kiểm toàn dependency món–lá–chấm–nhân vật–hành động. Ba ảnh đủ props vẫn REWORK/HOLD. Thêm tên agent không tự đóng lỗi orchestration.

## Khuyến nghị

Giữ root chịu trách nhiệm bối cảnh toàn dự án; thêm **Episode Context Gate** trước mỗi request sản xuất/sửa có ảnh hưởng scene. Trước mắt dùng role CTD hiện có cho paper context check và CONT cho actual scene check. Nếu owner muốn tách người chịu trách nhiệm, thiết kế một **Episode Context Steward** dưới đây, không phải agent nhắc nhở chung chung và không thay agent chuyên môn.

## Role draft AG-CTX-01 — Episode Context Steward

Mục tiêu: không có maker request được gọi READY khi thiếu/mâu thuẫn context trọng yếu. Chỉ PAPER_REVIEW; không tạo nội dung/media, không duyệt asset, spend, sửa canon hoặc quyền release. Root/operator không dùng reviewer verdict làm owner approval.

Inputs mandatory: exact latest script+approval; P0/P1 relevant canon; P2 claims/source boundary; scene/treatment/shot status; selected P6 refs+version/status; rights/use constraints; latest decisions; open findings; proposed request+input manifest. Thiếu shot ở P6 không bịa shot: đánh scope P6 và ghi dependency chưa có.

Checks:

1. **CTX-1 Current truth:** quyết định mới ưu tiên lịch sử; mỗi source có version/status, không lẫn demo/rejected/approved.
2. **CTX-2 Story trace:** từng prop/layout/action constraint nối beat cụ thể hoặc labeled staging assumption; không thêm hành động/canon/claim ngầm.
3. **CTX-3 Whole-scene function:** món, lá, chấm, cốc, bát, người cùng phục vụ một scene; kiểm blocking/occlusion/path ở mức brief. Không từ khoảng trống kết luận reach thực đạt.
4. **CTX-4 Dependency/change impact:** thay plate/layout làm các ref/shot/join nào hết hiệu lực; sửa component không bỏ kiểm tích hợp và regression.
5. **CTX-5 Evidence/authority:** source không bằng reuse rights; still không bằng action pass; request không bằng output approval; settings/cost/count cần current operator readback.

Outputs: context manifest actualread, prop→beat table, fixed/open/assumed ledger, missing inputs, findings severity+route+closure, downstream invalidation, disposition READY_FOR_REQUEST_REVIEW/REWORK/INPUT_BLOCKED (không GENERATE_READY). Critical/major contradiction HOLD; không average score bù blocker. Mỗi run chỉ đọc allowlist và viết report được giao; không browser/upload/generate/Git.

Independence: đây là informed preflight, được đọc request+intent nên không gọi cold audience review. CONT/PERF vẫn cold actual media trước rồi nhận context ledger để so, không maker rationale. Same model bias vẫn có.

## Đề xuất runtime nếu được duyệt

Root cập nhật SoT + context envelope → CTD hoặc CTX preflight → maker ART/CHAR/SHOT/PROMPT → specialist request review → owner gate theo scope → operator → Food/CONT/PERF actual review → root closure + owner asset gate.

Fixture trước khi thêm mandatory new-agent runtime: stale approvedversion; missing glass beat; leafcorrect but blocking platepull; sourcephotoreuse missing; foodcomponentpass but compositewrong; watermarkexceptionmisclassified. Chưa chạy fixtures, chưa sửa contracts02/03 hoặc cài skill/daemon.

## Điều owner cần chốt

Đề xuất A: tăng trách nhiệm/preflight cho CTD+root hiện có, không thêm role. B: tách AG-CTX-01 để review preflight độc lập, thêm chi phí context/run nhưng rõ trách nhiệm. Khuyến nghị A cho sửa hiện tại; B nếu owner muốn tách gate trách nhiệm lâu dài. Chất lượng phải kiểm qua findings bị chặn trước run và regression thực tế, không đo bằng số agent.
