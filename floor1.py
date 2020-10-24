# 1층 지도

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pickup_map.settings.local')
import django
django.setup()
from floormanage import *
    
if __name__ == '__main__':
    Point(id=10, name='에스컬레이터1', floor=1, locationX=0, locationY=0, locationZ=0).save()
    Point(15, floor=1, locationX=0, locationY=0, locationZ=-10).save()
    Point(11, '게이트1', floor=1, locationX=0, locationY=0, locationZ=-15).save()
    Point(124, floor=1, locationX=0, locationY=0, locationZ=10).save()
    Point(129, '게이트3', floor=1, locationX=0, locationY=0, locationZ=15).save()
    Point(14, floor=1, locationX=-10, locationY=0, locationZ=-10).save()
    Point(13, floor=1, locationX=-15, locationY=0, locationZ=-10).save()
    Point(12, floor=1, locationX=-23, locationY=0, locationZ=-10).save()
    Point(16, floor=1, locationX=10, locationY=0, locationZ=-10).save()
    Point(17, floor=1, locationX=15, locationY=0, locationZ=-10).save()
    Point(18, floor=1, locationX=20, locationY=0, locationZ=-10).save()
    Point(19, floor=1, locationX=30, locationY=0, locationZ=-10).save()
    Point(110, floor=1, locationX=10, locationY=0, locationZ=-5).save()
    Point(111, floor=1, locationX=15, locationY=0, locationZ=-5).save()
    Point(112, floor=1, locationX=20, locationY=0, locationZ=-5).save()
    Point(113, '게이트2', floor=1, locationX=-28, locationY=0, locationZ=0).save()
    Point(114, floor=1, locationX=-23, locationY=0, locationZ=0).save()
    Point(115, floor=1, locationX=-15, locationY=0, locationZ=0).save()
    Point(116, floor=1, locationX=-10, locationY=0, locationZ=0).save()
    Point(117, floor=1, locationX=10, locationY=0, locationZ=0).save()
    Point(118, floor=1, locationX=15, locationY=0, locationZ=0).save()
    Point(119, floor=1, locationX=20, locationY=0, locationZ=-10).save()
    Point(120, floor=1, locationX=30, locationY=0, locationZ=0).save()
    Point(121, floor=1, locationX=-23, locationY=0, locationZ=10).save()
    Point(122, floor=1, locationX=-15, locationY=0, locationZ=10).save()
    Point(123, floor=1, locationX=-10, locationY=0, locationZ=10).save()
    Point(124, floor=1, locationX=0, locationY=0, locationZ=10).save()
    Point(125, floor=1, locationX=10, locationY=0, locationZ=10).save()
    Point(126, floor=1, locationX=15, locationY=0, locationZ=10).save()
    Point(127, floor=1, locationX=20, locationY=0, locationZ=10).save()
    Point(128, floor=1, locationX=30, locationY=0, locationZ=10).save()
    
    Point(1101, '더바디샵', 1, -25, 0, -13).save()
    Point(1102, '오휘/후', 1, -18, 0, -12).save()
    Point(1103, '키엘',1, -13, 0, -12).save()
    Point(1104, '라스트핏',1, -8, 0, -12).save()
    Point(1105, '스와치그룹 멀티샵',1, 10, 0, -12).save()
    Point(1106, 'TOPS',1, 22, 0, -12).save()
    Point(1107, '하우스오브 쌤소나이트',1, 32, 0, -12).save()
    Point(1108, '설화수',1, -25, 0, -8).save()
    Point(1109, 'SK-II', 1, -20, 0, -7).save()
    Point(1110, '헤라', 1, -20, 0, -3).save()
    Point(1111, '디올', 1, -13, 0, -5).save()
    Point(1112, '빌리프', 1, -8, 0, -5).save()
    Point(1113, '메이크업포에버', 1, 0, 0, -5).save()
    Point(1114, '베네피트', 1, 5, 0, -5).save()
    Point(1115, '제이에스티나', 1, 12.5, 0, -7.5).save()
    Point(1116, '젬크레인', 1, 17.5, 0, -7.5).save()
    Point(1117, '스와로브스키', 1, 12.5, 0, -2.5).save()
    Point(1118, '골등듀', 1, 17.5, 0, -2.5).save()
    Point(1119, '자파즈', 1, 22, 0, -7.5).save()
    Point(1120, '시즌잡화 SEASON', 1, 25, 0, -5).save()
    Point(1121, '엔클라인', 1, 12, 0, -5).save()
    Point(1122, '숨37', 1, -20, 0, 2).save()
    Point(1123, '클라랑스', 1, -18, 0, 2).save()
    Point(1124, '비다벨로', 1, -18, 0, 8).save()
    Point(1125, '동인비', 1, -20, 0, 8).save()
    Point(1126, '불가리 퍼퓸', 1, -25, 0, 5).save()
    Point(1127, '에스티로더', 1, -13, 0, 5).save()
    Point(1128, '샤넬', 1, -2, 0, 4).save()
    Point(1129, '대니 맥켄지', 1, 2, 0, 4).save()
    Point(1130, '스톤헨지', 1, 12.5, 0, 2.5).save()
    Point(1131, '파슬', 1, 12.5, 0, 7.5).save()
    Point(1132, '갤러리아 클락', 1, 17.5, 0, 5).save()
    Point(1133, '투바니', 1, 27.5, 0, 2.5).save()
    Point(1134, '피에르가르멩', 1, 27.5, 0, 7.5).save()
    Point(1135, '닥스', 1, 32, 0, 2).save()
    Point(1136, '루이까또즈', 1, 32, 0, 7.5).save()
    Point(1137, '비오템', 1, -18, 0, -3).save()
    Point(1138, '랑콤', 1, -13, 0, -3).save()
    Point(1139, '메트로시티', 1, 13, 0, 13).save()
    Point(1140, '폴바셋', 1, 27, 0, 13).save()
    
    # 도로 연결
    connectPoints(114, 12, 121, 115) # a14가 가운데
    connectPoints(115, 13, 122, 116) # a15가 가운데
    connectPoints(116, 14, 123) # 16이 가운데
    connectPoints(117, 110, 118, 125) # a17이 가운데
    connectPoints(118, 111, 126, 119) # a18이 가운데
    connectPoints(119, 112, 120, 127) # a19가 가운데
    connectPoints(111, 110, 112, 17) # a11이 가운데
    connectPoints(110, 16)
    connectPoints(112, 18)
    # 맨 윗변
    connectPoints(13, 12, 14)
    connectPoints(15, 14, 16)
    connectPoints(17, 16, 18)
    connectPoints(18, 19)
    # 오른쪽 변
    connectPoints(120, 19, 128)
    # 아랫변
    connectPoints(122, 121, 123)
    connectPoints(124, 123, 125)
    connectPoints(126, 125, 127)
    connectPoints(127, 128)
    
    # 가게 연결
    connectMarketAndPoint(11, 15)
    connectMarketAndPoint(113, 114)
    connectMarketAndPoint(129, 124)
    connectMarketAndPoint(10, 16, 17)
    connectMarketAndPoint(1101, 12) # 더바디샵
    connectMarketAndPoint(1102, 12, 13) # 오휘/후
    connectMarketAndPoint(1103, 13, 14) # 키엘
    connectMarketAndPoint(1104, 14, 15) # 라스트핏
    connectMarketAndPoint(1105, 16) # 스와치그룹 멀티샵
    connectMarketAndPoint(1106, 18) # TOPS
    connectMarketAndPoint(1107, 19) # 하우스오브 쌤소나이트
    connectMarketAndPoint(1108, 12) # 설화수
    connectMarketAndPoint(1109, 12, 13) # SK-II
    connectMarketAndPoint(1110, 114, 115) # 헤라
    connectMarketAndPoint(1111, 13, 115) # 디올
    connectMarketAndPoint(1112, 14, 116) # 빌리프
    connectMarketAndPoint(1113, 15) # 메이크업 포에버
    connectMarketAndPoint(1114, 110) # 베네피트 
    connectMarketAndPoint(1115, 110, 111) # 제이에스티나
    connectMarketAndPoint(1116, 17, 18, 111, 112) # 젬크레인
    connectMarketAndPoint(1117, 110, 111) # 스와로브스키
    connectMarketAndPoint(1118, 111, 112, 118, 119) # 골든듀
    connectMarketAndPoint(1119, 18) # 자파즈
    connectMarketAndPoint(1120, 119, 120) # 시즌잡화
    connectMarketAndPoint(1121, 19) # 엔클라인
    connectMarketAndPoint(1122, 114) # 숨37
    connectMarketAndPoint(1123, 115) # 클라랑스
    connectMarketAndPoint(1124, 122) # 비다벨로
    connectMarketAndPoint(1125, 121) # 동인비
    connectMarketAndPoint(1126, 114, 121) # 불가리 퍼퓸
    connectMarketAndPoint(1127, 115, 122) # 에스티로더
    connectMarketAndPoint(1128, 124) # 샤넬
    connectMarketAndPoint(1129, 124) # 대니 맥켄지
    connectMarketAndPoint(1130, 118) # 스톤헨지
    connectMarketAndPoint(1131, 126) # 파슬
    connectMarketAndPoint(1132, 118, 126) # 갤러리아 클락
    connectMarketAndPoint(1133, 120) # 투바니
    connectMarketAndPoint(1134, 128) # 피에르가르멩
    connectMarketAndPoint(1135, 120) # 닥스
    connectMarketAndPoint(1136, 128) # 루이까또즈
    connectMarketAndPoint(1137, 122) # 비오템
    connectMarketAndPoint(1138, 122) # 랑콤
    connectMarketAndPoint(1139, 125) # 메트로시티
    connectMarketAndPoint(1140, 127, 128) # 풀바셋
