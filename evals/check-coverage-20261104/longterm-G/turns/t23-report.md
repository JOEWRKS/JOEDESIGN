다른 세션이 바꾼 것은 승률 가이드 토글을 파란색으로 바꾼 한 건(ds18)이고, 화면 자체는 DESIGN 기준에 맞습니다. 다만 그 세션의 검사 결과는 글꼴이 없는 dev 서버를 잰 값이었고, 원인은 제가 만든 `design:check` 진입점의 결함이라 그것을 고쳤습니다.

**바뀐 것** (커밋이 없어 파일 수정 시각과 TASK로 대조)
- `src/tokens.css`: 새 토큰 `--switch-on` #1F6FB0
- `src/style.css`: 켜진 토글의 알약을 하늘색(`--sky-btn`), 글자를 진한 남색, 스위치를 `--switch-on`으로
- DESIGN 토큰 행, ROADMAP DS12, 캡처 `ds18-*`
- `src/main.ts`와 검사 스크립트는 그대로입니다.

**어긋난 것과 고친 것: 검사 진입점**
- 그 세션의 `design:check` 결과에 R5 183/207(글꼴 로드 실패)이 있었습니다. 5299 포트에 떠 있던 dev 서버를 잰 것입니다. 이 폴더의 dev 서버는 글꼴 파일을 403으로 거절합니다(ENV-06).
- 원인은 `work/design/design-check.mjs`의 결함입니다. 포트가 이미 쓰이고 있어 자기 preview 서버가 못 떴는데도, 그 포트의 다른 서버 응답을 받아 그대로 쟀습니다.
- 이제는 직접 띄운 preview 서버가 살아 있을 때만 재고, 포트가 다른 서버에 쓰이고 있으면 안내를 띄우고 종료 코드 1로 멈춥니다.
- 확인: 5299에 dev 서버를 띄운 채 실행하면 멈추고, 끄고 실행하면 정상으로 돕니다. 그 확인용 dev 서버는 끈 상태입니다.

**다시 잰 결과** (출하 빌드, 실제 글꼴, 엔진 대역, 기본 2크기)
- 밝은 모드·다크 모드 모두 R5 글꼴 207/207, R7 버튼 크기 94/94, R12 그림자 123/123입니다.
- R8 글자 대비에 토글 관련 미달은 없습니다. 남은 미달은 원래 있던 A11Y-05(R8·R8B)뿐입니다.
- spacing·replay 검사는 두 모드 모두 통과, 동작 감소(R13)도 12/12입니다.
- 그 세션에는 없던 실제 대국 화면(후보 상태) 캡처도 밝은·다크 모두 찍었습니다. 켜진 토글은 하늘 알약에 남색 글자, 파란 스위치로 보입니다.

**고치지 않고 판단을 맡길 것 (색은 정하실 부분이라 그대로 둠)**
- 켜진 토글 알약 색이 바로 위 되돌리기 버튼과 같은 하늘색이라, 휴대폰에서 두 버튼이 한 묶음처럼 보일 수 있습니다. 이 하늘색은 DESIGN 토큰 표에서 "되돌리기·안내" 역할의 색입니다.
- 켜진 스위치(#1F6FB0)와 하늘 알약의 대비가 2.67:1로, 상태 표시에 권장되는 3:1보다 낮습니다. 지금은 남색 테두리와 손잡이 위치로 켜짐/꺼짐이 구별됩니다.

**업데이트 파일**
- `work/design/design-check.mjs`
- `TASK.md`(ds19), `ROADMAP.md`(현재 줄), `DESIGN.md`(검사 명령 설명)
- 캡처: `work/design/shots/ds13-*`
- 커밋은 하지 않았습니다.

**남은 문제**
- 위의 토글 색 두 가지를 정해 주세요.
- E2E는 아직 실행하지 못했습니다.
- 앞 턴들의 확인 요청과 LAYOUT-07, A11Y-08, A11Y-05 결정도 남아 있습니다.

결과 목록 (JOEDESIGN `report-check.mjs` 결과 ok):
- fix design:check가 다른 서버를 재던 문제 | fixed | 1 port x 2 runs | code | 5299에 dev 서버를 띄운 채 실행: 다른 서버 응답으로 잼 before / 멈춤·종료 코드 1 after, observed
- design:check --both | system-check R5 207/207·R7 94/94·R12 123/123, R8·R8B 기존 미달, spacing·replay PASS | 2 sizes x 6 states, light+dark | rendered | not spot-checked
- design:check --reduce R13 | 12/12 | 2 sizes x 6 states, light, reduced motion | rendered | not spot-checked

`tsc` 통과입니다.
