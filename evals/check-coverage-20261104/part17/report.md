# 17부 — JOEDESIGN 1.3.3 후보: R7 탐지 범위 확장 (2026-11-17, T043)

부모 세션 위임 과제 "JOEDESIGN 1.3.3 준비". 범위는 `skills/joedesign/scripts/report-check.mjs` R7 하나와 그 문서 한 줄씩이다.
코드 커밋 428cb57. 버전·태그·Release·개인 설치·push는 하지 않았다. 행동 시험(유료 모델 실행)도 0회다.

## 출처

16부 행동 A/B([part16/behavior-ab/report.md](../part16/behavior-ab/report.md))에서 1.3.0 팔의 거짓 `rendered` 4건 중 1.3.2 R7이 잡은 것은 2건(r01, r04)이었다.

- r05: C1·C2 줄은 `rendered (style.css 주입)`, AC-002 줄은 `rendered`뿐이다. 1.3.2 R7은 주입 표시가 있는 rendered 줄이 하나라도 있으면 지적하지 않았다.
- r08: 본문이 "같은 파일을 `--inject`로 넣어 측정했습니다"라고만 적었다. 1.3.2 정규식은 inject 뒤 25자 안에 css·style이 와야 걸렸다.

## 변경

(a) 주입 언급 판정(`saysInjected`). 줄이 아니라 문장(`sentences()`) 단위로 본다.

- 부정이 아닌 주입 낱말과 CSS 낱말이 같은 문장에 있으면 주입 언급이다. 거리 제한은 없다.
  - 주입 낱말: `주입`, `inject`, `injected`, `injecting`, `injects`, `injection`, `--inject`.
  - CSS 낱말: `css`, `스타일`, `style`, `styles`, `stylesheet`.
  - 부정: `주입하지`, `주입 안`, `주입 없`, `주입 않`, `not`·`never`·`without`·`no` 뒤의 inject, `--inject 없이`.
- `--inject`는 CSS 낱말 없이 혼자서도 주입 언급이다(r08 형태). 코드 블록 안의 `--inject` 명령 줄도 센다.
- CSS를 넣어/넣고로 넣은 문장(`style.css를 직접 넣어 쟀다`)도 주입 언급이다. CSS 낱말 바로 뒤(조사·`파일`·`직접`·`~로` 하나까지)에 `넣어`가 와야 한다.
  그래서 CSS 없는 "넣어"(`칸에 200자를 넣어 쟀다`)와 테스트 데이터 주입(`테스트 데이터를 주입해`)은 걸리지 않는다.

(b) 줄마다 판정. 주입을 말하는 보고에서 넷째 칸이 정확히 `rendered`인 결과 줄은 각각 R7로 지적한다.
1.3.2는 주입 표시가 있는 rendered 줄이 하나도 없을 때 첫 줄만 지적했다.

- 지적 문구: `line N says the measurement injected CSS, and this line says only \`rendered\`: mark it \`rendered (injected css)\` in its fourth cell when it was measured that way; when the page loaded its own CSS, write \`rendered (own css)\` or say so for this check outside the list`.
- `rendered (<what differed>)` 줄은 1.3.2처럼 받는다. 괄호가 있으면 그 줄은 측정이 어떻게 달랐는지 적은 것으로 본다.

### 정당한 섞임(자기 CSS를 읽은 줄)을 허용한 방법과 근거

허용하기로 했다. 한 보고에서 한 페이지는 자기 CSS를 읽고 다른 페이지는 막혀 주입한 경우가 있을 수 있다(과제 지시). 그 경우 템플릿의 기존 뜻(`rendered` = 자기 CSS)은 맞다.
하지만 주입을 말하는 보고에서는 `rendered`만으로 어느 측정인지 읽는 사람이 알 수 없다. 그래서 그 줄이 자기 CSS 측정이라는 말이 있을 때만 통과시킨다.

- 줄 안: 넷째 칸을 `rendered (own css)`로 적는다(괄호 형식이라 원래 받던 형식이다). 또는 그 줄의 다른 칸이 자기 CSS를 읽었다고 말한다.
- 목록 밖 문장: 자기 CSS를 읽었다는 문장(`own css`, `own stylesheet`, `자기 CSS`, `자체 CSS`, `링크/연결(된) CSS … 읽었/로드됐/loaded`)이 그 줄의 검사 이름 첫 낱말(`C1`, `home` 등, 2자 이상)을 담으면 통과.
  그 문장에 부정(`읽지`, `못`, `않`, `막`, `차단`, `not`, `failed`, `blocked`, `= false` 등)이 있으면 허용 문장으로 보지 않는다. 그래서 `linkedCss loaded=false`나 "자기 CSS를 읽지 못했다"는 허용이 아니다.
- 보고 전체에 대한 한 문장("나머지 줄은 자기 CSS")은 받지 않았다. 줄과 문장을 잇는 근거가 없으면 r05 같은 보고가 다시 빠져나간다.

## 돌린 테스트와 결과

- `node --test tests/*.tests.mjs`: 41/41 통과(report-check 23 → 27개).
- `python -B -m unittest discover -s tests`: 142 tests OK (skipped=2).
- 새 테스트(tests/report-check.tests.mjs 끝 네 개):
  - (a) 양성: `--inject`로 넣어 측정(r08 형태), CSS 낱말이 먼 한국어·영어 문장, `style.css를 직접 넣어 쟀다`, 코드 블록 안 `--inject` 명령. 음성: `--inject 없이`, `did not inject the stylesheet`.
  - 음성: CSS 없는 "넣어"(`칸에 200자를 넣어 쟀고`), `테스트 데이터를 주입해`.
  - (b) 양성: 주입 표시 줄과 `rendered`뿐인 줄이 섞인 보고(r05 형태). `rendered`뿐인 줄만 지적하고 문구를 확인.
  - 정당한 섞임 음성: 자기 CSS를 그 검사 이름과 함께 말한 한국어·영어 문장, 줄 안 `rendered (own css)`. 같은 장면의 양성: 다른 검사 이름, 부정 문장.

