from django.contrib import admin
from .models import Category , Corse , Review
# Register your models here.


admin.site.register(Corse)
admin.site.register(Category)
admin.site.register(Review)