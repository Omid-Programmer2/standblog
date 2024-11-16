from django.db import models
from django.contrib.auth.models import User
from django.db.models import SET_DEFAULT, PROTECT, DO_NOTHING, IntegerField
# from django.utils import timezone
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html
from django.utils.text import slugify


# article to user
# ManyToOne ==> this is what we want
# ManyToMany
# OneToOne
# each article has only one author
# each user can have several article

# cascade
# set null

# protect
# set default

# do nothing

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class ArticleManager(models.Manager):
    # def counter(self):
    #     return len(self.all())
    #
    # def published(self):
    #     return self.filter(published=True)

    def get_queryset(self):
        return super(ArticleManager, self).get_queryset().filter(status=True)

class Article(models.Model):
    CHOICES = (
        ('A', 'پایتون'),
        ('B', 'جنگو')
    )

    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # author = models.ForeignKey(User, on_delete=SET_DEFAULT, default='1')
    # author = models.ForeignKey(User, on_delete=PROTECT)
    # author = models.ForeignKey(User, on_delete=DO_NOTHING)
    # title = models.CharField(max_length=70, help_text="Enter a valid title", unique=True)
    # title = models.CharField(max_length=70, help_text="Enter a valid title", unique=True, db_column="mytitle")
    # title = models.CharField(max_length=70, editable=False)
    # title = models.CharField(max_length=70, choices=CHOICES, default='A')

    # id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', verbose_name="نویسنده مقاله")
    category = models.ManyToManyField(Category, related_name='articles', verbose_name="دسته بندی")
    # category = models.ManyToManyField(Category, related_name='+')
    # title = models.CharField(max_length=70, unique_for_date='pub_date')
    # title = models.CharField(max_length=70, primary_key=True)
    title = models.CharField(max_length=70, verbose_name="عنوان")
    body = models.TextField()
    image = models.ImageField(upload_to='images/articles', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # pub_date = models.DateField(default=timezone.now())

    # myfile = models.BinaryField(null=True)
    myfile = models.FileField(upload_to='test', null=True)
    status = models.BooleanField(default=True)
    # objects = models.Manager()
    # articles = models.Manager()
    published = models.BooleanField(default=True)
    # objects = ArticleManager()
    pub_date = models.DateTimeField(default=timezone.now())
    objects = models.Manager()
    custom_manager = ArticleManager()
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        ordering = ('-created',)
        # ordering = ('-updated')
        # ordering = ('-updated', '-created')
        # verbose_name = 'post'
        # verbose_name_plural = 'stories'

        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.title)
        super(Article, self).save()

    # is_published = models.BooleanField()

    # article = Article.objects.get(id=16)
    # article.is_published = 0
    # article.save()

    # is_published = models.DateField()
    # is_published = models.TimeField()
    # is_published = models.DateTimeField()
    # is_published = models.DurationField(default=timezone.timedelta(days=23, hours=21, minutes=43, seconds=54))

# article = Article.objects.get(id=17)
# article.is_published.days += 45
# article.save()

# article = Article.objects.get(id=17)
# article.is_published.days -= 1
# article.save()

    # is_published = models.IntegerField()
    # is_published = models.BigIntegerField()

    # is_published = models.EmailField('amir@ma.com')
    # is_published = models.URLField(null=True)
    # floatfield = models.FloatField(default=1)

    def get_absolute_url(self):
        # return reverse('blog:article_detail', args=[str(self.id)])
        return reverse('blog:article_detail', kwargs={'slug':self.slug})

    # def print_title(self):
    #     # print(self.title)
    #     return self.title
    #
    # print_title.short_description = "چاپ عنوان"

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="60px" height="50px">')
        return format_html('<h3 style="color: red">تصویر ندارد</h3>')


    def __str__(self):
        return f"{self.title} - {self.body[:30]}"

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):

    # def save(self, *args, **kwargs):
    #     print('hello')
    #     super(Article, self).save(args, kwargs)

# class MyTest(models.Model):
#     title = models.CharField(max_length=50, primary_key=True)


# class New(models.Model):
#     title = models.CharField(max_length=30)
#     des = models.TextField()
#
#     def __str__(self):
#         return self.title
#
#     def save(self, *args, **kwargs):
#         self.title = self.title.replace(' ', '-')
#         super(New, self).save(args, kwargs)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"


class Message(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    age = IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"