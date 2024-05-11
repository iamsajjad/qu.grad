
from django.urls import path
from post.views import post, getpost

urlpatterns = (
    path('posts/', post, name='post'),
    path('<str:pid>', getpost, name='getpost'),
)

