from django.urls import path
from . import views

# /articles
app_name = 'blog'
urlpatterns = [
    # path('detail/<int:pk>', views.post_detail, name='article_detail'),
    # path('detail/<int:pk>/<int:number>', views.post_detail, name='article_detail'),
    # path('detail/<str:title>', views.post_detail, name='article_detail'),
    # path('detail/<slug:slug>', views.article_detail, name='article_detail'),
    path('detail/<slug:slug>', views.ArticleDetailView.as_view(), name='article_detail'),
    # path('detail/<int:pk>', views.ArticleDetailView.as_view(), name='article_detail'),
    # path('detail/<slug:item_slug>', views.ArticleDetailView.as_view(), name='article_detail'),
    # path('detail/<int:id>', views.ArticleDetailView.as_view(), name='article_detail'),

    # path('detail/<str:slug>', views.post_detail, name='article_detail'),
    # path('list', views.article_list, name='article_list'),
    path('category/<int:pk>', views.category_detail, name='category_detail'),
    path('search/', views.search, name='search_articles'),
    # path('contactus', views.contactus, name='contact_us'),
    # path('contactus', views.ContactUsView.as_view(), name='contact_us'),
    path('contactus', views.MessageView.as_view(), name='contact_us'),
    # path('testbase', views.TestBaseView.as_view(), name='test_base'),
    # path('testbase', views.TestBaseView.as_view(name='reza'), name='test_base'),
    # path('reza', views.HelloToReza.as_view(), name='test_reza'),
    # path('karim', views.HelloToKarim.as_view(), name='test_karim'),
    # path('list', views.ArticleList.as_view(), name='article_list'),
    # path('list', views.ArticleList.as_view(template_name='blog/article_list2.html'), name='article_list'),
    # path('list', views.article_list, name='article_list'),
    path('list', views.ArticleListView.as_view(), name='article_list'),
    path('users', views.UserList.as_view(), name='user_list'),
    # path('red', views.HomePageRedirect.as_view(), name='redirect'),
    path('red/<slug:slug>', views.HomePageRedirect.as_view(), name='redirect'),
    path('messages', views.MessageListView.as_view(), name='messages_list'),
    path('message/edit/<int:pk>', views.MessageUpdateView.as_view(), name='messages_edit'),
    path('message/delete/<int:pk>', views.MessageDeleteView.as_view(), name='messages_delete'),

]