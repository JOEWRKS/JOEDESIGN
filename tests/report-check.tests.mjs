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

const NONE = 'design checks: none ran';

test('R5: a report that moved, overlapped, hid or merged an element needs before/after lines or `display unchanged`', () => {
  assert.deepEqual(rules(`복기 버튼을 상단 바로 옮겼습니다.\n\n${NONE}\n`), ['R5']);
  assert.deepEqual(rules(`I moved the replay buttons into the top bar.\n\n${NONE}\n`), ['R5']);
  assert.deepEqual(rules(`해설 카드를 판 구석에 겹쳐 띄웠습니다.\n\n${NONE}\n`), ['R5']);
  assert.deepEqual(rules(`복기 버튼을 상단 바로 옮겼습니다.\ndisplay unchanged: 같은 버튼·글자, 위치만 바뀜\n\n${NONE}\n`), []);
});

test('R5: matching before/after lines are a design decision; a differing pair needs product decision pending', () => {
  const same = [
    '복기 버튼을 상태 문장 위로 옮겼습니다.', '', '## Display before/after',
    '- before: 복기 버튼 3개 | ◀ 이전 수, 다음 수 ▶, 종료 판으로 | 복기 중 항상 보임',
    '- after: 복기 버튼 3개 | ◀ 이전 수, 다음 수 ▶, 종료 판으로 | 복기 중 항상 보임', '', NONE, '',
  ].join('\n');
  assert.deepEqual(rules(same), []);
  const differ = [
    '복기 버튼을 상단 바로 옮겼습니다.', '', '## Display before/after',
    '- before: 대결줄 수 표시 | 복기 12/40수 | 항상 보임',
    '- after: 대결줄 수 표시 | 복기 중 | 항상 보임', '', NONE, '',
  ].join('\n');
  const f = check(differ);
  assert.deepEqual(f.map((x) => x[1]), ['R5']);
  assert.match(f[0][3], /content or route differs/);
  assert.equal(f[0][0], 5);
  assert.deepEqual(rules(`${differ}\n남은 문제: 대결줄 수 표시 변경은 product decision pending (JOEFLOW 재진입)\n`), []);
  assert.deepEqual(rules(`${differ}\n제품 결정 대기 없음 (위치만 바꿈)\n`), ['R5']);
});

test('R5: an element hidden after the change or shown only after it differs', () => {
  const hidden = '카드를 숨겼습니다.\n\n- before: 직전 수 카드 | 해설 문장 | 항상 보임\n- after: 직전 수 카드 | hidden | 없음\n\n' + NONE + '\n';
  assert.deepEqual(rules(hidden), ['R5']);
  const added = '수 표시를 합쳤습니다.\n\n- before: 대결줄 | 흑 vs 백 | 항상 보임\n- after: 대결줄 | 흑 vs 백 | 항상 보임\n- after: 상단 바 수 번호 | 12 / 40 | 복기 중\n\n' + NONE + '\n';
  const f = check(added);
  assert.deepEqual(f.map((x) => x[1]), ['R5']);
  assert.match(f[0][3], /no before line/);
});

test('R5: a before/after line takes three cells and is not read as a check outcome', () => {
  assert.deepEqual(rules(`- before: 수 표시 12/40\n- after: 수 표시 12/40\n\n${NONE}\n`), ['R5', 'R5']);
  assert.deepEqual(rules(`- before: 수 표시 | 복기 12/40수 | 항상 보임\n- after: 수 표시 | 복기 12/40수 | 항상 보임\n\n${NONE}\n`), []);
});

test('R5: descriptions of existing behavior, CSS and other uses of the words are not a relocation', () => {
  const text = [
    '좁은 화면에서는 기존 RULE-025에 따라 직전 내 수 카드가 숨겨집니다.',
    '`overflow: hidden`은 그대로 두었습니다.',
    '엔진 응답은 합성값으로 바꿔 재현했습니다.',
    '키보드 포커스 이동 순서는 바꾸지 않았습니다.',
    'The move number and the last move card are unchanged.',
    '카드를 옮기지 않았고 숨기지도 않았습니다.',
    '', NONE, '',
  ].join('\n');
  assert.deepEqual(rules(text), []);
});

const SIX = [
  '- 작업: 요청 내용 칸 아래 글자 수 표시',
  '- 업데이트 파일: src/index.html, src/style.css',
  '- 이슈: 없음',
  '- 해결: 없음',
  '- 남은 문제: C2 대조 안 함',
  '- 다음 작업: 사용자 화면 확인',
].join('\n');

