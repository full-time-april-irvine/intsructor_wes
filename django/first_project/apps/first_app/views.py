from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'first_app/index.html')