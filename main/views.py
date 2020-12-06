from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import *
from .algorithms import *
from .forms import *
from .data import info


def login(request):
    if request.method == 'POST':
        print('POST')
        print('요청', request.POST)
        form = VisitorForm(request.POST)
        if form.is_valid():
            visitor = form.save(commit=False)
            visitor.save()
            return redirect('index', visitor.phone)
    else:
        form = VisitorForm()
        print('로그인 생성')
    return render(request, 'main/login.html', {'form': form})

def manage(request):
    visitors = Visitor.objects.all()
    print('전체 방문자', visitors)

    return render(request, 'main/manage.html', {'visitors':visitors })

def index(request, v_id):
    print(v_id)
    return render(request, 'main/index.html', {"v_id": v_id})

def map(request):
    if request.method == 'POST':
        print('검색', request.POST)
        search = request.POST.get('search')
        print('검색 내용', search, info.get(search))
        search = info.get(search, 0)
        return redirect('detail', search)

    start = request.GET.get('start','11') # 시작 점 
    end = request.GET.get('end','') # 종료점
    phone = request.GET.get('phone', '')

    visitor = get_object_or_404(Visitor, pk=phone)
    visitor.startPoint = start
    visitor.endPoint = end
    visitor.save()

    print('요청', request.GET)

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
    return render(request, 'main/PickupMap.html', {'destination':point_end, 'base_position': point_start, 'root':points_list, 'points': points, 'phone':phone})

def mapPhone(request, phone):
    if request.method == 'POST':
        print('검색', request.POST)
        search = request.POST.get('search')
        print('검색 내용', search, info.get(search))
        search = info.get(search, 0)
        return redirect('detail', search)

    visitor = get_object_or_404(Visitor, pk=phone)

    start = visitor.startPoint # 시작 점 
    end = visitor.endPoint # 종료점
    

    visitor = get_object_or_404(Visitor, pk=phone)
    visitor.startPoint = start
    visitor.endPoint = end
    visitor.save()

    print('요청', request.GET)

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
    return render(request, 'main/PickupMap.html', {'destination':point_end, 'base_position': point_start, 'root':points_list, 'points': points, 'phone':phone})


def detail(request, post_id):
    if post_id == 109: # 학생회실
        return render(request, 'main/studentunion.html') 
    elif post_id >= 314 and post_id <= 320:  # 교슈실
        return render(request, 'main/aziz.html')
    elif post_id >= 323 and post_id <= 329: # 교수실
        return render(request, 'main/aziz.html')
    elif post_id >= 110 and post_id <= 117: # 동아리방
        return render(request, 'main/sammaru.html')


def delete(request, phone):
    visitor = get_object_or_404(Visitor, pk=phone)
    visitor.delete()
    return redirect('manage')