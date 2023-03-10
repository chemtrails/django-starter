from django.urls import path, include
from . import views

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]