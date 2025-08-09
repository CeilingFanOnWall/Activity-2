from django.shortcuts import render, redirect
from .forms import TweetForm

def post_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = TweetForm()
    return render(request, 'tweets/post_tweets.html', {'form': form})

def tweet_success(request):
    return render(request, 'tweets/success.html')