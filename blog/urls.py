# from django.conf.urls import url
from django.template.defaulttags import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]