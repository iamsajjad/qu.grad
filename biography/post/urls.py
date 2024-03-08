
from django.urls import path
from post.views import post, getpost

urlpatterns = (
    path('', post, name='post'),
    path('<str:pid>', getpost, name='getpost'),
)

