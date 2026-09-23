p='template.html';s=open(p,encoding='utf-8',newline='').read()
def rep(a,b):
    global s
    assert a in s, a[:70]
    s=s.replace(a,b,1)
# 표 칸에 머리글 이름 달기(휴대폰에서 카드처럼 쌓을 때 씀)
rep('''${(t.rows || []).map(r => `<tr>${r.map((v, j) => `<td${j === 0 ? ' class="k0"' : ''}>${esc(v)}</td>`).join('')}</tr>`).join('')}''',
    '''${(t.rows || []).map(r => `<tr>${r.map((v, j) => `<td data-h="${esc((t.head || [])[j] || '')}"${j === 0 ? ' class="k0"' : ''}>${esc(v)}</td>`).join('')}</tr>`).join('')}''')
mob=r'''
  .xt table.t{min-width:0}
  .xt table.t thead{display:none}
  .xt table.t tr{display:block;padding:10px 16px;border-top:1px solid var(--line2)}
  .xt table.t tr:first-child{border-top:0}
  .xt table.t td{display:grid;grid-template-columns:92px 1fr;gap:8px;padding:3px 0;border:0;font-size:14px}
  .xt table.t td::before{content:attr(data-h);font-size:12px;font-weight:700;color:var(--sub);padding-top:1px}
  .xt table.t td.k0{white-space:normal;font-size:15px}
  .deep summary{padding:13px 40px 13px 14px;font-size:15px}
  .deep .db{padding:0 16px 14px 16px}
  .now li{font-size:15px}
  .sec h2{font-size:18px}
  .step{padding:12px 14px 12px 8px}
  .how li{font-size:14px}
  .xrow{flex-direction:column;gap:2px}
'''
rep("  table.t td.due{white-space:normal}\n}", "  table.t td.due{white-space:normal}\n"+mob+"}")
open(p,'w',encoding='utf-8',newline='').write(s)
print('patched')
