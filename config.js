// 화면 구성 설정 — 사안 내용은 research/*.json 에 있다.
module.exports = {
  updated: '2026-09-24',
  categories: ['학생 간 사안', '학생 보호·위기', '교원 보호', '안전·보건', '행정·정보'],
  order: [
    'emergency-medical', 'suicide-risk', 'child-abuse', 'school-violence', 'sexual-violence', 'cyber-deepfake',
    'safety-accident', 'runaway-missing', 'teacher-rights', 'teacher-abuse-accusation', 'malicious-complaint',
    'student-guidance', 'student-photo-sns', 'absence-unknown', 'drugs-substance', 'infectious-disease',
    'food-poisoning', 'field-trip-accident', 'fire-earthquake', 'student-death', 'privacy-leak'
  ],
  // 첫 화면 «이럴 때» 단추
  quick: [
    { label: '학생끼리 때렸어요', id: 'school-violence' },
    { label: '자해 흔적·죽고 싶다는 말', id: 'suicide-risk' },
    { label: '아이 몸에 멍·방임 의심', id: 'child-abuse' },
    { label: '쓰러졌어요·경련', id: 'emergency-medical' },
    { label: '수업 중 다쳤어요', id: 'safety-accident' },
    { label: '학부모가 폭언해요', id: 'teacher-rights' },
    { label: '아동학대로 신고당했어요', id: 'teacher-abuse-accusation' },
    { label: '딥페이크·불법촬영', id: 'cyber-deepfake' },
    { label: '성추행을 털어놨어요', id: 'sexual-violence' },
    { label: '며칠째 연락 없이 결석', id: 'absence-unknown' },
    { label: '수업 방해가 심해요', id: 'student-guidance' },
    { label: '성적표를 잘못 보냈어요', id: 'privacy-leak' }
  ],
  // 내 역할 → 단계의 «누가»에 들어 있을 낱말
  roleGroups: {
    '담임·교과 교사': ['담임', '교사', '교원', '알게 된', '목격', '인솔', '교직원'],
    '업무 담당·부장': ['책임교사', '담당', '부장', '전담기구', '생활지도', '보건교사', '상담'],
    '교감·교장': ['교감', '교장', '학교장', '관리자']
  },
  related: {
    'school-violence': ['cyber-deepfake', 'sexual-violence', 'student-guidance'],
    'cyber-deepfake': ['school-violence', 'sexual-violence', 'student-photo-sns'],
    'sexual-violence': ['school-violence', 'cyber-deepfake', 'child-abuse'],
    'child-abuse': ['sexual-violence', 'absence-unknown', 'suicide-risk'],
    'teacher-abuse-accusation': ['teacher-rights', 'student-guidance', 'malicious-complaint'],
    'teacher-rights': ['malicious-complaint', 'teacher-abuse-accusation', 'student-photo-sns'],
    'student-guidance': ['teacher-rights', 'teacher-abuse-accusation'],
    'malicious-complaint': ['teacher-rights', 'teacher-abuse-accusation'],
    'suicide-risk': ['student-death', 'child-abuse', 'emergency-medical'],
    'student-death': ['suicide-risk'],
    'absence-unknown': ['runaway-missing', 'child-abuse'],
    'runaway-missing': ['absence-unknown', 'field-trip-accident', 'suicide-risk'],
    'drugs-substance': ['emergency-medical', 'student-guidance'],
    'safety-accident': ['emergency-medical', 'field-trip-accident'],
    'field-trip-accident': ['safety-accident', 'runaway-missing', 'emergency-medical'],
    'emergency-medical': ['safety-accident', 'suicide-risk'],
    'infectious-disease': ['food-poisoning'],
    'food-poisoning': ['infectious-disease'],
    'fire-earthquake': ['safety-accident', 'emergency-medical'],
    'privacy-leak': ['student-photo-sns'],
    'student-photo-sns': ['teacher-rights', 'cyber-deepfake', 'privacy-leak']
  },
  patch: {},
  contactGroup(x) {
    const s = (x.name || '') + (x.group || '');
    if (/경북|경상북도/.test(s)) return { group: '경상북도' };
    return { group: x.group || '전국 공통' };
  }
};
