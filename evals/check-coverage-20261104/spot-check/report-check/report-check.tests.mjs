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
