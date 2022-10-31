from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('aja/', views.aja, name='aja'),
    path('info/<int:product_id>/<str:product>/', views.info, name='info'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout1, name='logout'),
    path('login/', views.login1, name='login'),
]
