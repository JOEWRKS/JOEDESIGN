판 위 추천(1순위) 고리를 더 진한 초록 #17692A로 바꿨습니다. 판 바탕과의 대비가 2.1:1에서 4.05:1로 올랐습니다(판에서 가장 어두운 쪽 기준, 캡처 픽셀로 측정).

- 작업: 바꾸기 전 고리 색 #2F9C3A는 판 두 끝색(#FFD98A·#F5BD5C) 위에서 대비가 2.62 / 2.07로, 구분에 필요한 3:1에 못 미쳤습니다. 새 변수 `--rec-ring`(#17692A)을 만들어 추천 고리 테두리에만 썼고, 고리 안 연두 채움·두께·점선 모양은 그대로 두었습니다. 필승 고리(노랑)와 나머지 후보(남색 점선)는 바꾸지 않았습니다. 다시 어긋나지 않도록 고리 색과 대비를 재는 검사 `work/design/ring-check.mjs`를 추가했습니다.
- 업데이트 파일: `src/style.css`, `DESIGN.md`(색 표, 규칙 14, 점검 행), `ROADMAP.md`(DS5, 현재·다음 줄), `TASK.md`, 새 검사 `work/design/ring-check.mjs`, `work/design/system-audit.mjs`(색 표에 추가), 로그 `work/design/ring-before.log`·`ring-after.log`·`matrix-ring.log`·`system-audit-ring.log`. 확대 캡처 `work/design/matrix/ring-1440-crop.png`. 커밋하지 않았습니다.
- 이슈: 색 값은 제가 골랐습니다. 더 밝은 #1D7A2B는 판 어두운 쪽 대비가 3.08로 여유가 적어서 뺐습니다. 엔진 후보가 없을 때 나오는 추천 고리에도 같은 색을 적용했지만, 이번 흐름에서는 그 상태가 나오지 않아 화면으로 보지 못했습니다.
- 해결: 추천 고리와 판의 구분. 1440×900 후보 화면 캡처에서 고리 픽셀 대비가 2.11에서 4.05가 된 것을 확인했습니다.
- 남은 문제: 새 색에 대한 사용자 확인(DS5). 12크기 전체는 돌리지 않았습니다(기본 두 크기). 지난 턴들의 질문(그림자 대상, 복기 바 모양, 판 10px 축소, `--all` 운영, DS1·DS3, DES-01·DES-02)은 그대로 열려 있습니다.
- 다음 작업: 색이 괜찮은지 알려 주세요. 더 진하거나 다른 초록을 원하시면 같은 검사로 다시 확인하겠습니다.

design checks:
- rec ring before | 0/2 | 2 sizes x 1 state, light | rendered | 1440x900 candidates: check 2.62/2.07 / observed pixel 2.58/2.11
- fix rec ring contrast | fixed | 2 sizes x 1 state, light | rendered | 1440x900 candidates ring pixel: 2.11 before / 4.05 after vs dark board end
- rec ring after | 2/2 | 2 sizes x 1 state, light | rendered | 390x844 candidates: check 5.03/3.99 / observed pixel 4.94/4.06
- overflow and clipping | 12/12 frames clean | 2 sizes x 6 states, light | rendered | not spot-checked
- color, shadow, control rules | 0 violations | 2 sizes x 7 states, light | rendered | not spot-checked
report-check: ok 1,756 chars ac243e2a
