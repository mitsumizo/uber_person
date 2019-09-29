from django.urls import path
from . import views


urlpatterns = [
    path('', views.Top_Page, name='Top_Page'),
    path('uber/login/', views.Form_User, name='Form_User'),
    path('syufu/login', views.login_syufu, name='login_syufu'),
    path('syufu/new', views.syufu_sign_up, name='syufu_sign_up'),
    path('detail/<int:pk>/', views.account_detail, name='account_detail'),
    path('food/detail_nikujaga', views.detail_food, name='detail_nikujaga'),

]