# 257 — Một lượt BR và bản nối mở đầu có điều kiện

## Quyết định và thực chi

Owner “ok đấy” chấp nhận đúng bản nối A→BM REC256, hash `4cb1b2d7c94081ec1c301eec57f9fdfcb7d08bceb40ada089f081991ed030510`, và cấp một BR 720p/dọc/x1 tối đa 15 credit, không tạo lại hoặc mở dự phòng. Owner nói tiếp “tiếp tục đi nào” trong quá trình kiểm: tiếp tục cùng phạm vi, không tự coi là chấp nhận lỗi mới hoặc quyền sinh lại. Quyết định: `restart_720p_v1/00_decisions/C01A-BM-join-and-one-BR-approval-257.json`.

Root kiểm và đọc đầy đủ báo cáo đầu vào độc lập trước đúng một lần gửi: Frames START A80/END C02F0, hai ảnh đúng thứ tự/UUID đã đối soát hồ sơ 246, prompt sản xuất đọc lại khớp (khác LF cuối file), không gửi ghi chú vận hành; Omni 1.1 Flash/720p/9:16/4 giây/x1, Tác nhân tắt, không giọng tùy chỉnh; giá 7≤15. Tùy chọn trong Cài đặt lưới ô “Trả về video không có âm thanh” bật trước gửi. Không dùng tùy chọn này làm chứng nhận file không tiếng.

Đã gửi một lượt, tải 720p kích thước gốc, không nâng độ phân giải. Flow output `3dc4676a-643a-4804-bc06-cbb9682c2a92`; native `05_native/EP01_720_C01B_BR_T01_NATIVE.mp4`, SHA256 `736655e4e3bdf662bb11e73eb6f83ca06f91b20ee28859f5709a3deeb069dd2d`. Số dư cùng tài khoản 972→965, thực chi 7. Dự án 115/500, còn 385; đợt 41/49, dự phòng 110 vẫn đóng. 8 credit chưa dùng trong trần đợt không là quyền thêm đầu ra. Không tạo lại.

## Kết quả thực, không nâng paper PASS thành media PASS

Native H.264, 720×1280, 24 fps, 96 khung/4 giây, giải mã đủ. Root và reviewer độc lập xem đủ 96 khung qua 12 bảng ảnh cùng ảnh toàn khung chọn thêm. Có hành vi nhìn sang Khoai→buông tay ngoài→thu cả hai tay→nhìn về món; đĩa đứng yên, không lấy/gắp/ăn/uống, nem không hơi. Hai mặt và đạo cụ giữ trong khung, không có chữ tự sinh. Đây là bằng chứng ảnh liên tiếp, chưa xem/nghe AV liên tục.

**Lỗi đường đi tay:** tay trong từ cong gần bát ở F0 tiến tới mép trái/sau đĩa F3–8, giữ tư thế sát mép tới khoảng F44; trái yêu cầu tay trong thu vào/không vươn lại/không giữ hai mép đĩa. Hai tay sát hai mép nhìn như giữ đĩa; không khẳng định lực nắm từ ảnh 2D. Reviewer giữ **HOLD_FULL_NATIVE_AS_SILENT_SPEC_PASS**. Root đọc đầy đủ `06_qc/C01B_BR_T01_native_independent_257.md`, không tự bỏ lỗi vì đĩa chưa kéo.

**Âm thanh:** file gốc vẫn có AAC 48 kHz/stereo, PCM 192480 sampleframes, max_abs 1432/nonzero 380859. Chưa nghe thực, không khẳng định nội dung tiếng. Tùy chọn bật không phải bằng chứng native im tiếng, cũng chưa đủ kết luận lỗi sản phẩm hoặc ý nghĩa chính xác của tùy chọn. Đã tạo bản dẫn xuất riêng `07_edits/C01B_BR_T01_SILENT_DERIVED_NOT_SELECTED.mp4` bằng video-copy/-an; xác nhận không có track audio và 96 khung giải mã bằng tuyệt đối native. Giữ bản gốc. Sau tải đã khôi phục tùy chọn tắt như trước request để không ảnh hưởng lượt thoại sau. Không tạo giọng mới, không tốn credit.

## Bản nối chỉ để trình ngoại lệ và xem nhịp

BR candidate `[28,78)` zero-based = F28..77, từ 1,166667..3,25 giây, 50 khung/2,083333 giây. Bỏ 1,166667 giây chờ/chớp mắt đầu và 0,75 giây đuôi; giữ nhìn lên F30+, buông F44+, thu tới F64+, nhìn lại món F71+. **Cắt bỏ chuyển động tiến ra không sửa tư thế hai tay sát đĩa vẫn còn ở đầu candidate.** BM giấu Đào không chứng minh tay cô đúng ngoài khung. Candidate chưa được chọn, cần owner quyết định ngoại lệ; không đóng băng/cắt khung/che bằng món để giả đóng lỗi.

