p='template.html';s=open(p,encoding='utf-8',newline='').read()
def rep(a,b):
    global s
    assert a in s, a[:70]
    s=s.replace(a,b,1)
rep(".node .nt{display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}",".node .nt{display:block}\n.node .nx{display:block;margin-top:4px;font-size:11.5px;font-weight:600;color:var(--sub)}")
css=r'''
.how{margin:8px 0 0;padding:0;list-style:none;counter-reset:h}
.how li{counter-increment:h;position:relative;padding:3px 0 3px 26px;font-size:14.5px;color:var(--tx2)}
.how li::before{content:counter(h);position:absolute;left:0;top:5px;width:18px;height:18px;border-radius:5px;background:var(--pt-soft);color:var(--pt);font-size:11.5px;font-weight:800;display:flex;align-items:center;justify-content:center}
.xrow{display:flex;gap:8px;margin-top:10px;font-size:13.5px;align-items:flex-start}
.xrow b{flex:none;font-size:12px;font-weight:800;color:var(--sub);padding-top:2px;min-width:44px}
.xrow.sc{background:var(--head);border:1px solid var(--line2);border-radius:var(--r1);padding:9px 12px}
.xrow.sc span{color:var(--tx)}
.xrow.ck span{color:var(--warn)}
.tip{position:fixed;z-index:60;max-width:380px;background:#1B2A41;color:#fff;border-radius:10px;padding:12px 14px;font-size:13.5px;line-height:1.55;pointer-events:none;opacity:0;transition:opacity .12s;box-shadow:0 8px 24px rgba(15,23,42,.25);left:-999px;top:0}
.tip.on{opacity:1}
.tip b{display:block;font-size:14px;margin-bottom:4px}
.tip .tw{color:#AFC2DD;font-size:12px;margin-bottom:6px}
.tip ol{margin:6px 0 0;padding-left:18px;color:#DCE5F2}
.tip .more{margin-top:6px;color:#AFC2DD;font-size:12px}
.drawer-bg{position:fixed;inset:0;background:rgba(15,23,42,.35);z-index:70;opacity:0;pointer-events:none;transition:opacity .18s}
.drawer-bg.on{opacity:1;pointer-events:auto}
.drawer{position:fixed;top:0;right:0;bottom:0;width:min(520px,100%);background:var(--card);z-index:71;transform:translateX(102%);transition:transform .22s ease;display:flex;flex-direction:column;box-shadow:-8px 0 30px rgba(15,23,42,.18);visibility:hidden}
.drawer.on{transform:none;visibility:visible}
.drawer .dh{display:flex;align-items:center;gap:8px;padding:10px 12px 10px 18px;border-bottom:1px solid var(--line)}
.drawer .dh .k{font-size:12.5px;font-weight:800;color:var(--sub)}
.drawer .dh .x{margin-left:auto;width:40px;height:40px;border:0;background:none;font-size:26px;cursor:pointer;color:var(--sub);line-height:1}
.drawer .dbody{padding:18px 20px 24px;overflow-y:auto;flex:1;-webkit-overflow-scrolling:touch}
.drawer h3{margin:0 0 8px;font-size:20px;line-height:1.4;letter-spacing:-.01em}
.drawer .det{color:var(--tx2);margin:0 0 6px;font-size:15px}
.drawer dl{margin:16px 0 0;display:grid;grid-template-columns:52px 1fr;gap:6px 10px;font-size:14px;background:var(--head);border-radius:var(--r1);padding:12px 14px}
.drawer dt{color:var(--sub);font-weight:600}
.drawer dd{margin:0}
.drawer .df{display:flex;gap:8px;padding:10px 14px calc(10px + env(safe-area-inset-bottom));border-top:1px solid var(--line);align-items:center}
.drawer .df .chk{margin:0 auto 0 0}
.lbl2{font-size:12.5px;font-weight:800;color:var(--sub);margin:16px 0 2px}
@media (max-width:860px){
  .drawer{top:auto;left:0;width:100%;max-height:88vh;border-radius:16px 16px 0 0;transform:translateY(102%)}
  .drawer.on{transform:none}
}
'''
rep("\n/* 목록형 흐름 */",css+"\n/* 목록형 흐름 */")
rep('''<div class="nt">${esc(x.s.what)}</div></div>''','''<div class="nt">${esc(x.s.what)}</div>${(x.s.how || []).length ? `<span class="nx">하는 법 ${x.s.how.length}가지</span>` : ''}</div>''')
rep("function memoTemplate(){",r'''function stepExtra(s, lbl){
  let h = '';
  if (s.how && s.how.length) h += `${lbl ? '<div class="lbl2">하는 법</div>' : ''}<ol class="how">${s.how.map(x => `<li>${esc(x)}</li>`).join('')}</ol>`;
  if (s.script) h += `<div class="xrow sc"><b>이렇게 말하기</b><span>${esc(s.script)}</span></div>`;
  if (s.check && s.check.length) h += `<div class="xrow ck"><b>놓치기 쉬움</b><span>${s.check.map(esc).join(' · ')}</span></div>`;
  if (s.form) h += `<div class="xrow"><b>서식</b><span>${esc(s.form)}</span></div>`;
  if (s.neis) h += `<div class="xrow"><b>나이스</b><span>${esc(s.neis)}</span></div>`;
  return h;
}
function memoTemplate(){''')
rep('''<h3>${esc(s.what)}</h3>${s.detail ? `<p class="det">${esc(s.detail)}</p>` : ''}
      <label class="chk">''','''<h3>${esc(s.what)}</h3>${s.detail ? `<p class="det">${esc(s.detail)}</p>` : ''}${stepExtra(s, true)}
      <label class="chk">''')
