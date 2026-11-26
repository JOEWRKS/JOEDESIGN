#!/bin/sh
# 2.0.2 collector evidence: run from the repository root with two loopback servers already up:
#   python -m http.server 8731 --bind 127.0.0.1 --directory fixtures/capture-cdp
#   python -m http.server 8732 --bind 127.0.0.1   (in ATELIER client/dist: the user's built client, read only)
# No Playwright package is installed in this repository, so capture.mjs falls back to capture-cdp.mjs.
set -x
S=skills/joedesign/scripts
C=evals/v2.0.2-tests-20261126/collector
PROBE='({...window.motion(), chipM: (() => { const r = document.getElementById("chip-m").getBoundingClientRect(); return [r.x, r.y, r.width, r.height]; })()})'
node $S/capture-cdp.mjs --url http://127.0.0.1:8731/ --sizes 1024x768,360x640 --dpr 2 --out $C/fixture --name fixture --probe "$PROBE"
node $S/capture-cdp.mjs --url http://127.0.0.1:8731/ --sizes 360x640 --out $C/fixture --name fixture-reduce-emulate --reduce-motion emulate --probe "$PROBE"
node $S/capture-cdp.mjs --url http://127.0.0.1:8731/ --sizes 360x640 --out $C/fixture --name fixture-reduce-inject --reduce-motion inject --probe "$PROBE"
node $S/capture.mjs < $C/request.json
node $S/capture-cdp.mjs --url http://127.0.0.1:8732/ --sizes 1024x768,360x640 --out $C/atelier-dist --name atelier-dist --settle 1500 --probe '({title: document.title, text: document.body.innerText.slice(0, 120), sheets: document.styleSheets.length})'
# chip M: the probe gives its CSS box [96, 114.875, 72, 44]; at DPR 2 that is 192,230,144,88 in capture pixels; the region stays 8 px inside the border
node $S/sample-pixels.mjs $C/fixture/fixture-360x640@2x-full.png --region 200,236,128,76 --expect '#8A8A8A'
node $S/sample-pixels.mjs $C/fixture/fixture-1024x768@2x-full.png --region 200,236,128,76 --expect '#8A8A8A'
node $S/capture-cdp.mjs --url https://example.com/ --sizes 360x640 --out $C/refused --name refused
