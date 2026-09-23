// 사용: node tools/shot.js <hash> <out.png> [w] [h] [full=1] [js]
const { chromium } = require('C:/Users/USER/Downloads/gb-edu-map/tools/node_modules/playwright-core');
(async () => {
  const [hash = '#/', out = 'shot.png', w = 1440, h = 900, full = '1', js] = process.argv.slice(2);
  const b = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
  const p = await b.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 1, isMobile: +w < 600, hasTouch: +w < 600 });
  const logs = [];
  p.on('console', m => { if (m.type() === 'error' || m.type() === 'warning') logs.push(m.type() + ': ' + m.text()); });
  p.on('pageerror', e => logs.push('PAGEERROR: ' + e.message));
  await p.goto('http://localhost:5731/' + hash);
  await p.waitForTimeout(1200);
  if (js && js.startsWith('HOVER:')) { const el = p.locator(js.slice(6)); await el.scrollIntoViewIfNeeded(); await el.hover(); await p.waitForTimeout(400); }
  else if (js) { const r = await p.evaluate(js); if (r !== undefined) console.log('JS→', typeof r === 'string' ? r : JSON.stringify(r)); await p.waitForTimeout(500); }
  await p.screenshot({ path: out, fullPage: full === '1' });
  const ov = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth);
  if (ov > 0) logs.push('가로 넘침 ' + ov + 'px');
  console.log(logs.join('\n') || 'ok');
  await b.close();
})();
