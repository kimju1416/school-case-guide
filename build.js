// research/*.json 을 모아 template.html 에 넣어 docs/index.html 을 만든다.
// 사용: node build.js
const fs = require('fs'), path = require('path');
const R = path.join(__dirname, 'research');
const cfg = require('./config.js');

const read = f => JSON.parse(fs.readFileSync(path.join(R, f), 'utf8'));
const skip = new Set(['contacts.json', 'sources.json']);
const files = fs.readdirSync(R).filter(f => f.endsWith('.json') && !skip.has(f));
const cases = [];
const problems = [];
for (const f of files) {
  let c;
  try { c = read(f); } catch (e) { problems.push(`${f}: JSON 오류 ${e.message}`); continue; }
  for (const k of ['id', 'title', 'category', 'urgency', 'summary']) if (!c[k]) problems.push(`${f}: ${k} 없음`);
  if (!cfg.categories.includes(c.category)) problems.push(`${f}: 분류 «${c.category}» 목록에 없음`);
  if (!['즉시', '당일', '며칠 안'].includes(c.urgency)) problems.push(`${f}: 긴급도 «${c.urgency}»`);
  const old = (c.sources || []).filter(s => s.year && +s.year < 2021);
  if (old.length) problems.push(`${f}: 5년 넘은 출처 ${old.map(s => s.title + '(' + s.year + ')').join(', ')}`);
  if (cfg.patch[c.id]) Object.assign(c, cfg.patch[c.id]);
  c.related = cfg.related[c.id] || c.related || [];
  cases.push(c);
}
cases.sort((a, b) => (cfg.order.indexOf(a.id) + 1 || 999) - (cfg.order.indexOf(b.id) + 1 || 999));
const ids = new Set(cases.map(c => c.id));
for (const q of cfg.quick) if (!ids.has(q.id)) problems.push(`빠른 찾기 «${q.label}» → 없는 사안 ${q.id}`);

let contacts = [], sources = [];
if (fs.existsSync(path.join(R, 'contacts.json'))) contacts = read('contacts.json');
if (fs.existsSync(path.join(R, 'sources.json'))) sources = read('sources.json');
contacts = contacts.map(x => Object.assign({}, x, cfg.contactGroup(x)));

const data = { updated: cfg.updated, cases, contacts, sources, quick: cfg.quick.filter(q => ids.has(q.id)), roleGroups: cfg.roleGroups };
const json = JSON.stringify(data).replace(/</g, '\\u003c');
const tpl = fs.readFileSync(path.join(__dirname, 'template.html'), 'utf8');
const out = tpl.replace('/*__DATA__*/null', () => json);
fs.mkdirSync(path.join(__dirname, 'docs'), { recursive: true });
fs.writeFileSync(path.join(__dirname, 'docs', 'index.html'), out);
console.log(`사안 ${cases.length}건 · 연락처 ${contacts.length} · 출처 ${sources.length} · ${Math.round(out.length / 1024)}KB`);
if (problems.length) { console.log('확인할 것:\n- ' + problems.join('\n- ')); process.exitCode = 1; }
