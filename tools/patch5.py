p='template.html';s=open(p,encoding='utf-8',newline='').read()
def rep(a,b):
    global s
    assert a in s, a[:70]
    s=s.replace(a,b,1)
old_start = s.index('  <section class="top"><div class="wrap">')
old_end = s.index('  </div></section>', old_start) + len('  </div></section>')
new = '''  <section class="top hero">
    <img class="hero-img" src="hero.jpg" alt="" aria-hidden="true" width="1800" height="1013" fetchpriority="high">
    <div class="wrap">
      <div class="hero-t">
        <p class="eyebrow">학교폭력 · 아동학대 · 교육활동 침해 · 위기 · 안전사고</p>
        <h1>사안이 생겼을 때,<br>지금 할 일부터</h1>
        <p class="lead2">신고부터 조사·심의·조치·불복·종결까지. 법령과 교육부 매뉴얼 원문을 바탕으로 누가, 언제, 무엇을 하는지 흐름도로 정리했습니다.</p>
        <div class="search">
          <label for="q">검색</label>
          <input id="q" type="search" autocomplete="off" enterkeyhint="search" placeholder="무슨 일인가요? 예: 때렸어요, 자해, 멍, 몰래 녹음" value="${esc(state.q)}">
          <button class="clr" id="clr" aria-label="검색어 지우기">×</button>
        </div>
        <div class="stats">
          <div class="stat"><b class="num">${CASES.length}</b><span>사안</span></div>
          <div class="stat u"><b class="num">${CASES.filter(c => c.urgency === '즉시').length}</b><span>즉시 대응</span></div>
          <div class="stat"><b class="num">${totalSteps}</b><span>처리 단계</span></div>
          <div class="stat"><b class="num">${totalLaw}</b><span>근거 법령</span></div>
        </div>
      </div>
    </div>
  </section>
  <section class="quickbar"><div class="wrap">
    <div class="quick"><span class="ql">이럴 때</span>${QUICK.filter(x => BYID[x.id]).map(x => `<button data-go="${x.id}">${esc(x.label)}</button>`).join('')}</div>
  </div></section>'''
s = s[:old_start] + new + s[old_end:]
css = '''
/* 첫 화면 머리 그림 */
.hero{position:relative;overflow:hidden;background:#F3F6FB;border-bottom:1px solid var(--line)}
.hero-img{position:absolute;right:max(-60px, calc((100vw - 1240px) / 2 - 140px));top:50%;transform:translateY(-50%);height:118%;width:auto;max-width:none;pointer-events:none;user-select:none}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,#F3F6FB 0%,#F3F6FB 34%,rgba(243,246,251,.85) 46%,rgba(243,246,251,0) 62%);pointer-events:none}
.hero .wrap{position:relative;z-index:1;padding-top:44px;padding-bottom:40px}
.hero-t{max-width:560px}
.eyebrow{margin:0 0 10px;font-size:13px;font-weight:700;color:var(--pt);letter-spacing:.01em}
.hero h1{margin:0 0 12px;font-size:40px;line-height:1.22;letter-spacing:-.035em;font-weight:800}
.lead2{margin:0 0 22px;color:var(--tx2);font-size:15.5px;max-width:520px}
.hero .search{flex:none}
.hero .search input{background:#fff;box-shadow:0 1px 3px rgba(15,23,42,.06)}
.hero .stats{margin-top:18px;gap:30px}
.quickbar{background:var(--card);border-bottom:1px solid var(--line)}
.quickbar .quick{margin:0;padding:12px 0}
@media (max-width:1080px){
  .hero::after{background:linear-gradient(90deg,#F3F6FB 0%,#F3F6FB 45%,rgba(243,246,251,.8) 60%,rgba(243,246,251,.2) 80%)}
}
@media (max-width:860px){
  .hero-img{position:static;transform:none;display:block;width:100%;height:auto;margin:0 auto;object-fit:cover;object-position:70% 50%;aspect-ratio:16/8}
  .hero::after{display:none}
  .hero .wrap{padding-top:18px;padding-bottom:22px}
  .hero h1{font-size:28px}
  .lead2{font-size:15px;margin-bottom:16px}
  .hero .stats{justify-content:space-between;gap:10px}
}
'''
rep("\n/* 홈 본문 */", css + "\n/* 홈 본문 */")
open(p,'w',encoding='utf-8',newline='').write(s)
print('patched')