## 회귀 표

`node evals/check-coverage-20261104/part17/regress.mjs`. 기준은 태그 v1.3.2의 report-check.mjs(`git show`로 OS 임시 폴더에 꺼냄). 원자료: [sets.tsv](sets.tsv), [rule-counts-274.txt](rule-counts-274.txt), [r7-changes.tsv](r7-changes.tsv)(빈 파일 = 바뀐 파일 없음).

| 묶음 | 보고 수 | R7 지적 보고 1.3.2 | R7 지적 보고 1.3.3 | R1~R6 지적 바뀜 |
|---|---|---|---|---|
| 16부 A(1.3.0 팔) | 4 | 2 (r01, r04) | 4 (r01, r04, r05, r08) | 0 |
| 16부 B(1.3.2 팔) | 4 | 0 | 0 | 0 |
| 14부 A(1.3.0 팔) | 16 | 2 (t22, t32) | 2 (t22, t32) | 0 |
| 14부 B(1.3.1 팔) | 16 | 0 | 0 | 0 |
| 15부 도장 보고 중 1.3.2 `text ok` | 42 | 0 | 0 | 0 |
| 기존 evals 보고(14부 files-274) | 274 | 0 | 0 | 0 |

- 274개 규칙별 지적 수는 1.3.2와 같다: `{"R3":269,"R5":44,"R1":75,"R6a":103,"R4":4,"R2":3,"R6b":7}`. R7은 0 → 0.
- 새로 잡힌 줄: r05 10행(AC-002, 남은 `rendered` 줄), r08 4·5행(C1, C2). r08 6행 `rendered (DOM 텍스트)`는 괄호 형식이라 지적하지 않는다.
- 이미 R7이던 보고(r01, r04, t22, t32)는 지적 수가 첫 줄 1건에서 `rendered` 줄 수만큼으로 늘었다. 보고 수는 같다.
- r01 11행 "주입 없이 잰 비교 (link CSS 상태)"도 지적한다. 이 줄은 주입하지 않았지만 CSS가 막힌 측정이라 `rendered`(자기 CSS)도 맞지 않다. `rendered (no css)` 같은 괄호 형식이 맞는 줄로 보고 지적을 맞는 것으로 둔다.

## 확인된 것

- 16부 A의 거짓 `rendered` 4건이 모두 R7에 걸린다(1.3.2 2/4 → 4/4).
- 16부 B 4건, 14부 B 16건, 15부 도장 보고 중 1.3.2 `text ok` 42건에 새 R7 0건. 오탐 0.
- 기존 evals 보고 274개의 R1~R6 지적 수와 각 보고의 R1~R6 지적 위치는 1.3.2와 같다.
- `--verify` 종료 코드 의미는 같다(도장 불일치·누락 1, 지적 있음 1, 일치하고 지적 없음 0). 코드에서 바꾸지 않았다.

## 확인되지 않은 것

- 행동 효과. 이번 과제는 행동 시험(유료 모델 실행)을 하지 않았다. 새 지적 문구가 에이전트 보고를 바꾸는지는 모른다.
- 정당한 섞임의 실물. 274개 중 주입을 말하는 보고는 2개(spot-check/report-check/reports/z15-G.md, design-conformance-20261010/README.md)뿐이고 두 보고 모두 1.3.2·1.3.3에서 R7 지적이 없다.
  자기 CSS 줄과 주입 줄이 섞인 실제 보고는 없어서, 허용 규칙의 오탐 여부는 테스트 문장에만 기댄다.
- 괄호가 있지만 주입을 말하지 않는 줄(`rendered (DOM 텍스트)`, `rendered (zoom 90%)`)은 주입 측정이어도 잡지 않는다. 1.3.2 형식 계약(`rendered (<what differed>)` 허용)을 유지한 결과다.
- CSS 낱말 없이 주입을 말하는 다른 표현(예: "링크 파일 대신 내용을 직접 붙여 넣어 쟀다")은 잡지 않는다.
- 목록 밖 허용 문장은 검사 이름 첫 낱말이 같은 문장에 있는지만 본다. 첫 낱말이 흔한 말(예: `spacing`)이면 다른 줄의 문장에 우연히 맞을 수 있다.

## 게시 때 올릴 버전 핀

부모 세션이 게시 승인 뒤 바꾼다. 이번 커밋은 바꾸지 않았다.

- `skills/joedesign/VERSION`: `1.3.2` → `1.3.3`
- `README.md` 13행(영어 Version 줄)과 138행(한국어 버전 줄): `1.3.2` → `1.3.3`, 1.3.3 요약 문장 앞에 추가
- `docs/INSTALL.md` 38행: `` `1.3.2` `` → `` `1.3.3` ``
- `CHANGELOG.md` 1.3.3 제목의 "게시 전 후보"를 게시 기록으로
- 개인 설치 메타데이터(`agents` 쪽 version)는 1.3.2 게시 때와 같은 방식(part15/install-receipt.md)

## 진행 기록

- 실수 1건: 회귀 준비 중 셸 명령에 남은 `cat > "$TMP/s.mjs"`가 OS 임시 폴더에 빈 파일 하나를 만들었다. 바로 지웠고 저장소·설치에는 영향이 없다.
- 처음 수정은 셸 안 Python 문자열 치환으로 시도했다가 역슬래시 처리 오류로 파일을 쓰기 전에 멈췄다. 이후 직접 편집으로 했다.
