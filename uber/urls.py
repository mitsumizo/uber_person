from django.urls import path
from . import views


urlpatterns = [
    path('', views.Post_Shufu, name='Post_Shufu'),
]