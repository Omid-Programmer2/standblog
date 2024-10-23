from django.db import models
from django.contrib.auth.models import User
from django.db.models import SET_DEFAULT, PROTECT, DO_NOTHING
from django.utils import timezone


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
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    # title = models.CharField(max_length=70, unique_for_date='pub_date')
    # title = models.CharField(max_length=70, primary_key=True)
    title = models.CharField(max_length=70)
    body = models.TextField()
    image = models.ImageField(upload_to='images/articles')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pub_date = models.DateField(default=timezone.now())

    # myfile = models.BinaryField(null=True)
    myfile = models.FileField(upload_to='test', null=True)
    status = models.BooleanField(default=True)
    # objects = models.Manager()
    # articles = models.Manager()
    published = models.BooleanField(default=True)
    # objects = ArticleManager()

    objects = models.Manager()
    custom_manager = ArticleManager()

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
    floatfield = models.FloatField(default=1)



    def __str__(self):
        return f"{self.title} - {self.body[:30]}"

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):

    def save(self, *args, **kwargs):
        print('hello')
        super(Article, self).save(args, kwargs)

class MyTest(models.Model):
    title = models.CharField(max_length=50, primary_key=True)


class New(models.Model):
    title = models.CharField(max_length=30)
    des = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.replace(' ', '-')
        super(New, self).save(args, kwargs)