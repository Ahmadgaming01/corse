from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Corse (models.Model):
    user = models.ForeignKey (User , related_name='corse_user' , on_delete= models.CASCADE)
    name = models.CharField (max_length= 200)
    description = models.TextField(max_length=10000)
    image = models.ImageField (upload_to= 'image')
    created_at = models.DateTimeField(timezone.now)
    price = models.FloatField()
    Category = models.ForeignKey(Category , related_name='category_corse', on_delete= models.CASCADE)



class Category (models.Model):

    name = models.CharField (max_length= 100)
    image = models.ImageField (upload_to= 'CatImage')


class Review(models.Model):
    corse = models.ForeignKey (Corse , related_name='review_cose',on_delete= models.CASCADE)
    review = models.TextField (max_length=10000)
    rate = models.IntegerField(range(1,5))
    created_at = models.DateTimeField(timezone.now)
    user = models.ForeignKey (User , related_name='corse_user' , on_delete= models.CASCADE)
