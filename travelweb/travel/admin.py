from django.contrib import admin

# Register your models here.

from .models import Blog, User, TouristType, Tourist, BlogCategory, Role

admin.site.register(Blog)
admin.site.register(User)
admin.site.register(TouristType)
admin.site.register(Tourist)
admin.site.register(BlogCategory)
admin.site.register(Role)