test('R6: six lines, then the results list, then explanation is the order; a results line above the six lines is flagged', () => {
  const ordered = `${SIX}\n\ndesign check results:\n- ${LINE}\n\n간격은 목록의 줄을 따른다.\n`;
  assert.deepEqual(rules(ordered), []);
  const listFirst = `design check results:\n- ${LINE}\n\n${SIX}\n`;
  const f = check(listFirst);
  assert.deepEqual(f.map((x) => x[1]), ['R6']);
  assert.equal(f[0][0], 2);
  assert.match(f[0][3], /start on line 4.*open the report/);
  const split = `- 작업: 표시\n- 업데이트 파일: a.css\n\n- ${LINE}\n\n- 이슈: 없음\n- 해결: 없음\n- 남은 문제: 없음\n- 다음 작업: 없음\n`;
  // a list nested inside the six lines (as several 1.3.0 reports did) is tolerated, not flagged
  assert.deepEqual(rules(split), []);
});

test('R6: without the six lines, or with a results line only in a code block or after them, nothing is flagged', () => {
  assert.deepEqual(rules(`design check results:\n- ${LINE}\n\n설명.\n`), []);
  assert.deepEqual(rules(`\`\`\`\n${LINE}\n\`\`\`\n\n${SIX}\n\n- ${LINE}\n`), []);
  // a later 해결: in the explanation does not move the end of the six lines
  assert.deepEqual(rules(`${SIX}\n\n- ${LINE}\n\n상세: 해결: 아래 참고가 아니라 남은 문제로 둔다.\n`), []);
});

const LIST = `design check results:\n- ${LINE}\n`;

test('R6a: a summary paragraph above the six lines is flagged, with the line and the order', () => {
  const f = check(`글자 수 표시를 구현했습니다. C1은 대조가 달라 남은 문제로 뒀습니다.\n\n${SIX}\n\n${LIST}`);
  assert.deepEqual(f.map((x) => x[1]), ['R6a']);
  assert.equal(f[0][0], 1);
  assert.match(f[0][3], /start on line 3.*one-line title.*open the report/);
  // a title followed by a summary: the summary is flagged
  const g = check(`R1-2 글자 수 표시 보고\n\n요약: C2는 맞고 C1은 대조가 다르다\n\n${SIX}\n\n${LIST}`);
  assert.deepEqual(g.map((x) => [x[0], x[1]]), [[3, 'R6a']]);
  // one long or sentence-ending line is not a title
  assert.deepEqual(rules(`글자 수 표시를 구현했다\n\n${SIX}\n\n${LIST}`), ['R6a']);
});

test('R6b: a paragraph between the six lines and the results list is flagged', () => {
  const f = check(`${SIX}\n\n질문: 글자 수 색을 --muted로 두어도 될까요?\n\n${LIST}`);
  assert.deepEqual(f.map((x) => x[1]), ['R6b']);
  assert.equal(f[0][0], 8);
  assert.match(f[0][3], /ending on line 6.*results list \(line 10\).*open the report/);
  // without the `design check results:` label, the first results line is the list
  assert.deepEqual(rules(`${SIX}\n\n측정은 tools/measure.mjs로 했습니다.\n\n- ${LINE}\n`), ['R6b']);
});

test('R6a/R6b: a title line, headings, labels and indented sub-items are not flagged', () => {
  assert.deepEqual(rules(`# R1-2 글자 수 표시 보고\n\nR1-2 글자 수 표시 — 구현과 C1·C2 측정\n\n${SIX}\n\n${LIST}`), []);
  assert.deepEqual(rules(`**R1-2 보고**\n\n${SIX}\n\n상세 보고\n\n검사 결과:\n- ${LINE}\n\n질문: 색을 바꿀까요?\n`), []);
  const nested = SIX.replace('- 다음 작업: 사용자 화면 확인',
    '- 다음 작업:\n  - 사용자 화면 확인. 소유자 답을 기다린다.\n  - C2 대조\n\n    들여쓴 이어지는 문단도 같은 항목이다.');
  assert.deepEqual(rules(`${nested}\n\n${LIST}\n설명 문단은 목록 뒤에 둔다.\n`), []);
  // a line right below the last item, with no blank line, belongs to that item
  assert.deepEqual(rules(`${SIX}\n이어지는 줄은 같은 항목이다.\n\n${LIST}`), []);
  // `design checks: none ran` stands in for the list; with no list after the six lines R6b has nothing to check
  assert.deepEqual(rules(`${SIX}\n\n설명입니다.\n\ndesign checks: none ran\n`), ['R6b']);
  assert.deepEqual(rules(`- ${LINE}\n\n${SIX}\n\n설명입니다.\n`), ['R6']);
});

const INJ = 'C1 gap | 8/8 | 4 sizes x 2 states, light | rendered (injected css) | not spot-checked';

