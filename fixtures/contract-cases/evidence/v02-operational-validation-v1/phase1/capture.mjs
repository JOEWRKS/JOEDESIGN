import { chromium } from "file:///C:/Users/tjdwo/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs"
import path from "node:path"

const output = path.dirname(new URL(import.meta.url).pathname).replace(/^\/([A-Z]:)/i, "$1")
const browser = await chromium.launch({
  executablePath: "C:/Users/tjdwo/.cache/puppeteer/chrome/win64-152.0.7977.75/chrome-win64/chrome.exe",
  headless: true,
})
const prefix = process.argv[2] ?? "final"
const errors = []
try {
  for (const [name, width, height] of [["desktop", 1440, 900], ["mobile", 390, 844]]) {
    const page = await browser.newPage({ viewport: { width, height }, deviceScaleFactor: 1 })
    page.on("pageerror", error => errors.push(error.message))
    await page.goto("http://127.0.0.1:8547/#/", { waitUntil: "networkidle" })
    await page.evaluate(async () => {
      await document.fonts.ready
      await Promise.all(Array.from(document.querySelectorAll("[data-home-signature] img"), image => image.decode().catch(() => {})))
    })
    for (const [scene, progress] of [["kf01", 0], ["kf02", 0.5], ["kf03", 0.95]]) {
      await page.evaluate(progress => {
        const story = document.querySelector("[data-home-signature]")
        window.scrollTo({ top: story.offsetTop + (story.offsetHeight - window.innerHeight) * progress, behavior: "instant" })
      }, progress)
      await page.waitForFunction(({ progress }) => Math.abs(Number(document.querySelector("[data-home-signature]").style.getPropertyValue("--signature-progress")) - progress) < 0.01, { progress })
      await page.screenshot({ path: path.join(decodeURIComponent(output), `${prefix}-${scene}-${name}-${width}x${height}.png`) })
      console.log(JSON.stringify(await page.evaluate(({ scene, name }) => ({
        scene, viewport: name, scrollY, phase: document.querySelector("[data-home-signature]").dataset.signaturePhase,
        overflow: document.documentElement.scrollWidth > innerWidth,
        font: document.fonts.check('16px "Instrument Sans"'),
        titles: Array.from(document.querySelectorAll("[data-home-signature] h1, [data-home-signature] h2"), element => ({
          text: element.textContent, rect: element.getBoundingClientRect().toJSON(), font: getComputedStyle(element).fontSize,
        })),
      }), { scene, name })))
    }
    await page.close()
  }
  console.log(JSON.stringify({ errors }))
} finally {
  await browser.close()
}
