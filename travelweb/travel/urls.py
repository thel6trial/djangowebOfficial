
from django.urls import path, include
from .views import BlogListView, PostView, BlogDetailView

app_name = "travel"

urlpatterns = [
    path("main", PostView.as_view(), name="index"),
    path("blog", BlogListView.as_view(), name="blog"),
    path("detail/<int:pk>", BlogDetailView.as_view(), name="detail"),
]