test('R7: `rendered (injected css)`, `rendered`, `code` and `rendered (<what differed>)` lines are all accepted', () => {
  assert.deepEqual(rules(`- ${INJ}\n`), []);
  assert.deepEqual(rules(`- ${LINE}\n- overflow | 0/8 overflow | 4 sizes x 2 states, light | code | not spot-checked\n`), []);
  assert.deepEqual(rules('- C1 gap | 8/8 | 4 sizes x 2 states, light | rendered (zoom 90%) | not spot-checked\n'), []);
});

test('R7: a report saying CSS was injected needs at least one line marked that way', () => {
  const plain = INJ.replace(' (injected css)', '');
  const ko = `- ${plain}\n\n측정은 미리보기 창이 연결 CSS를 읽지 못해 같은 파일 내용을 주입해 잰 값이다.\n`;
  const f = check(ko);
  assert.deepEqual(f.map((x) => x[1]), ['R7']);
  assert.match(f[0][3], /line 3 says .*rendered \(injected css\)/);
  assert.deepEqual(rules(`- ${plain}\n\nThe preview could not load the stylesheet, so we injected the same CSS.\n`), ['R7']);
  assert.deepEqual(rules(`- ${INJ}\n\n측정은 미리보기 창이 연결 CSS를 읽지 못해 같은 파일 내용을 주입해 잰 값이다.\n`), []);
  // saying nothing was injected, or injecting something else, is not the case
  assert.deepEqual(rules(`- ${plain}\n\nCSS는 주입하지 않고 페이지가 직접 읽었다. 테스트 데이터를 주입했다.\n`), []);
  assert.deepEqual(rules(`- ${plain}\n\nWe did not inject any CSS.\n`), []);
});

test('R7 1.3.3: `--inject`, an inject word anywhere in the sentence, or CSS put in with 넣어 says CSS was injected', () => {
  const plain = INJ.replace(' (injected css)', '');
  // r08 form: the command name alone, no CSS word in the sentence
  assert.deepEqual(rules(`- ${plain}\n\n그래서 같은 파일을 \`--inject\`로 넣어 측정했습니다.\n`), ['R7']);
  // a CSS word far from the inject word, same sentence
  assert.deepEqual(rules(`- ${plain}\n\n측정 도구 설정이 링크된 파일 요청을 막아서, 모든 행은 원래 페이지가 읽으려던 style.css 내용을 그대로 주입했다.\n`), ['R7']);
  assert.deepEqual(rules(`- ${plain}\n\nThe stylesheet request was blocked by the harness config, which is why every value here was injected.\n`), ['R7']);
  assert.deepEqual(rules(`- ${plain}\n\nstyle.css를 직접 넣어 쟀다.\n`), ['R7']);
  // a --inject command shown in a code block
  assert.deepEqual(rules(`- ${plain}\n\n\`\`\`\nnode tools/measure.mjs --inject src/style.css\n\`\`\`\n`), ['R7']);
  // negated forms are not the case
  assert.deepEqual(rules(`- ${plain}\n\n이번에는 --inject 없이 쟀다. We did not inject the stylesheet.\n`), []);
});

test('R7 1.3.3: 넣어 without CSS, or injecting something else, is not CSS injection', () => {
  const plain = INJ.replace(' (injected css)', '');
  assert.deepEqual(rules(`- ${plain}\n\n값은 스크립트로 칸에 200자를 넣어 쟀고 input 이벤트를 보냈다.\n`), []);
  assert.deepEqual(rules(`- ${plain}\n\n상태는 테스트 데이터를 주입해 만들었다.\n`), []);
});

test('R7 1.3.3: with injection said, each bare `rendered` line is flagged even when another line is marked (r05 form)', () => {
  const plain = 'AC-002 text | 3/3 | 4 sizes x 3 states, light | rendered | not spot-checked';
  const text = `- ${INJ}\n- ${plain}\n\n모든 측정은 도구가 링크 CSS를 막아서 style.css를 주입한 상태로 했다.\n`;
  const f = check(text);
  assert.deepEqual(f.map((x) => [x[0], x[1], x[2]]), [[2, 'R7', 'AC-002 text']]);
  assert.match(f[0][3], /line 4 says .*says only `rendered`.*rendered \(injected css\).*rendered \(own css\)/);
});

test('R7 1.3.3: a legitimate mix of own-CSS and injected lines passes when the own-CSS line says so', () => {
  const home = 'home spacing | 8/8 | 4 sizes x 2 states, light | rendered | 1280x800: check 16 / observed 16';
  const prose = '설정 페이지는 미리보기가 링크 CSS를 막아 style.css를 주입해 쟀다.';
  // stated in prose for that check
  assert.deepEqual(rules(`- ${INJ}\n- ${home}\n\n${prose} home 페이지는 자기 CSS를 읽었다.\n`), []);
  assert.deepEqual(rules(`- ${INJ}\n- ${home}\n\n${prose} The home page loaded its own CSS.\n`), []);
  // stated in the line itself
  assert.deepEqual(rules(`- ${INJ}\n- ${home.replace('| rendered |', '| rendered (own css) |')}\n\n${prose}\n`), []);
  // a statement for another check, or a negated one, does not cover the line
  assert.deepEqual(rules(`- ${INJ}\n- ${home}\n\n${prose} settings 페이지는 자기 CSS를 읽지 못했다.\n`), ['R7']);
  assert.deepEqual(rules(`- ${INJ}\n- ${home}\n\n${prose} about 페이지는 자기 CSS를 읽었다.\n`), ['R7']);
});

