from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    # path('detail/<int:pk>', views.post_detail, name='article_detail'),
    # path('detail/<int:pk>/<int:number>', views.post_detail, name='article_detail'),
    # path('detail/<str:title>', views.post_detail, name='article_detail'),
    path('detail/<slug:slug>', views.article_detail, name='article_detail'),
    # path('detail/<str:slug>', views.post_detail, name='article_detail'),
    path('list', views.article_list, name='article_list'),
    path('category/<int:pk>', views.category_detail, name='category_detail'),
    path('search/', views.search, name='search_articles'),
    path('contactus', views.contactus, name='contact_us'),
    path('testbase', views.TestBaseView.as_view(), name='test_base'),
    path('reza', views.HelloToReza.as_view(), name='test_reza'),
    path('karim', views.HelloToKarim.as_view(), name='test_karim'),
]