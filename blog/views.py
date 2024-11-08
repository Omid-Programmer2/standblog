from lib2to3.fixes.fix_input import context

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.template.defaultfilters import title

from blog.models import Article, Category, Comment,Message
from django.core.paginator import Paginator
from .forms import ContactUsForm, MessageForm
from django.views.generic.base import View, TemplateView, RedirectView
from django.views.generic import ListView, DetailView,FormView
from django.urls import reverse, reverse_lazy

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
    # return render(request, "blog/article_list.html", {"articles": articles, "name": "ghazanfar"})
    return render(request, "blog/article_list.html", {"articles": objects_list})

def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    # articles = category.article_set.all()
    articles = category.articles.all()
    # articles = category.articles.+.all()
    return render(request, "blog/article_list.html", {'articles': articles})



def search(request):
    q = request.GET.get('q')
    # amir
    # Amir
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    objects_list = paginator.get_page(page_number)
    # return render(request, "blog/article_list.html", {'articles': articles})
    return render(request, "blog/article_list.html", {'articles': objects_list})

    # contains --> case sensitive
    # icontains --> case insensitive


def contactus(request):
    if request.method == 'POST':
        # form = ContactUsForm(data=request.POST)
        form = MessageForm(data=request.POST)
        if form.is_valid():
            # print(form.cleaned_data['text'])
            # print(form.cleaned_data['name'])
            # title = form.cleaned_data['title']
            # title = form.cleaned_data.get('title')
            # text = form.cleaned_data['text']
            # email = form.cleaned_data['email']
            # Message.objects.create(title=title, text=text, email=email)
            # form.save()
            instance =  form.save(commit=True)
            # instance.age += 5
            # instance.save()
            # instance.bmi = instance.weight * instance.height

            # print(form.cleaned_data['birth_year'])
            # print(type(form.cleaned_data['birth_year']))
            # print(form.cleaned_data['birth_year'].year)
            # print(form.cleaned_data['colors'])
            # return redirect('home_app:home')
    else:
        # form = ContactUsForm()
        form = MessageForm()
    return render(request, "blog/contact_us.html", {'form': form})



# class TestBaseView(View):
#     name = "amir"
#     def get(self, request):
#         return HttpResponse(self.name)
#
#     # def post(self, request):
#     #     return HttpResponse(self.name)


# class HelloToReza(TestBaseView):
#     name = "reza"
#
# class HelloToKarim(TestBaseView):
#     name = "karim"



# class ListView(View):
#     queryset = None
#     template_name = None
#
#     def get(self, request):
#         return render(request, self.template_name, {'object_list': self.queryset})
#         # return render(request, self.template_name, {'articles': self.queryset})


# class ArticleList(ListView):
#     queryset = Article.objects.all()
#     # template_name = "blog/article_list.html"
#     template_name = "blog/article_list2.html"

class HomePageRedirect(RedirectView):
    # url = "/"
    # url = "/articles/list"
    # pattern_name = 'blog:article_list'
    # pattern_name = 'home_app:home'
    # pattern_name = 'blog:article_list'
    pattern_name = 'blog:article_detail'
    # permanent = True
    query_string = False

    def get_redirect_url(self, *args, **kwargs):
        print("amir")
        print(self.request.user)
        print(self.request.user.username)
        return super().get_redirect_url(*args, **kwargs)

class ArticleList(TemplateView):
    # template_name = "blog/article_list2.html"
    pass

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['object_list'] = Article.objects.all()
    #     return context

class UserList(ListView):
    queryset = User.objects.all()
    template_name = "blog/user_list.html"



class ArticleDetailView(DetailView):
    model = Article
    # template_name = "blog/article_detail2.html"
    # context_object_name = 'art'
    # slug_field = 'karim'
    # slug_url_kwarg = "item_slug"
    # pk_url_kwarg = 'id'
    # queryset = Article.objects.filter(published=True)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['name'] = "amirhossein"
    #     return context


class ArticleListView(ListView):
    model = Article
    template_name = "blog/article_list.html"
    context_object_name = 'articles'
    paginate_by = 1
    queryset = Article.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "amirhossein"
        return context


class ContactUsView(FormView):
    template_name = "blog/contact_us.html"
    form_class = MessageForm
    # success_url = '/'
    # success_url = reverse("home_app:home")
    success_url = reverse_lazy("home_app:home")

    def form_valid(self, form):
        form_data = form.cleaned_data
        # Message.objects.create(title=form_data['title'])
        Message.objects.create(**form_data)
        # print(form_data['title'])
        return super().form_valid(form)