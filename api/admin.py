from django.contrib import admin
from .models import Restaurant,Rating,Customer
 #Register your models here.
admin.site.register(Customer)
admin.site.register(Restaurant)
admin.site.register(Rating)