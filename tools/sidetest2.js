const { chromium } = require('C:/Users/USER/Downloads/gb-edu-map/tools/node_modules/playwright-core');
(async () => {
  const b = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
  const p = await b.newPage({ viewport: { width: 1440, height: 900 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('http://localhost:5731/#/'); await p.waitForTimeout(800);
  let bad = 0;
  // 모든 조합: 분류 하나 누르고 → 긴급도 하나씩(누를 수 있는 것만)
  const cats = await p.locator('.side [data-f="cat"]').count();
  for (let i = 0; i < cats; i++) {
    await p.locator('.side [data-f="cat"]').nth(i).click();
    const urgs = await p.locator('.side [data-f="urg"]').count();
    for (let j = 0; j < urgs; j++) {
      const u = p.locator('.side [data-f="urg"]').nth(j);
      if (await u.isDisabled()) continue;
      const want = +(await u.locator('.n').innerText());
      await u.click();
      const rows = await p.locator('#list tbody tr').count();
      if (rows !== want || rows === 0) { bad++; console.log('틀림', i, j, want, rows); }
    }
    await p.locator('.side [data-f="urg"]').first().click();
  }
  await p.locator('.side [data-f="cat"]').nth(1).click();
  console.log('조건 지우기 단추', await p.locator('#freset').count());
  await p.locator('#freset').click();
  console.log('지운 뒤', await p.locator('#list tbody tr').count(), '건 · 오류', bad, errs.join('|') || '없음');
  await b.close();
})();
