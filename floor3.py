# 3층
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pickup_map.settings.local')
import django
django.setup()
from floormanage import *


if __name__ == '__main__':
    Point(id=300, name='계단3', floor=3, locationX=0, locationY=2, locationZ=-10).save()
    Point(id=40, floor=3, locationX=0, locationY=2, locationZ=0).save()
    Point(id=41, floor=3, locationX=45, locationY=2, locationZ=0).save()
    Point(id=42, floor=3, locationX=40, locationY=2, locationZ=0).save()
    Point(id=43, floor=3, locationX=35, locationY=2, locationZ=0).save()
    Point(id=44, floor=3, locationX=30, locationY=2, locationZ=0).save()
    Point(id=45, floor=3, locationX=25, locationY=2, locationZ=0).save()
    Point(id=46, floor=3, locationX=20, locationY=2, locationZ=0).save()
    Point(id=47, floor=3, locationX=15, locationY=2, locationZ=0).save()
    Point(id=48, floor=3, locationX=10, locationY=2, locationZ=0).save()
    Point(id=49, floor=3, locationX=5, locationY=2, locationZ=0).save()
    Point(id=50, floor=3, locationX=-5, locationY=2, locationZ=0).save()
    Point(id=51, floor=3, locationX=-10, locationY=2, locationZ=0).save()
    Point(id=52, floor=3, locationX=-15, locationY=2, locationZ=0).save()
    Point(id=53, floor=3, locationX=-20, locationY=2, locationZ=0).save()
    Point(id=54, floor=3, locationX=-25, locationY=2, locationZ=0).save()
    Point(id=55, floor=3, locationX=-30, locationY=2, locationZ=0).save()
    Point(id=56, floor=3, locationX=-35, locationY=2, locationZ=0).save()
    Point(id=57, floor=3, locationX=-40, locationY=2, locationZ=0).save()
    Point(id=58, floor=3, locationX=-45, locationY=2, locationZ=0).save()
    Point(id=59, floor=3, locationX=-50, locationY=2, locationZ=0).save()
    


    connectPoints(42, 41, 43) # 5이 가운데
    connectPoints(44, 43, 45)# 6이 가운데
    connectPoints(46, 45, 47) # 7이 가운데
    connectPoints(48, 47, 49) #89가 가운데
    connectPoints(40, 49, 50) # 2가 가운데
    connectPoints(51, 50, 52) # 4가 가운데
    connectPoints(53, 52 ,54) # 10이 가운데
    connectPoints(55, 54, 56) # 12이 가운데
    connectPoints(57, 56, 58) # 12이 가운데
    connectPoints(59, 58) # 12이 가운데
    

    Point(301, '문서보관창고', 3, 45, 2, 5).save()
    Point(302, '언어지식공학 연구실', 3, 40, 2, 5).save()
    Point(303, '데이터베이스 및 스마트팩토리 연구실', 3, 32.5, 2, 5).save()
    Point(304, '데이터 분석 연구실', 3, 22.5, 2, 5).save()
    Point(305, '인공지능 연구실', 3, 17.5, 2, 5).save()
    Point(306, '정보시스템 연구실', 3, 5, 2, 5).save()
    Point(307, '컴퓨터그래픽 및 콘텐츠 연구실', 3, -5, 2, 5).save()
    Point(308, '소프트웨어공학 연구실', 3, -12.5, 2, 5).save()
    Point(309, '컴퓨터비전 및 패턴인식 연구실', 3, -22.5, 2, 5).save()
    Point(310, '실시간 시스템 연구실', 3, -35, 2, 5).save()
    Point(311, '데이터컴퓨팅 연구실', 3, -45, 2, 5).save()
    Point(312, '세미나실I', 3, -50, 2, 5).save()
    Point(313, '임베디드시스템 연구실', 3, -50, 2, -5).save()
    Point(314, '전중남 교수', 3, -45, 2, -2.5).save()
    Point(315, '노서영 교수', 3, -40, 2, -5).save()
    Point(316, '김명준 교수', 3, -35, 2, -5).save()
    Point(317, '이의종 교수', 3, -30, 2, -5).save()
    Point(318, '최경주 교수', 3, -25, 2, -5).save()
    Point(319, '류관희 교수', 3, -20, 2, -5).save()
    Point(320, '홍장의 교수', 3, -15, 2, -5).save()
    Point(321, '기계실', 3, -10, 2, -5).save()
    Point(322, '학과 회의실', 3, -5, 2, -5).save()
    Point(323, '조오현 교수', 3, 5, 2, -5).save()
    Point(324, '이재성 교수', 3, 10, 2, -5).save()
    Point(325, '이건명 교수', 3, 15, 2, -5).save()
    Point(326, '아지즈 교수', 3, 20, 2, -5).save()
    Point(327, '조희승 교수', 3, 25, 2, -5).save()
    Point(328, '이종연 교수', 3, 30, 2, -5).save()
    Point(329, '조승범 교수', 3, 35, 2, -5).save()
    Point(330, '컴퓨터시스템 연구실', 3, 40, 2, -5).save()
    Point(331, '자료구조 및 알고리즘 연구실', 3, 45, 2, -5).save()
    Point(332, '대학원세미나실', 3, 25, 2, 2.5).save()

    
    connectPointAndMarket(41, 301, 331)
    connectPointAndMarket(42, 302, 330)
    connectPointAndMarket(43, 303, 329)
    connectPointAndMarket(44, 303, 328)
    connectPointAndMarket(45, 304, 327)
    connectPointAndMarket(46, 304, 326)
    connectPointAndMarket(47, 305, 325)
    connectPointAndMarket(48, 305, 324)
    connectPointAndMarket(49, 323, 306)
    connectPointAndMarket(40, 332, 300)
    connectPointAndMarket(50, 307, 322)
    connectPointAndMarket(51, 308, 321)
    connectPointAndMarket(52, 320, 308)
    connectPointAndMarket(53, 309, 319)
    connectPointAndMarket(54, 309, 318)
    connectPointAndMarket(55, 317, 310)
    connectPointAndMarket(56, 310, 316)
    connectPointAndMarket(57, 315, 310, 311)
    connectPointAndMarket(58, 314, 311)
    connectPointAndMarket(59, 313, 312)

    
    
    
    
    
    
    
    