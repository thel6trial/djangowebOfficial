from django.contrib import admin

# Register your models here.

from .models import Blog,  TouristType, Tourist, BlogCategory, Role, User

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blogId', 'blogTitle', 'blogAuthor', 'blogDate', 'get_category_name')

    search_fields = ('blogTitle', 'blogAuthor', 'category')

    def get_category_name(self, obj):
        return obj.category.categoryName

class TouristAdmin(admin.ModelAdmin):
    list_display = ( 'touristName', 'touristLocation', 'get_type')

    def get_type(self, obj):
        return obj.type.typeName

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('categoryId', 'categoryName', 'categoryCount')

    search_fields = ('categoryName',)
    list_filter = ('categoryName', 'categoryCount')
    ordering = ('-categoryCount',)
    
class RoleAdmin(admin.ModelAdmin):
    list_display = ('roleId', 'roleName')

class TouristTypeAdmin(admin.ModelAdmin):
    list_display = ('typeId', 'typeName', 'typeCount')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'userBirthyear', 'userPhone', 'blogCount')

    search_fields = ('username',)
    list_filter = ('username', 'blogCount')
    ordering = ('-blogCount',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(TouristType, TouristTypeAdmin)
admin.site.register(Tourist, TouristAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Role, RoleAdmin)
