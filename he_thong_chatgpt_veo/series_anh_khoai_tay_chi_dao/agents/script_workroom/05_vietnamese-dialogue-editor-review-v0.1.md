# Vietnamese Dialogue & Voice Editor — review P5-A01/P5-B01 v0.1

- **Run:** VI-DIALOGUE-20260930.
- **Status:** `REWRITE_REQUIRED` for both scripts; concept-level gate not decided here.
- **Input:** `17_p5-provisional-test-scripts-v0.1.md`, P1 character canon, approved P2/P3, language editor design v0.1.
- **Independence:** reviewed the drafts as a language/voice pass; did not choose a concept or replace Fact & Source Auditor.

## Why the drafts failed the language gate

They carried research-brief and storyboard language directly into the characters' mouths. This produces semantically careful lines that sound like a report, a translation, or a slogan. The defect affects character identity and retention, not just polish.

## A — line rewrites

| Current line | Diagnosis | Spoken alternative |
|---|---|---|
| “Một hạt gạo mà dẫn tới món này à?” | `AWKWARD / GENERIC` | Đào: “Hạt gạo này liên quan gì đến Nem Bùi vậy?” |
| “Khoan gắn nó lên miếng nem. Mình đang lần theo một chi tiết thôi.” | `TRANSLATION_LIKE / ABSTRACT` | Khoai: “Từ từ. Đây mới là gợi ý thôi — đừng cho nó lên miếng nem.” |
| “Rang rồi thành thính?” | `CLAIM_RISK` | Đào: “À, đây là thính gạo rang à?” |
| “Trong các cách làm được mô tả, thính gạo rang góp phần tạo mùi/vị.” | `REPORT_PROSE` | Khoai: “Ừ. Thính gạo rang góp một phần vào mùi vị của Nem Bùi.” `[F02]` |
| “Vậy mình không bắt món kể hết trong một cái nhìn.” | `ABSTRACT` | Đào: “Để cạnh đây. Nhìn cả món đã.” |
| “Nhưng nhìn kỹ hơn thì được.” | `GENERIC` | Khoai: “Ừ. Nhìn kỹ rồi hẵng nói.” |
| “Một món, thêm một lớp để tò mò.” | `SLOGAN` | Đào: “Rồi, mình hỏi tiếp nhé.” |

**A spoken pass candidate:**

```text
Đào: Hạt gạo này liên quan gì đến Nem Bùi vậy?
Khoai: Từ từ. Đây mới là gợi ý thôi — đừng cho nó lên miếng nem.
Đào: À, đây là thính gạo rang à?
Khoai: Ừ. Thính gạo rang góp một phần vào mùi vị của Nem Bùi.
Đào: Để cạnh đây. Nhìn cả món đã.
Khoai: Ừ. Nhìn kỹ rồi hẵng nói.
Đào: Rồi, mình hỏi tiếp nhé.
```

The “một món, thêm một lớp để tò mò” line is removed; it cannot be made conversational without changing it into a tagline.

## B — line rewrites

| Current line | Diagnosis | Spoken alternative |
|---|---|---|
| “Hôm nay tớ sẽ nói—” | `AWKWARD / GENERIC` | Khoai: “Để anh giới thiệu món này—” |
| “Nói sau. Cho món vào giữa đã.” | `MOSTLY_NATURAL / WRITTEN` | Đào: “Nói sau. Đưa món vào giữa đi.” |
| “Cận thế này đẹp, nhưng ảnh không tự chứng minh thính.” | `AWKWARD_COLLOCATION` | Khoai: “Cận thế này đẹp thật. Nhưng nhìn ảnh thôi, anh chưa dám bảo đó là thính.” |
| “Thính gạo rang góp phần tạo mùi/vị theo những cách làm được mô tả.” | `REPORT_PROSE` | Đào: “Thính gạo rang góp một phần vào mùi vị của Nem Bùi.” `[F02]` |
| “Vậy tớ không lấy cận cảnh làm kết luận.” | `TRANSLATION_LIKE` | Khoai: “Ừ. Nhìn gần hơn thôi, chưa chốt gì cả.” |
| “Nhưng vẫn nhìn kỹ hơn.” | `GENERIC` | Đào: “Nhìn rõ rồi hỏi tiếp.” |
| “Món ở giữa rồi.” | `WRITTEN / DIRECTORIAL` | Khoai: “Được rồi, món lên hình đàng hoàng rồi.” |
| “Ừ. Câu hỏi ở lại.” | `SLOGAN / EMPTY_PAYOFF` | Đào: “Giờ thì mình hỏi tiếp nhé.” |

**B spoken pass candidate:**

```text
Khoai: Để anh giới thiệu món này—
Đào: Nói sau. Đưa món vào giữa đi.
Khoai: Cận thế này đẹp thật. Nhưng nhìn ảnh thôi, anh chưa dám bảo đó là thính.
Đào: Thính gạo rang góp một phần vào mùi vị của Nem Bùi.
Khoai: Ừ. Nhìn gần hơn thôi, chưa chốt gì cả.
Đào: Nhìn rõ rồi hỏi tiếp.
Khoai: Được rồi, món lên hình đàng hoàng rồi.
Đào: Giờ thì mình hỏi tiếp nhé.
```

The “Câu hỏi ở lại” line is removed; it reads as a slogan, not as a character response.

## Character voice findings

- Khoai currently sounds like a fact-checker or research coordinator. He needs short, calm, everyday boundaries such as “từ từ”, “chưa dám”, “hẵng nói”, with occasional dry humor.
- Đào currently sounds like a content director. She needs concrete observations and active invitations, not abstract statements about how a dish “tells” a story.
- Both drafts talk too much about information design and not enough about the actual dish and their immediate choices.

## Gate result and next constraints

- Both scripts: `REWRITE_REQUIRED` at the language gate; neither is rejected at concept level by this editor.
- Suggested working address system for the rewrite: `anh/em`, because the project canon names “Anh Khoai” and “Chị Đào”; this should be treated as a working assumption until owner locks it.
- F01 remains “Nem Bùi gắn với Bùi Xá, Bắc Ninh.” F02 remains qualified; Fact Auditor must read back the final spoken wording before script lock.
- After a language rewrite, run timed read, silent/audio-only pass and independent cold reader. Do not infer production readiness from this language pass.
