// Static fixture collector only. No geometry calls or screenshots in this pass.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {createRequire} from 'node:module';
const require=createRequire(import.meta.url);
const request=JSON.parse(fs.readFileSync(0,'utf8'));
const {chromium}=require(process.env.JOEDESIGN_PLAYWRIGHT_MODULE);
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const browser=await chromium.launch({headless:true,executablePath:process.env.JOEDESIGN_BROWSER_EXECUTABLE});
try {
  const rows=[];
  for(const target of request.baseline.targets){
    const context=await browser.newContext({viewport:{width:target.viewport[0],height:target.viewport[1]},locale:target.locale,colorScheme:target.theme});
    const page=await context.newPage();const pending=[];const resources=[];const failures=[];
    page.on('requestfailed',r=>failures.push(r.url()));
    page.on('response',response=>pending.push((async()=>{
      const url=new URL(response.url());
      if(url.origin!==new URL(request.base_url).origin)throw Error('Unexpected external resource');
      const relative=url.pathname==='/'?'index.html':decodeURIComponent(url.pathname.slice(1));
      const file=path.resolve(request.project,relative);
      if(!file.startsWith(path.resolve(request.project)+path.sep))throw Error('Resource outside fixture');
      const bytes=await response.body();
      if(!response.ok())throw Error('Unsuccessful resource');
      resources.push({path:relative,sha256:hash(fs.readFileSync(file)),response_sha256:hash(bytes),url:response.url(),status:response.status()});
    })()));
    await page.goto(request.base_url+target.route,{waitUntil:'networkidle'});
    await page.locator('#page').waitFor({state:'visible'});
    await Promise.all(pending);
    if(failures.length)throw Error('Request failure '+failures.join(','));
    if(resources.length!==1||resources[0].path!=='index.html')throw Error('Fixture resource set changed');
    // This fixture is a single document with inline CSS, no JS, images, fonts,
    // network calls, state transitions or lazy assets. No general coverage claim.
    rows.push({target,build_id:request.build_id,dependencies_complete:true,resources,limitations:[]});
    await context.close();
  }
  process.stdout.write(JSON.stringify({schema:'joedesign.served-build.v1',scope_id:request.baseline.scope_id,
    baseline_sha256:request.baseline_sha256,targets:rows,collector:{kind:'actual-playwright-response-bytes',geometry_reads:0,screenshots:0,
      scope:'Single static inline-CSS document only; no dynamic dependency coverage claim'}}));
}finally{await browser.close();}
