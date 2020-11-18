# 2층 지도

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pickup_map.settings.local')
import django
django.setup()
from django.shortcuts import get_object_or_404
from floormanage import *

if __name__ == '__main__':
    Point(id=200, name='계단2', floor=2, locationX=0, locationY=1, locationZ=-10).save()
    Point(id=20, floor=2, locationX=0, locationY=1, locationZ=0).save()
    Point(id=21, floor=2, locationX=30, locationY=1, locationZ=0).save()
    Point(id=22, floor=2, locationX=25, locationY=1, locationZ=0).save()
    Point(id=23, floor=2, locationX=20, locationY=1, locationZ=0).save()
    Point(id=24, floor=2, locationX=15, locationY=1, locationZ=0).save()
    Point(id=25, floor=2, locationX=10, locationY=1, locationZ=0).save()
    Point(id=26, floor=2, locationX=5, locationY=1, locationZ=0).save()
    Point(id=27, floor=2, locationX=-5, locationY=1, locationZ=0).save()
    Point(id=28, floor=2, locationX=-10, locationY=1, locationZ=0).save()
    Point(id=29, floor=2, locationX=-15, locationY=1, locationZ=0).save()
    Point(id=30, floor=2, locationX=-20, locationY=1, locationZ=0).save()
    Point(id=31, floor=2, locationX=-25, locationY=1, locationZ=0).save()
    Point(id=32, floor=2, locationX=-30, locationY=1, locationZ=0).save()
    Point(id=33, floor=2, locationX=-35, locationY=1, locationZ=0).save()
    Point(id=34, floor=2, locationX=-40, locationY=1, locationZ=0).save()
    
    connectPoints(22, 21, 23) # 6이 가운데
    connectPoints(24, 23, 25)# 7이 가운데
    connectPoints(26, 25, 20) # 8이 가운데
    connectPoints(27, 20, 28) # 9가 가운데
    connectPoints(29, 28, 30) # 2가 가운데
    connectPoints(31, 30, 32) # 4가 가운데
    connectPoints(33, 32, 34) # 11이 가운데

    Point(201, '캡스톤 디자인 랩3', 2, 25, 1, 5).save()
    Point(202, '실습 준비실', 2, 15, 1, 5).save()
    Point(203, '서버실', 2, 10, 1, 5).save()
    Point(204, '캡스톤 디자인 랩4', 2, 5, 1, 5).save()
    Point(205, 'PC 실습실1', 2, -5, 1, 5).save()
    Point(206, 'PC 실습실2', 2, -20, 1, 5).save()
    Point(207, '세미나실 I', 2, -32.5, 1, 5).save()
    Point(208, '창고', 2, -40, 1, 5).save()
    Point(209, '지역선도대학 육성사업 사무실', 2, -40, 1, -5).save()
    Point(210, '주영관 교수', 2, -35, 1, -5).save()
    Point(211, '산학협력실', 2, -30, 1, -5).save()
    Point(212, '박명호 교수', 2, -25, 1, -5).save()
    Point(213, '초빙교수실 지역선도대학', 2, -20, 1, -5).save()
    Point(214, '문현주 교수', 2, -15, 1, -5).save()
    Point(215, '스마트팩토리 실습실', 2, -10, 1, -5).save()
    Point(216, '강재구 교수', 2, -5, 1, -5).save()
    Point(217, '소프트웨어학과 학과사무실', 2, 5, 1, -5).save()
    Point(218, '', 2, 10, 1, -5).save()
    Point(219, '교양컴퓨터사무실', 2, 15, 1, -5).save()
    Point(220, '교육 준비실 2', 2, 20, 1, -5).save()
    Point(221, '교육사업지원실 3', 2, 25, 1, -5).save()
    Point(222, '대학원 강의실', 2, 30, 1, -5).save()

    
    connectMarketAndPoint(200, 20) # 에스컬레이터
    connectMarketAndPoint(201, 21) # 토모톰스
    connectMarketAndPoint(202, 22) # 에고이스트
    connectMarketAndPoint(203, 23, 24) # 이프네
    connectMarketAndPoint(204, 26) # 올리브데올리브
    connectMarketAndPoint(205, 27) # 듀엘
    connectMarketAndPoint(206, 29, 30) # 주크
    connectMarketAndPoint(207, 31) # 베네통
    connectMarketAndPoint(208, 34) # 르니앤맥코이
    connectMarketAndPoint(209, 34) # 시슬리
    connectMarketAndPoint(210, 33) # 톰보이
    connectMarketAndPoint(211, 32) # ab fz
    connectMarketAndPoint(212, 31) # 담다
    connectMarketAndPoint(213, 30) # 마리앤
    connectMarketAndPoint(214, 29) # SOUP
    connectMarketAndPoint(215, 28) # 난닝구
    connectMarketAndPoint(216, 27) # 이엔씨
    connectMarketAndPoint(217, 26) # 폴스부띠끄
    connectMarketAndPoint(218, 25) # GGPX
    connectMarketAndPoint(219, 24) # 오즈세컨
    connectMarketAndPoint(220, 23) # 스튜디오럭스
    connectMarketAndPoint(221, 22) # 꾸즈
    connectMarketAndPoint(222, 21) # 밸리걸
 
    
    