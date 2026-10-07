# REC221-SIA-R1 — N02 PA-V: nguồn tiếng, alignment và giới hạn nghiệm thu

Reviewer độc lập `REC221-SIA-R1`, theo dispatch owner217/220/221. Chỉ đọc local và viết report này; không đọc reviewer khác, browser, generation, credit, API, dependency mới hoặc sửa media. Trạng thái: **MEASURED_AUDIO_COMPARISON_COMPLETE / IDENTITY_AND_FULL_AV_HOLD**. Không chọn winner hoặc cấp quyền sử dụng output.

## Năng lực và đầu vào thực

Đã đọc main220, main221, script `scripts/inspect_ep01_n02_edit_trial.py`, `inspection/inspection.json` và ba `AUDIO_REVIEW.wav`. Đã rehash native nguồn và A/B/C; chạy FFprobe trực tiếp, FFmpeg giải mã PCM vào bộ nhớ, Python3.14/NumPy2.5.3 có sẵn để đo tương quan/alignment. SciPy không có trong Python đang dùng; không cài, dùng NumPy FFT. Không có actual hearing hoặc continuous/full AV trong phiên; observed text, speaker, preset, overlap, đổi giọng giữa câu, độ nghe tự nhiên và lip-sync đều **UNKNOWN**. Không chạy ASR để suy identity; không xem ảnh rồi nhận đã kiểm môi.

Nguồn `C:/Users/PC/Downloads/du_an_nem_bui/200_n02_replacement/N02_NATIVE.mp4` đã được owner201 chấp nhận về Khoai/K20 xuyên suốt và nhịp. Lần này rehash đúng `72cbaf7d9f66932002dfce1b1a57fa464935c315e84e54ae094fe29aa805a153`. Dùng nguồn ấy làm đối chứng **preservation** của audio đã được chấp nhận; không gọi nó là mẫu audition K20 độc lập. K20 custom audition149/151 chưa có exact local reference trong dispatch. Approval201/203 vẫn thuộc nguồn cũ, không tự chuyển thành duyệt output221 khác bytes.

Expected N02: Khoai/K20 nói toàn lượt “Khoan. Mùi này làm anh nhớ đến bếp nhà anh. Hồi bé, mẹ rang gạo, anh đứng chờ.” Giả thuyết thử PA-V giữ tiếng/thời gian nguồn trong khi sửa hình; actual observed bằng tai chưa xác định. Đào phải nghe im; mặt/miệng Khoai qua hết lời cần xem-nghe đúng từng output. Approval batch221 là quyền chạy phép thử, chưa là acceptance.

## File và provenance

Targets tại `C:/Users/PC/Downloads/du_an_nem_bui/221_n02_pa_v_trial/`:

| Native | SHA256 live | WAV inspection SHA256 |
|---|---|---|
| N02_A_NATIVE.mp4 | `35c1a0e527bf4171d8d92ed530f2058d5f7c0c005f372ff6d2f68dacbf524537` | `d0d98bb3227b27533df8c9e3fab210925ba1b29a9676886048470dbdb4d82ef6` |
| N02_B_NATIVE.mp4 | `660f175775db6b082458846edb5c8edc8beb771b90a3330f53cb37d07f31a535` | `bafac31224a35eb80d2121dc05f0e6f5ae4839e6623895a1d51adeff21decb1f` |
| N02_C_NATIVE.mp4 | `9bd637ed26b953d8ea87019c1fa93c1d09228551240f3b85be98815fbd2a494d` | `bf010b29a4afaf7b444cac5bbe2f49fdd773ff070cfb09ecd40e56de20c2c4e0` |

Mỗi WAV nằm trong `inspection/N02_{A,B,C}_NATIVE/AUDIO_REVIEW.wav`. Decode native trực tiếp bằng FFmpeg **bằng toàn PCM WAV tương ứng**, không dựa riêng kết luận root. Inspection JSON hash `eead00f829b6c356b428a6e756ef1fadeddd0c8fc5569ec023a0b99447a91ff6`.

Nguồn và ba output đều H264 360×640/24fps, 240 frame/10,000s video; AAC48kHz stereo/10,005s audio, 470 packet-frame AAC. WAV đều PCM16 stereo48kHz, 480.240 sample-frame. Thời lượng bằng nhau không chứng minh nội dung hoặc timestamp lời bằng nhau. Source PCM hash `7236b44500ce337c80372e530a4568550e872806907dd9802c5124c5316d3bc6`; PCM A/B/C lần lượt `c7296ea79f04024cc1f75058e1684d3cafda98702ee9dd96ac81ced40af288fb`, `ac1a765669cfd950d8fef043e1d2ceb2ec7be3a5c984e49a013e23a0838d7609`, `2f6f4b3bcffa65cc6dcd6aa68bf787a35b65b0059517bbc5ca48394d708d9240`.

## Phương pháp và số đo

So toàn 10,005s: PCM stereo16-bit giải mã cùng cấu hình, downmix số học hai kênh thành mono float64. Global FFT cross-correlation tìm lag tối đa covariance trong ±0,5s; sau đó Pearson trên overlap đã căn. Envelope là RMS từng khối10ms; tìm lag envelope ±1s. Gain là least-squares của output theo source đã trừ mean, **không phải bằng chứng model chỉ đổi gain**. Residual SNR chỉ lượng hóa phần khác waveform, không đo chất lượng nghe hoặc identity. Không đặt ngưỡng PASS chưa hiệu chuẩn.

