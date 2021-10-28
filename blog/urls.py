from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

    # path('home/',home,name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='blog-user'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name="blog-detail"),
    path('detail/<int:pk>/update', PostUpdateView.as_view(), name="blog-update"),
    path('detail/<int:pk>/delete', PostDeleteView.as_view(), name="blog-delete"),
    path('post/new/', PostCreateView.as_view(), name='blog-create'),
    path('about/', about, name='blog-about'),

]
