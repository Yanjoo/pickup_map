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
    
from collections import deque

# BFS 메서드 정의
def bfs(start, end): # 시작 포인트, 끝 포인트
    if start == end: return 1
    
    visited = [False] * 400

    visited[start] = True
    queue = deque([start])
    distant = 1
    
    while queue:
        size = len(queue)

        while size:
            v = queue.popleft()
            cur = get_object_or_404(Point, pk=v)

            next_points = [int(i) for i in cur.connectPoints.split(',')[:-1]]
            for i in next_points:
                if i == end: return distant + 1

            for i in next_points:    
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
            size -= 1
        distant += 1
    return distant


# DFS 메서드 정의
done = False

def dfs(v, visited, queue, end, step, distance):
    visited[v] = True
    if step > distance: return

    if v == end and step == distance:
        global done
        done = True
        return 

    cur = get_object_or_404(Point, pk=v)
    next_points = [int(i) for i in cur.connectPoints.split(',')[:-1]]

    for i in next_points:
        if not visited[i]: 
            dfs(i, visited, queue, end, step+1, distance)
            if done == True:
                queue.append(i)
                return
            visited[i] = False


def toElebator(_from):
    from_store = get_object_or_404(Point, pk=_from)
    start_points = [int(i) for i in from_store.connectPoints.split(',')[:-1]]
    floor = from_store.floor

    end_points = []
    if floor == 1: # 1층일 때
        end_points.extend([116, 117])
    elif floor == 2:
        end_points.extend([27, 28])
    else:
        end_points.extend([36, 37])
    distance = 1000
    point_begin, point_end = 0, 0
    for s in start_points:
        for e in end_points:
            cnt = bfs(s, e)
            if distance > cnt:
                distance = cnt
                point_begin, point_end = s, e

    print(point_begin, point_end, distance)
        
    visited = [False] * 400
    q = deque()
    global done
    done = False
    dfs(point_begin, visited, q, point_end, 1, distance)
    q.append(point_begin)
    print("경로", list(q)[::-1])
    return list(q)[::-1]
    


# 상점과 상점 사이의 최소 길을 찾는다. bfs 후 dfs
def findPath(_from, to):
    # 시작 포인트와 끝 포인트를 찾는다.
    from_store = get_object_or_404(Point, pk=_from)
    start_points = [int(i) for i in from_store.connectPoints.split(',')[:-1]]
    
    to_store = get_object_or_404(Point, pk=to)
    end_points = [int(i) for i in to_store.connectPoints.split(',')[:-1]]
    
    print(start_points)
    print(end_points)
    
    if from_store.floor == to_store.floor: # 같은 층일 때
        distance = 1000
        point_begin, point_end = 0, 0
        for s in start_points:
            for e in end_points:
                cnt = bfs(s, e)
                if distance > cnt:
                    distance = cnt
                    point_begin, point_end = s, e

        print(point_begin, point_end, distance)
        
        visited = [False] * 400
        q = deque()
        global done
        done = False
        dfs(point_begin, visited, q, point_end, 1, distance)
        q.append(point_begin)
        print("경로", list(q)[::-1])
        x = list(q)[::-1]
        l = []
        for i in x:
            pt = get_object_or_404(Point, pk=i)
            l.append([pt.locationX, pt.locationY, pt.locationZ])
        print(l)
        return l
    else: # 다른 층일 때
        q = toElebator(_from) # 엘리베이터까지 간다
        print(q)
        begin_floor = from_store.floor # 시작 층
        end_floor = to_store.floor # 목적지 층
        
        begin_elebator = 10
        if begin_floor == 1: begin_elebator = 10
        elif begin_floor == 2: begin_elebator = 20
        else: begin_elebator = 30 
        
        if begin_floor < end_floor: # 올라가는 경우
            while begin_floor != end_floor:
                q.append(begin_elebator)
                begin_elebator += 10
                begin_floor += 1
            q.append(begin_elebator)
        else: # 내려가는 경우
            while begin_floor != end_floor:
                q.append(begin_elebator)
                begin_elebator -= 10
                begin_floor -= 1
            q.append(begin_elebator)
        q.extend(findPath(begin_elebator, to))
        print(q)
        l = []
        for i in q:
            pt = get_object_or_404(Point, pk=i)
            l.append([pt.locationX, pt.locationY, pt.locationZ])
            
        print(l)
        return l