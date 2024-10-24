from django.shortcuts import render, redirect
from django.template.defaultfilters import title
from django.views.generic import CreateView
from blog.models import Article, New
from django.urls import reverse

def home(request):
    articles = Article.objects.all() #Manager
    # print(reverse('blog:article_detail', args=[2]))
    # print(reverse('blog:article_detail', kwargs={'pk': 11}))
    # return redirect('/articles/detail/2')
    # return redirect(reverse(''))
    # reverse(args[1, 69])
    # reverse(kwargs={'number : 3, 'pk : 1})
    # art = Article.objects.get(id=11)
    # print(art.get_absolute_url())

    # print(Article.objects.counter())

    # articles = Article.objects.published()
    # articles = Article.custom_manager.all()

    # articles = Article.articles.all() #Manager
    # articles = Article.objects.get(title='python')
    # articles = Article.objects.all()
    # art = Article.objects.get(title='python') #READ
    # # print(art.title)
    # art.title = 'java 2' #UPDATE
    # art.save()

    # articles = Article.objects.filter(status=True)
    # print(type(articles))

    # articles = Article.objects.filter(status=True)
    # articles[:5]
    # Lazy evaluation

    # obj = New(title='jafar', des='jafar is a good guy')
    # obj.save()

    # obj = New(id=2)
    # obj.title = 'farid rezaei asle ahwzie gol abadi'
    # obj.save()

    # article = Article.objects.get(id=10)
    # # article.myfile = bytes('hello codeyad', 'utf-8')
    # article.myfile = 'hello codeyad'.encode()
    # article.save()
    # print(article.myfile)
    # print(type(article.myfile))
    # print((article.myfile).decode())
    return render(request, "home/home.html", {'articles':articles})

# GRUD
#
# Create
# Read
# Update
# Delete
