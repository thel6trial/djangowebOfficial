
from django.urls import path, include
from .views import BlogListView, PostView, BlogDetailView, HotelListView, RestaurantListView, SightListView, LoginView, CustomLogoutView, RegistrationView, BlogCreateView, TouristDetailView

app_name = "travel" 

urlpatterns = [
    path("main", PostView.as_view(), name="index"),
    path("blog", BlogListView.as_view(), name="blog"),
    path("detail/<int:pk>", BlogDetailView.as_view(), name="detail"),
    path("tourist/<int:pk>", TouristDetailView.as_view(), name="tourist"),
    path("hotels", HotelListView.as_view(), name="hotel"),
    path("restaurants", RestaurantListView.as_view(), name="restaurant"),
    path("sights", SightListView.as_view(), name="sight"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", CustomLogoutView.as_view(), name = "logout"),
    path("register", RegistrationView.as_view(), name = "registration"),
    path("creation", BlogCreateView.as_view(), name = "blog_create"),
]