Đã dựng `07_edits/C01A_BM_BR_C02_13p75S_CONDITIONAL_QC_NOT_FINAL.mp4`, hash `dd8a24d271b28796a1df28b35e5d7ac4f3e5902614cc53ca9d7886c0e3eaf12c`, 330 khung/13,75 giây/720×1280/24 fps. Thứ tự A 81→BM 18→BR 50→C02 181 khung. Cắt ở F81/3,375 giây, F99/4,125 giây và F149/6,208333 giây. Không phải phim 30 giây hoặc final.

Giữ nguồn A→BM và C02 owner đã chấp nhận. Không đổi lời, giọng, tốc độ, âm lượng hoặc tạo crossfade; BR chèn 100000 stereo silence sampleframes ở 198000..298000 của audio 48 kHz. C02 đặt từ 298000/6,208333 giây, pad nguồn đến hết thời lượng hình. Mã hóa lại H.264/AAC, không bit-exact. Correlation PCM zero-lag với nguồn A→BM là 0,999992, C02 là 0,999824; vùng giữa BR (chừa 2048 sampleframes mỗi mép) bằng 0. Đây là kiểm kỹ thuật/vị trí nguồn, không thay kiểm nghe, khẩu hình hoặc chất giọng của người.

Root kiểm 66 khung encoded F91..156, gồm đủ 50 khung BR và 8 khung hai phía điểm nối mới. BM→BR chuyển cận Khoai sang hai người, Khoai môi khép khi vào BR, Đào từ chớp mắt nhìn lên; lỗi tư thế đầu vẫn giữ. BR→C02 hai tay Đào đã nghỉ, hướng nhìn về món, giữ góc bàn, có thay đổi nhỏ mặt/đồ ăn/ánh sáng, không gọi match pixel. Root đã đọc đầy đủ `06_qc/C01A_BM_BR_C02_join_independent_257.md`: **GO_FOR_OWNER_CONDITIONAL_CHECK**, không có blocker hình lớn mới, có seam mắt/đầu nhẹ tại F149 cần playback. Reviewer đo PCM vùng BR: dư đầu max_abs1, 65 giá trị khác0 trong sampleframes198000..198202, nội vùng bằng0; không gọi toàn vùng bit-zero hoặc đã nghe. Owner còn cần xem/nghe nhịp và quyết định ngoại lệ; chưa chọn BR hoặc mở finishing.

## Hồ sơ và học hỏi

- Request/prompt/approval257: authority, hash, live gate, một submit, output/debit.
- `06_qc/C01B_BR_silence_and_join_technical_257.json`: kiểm derivative và vị trí audio, không AV PASS.
- `06_qc/run-registry-257.json`: trạng thái mới; registry256 giữ snapshot lịch sử.
- `09_lessons/REC257_BR_path_and_silence_output_gates.md`: endpoint không chứng minh path, toggle không chứng minh bytes/output, không dùng trim để đóng lỗi còn hiện.
- Local evidence `C:/Users/PC/Downloads/du_an_nem_bui/257_BR_PRODUCTION/`: quote/account/download screenshots, native96frames, join330frames, denseboards, EDL. Native copy nằm ở thư mục lưu trữ owner; screenshot account không đưa Git.

Skill [Computer Use](C:/Users/PC/.codex/plugins/cache/openai-bundled/computer-use/26.1002.52244/skills/computer-use/SKILL.md) áp dụng đối soát UI trước gửi, một click có bằng chứng, tải gốc và lưu ảnh chứng minh thao tác; không dùng UI setting thay kiểm output.

## Tổng hợp vòng

- Đã xác định: một BR đã sinh/tải/kiểm; có đoạn buông–thu tay hữu ích, không kéo đĩa, nhưng inner hand sai path đầu.
- Đã chốt: A→BM chính xác owner chấp nhận, một requestBR thực chi7; original được giữ và derivative bỏ tiếng không đổi hình.
- Giả định: candidate cắt gọn có thể dùng **nếu** owner chấp nhận tư thế đầu hai tay sát đĩa và nhịp AV bản nối. Không phải quyết định đã chốt.
- Còn mở: ngoại lệ inner hand, nghiệm thu AV/nhịp trên exact13,75s mới, BR selection, C03A trở đi và phim30s/final.
- Tiếp theo: trình bản nối có caveat, hỏi đúng một quyết định ngoại lệ. Nếu không chấp nhận, giữ HOLD và trình hướng sửa có scope/quote riêng; không tự retry/reserve hoặc sinh voice mới.
