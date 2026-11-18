# 미리보기·측정 도구

`node tools/measure.mjs`는 헤드리스 Chrome으로 `file://` 페이지를 열고, 주어진 화면 크기에서 JS 식을 계산해 JSON 한 줄을 출력한다. 환경 제공물이므로 고치지 않는다. 사용법은 파일 머리 주석.

- `--before`로 상태를 만든 뒤(예: 텍스트 입력과 `input` 이벤트) `--eval`로 값을 읽는다.
- `--screenshot out.png`로 캡처를 남길 수 있다.
