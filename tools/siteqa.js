const { chromium } = require('C:/Users/USER/Downloads/gb-edu-map/tools/node_modules/playwright-core');
const BASE = process.argv[2] || 'https://kimju.kr/guide/';
(async () => {
  const b = await chromium.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe' });
  const issues = [];
  for (const [vw, vh, mob] of [[1440, 900, false], [375, 812, true]]) {
    const p = await b.newPage({ viewport: { width: vw, height: vh }, isMobile: mob, hasTouch: mob });
    const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
    await p.goto(BASE + '?qa=' + Date.now()); await p.waitForTimeout(1500);
    const ids = await p.evaluate(() => [...document.querySelectorAll('[data-go], #list tbody tr')].map(e => e.dataset.go || e.dataset.id).filter(Boolean));
    const cases = await p.evaluate(() => (window.CASES || window.DATA?.cases || []).map(c => c.id));
    const all = 'absence-unknown,child-abuse,cyber-deepfake,drugs-substance,emergency-medical,field-trip-accident,fire-earthquake,food-poisoning,infectious-disease,malicious-complaint,privacy-leak,runaway-missing,safety-accident,school-violence,sexual-violence,student-death,student-guidance,student-photo-sns,suicide-risk,teacher-abuse-accusation,teacher-rights'.split(',');
    if (vw === 1440) console.log('사안 수', all.length);
    for (const id of all) {
      await p.goto(BASE + '#/c/' + id); await p.waitForTimeout(350);
      const r = await p.evaluate(() => {
        const t = document.body.innerText;
        const bad = ['undefined', 'NaN', '[object', 'null'].filter(w => t.includes(w));
        const h1 = document.querySelector('h1')?.innerText || '';
        const secs = [...document.querySelectorAll('section, .sec')].filter(s => s.offsetParent && s.innerText.trim().length < 4).length;
        const ov = document.documentElement.scrollWidth - innerWidth;
        const tels = [...document.querySelectorAll('a[href^="tel:"]')].map(a => a.getAttribute('href')).filter(h => !/^tel:[0-9#*+-]+$/.test(h));
        const nodes = document.querySelectorAll('.node, .step').length;
        return { h1, bad, secs, ov, tels, nodes };
      });
      const tag = `${vw}px ${id}`;
      if (!r.h1) issues.push(`${tag}: 제목 없음`);
      if (r.bad.length) issues.push(`${tag}: 화면에 ${r.bad.join(',')}`);
      if (r.ov > 0) issues.push(`${tag}: 가로 넘침 ${r.ov}px`);
      if (r.tels.length) issues.push(`${tag}: 이상한 전화 링크 ${r.tels.join(' ')}`);
      if (r.nodes < 5) issues.push(`${tag}: 단계 ${r.nodes}개뿐`);
    }
    for (const h of ['#/', '#/contacts', '#/about']) { await p.goto(BASE + h); await p.waitForTimeout(300); const ov = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth); if (ov > 0) issues.push(`${vw}px ${h}: 가로 넘침 ${ov}`); }
    // 검색
    await p.goto(BASE + '#/'); await p.waitForTimeout(400);
    for (const q of ['때렸어요', '자해', '멍', '몰래 녹음', '교권', '식중독', '딥페이크', '가출', '개인정보', '민원']) {
      await p.fill('#q', q); await p.waitForTimeout(150);
      const n = await p.evaluate(() => document.querySelectorAll('#list tbody tr').length);
      if (!n) issues.push(`${vw}px 검색 «${q}» 결과 0`);
    }
    if (errs.length) issues.push(`${vw}px 콘솔 오류: ${[...new Set(errs)].slice(0, 5).join(' | ')}`);
    await p.close();
  }
  console.log(issues.length ? issues.join('\n') : '문제 없음');
  await b.close();
})();
