- 작업: DESIGN.md 맨 앞에 디자인 시스템 v1을 DRAFT로 확립했다. 출하된 src/style.css(커밋 8ab7db7, rev 20) 값을 읽어 색 18역할·글꼴 4역할과 글자 크기 단계·선/그림자/모서리·간격/조작 높이를 토큰 역할 표로 정리했고(모두 measured, 승인 값 없음), 화면 규칙 9개(사용자 지시 5, 출하 관계 measured 4), Rule Coverage 8행, Report Form, Open Decisions를 적었다. 이전 v0.1~rev 20 기록은 "이력" 아래로 내용 그대로 옮겼다. 앱 코드는 바꾸지 않았다. 렌더 검사는 vite build 후 vite preview(5198)에서 브라우저로 돌렸다.
- 업데이트 파일: DESIGN.md, ISSUES.md(DS-01, ENV-05, ENV-06), TASK.md(2026-11-10 디자인 시스템 v1), ROADMAP.md(현재/다음 줄, P7 DS1), 새 검사 스크립트 work/design/token-inventory.mjs, ds-v1-check.mjs, ds-v1-spot.mjs, ds-v1-contrast.mjs, 캡처 work/design/shots/ds-v1-*.png 4장.
- 이슈: (1) 대결줄 수 세기 글자 분홍 #ff6f91 on 흰색 대비가 2.65:1로 기준 미달(DS-01, 코드 값 계산). (2) 이 작업 폴더의 dev 서버는 node_modules가 폴더 밖으로 연결돼 글꼴 파일이 403이라 Jua·Pretendard 대신 대체 글꼴로 그려진다(ENV-05). 그래서 빌드+preview로 검사했다. (3) 엔진 파일(public/engine/rapfi*, 약 42MB)이 없어 앱이 "시작할 수 없어요"에서 멈추므로 대국 화면은 하나도 재지 못했다(ENV-06). 외부 다운로드라 허락 없이 받지 않았다. (4) 말풍선과 주 버튼 사이 보이는 간격이 크기마다 6~22px로 다르고, --danger 토큰은 쓰이지 않으며, 변수 없이 박힌 원시 색 값이 57종이다.
- 해결: 없음
- 남은 문제: v1 전체 사용자 승인 전(DRAFT). 대국 상태(추천·예정·평가·종료·복기)의 토큰·한 화면·조작 높이 렌더 검사 미실행. DS-F·DS-C·DS-V·DS-M 행은 not spot-checked. 열린 결정: 조작 높이 하한(출하 36px vs v0.1 제안 44px), 말풍선과 버튼 간격 통일 여부, 분홍 글자 색, 원시 색 값의 변수화, 간격 단계 정리. DS-01·ENV-05·ENV-06 open.
- 다음 작업: 사용자가 v1 토큰 표·규칙과 열린 결정을 검토해 승인 여부를 정한다. 엔진 파일 받기를 허락하면 ds-v1-check를 대국 상태까지 넓혀 다시 돌린다.

design-check results:
- DS-T token roles | 213/213 | 12 sizes x 1 state (intro, engine failed), light | rendered | 1440x900 bubble shadow: check 8 / observed 8 (pixel column 695-706 = border 4 + shadow 8)
- DS-O one screen (scroll, out, clip) | 24/24 | 12 sizes x 2 states (intro, help), light | rendered | 1440x900 intro: check 0 / observed 0 (all edges inside the capture)
- DS-H control height floor | 0 below floor | 12 sizes x 1 state (intro), light | rendered | 1440x900 main button: check 76 / observed 76 (pixels 727-802)
- DS-F text floor | min 12px | 12 sizes x 1 state (intro), light | rendered | not spot-checked
- DS-S bubble to main button visible gap | 6-22px, no approved value | 12 sizes x 1 state (intro), light | rendered | 1440x900 check 20 / observed 20; 390x844 check 22 / observed 22; 375x667 check 6 / observed 6
- DS-C text contrast | 14/15 | 15 token pairs x 0 states, code | code | not spot-checked
- DS-V hierarchy and cartoon look | observed, no finding | 2 sizes x 2 states (1440x900 intro, 390x844 help), light | rendered | not spot-checked
report-check: ok 2,433 chars 2bbb4a90
