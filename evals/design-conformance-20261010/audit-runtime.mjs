// Corroborate the explicit dependency map with actual response bytes; no auto-baseline.
import fs from 'node:fs';
import path from 'node:path';
import {createRequire} from 'node:module';
import {createHash} from 'node:crypto';
const require=createRequire(import.meta.url), input=JSON.parse(fs.readFileSync(0,'utf8'));
const {chromium}=require(input.playwright_module);
const browser=await chromium.launch({headless:true,executablePath:input.executable});
const result=[];
try {
  for (const target of input.targets) {
    const context=await browser.newContext({viewport:{width:target.viewport[0],height:target.viewport[1]},locale:target.locale});
    const page=await context.newPage(), rows=[],pending=[];
    page.on('response', response=>pending.push((async()=>{
      const url=new URL(response.url());
      let row={url:url.href,status:response.status()};
      try {
        if(url.origin!==new URL(input.base_url).origin)throw Error('External dependency');
        let rel=decodeURIComponent(url.pathname).replace(/^\//,'');
        if(rel.endsWith('/'))rel+='index.html';
        row.input=input.prefix+rel;
        const local=path.resolve(input.project,row.input);
        if(!local.startsWith(path.resolve(input.project)+path.sep))throw Error('Escaped root');
        row.sha256=createHash('sha256').update(await response.body()).digest('hex');
        row.file_sha256=createHash('sha256').update(fs.readFileSync(local)).digest('hex');
        row.covered=input.checks.filter(c=>c.target_id===target.id).every(c=>c.inputs.includes(row.input));
        row.valid=row.status===200&&row.sha256===row.file_sha256&&row.covered;
      }catch(e){row.error=String(e);row.valid=false;}
      rows.push(row);
    })()));
    await page.goto(new URL(target.route,input.base_url).href,{waitUntil:'networkidle'});
    await page.evaluate(()=>document.fonts.ready);
    await page.locator('#main').waitFor();
    // Trigger below-fold lazy images without relying on viewport-only requests.
    await page.evaluate(()=>document.querySelectorAll('img[loading=lazy]').forEach(x=>x.loading='eager'));
    await page.waitForLoadState('networkidle');
    await Promise.all(pending);
    result.push({target_id:target.id,resources:rows,valid:rows.length>0&&rows.every(r=>r.valid)});
    await context.close();
  }
}finally{await browser.close();}
process.stdout.write(JSON.stringify(result,null,2));