rep('''${s.detail ? `<div class="det">${esc(s.detail)}</div>` : ''}<div class="bs">${esc(s.when || '')}''','''${s.detail ? `<div class="det">${esc(s.detail)}</div>` : ''}${stepExtra(s)}<div class="bs">${esc(s.when || '')}''')
old="$app.querySelectorAll('.node').forEach(n => { const go = () => { const i = +n.dataset.n; flowState.sel = flowState.sel === i ? null : i; paint(); }; n.addEventListener('click', go); n.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); go(); } }); });"
new=r'''$app.querySelectorAll('.node').forEach(n => {
    const i = +n.dataset.n;
    const go = () => { hideTip(); openDrawer(i); };
    n.addEventListener('click', go);
    n.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); go(); } });
    n.addEventListener('mouseenter', () => showTip(n, L[i].s, i));
    n.addEventListener('mouseleave', hideTip);
  });
  function openDrawer(i){
    const x = L[i]; if (!x) return;
    const s = x.s, done = getDone();
    flowState.sel = i; paint();
    const dr = document.getElementById('drawer'), bg = document.getElementById('drawerbg');
    dr.innerHTML = `<div class="dh"><span class="k">S${String(i + 1).padStart(2, '0')} · ${esc(PHASES[x.phase].name)} · ${i + 1}/${L.length}</span><button class="x" aria-label="닫기">×</button></div>
      <div class="dbody"><h3>${esc(s.what)}</h3>${s.detail ? `<p class="det">${esc(s.detail)}</p>` : ''}${stepExtra(s, true)}
      <dl><dt>언제</dt><dd>${esc(s.when || '-')}</dd><dt>누가</dt><dd>${esc(s.who || '-')}</dd><dt>근거</dt><dd>${esc(s.basis || '매뉴얼 절차')}</dd></dl></div>
      <div class="df"><label class="chk"><input type="checkbox" id="drchk" ${done[i] ? 'checked' : ''}> 마쳤습니다</label><button class="btn" id="drprev" ${i ? '' : 'disabled'}>← 앞</button><button class="btn dark" id="drnext" ${i < L.length - 1 ? '' : 'disabled'}>다음 →</button></div>`;
    dr.classList.add('on'); bg.classList.add('on');
    const close = () => { dr.classList.remove('on'); bg.classList.remove('on'); flowState.sel = null; paint(); };
    dr.querySelector('.x').onclick = close; bg.onclick = close;
    document.getElementById('drchk').onchange = e => { setDone(i, e.target.checked); };
    document.getElementById('drprev').onclick = () => openDrawer(i - 1);
    document.getElementById('drnext').onclick = () => openDrawer(i + 1);
    dr.querySelector('.dbody').scrollTop = 0;
    document.onkeydown = e => { if (e.key === 'Escape' && dr.classList.contains('on')) close(); };
  }
  flowState.open = openDrawer;'''
rep(old,new)
rep("// 흐름도 화살표: 단계 번호 순서대로 잇는다",r'''// 마우스 말풍선(마우스가 있는 기기만)
const canHover = window.matchMedia('(hover:hover) and (pointer:fine)').matches;
function showTip(el, s, i){
  if (!canHover) return;
  const t = document.getElementById('tip');
  const how = (s.how || []).slice(0, 4);
  t.innerHTML = `<b>S${String(i + 1).padStart(2, '0')} ${esc(s.what)}</b><div class="tw">${esc([s.when, s.who].filter(Boolean).join(' · '))}</div>${s.detail ? esc(s.detail) : ''}${how.length ? `<ol>${how.map(h => `<li>${esc(h)}</li>`).join('')}</ol>` : ''}<div class="more">눌러서 자세히 보기</div>`;
  const r = el.getBoundingClientRect();
  t.classList.add('on');
  const tw = t.offsetWidth, th = t.offsetHeight;
  let x = r.right + 10, y = r.top;
  if (x + tw > innerWidth - 8) x = r.left - tw - 10;
  if (x < 8) x = Math.min(innerWidth - tw - 8, Math.max(8, r.left));
  if (y + th > innerHeight - 8) y = Math.max(8, innerHeight - th - 8);
  t.style.left = x + 'px'; t.style.top = y + 'px';
}
function hideTip(){ const t = document.getElementById('tip'); if (t) t.classList.remove('on'); }
window.addEventListener('scroll', hideTip, { passive: true });
// 흐름도 화살표: 단계 번호 순서대로 잇는다''')
rep('<div class="toast" id="toast" role="status" aria-live="polite"></div>','<div class="toast" id="toast" role="status" aria-live="polite"></div>\n<div class="tip" id="tip" role="tooltip"></div>\n<div class="drawer-bg" id="drawerbg"></div>\n<aside class="drawer" id="drawer" aria-label="단계 자세히"></aside>')
rep("function route(){\n  const h = location.hash || '#/';","function route(){\n  const h = location.hash || '#/';\n  hideTip(); document.getElementById('drawer').classList.remove('on'); document.getElementById('drawerbg').classList.remove('on');")
rep("  .bar,.sos,.dbar,.acts,.toc,.memo,.foot,.step input,.seg,.calc,#s-flow,.chk{display:none!important}","  .bar,.sos,.dbar,.acts,.toc,.memo,.foot,.step input,.seg,.calc,#s-flow,.chk,.tip,.drawer,.drawer-bg{display:none!important}")
rep("단계를 눌러 자세히 보고, 끝낸 일은 체크하세요.","칸에 마우스를 올리면 요약, 누르면 하는 법까지 나옵니다. 끝낸 일은 체크하세요.")
open(p,'w',encoding='utf-8',newline='').write(s)
print('patched')
