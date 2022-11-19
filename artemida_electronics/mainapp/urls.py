from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('constructor/', views.constructor, name='constructor'),
    path('aja/', views.aja, name='aja'),
    path('info/<int:product_id>/<str:product>/', views.info, name='info'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout1, name='logout'),
    path('login/', views.login1, name='login'),
    path('profile/<int:id>/', views.profile, name='profile'),
    
    path('processors/', views.processors, name='processors'),
    path('processors/<str:filter>/', views.processors),
    path('coolers/', views.coolers, name='coolers'),
    path('coolers/<str:filter>/', views.coolers),
    path('motherboards/', views.motherboards, name='motherboards'),
    path('motherboards/<str:filter>/', views.motherboards),
    path('rams/', views.rams, name='rams'),
    path('rams/<str:filter>/', views.rams),
    path('ssd_m2s/', views.ssd_m2s, name='ssd_m2s'),
    path('ssd_m2s/<str:filter>/', views.ssd_m2s),
    path('hdds/', views.hdds, name='hdds'),
    path('hdds/<str:filter>/', views.hdds),
    path('ssd_satas/', views.ssd_satas, name='ssd_satas'),
    path('ssd_satas/<str:filter>/', views.ssd_satas),
    path('videocards/', views.videocards, name='videocards'),
    path('videocards/<str:filter>/', views.videocards),
    path('power_blocks/', views.power_blocks, name='power_blocks'),
    path('power_blocks/<str:filter>/', views.power_blocks),
    path('corpuses/', views.corpuses, name='corpuses'),
    path('corpuses/<str:filter>/', views.corpuses),
]
