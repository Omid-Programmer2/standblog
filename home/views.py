from django.shortcuts import render
from blog.models import Article

def home(request):
    articles = Article.objects.all()
    # article = Article.objects.get(id=10)
    # # article.myfile = bytes('hello codeyad', 'utf-8')
    # article.myfile = 'hello codeyad'.encode()
    # article.save()
    # print(article.myfile)
    # print(type(article.myfile))
    # print((article.myfile).decode())
    return render(request, "home/home.html", {'articles':articles})
