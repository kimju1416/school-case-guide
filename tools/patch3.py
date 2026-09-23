p='template.html';s=open(p,encoding='utf-8',newline='').read()
def rep(a,b):
    global s
    assert a in s, a[:70]
    s=s.replace(a,b,1)
# 숫자는 «다른 조건을 그대로 둔 채 이걸 누르면 몇 건»으로. 0건은 못 누르게.
rep("  const cnt = (key, v) => v === '전체' ? CASES.length : CASES.filter(c => key === 'role' ? roleMatch(c, v) : c[key] === v).length;",
"""  const cnt = (key, v, sk) => { const t = Object.assign({}, state, { q: state.q, [sk]: v }); return CASES.filter(c => score(c, t.q) > 0 && (t.cat === '전체' || c.category === t.cat) && (t.urg === '전체' || c.urgency === t.urg) && roleMatch(c, t.role)).length; };""")
rep("""<button data-f="${sk}" data-v="${esc(v)}" class="${state[sk] === v ? 'on' : ''}"><span>${dot && v !== '전체' ? `<i class="dot d-${u1(v)}"></i>` : ''}${esc(v)}</span><span class="n num">${cnt(key, v)}</span></button>""",
"""${(() => { const n = cnt(key, v, sk); return `<button data-f="${sk}" data-v="${esc(v)}" class="${state[sk] === v ? 'on' : ''}" ${n || state[sk] === v ? '' : 'disabled'}><span>${dot && v !== '전체' ? `<i class="dot d-${u1(v)}"></i>` : ''}${esc(v)}</span><span class="n num">${n}</span></button>`; })()}""")
# 내 역할: 거의 모든 사안이 걸려 거르는 힘이 없어 뺀다
rep("      ${roles.length > 1 ? grp('내 역할', 'role', roles, 'role') : ''}\n","      ${state.cat !== '전체' || state.urg !== '전체' ? `<button class=\"reset\" id=\"freset\">조건 지우기</button>` : ''}\n")
rep("  $app.querySelectorAll('[data-f]').forEach(b => b.addEventListener('click', () => { state[b.dataset.f] = b.dataset.v; renderHome(); }));",
"""  $app.querySelectorAll('[data-f]').forEach(b => b.addEventListener('click', () => { state[b.dataset.f] = b.dataset.v; renderHome(); }));
  const fr = document.getElementById('freset'); if (fr) fr.addEventListener('click', () => { state.cat = '전체'; state.urg = '전체'; state.role = '전체'; renderHome(); });""")
# 검색어가 바뀌면 숫자도 다시
rep("  q.addEventListener('input', () => { state.q = q.value.trim(); upd(); drawList(); });",
"""  q.addEventListener('input', () => { state.q = q.value.trim(); upd(); drawList(); refreshCounts(); });""")
rep("function drawList(){","""function refreshCounts(){
  $app.querySelectorAll('.side [data-f]').forEach(b => {
    const sk = b.dataset.f, v = b.dataset.v;
    const t = Object.assign({}, state, { [sk]: v });
    const n = CASES.filter(c => score(c, t.q) > 0 && (t.cat === '전체' || c.category === t.cat) && (t.urg === '전체' || c.urgency === t.urg) && roleMatch(c, t.role)).length;
    b.querySelector('.n').textContent = n; b.disabled = !n && state[sk] !== v;
  });
}
function drawList(){""")
rep("  if (!arr.length){ el.innerHTML = `<div class=\"empty\">맞는 사안이 없습니다. 더 짧은 낱말로 찾아보세요. 예: 폭력, 학대, 사고, 교권</div>`; return; }",
"  if (!arr.length){ el.innerHTML = `<div class=\"empty\">맞는 사안이 없습니다. ${state.cat !== '전체' || state.urg !== '전체' ? '왼쪽 조건을 지우거나 ' : ''}더 짧은 낱말로 찾아보세요. 예: 폭력, 학대, 사고, 교권</div>`; return; }")
css = """.side button[disabled]{opacity:.38;cursor:default}
.side button[disabled]:hover{background:none}
.side .reset{display:block;width:auto;margin:0 0 0 10px;padding:6px 0;min-height:36px;border:0;background:none;color:var(--pt);font-size:13.5px;font-weight:700;cursor:pointer;box-shadow:none}
.side .reset:hover{background:none;text-decoration:underline}
"""
rep(".dot{display:inline-block;", css + ".dot{display:inline-block;")
open(p,'w',encoding='utf-8',newline='').write(s)
print('patched')