| Output | Exact PCM | Global best lag | Aligned Pearson | RMS envelope Pearson | LS gain / residual SNR | Expected → observed |
|---|---|---|---|---|---|---|
| A | Khác | 0 sample | 0,965729 | 0,986216, lag0 | −1,455dB / 11,413dB | Giữ nguồn/thời gian → tương đồng waveform cao; không bit-exact; identity UNKNOWN |
| B | Khác | 0 sample | 0,706849 | 0,720185, lag0 | −4,476dB / −0,006dB | Giữ nguồn/thời gian → khác đáng kể phần cuối, cần local alignment; identity UNKNOWN |
| C | Khác | 0 sample | 0,970157 | 0,988722, lag0 | −1,283dB / 12,043dB | Giữ nguồn/thời gian → tương đồng waveform cao; không bit-exact; identity UNKNOWN |

A/C các cửa sổ2s ở0–10,005s có correlation lần lượt0,9466–0,9928 và0,9476–0,9926. Đây là bằng chứng mạnh về quan hệ waveform với nguồn đã duyệt, phù hợp khả năng tái mã hóa/xử lý âm thanh; **không chứng minh cơ chế nội bộ hoặc voice identity**. Không được gọi “giọng mới” vì hash khác, cũng không được gọi K20 PASS vì correlation cao. Âm nền/nhạc có thể đóng góp vào metric toàn nguồn; chưa có speech-only segmentation bằng nghe.

### B: global lag không giải thích được mọi khoảng

Đo cửa sổ0,25s, match normalized Pearson của source với vùng output ±0,5s. Quy ước lag âm: mẫu tương ứng xuất hiện sớm hơn trong B. Lag là ước lượng alignment trên cửa sổ, không phải speech boundary hoặc điểm cắt sample-accurate. Kết quả:

| Source interval | Pearson cùng thời điểm | Best local Pearson | Lag |
|---|---|---|---|
| 6,500–6,750s | 0,248305 | 0,955176 | −41,667ms |
| 6,750–7,000s | −0,041629 | 0,977244 | −41,667ms |
| 7,000–7,250s | −0,000211 | 0,941342 | −41,667ms |
| 8,000–8,250s | −0,011921 | 0,983710 | +376,396ms |
| 9,250–9,500s | −0,013301 | 0,991587 | −288,813ms |

Đây là các acoustic matches, chưa ánh xạ từ/người nói. Nhiều lag khác nhau không thể giải quyết bằng một offset toàn clip. Một số đoạn cuối khác có local correlation thấp; chưa đủ kết luận bị cắt, lặp, đảo lời hoặc thu mới. Cửa sổ ngắn/âm nền lặp có thể tạo match mơ hồ; các khoảng năng lượng thấp không dùng chốt lỗi phát âm. Tuy nhiên B **không giữ waveform ở thời điểm nguồn** như giả thuyết strict preservation. Cần nghe source và B toàn lượt, ưu tiên6,25–10,005s, rồi đối chiếu AV; không tự retime hoặc chồng audio cũ.

Peak A/B/C:25.712/27.756/27.773 đơn vịPCM16; không có sample fullscale. Số đo này không xác nhận không méo/clip khi nghe.

## Findings, status và closure

| ID / mức / trạng thái | Bằng chứng / uncertainty | Xử lý và điều kiện đóng |
|---|---|---|
| SIA221-01 / MAJOR / HOLD_FOR_INPUT — A/B/C | Chưa hearing/reference/AV thật. Expected Khoai/K20 và người nghe im; observed UNKNOWN. Không có confirmed voice defect. | Reviewer có capability hoặc owner nghe-xem từng native exact hash, ghi lời/voice xuyên lượt/overlap/miệng/listener/timecode. Formal identity cần reference/provenance chuẩn. |
| SIA221-02 / MAJOR / PRESERVATION_TIMING_DEFECT_MEASURED — B | Global lag0 che local shift−41,667ms và matches cuối ởlags khác. Đo chắc về sai khác waveform/time, chưa xác định speech impact/cause. | Giữ B chưa chọn; nghe đối chứng cuối và fullAV. Nếu chấp nhận như performance mới phải duyệt lại exact artifact; không dùng approval201 thay. |
| SIA221-03 / MINOR / MEASURED_DIFFERENCE_REVIEW_REQUIRED — A/C | Không bit-exact nhưng correlation cao/global lag0. Sai khác chưa được nghiệm thu nghe; severity có thể đổi sau actual review. | Nghe toàn nguồn đối chứng và native A/C, kiểm nhịp/âm cuối/âm nền; closing evidence bind target. Không tạo winner chỉ bằng metric. |

```json
{"run_id":"REC221-SIA-R1","mode":"MEASURED_AUDIO_COMPARISON","actual_audio_reviewed":false,"references_compared":false,"actual_full_av_reviewed":false,"observed_speaker":"UNKNOWN","voice_identity":"HOLD_FOR_INPUT","lip_sync":"HOLD_FOR_INPUT","release_authorized":false}
```

## Tổng hợp vòng

- Đã xác định: hash/probe/PCM extraction đúng; cả ba khác PCM; A/C tương đồng cao, B có biến đổi alignment cục bộ.
- Đã chốt giữ: nguồn201/203 vẫn được duyệt trong scope cũ; batch221 không tự thành acceptance output hoặc full-film PASS.
- Giả định sử dụng: mono/envelope làm diagnostic preservation, không classifier giọng; không gán match thành lời đã nghe.
- Còn mở: voice/text/nhịp nhận thức, tail B, người nghe/khẩu hình và fullAV của từng output; local K20 audition chưa có.
- Tiếp: trình exact source và A/B/C tại checkpointG2 với checklist nghe-xem trên; ưu tiên B6,25–10,005s. Chưa overlay tiếng, retime, generation/retry hoặc finishing.
