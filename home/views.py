from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Post

class HomePage(ListView):
    template_name = "index.html"
    template_name = "blog.html"
    
    model = Post
class BlogAsos(ListView):
    template_name = "asosi.html"
    template_name = "about.html"
    template_name = "service.html"
    template_name = "team.html"
    template_name = "why.html"
    model = Post
class BlogPage(ListView):
    template_name = "blog.html"
    model = Post

class BlogDetailView(DetailView):
    template_name = "post_detail.html"
    model = Post

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ['title','desc']
class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ['title','desc']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('home')