test('R7 1.3.4: a clause naming the line\'s page (not only its check id) covers a bare `rendered` line', () => {
  const idx = 'C1 상자 간격, 요청 화면 | 8/8 | 4 sizes x 2 states, light | rendered | 320 빈 칸: check 4 / observed 9';
  const cf = 'C1 상자 간격, 확인 화면 | 8/8 | 4 sizes x 2 states, light | rendered (injected css) | 320 빈 칸: check 4 / observed 9';
  const prose = '확인 화면은 도구가 링크 CSS를 막아 같은 style.css를 주입해 쟀다.';
  // part18 r01 form: the page is named, the check id is not
  assert.deepEqual(rules(`- ${idx}\n- ${cf}\n\n${prose} 요청 화면은 자기 링크 CSS를 읽었다(loaded=true).\n`), []);
  // parenthesis form of the page name
  assert.deepEqual(rules(`- ${idx.replace(', 요청 화면', ' (요청 화면)')}\n- ${cf}\n\n${prose} 요청 화면은 자기 링크 CSS를 읽었다.\n`), []);
  // a clause about the other page, naming the check id, does not cover this line (part18 r02 form)
  assert.deepEqual(rules(`- ${idx}\n- ${cf}\n\n${prose} 확인 화면을 자체 CSS로 여는 방법이 생기면 C1·C2를 확인 화면에서 다시 잰다.\n`), ['R7']);
  // no own-CSS statement at all
  assert.deepEqual(rules(`- ${idx}\n- ${cf}\n\n${prose}\n`), ['R7']);
});

test('R7 1.3.4: negation is read by word form; 마지막 and `not spot-checked` are not negation', () => {
  const idx = 'C2 overflow (요청 화면) | 8/8 | 4 sizes x 2 states, light | rendered | 320x800: 마지막 잉크 열 303';
  const ac = 'AC-002 글자 수 (요청 화면) | 3/3 | 1 size x 3 states, light | rendered | not spot-checked';
  const prose = '확인 화면은 링크 CSS가 막혀 style.css를 주입해 쟀다.';
  // part18 r04 form: the own-CSS clause carries 마지막 and not spot-checked
  assert.deepEqual(rules(`- ${idx}\n- ${ac}\n\n${prose} C2·AC-002 요청 화면은 own css로 쟀고 캡처 마지막 잉크 열은 303이며 AC-002는 not spot-checked다.\n`), []);
  // real negation still cancels the clause
  assert.deepEqual(rules(`- ${idx}\n\n${prose} C2 요청 화면은 자기 CSS를 읽지 못했다.\n`), ['R7']);
  assert.deepEqual(rules(`- ${idx}\n\n${prose} C2 요청 화면의 자기 CSS는 막혀 있었다.\n`), ['R7']);
  assert.deepEqual(rules(`- ${idx}\n\n${prose} The 요청 화면 did not load its own CSS.\n`), ['R7']);
});

test('R7 1.3.4: clauses split at commas, semicolons and slashes, so one sentence can cover one page and inject the other', () => {
  const idx = 'C1 요청 화면 | 8/8 | 4 sizes x 2 states, light | rendered | 320x800: check 4 / observed 9';
  const cf = 'C1 확인 화면 | 8/8 | 4 sizes x 2 states, light | rendered (injected css) | 320x800: check 4 / observed 9';
  // part18 r03 form
  assert.deepEqual(rules(`- ${idx}\n- ${cf}\n\nC1은 두 화면 모두 4px였다(16/16, rendered: 요청 화면 own css, 확인 화면 injected css, 도구가 확인 화면 링크 CSS를 막아 주입했다).\n`), []);
  // part18 r02 form: a parenthesis stays with its clause
  assert.deepEqual(rules(`- ${idx}\n- ${cf}\n\nC1은 통과로 볼 수 없다(4 sizes x 2 states, rendered (own css) 요청 화면 / rendered (injected css) 확인 화면, spot check differs: check 4 / observed 9, 도구가 CSS를 막아 주입함).\n`), []);
  // the own-CSS clause names only the other page
  assert.deepEqual(rules(`- ${idx}\n- ${cf}\n\nC1은 두 화면 모두 4px였다(rendered: 확인 화면 own css, 도구가 요청 화면 링크 CSS를 막아 주입했다).\n`), ['R7']);
});
