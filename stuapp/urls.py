from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index' ),
    path('login/', views.login, name= 'login' ),
    path('doLogin/', views.doLogin, name='doLogin'),
    path('get_user_detail/', views.GetUserDetail, name='get_user_detail'),
    path('logout_user/', views.logout_user, name='logout_user'),
]