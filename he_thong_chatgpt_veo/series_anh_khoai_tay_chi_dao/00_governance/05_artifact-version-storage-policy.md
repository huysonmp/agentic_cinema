# Artifact, Version and Storage Policy

- **Version:** P0-v1
- **Status:** proposed

## Source of truth

- Governance, brief, script, register và QC: Markdown/JSON/CSV trong folder project.
- Media thật và project editor: owner lưu trong `media/`; không commit Git.
- Mọi media phải có record trong asset/generation/delivery manifest.

## Naming

```text
<series>_<episode>_<artifact>_vNN_<status>.<ext>
```

Ví dụ:

```text
khoai-tao_ep01_script_v03_APPROVED.md
khoai-tao_ep01_sh03_candidate_c02.mp4
khoai-tao_ep01_master_v02_QC-PASS.mp4
```

## Rules

- Không ghi đè version `APPROVED`, `QC-PASS`, `ACCEPTED`.
- Revision mới phải liên kết version bị thay thế và lý do.
- Raw candidate của pilot được giữ đầy đủ tới khi retrospective hoàn tất.
- Mỗi master/delivery file có checksum trong delivery manifest.
- Retention cho batch còn lại được quyết định sau pilot.

## Local media layout

```text
media/raw/
media/selected/
media/editor-projects/
media/masters/
```

