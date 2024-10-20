from django.db import models
from django.contrib.auth.models import User

# auto-generated
# auto incrementiong
# integer
# not null



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fathers_name = models.CharField(max_length=25)
    melicode = models.CharField(max_length=10)
    image = models.ImageField(upload_to='profiles/images', blank=True, null=True)

    def __str__(self):
        return self.user.username



# Profile.objects.get(id=1)
# Profile.objects.get(melicode=12312412)


# class MyTestModel(models.Model):
#     id = models.BigAutoField()
#     my_id = models.BigAutoField()

