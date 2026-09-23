# Approved visual authority — static BIO/02 keyframes only

Project root: `C:/Users/tjdwo/Documents/포폴만들기/bio02-medical-site/.worktrees/bio02-gate-b-accepted`

Design contract: root `DESIGN.md`, APPROVED Revision 1, commit `a7de6e82a7b6e12d73dd14b8ba6ef8d0c26ff2af`. Each proof below is scoped preservation evidence, not a second project-wide authority. All six files exist; each matches the SHA-256 stated in its approval record. The approval commits exist and the corresponding `src/proofs/kf-0N` source has no diff from its approval commit at the user-named HEAD.

| Surface / approved state | Approval source / proof commit | Desktop 1440×900 | Mobile 390×844 |
| --- | --- | --- | --- |
| KF-01 Opening Hero / static initial | `docs/qa/BIO02_KF01_OPENING_HERO_APPROVAL_2026-09-05.md` / `b18c079c3ca79a78c501cbe9e2a08bdf181d1b20` | `artifacts/kf-01/attempt-01/kf01-proof-desktop-1440x900.png` (`6558511d0af876bd847c04146506b355f22ab13f5b4b0f1fb5b524d817c33056`) | `artifacts/kf-01/attempt-01/kf01-proof-mobile-390x844.png` (`2f32446325ca5ff2290a1abe0833d68fa360efad150c39d8dc47913f66c6b719`) |
| KF-02 Structural Transformation Midpoint / static midpoint | `docs/qa/BIO02_KF02_STRUCTURAL_TRANSFORMATION_APPROVAL_2026-09-05.md` / `85e269dd6691b2c4ba2d3fbe71cc90284205121e` | `artifacts/kf-02/attempt-02/kf02-proof-desktop-1440x900.png` (`c2b0362c3966056174650752de1535dfccf72937c851af11d112c45697299a20`) | `artifacts/kf-02/attempt-02/kf02-proof-mobile-390x844.png` (`ae39f75bbf9985d2d392a68589bc2d249e674f86a43c77ee4e0af13d5421f75d`) |
| KF-03 Scientific Field → Evidence World / static transition keyframe | `docs/qa/BIO02_KF03_EVIDENCE_WORLD_APPROVAL_2026-09-05.md` / `91ade65dd33120749629a7ab4cca2b63ad0b5a62` | `artifacts/kf-03/attempt-01/kf03-proof-desktop-1440x900.png` (`6244532866ae995112aa07f6e59599d69ec81f2b131ab1c7e04b40a1a5066b0b`) | `artifacts/kf-03/attempt-01/kf03-proof-mobile-390x844.png` (`5900d28618d0536c0c512a21de13747d9813fb0d76ff63ab224718bd3bfa453c`) |

Proof source: `src/proofs/kf-01/KF01OpeningHero.tsx` and `kf-01.css`; `src/proofs/kf-02/KF02StructuralMidpoint.tsx` and `kf-02.css`; `src/proofs/kf-03/KF03EvidenceTransition.tsx` and `kf-03.css`. The implementation must retain direct access to the original PNGs and actual project assets; this index does not replace the originals.

Repository-contained copies for independent review are in `originals/` with the
same basenames and SHA-256 values shown above. They are byte-for-byte copies,
not regenerated authority or new mockups.

Not approved: motion timing/easing/transitions between the keyframes, production Home integration, full Home, other states or viewport compositions. The current motion proof at `20da3d15c92c4c6b0786a3b7e76c460e2506d5f1` remains `USER VISUAL ACCEPTANCE: PENDING`.
