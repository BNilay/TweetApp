from django.shortcuts import render
from . import models

def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {"tweets":all_tweets}
    return render(request,'tweetapp/listtweet.html')



def addtweet(request):
    if request.POST:
        print(request.POST["nickname"])
    return render(request,'tweetapp/addtweet.html')


