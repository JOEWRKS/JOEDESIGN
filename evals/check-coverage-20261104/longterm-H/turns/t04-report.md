복기 모드에 상단 바를 추가했습니다. 복기 중에는 화면 맨 위 줄의 대결줄(나 · 수 · AI) 자리에 `[◀ 이전 수] [4 / 9수] [다음 수 ▶] [종료 판으로]` 바가 나옵니다. 말풍선 영역에 있던 복기 버튼 3개는 이 바로 옮겼습니다. 바의 자리와 모양은 제가 고른 것이라 확인이 필요합니다.

- 작업: 복기 중에만 대결줄을 숨기고 같은 자리에 바를 보이게 했습니다. 바는 대결줄과 같은 흰 알약에 남색 테두리이고, "종료 판으로"만 노란색입니다. 휴대폰 폭(700px 이하)에서는 이전·다음 버튼을 ◀ ▶ 기호로만 줄이고, 화면 읽기용 이름은 그대로 둡니다. 종료 결과·총 수 문장("종료된 대국: 흑 승리 · 총 9수")은 말풍선 안으로 옮겼습니다. 말풍선 영역에는 대국이 끝난 뒤의 "대국 복기" 시작 버튼만 남고, 복기 중에는 그 칸이 숨습니다. 버튼 id와 초점 이동(시작 → 다음 수, 종료 판으로 → 대국 복기)은 그대로라 기존 테스트가 쓰는 이름은 바뀌지 않았습니다.
- 업데이트 파일: `src/main.ts`, `src/style.css`, `DESIGN.md`(규칙 13과 점검 행), `ROADMAP.md`(P5에 RPL4 추가, 현재·다음 줄), `TASK.md`, 새 검사 `work/design/replay-bar-check.mjs`, 로그 `work/design/replay-bar.log`·`spacing-after-replay.log`·`matrix-replaybar.log`. 캡처는 `work/design/matrix/replay-*.png`. 커밋하지 않았습니다.
- 이슈: 엔진 파일이 없어 실제 대국으로 복기를 확인하지 못했습니다. 가짜 엔진의 AI가 판 구석에 두게 해서, 흑 H8~L8 다섯으로 9수 만에 끝낸 대국으로 확인했습니다. 기존 복기 E2E(`tests/e2e/replay.spec.ts`)는 실제 엔진이 필요해 돌리지 못했습니다.
- 해결: 없음
- 남은 문제: 바의 자리·모양에 대한 사용자 확인(RPL4). E2E 실행. 무승부·백 승 대국의 복기, 색·그림자 토큰 점검의 복기 상태 포함. 지난 턴들의 DS1·DS3 확인, DES-01·DES-02, 턴 3의 그림자 대상 질문은 그대로 열려 있습니다.
- 다음 작업: 바 모양이 괜찮은지 알려 주세요. 엔진 파일을 내려받아도 된다고 하시면 E2E로 실제 대국 복기를 확인하겠습니다.

design checks:
- replay bar | 120/120 | 12 sizes x 10 checks, light | rendered | 360x640 replay start bar to help button: check 8.0px / observed 8px between ink edges at y=29 in capture
- spacing S1/S2 | 198/198 | 12 sizes x 6 states, light | rendered | not spot-checked
- overflow and clipping | 72/72 frames clean | 12 sizes x 6 states, light | rendered | not spot-checked

상세 보고:
- 바 검사가 보는 것: 복기 전에는 대결줄만 보이는지, 복기 중에는 바만 보이고 말풍선 영역에 옛 버튼이 없는지, 수 번호와 총 수, 처음·끝의 버튼 비활성, 초점, 결과 문장, 바가 상단 줄 안에서 도움말 버튼과 4px 이상 떨어지는지, 버튼 높이 32px 이상, 잘림과 스크롤입니다. 위의 넘침 검사 72장에는 복기 상태가 들어 있지 않고, 바의 넘침은 바 검사가 봅니다.
- 360×640처럼 가장 좁은 화면에서 바와 도움말 버튼 사이가 8px입니다. 이보다 좁은 화면은 재지 않았습니다.
report-check: ok 1,841 chars 86bcee1f
