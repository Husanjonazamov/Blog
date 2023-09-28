from django.contrib import admin
from django.urls import path,include
from home.views import (
    HomePage,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    BlogAsos,
    BlogPage
)

urlpatterns = [
    path("post/<int:pk>/delete/",BlogDeleteView.as_view(), name="post_delete"),
    path("post/<int:pk>/edit",BlogUpdateView.as_view(), name="post_edit"),
    path("post/new/",BlogCreateView.as_view(), name="post_new"),
    path("home/",HomePage.as_view(), name='home'),
    path("",BlogAsos.as_view(), name="asos"),
    path("home/",BlogPage.as_view(), name="logout"),
    path("post/<int:pk>/",BlogDetailView.as_view(), name="post_detail"),
]
