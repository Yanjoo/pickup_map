import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pickup_map.settings.local')
import django
django.setup()
from main.models import Point
from django.shortcuts import get_object_or_404

def connectPoints(point, *points):
    pt = get_object_or_404(Point, pk=point) # 포인트 노드를 찾음
    for i in points:
        x = get_object_or_404(Point, pk=i) # 연결할 포인트
        data = str(point)+","   # 연결할 포인트에 현재 포인트 추가
        x.connectPoints += data 
        x.save()
        
        data = str(i)+","   # 포인트에 연결할 포인트를 추가
        pt.connectPoints += data
    pt.save()

def connectMarketAndPoint(market, *points):
    mk = get_object_or_404(Point, pk=market)
    for i in points:
        pt = get_object_or_404(Point, pk=i)
        data = str(market)+","
        pt.connectMarkets += data
        pt.save()
        
        data = str(i)+","
        mk.connectPoints += data
    mk.save()
    
def connectPointAndMarket(point, *markets):
    pt = get_object_or_404(Point, pk=point)
    for i in markets:
        data = str(point)+","
        mk = get_object_or_404(Point, pk=i)
        mk.connectPoints += data
        mk.save()
        data = str(i)+","
        pt.connectMarkets += data
    pt.save()