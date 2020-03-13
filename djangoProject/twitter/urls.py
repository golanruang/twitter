from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('0', views.twitterPosts, name='posts'),
    path('0/', views.twitterPosts, name='posts'),
    path('1', views.twitterLogin, name='login'),
    path('1/', views.twitterLogin, name='login'),
    path('1/authenticate/', views.authenticate, name="authenticate"),
    path('1/authenticate', views.authenticate, name="authenticate"),
    path('login/', views.twitterPosts, name='posts'),
    path('login',views.twitterPosts, name='posts'),
    path('authenticate/', views.authenticate, name="authenticate"),
    path('authenticate', views.authenticate, name="authenticate"),
]
