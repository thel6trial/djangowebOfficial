from django.db import models

from django.db import models

class TouristType(models.Model):
    typeId = models.AutoField(primary_key=True)
    typeName = models.CharField(max_length=45, null=True, default=None)
    typeCount = models.IntegerField(null=True, default=None)

    class Meta:
        db_table = "tourist_type_seq"
        

class Tourist(models.Model):
    tourist_id = models.AutoField(primary_key=True)
    
    touristName = models.CharField(max_length=45, null=True, default=None)
    touristDescription = models.TextField()
    touristLocation = models.CharField(max_length=45, null=True, default=None)
    touristImage = models.ImageField(upload_to='images/', null=True, blank=True)

    type = models.ForeignKey(TouristType, on_delete=models.CASCADE)

    class Meta:
        db_table = "tourist_seq"

class BlogCategory(models.Model):
    categoryId = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=45, null=True, default=None)
    categoryCount = models.IntegerField(null=True, default=None)

    class Meta:
        db_table = "blog_category_seq"

class Role(models.Model):
    roleId = models.AutoField(primary_key=True)
    roleName = models.CharField(max_length=45, null=True, default=None)

    class Meta:
        db_table = "role_seq"

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    
    userName = models.CharField(max_length=45, null=True, default=None)
    userPassword = models.CharField(max_length=45, null=True, default=None)
    userBirthyear = models.IntegerField(null=True, default=None)
    userPhone = models.CharField(max_length=45, null=True, default=None)

    role = models.ForeignKey('Role', on_delete=models.CASCADE)

    class Meta:
        db_table = "user_seq"

class Blog(models.Model):
    blogId = models.AutoField(primary_key=True)
    
    
    blogTitle = models.CharField(max_length=45, null=True, default=None)
    blogDate = models.DateTimeField()
    blogAuthor = models.CharField(max_length=45, null=True, default=None)
    blogContent = models.TextField(null=True, default=None)
    blogImage = models.ImageField(upload_to='images/', null=True, blank=True)

    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "blog_seq"
