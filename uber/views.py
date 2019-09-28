from django.shortcuts import render

# Create your views here.
from . import models

def Post_Shufu(request):
    return render(request, 'uber/syufu_form.html', {})
