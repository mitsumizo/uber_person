from django.shortcuts import render, get_object_or_404, redirect
from .form import Login, SignUp, PostingForm
# Create your views here.
from .models import SyufuAccounts, Recipi
## Create your views here.
from .form import PostUser

# import django.http
# import uber.models
# from django.shortcuts import render
# import uuid
# from django.contrib.auth.models import User
# import re
# from django.contrib.auth import authenticate, login as django_login
#
#


def Top_Page(request):
    syufus = SyufuAccounts.objects.all()
    recipis = Recipi.objects.all()
    return render(request, 'uber/top_page.html', {'syufus': syufus, 'recipis' : recipis})

def login_syufu(request):
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():

            datas = form.save(commit=False)
            datas = SyufuAccounts.objects.filter(shufu_name=datas.shufu_name)
            datas = form.save()
            return redirect('account_detail', pk=datas.pk)

    else:
        form = Login

    return render(request, 'uber/login.html', {'form': form})

def syufu_sign_up(request):
    form = SignUp()
    return render(request, 'uber/sign_up.html', {'form': form})


def account_detail(request, pk):
    post = get_object_or_404(SyufuAccounts, pk=pk)
    return render(request, 'uber/account_detail.html', {'post': post})

def detail_food(request):
    post = Recipi.objects.all()[0]
    return render(request, 'uber/nikujaga_detail.html', {'post': post})


def Form_User(request):
    form = PostingForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()

    users = PostUser.objects.all()
    contexts = {
        'form':form,
        'users':users,
    }
    return render(request, 'uber/user_form.html', contexts)