from django.urls import path
from.views import CustomerViweSet,RestaurantViewSet,RatingViewSet
from django.conf.urls import include
from rest_framework import  routers 


router=routers.DefaultRouter()
router.register('customers',CustomerViweSet)
router.register('ratings',RatingViewSet)
router.register('restaurants',RestaurantViewSet)


urlpatterns = [
    path('',include(router.urls)),
]