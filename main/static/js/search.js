var searchData = [
    '게이트1',
    '게이트2',
    '전공강의실 1',
    '전공강의실 2',
    '전공강의실 3',
    '전공강의실 4',
    '캡스톤 디자인 랩 1',
    '전공강의실 5',
    '정독실',
    '삼성소프트웨어 부전공 프로젝트실',
    '학생회실',
    '엠시스',
    'CGAC',
    '오피스룸',
    '샘마루',
    '큐빅',
    '네스트넷',
    'PDA',
    '노바',
    '관리실',
    '캡스톤 디자인 랩3',
    '실습 준비실',
    '서버실',
    '캡스톤 디자인 랩4',
    'PC 실습실1',
    'PC 실습실2',
    '세마니실 I',
    '창고',
    '지역선도대학 육성사업 사무실',
    '주영관 교수',
    '산학협력실',
    '박명호 교수',
    '초빙교수실 지역선도대학',
    '문현주 교수',
    '스마트팩토리 실습실',
    '강재구 교수',
    '소프트웨어학과 학과사무실',
    '',
    '교양컴퓨터사무실',
    '교육 준비실 2',
    '교육사업지원실 3',
    '대학원 강의실',
    '학부생 스터디룸'
]

function testLocation(value){
    let end = '';
    for (key in floor1) {
        if (floor1[key] == value) {
            end = key
        }
    }
    for (key in floor2) {
        if (floor2[key] == value) {
            end = key
        }
    }
    for (key in floor3) {
        if (floor3[key] == value) {
            end = key
        }
    }

  $('#'+modalFlag+'Code').val(end);
  $('#'+modalFlag).val(value);

  modal.style.display = 'none';
    
}
var findPath = $('#findpath');

$('html').on('click', '#findpath', function(e){
    var start = $('#startCode').val();
    var end = $('#endCode').val();
    
    location.href = `/map?start=${start}&end=${end}`;
})

