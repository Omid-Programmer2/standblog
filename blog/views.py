from django.shortcuts import render, get_object_or_404
from blog.models import Article



# def post_detail(request, title):
def post_detail(request, slug):
    # print(type(slug))
    # article = Article.objects.get(id=pk)
    article = get_object_or_404(Article, slug=slug)
    return render(request, "blog/article_detail.html", {"article": article})
