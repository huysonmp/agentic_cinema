# SIA-01 R1 — Capability và kiểm chốt chặn người nói

Ngày: 2026-10-05. Run: SIA-01-CAPABILITY-GATE-R1. Reviewer: `/root/speaker_gate_critic`; maker triển khai: `/root`. Scope: `AUDIO_SELECTION`, script `C-v0.6`, request184. Kết luận thực tế: **HOLD_FOR_INPUT — chưa xác minh người nói/giọng của nguồn A03 và R01**. Kiểm logic gate đã hoàn thành; acoustic review chưa thực hiện.

## Quyền, đầu vào và capability

Dispatch chỉ cho đọc contract, code và evidence liên quan; chạy kiểm local không network; ghi duy nhất report này. Không sửa media/code/evidence gốc, không browser/API/credit/install, không nhận dạng từ ASR hoặc ảnh, không tự approve. Report độc lập này không là listening record đạt chuẩn để mở gate.

Đã đọc đầy đủ contract02 trong lượt review trước và contract10 bản mới trong lượt này. Đã đọc code gate/tests/builder và diff tương thích audit183; evidence179/package, script178, manifest182, audit183; request184 và current-source-gate184. Gate đọc bytes/hash và metadata audio của đúng nguồn local qua `wave`/`ffprobe`. Đọc file/hash/probe không có nghĩa nghe được âm thanh.

| Năng lực | Thực hiện trong run | Giới hạn |
| --- | --- | --- |
| Đọc script, vai dự kiến, source map và report | Có | Chỉ xác định expected; không chứng minh observed |
| Xác minh file/hash và source range bằng code | Có | Provenance/metadata; không nhận dạng giọng |
| Nghe toàn A03/R01 và từng lượt | Chưa | Không có actual listening trong run |
| So giọng với local reference K20/D06 đã duyệt | Chưa | Không được cấp file reference và approval artifact local; audit183 cũng ghi chưa có local reference xác minh |
| Xem-nghe liên tục current AV cut/diễn môi | Chưa | Request184 có `target=null`, scope AUDIO_SELECTION |
| ASR/diarization/nhận dạng acoustic | Không chạy | Không suy speaker từ text, nhãn, cao độ hoặc metadata |
| Code fixture và mapping regression | Có | Chỉ xác minh hành vi validator; không chứng minh khả năng phát hiện giọng thật |

`actual_audio_reviewed=false`, `references_compared=false`, `actual_full_av_reviewed=false`. Không điền observed bằng expected, không tạo confidence.

## Phiên bản và bằng chứng kỹ thuật

Request fingerprint hiện hành: `98643c66c2364aba44c4f8f745cd656d97d4f937dac0f2630c5925477c61b49f`. Tính lại bằng `fingerprint(request)` khớp envelope184.

| Artifact | SHA-256 tại review |
| --- | --- |
| script178 C-v0.6 | `ece42d39462cc9496fbc3ad6aa45a597bfcce8f8e1998cde66484cb362ee2626` |
| dialogue-package179 | `42a65734684c432978a7a37c32ada2721f5217a962a09a32e69d6aa0fd1ecd9b` |
| A03_VOICE_REVIEW.wav | `9b560b03a98e3d0cd722a0a2877d5395c08110ad2f361230f534d8a8736b3ae0` |
| R01.mp4 | `9530c8c8315a7e3653c43cc400e7ab8891f536256e4d7dfaee5b16f326e59b19` |
| ep01_speaker_gate.py | `1319e134a3a302574478b09d48522675532d559e5e2aa74c9d8325db02da6521` |
| test_ep01_speaker_gate.py | `06edfef853887723714e9b5143bc9d905ffb398427450e61be66ddd8cef7fbc8` |
| build_ep01_c_v06_assembly.py | `c9aeb5f21f8fe25d060f71aec174379cbe74d61f940a71d5bd0fd163178bdcdc` |
| contract10 | `879a2e345146fc2249a091a653d88d7acf5dbae65d9074215fe0a553815df9d1` |

Commands thực chạy trong run này:

```text
python -B -m unittest discover -s scripts -p test_ep01_speaker_gate.py -v
python -B -m unittest discover -s scripts -p test_voice_assembly_diagnostic.py -v
evaluate(request184, None)
evaluate(request184, audit183)
```

Kết quả: **39/39 synthetic gate tests PASS, 5/5 mapping regression tests PASS**; không skip. Fixture nguồn/ref là WAV synthetic; AV fixture là video màu và audio silent tạo trong thư mục test tạm. Các trường quan sát trong fixture là dữ liệu mô phỏng. Đây không phải 39 lượt nghe giọng thực và không là acoustic benchmark.

