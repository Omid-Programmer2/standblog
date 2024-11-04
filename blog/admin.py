from django.contrib import admin
# from .models import Article, Category, MyTest, New
# from .models import Article, Category, MyTest, Comment
from . import models

# admin.site.register(Article)
# admin.site.register(Category)
# admin.site.register(MyTest)
# # admin.site.register(New)
# admin.site.register(Comment)


admin.site.register(models.Article)
admin.site.register(models.Category)
admin.site.register(models.MyTest)
# admin.site.register(New)
admin.site.register(models.Comment)
admin.site.register(models.Message)

