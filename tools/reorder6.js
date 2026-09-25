const fs = require('fs');
const P = id => 'research/' + id + '.json';
const load = id => JSON.parse(fs.readFileSync(P(id), 'utf8'));
const save = (id, c) => fs.writeFileSync(P(id), JSON.stringify(c, null, 2) + '\n');
const find = (c, what) => { const i = c.steps.findIndex(s => s.what === what); if (i < 0) throw new Error('없음: ' + what); return i; };
function move(c, what, afterWhat) { const i = find(c, what); const [s] = c.steps.splice(i, 1); const j = find(c, afterWhat); c.steps.splice(j + 1, 0, s); }
const log = [];
let c;
// 교사 아동학대 피소: 직위해제 제한(수사 중)을 경찰 진술 뒤로
c = load('teacher-abuse-accusation'); move(c, '직위해제 제한', '피의자(또는 피신고자) 진술'); c.steps[find(c, '직위해제 제한')].stage = '조사·확인'; save('teacher-abuse-accusation', c); log.push('teacher-abuse-accusation: 직위해제 제한 → 경찰 진술 뒤, 조사·확인');
// 장기결석
c = load('absence-unknown');
c.steps[find(c, '경찰 수사 의뢰')].stage = '조사·확인';
c.steps[find(c, '읍·면·동장·교육장 통보')].stage = '조치·이행';
move(c, '과태료', '복귀 보고(3일 이내)'); save('absence-unknown', c); log.push('absence-unknown: 수사 의뢰 조사·확인, 통보 조치·이행, 과태료 → 복귀 보고 뒤');
// 가출·실종
c = load('runaway-missing'); move(c, '장기실종 관리', '경찰 협조와 학생 주변 정보'); save('runaway-missing', c); log.push('runaway-missing: 장기실종 관리 → 경찰 협조 뒤');
// 자살 위기
c = load('suicide-risk'); c.steps[find(c, '직접 묻고 위험도 가리기')].stage = '초기 대응'; save('suicide-risk', c); log.push('suicide-risk: 위험도 가리기 초기 대응');
// 학생 사망
c = load('student-death');
c.steps[find(c, '정확한 사건 정보 수집')].stage = '초기 대응';
c.steps[find(c, '유가족 협의')].stage = '초기 대응';
c.steps[find(c, '고위기 학생 선별과 특별상담실')].stage = '조치·이행';
save('student-death', c); log.push('student-death: 정보 수집·유가족 협의 초기 대응, 선별 조치·이행');
// 학교폭력: 자체해결 심의 단계에 비학생 가해 사안 체크
c = load('school-violence');
const k = c.steps.findIndex(s => /자체해결/.test(s.what) && /심의|부의/.test(s.what));
const s = c.steps[k]; s.check = s.check || [];
const add = '가해자가 학생이 아닌 사안은 자체해결 대상이 아니다 — 심의위원회 개최 요청(피해 측이 보호조치를 원하지 않으면 미개최 동의서 양식 3-7로 보고)';
if (!s.check.includes(add)) s.check.push(add);
save('school-violence', c); log.push('school-violence: «' + s.what + '» 놓치기 쉬움에 비학생 가해 사안 추가');
console.log(log.join('\n'));
