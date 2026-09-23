const { chromium } = require('C:/Users/USER/Downloads/gb-edu-map/tools/node_modules/playwright-core');
(async () => {
  const b = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
  const p = await b.newPage({ viewport: { width: 1200, height: 630 } });
  await p.goto('http://localhost:5731/og-src.html'); await p.waitForTimeout(1500);
  await p.evaluate(() => document.fonts.ready);
  await p.screenshot({ path: 'docs/og.jpg', type: 'jpeg', quality: 88 });
  await b.close();
})();
