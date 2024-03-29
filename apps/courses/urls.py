from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r"^courses/destroy/(?P<id>\d+)$", views.confirmation),
    url(r"^destroy/(?P<id>\d+)$", views.destroy)
]
