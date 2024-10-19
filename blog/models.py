from django.db import models
from django.contrib.auth.models import User
from django.db.models import SET_DEFAULT, PROTECT, DO_NOTHING


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

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # author = models.ForeignKey(User, on_delete=SET_DEFAULT, default='1')
    # author = models.ForeignKey(User, on_delete=PROTECT)
    # author = models.ForeignKey(User, on_delete=DO_NOTHING)
    title = models.CharField(max_length=70)
    body = models.TextField()
    image = models.ImageField(upload_to='images/articles')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.body[:30]}"
