from django.shortcuts import render
from django.conf import settings
from .algorithms import *
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
    
    return render(request, 'main/PickupMap.html')