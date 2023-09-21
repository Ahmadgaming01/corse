from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Corse (models.Model):
    user = models.ForeignKey (User , related_name='corse_user' , on_delete= models.CASCADE)
    name = models.CharField (max_length= 200)
    description = models.TextField(max_length=10000)
    image = models.ImageField (upload_to= 'image')
    video = models.URLField (blank=True , null=True)
    created_at = models.DateTimeField(timezone.now)
    price = models.FloatField()
    category = models.ForeignKey('Category' , related_name='category_corse', on_delete= models.CASCADE)
    def __str__(self) :
        return self.name


class Category (models.Model):

    name = models.CharField (max_length= 100)
    image = models.ImageField (upload_to= 'CatImage')
    def __str__(self) :
        return self.name

class Review(models.Model):
    corse = models.ForeignKey (Corse , related_name='review_cose',on_delete= models.CASCADE)
    review = models.TextField (max_length=10000)
    rate = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator (5)])
    created_at = models.DateTimeField(timezone.now)
    user = models.ForeignKey (User , related_name='review_user' , on_delete= models.CASCADE)
    def __str__(self) :
        return str(self.corse)