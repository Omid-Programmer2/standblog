from django.shortcuts import render
from django.template.defaultfilters import title
from blog.models import Article, New

def home(request):
    articles = Article.objects.all()
    # obj = New(title='jafar', des='jafar is a good guy')
    # obj.save()

    obj = New(id=2)
    obj.title = 'farid rezaei asle ahwzie gol abadi'
    obj.save()

    # article = Article.objects.get(id=10)
    # # article.myfile = bytes('hello codeyad', 'utf-8')
    # article.myfile = 'hello codeyad'.encode()
    # article.save()
    # print(article.myfile)
    # print(type(article.myfile))
    # print((article.myfile).decode())
    return render(request, "home/home.html", {'articles':articles})
