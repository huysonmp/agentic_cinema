# EP01 — Local media QC và hướng ghép Flow

2026-10-01 (Asia/Saigon).

## Quyết định owner

Owner: `cái kết nối gemini api chưa cần đâu, nếu veo có sẵn ghép thì dùng nó luôn đi, còn cài kia thì tôi chấp nhận`.

- APPROVED: FFmpeg/FFprobe và Python environment riêng chạy faster-whisper local.
- DEFERRED: Gemini API; không cài SDK/kết nối API, không gửi audio tới API.
- Ưu tiên ghép cảnh trong Flow nếu tính năng sẵn có và đáp ứng yêu cầu; Canva vẫn là phương án hoàn thiện/dự phòng theo35. Không tự đổi owner final approval.
- Không có phê duyệt voice mới hoặc Quality mới. V02 vẫn NOT_SUBMITTED theo88, listening gate chưa đóng.

## Bộ cài đã kiểm

- Python3.12.14 tại `.venv`, không sửa Python3.14 hệ thống hoặc PATH toàn máy.
- faster-whisper1.2.1, CTranslate2 4.8.2, PyAV16.1.0; `pip check` PASS. Full dependency pins: `scripts/requirements-voice-local.txt`.
- PyAV19.0.0 ban đầu gây `metadata_errors` TypeError khi đọc audio. Đã pin16.1.0 và chạy thử thành công; giữ kết quả lỗi vòng01, không ghi đè.
- FFmpeg/FFprobe9.0.2 essentials portable ở `.local-tools/ffmpeg/verified-9.0.2/ffmpeg-9.0.2-essentials_build/bin`.
- Nguồn: https://ffmpeg.org/download.html → Gyan → official publisher mirror https://github.com/GyanD/codexffmpeg/releases/tag/9.0.2 . Archive35430500bytes; SHA256 `4705843CCAAF54257C16AD90F3E952ECE33C17DF964ECF7BFDBB0F49C7171077`, đối chiếu publisher checksum https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.7z.sha256 trước giải nén/chạy. Hai lượt ZIP nguồn chậm đã dừng, không dùng partial downloads.
- Model multilingual `small` đã tải về cache `.local-tools/whisper-models`. Inference CPU/int8, không GPU/CUDA; không gửi audio ra ngoài. Tải package/model có network; các lượt sau có thể dùng `--offline`.
- Script `scripts/local_voice_qc.py`: lưu SHA256 đầu vào, ffprobe JSON, WAV16kmono, volume/silence log, unprompted ASR JSON/text và timestamps. Không truyền kịch bản làm initial prompt; không ghi đè output đã tồn tại.
- Binaries, environment, cache và generated media/logs gitignored. Script/pins/biên bản được version control.

## V01 kiểm từ file thật

Input owner `C:/Users/PC/Downloads/du_an_nem_bui/V01_Khoai_Lite_v0.1.mp4`; SHA256 khớp88: `A291BF77C9B913DE43A006F4737DFCB5D27DA2E9811CA6812BDC045C6E81BF76`.

Native metadata: duration8.000s, H264720×1280/24fps; AAC-LC48kHz/stereo. Extraction thành công. Volume diagnostic mean−19.9dB, sample peak−0.1dB; peak sát0 không đủ để kết luận clipping hoặc chất lượng cảm nhận. Không tự normalize/ghi đè bản gốc.

ASR vòng02 nhận:

> Khoan! Mùi này làm anh nhớ cái chảo, bếp nhà anh, hội bé, mẹ răng gạo, anh đứng chờ.

So exact prompt85: phần lớn nội dung có dấu vết trong transcript, nhưng `hồi bé` → `hội bé` (khoảng3.76–4.16s), `rang` → `răng` (khoảng5.20–5.42s). Đây là ASR mismatch, chưa thể quy thành lỗi phát âm VEO; owner nghe lại hai vị trí. Mốc thời gian là ước lượng ASR. Không khẳng định đúng speaker, tự nhiên, sắc thái hoặc lip-sync từ transcript. `ASR_EVIDENCE_AVAILABLE / LISTENING_PENDING`.

Raw local evidence: `artifacts/voice-qc/v01-lite-local-02/`; vòng03 sau sửa serialization chạy `--offline` exit0, transcript khớp vòng02. Owner copies vòng03 trong `C:/Users/PC/Downloads/du_an_nem_bui/V01_local_QC/`. Cả hai lượt chạy cùng file đã có, không generation mới. Gate chống overwrite đã kiểm: rerun output03 phải exit nonzero với thông báo dùng folder mới.

### Lệnh tái sử dụng tại repository root (PowerShell)

```powershell
./.venv/Scripts/python.exe -m pip install -r scripts/requirements-voice-local.txt
./.venv/Scripts/python.exe scripts/local_voice_qc.py 'C:/Users/PC/Downloads/du_an_nem_bui/V01_Khoai_Lite_v0.1.mp4' --ffmpeg-bin 'D:/Workspace/agentic_cinema/.local-tools/ffmpeg/verified-9.0.2/ffmpeg-9.0.2-essentials_build/bin' --out 'artifacts/voice-qc/v01-lite-local-next' --model-cache '.local-tools/whisper-models' --offline
```

Chọn output folder chưa tồn tại kết quả. Bỏ `--offline` chỉ khi cần tải model public lần đầu, không upload audio.

## Ghép cảnh trong Flow

Official help https://support.google.com/labs/answer/16935718?hl=en xác nhận Scenebuilder: xếp/reorder/cắt đầu-cuối/preview/download scene. Live project9276788e-9781-44fb-ba5b-083006667374 có mục `Cảnh`; hiện trống. Context menu V01 có `Thêm vào cảnh`.

Chưa tạo scene, chưa thao tác trim/export hoặc chứng minh độ liền audio sau xuất. V01 là probe voice, không tự coi là clip production đã duyệt. Ưu tiên Add to Scene cho các clip đạt gate; không dùng Extend/AI-edit thay concatenation, không sinh footage hoặc credit mới trong vòng này. Khả năng xuất9:16/codec/timing/audio liên cảnh phải kiểm trên bản ráp thực. Không đóng master QC bằng việc có nút ghép.

## Bước tiếp

1. Owner nghe V01, nhất là hai vị trí ASR lệch; duyệt/ghi lỗi về voice và speaking turn.
2. V02 chỉ chạy khi listening gate88 đủ; budget riêng còn10credit, không retry/Quality.
3. Khi có các scene production đạt gate, ráp thử trong Flow, tải bản ráp rồi kiểm local trước final owner review. Canva xử lý phần cần thiết nếu Flow không đủ.
