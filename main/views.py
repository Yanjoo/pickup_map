from django.shortcuts import render
from django.conf import settings
from .algorithms import *
def checkLocation(code):

    # 코드 

    return 

def index(request):
    paths = findPath(1102, 2101)
    print('=========')
    print(paths)
    points_list = []
    for i in paths:
        pt = get_object_or_404(Point, pk=i)
        points_list.append([pt.locationX, pt.locationY, pt.locationZ])
    print(points_list)    
    

    if request.is_ajax():
        code = request.GET.get('code','')
        shop = request.GET.get('shop','')
        search()
    else:
        return render(request, 'main/index.html')


def map(request):
    
    return render(request, 'main/PickupMap.html')