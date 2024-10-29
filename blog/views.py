from django.shortcuts import render, get_object_or_404
from blog.models import Article, Category


# def post_detail(request, title):
def article_detail(request, slug):
    # print(type(slug))
    # article = Article.objects.get(id=pk)
    article = get_object_or_404(Article, slug=slug)
    return render(request, "blog/article_detail.html", {"article": article})


def article_list(request):
    articles = Article.objects.all()
    return render(request, "blog/articles_list.html", {"articles": articles, "name": "ghazanfar"})

def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    # articles = category.article_set.all()
    articles = category.articles.all()
    # articles = category.articles.+.all()
    return render(request, "blog/articles_list.html", {'articles': articles})

