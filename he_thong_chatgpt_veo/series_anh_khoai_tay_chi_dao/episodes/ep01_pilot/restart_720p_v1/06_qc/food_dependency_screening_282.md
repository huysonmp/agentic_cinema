# REC282 — Rà mẫu món trong các đoạn đã chọn

Ngày 13-10-2026. Phạm vi **SAMPLED_STILLS / FOOD DEPENDENCY SCREENING**, không xem toàn bộ 689 khung, không AV/listening hoặc nghiệm thu lại phim. Không tự bác tiếng/diễn đã được owner duyệt và không sinh lại nguồn.

## Nguồn và mẫu trực tiếp xem

Mở đầu 330 khung đã được owner chọn tại REC258, hash hiện kiểm lại `dd8a24d271b28796a1df28b35e5d7ac4f3e5902614cc53ca9d7886c0e3eaf12c`. Dùng đúng PNG trích từ target này trong `C:/Users/PC/Downloads/du_an_nem_bui/257_BR_PRODUCTION/join_qc/all_native_frames/`, không dùng overview của toàn native khác rồi gọi phần đã chọn.

| Đoạn | Khung trực tiếp xem | Quan sát món / phụ thuộc |
| --- | --- | --- |
| C01A | Opening F40, file `00041.png` | Đĩa rõ ở dưới hai mặt; nhiều miếng phẳng/dày, thịt đặc màu hồng nâu. Nếu đổi món cuối mà giữ nguồn này, hình thái đĩa không đồng nhất. |
| BM “Khoan” | Opening F89, file `00090.png`, offset 8 trong BM | Khung gần Khoai, đĩa chỉ hiện một phần ở mép dưới nhưng vẫn có phiến lớn đọc rõ. Ít vùng món hơn khung chung; chưa đánh giá mức chấp nhận trên chuyển động. |
| BR thu tay | Opening F124, file `00125.png`, tương ứng native BR F53 | Khung chung và đĩa rõ; món cùng hình thái phẳng như C01A. |
| C02 ký ức | Opening F239, file `00240.png`, offset 90 của C02 | Đĩa rõ trong khung hai mặt; không chỉ là hậu cảnh mờ có thể mặc định bỏ qua. |
| C03A | Native F21, `258_C03A/native_qc/all_native_frames/00022.png`, thuộc range [0,42) | Đĩa rõ dưới thoại; cùng phiến phẳng/đặc. |
| C03B | Native F25, `259_C03B/native_qc/all_native_frames/00026.png`, thuộc range [0,50) | Đĩa rõ và cùng cấu trúc lệch. |
| C04 T02 | Native F72, `262_C04/native_qc/all_native_frames/00073.png`, thuộc range [0,144) | Đĩa là nguồn của hành động gắp; sửa đĩa và phần được gắp phải cùng nhau, không chỉ đổi màu. |
| C05 T02 | Native F32, `265_C05/C05_T02_QC_267/all_native_frames/00033.png`, thuộc range [0,66) | A trên đũa là lát đặc hình chữ nhật; liên quan trực tiếp điểm nhận mới. |
| C06 T03 prefix57 | Prefix F28, `275_C06_T03/prefix57_qc/all_native_frames/00029.png`, thuộc range [0,57) | A vẫn là lát đặc; prefix vẫn giữ approval tiếng/diễn trước, nhưng food continuity với ảnh mới chưa đạt. |

File PNG được đánh số F+1. Không ngoại suy rằng mọi khung trong các range đều có cùng mức rõ; chín mẫu đủ chỉ ra vấn đề có trên nhiều đoạn và không riêng T03. Không sử dụng mẫu này để quyết định cắt frame hoặc thay render toàn tập.

## Hash nguồn đối soát hiện hành

- C03A native: `051202d30ea7317b38ee74de8a690db48510940f3311543e208f2807b56b3b0c`.
- C03B native: `f85df55c24a267851258bc64a8d0e5579e954175a34039ed563903a89ed343a1`.
- C04 T02 native: `8ad98f21c0c904b01055d6f579900cd60c107a152a9166a8cfa563165a47a209`.
- C05 T02 native: `3df61217ddf6d09792fe1e5991c3668d115ce5648c00802f196d87abe57d23df`.
- C06 prefix57: `58f13ea424300e0cde09000d37cf42839ac7b8ba7c6d2d6f64c02eeb9022594d`.

Hash kiểm lại trực tiếp từ các file, khớp evidence đã trích. Chuẩn đối chiếu hình món là hai ảnh thật đã kiểm REC281, không recipe mới hoặc ảnh search khác.

## Phạm vi sửa chưa được chốt

Ưu tiên phụ thuộc là phần A ở C04→C05→C06→nhận món mới, rồi đĩa ở những khung chung. Tuy nhiên không kết luận cần sinh lại tất cả bằng cùng cách: cần xem khả năng sửa vật thể mà giữ mặt/tiếng/khẩu hình, giá và rủi ro trên route thực, rồi trình owner. Chưa có bằng chứng một ảnh sửa mới có thể truyền vào native cũ mà không mất quality.

Không che toàn món/giấu mặt hoặc bỏ nhịp để hợp thức hóa. Không dùng approval ảnh mới thay approval source cũ, không mua thêm/cài API, không chi credit. Sau owner chốt ngoại hình món, lập phương án xử lý các phần phụ thuộc trước khi hứa phim đã đủ điều kiện bàn giao.
