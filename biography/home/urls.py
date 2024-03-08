
from django.urls import path
from home.views import homepage, linkspage, language, notfound

urlpatterns = (
    path('', homepage, name='homepage'),
    path('links', linkspage, name='linkspage'),
    path('language/<path:pagepath>', language, name='language'),
    path('notfound/', notfound, name='notfound'),
)

