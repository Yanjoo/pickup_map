from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Point
from .algorithms import *


def find(start, end):
    start = 1102 # 시작 점
    end = 3101 # 종료점
    paths = findPath(start, end)
    print('=========')
    print('경로', paths)
    points_list = [] # 중간 경로 좌표
    for i in paths:
        pt = get_object_or_404(Point, pk=i)
        points_list.append([pt.locationX, pt.locationY, pt.locationZ])
    
    start_point = get_object_or_404(Point, id=start)
    end_point = get_object_or_404(Point, id=end)
    point_start = [start_point.locationX, start_point.locationY, start_point.locationZ]
    point_end = [end_point.locationX, end_point.locationY, end_point.locationZ]
    
    print('중간 좌표', points_list)
    print('시작 좌표', point_start)
    print('종료 좌표', point_end)

def checkLocation(code):

    # 코드 

    return 

def index(request):
    if request.is_ajax():
        code = request.GET.get('code','')
        shop = request.GET.get('shop','')
        search()
    else:
        return render(request, 'main/index.html')


def map(request):
    start = 1102 # 시작 점
    end = 3101 # 종료점
    paths = findPath(start, end)
    print('=========')
    print('경로', paths)
    points_list = [] # 중간 경로 좌표
    for i in paths:
        pt = get_object_or_404(Point, pk=i)
        points_list.append([pt.locationX, pt.locationY, pt.locationZ])
    
    start_point = get_object_or_404(Point, id=start)
    end_point = get_object_or_404(Point, id=end)
    point_start = [start_point.locationX, start_point.locationY, start_point.locationZ]
    point_end = [end_point.locationX, end_point.locationY, end_point.locationZ]
    
    print('중간 좌표', points_list)
    print('시작 좌표', point_start)
    print('종료 좌표', point_end)
    
    return render(request, 'main/PickupMap.html', {'destination':point_end, 'base_position': point_start, 'root':points_list})