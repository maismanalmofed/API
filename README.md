project about rating restaurant with using api 


Business requirements :


1- Restaurant list screen has the foloowing information - restaurant name - restaurant number of stars - restaurant average rate - Login - Register - showing already logged in customer

2- Popup error if the customer already rated

3- Add rate scree, stars 1 to 5 only and SAVE




Technical requirements:
Using Django REST frame work please implement the followings

1- Models - restaurant - Stars - customer

2- validation if the customer already rated the restuarant

3- validation to rate min 1 and max 5

4- CRUD API for resaurants http://127.0.0.1:8000/restaurants it should return the average rating and number of rating a long with the restaurant name and detail

5- CRUD API for ratings http://127.0.0.1:8000/ratings/ no one should be able to use this crud for rating !!

6- Rate API http://127.0.0.1:8000/restaurants/restaua_pk/rat_restaurant create and update API

7- Token authentication (restauarnt,rating,customer)

8- Login and register API

9- Token request API


