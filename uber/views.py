from django.shortcuts import render

# Create your views here.
from . import models

def Post_Shufu(request):
    model = models.HelloForm(request.GET or None)
    if form.is_valid():
        message = 'データ検証に成功しました'
    else:
        message = 'データ検証に失敗しました'
    d = {
        'form': model,
        'message': message,
    }
    return render(request, 'forms.html', d)