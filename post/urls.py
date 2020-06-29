from django.urls import path
from django.conf.urls import url
from . import views
from .views import PostListView

app_name = 'post'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'), 
]