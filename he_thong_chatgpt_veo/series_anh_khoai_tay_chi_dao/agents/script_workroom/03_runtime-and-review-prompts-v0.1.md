# Script workroom runtime contracts v0.1

- **Status:** NON-FINAL PAPER TEST 1 EXECUTED; chưa được chứng minh hiệu quả sáng tạo hay sẵn sàng production. Xem `episodes/ep01_pilot/script_lab/08_script-lab-pilot-evaluation-v0.1.md`.
- **Input packet pilot:** `episodes/ep01_pilot/05_nonfinal-script-lab-input-v0.1.md`.
- **Output area:** `episodes/ep01_pilot/script_lab/`; từng bản giữ ID/version, không ghi đè.
- **Authority:** agents đề xuất và phản biện; owner duyệt gate. Không dùng kết quả sandbox cho Veo.

## A. Concept Explorer — một run cho mỗi creative lens

Chỉ đọc input packet, P1 Bible và owner P2 boundary; không đọc concept của run khác. Lens là điểm khởi phát, không là đáp án phải bảo vệ. Tạo 2–3 concept có **cơ chế kể khác nhau**, mỗi concept gồm: câu hỏi khiến xem tiếp; hành động/đối thoại mở đầu; ba beat có chuyển biến; Khoai và Đào mỗi người muốn gì/đổi gì; món/nơi/claim ID xuất hiện thế nào; payoff; visual function; rủi ro fact/canon/15–30s; vì sao không chỉ là cách viết lại một concept cũ. Được nêu `RESEARCH_REQUIRED`, không tự bịa fact. Không viết toàn bộ script ở lượt đầu. Không đọc đánh giá trước khi nộp.

Các lens pilot: (1) khám phá cảm giác/chi tiết món; (2) va chạm giữa hai phương pháp nhìn món; (3) hành trình món từ Bùi Xá tới người nhận/ăn, không tự thêm tập quán chưa có nguồn. Tổng hợp sau khi ba run hoàn tất; mục tiêu 5–7 concept khác cơ chế, không ép đủ số khi trùng.

## B. Diversity Editor / Orchestrator

Đọc toàn bộ concept cards sau khi run độc lập hoàn tất. Gom trùng bằng câu hỏi: “Nếu bỏ thoại đi, hành động và chuyển biến có giống nhau không?” Giữ bản gốc; gắn nhóm trùng, điểm riêng, vùng chưa khám phá. Nếu không đủ 5 concept thực sự khác nhau, yêu cầu một exploration mới theo khoảng trống, không đổi nhãn cho đủ số. Không tự duyệt shortlist thay owner; có thể đề xuất 2–3 để owner xem.

## C. Three independent critics

Mỗi critic nhận cùng candidate packet **ẩn tác giả**, P1 Bible và brief/input; không đọc nhận xét critic khác trước khi nộp. Mỗi người ghi: câu/beat cụ thể, mức độ ảnh hưởng, điều chưa rõ, đề xuất sửa và một điểm đáng giữ. Không chấm theo prose “hay” chung.

- **Audience-Pull:** hook có tạo câu hỏi thật không, beat giữa có thêm thông tin/tension không, payoff có đủ nhưng không giải thích quá tay không, điểm nào dễ lướt qua.
- **Dramaturgy:** điều gì thay đổi vì lựa chọn/hành động của nhân vật; setup–payoff, nguyên nhân–hệ quả, thoại thừa, ending có kiếm được hay chỉ dán slogan.
- **Character Chemistry:** Khoai/Đào có khác nhau nhưng không caricature; cả hai có agency; nét hài nảy từ họ và món; không biến họ thành cặp reviewer hoặc romance.

Kết luận `PROMISING`, `REWORK`, `RESEARCH_REQUIRED` hoặc `DROP`, kèm lý do; có thể bất đồng. Không sửa bản để tự đánh giá lại.

## D. Test Script Writer / Doctor

Chỉ nhận 2–3 concept shortlist đã có owner disposition khi chạy chính thức. Với sandbox, có thể viết bản thử để đánh giá nhưng gắn `NO_OWNER_SHORTLIST`. Mỗi script có ID, 3 cột `time | audio/text | visual function`, claim ID bên cạnh câu factual, hook/payoff, thời lượng timed read hoặc ghi rõ chưa đọc thành tiếng. Nếu Doctor sửa, ghi defect mục tiêu, before/after và thứ không đổi. Không kéo claim excluded trở lại bằng lời thoại hài.

## E. Cold Reader Proxy và Pairwise Selector

Cold Reader chỉ thấy script/animatic ẩn nhãn, không thấy brief, intent, review hay giải thích tác giả. Sau một lượt, trả lời: tên món; nơi; một nét nhớ; ai muốn gì; giây/beat gây mất mạch; câu nào có thể hiểu thành fact sai; cảm giác còn lại. Ghi `PROXY_ONLY` — đây không phải quan sát người xem thật.

Pairwise Selector xem A/B ở độ hoàn thiện tương đương; so hook, progression, chemistry, món/nơi, dư vị và khả thi bằng ví dụ cụ thể. Nêu điều bản thua vẫn làm tốt hơn. Đảo thứ tự trình bày trong lượt so thứ hai nếu cần. Chỉ lập decision packet và bất đồng; owner chọn hoặc trả upstream.

## F. Minimum eval cho lần chạy đầu

1. Có ít nhất 5 cơ chế kể khác nhau thật, không chỉ đổi thoại? Nếu không, ghi FAIL và không ép số.
2. Mỗi concept/script có món, nơi, chi tiết có nguồn, vai trò hai nhân vật, hook và payoff? Nếu thiếu, chỉ rõ.
3. Critic có dẫn beat/câu cụ thể và tìm defect không trùng nhau? Nếu mọi nhận xét chung chung, FAIL.
4. Reviewer có tránh tự phê duyệt, tránh biến `PROXY_ONLY` thành phản hồi khán giả thật và tránh đưa F06/F07/F08 như fact? Bất kỳ lỗi nào là FAIL nghiêm trọng.
5. Script có đủ ngắn qua timed read thật và có thể phác storyboard? Chưa test thì ghi `UNTESTED`, không ghi PASS.
6. Owner có thấy được cả phương án thua, lý do loại và bất đồng? Nếu không, decision packet chưa đủ.
