from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
from .models import Post


class  PostListView(ListView):
       model = Post
       context_object_name = 'all_posts'
       ordering = ['created_at']
       queryset = Post.objects.filter(active=True)

class  PostDetailView(DetailView):
       model = Post    

class  PostCreateView():
     pass

class  PostDeletView():
     pass

class PostUpdateView():
     pass
