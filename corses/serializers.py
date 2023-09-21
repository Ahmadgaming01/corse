from rest_framework import serializers
from .models import Corse , Category , Review


class CorseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corse
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    corses =CorseSerializer (source = 'category_corse'  ,many=True)
    class Meta:
        model = Category
        fields = '__all__'
