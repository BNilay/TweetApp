from django.urls import path
from . import views

app_name= 'tweetapp'

urlpatterns = [
    path('',views.listtweet,name='listtweet'), 
    #atil.com/tweetapp
    path('addtweet/',views.addtweet,name='addtweet')
    #atil.com/tweetapp/addtweet
]
