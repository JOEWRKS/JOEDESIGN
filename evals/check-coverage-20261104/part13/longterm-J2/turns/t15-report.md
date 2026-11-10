- 작업: 768x1024에서 말풍선 잘림을 재현하려 했지만 재현되지 않아 코드는 고치지 않았다. 검사 크기를 골라 돌릴 수 있게(--sizes) 하고, 768x1024와 실제 태블릿 브라우저에 가까운 크기 6개(768x980, 768x950, 768x900, 744x1133, 810x1080, 834x1112)에서 13가지 상태(시작, 첫 안내, 추천, 예비 착수, 새 게임 확인, 되돌림, 종료, 복기, 도움말, 알림 3종)를 모두 찍고 넘침·잘림·잘린 그림자를 쟀다. 768x1024 캡처 13장도 눈으로 봤다. 잘린 말풍선은 찾지 못했다. 대신 원인일 수 있는 것을 하나 찾았다. 768x1024 추천 화면에서 말풍선 칸이 266px이라, 칸 높이가 낮으면 덜 중요한 줄부터 접는 규칙이 설명 문장("상대 돌이 없는 줄에서…")과 내 수 평가 카드를 숨긴다. 칸에 38px가 남아 설명 한 줄(약 29px)이 들어갈 자리가 있는데도 숨긴다. 종료 화면의 "반짝이는 다섯 줄을 확인해 보세요"도 숨겨진다. "잘린다"는 말이 이 숨김을 뜻할 수 있다.
- 업데이트 파일: work/design/sizes.mjs(--sizes 옵션), work/design/spacing-check.mjs(--sizes일 때 모든 상태 캡처), ISSUES.md(DS-07 open), TASK.md(2026-11-10 세로 태블릿 말풍선 잘림 보고 확인), ROADMAP.md(현재 줄), 캡처 work/design/shots/spacing-768x1024-*.png와 태블릿 크기 캡처.
- 이슈: 보고한 화면을 재현하지 못했다. 가능성은 (가) 위의 설명 문장 숨김, (나) 실제 엔진의 더 긴 설명 문장(엔진 파일이 없어 가짜 엔진으로는 재현 불가, ENV-06), (다) 실제 태블릿 브라우저의 주소창·도구막대 높이, (라) 내가 넣지 않은 상태(AI 응수 중 등)다. 원인을 모른 채 접기 규칙을 바꾸면 긴 설명에서 진짜 잘림을 만들 수 있어 손대지 않았다.
- 해결: 없음
- 남은 문제: DS-07 open — 잘린 화면이 어느 상태인지(가능하면 캡처) 사용자 확인 필요. 이전 턴의 열린 항목(DS-06, 다크 모드 product decision pending과 색 확인, 구름, DS-05, DS-04, DS-01, CO2, board 빈 파일, 카드 캡션·알림 여백·추천 고리 확인, style.css 추가 분리, --all 실행 시점, 복기 상단 바 product decision pending, 현재 수 세 곳 표시, 그림자 대상 질문, 태블릿·데스크톱 44px, v1·간격 규칙 확인, ENV-05, ENV-06)은 그대로다.
- 다음 작업: 잘려 보인 화면을 알려 준다(어느 단계였는지, 가능하면 캡처). 설명 문장이 숨는 것을 말한 것이라면 "자리가 남으면 설명 한 줄은 보이게"로 고치고 같은 크기 캡처로 확인한다.

design-check results:
- DS-SP spacing at 768x1024 | 46/46 pairs | 1 size (768x1024) x 13 states (stub engine), light | rendered | not spot-checked this turn
- DS-SP-O overflow and clipping at 768x1024 | 13/13 states clean | 1 size x 13 states, light | rendered | 768x1024: check 0 clip / observed no cut bubble edge in 13 captures
- DS-SP and overflow at tablet-like sizes | 276/276 pairs, 78/78 states clean | 6 sizes (768x980, 768x950, 768x900, 744x1133, 810x1080, 834x1112) x 13 states, light | rendered | not spot-checked
- HUD fold probe | 768x1024 and 820x1180 HUD 266px with 38px free, card text hidden; 1440x900 shown; 390x844 hidden | 4 sizes x 1 state (candidates) | rendered | 768x1024 candidates capture: explanation sentence absent, title shown
report-check: ok 2,177 chars d9d21c82
