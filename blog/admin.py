from django.contrib import admin
# from .models import Article, Category, MyTest, New
from .models import Article, Category, MyTest, Comment

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(MyTest)
# admin.site.register(New)
admin.site.register(Comment)
