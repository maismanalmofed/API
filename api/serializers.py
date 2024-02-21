from rest_framework import serializers
from.models import Customer, Rating,Restaurant
#from django.contrib.auth.models import User



class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Restaurant
        fields=['name_restaurant','meal_type','num_ofrating','avg_ofrating']



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['name']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields=['customer','restaurant','stars']       