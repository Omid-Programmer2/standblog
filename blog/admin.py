from django.contrib import admin
from django.template.defaultfilters import truncatechars

# from .models import Article, Category, MyTest, New
# from .models import Article, Category, MyTest, Comment
from . import models
from .models import Article


# admin.site.register(Article)
# admin.site.register(Category)
# admin.site.register(MyTest)
# # admin.site.register(New)
# admin.site.register(Comment)

class FilterByTitle(admin.SimpleListFilter):
    title = "کلید های پر تکرار"
    parameter_name = "title"

    def lookups(self, request, model_admin):
        return (
            # ("django", "DJANGO"),
            ("django", "جنگو"),
            # ("python", "PYTHON"),
            ("python", "پایتون"),
        )

    def queryset(self, request, queryset):
        if self.value():
            print(self.value())
            return queryset.filter(title__icontains=self.value())

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    # list_display = ('title', 'body', 'status')
    # list_display = ("__str__", "status")
    # list_display = ("__str__", "title", "status", "print_title")
    list_display = ("__str__", "title", "status", "show_image")
    # list_editable = ("title", "status")
    list_editable = ("title",)
    list_filter = ("status", "published", FilterByTitle)
    search_fields = ("title", "body")
    # fields = ("body", "title")

# admin.site.register(models.Article)
admin.site.register(models.Category)
# admin.site.register(models.MyTest)
# admin.site.register(New)
admin.site.register(models.Comment)
admin.site.register(models.Message)

