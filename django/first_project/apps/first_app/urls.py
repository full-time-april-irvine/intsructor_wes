from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/(?P<color>\w+)/$', views.index, name="index")
]