const { chromium } = require('C:/Users/USER/Downloads/gb-edu-map/tools/node_modules/playwright-core');
(async () => {
  const b = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
  for (const w of [1440, 375]) {
    const p = await b.newPage({ viewport: { width: w, height: 900 } });
    await p.goto('http://localhost:5731/#/'); await p.waitForTimeout(800);
    const n = await p.locator('.side button').count();
    for (let i = 0; i < n; i++) {
      const bt = p.locator('.side button').nth(i);
      const label = (await bt.innerText()).replace(/\s+/g, ' ');
      await bt.click(); await p.waitForTimeout(150);
      const rows = await p.locator('#list tbody tr').count();
      const want = +(label.match(/(\d+)$/) || [0, -1])[1];
      console.log(w, label.padEnd(22), '보임', rows, rows === want ? '' : '  ← 다름');
      // 다른 필터 초기화
      await p.goto('http://localhost:5731/#/x'); await p.goto('http://localhost:5731/#/'); await p.evaluate(() => location.reload()); await p.waitForTimeout(600);
    }
  }
  await b.close();
})();
