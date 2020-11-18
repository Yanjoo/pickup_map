from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import Point
from .algorithms import *

def index(request):
    return render(request, 'main/index.html')


def map(request):
    start = request.GET.get('start','11') # 시작 점 
    end = request.GET.get('end','') # 종료점
    if end == '':
        return redirect('index')
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

    points = []

    for i in range(100, 120):
        point = get_object_or_404(Point, pk=i)
        point_info = [point.locationX, point.locationY, point.locationZ, point.name]
        points.append(point_info)
    
    for i in range(200, 223):
        point = get_object_or_404(Point, pk=i)
        point_info = [point.locationX, point.locationY, point.locationZ, point.name]
        points.append(point_info)

    for i in range(300, 333):
        point = get_object_or_404(Point, pk=i)
        point_info = [point.locationX, point.locationY, point.locationZ, point.name]
        points.append(point_info)
    return render(request, 'main/PickupMap.html', {'destination':point_end, 'base_position': point_start, 'root':points_list, 'points': points})