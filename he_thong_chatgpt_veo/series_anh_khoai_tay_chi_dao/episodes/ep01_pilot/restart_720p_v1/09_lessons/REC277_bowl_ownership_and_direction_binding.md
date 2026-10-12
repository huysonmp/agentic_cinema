# REC277 — Chọn đúng vật thể trước khi chỉ hướng chuyển động

Ngày 13-10-2026. Source C07T01 SHA `d1ed08ffca20e8bbee1455f14ed672fb4e2f538374a3ba209d6cfe49a195bfc0`, prompt276 SHA `ff869d873dbad96e81d323d770fb6f656274df691bf0136c1ae2a5f399b5353f`, reference nativeC06F56 SHA `69fb0e62a3a6f138a0eae622603945b248ec8d2809c8cda513dcdfdc33d00863`.

## Quan sát và tầng lỗi

Input ảnh có đúng hai bát riêng, lời N07 và một D06. Output đúng request/prompt và native720p. Trong source F64/80, Đào chạm/nắm bát phía trái trước Khoai; sau đó dịch bát ấy vào giữa. Bát trước Đào phía phải vẫn đứng nguyên suốt source. Đây là lỗi **gắn hành động vào sai vật thể trong native**, trước trim/ghép. Không gọi là lỗi dựng hoặc đổi nhãn sở hữu để nhận source đạt. Không range nào thực hiện chuẩn bị bát Đào; cắt bỏ đuôi không sửa được.

Root đã xem đủ144 ảnh qua18 board, thêm fullF0/F64/F80/F95/F143. Các điểm giữ được (cốc nâng, A còn kẹp, mặt Đào có khẩu hình, món nguội) không bù lỗi sở hữu bát. Scope nghe/AV chưa thực hiện; ASR nhận N07 không thay chứng nhận D06 hoặc sync.

## Giả thuyết góp phần — chưa chứng minh nhân quả duy nhất

Hai bát cùng chất liệu/màu và đều rỗng; “her own bowl” gắn vai ngữ nghĩa nhưng chưa phân biệt đủ vị trí. Prompt nối cụm hand LEFT / outside LEFT wall / slide LEFT có thể làm model chọn vật thể bên trái màn hình thay vì thành trái của bát bên phải. T01 đồng thời reset A về phía Khoai rồi nâng/đưa lại, dù ref đã gần bát Đào; đó là regression đầu shot cần kiểm riêng. Chưa có bằng chứng model đọc từng cụm theo cơ chế nào hoặc chỉ sửa wording chắc chắn hết lỗi.

## Kiểm soát đầu vào đề nghị

1. Chốt **vật thể đích** bằng vị trí trong khung + quan hệ props: bát bên phải trước Đào, ngay bên phải tay trong đang nghỉ, bên trái đôi đũa nghỉ, phía dưới/trong cốc. Tách rõ bát trái trước Khoai phải đứng nguyên, không được chạm.
2. Tách **tiếp cận → dịch chuyển**: tay nghỉ ngay trái bát Đào nên bước tiếp cận ban đầu đi ngắn sang phải; chỉ sau nắm bát đúng mới dịch bát trái một đoạn ngắn. Không dùng một chữ “trái” cho cả vị trí đích, thành bát, tay và hướng dịch.
3. Kế thừa A ở gần tay trong Đào/cạnh trái bát cô. Không reset về phía Khoai hoặc nâng tới ngực/mặt trước khi đưa lại. Ảnh tĩnh không khóa vận tốc, nên vẫn cần kiểm seam chuyển động.
4. Gate actual phải theo dõi ID của **cả hai bát** qua mọi khung, không chỉ “có bát rỗng dịch tới đâu đó”. Kiểm tay đi đúng phía, tiếp xúc/nắm/kéo có lý, cốc giữ nâng, A còn kẹp và air gap.
5. Sửa có mục tiêu phải qua current-final maker/reviewer và live mới. Hai lượt liên tiếp cùng lỗi lớn phải dừng theo238; không chạy batch, không sửa bằng giấu mặt hoặc dùng bát Khoai làm bát Đào.

Draft T02 trong `04_requests/C07_T02_prompt_DRAFT_277.txt` chỉ là can thiệp đề nghị, không output đã sửa/paid GO. Không thay canon, camera, giọng, món hoặc nhiệm vụ nhận–thả.

## Kết quả can thiệp T02 — phải kiểm regression toàn cảnh

Final T02 SHA `ae636235971fb36f5a31234dcb294cb91ea5d12c9231c8b046b797b8ad756ef4`; native SHA `c793308e55ed02f5b61fb9dfd1f4f6edaa4b3302bdb520defb108cfa5b5140da`. Một lượt720p giá10, debit1033→1023. Root xem đủ144 khung qua18 board, thêm fullF0/F64/F143 và exactSTART. Đào đã thành phụ nữ người thật suốt nguồn, bát Khoai mất từ đầu, cốc đổi tay/phía và thấp hơn, A reset về phía Khoai. Một bát còn lại được kéo xa sang trái; không gọi là thành công sửa ownership vì nền hình và danh tính đã sai.

Kiểm truy xuất sau chạy: chip ảnh trong lịch sử đúng take vẫn hiện hai nhân vật Khoai–Đào nguyên bản, hai bát và bố cục ảnh predecessor. Screenshot `277_C07_T02/C07_T02_ACTUAL_IMAGE_INGREDIENT_PROOF.png`; đây là đối chiếu trực quan UI, không claim hash byte ảnh trên server. Output gắn đúng final prompt, cấu hình và take. Không thấy bằng chứng đã chọn ảnh phụ nữ người thật. Tầng lỗi quan sát là tái dựng source/reference adherence; chưa biết cơ chế nội bộ hoặc xác suất từ hai mẫu.

Đổi wording hành động không bảo đảm giữ character/set. Bài học: kiểm **danh tính, số lượng/vị trí/owner đạo cụ, tay cầm, entry pose** trước khi xét động tác mục tiêu; không tối ưu một lỗi rồi nhận regression khác là đạt. Single Ingredients reference được dùng như tham chiếu, không coi là khóa first frame/vận tốc. Lệnh dài/ràng buộc nhiều là giả thuyết góp phần, chưa kết luận nhân quả.

Entry reset lặp T01→T02 cùng với MAJOR mới: dừng theo238, không T03 tự động. Giữ nguồn lỗi và tất cả bằng chứng; không sửa bằng crop mặt, đổi canon hoặc đổi tên bát. Bước sau là kiểm/đề xuất cơ chế neo hình mạnh hơn hoặc thay ranh giới shot, trình owner trước lượt mới; chưa có route nào được chứng minh sẽ đạt.
