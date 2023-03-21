from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    post_date = models.DateTimeField()
    author = models.ForeignKey(User, verbose_name="author", related_name="author", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="chat/images", default="")
    def __str__(self):
        return self.title[0:7] + "..."