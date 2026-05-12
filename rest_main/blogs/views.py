from django.shortcuts import render
from .serializers import BlogSerializer, CommentSerializer
from rest_framework import filters
#ordering filters
from django_filters import rest_framework as django_filters
# Create your views here.
from .models import Blog, Comment
from rest_framework import generics
class blogs_all(generics.ListCreateAPIView,generics.RetrieveDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class =  BlogSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['title', 'created_at']
class comments_all(generics.ListCreateAPIView,generics.RetrieveDestroyAPIView):
   
    queryset = Comment.objects.all()
    serializer_class =  CommentSerializer
class blog_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'
class comment_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'