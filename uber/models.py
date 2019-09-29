from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms


# Create your models here.
class SyufuAccounts(models.Model):
    # id_member = models.CharField(max_length=10, primary_key=True)
    shufu_name = models.CharField(max_length=20)
    email = models.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput)

    def publish(self):
        self.save()

    def __str__(self):
        return self.shufu_name


class Recipi(models.Model):

    recipi_id = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.IntegerField()
    url = models.CharField(max_length=100)
    person_id = models.ForeignKey('SyufuAccounts', on_delete=models.CASCADE)



class PostUser(models.Model):
    user_name = models.CharField(
        max_length=20
    )

    user_email = models.EmailField()
    user_phone = models.IntegerField(
        default = 0
    )
    user_adress = models.CharField(
        max_length=30
    )

    def publish(self):
        self.save()

    def __str__(self):
        return self.user_name


