from django.urls import path
from .views import re_corse_list , re_corse_detail
app_name = 'corses'

urlpatterns = [
    path ('' , re_corse_list ),
    path ('/corse/<int:corse_id>/detail' , re_corse_detail )
]
