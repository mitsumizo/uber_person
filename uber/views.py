from django.shortcuts import render, get_object_or_404,redirect
from .form import Login, SignUp
# Create your views here.
from .models import SyufuAccounts, Recipi
#
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
#
#
def login_syufu(request):
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():

            datas = form.save(commit=False)
            datas = SyufuAccounts.objects.filter(shufu_name=datas.shufu_name)
            print(datas)
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
#
# def login_user(request):
#     if request.method == 'POST':
#         login_form = uber.forms.SyufuLogin(request.POST)
#         username = login_form.username
#         password = login_form.password
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             django_login(request, user)
#             return django.http.HttpResponseRedirect('uber/syufu_form.html')
#         else:
#             login_form.add_error(None, "ユーザー名またはパスワードが異なります。")
#             return render(request, 'uber/sign_up.html', {'form': login_form})
#         return render(request, 'uber/sign_up.html', {'form': login_form})
#     else:
#         return django.http.HttpResponseRedirect('uber/syufu_form.html')
#     return render(request, 'uber/sign_up.html', {'form': login_form})
