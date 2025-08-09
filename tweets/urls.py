from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_tweet, name='post_tweets'),
    path('success/', views.tweet_success, name='success'),
]