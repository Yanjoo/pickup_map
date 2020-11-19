from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('map/<int:post_id>/', views.detail, name='detail'),
]
