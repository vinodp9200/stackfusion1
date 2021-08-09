from django.urls import path
from .views import index,showallsub_data

urlpatterns=[
    path('index',index),
    path('showall',showallsub_data,name='/showall')
]
