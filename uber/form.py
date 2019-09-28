from django import forms
from .models import PostSyufu


class SyufuLogin(forms.ModelForm):

    class Meta:
        model = PostSyufu
        fields = ('shufu_name', 'email')


class SyfuSignUp(forms.ModelForm):
    class Meta:
        model = PostSyufu
        fields = ('id_member', 'shufu_name', 'email')