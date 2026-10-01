# AEQ local diagnostic evidence — 2026-10-01

MEASURED_MEDIA_EVIDENCE, không production edit hoặc voice approval. Root dựng bản sao local bằng FFmpeg9.0.2, không Flow/API/credit. Source V01 SHA256 `a291bf77c9b913de43a006f4737dfcb5d27da2e9811ca6812bdc045c6e81bf76`,2143707bytes; owner và project raw hash cùng giá trị. Script kiểm lại source không đổi sau render.

Script: `scripts/voice_assembly_diagnostic.py`. Source A[0,2.5s], B[2.5,8s]. Đây là split diagnostic theo target điểm ngừng, không hearing-approved safe cut, không production EDL. Reencode H264/AAC; không export bit-identical.

| Output | Executed mapping | Target | ffprobe actual duration | SHA256 |
|---|---|---|---|---|
| control | A→B |8s|8.000000s|088d4ac5005e03343016cd4388d08a58d3fcb832a08bcd29121e3b51184709e0|
| repeat | A→B→B |8s|13.500000s|2638598b2017c181768ea79222ebb812a8f5ec6eb59f87be3f9d59ce244176d9|

Native metadata và command/mapping thực ở `D:/Workspace/agentic_cinema/artifacts/voice-assembly/aeq-r1/manifest.json`; file `.mp4` cùng folder. Năm unit tests exact source-map control/repeat/reorder/change-version/change-trim PASS. Không chỉ so duration; reorder vẫn lỗi dù duration bằng. Các unit tests không bằng agent fixture pass.

ASR repeat actual chạy multilingualsmallCPUint8/offline/no initial prompt, exit0. Text:

> Khoan! Mùi này làm anh nhớ cái chảo. Bếp nhà anh, hội bé. Mẹ rang gạo, anh đứng chờ. Bếp nhà anh, hội bé. Mẹ rang gạo, anh đứng chờ.

Evidence `artifacts/voice-assembly/aeq-repeat-asr-r1/asr.json`, `media.json`, `transcript.txt`. Timestamp từng segment/word có trong JSON, chỉ estimated. Không viết lại transcript cho khớp expected. `rang` nhận đúng ở lần diagnostic này trong khi V01small vòng trước nhận `răng`: bằng chứng ASR có biến động, không tự chứng nhận phát âm đúng/sai. Reviewer không có hearing input, full playback/video-frame interpretation; chưa kiểm lip-sync/continuity subjective/ambience pops.

Initial bounded render guard fail do so digest lowercase với literal uppercase; đã sửa normalization, không nguồn changed. Bản sao diagnostic có output filename phân biệt, không thay V01.
