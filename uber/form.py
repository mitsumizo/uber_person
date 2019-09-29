from django import forms
from .models import SyufuAccounts


class Login(forms.ModelForm):
    class Meta:
        model = SyufuAccounts
        fields = ('shufu_name', 'email')


class SignUp(forms.ModelForm):
    class Meta:
        model = SyufuAccounts
        fields = ('shufu_name', 'email')