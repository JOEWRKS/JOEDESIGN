그림자 깊이를 역할마다 하나의 값으로 통일했습니다. 이제 같은 역할의 카드·버튼은 모든 화면에서 그림자 깊이가 같고, 다시 어긋나면 검사가 잡습니다. 역할을 나눈 방식과 값은 제가 정했으니 화면을 보고 확인해 주세요.

- **역할별 깊이 (데스크톱/휴대폰, `src/tokens.css`):**

  | 역할 | 해당 요소 | 깊이 |
  | --- | --- | --- |
  | 카드 | 말풍선, 내 수 카드, 복기 카드, 첫 안내, 복기 바, 도움말 창, 새 게임 확인 | 8 / 6px |
  | 큰 버튼 | 주 버튼, 되돌리기, 취소 | 7 / 6px |
  | 칩 | 후보 알약, 알약, 시작 선택, 아이콘 버튼, 대결줄, 토글 | 4 / 3px |
  | 작은 표식 | 카드 라벨, 제한 안내, 돌, 판 위 표식 | 3 / 2px |
  | 판 | 판 | 10 / 7px |

- **바꾸기 전에는 이렇게 흩어져 있었습니다:**
  - 카드: 4·5·7·8px
  - 큰 버튼: 5·7px
  - 칩: 3·4px
  - 휴대폰 값도 요소마다 따로 정해져 있었습니다.
- **고친 방식:**
  - `src/style.css`의 그림자를 모두 역할 토큰으로 바꾸고, 휴대폰용 개별 그림자 설정 9줄을 지웠습니다.
  - 간격 계산도 같은 토큰을 따르게 해서, 그림자가 깊어져도 카드 사이 틈은 그대로입니다.
  - 일부러 통일하지 않은 것: 눌렀을 때 줄어드는 그림자, 로고 그림, 판 위 히트맵, 그림자가 없는 금수·엔진 안내 줄.
- **검사 추가:** `work/design/system-check.mjs`에 R12를 넣었습니다. 역할별 요소의 그림자가 토큰 값과 다르면 실패합니다.
- **결과:**
  - R12는 12크기 × 6상태 전부 통과했고, 간격·잘림·복기 바 검사도 그대로 통과합니다.
  - 캡처 픽셀로 테두리와 그림자 두께를 7곳 직접 재 보니 검사 값과 같았습니다.
  - 내 수 카드는 5px였던 그림자가 8px로 바뀐 것을 캡처로 확인했습니다.
- **업데이트 파일:**
  - 코드: `src/tokens.css`, `src/style.css`, `work/design/system-check.mjs`
  - 기록: `DESIGN.md`(그림자 표, 화면 규칙과 검사 표의 R12), `TASK.md`(ds14), `ROADMAP.md`(DS9)
  - 증거: `work/design/shots/ds10-*`
  - 커밋은 하지 않았습니다.
- **이슈:** 없음.
- **해결:** 카드마다 달랐던 그림자 깊이. 캡처 픽셀로 직접 확인했습니다.
- **남은 문제:**
  - 역할 나눔과 값(8/7/4/3px)을 확인해 주세요. 특히 복기 바와 첫 안내가 말풍선과 같은 카드 깊이가 되어 이전보다 깊어졌습니다.
  - E2E는 아직 실행하지 못했습니다.
  - 앞 턴들의 확인 요청과 LAYOUT-07, A11Y-08 결정도 남아 있습니다.

결과 목록 (preview 빌드, 엔진 대역; JOEDESIGN `report-check.mjs` 결과 ok):

- fix 카드 그림자 4·5·7·8 → 8 | fixed | 2 sizes x 1 state, light | rendered | 1440x900 candidates 내 수 카드: 5 before / observed 테두리 3+그림자 8 = 11 잉크 after, capture
- R12 역할별 그림자 | 728/728 | 12 sizes x 6 states, light | rendered | 1440x900 candidates 말풍선: check 12 / observed 12; 390x844 알약: check 6 / observed 6
- spacing-check --all | 224/224, clip 156/156 | 12 sizes x 4 states, light | rendered | not spot-checked
- system-check --all 나머지 | 이전과 같음(R8·R8B 기존 미달) | 12 sizes x 6 states, light | rendered | not spot-checked
- replay-check --all | 48/48 | 12 sizes x 4 states, light | rendered | not spot-checked

`tsc` 통과입니다.
