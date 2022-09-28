from django.urls import path
from . import views

urlpatterns=[
    path('dd', views.demo,name='dd'),
    path('', views.tt, name='test'),
    path('About', views.about,)
    ]
    