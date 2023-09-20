from django.shortcuts import render , redirect
from .models import Category , Corse , Review


def re_corse_list (request):
    data = Corse.objects.all()
    return render(request , 'corses/corse_list.html', {'corse_list':data})


