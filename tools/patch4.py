p='template.html';s=open(p,encoding='utf-8',newline='').read()
def rep(a,b):
    global s
    assert a in s, a[:70]
    s=s.replace(a,b,1)
URL='https://kimju1416.github.io/school-case-guide/'
# OG·트위터 카드
rep('''<meta property="og:type" content="website">''','''<meta property="og:type" content="website">
<meta property="og:url" content="'''+URL+'''">
<meta property="og:site_name" content="학교 사안 처리 길잡이">
<meta property="og:locale" content="ko_KR">
<meta property="og:image" content="'''+URL+'''og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="학교 사안 처리 길잡이 — 학교폭력·아동학대·교육활동 침해·위기·안전사고 21가지 사안의 처리 흐름">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="학교 사안 처리 길잡이">
<meta name="twitter:description" content="사안이 터졌을 때 지금 할 일부터. 조사·심의·불복까지 법령·교육부 매뉴얼 원문 기준 업무 흐름도.">
<meta name="twitter:image" content="'''+URL+'''og.png">
<link rel="canonical" href="'''+URL+'''">''')
rep('''<meta property="og:description" content="사안이 터졌을 때 지금 할 일부터. 법령·교육부 매뉴얼 원문 기준 업무 흐름도.">''','''<meta property="og:description" content="사안이 터졌을 때 지금 할 일부터. 조사·심의·불복까지 법령·교육부 매뉴얼 원문 기준 업무 흐름도.">''')
# 푸터: 인스타
rep("document.getElementById('foot').innerHTML = `법령·교육부 매뉴얼 원문을 요약한 참고 자료입니다. 최종 판단은 원문과 소속 교육청 안내를 따르세요. · 기준일 ${esc(DATA.updated)} · <a href=\"#/about\">출처와 안내</a>`;",
"document.getElementById('foot').innerHTML = `<div class=\"fr\"><div>법령·교육부 매뉴얼 원문을 요약한 참고 자료입니다. 최종 판단은 원문과 소속 교육청 안내를 따르세요.<br>기준일 ${esc(DATA.updated)} · <a href=\"#/about\">출처와 안내</a></div><a class=\"insta\" href=\"https://www.instagram.com/kimju.zip/\" target=\"_blank\" rel=\"noopener\"><svg width=\"18\" height=\"18\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\" aria-hidden=\"true\"><rect x=\"3\" y=\"3\" width=\"18\" height=\"18\" rx=\"5\"/><circle cx=\"12\" cy=\"12\" r=\"4.2\"/><circle cx=\"17.3\" cy=\"6.7\" r=\"1\" fill=\"currentColor\" stroke=\"none\"/></svg>@kimju.zip</a></div>`;")
rep(".foot{border-top:1px solid var(--line);color:var(--sub);font-size:13px;padding:22px 0 44px;background:var(--card)}",
".foot{border-top:1px solid var(--line);color:var(--sub);font-size:13px;padding:22px 0 44px;background:var(--card)}\n.foot .fr{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap}\n.foot .insta{display:inline-flex;align-items:center;gap:7px;color:var(--tx);font-weight:700;font-size:14px;text-decoration:none;border:1px solid var(--line);border-radius:999px;padding:8px 14px;min-height:40px}\n.foot .insta:hover{border-color:var(--pt);color:var(--pt)}")
open(p,'w',encoding='utf-8',newline='').write(s)
print('patched')
