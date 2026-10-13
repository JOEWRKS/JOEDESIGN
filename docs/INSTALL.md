# 설치·업데이트·복구

설치 단위는 `skills/joedesign/` 전체다. 스킬 ID는 `joedesign`, 실행 요청은
`$joedesign`이다. 버전 원본은 [VERSION](../skills/joedesign/VERSION)이다.
1.0.0으로 올려도 기존 JSON schema/contract 버전이나 예전 증거의 의미는 바뀌지 않는다.

## 처음 설치

[README의 PowerShell 명령](../README.md#3-바로-시작하기)은 Windows의
`$CODEX_HOME/skills/joedesign`에 복사한다. CODEX_HOME을 지정하지 않았다면
`%USERPROFILE%/.codex/skills/joedesign`이다. 저장소 폴더에서 실행하며 기존
`joedesign` 또는 `joedesign-harness`가 있으면 덮어쓰지 않고 중단한다.

비공개 저장소는 접근 권한과 GitHub 로그인이 필요하다. `git clone`이 인증 오류로
실패하면 Git Credential Manager의 GitHub 로그인을 연결한다. 2단계 인증은
GitHub 화면에서 직접 완료한다. 토큰을 채팅이나 저장소 파일에 넣지 않는다.

설치 뒤 Codex의 새 대화에서 `$joedesign`을 사용한다. 다른 운영체제에서도 같은
전체 폴더를 해당 Codex 스킬 경로에 복사할 수 있으나 위 명령은 Windows 전용이다.
프로젝트별 설치는 해당 호스트가 실제로 검색하는 경로를 확인한 뒤 사용한다.
동일한 이름의 여러 설치본 중 어느 것이 활성화됐는지 추측하지 않는다.

## 설치 확인과 필요한 도구

설치 폴더의 `scripts/harness_cli.py`를 **절대 경로로** 실행한다.

```text
python -B <설치폴더>/scripts/harness_cli.py version
python -B <설치폴더>/scripts/harness_cli.py doctor
```

- `version`: `1.0.0`과 실제 운영지침 경로를 확인한다.
- `doctor`: 발견된 스킬 경로와 누락된 전문 스킬을 확인한다. 준비가 부족하면
  종료코드 2가 정상적인 진단 결과다. 폴더 생성만으로 이를 PASS 처리하지 않는다.
- 기본 전문 검수에는 `impeccable`, `ui-ux-pro-max`, `web-design-guidelines`가 필요하다.
  모션·React 성능 검수가 필요한 작업은 해당 전문 스킬도 준비한다. 실제 제공처의
  설치 방법을 사용하며 이름만 같은 가짜 파일로 누락을 메우지 않는다.
- 진단기는 패키지 형제 폴더, 사용자 `.codex/skills`, `.agents/skills`를 찾는다.
  사용자 지정 경로만 점검하려면 `doctor --skills-root <스킬들상위폴더>`를 쓴다.
  AVAILABLE은 발견 결과이지 실제 전문 스킬 호출·검수 완료가 아니다.
- 자동 실행에는 기존 Codex 실행기와 Python 3가 필요하다. 브라우저 수집에는 기존
  Node, Playwright 패키지와 브라우저 경로가 추가로 필요하다. Python 표준 라이브러리만
  쓰는 진단 CLI에 pip 설치는 필요 없다. [실행 설정](../skills/joedesign/references/execution.md).
  검증 환경은 [1.0.0 검증 기록](../evals/v1-release-candidate-20261013/README.md)에 남긴다.

## 기존 설치 업데이트

Git 저장소 갱신과 설치 폴더 갱신은 서로 다른 작업이다. 먼저 새 패키지의
버전·파일 해시와 실제 활성 설치 경로를 확인한다. 다음 요청을 담당 에이전트에 전달할 수 있다.

```text
이 JOEDESIGN 저장소의 검증된 패키지로 내 설치를 업데이트해줘.
실제로 검색되는 설치 경로와 현재 버전부터 확인해.
기존 joedesign, 남아 있다면 구 joedesign-harness를 전부 파일 목록과 해시로 기록하고
스킬 검색 경로 밖에 백업해. 백업의 전체 파일 해시가 맞는지 먼저 확인해.
검토한 패키지 전체와 최종 설치가 일치하도록 바꾸고 version/doctor를 실행해.
설정·다른 스킬·제품 파일은 보존하고, 실패 시 검증한 백업으로 원복해.
바뀐 파일과 미확인 의존성, 복구 경로를 보고해.
```

백업 예시는 사용자 문서 폴더의 `JOEDESIGN-backups/<날짜와고유이름>/`이다.
이 폴더가 실제 스킬 검색 대상이 아닌지 먼저 확인한다. `.codex/skills` 아래에
옛 패키지를 이름만 바꿔 남기면 중복 발견될 수 있으므로 백업 장소로 쓰지 않는다.
기존 생성 캐시·사용자 추가 파일도 먼저 보존하며 임의로 일괄 삭제하지 않는다.
복사 중 실패하거나 입력이 달라지면 멈추고, 고정한 백업과 전후 목록으로 복구한다.

구형 두 패키지에서 넘어올 때는 `joedesign-harness`가 별도 공개 진입점으로 남지
않도록 한다. 현재는 `joedesign` 하나가 운영을 맡고 내부 하네스를 포함한다.
이미 이전한 설치라면 과거 이전 작업을 다시 실행하지 않는다.

## 복구와 이전 실행 자료

1. 새 실행을 멈추고 변경 전 백업의 전체 파일 해시를 검증한다.
2. 실패한 현재 설치도 별도 보존한다. 사용자 추가 변경은 자동 덮어쓰지 않는다.
3. 업데이트 전 기록한 경로로 백업을 복원하고 전체 해시와 `version`을 대조한다.
4. 기존 설정·다른 스킬·제품 파일이 보존됐는지 확인하고 새 대화에서 시작한다.

CLI와 캡처 경로는 `joedesign/scripts/` 아래다. 구 runtime JSON의 외부 `skills.J`
재정의는 제거하고 같은 패키지 내부 코어를 사용한다. 이전 두 패키지의 실행을 새
정책으로 재개하지 않는다. 예전 기준·receipt·캡처는 보존하고 새 작업 후보를 준비한다.
과거 검증 자료를 1.0.0의 새 행동 증거로 다시 표시하지 않는다.

[예전 설치 전환 기록](../evals/design-conformance-20261010/operational.md) ·
[F05 백업·복구 검증](../evals/f05-impact-20261013/COMPLETION.md)
