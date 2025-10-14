from django.urls import path
from . import views
from .views import SignUpView

app_name= 'tweetapp'

urlpatterns = [
    path('',views.listtweet,name='listtweet'), 
    #atil.com/tweetapp
    path('addtweet/',views.addtweet,name='addtweet'),
    #atil.com/tweetapp/addtweet
    path('addtweetbyform',views.addtweetbyform,name='addtweetbyform'),
    path('addtweetbymodelform',views.addtweetbymodelform,name='addtweetbymodelform'),
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path("deletetweet/<int:id>",views.deletetweet, name="deletetweet")

]
