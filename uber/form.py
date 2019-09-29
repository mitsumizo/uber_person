from django import forms
from .models import SyufuAccounts, PostUser


class Login(forms.ModelForm):
    class Meta:
        model = SyufuAccounts
        fields = ('shufu_name', 'email')


class SignUp(forms.ModelForm):
    class Meta:
        model = SyufuAccounts
        fields = ('shufu_name', 'email')

class PostingForm(forms.ModelForm):
    class Meta:
        model = PostUser
        fields = ('user_name','user_email','user_phone','user_adress',)
        widgets = {
            'user_name' : forms.Textarea(attrs={'cols': 40, 'rows': 1}),
            'user_mail' : forms.TextInput(attrs={'cols': 40, 'rows': 4}),
            'user_phone' : forms.TextInput(attrs={'cols': 40, 'rows': 4}),
            'user_adress' : forms.Textarea(attrs={'cols': 40, 'rows': 4}),
        }