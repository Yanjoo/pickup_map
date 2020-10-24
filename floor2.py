# 2층 지도

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pickup_map.settings.local')
import django
django.setup()
from django.shortcuts import get_object_or_404
from algorithms import *

if __name__ == '__main__':
    Point(id=20, name='에스컬레이터2', floor=2, locationX=0, locationY=1, locationZ=0).save()
    Point(id=21, floor=2, locationX=-23, locationY=1, locationZ=-10).save()
    Point(id=22, floor=2, locationX=-10, locationY=1, locationZ=-10).save()
    Point(id=23, floor=2, locationX=10, locationY=1, locationZ=-10).save()
    Point(id=24, floor=2, locationX=20, locationY=1, locationZ=-10).save()
    Point(id=25, floor=2, locationX=30, locationY=1, locationZ=-10).save()
    Point(id=26, floor=2, locationX=-23, locationY=1, locationZ=0).save()
    Point(id=27, floor=2, locationX=-10, locationY=1, locationZ=0).save()
    Point(id=28, floor=2, locationX=10, locationY=1, locationZ=0).save()
    Point(id=29, floor=2, locationX=30, locationY=1, locationZ=0).save()
    Point(id=210, floor=2, locationX=-23, locationY=1, locationZ=10).save()
    Point(id=211, floor=2, locationX=-10, locationY=1, locationZ=10).save()
    Point(id=212, floor=2, locationX=10, locationY=1, locationZ=10).save()
    Point(id=213, floor=2, locationX=30, locationY=1, locationZ=10).save()

    connectPoints(26, 21, 27, 210) # 6이 가운데
    connectPoints(27, 22, 211)# 7이 가운데
    connectPoints(28, 23, 212, 29) # 8이 가운데
    connectPoints(29, 25, 213) # 9가 가운데
    connectPoints(22, 21, 23) # 2가 가운데
    connectPoints(24, 23, 25) # 4가 가운데
    connectPoints(211, 210 ,212) # 11이 가운데
    connectPoints(213, 212) # 13이 가운데
    
    Point(2101, '토모톰스', 2, -27, 1, -5).save()
    Point(2102, '에고이스트', 2, -18, 1, -12).save()
    Point(2103, '이프네', 2, -13, 1, -12).save()
    Point(2104, '올리브데올리브', 2, -5, 1, -12).save()
    Point(2105, '듀엘', 2, 0, 1, -12).save()
    Point(2106, '주브', 2, 15, 1, -12).save()
    Point(2107, '베네통', 2, 20, 1, -12).save()
    Point(2108, '르니앤맥코이', 2, 20, 1, -12).save()
    Point(2109, '시슬리', 2, 32, 1, -8).save()
    Point(2110, '톰보이', 2, -25, 1, -5).save()
    Point(2111, 'ab f.z.', 2, -20, 1, -7.5).save()
    Point(2112, '담다', 2, -15, 1, -7.5).save()
    Point(2113, '마리앤', 2, -20, 1, -2.5).save()
    Point(2114, 'SOUP', 2, -15, 1, -2.5).save()
    Point(2115, '난닝구', 2, -5, 1, -5).save()
    Point(2116, '이엔씨', 2, 5, 1, -5).save()
    Point(2117, '폴스부띠끄 / 세컨스킨', 2, 15, 1, -7.5).save()
    Point(2118, 'GGPX', 2, 25, 1, -5).save()
    Point(2119, '오즈세컨', 2, 32, 1, -3).save()
    Point(2120, '스튜디오럭스', 2, -25, 1, 2).save()
    Point(2121, '꾸즈', 2, -20, 1, 2.5).save()
    Point(2122, '밸리걸', 2, -15, 1, 2.5).save()
    Point(2123, '루코루코', 2, -20, 1, 7.5).save()
    Point(2124, '리안뉴욕', 2, -15, 1, 7.5).save()
    Point(2125, '르피타', 2, -5, 1, 5).save()
    Point(2126, '온앤온', 2, 2, 1, 5).save()
    Point(2127, '반에이크', 2, 15, 1, 2.5).save()
    Point(2128, '탑걸', 2, 15, 1, 7.5).save()
    Point(2129, '케네스레이디', 2, 23, 1, 5).save()
    Point(2130, '보브', 2, 32, 1, 2).save()
    Point(2131, '라인', 2, 32, 1, 8).save()
    Point(2132, '타미힐피거여성', 2, -20, 1, 13).save()
    Point(2133, '해지스레이디스', 2, -13, 1, 13).save()
    Point(2134, '빈폴 레이디스', 2, -8, 1, 13).save()
    Point(2135, '쥬시쥬디', 2, 3, 1, 13).save()
    Point(2136, '잇미샤', 2, 12, 1, 13).save()
    Point(2137, '로엠', 2, 17, 1, 13).save()
    Point(2138, 'JJ지고트', 2, 25, 1, 13).save()
    Point(2139, '리스트', 2, 32, 1, 13).save()
    
    connectMarketAndPoint(20, 27, 28) # 에스컬레이터
    connectMarketAndPoint(2101, 21) # 토모톰스
    connectMarketAndPoint(2102, 21) # 에고이스트
    connectMarketAndPoint(2103, 22) # 이프네
    connectMarketAndPoint(2104, 22) # 올리브데올리브
    connectMarketAndPoint(2105, 23) # 듀엘
    connectMarketAndPoint(2106, 23) # 주크
    connectMarketAndPoint(2107, 24) # 베네통
    connectMarketAndPoint(2108, 24) # 르니앤맥코이
    connectMarketAndPoint(2109, 25) # 시슬리
    connectMarketAndPoint(2110, 26) # 톰보이
    connectMarketAndPoint(2111, 21) # ab fz
    connectMarketAndPoint(2112, 22) # 담다
    connectMarketAndPoint(2113, 26) # 마리앤
    connectMarketAndPoint(2114, 27) # SOUP
    connectMarketAndPoint(2115, 22, 27) # 난닝구
    connectMarketAndPoint(2116, 23) # 이엔씨
    connectMarketAndPoint(2117, 23, 24) # 폴스부띠끄
    connectMarketAndPoint(2118, 25) # GGPX
    connectMarketAndPoint(2119, 29) # 오즈세컨
    connectMarketAndPoint(2120, 26) # 스튜디오럭스
    connectMarketAndPoint(2121, 26) # 꾸즈
    connectMarketAndPoint(2122, 27) # 밸리걸
    connectMarketAndPoint(2123, 210) # 루코루코
    connectMarketAndPoint(2124, 211) # 리안뉴욕
    connectMarketAndPoint(2125, 27, 211) # 르피타
    connectMarketAndPoint(2126, 28, 212) # 온앤온
    connectMarketAndPoint(2127, 28) # 반에이크
    connectMarketAndPoint(2128, 212) # 탑걸
    connectMarketAndPoint(2129, 29, 213) # 케네스레이디
    connectMarketAndPoint(2130, 29) # 보브
    connectMarketAndPoint(2131, 213) # 라인
    connectMarketAndPoint(2132, 210) # 타미힐피거 여성
    connectMarketAndPoint(2133, 211) # 해지스레이디
    connectMarketAndPoint(2134, 211) # 빈폴레이디스
    connectMarketAndPoint(2135, 212) # 쥬시 쥬디
    connectMarketAndPoint(2136, 212) # 잇미샤
    connectMarketAndPoint(2137, 212) # 로엠
    connectMarketAndPoint(2138, 213) # JJ지고트
    connectMarketAndPoint(2139, 213) # 리스트
    
    
    