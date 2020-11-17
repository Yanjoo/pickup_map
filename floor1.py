# 1층 지도

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pickup_map.settings.local')
import django
django.setup()
from floormanage import *
    
if __name__ == '__main__':
    Point(id=0, name='계단1', floor=1, locationX=0, locationY=0, locationZ=0).save()
    Point(1, floor=1, locationX=-30, locationY=0, locationZ=0).save()
    Point(2, floor=1, locationX=-25, locationY=0, locationZ=0).save()
    Point(3, floor=1, locationX=-20, locationY=0, locationZ=0).save()
    Point(4, floor=1, locationX=-15, locationY=0, locationZ=0).save()
    Point(5, floor=1, locationX=-10, locationY=0, locationZ=0).save()
    Point(6, floor=1, locationX=-5, locationY=0, locationZ=0).save()
    Point(7, floor=1, locationX=5, locationY=0, locationZ=0).save()
    Point(8, floor=1, locationX=10, locationY=0, locationZ=0).save()
    Point(9, floor=1, locationX=15, locationY=0, locationZ=0).save()
    Point(10, floor=1, locationX=20, locationY=0, locationZ=0).save()
    Point(11, floor=1, locationX=25, locationY=0, locationZ=0).save()
    Point(12, floor=1, locationX=30, locationY=0, locationZ=0).save()
    
    Point(101, '101호 전공강의실', 1, 25, 0, 5).save()
    Point(102, '102호 전공강의실', 1, 15, 0, 5).save()
    Point(103, '103호 전공강의실', 1, 5, 0, 5).save()
    Point(104, '104호 전공강의실', 1, -5, 0, 5).save()
    Point(105, '105호 전공강의실', 1, -10, 0, 5).save()
    Point(106, '106호 전공강의실', 1, -20, 0, 5).save()
    Point(107, '정독실', 1, -30, 0, -5).save()
    Point(108, '삼성소프트웨어 부전공실', 1, -25, 0, -5).save()
    Point(109, '학생회실', 1, -20, 0, -5).save()
    Point(110, '엠시스', 1, -15, 0, -5).save()
    Point(111, 'CGAC', 1, -10, 0, -5).save()
    Point(112, '오피스룸', 1, -5, 0, -5).save()
    Point(113, '샘마루', 1, 10, 0, -5).save()
    Point(114, '큐빅', 1, 15, 0, -5).save()
    Point(115, '네스트넷', 1, 20, 0, -5).save()
    Point(116, 'PDA', 1, 25, 0, -5).save()
    Point(117, '노바', 1, 30, 0, -5).save()
    Point(118, '관리실', 1, 5, 0, -5).save()

 
    # 도로 연결
    connectPoints(2, 1, 3) # a14가 가운데
    connectPoints(4, 3, 5) # a15가 가운데
    connectPoints(6, 5, 0) # 16이 가운데
    connectPoints(7, 0, 8) # a17이 가운데
    connectPoints(9, 8, 10) # a18이 가운데
    connectPoints(11, 10, 12) # a19가 가운데

    # 가게 연결
    connectMarketAndPoint(0, 6, 7)
    connectMarketAndPoint(101, 11)
    connectMarketAndPoint(102, 10, 9)
    connectMarketAndPoint(103, 8, 7)
    connectMarketAndPoint(104, 5, 6)
    connectMarketAndPoint(105, 4)
    connectMarketAndPoint(106, 2, 3)
    connectMarketAndPoint(107, 1)
    connectMarketAndPoint(108, 2)
    connectMarketAndPoint(109, 3)
    connectMarketAndPoint(110, 4)
    connectMarketAndPoint(111, 5)
    connectMarketAndPoint(112, 6)
    connectMarketAndPoint(113, 8)
    connectMarketAndPoint(114, 9)
    connectMarketAndPoint(115, 10)
    connectMarketAndPoint(116, 11)
    connectMarketAndPoint(117, 12)
    connectMarketAndPoint(118, 7)
