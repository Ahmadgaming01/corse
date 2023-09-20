from django.urls import path
from .views import re_corse_list
app_name = 'corses'

urlpatterns = [
    path ('/corse' , re_corse_list )
]
