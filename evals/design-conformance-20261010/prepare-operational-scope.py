"""Prepare a reviewable scope in an isolated product-shaped tree; never edit GEO."""
import argparse
import copy
import json
from pathlib import Path
import shutil
import sys

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO/'skills/joedesign/scripts'))
from harness.io import file_hash, write_artifact
from harness.conformance import load_baseline

p=argparse.ArgumentParser()
p.add_argument('--product',type=Path,required=True)
p.add_argument('--previous-baseline',type=Path,required=True)
p.add_argument('--output',type=Path,required=True)
a=p.parse_args()
out=a.output.resolve();out.mkdir(parents=True,exist_ok=False)
project=out/'project';project.mkdir()
prefix='examples/geo-fresh-market/wireframes/'
common=['commerce-data.mjs','commerce-engine.mjs','foundation/system.css','foundation/views.mjs',
        'foundation/scenes.mjs','design/app.mjs','design/views.mjs','design/interactions.mjs',
        'design/service-ui.mjs','design/visual.css','design/service.css',
        'design/assets/PretendardVariable.woff2','design/assets/sinseon-mart-word.png']
families={'products':['produce-grid-v1.png','design/site/products/index.html'],
          'collections':['design/assets/hero-organic.png','design/assets/hero-seafood.png','design/site/collections/index.html']}
baseline=json.loads(a.previous_baseline.read_text(encoding='utf-8'))
baseline=copy.deepcopy(baseline)
baseline['scope_id']='geo-header-product-campaign-spacing'
baseline['authorization_ref']='User continue request 2026-10-10; narrow spacing scope only, not whole design or user visual acceptance'
files=['DESIGN.md']+sorted({prefix+s for s in common+sum(families.values(),[])})
provenance=[]
for name in files:
    source=a.product/name;dest=project/name;dest.parent.mkdir(parents=True,exist_ok=True)
    h=file_hash(source);shutil.copyfile(source,dest)
    assert file_hash(source)==h==file_hash(dest),'Source changed during copy'
    provenance.append(dict(source=str(source.resolve()),relative=name,sha256=h))
baseline['authority']=[dict(path='DESIGN.md',sha256=file_hash(project/'DESIGN.md'))]
for c in baseline['required_checks']:
    family=c['target_id'].split('-')[0]
    c['inputs']=sorted(prefix+s for s in common+families[family])
relative='.design-harness/conformance/spacing-baseline.json'
write_artifact(project/relative,baseline)
pin=file_hash(project/relative)
load_baseline(project/relative,pin,project)
write_artifact(out/'scope-review.json',dict(baseline=relative,baseline_sha256=pin,provenance=provenance,
    input_counts={k:len(common+v) for k,v in families.items()},
    source_mapping='Unchanged 51 geometric criteria from corrected geo-r2, checked against current DESIGN. Independent review pending.',
    common_reason='Shared HTML rendering, commerce state/data, imported modules, CSS, font and logo affect layout. Whole-file granularity retained.',
    family_reason='Only that family built entry HTML and displayed images. Other routes, boards, builds scripts and old screenshots excluded.',
    non_file_context='Fresh session, target viewport/theme/locale, local static server rooted at wireframes; request config and browser observation retained separately.',
    coverage='Header total height/narrow vertical spacing, product card spacing, campaign card spacing only. Not all DESIGN/header rules.',
    excluded='Header desktop centering/navigation/control sizing, page spacing, other states/routes, optical quality and user acceptance remain outside this scope.'))
print(json.dumps(dict(project=str(project),baseline_sha256=pin,inputs={k:len(common+v) for k,v in families.items()})))
