from django.urls import path, include
from . import views


appname='homepage'

urlpatterns = [ path('', views.index, name='Home'),
                path('index', views.index2, name='index'),
                path('logout/', views.logout, name='logout'),
                path('questions/', include('questions.urls')),



]
