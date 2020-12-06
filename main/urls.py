from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('index/<str:v_id>', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('map/<str:phone>', views.mapPhone, name='mapPhone'),
    path('map/detail/<int:post_id>/', views.detail, name='detail'),
    path('manage/', views.manage, name='manage'),
    path('delete/<str:phone>', views.delete, name='delete')
]
