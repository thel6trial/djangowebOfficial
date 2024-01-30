from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, View, DeleteView
from .models import Blog, User, BlogCategory
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from datetime import datetime
from django.http import QueryDict

# Create your views here.

class PostView(ListView):
    model = Blog
    context_object_name = "blog_list"
    template_name = "index.html"


class BlogListView(ListView):
    template_name = 'blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        # Lấy tất cả các bài viết từ mô hình Blog
        return Blog.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Thêm dữ liệu từ mô hình BlogCategory vào context
        context['categories'] = BlogCategory.objects.all()
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        return context
