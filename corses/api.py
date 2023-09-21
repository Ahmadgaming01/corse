from .serializers import CorseSerializer , CategorySerializer , CategoryDetailSerializer
from .models import Corse , Category , Review
from rest_framework import generics
from rest_framework.decorators import api_view


class CorseListAPI (generics.ListAPIView):
    queryset = Corse.objects.all()
    serializer_class=CorseSerializer

class CorseDetailAPI (generics.RetrieveAPIView):
    queryset = Corse.objects.all ()
    serializer_class = CorseSerializer

class CategoryListAPI (generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class= CategorySerializer


class CategoryDetailAPI (generics.RetrieveAPIView):
    queryset = Category.objects.all ()
    serializer_class = CategoryDetailSerializer