`evaluate(request184, None)` cho kết quả bằng chính `current-source-gate.json` đã lưu: `HOLD_FOR_INPUT`, `defects=[]`, `identity_detection_performed_by_gate=false`, `release_authorized=false`. `evaluate(request184, audit183)` cũng HOLD, không xác nhận defect. Audit183 có `actual_identity_verified=false`, `heard_by_reviewer=false`, và cả bảy `observed_speaker=null`.

## Coverage từng lượt của nguồn thật

Các khoảng dưới lấy từ request184; đều là **ASR_HINT_NOT_SAMPLE_ACCURATE**, chỉ hướng dẫn tìm chỗ nghe. Không dùng chúng làm chứng cứ cắt sample-accurate. Phải nghe toàn source và các chuyển lượt, đặc biệt N02, để kiểm đổi giọng giữa câu và nói chồng.

| Lượt | Expected người/giọng | Source range giây | Observed / heard_text / voice ID | Identity / giữa lượt / overlap |
| --- | --- | --- | --- | --- |
| N01 | Đào / D06 | A03 0.00–2.00 | UNKNOWN / UNKNOWN / UNKNOWN | UNKNOWN / UNKNOWN / UNKNOWN |
| N02 | Khoai / K20 | A03 2.20–7.66 | UNKNOWN / UNKNOWN / UNKNOWN | UNKNOWN / UNKNOWN / UNKNOWN |
| N03 | Đào / D06 | A03 8.04–8.64 | UNKNOWN / UNKNOWN / UNKNOWN | UNKNOWN / UNKNOWN / UNKNOWN |
| N04 | Khoai / K20 | A03 9.02–9.78 | UNKNOWN / UNKNOWN / UNKNOWN | UNKNOWN / UNKNOWN / UNKNOWN |
| N05 | Đào / D06 | R01 0.00–1.90 | UNKNOWN / UNKNOWN / UNKNOWN | UNKNOWN / UNKNOWN / UNKNOWN |
| N06 | Khoai / K20 | R01 2.62–3.84 | UNKNOWN / UNKNOWN / UNKNOWN | UNKNOWN / UNKNOWN / UNKNOWN |
| N07 | Đào / D06 | R01 4.74–6.34 | UNKNOWN / UNKNOWN / UNKNOWN | UNKNOWN / UNKNOWN / UNKNOWN |

Expected reference ID của Khoai: `fb1188da-e6c8-4156-9bba-0576c01a8da6`; Đào: `0ce1551e-e74b-481c-bb9e-d31e04f8b352`. Đây là lựa chọn/preset dự kiến trong package, chưa phải kết quả so giọng trong run này. `visible_speaker`, listener silent và lip-sync đều UNKNOWN; không thuộc phép kiểm nguồn audio đã hoàn thành.

| Tiêu chí | Coverage | Evidence / giới hạn |
| --- | --- | --- |
| Script/package/roles/hash/source audio/range cấu trúc | MET | Gate đọc đúng artifacts, không có source hash/range hold |
| Fingerprint chống tái dùng report sai version/range/cut | MET | Fixture stale source/trim/script/ref/cut bị chặn |
| Reviewer độc lập, actual listening/reference, đủ từng lượt | MET cho gate logic; UNKNOWN cho nguồn thật | Thiếu evidence thật trả HOLD |
| Đổi giọng giữa lượt, nói chồng | MET cho fixture logic; UNKNOWN cho nguồn thật | FAIL_SWITCHED/FAIL_OVERLAP mô phỏng trả REWORK; thiếu kiểm giữa lượt trả HOLD |
| Script/ASR/anonymous diarization không thay identity | MET | Methods không hợp lệ bị chặn |
| Voice ID riêng với visible speaker/lip-sync | MET cho scope logic; UNKNOWN cho AV thật | Source PASS không đủ final; target cần video+audio và actual full AV review |
| Planning riêng với selected source/final delivery | MET | Builder yêu cầu `--speaker-review` hoặc explicit `--allow-unverified-planning`; release luôn false |
| Acoustic detection/real nghe so giọng | UNKNOWN | Chưa chạy, không gán PASS |

## Findings và điều kiện đóng

