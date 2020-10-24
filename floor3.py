# 3층
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pickup_map.settings.local')
import django
django.setup()
from floormanage import *


if __name__ == '__main__':
    Point(id=30, name='에스컬레이터3', floor=3, locationX=0, locationY=2, locationZ=0).save()
    Point(id=31, floor=3, locationX=-23, locationY=2, locationZ=-10).save()
    Point(id=32, floor=3, locationX=-10, locationY=2, locationZ=-10).save()
    Point(id=33, floor=3, locationX=10, locationY=2, locationZ=-10).save()
    Point(id=34, floor=3, locationX=30, locationY=2, locationZ=-10).save()
    Point(id=35, floor=3, locationX=-23, locationY=2, locationZ=0).save()
    Point(id=36, floor=3, locationX=-10, locationY=2, locationZ=0).save()
    Point(id=37, floor=3, locationX=10, locationY=2, locationZ=0).save()
    Point(id=38, floor=3, locationX=30, locationY=2, locationZ=0).save()
    Point(id=39, floor=3, locationX=-23, locationY=2, locationZ=10).save()
    Point(id=310, floor=3, locationX=-10, locationY=2, locationZ=10).save()
    Point(id=311, floor=3, locationX=10, locationY=2, locationZ=10).save()
    Point(id=312, floor=3, locationX=30, locationY=2, locationZ=10).save()
    
    connectPoints(35, 31, 36, 39) # 5이 가운데
    connectPoints(36, 32, 310)# 6이 가운데
    connectPoints(37, 33, 311, 38) # 7이 가운데
    connectPoints(38, 34, 312) #89가 가운데
    connectPoints(32, 31, 33) # 2가 가운데
    connectPoints(34, 33) # 4가 가운데
    connectPoints(310, 39 ,311) # 10이 가운데
    connectPoints(312, 311) # 12이 가운데
    
    Point(3101, '시크릿우먼', 3, -25, 2, -15).save()
    Point(3102, '마담포라', 3, -18, 2, -12).save()
    Point(3103, '닥스1', 3, -13, 2, -12).save()
    Point(3104, '리본', 3, -5, 2, -12).save()
    Point(3105, '비비안', 3, 5, 2, -12).save()
    Point(3106, '비너스', 3, 10, 2, -12).save()
    Point(3107, '와코루', 3, 14, 2, -12).save()
    Point(3108, '금강/랜드로바', 3, 21, 2, -12).save()
    Point(3109, '세라젬(오가다)', 3, 30, 2, -15).save()
    Point(3110, '부르다문', 3, -27, 2, -12).save()
    Point(3111, '시스막스', 3, -26, 2, -5).save()
    Point(3112, '에스투피', 3, -20, 2, -7.5).save()
    Point(3113, '벨리시앙', 3, -15, 2, -7.5).save()
    Point(3114, '에스깔리에', 3, -20, 2, -2.5).save()
    Point(3115, '정호진', 3, -15, 2, -2.5).save()
    Point(3116, '로잔', 3, -7, 2, -5).save()
    Point(3117, '뽀뜨레', 3, 0, 2, -5).save()
    Point(3118, '베띠앙뜨', 3, 7, 2, -5).save()
    Point(3119, '에스콰이아', 3, 15, 2, -2.5).save()
    Point(3120, '엘칸토', 3, 25, 2, -7.5).save()
    Point(3121, '바이네르', 3, 15, 2, -2.5).save()
    Point(3122, '닥스2', 3, 25, 2, -2.5).save()
    Point(3123, '소다', 3, 33, 2, -6).save()
    Point(3124, '루치아노최', 3, -25, 2, 3).save()
    Point(3125, '빈루즈', 3, -25, 2, 7.5).save()
    Point(3126, '이동수', 3, -21, 2, 5).save()
    Point(3127, '리베도', 3, -16, 2, 2.5).save()
    Point(3128, '올리비아하슬러', 3, -16, 2, 7.5).save()
    Point(3129, '엠씨', 3, -3.5, 2, 5).save()
    Point(3130, '요하네스', 3, 5, 2, 5).save()
    Point(3131, '미소페', 3, 15, 2, 2.5).save()
    Point(3132, '마겟', 3, 25, 2, 2.5).save()
    Point(3133, '트리아나', 3, 15, 2, 7.5).save()
    Point(3134, '리아트', 3, 25, 2, 7.5).save()
    Point(3135, '탠디', 3, 33, 2, 5).save()
    Point(3136, '몬테밀라노', 3, -20, 2, 13).save()
    Point(3137, '레노마레이디', 3, -17, 2, 13).save()
    Point(3138, '크로커다일', 3, -12, 2, 13).save()
    Point(3139, '더람', 3, -8, 2, 13).save()
    Point(3140, '우바', 3, 0, 2, 13).save()
    Point(3141, '아이잗바바', 3, 8, 2, 13).save()
    Point(3142, '크레송', 3, 13, 2, 13).save()
    Point(3143, '근화모피', 3, 22, 2, 13).save()
    Point(3144, '휴테크', 3, 28, 2, 13).save()
    
    connectPointAndMarket(31, 3101, 3102, 3110, 3112)
    connectPointAndMarket(32, 3103, 3104, 3113, 3116, 3117)
    connectPointAndMarket(33, 3105, 3106, 3107, 3117, 3118, 3119)
    connectPointAndMarket(34, 3108, 3109, 3120, 3123)
    connectPointAndMarket(35, 3111, 3114, 3124, 3126)
    connectPointAndMarket(36, 3116, 3115, 3127, 3129, 30)
    connectPointAndMarket(37, 3118, 3121, 3130, 3131, 30)
    connectPointAndMarket(38, 3122, 3123, 3132, 3132)
    connectPointAndMarket(39, 3125, 3126, 3136, 3137)
    connectPointAndMarket(310, 3128, 3129, 3137, 3138, 3139, 3140)
    connectPointAndMarket(311, 3133, 3130, 3140, 3141, 3142, 3143)
    connectPointAndMarket(312, 3134, 3135, 3143, 3144)
    
    
    
    
    
    
    
    