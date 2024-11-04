from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article, Category, Comment
from django.core.paginator import Paginator
from .forms import ContactUsForm


# def post_detail(request, title):
def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        # parent_id = 5
        parent_id = request.POST.get('parent_id')
        body = request.POST['body']
        # Comment.objects.create(body=body, article=article, user=request.user)
        Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)
    # print(type(slug))
    # article = Article.objects.get(id=pk)
    return render(request, "blog/article_detail.html", {"article": article})


def article_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    print(page_number)
    paginator = Paginator(articles, 1)
    # object_list = paginator.get_page(2)
    objects_list = paginator.get_page(page_number)
    # return render(request, "blog/articles_list.html", {"articles": articles, "name": "ghazanfar"})
    return render(request, "blog/articles_list.html", {"articles": objects_list})

def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    # articles = category.article_set.all()
    articles = category.articles.all()
    # articles = category.articles.+.all()
    return render(request, "blog/articles_list.html", {'articles': articles})



def search(request):
    q = request.GET.get('q')
    # amir
    # Amir
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    objects_list = paginator.get_page(page_number)
    # return render(request, "blog/articles_list.html", {'articles': articles})
    return render(request, "blog/articles_list.html", {'articles': objects_list})

    # contains --> case sensitive
    # icontains --> case insensitive


def contactus(request):
    if request.method == 'POST':
        form = ContactUsForm(data=request.POST)
        if form.is_valid():
            # print(form.cleaned_data['text'])
            print(form.cleaned_data['name'])
            # return redirect('home_app:home')
    else:
        form = ContactUsForm()
    return render(request, "blog/contact_us.html", {'form': form})
