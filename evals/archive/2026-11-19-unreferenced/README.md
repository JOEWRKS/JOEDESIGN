# 참조 없는 기록 보관 (2026-11-19, T043, 2.0.0 후보)

`v02-operational-validation-v1/`은 원래 `fixtures/contract-cases/evidence/v02-operational-validation-v1/`에 있던 기록 52개(약 18.8MB)다.
저장소의 테스트·회귀 스크립트·문서 어느 것도 이 폴더를 가리키지 않아(`evals/v2-survey-20261119/report.md` 1-e절 5번) 2.0.0 위생 작업에서 여기로 옮겼다. 내용은 지우지 않았다.

## 바뀐 것

- 위치만 옮김(git rename).
- 파일 8개에서 사용자 이름이 든 홈 경로를 `~`로 가렸다: authority/PRODUCT.md, authority/approved-visual-authority.md, authority/asset-manifest.json, authority/input-audit.md, final/pm-report.md, phase1/candidate-input.md, phase1/capture.mjs, phase1/verify.mjs.
- 그래서 이 8개의 해시는 `final/manifest.json`에 적힌 값과 더는 맞지 않는다. 원래 바이트는 git 이력(2.0.0 직전 커밋까지의 원래 경로)에 있다. 이 폴더 안의 `capture.mjs`·`verify.mjs`는 기록을 만든 도구이며, 옮긴 뒤 다시 실행하는 것을 전제로 하지 않는다.
