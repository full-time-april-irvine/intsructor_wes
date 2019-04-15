from django.shortcuts import render, redirect

# Create your views here.
def index(request, color):
    request.session['thing'] = "Hello World"
    # request.POST
    context = {
        "color": color,
        "title": "Home"
    }
    return render(request, 'first_app/index.html', context)