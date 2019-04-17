from django.shortcuts import render, redirect
from .models import Tweet
# Create your views here.
def index(req):
    if 'user_id' not in req.session:
        return redirect('/users/new')

    context = {
        "tweets": Tweet.objects.order_by('-created_at')
    }
    return render(req, 'tweets/index.html', context)