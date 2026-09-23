import { chromium } from "file:///C:/Users/tjdwo/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs"
import assert from "node:assert/strict"
import { fileURLToPath } from "node:url"
import path from "node:path"
import sharp from "sharp"

const browser = await chromium.launch({ executablePath: "C:/Users/tjdwo/.cache/puppeteer/chrome/win64-152.0.7977.75/chrome-win64/chrome.exe", headless: true })
const output = path.dirname(fileURLToPath(import.meta.url))
async function open(page) {
  await page.goto("http://127.0.0.1:8547/#/", {waitUntil:"networkidle"})
  await page.evaluate(async()=>{await document.fonts.ready;await Promise.all(Array.from(document.querySelectorAll("[data-home-signature] img"),image=>image.decode().catch(()=>{})))})
}
async function scroll(page, progress) {
  await page.evaluate(progress=>{const story=document.querySelector("[data-home-signature]");window.scrollTo({top:story.offsetTop+(story.offsetHeight-innerHeight)*progress,behavior:"instant"})},progress)
  await page.waitForFunction(progress=>Math.abs(Number(document.querySelector("[data-home-signature]").style.getPropertyValue("--signature-progress"))-progress)<0.01,progress)
}
function luminance(rgb) {
  return rgb.map(value=>{value/=255;return value<=0.04045?value/12.92:((value+0.055)/1.055)**2.4}).reduce((sum,value,index)=>sum+value*[0.2126,0.7152,0.0722][index],0)
}
try {
 for(const [name,width,height] of [["desktop",1440,900],["mobile",390,844]]) {
  const page = await browser.newPage({viewport:{width,height},deviceScaleFactor:1})
  await open(page)
  assert.equal(await page.locator(".home-signature__copy[aria-hidden=false]").count(),1)
  await page.locator("[data-search-trigger]").click()
  assert.equal(await page.getByRole("dialog").isVisible(),true)
  await page.keyboard.press("Escape")
  if(name==="mobile") {
   await page.getByRole("button",{name:"Open menu",exact:true}).click()
   assert.equal(await page.locator("#mobile-navigation").isVisible(),true)
   await page.keyboard.press("Escape")
   assert.equal(await page.locator("[data-mobile-menu-trigger]").evaluate(e=>e===document.activeElement),true)
  }else{
   await page.getByRole("button",{name:"Open Science menu",exact:true}).click()
   assert.equal(await page.locator("#mega-navigation").isVisible(),true)
   await page.keyboard.press("Escape")
  }
  await scroll(page,0.5)
  await page.locator(".home-kf02-cta").click()
  await page.waitForURL("**/#/science")
  await open(page)
  await scroll(page,0.95)
  // Check actual background samples beneath approved low-emphasis text.
  for(const selector of [".home-kf03-kicker",".home-kf03-record p:first-child > span",".home-kf03-disclaimer"]){
   const item=page.locator(selector)
   const box=await item.boundingBox()
   const rgba=await item.evaluate(e=>getComputedStyle(e).color.match(/[\d.]+/g).map(Number))
   await item.evaluate(e=>e.style.visibility="hidden")
   const {data,info}=await sharp(await page.screenshot({clip:{x:Math.floor(box.x),y:Math.floor(box.y),width:Math.ceil(box.width),height:Math.ceil(box.height)}})).removeAlpha().raw().toBuffer({resolveWithObject:true})
   await item.evaluate(e=>e.style.visibility="")
   const ratios=[]
   for(let index=0;index<data.length;index+=info.channels*7){const bg=Array.from(data.subarray(index,index+3));if(bg.length<3)continue;const alpha=rgba[3]??1;const fg=rgba.slice(0,3).map((v,c)=>v*alpha+bg[c]*(1-alpha));const l1=luminance(fg),l2=luminance(bg);ratios.push((Math.max(l1,l2)+0.05)/(Math.min(l1,l2)+0.05))}
   console.log(JSON.stringify({viewport:name,selector,sampledContrast:{min:Math.min(...ratios).toFixed(2),max:Math.max(...ratios).toFixed(2)},method:"actual screenshot background with text temporarily hidden; CSS foreground composited over sample"}))
  }
  await scroll(page,0)
  assert.equal(await page.locator("[data-home-signature]").getAttribute("data-signature-phase"),"A")
  assert.equal(await page.locator(".home-kf01-action").first().isVisible(),true)
  assert.equal(await page.locator("[data-signal-to-medicine]").count(),1)
  assert.equal(await page.locator("[data-evidence-field]").count(),1)
  assert.equal(await page.locator("[data-editorial-close]").count(),1)
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false)
  await page.close()
  const reduced=await browser.newPage({viewport:{width,height},deviceScaleFactor:1,reducedMotion:"reduce"})
  await open(reduced)
  assert.equal(await reduced.locator(".home-signature__copy[aria-hidden=false]").count(),3)
  for(const [scene,selector] of [["kf01",".home-kf01-hero"],["kf02",".home-kf02-stage"],["kf03",".home-kf03-stage"]]){
   await reduced.locator(selector).evaluate(e=>e.scrollIntoView({block:"start",behavior:"instant"}))
   await reduced.screenshot({path:path.join(output,`reduced-${scene}-${name}-${width}x${height}.png`)})
  }
  await reduced.close()
  console.log(JSON.stringify({viewport:name,checks:"PASS: search/Escape, navigation/Escape, loop CTA to science, reverse scroll, lower Home retained, no horizontal overflow, reduced-motion three complete scenes"}))
 }
}finally{await browser.close()}
