from .serializers import CorseSerializer , CategorySerializer
from .models import Corse , Category , Review
from rest_framework import generics
from rest_framework.decorators import api_view


class CorseListAPI (generics.ListAPIView):
    queryset = Corse.objects.all()
    serializer_class=CorseSerializer

class CorseDetailAPI (generics.RetrieveAPIView):
    queryset = Corse.objects.all ()
    serializer_class = CorseSerializer