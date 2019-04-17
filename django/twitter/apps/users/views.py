from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def new(req):
    return render(req, 'users/new.html')

def create(req):
    # send form to models
    errors = User.objects.validate(req.POST)
    # decide what to do based on result
    if errors:
        for error in errors:
            messages.error(req, error)
        return redirect('/users/new')
    # create the user in the db
    user_id = User.objects.easy_create(req.POST)
    # log them in
    req.session['user_id'] = user_id
    return redirect('/')