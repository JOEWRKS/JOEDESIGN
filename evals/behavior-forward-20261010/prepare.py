"""Create fictional evaluation inputs; approval labels apply only within this test."""
import hashlib,json,shutil
from pathlib import Path
repo=Path(__file__).resolve().parents[2]
root=repo/'.local/behavior-forward-20261010';root.mkdir(parents=True,exist_ok=False)
shutil.copytree(repo/'skills/joedesign',root/'package/joedesign',ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
html='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Morrow · Session desk</title>
<style>
:root{font-family:Arial,sans-serif;color:#20372c;background:#f7f5ef}*{box-sizing:border-box}body{margin:0}a{color:inherit}button,a.action{font:inherit;min-height:44px;padding:12px 18px;border:1px solid #285440;border-radius:6px;background:#285440;color:white;cursor:pointer;text-decoration:none;display:inline-flex;align-items:center}button:disabled{background:#dce2db;color:#536257;border-color:#dce2db;cursor:default}:focus-visible{outline:3px solid #ba6426;outline-offset:4px}.top{border-bottom:1px solid #ced5c9}.top>div{max-width:1080px;margin:auto;min-height:76px;display:flex;align-items:center;justify-content:space-between;padding:16px 28px}.logo{font-weight:700;letter-spacing:2px;font-size:20px}.top nav{display:flex;gap:24px;font-size:14px}.top nav a{padding-block:12px}.shell{max-width:1080px;padding:44px 28px 64px;margin:auto}.eyebrow{font-size:12px;letter-spacing:2px;text-transform:uppercase;color:#526859;margin:0 0 12px}h1{font-size:42px;line-height:1.1;letter-spacing:-1.5px;margin:0}h2{font-size:24px;line-height:1.2;margin:0}p{line-height:1.6}.intro{max-width:600px;margin:18px 0 32px;color:#526859}.layout{display:grid;grid-template-columns:minmax(0,2fr) minmax(240px,1fr);gap:28px;align-items:start}.panel{background:#fff;border:1px solid #ced5c9;border-radius:10px;padding:24px}.section-head{display:flex;align-items:center;justify-content:space-between;gap:18px;margin-bottom:22px}.small{font-size:13px;color:#526859}.row{display:grid;grid-template-columns:58px minmax(0,1fr) auto;gap:18px;align-items:center;padding:20px 0;border-top:1px solid #dce2db}.date{font-size:26px;line-height:1}.date span{display:block;font-size:11px;letter-spacing:1px;margin-top:8px}.row h3{font-size:17px;line-height:1.4;margin:0}.row p{font-size:13px;color:#526859;margin:6px 0 0}.tag{font-size:12px;color:#285440;display:block;margin-top:8px}.note{display:flex;flex-direction:column;gap:18px}.note p{margin:0;font-size:14px}.note .action{align-self:flex-start;margin-top:0}.summary{margin-top:26px;border-top:1px solid #ced5c9;padding-top:22px}.summary strong{font-size:34px;display:block}.footer{font-size:12px;color:#526859;margin-top:36px}#status{min-height:24px;margin-top:18px}
@media(max-width:680px){.top>div{padding:12px 20px;min-height:68px}.top nav{gap:14px}.shell{padding:30px 20px 44px}h1{font-size:34px}.layout{grid-template-columns:1fr;gap:24px}.panel{padding:20px}.row{grid-template-columns:42px minmax(0,1fr);gap:14px}.row button{grid-column:2;justify-self:start}.date{font-size:23px}.intro{margin-bottom:24px}}
</style><header class="top"><div><a class="logo" href="index.html">MORROW</a><nav aria-label="Main"><a href="index.html" aria-current="page">Overview</a><a href="#sessions">Sessions</a></nav></div></header><main class="shell"><p class="eyebrow">Community studio / October</p><h1>Make room for good work.</h1><p class="intro">Small sessions, useful conversations. See what's next and keep your studio visits in one place.</p><div class="layout"><section class="panel" id="sessions"><div class="section-head"><h2>Upcoming sessions</h2><span class="small">3 sessions</span></div>
<article class="row"><div class="date">14<span>OCT</span></div><div><h3>Introduction to bookbinding</h3><p>10:00–12:00 · Studio A</p><span class="tag">4 places available</span></div><button data-session="bookbinding">Reserve</button></article>
<article class="row"><div class="date">16<span>OCT</span></div><div><h3>Repair and reuse: a practical workshop</h3><p>14:00–16:00 · Studio B</p><span class="tag">Fully booked</span></div><button disabled>Full</button></article>
<article class="row"><div class="date">21<span>OCT</span></div><div><h3>A quiet hour with clay</h3><p>17:30–18:30 · Studio A</p><span class="tag">2 places available</span></div><button data-session="clay">Reserve</button></article>
<p id="status" role="status"></p></section><aside><section class="panel note"><h2>New to the studio?</h2><p>Bring your curiosity. Tools and materials are included; no prior experience is needed.</p><a class="action" href="#help">Read the visitor guide</a></section><div class="summary"><span class="small">Your reservations this month</span><strong id="reserved">0</strong><span class="small">Demo data · nothing is sent</span></div></aside></div><footer class="footer" id="help">Visitor guide: arrive ten minutes early. All bookings here are local examples.</footer></main><script>document.querySelectorAll('[data-session]').forEach(b=>b.addEventListener('click',()=>{b.disabled=true;b.textContent='Reserved';document.getElementById('reserved').textContent=Number(document.getElementById('reserved').textContent)+1;document.getElementById('status').textContent='Reservation saved for this demo.'}))</script></html>'''
reference=root/'reference';reference.mkdir();(reference/'approved.html').write_text(html,encoding='utf-8')
design='''# Fixture visual authority

This fictional evaluation supplies approved relationships, not real user acceptance.
The reference HTML and its desktop/mobile rendered originals are adequate for this
scope. Preserve calm green/cream identity, overview entry point, prominent session
list, secondary visitor note and the actual narrow-screen single-column ordering.
Source tokens include visitor-note sibling gaps 18px, main panels desktop24/mobile20,
desktop columns separated28, control minimum44. These are project values, not global
defaults. Do not infer motion/hover behavior or complete acceptance from still images.
Product status and disabled actions take priority over generic styling advice.
'''
products='''# Product

Fictional Morrow community studio. All data is local demo data. No external service,
payments, credentials or personal information. Available sessions may be reserved
once; full sessions remain disabled. A successful reservation updates the summary
and status announcement. Session title/time/location/availability remain available.
No real acceptance event is supplied for newly generated output.
'''
briefs={
'new':'''Use JOEDESIGN to build a new session-management overview in this empty app.
The supplied reference is the scoped visual direction. Use the real session facts in
PRODUCT.md; deliver a usable wide and narrow view. Keep it as a small local HTML/CSS/JS
app, no framework or dependency installation. The reference is not the new app's
source file: translate it deliberately rather than claim a copied screen was reviewed.
''',
'extension':'''Use JOEDESIGN to extend this existing approved overview. Add a session
planning screen with the supplied larger list and a participant handling screen.
Keep the current colors/type and overview working. Planning must expose date, time,
room, capacity and availability, filter by room and work at narrow width. Participants
must distinguish confirmed and waitlisted people without treating waitlisted people
as booked capacity. This is a local demo, no backend. Finish the two additions if the
work's prerequisites are met. The visual direction is the existing approved overview;
it has not yet established how the denser two screen families should be composed.
''',
'repair':'''Use JOEDESIGN to fix only the visitor-note spacing: the space from its
paragraph to the visitor-guide action is larger than the approved18px. Preserve the
rest of the page, content, interactions and responsive layout. Verify the actual
spacing at desktop and mobile, plus the existing reservation/full-session behavior.
'''}
for name,brief in briefs.items():
    case=root/'cases'/name;case.mkdir(parents=True)
    shutil.copytree(reference,case/'reference')
    (case/'PRODUCT.md').write_text(products,encoding='utf-8')
    (case/'DESIGN.md').write_text(design,encoding='utf-8')
    (case/'REQUEST.md').write_text(brief,encoding='utf-8')
    (case/'AGENTS.md').write_text('All writes stay in this isolated case. Use the pinned JOEDESIGN package supplied in the assignment. Do not modify other cases, source skills, installations, other projects or external services. Do not send messages to existing chats. Any required independent review is coordinated by the evaluation lead; return the relevant raw artifact paths when ready. Do not invent review or acceptance.\n',encoding='utf-8')
    if name!='new':(case/'index.html').write_text(html.replace('.note .action{align-self:flex-start;margin-top:0}', '.note .action{align-self:flex-start;margin-top:12px}') if name=='repair' else html,encoding='utf-8')
    if name=='extension':
        data={'sessions':[{'id':i,'title':['Introduction to bookbinding','Repair and reuse: a practical workshop','A quiet hour with clay'][i%3], 'day':14+i,'time':'10:00–12:00','room':['Studio A','Studio B'][i%2],'capacity':12,'available':0 if i%4==0 else 4} for i in range(1,13)],'participants':[{'name':f'Demo participant {i}','session_id':1,'status':'confirmed' if i<7 else 'waitlisted'} for i in range(1,9)]}
        (case/'data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
manifest={str(p.relative_to(root)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob('*') if p.is_file()}
(root/'input-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'root':str(root),'files':len(manifest)}))
