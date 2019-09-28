from django.urls import path
from . import views


urlpatterns = [
    path('', views.Post_Shufu, name='Post_Shufu'),
    path('/syufu/login', views.syufu_login, name='syufu_login'),
    path('/syufu/new', views.syufu_sign_up, name='syufu_sign_up')
]