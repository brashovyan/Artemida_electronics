from . import views
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('cart_add/<int:product_id>/<str:product>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/<str:product>/', views.cart_remove, name='cart_remove'),
    path('quantity_plus/<int:product_id>/<str:product>/', views.change_quantity_plus, name='change_quantity_plus'),
    path('quantity_minus/<int:product_id>/<str:product>/', views.change_quantity_minus, name='change_quantity_minus'),
    path('clear/', views.clear, name='clear'),
    path('success/', views.success, name='success'),
    path('info/<int:product_id>/<str:product>/', views.cart_info, name='cart_info'),
]
