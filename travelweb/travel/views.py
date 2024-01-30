from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, View, DeleteView
from .models import Blog, BlogCategory, Tourist, User, Role, BlogCategory
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from datetime import datetime
from django.http import QueryDict
from django.contrib.auth import authenticate, login
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import redirect, render
from django.views import View
from datetime import datetime
from django.core.files.storage import default_storage


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
    
class TouristDetailView(DetailView):
    model = Tourist
    template_name = 'detail.html'
    
class HotelListView(ListView):
    model = Tourist
    template_name = 'hotel_list.html'
    context_object_name = 'hotels'

    def get_queryset(self):
        return Tourist.objects.filter(type__typeName="Khách sạn")
    
class RestaurantListView(ListView):
    model = Tourist
    template_name = 'restaurant_list.html'
    context_object_name = 'restaurants'

    def get_queryset(self):
        return Tourist.objects.filter(type__typeName="Quán ăn")
    
class SightListView(ListView):
    model = Tourist
    template_name = 'sight_list.html'
    context_object_name = 'sights'

    def get_queryset(self):
        return Tourist.objects.filter(type__typeName="Địa điểm du lịch")
    
class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('travel:index')

        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        #user = authenticate(request, username = username, password = password)
        if User.objects.filter(username = username).exists():
            
            user = User.objects.get(username = username)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            #request.session['role'] = user.role.roleName

            return redirect('travel:index') 

        error_message = "Thông tin đăng nhập không hợp lệ"
        return render(request, 'login.html', {'error_message': error_message})
    
class CustomLogoutView(View):
    next_page = reverse_lazy('travel:login')

    def dispatch(self, request, *args, **kwargs):
        logout(request)  # Xóa thông tin người dùng khỏi request
        # Thực hiện bất kỳ xử lý bổ sung nếu cần
        return redirect(self.next_page)
    
class RegistrationView(View):
    template_name = "registration.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):

        form = QueryDict(request.POST.urlencode())

        username = form.get('username')
        if User.objects.filter(username = username).exists():
            form.add_error('username', 'Username already exists.')
        else:
            user = User(
                username = form.get('username'),
                password = form.get('password'),
                userBirthyear=form.get('userBirthyear'),
                userPhone=form.get('userPhone'),
                first_name=form.get('first_name'),
                last_name = form.get('last_name'),
                date_joined = datetime.now(),
                is_active = 1,
                blogCount = 0
            )
            
            user.save()
            return redirect('travel:login')

        return render(request, self.template_name, {'form': form})
    
class BlogCreateView(LoginRequiredMixin, View):
    template_name = "blog_create.html"
    login_url = reverse_lazy('travel:login')

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):

        form = QueryDict(request.POST.urlencode())

        user = request.user
        
        image_file = request.FILES.get('blogImage')
        if image_file:
        # Lưu tệp tin vào thư mục media_root
            file_path = default_storage.save(image_file.name, image_file)
            file_url = default_storage.url(file_path)
        else:
            file_url = None
    
        blog = Blog(
            blogTitle=form.get('blogTitle'),
            blogAuthor=form.get('blogAuthor'),
            blogContent=form.get('blogContent'),
            category=BlogCategory.objects.get(categoryName=form.get('categoryName')),
            blogDate=datetime.now(),
            blogImage=file_url
        )

        category=BlogCategory.objects.get(categoryName=form.get('categoryName'))
        category.categoryName += 1
        category.save()
            
        blog.save()
        user.blogCount += 1
        user.save()
        return redirect('travel:blog')