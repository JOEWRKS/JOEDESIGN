말풍선 안 11px 글자는 한 군데뿐이었고, 12px로 올렸습니다. 이제 14크기 × 6상태 어디에서도 말풍선 안에 12px보다 작은 글자가 없습니다.

- **작업:**
  - 14크기 × 6상태(시작, 첫 수, 예비 착수, 후보, 종료, 복기), 총 84곳에서 말풍선 안의 보이는 글자 크기를 모두 쟀습니다.
  - 12px 미만은 예비 착수 때 나오는 부제("상대 예상 H8 · 번호는 이어질 수순 3수") 11px 하나였습니다. 말풍선 칸이 낮은 9개 크기(세로 휴대폰·태블릿과 가로 2크기)에서 나타났습니다.
  - 이 부제를 12px로 바꿨습니다. 지금은 쓰이지 않는 "자세히 보기" 화면 규칙의 같은 11px도 함께 12px로 바꿨습니다.
  - 다음 11px 글자는 말풍선 밖이라 그대로 뒀습니다.
    - 내 수 카드 아래 캡션
    - 휴대폰 고지문("엔진 추정 승률 · 실제 승률 아님")
    - 복기 바의 결과 줄
    - 휴대폰 도움말 라이선스 11.5px
  - 다시 작아지지 않도록 `system-check`의 R6(최소 글자 크기) 기준을 말풍선 안은 12px로 올렸습니다.
- **결과:**
  - 부제가 두 줄로 꺾이거나 말풍선이 칸 밖으로 잘린 곳은 없습니다.
  - 14크기 전체 디자인 검사에서 새 실패가 없습니다. 실패로 남은 것은 기존 대비 미달(A11Y-05)뿐입니다.
  - 390×844 캡처에서 부제 글자 높이가 10px에서 11px로 커진 것을 픽셀로 확인했습니다.
- **업데이트 파일:**
  - 코드: `src/style.css`, `work/design/system-check.mjs`
  - 기록: `DESIGN.md`(R6 규칙·검사 행), `TASK.md`(ds24), `ROADMAP.md`(DS15)
  - 캡처: `work/design/shots/ds16-*`
  - 커밋은 하지 않았습니다.
- **이슈:** 없음.
- **해결:** 말풍선 부제 11px. 캡처로 직접 확인했습니다.
- **남은 문제:**
  - 말풍선 밖 11px 글자(위 목록)도 12px로 올릴지 정해 주세요.
  - 앞 턴들의 확인 요청과 LAYOUT-07, A11Y-08, A11Y-05 결정이 남아 있습니다.

결과 목록 (preview 빌드, 엔진 대역; JOEDESIGN `report-check.mjs` 결과 ok):

- fix 말풍선 부제 11px → 12px | fixed | 9 sizes x 1 state, light | rendered | 390x844 route #hero-sub: 잉크 10px(11px) before / 11px(12px) after, capture
- 말풍선 안 12px 미만 글자 | 0/84 | 14 sizes x 6 states, light | rendered | not spot-checked
- design:check --all | R6 1769/1769·R1 84/84, spacing 256/256·clip 182/182, replay 56/56, R8·R8B 기존 미달 | 14 sizes x 6 states, light | rendered | 390x844 route: check 12px / observed 잉크 11px

`tsc` 통과입니다.
