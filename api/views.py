from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, Restaurant,Rating
from .serializers import CustomerSerializer,RestaurantSerializer,RatingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication,BasicAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated
#from django.contrib.auth.models  import User

class CustomerViweSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset=Restaurant.objects.all()
    serializer_class=RestaurantSerializer

    authentication_classes=(BasicAuthentication,)
    permission_classes=(IsAuthenticated,)

@action(method=['post'],detail=True)
def rat_restaurant(self,request,id):
    if stars in request.data:
        restaurant= Restaurant.objects.get(id=id)
        stars=request.data['stars']
        #user=request.data['user']
        #username=Rating.objects.get(user=user)
        #username=requset.username
        customer=request.data['customer']
        cust=Customer.objects.get(customer=customer)
        try:
            rating=Rating.objects.get(cust=cust.id, restaurant=restaurant.id,)
            rating.stars=stars
            rating.save()
            serializer=RatingSerializer(rating,many=False)          
            json={
                'message':'we update of stars',
                "resulr":serializer.data 
            }
            return Response(json)
        except:
            rating=Rating.objects.create(stars=stars,restaurant=restaurant, customer=customer)
            serializer=RatingSerializer(rating,many=true)
            json={
                'message':'we create of stars',
                "resulr":serializer.data 
            }
            return Response(json)
    else:
        json={
            'message':'there isnot stars'
        }
        return Response(json)

class RatingViewSet(viewsets.ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class=RatingSerializer 

    authentication_classes=(BasicAuthentication,)
    permission_classes=(IsAuthenticated,)

    def update(self,request,*arg,**kwargs):

        json={
            'message':'you canot update in this def',
        }
        return Response (json)

    def creat(self,request,*arg,**kwargs):

        json={
            'message':'you canot create in this def',
        }
        return Response (json)