| ID | Asset/version và evidence cụ thể | Expected → observed | Method / uncertainty | Severity và action / owner / closure |
| --- | --- | --- | --- | --- |
| SIA-R1-01 | Request184 C-v0.6, N01–N07; audit183: `actual_identity_verified=false`, `heard_by_reviewer=false`; gate184: `Actual listening/reference comparison missing` | Trước actual source-selection phải đủ nghe/so reference → hiện chưa có | Đọc record + evaluate read-only; giọng thật UNKNOWN, không phải defect âm thanh đã xác nhận | CRITICAL blocker của source-selection. SIA/reviewer có năng lực nghe + owner cung cấp provenance reference. Đóng bằng reference audio/hash/approval đúng K20/D06 và review thật đủ bảy lượt gắn đúng fingerprint |
| SIA-R1-02 | Gate code hash nêu trên; 39 fixture tests và 5 regression; field `identity_detection_performed_by_gate=false` | Gate bảo đảm record/evidence được kiểm → chưa có nhận dạng acoustic tự động | Code/test, không nghe. Không còn implementation defect cần sửa trong phạm vi đã review; truthful attestation vẫn cần reviewer thật | MAJOR giới hạn readiness. Không quảng bá tests là acoustic QC. Đóng phần acoustic bằng run nghe/so reference có quan sát và evidence; không đóng bằng schema PASS đơn thuần |
| SIA-R1-03 | R01 reuse approval168 và A03 working selection trong manifest182; request184 AUDIO_SELECTION, target null | Approval tái dùng/tạm chọn và provenance phải đi cùng SIA → không thay được voice/AV verdict | Đọc manifest/contract; actual voice và lip-sync UNKNOWN | MAJOR handoff. Giữ HOLD nguồn; sau chọn nguồn mới kiểm AV_ASSEMBLY và FINAL_AV đúng target/hash với các gate khác, owner duyệt cuối |

Không có acoustic defect được xác nhận trong run này. Gate báo thiếu reference/method/observation khi chưa có report là thiếu đầu vào; không suy các preset thực tế sai hoặc câu nào đã lẫn giọng.

## Verdict và handoff

Paper/implementation review: `FIXTURE_RESPONSE_COMPLETE`. Source provenance/metadata: hoàn thành trong phạm vi gate; không là voice PASS. Actual listening/voice identity: `HOLD_FOR_INPUT` cho cả bảy lượt. Motion/lip-sync: UNKNOWN, chưa review. Production/final: chưa đủ điều kiện, `release_authorized=false`.

1. Đã xác định: guard và fixture logic hoạt động; source184 hiện đúng hash nhưng người nói thật vẫn unknown.
2. Quyết định đã chốt: không chuyển thiếu QC thành selected source đã đạt; chỉ bản tạm có nhãn được đi nhánh planning; tái kiểm sau thay source/range/cut.
3. Giả định đang dùng: K20/D06 và script C-v0.6 tiếp tục là lựa chọn đã khóa theo package; không giả định nguồn hiện hành đã phát đúng giọng đó.
4. Còn mở: local approved reference/provenance, actual independent listening, đổi giọng giữa lượt/overlap, actual AV playback và owner verdict.
5. Bước tiếp: chuẩn bị reference đúng khóa và reviewer nghe phù hợp; nghe toàn A03/R01, ghi quan sát từng lượt và chuyển vai; nếu mismatches được xác nhận thì sửa/chọn nguồn trong quyền riêng, kiểm lại source rồi AV/final. Không cần API để chạy guard; không tự dùng thêm credit để lấp khoảng trống evidence.

## Final delta check

Sau review chính, root bổ sung hai metadata fields vào manifest builder: `independent_source_speaker_review=speaker_gate['status']` và `independent_ear_review_scope='Full mix/creative voice quality not checked by SIA source gate.'`. Đã đọc lại diff và block report hiện hành; hash builder mới là `d91cc1f2421718372a9bf2c65dfeabcd1ee0f226c88c47fbc02da9b93afa02c6`.

Kiểm read-only trên bytes: mỗi dòng bổ sung xuất hiện đúng một lần; khi loại đúng hai dòng đó trong bộ nhớ, SHA-256 trở về `c9aeb5f21f8fe25d060f71aec174379cbe74d61f940a71d5bd0fd163178bdcdc`, đúng hash-at-review lịch sử phía trên. Như vậy delta chỉ bổ sung metadata mô tả scope; không đổi source_request, evaluate, validation, chốt chặn hoặc render logic.

Hai fields giúp tách source speaker verdict khỏi full mix/creative ear review. Không phát hiện issue mới ở delta này; không chạy lại acoustic hoặc nâng verdict nguồn. Source-selection vẫn HOLD, actual voice/AV/final vẫn UNKNOWN như kết luận chính. Không thay các hash-at-review lịch sử và không sửa file nào ngoài append report này.
