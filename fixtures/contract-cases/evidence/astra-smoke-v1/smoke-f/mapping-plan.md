# Smoke F pre-edit semantic mapping

Recorded before the implementation candidate. `DESIGN.md` is authority; existing CSS roles are implementation targets, not authority.

| semantic role | before project-native role/value | intended after | source | reason | scope |
| --- | --- | --- | --- | --- | --- |
| `surface.page` | `--workspace` / `#F2F4F7` | reuse `--workspace` / `#F6F7F4` | APPROVED `DESIGN.md` Rev 1 | exact approved page surface | Smoke F page |
| `surface.panel` | `--sheet` / `#FFFFFF` | reuse `--sheet` / `#FFFFFF` | APPROVED `DESIGN.md` Rev 1 | existing equivalent exact value | Smoke F panels |
| `text.primary` | `--copy` / `#1E2520` | reuse `--copy` / `#1E2520` | APPROVED `DESIGN.md` Rev 1 | existing equivalent exact value | Smoke F text |
| `action.primary` | `--commit-action` / `#3459A8` | reuse `--commit-action` / `#205C4A` | APPROVED `DESIGN.md` Rev 1 | material exact-value correction without role rename | primary action only |
| `space.section` | `--section-gap` / `24px` | reuse `--section-gap` / `32px` | APPROVED `DESIGN.md` Rev 1 | exact approved section rhythm | major page sections |
| `status.attention.icon` | no role/value | unresolved; do not create | APPROVED `DESIGN.md` Rev 1 Open Visual Decisions | authority intentionally omits the value | no implementation mapping |

No project-native role rename or token architecture change is planned. JOEDESIGN custom rationale, Visual Flow, Approved Visual Evidence, Open Visual Decisions, and responsive prose remain in `DESIGN.md` rather than being flattened into structured tokens.

