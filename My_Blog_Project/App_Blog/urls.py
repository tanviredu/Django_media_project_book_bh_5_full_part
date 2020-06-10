from django.urls import path
from . import views



app_name = 'App_Blog'

# add support for the media file

urlpatterns = [
    path('',views.blog_list,name='blog_list'),
]
