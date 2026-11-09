휴대폰(700px 미만)에서 판 칸을 뺀 모든 버튼을 높이 44px 이상으로 키웠고, 아이콘만 있는 버튼은 너비도 44px 이상입니다. 그 대가로 작은 휴대폰에서 판이 조금 작아졌습니다(360×640에서 270→254px).

- **작업:**
  - **바꾸기 전:** 버튼 크기 검사(R7)를 휴대폰 44×44 기준으로 고쳐 재보니 564개 중 409개만 통과했습니다. 작았던 버튼은 다음과 같습니다.
    - 도움말·새 게임 아이콘 42×42
    - 승률 가이드 스위치 38
    - 첫 안내의 건너뛰기·다음 36
    - 후보 알약 36–40
    - 시작 화면의 돌·강도 선택 40
    - 도움말 닫기 38
    - 돌 위치를 고른 상태의 되돌리기 너비 38
    - 복기 바 버튼 34
  - **변경(CSS만, `src/style.css` 끝 블록):**
    - 휴대폰의 모든 버튼에 최소 높이 44px를 주었습니다.
    - 아이콘 버튼은 44×44, 되돌리기는 최소 너비 56px입니다.
    - 복기 바의 이전/다음 버튼은 최소 너비 44px로, 바 높이는 56px로 키웠습니다.
  - **버튼이 커지면서 생긴 문제 두 가지도 같이 고쳤습니다.**
    - 489×866에서 말풍선 칸이 줄어 카드 제목("연결을 넓히는 자리")이 숨겨졌습니다. 판 크기 계산에서 버튼 영역 높이를 6px 늘려 다시 보이게 했습니다.
    - 375×667·360×640에서 후보 알약 아래가 말풍선 칸 밖으로 4px 잘렸습니다. 키 작은 휴대폰의 말풍선 칸 최소 높이를 10px 늘려 해결했습니다.
  - **그 결과 판 폭이 줄었습니다:** 489×866 446→440, 375×667 297→281, 360×640 270→254px. 보이는 글자 정보는 바꾸기 전과 같습니다.
  - **검사 기준 갱신:** `system-check`의 R7과 `replay-check`(종료 판·복기 바 버튼)를 휴대폰 44×44 기준으로 바꿔, 다시 작아지면 실패하게 했습니다.

- **업데이트 파일:**
  - `src/style.css`
  - `DESIGN.md`: R7 규칙·검사 행, 열린 결정 4, 복기 바 크기
  - `TASK.md`: ds4 항목
  - `ROADMAP.md`: DS3 추가, 현재·다음 줄
  - `work/design/system-check.mjs`, `work/design/replay-check.mjs`
  - 증거: `work/design/shots/ds4-360x640-candidates.png`, `ds4-spot.txt`
  - 커밋은 하지 않았습니다.

- **이슈:**
  - E2E는 여전히 브라우저가 없어 돌리지 못했습니다(ENV-06). 판 칸이 24px보다 작은지 보는 E2E 테스트(AC-014)도 판이 작아진 뒤로 실행하지 못했습니다.
  - 판 칸(교차점)은 44px 대상에서 뺐습니다. 15×15 판이라 휴대폰에서 칸을 44px로 만들 수 없습니다.

- **해결:**
  - 휴대폰 버튼 44px: 360×640 캡처 픽셀로 직접 확인했습니다.
  - 후보 알약 잘림: 같은 캡처에서 잘림이 없어진 것을 확인했습니다.
  - 489×866 카드 제목 접힘은 검사 데이터로만 확인했기 때문에, 아래 목록에서는 `changed`로 표시했습니다.

- **남은 문제:**
  - 판이 6–16px 작아진 것을 받아들일지 정해 주세요.
  - E2E 미실행.
  - 새 게임 확인 창, "자세히 보기"의 수순 버튼, "다시 분석" 버튼은 재지 않았습니다.
  - 앞 턴들에서 남은 것:
    - 어느 그림자를 줄일지(내 수 카드 그림자는 실제로 5px이고, 10px인 것은 판입니다)
    - 복기 바 구성 확인
    - 간격 값 확인
    - 글자 대비 부족 3곳(A11Y-05)

- **다음 작업:** 판 크기 변화를 확인해 주시면 DS3을 마칩니다. 브라우저 설치를 허가해 주시면 E2E를 돌리겠습니다.

결과 목록 (preview 빌드, 엔진 대역; JOEDESIGN `report-check.mjs` 결과 ok):

- R7 버튼 크기(휴대폰 44x44) 전 | 409/564 | 12 sizes x 6 states, light | rendered | not spot-checked
- fix 휴대폰 버튼 44px | fixed | 12 sizes x 6 states, light | rendered | 360x640 candidates: 후보 알약 check 48 / observed 48, 도움말 47 / 47, 가이드 스위치 47 / 47, 되돌리기 66 / 66, capture
- R7 후 | 564/564 | 12 sizes x 6 states, light | rendered | 360x640 candidates: check 48 / observed 48
- replay-check 종료·복기 버튼 | 48/48 | 12 sizes x 4 states, light | rendered | not spot-checked
- spacing 회귀 | 224/224, clip 156/156 | 12 sizes x 4 states, light | rendered | not spot-checked
- fix 360x640·375x667 후보 알약 잘림 | fixed | 2 sizes x 1 state, light | rendered | 360x640 candidates: 알약 아래 4px 잘림 before / 0 after, capture
- fix 489x866 카드 제목 접힘 | changed | 1 size x 3 states, light | rendered | not spot-checked (검사 데이터의 보이는 글자 목록으로만 확인)
- 보이는 정보 전후 비교 | 72/72 같음 | 12 sizes x 6 states, light | rendered | not spot-checked
