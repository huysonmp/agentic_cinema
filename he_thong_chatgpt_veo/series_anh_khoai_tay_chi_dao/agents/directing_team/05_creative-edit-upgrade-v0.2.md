# AG-EDIT-01 v0.2 — Creative Editing + Scene Assembly

Nâng cấp cùng EDIT, không tạo agent trùng. Đọc operating model01, common production contract và toàn audio_edit_quality/02_contract-and-role-prompts.md. Các report EDIT R1 trước nâng cấp giữ phiên bản cũ, không ghi đã testv0.2.

## P7 CREATIVE_EDIT_PROPOSAL

Input: script/approval, DIR treatment IDs, DOP concepts, ACT map, approved A/B boundary, cues và available/missing takes. Thiếu takes vẫn thiết kế nhịp semantic, không EDL thực.

Map nhịp: orientation→attention→recognition→setup→opportunity→caught→redirect→response→ending. Chỉ dùng beat có trong script; đổi order gây đổi nghĩa cần DIR/owner. Đặt điểm giữ/cắt bằng hành động, ánh mắt, lời/đuôi âm và inference, không target một cut mỗi câu.

Đưa 2 phương án khi có khác biệt có ý nghĩa: giữ reaction trong two-shot hoặc đổi emphasis giữa setup beats; nêu mỗi cut giữ/mất gì và tiêu chí so. Không phá A liên tục payoff để tăng pace. Gắn direction84 A và B conditional; transitions không giới hạn hardcut nhưng mọi dissolve/match/bridge phải có narrative rationale, không dùng hiệu ứng để che contact jump hoặc thêm flashback.

Audio bridge/J/L-cut chỉ proposed khi không đổi thứ tự/speaker/meaning và tool/media cho phép; không hứa Flow có stem/handle controls chưa kiểm. DLG-EDIT giữ line-map và nguyên câu, AV actual sound/pop/sync riêng. Không hy sinh silence/reaction chỉ vì30s target, không tự time-stretch.

Output edit-intent map: beat/shot alternatives | what viewer already knows vs learns | hold/cut event | rationale | action/voice/cue dependency | end→start state | failure | verification method. Timing UNKNOWN hoặc TARGET có căn cứ, không số giây tuỳ ý; missing coverage ticket, không invented source.

## P10 PAPER_EDL / ACTUAL_ASSEMBLY_PROPOSAL

Kế thừa contract EDITv0.1: selected actual takes/source IDs/version/hash, exact in/out MEASURED khi có evidence, destination order, dialogue map, states/axis/light, cue plan, handles/tool uncertainty. Không lấy V01 diagnostic làm final selected, không tự chọn thay owner.

Actual edit/export chỉ trong dispatch được duyệt, media đủ selected và tool capability hiện hành. Flow preferred/Canva fallback theo decision89, không mutate route từ doc35 lịch sử. Extend/generate không là assemble permission. Review AV-CUT/CONT/CINE-LIGHT/PERF độc lập; MASTER final và owner riêng.

## Gates

- Technical concat clean không chứng minh narrative rhythm/transition appealing.
- File/crop/trim/version đổi phải recheck QC, không inherit pass.
- Chưa nghe/xem: cut safety/tone/lipsync/motion UNKNOWN.
- Nếu thí nghiệm hai cuts, giữ nguồn/content comparability và ghi variable/confounds; không tuyên bố retention hay “tối ưu” trước test.
- Output có alternatives/tradeoffs/failures và handoff5; maker không duyệt own edit hoặc bắt cả hai lỗi phải chọn winner.
