from django.shortcuts import render , redirect
from .models import Category , Corse , Review


def re_corse_list (request):
    data = Corse.objects.all()
    return render(request , 'corses/corse_list.html', {'corse_list':data})

def re_corse_detail (request , corse_id):
    data = Corse.objects.get (id=corse_id)
    return render (request , 'corses/corse_detail.html' , {'corse_detail':data})
