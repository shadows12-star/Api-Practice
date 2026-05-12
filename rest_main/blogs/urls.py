from django.contrib import admin
from django.urls import path
from django.urls import include

from . import views
urlpatterns = [
   
    path('blogs/',views.blogs_all.as_view(), name='blogs_all'),
    path('comments/',views.comments_all.as_view(), name='comments_all'),
    path('blogs/<int:pk>/',views.blog_detail.as_view(), name='blog_detail'),
    path('comments/<int:pk>/',views.comment_detail.as_view(), name='comment_detail'),
]