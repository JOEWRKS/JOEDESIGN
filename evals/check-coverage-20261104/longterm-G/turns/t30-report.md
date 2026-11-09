모든 버튼의 눌림 효과를 같은 방식으로 맞췄습니다. 이제 어떤 버튼을 눌러도 그림자가 1px만 남을 만큼 내려앉고, 그림자 아래 끝은 제자리에 있습니다.

- **"새 게임 버튼"의 범위:** 위쪽 새 게임 아이콘과 대국이 끝났을 때 나오는 "새 게임!" 버튼 둘 다 해당될 수 있어서, 둘을 포함한 모든 버튼을 함께 맞췄습니다.
- **바꾸기 전 측정** (DevTools로 눌린 상태를 강제해 전후 위치를 잼):
  - 휴대폰에서는 새 게임 아이콘, "새 게임!", 주 버튼 등 모든 버튼이 눌릴 때 1px 더 내려가 바닥보다 아래로 꺼졌습니다. 지난번 그림자를 휴대폰에서 얇게 바꿀 때 눌림 값을 같이 고치지 않은 탓입니다.
  - 데스크톱에서는 취소 버튼만 다른 큰 버튼보다 덜 내려가, 그림자 끝이 2px 위로 떴습니다.
  - 남는 그림자 두께도 아이콘·알약은 1px, 큰 버튼은 2px로 달랐습니다.
- **고친 방식:**
  - 눌림 그림자 두께를 토큰 `--lift-pressed` 1px 하나로 정했습니다.
  - 눌림 규칙 7곳(아이콘, 후보 알약, 알약, 시작 선택, 주 버튼, 되돌리기, 취소)을 "역할 그림자 − 1px만큼 내려앉음"으로 바꿨습니다.
- **결과:**
  - 1440×900과 390×844에서 버튼 9종(새 게임 아이콘, 도움말, 주 버튼, 되돌리기, 후보 알약, 취소, 두기, 새 게임!, 대국 복기)을 쟀습니다. 모두 눌림 전후 그림자 끝 이동이 0px이고, 남는 그림자는 1px입니다.
  - 다시 어긋나지 않게 `work/design/press-check.mjs`(R15)를 만들어 `npm run design:check`에 넣었습니다. 밝은·다크 모두 18/18 통과했고, 다른 검사 결과도 그대로입니다.
- **업데이트 파일:**
  - 코드: `src/tokens.css`, `src/style.css`, `work/design/press-check.mjs`(새 파일), `work/design/design-check.mjs`, `work/design/sizes.mjs`(안내 문구)
  - 기록: `DESIGN.md`(눌림 행, 화면 규칙과 검사 표의 R15), `TASK.md`(ds25), `ROADMAP.md`(DS16)
  - 커밋은 하지 않았습니다.
- **이슈:** 없음.
- **해결:**
  - 휴대폰에서 버튼이 1px 더 꺼지던 것
  - 취소 버튼이 덜 내려가던 것
  - 둘 다 렌더 위치로 직접 확인했습니다. 캡처 대조는 하지 않았습니다.
- **남은 문제:**
  - 바뀐 눌림이 괜찮은지 직접 눌러 보고 확인해 주세요. 큰 버튼은 이전보다 1px 더 내려앉습니다.
  - 새 게임 확인 창의 버튼은 측정하지 못했습니다. 끝난 판에서는 확인 창 없이 바로 새 게임이 시작되기 때문입니다.
  - 앞 턴들의 확인 요청과 LAYOUT-07, A11Y-08, A11Y-05 결정이 남아 있습니다.

결과 목록 (preview 빌드, 엔진 대역; JOEDESIGN `report-check.mjs` 결과 ok):

- fix 휴대폰 눌림 1px 더 꺼짐 | fixed | 1 size x 3 states, light | rendered | 390x844 새 게임!(종료): 그림자 끝 +1px before / 0px after, observed 렌더 위치
- fix 취소 눌림이 덜 내려감 | fixed | 2 sizes x 1 state, light | rendered | 1440x900 취소: 그림자 끝 -2px before / 0px after, observed 렌더 위치
- press-check R15 | 18/18 | 2 sizes x 3 states, light+dark | rendered | not spot-checked
- design:check --both 나머지 | spacing·replay PASS, R8·R8B 기존 미달 | 2 sizes x 6 states, light+dark | rendered | not spot-checked

`tsc` 통과입니다.
