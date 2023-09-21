from django.urls import path
from .views import re_corse_list , re_corse_detail
from .api import CorseListAPI , CorseDetailAPI
app_name = 'corses'

urlpatterns = [
    path ('' , re_corse_list ),
    path ('corse/<int:corse_id>/detail' , re_corse_detail ),
    path('corse/list',CorseListAPI.as_view ()),
    path ('corse/<int:pk>' , CorseDetailAPI.as_view ()),
]
