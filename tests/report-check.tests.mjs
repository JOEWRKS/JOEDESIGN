// node --test tests/report-check.tests.mjs : the report form check reads text only; these cases pin what it flags.
import test from 'node:test';
import assert from 'node:assert/strict';
import { check } from '../skills/joedesign/scripts/report-check.mjs';

const LINE = 'spacing S1 | 918/918 | 12 sizes x 6 states, light | rendered | 1440x900 bubble to chips: check 16 / observed 8';
const rules = (text) => check(text).map((f) => f[1]);

test('a bare pass outside the list is flagged, with the missing parts named', () => {
  const f = check(`요청하신 대로 바꿨고 검사도 통과합니다.\n\n- ${LINE}\n`);
  assert.equal(f.length, 1);
  assert.equal(f[0][1], 'R3');
  assert.match(f[0][3], /sizes x states, rendered or code, spot check outcome/);
});

test('a pass with scope, mode and spot check outcome in the same sentence is not flagged', () => {
  assert.deepEqual(rules(`간격 검사는 918/918입니다(12 sizes x 6 states, rendered; spot check differs: check 16 / observed 8).\n\n- ${LINE}\n`), []);
  assert.deepEqual(rules(`spacing passed 918/918 (12 sizes x 6 states, rendered; not spot-checked).\n\n- ${LINE}\n`), []);
});

test('a pointer to the list is not the spot check outcome', () => {
  assert.deepEqual(rules(`검사 결과 간격 위반은 없습니다(12개 크기×9개 상태, 렌더 측정, 표본 대조 결과는 아래 결과 목록).\n\n- ${LINE}\n`), ['R3']);
});

test('technical checks, plans, conditions and denials are not outcome claims', () => {
  const text = [
    'tsc 통과, 단위 테스트 87개 통과·1개 건너뜀입니다.',
    '브라우저가 있는 세션에서 잘림 0건을 확인하겠습니다.',
    '검사는 숨은 요소를 재지 않아서 통과로 나옵니다.',
    'The overflow check did not pass on two sizes.',
    '',
    `- ${LINE}`,
    '',
  ].join('\n');
  assert.deepEqual(rules(text), []);
});

test('a report without a results list is flagged once', () => {
  const f = check('카드 간격을 16px로 키웠습니다. 커밋은 하지 않았습니다.\n');
  assert.deepEqual(f.map((x) => x[1]), ['R1']);
});

test('a result row with fewer than five cells is flagged once', () => {
  const text = '| 쌓기 간격 | 150/150 | 12크기 × 6상태 | 대조 안 함 |\n| 카드 안 | 314/314 | 12크기 × 6상태 | 대조 안 함 |\n';
  const f = check(text);
  assert.deepEqual(f.map((x) => x[1]), ['R1', 'R1']);
  assert.ok(f.some((x) => /fewer than five cells/.test(x[3])));
});

test('a fix line takes fixed or changed, and fixed needs an observation', () => {
  assert.deepEqual(rules(`- ${LINE}\n- 잘림 수정 | resolved | 375x667 | rendered | 캡처 확인\n`), ['R2']);
  assert.deepEqual(rules(`- ${LINE}\n- 잘림 수정 | fixed | 375x667 | rendered | not spot-checked\n`), ['R2']);
  assert.deepEqual(rules(`- ${LINE}\n- 잘림 수정 | fixed | 375x667 | rendered | 375x667 replay bubble: clipped 14 before / 0 after, capture\n`), []);
  assert.deepEqual(rules(`- ${LINE}\n- 잘림 수정 | changed | 375x667 | rendered | not spot-checked\n`), []);
  assert.deepEqual(rules(`- ${LINE}\n- 수정 전 CSS에 같은 검사 | 위반 76건 | 모든 CSS 문맥 | code | not spot-checked\n`), []);
});

test('rows inside a code fence count as the list, and a note about this script is not a claim', () => {
  assert.deepEqual(rules('본문입니다.\n\n```\n' + LINE + '\n```\n\n(이 보고는 report-check.mjs로 검사해 통과했습니다.)\n'), []);
});

test('a turn with no design check says so in one line instead of a results list', () => {
  assert.deepEqual(rules('- 작업: 토큰 이름 정리.\n- 해결: 없음.\n\ndesign checks: none ran\n'), []);
  assert.deepEqual(rules('- 작업: 토큰 이름 정리.\n\n디자인 검사: 실행 안 함\n'), []);
  assert.deepEqual(rules('- 작업: 토큰 이름 정리.\n\n디자인 검사: 실행 안 함. 간격은 통과합니다.\n'), ['R3']);
});

test('a changed fix named under 해결 is flagged (R4); under 남은 문제 or with 해결: 없음 it is not', () => {
  const fix = '- 말풍선 잘림 수정 | changed | 2 sizes x 1 state, light | rendered | not spot-checked\n';
  assert.deepEqual(rules(`- 해결: 말풍선 잘림 수정, 캡처로 확인.\n\n${fix}`), ['R4']);
  assert.deepEqual(rules(`- 해결: 없음.\n- 남은 문제: 말풍선 잘림 수정은 확인 전.\n\n${fix}`), []);
  assert.deepEqual(rules(`- 해결: 말풍선 잘림 수정.\n\n- 말풍선 잘림 수정 | fixed | 2 sizes x 1 state, light | rendered | 360x640: 4px before / 0 after, capture\n`), []);
});

test('the ok stamp binds the checked text: verify matches the same text and rejects a changed or unstamped one', async () => {
  const { stamp, splitStamp } = await import('../skills/joedesign/scripts/report-check.mjs');
  const body = `- 해결: 없음.\n\n- ${LINE}\n`;
  const s = stamp(body);
  assert.match(s, /^report-check: ok \d[\d,]* chars [0-9a-f]{8}$/);
  assert.equal(stamp(`${body}\r\n`), s, 'line endings and trailing whitespace do not change the stamp');
  const sent = `${body}${s}\n`;
  assert.equal(splitStamp(sent).stampLine, s);
  assert.equal(stamp(splitStamp(sent).body), s);
  assert.notEqual(stamp(`${body}\n한 줄 더.\n`), s);
  assert.equal(splitStamp(body).stampLine, null);
  assert.deepEqual(rules(sent), [], 'a stamp line at the end is not a claim');
});
