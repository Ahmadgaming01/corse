from django.urls import path
from .views import re_corse_list , re_corse_detail ,re_category_list
from .api import CorseListAPI , CorseDetailAPI , CategoryListAPI , CategoryDetailAPI
app_name = 'corses'

urlpatterns = [
    path ('' , re_corse_list ),
    path ('corse/<int:corse_id>/detail' , re_corse_detail ),
    path('corse/category' , re_category_list),
    #----api url -----------#
    path('corse/list',CorseListAPI.as_view ()),
    path ('corse/<int:pk>' , CorseDetailAPI.as_view ()),
    path ('category/list' , CategoryListAPI.as_view () ),
    path ('category/list/<int:pk>' , CategoryDetailAPI.as_view () ),
]
