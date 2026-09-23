# Operational input audit — resolved after user clarification

The first-pass input gate and its then-correct `BLOCKED_BY_INPUT` report are
preserved in `../history/`. A later direct user reply nominated BIO/02 and the
exact approval scope. No synthetic authority or substitute asset was created.

| Required preflight input | Current finding |
| --- | --- |
| Project path | `C:/Users/tjdwo/Documents/포폴만들기/bio02-medical-site/.worktrees/bio02-gate-b-accepted` exists |
| Branch / HEAD | `codex/bio02-living-atlas` / `20da3d15c92c4c6b0786a3b7e76c460e2506d5f1` |
| Design authority | Root `DESIGN.md` exists; APPROVED Revision 1 at `a7de6e82a7b6e12d73dd14b8ba6ef8d0c26ff2af` |
| Approved PNGs | KF-01/02/03 desktop and mobile all exist and match the approval-record SHA-256 values; local unchanged copies are in `originals/` |
| Proof sources | `src/proofs/kf-01`, `kf-02`, `kf-03` source components/CSS inspected; no diff against corresponding approval proof commits |
| Actual assets | Five image paths traced from proof source; all exist and are hashed in `asset-manifest.json`; no `ASSET_MISSING` |
| Product authority | Root `BIO02_CODEX_MASTER_HANDOFF_V1.md` explicitly identifies itself as the authoritative consolidated handoff; root `DESIGN.md` delegates Product/UX authority there and the active Product/UX contract. Relevant Home meaning is in `PRODUCT.md` |
| JOEDESIGN v0.2 | Isolated validation branch starts at `2ccb229353ebb2776ebed793056158efffb50b33`; shipped bytes match frozen v0.2 hashes |

Approval boundary: static KF-01/02/03 states at 1440×900 desktop and 390×844
mobile. The motion proof at the user-named BIO HEAD is not user-accepted;
timing, easing and transitions are not approved visual authority. Product
meaning and existing healthy behavior remain protected.
