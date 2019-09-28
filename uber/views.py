from django.shortcuts import render
from .form import PostSyufuForm
# Create your views here.
from .models import PostSyufu


def Post_Shufu(request):
    syufus = PostSyufu.objects.all()
    return render(request, 'uber/syufu_form.html', {'syufus': syufus})


def post_new(request):
    form = PostSyufuForm()
    return render(request, 'uber/post_edit.html', {'form': form})
