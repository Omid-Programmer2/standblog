from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    # path('detail/<int:pk>', views.post_detail, name='article_detail'),
    # path('detail/<int:pk>/<int:number>', views.post_detail, name='article_detail'),
    # path('detail/<str:title>', views.post_detail, name='article_detail'),
    path('detail/<slug:slug>', views.post_detail, name='article_detail'),
    # path('detail/<str:slug>', views.post_detail, name='article_detail'),

]