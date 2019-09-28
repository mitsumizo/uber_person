from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class PostSyufu(models.Model):
    id_member = models.CharField(max_length=10, primary_key=True)
    shufu_name = models.CharField(
        max_length=20
    )
    email = models.EmailField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.id_member


class Post_user(models.Model):
    pass