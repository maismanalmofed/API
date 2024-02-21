from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
#from django.contrib.auth.models import User

class Customer (models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
     return self.name 


class Restaurant (models.Model):
    name_restaurant=models.CharField(max_length=50)
    meal_type=models.CharField(max_length=100)
    def __str__(self):
     return self.name_restaurant 

    def num_ofrating(self):#to compute the number of rating for each restaurant
        rate=Rating.objects.filter(restaurant=self)
        return len(rate)

    def avg_ofrating(self):#to compute the average for each restaurant
        sum=0
        rate=Rating.objects.filter(restaurant=self)
        for rat in rate:
            sum+=rat.stars
        if len(rate) > 0:
            return sum / len(rate)     
        else:
            return 0



class Rating (models.Model):
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,default=True)
    stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    #user=models.CharField(max_length=50)


    class Meta:
        unique_together=(('customer','restaurant'))
        index_together=(('customer','restaurant'))


