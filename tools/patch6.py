import urllib.parse
p='template.html';s=open(p,encoding='utf-8',newline='').read()
def rep(a,b):
    global s
    assert a in s, a[:70]
    s=s.replace(a,b,1)
LOGO='''<svg width="{w}" height="{h}" viewBox="0 0 40 44" fill="none" aria-hidden="true"><path d="M20 2.5 35 8v12.2c0 10.2-6.3 17.6-15 21.3C11.3 37.8 5 30.4 5 20.2V8z" fill="#2456A6"/><path d="M20 2.5 35 8v12.2c0 10.2-6.3 17.6-15 21.3z" fill="#1C4487"/><path d="M13 13.5h7.5a4 4 0 0 1 0 8H17a4 4 0 0 0 0 8h1" stroke="#fff" stroke-width="2" stroke-linecap="round" opacity=".55"/><circle cx="12.6" cy="13.5" r="2.7" fill="#F28B74"/><path d="m19.5 29.5 3 3 6.5-7.5" stroke="#fff" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'''
old_brand = s[s.index('    <svg width="36" height="36" viewBox="0 0 32 32" aria-hidden="true">'):]
old_brand = old_brand[:old_brand.index('</svg>')+6]
rep(old_brand, '    ' + LOGO.format(w=34, h=37))
rep('<span><b><span class="hide-s">학교 </span>사안 처리 길잡이</b>', '<span><b><span class="hide-s">학교 </span>사안 처리 <em>길잡이</em></b>')
rep('.brand b{display:block;font-size:18px;font-weight:800;letter-spacing:-.02em;line-height:1.2;white-space:nowrap}',
    '.brand b{display:block;font-size:18px;font-weight:800;letter-spacing:-.03em;line-height:1.2;white-space:nowrap}\n.brand b em{font-style:normal;color:var(--pt)}')
# 파비콘
fav = LOGO.format(w=40, h=44).replace(' aria-hidden="true"', ' xmlns="http://www.w3.org/2000/svg"')
old_fav = s[s.index('<link rel="icon" href="data:image/svg+xml,'):]
old_fav = old_fav[:old_fav.index('">')+2]
rep(old_fav, '<link rel="icon" href="data:image/svg+xml,' + urllib.parse.quote(fav, safe=' =:/"-.,') .replace('"', "'") + '">')
# 머리글 뒤로 본문이 비치지 않게
rep('.bar{position:sticky;top:0;z-index:30;background:rgba(255,255,255,.97);border-bottom:1px solid var(--line)}',
    '.bar{position:sticky;top:0;z-index:30;background:#fff;border-bottom:1px solid var(--line)}')
rep("  .brand svg{width:30px;height:30px}", "  .brand svg{width:28px;height:31px}")
open(p,'w',encoding='utf-8',newline='').write(s)
open('tools/logo.svg','w',encoding='utf-8').write(LOGO.format(w=40,h=44).replace(' aria-hidden="true"',' xmlns="http://www.w3.org/2000/svg"'))
print('patched')
