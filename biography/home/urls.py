
from django.urls import path
from home.views import homepage, linkspage, graduates, language, notfound

urlpatterns = (
    path('', homepage, name='homepage'),
    path('links', linkspage, name='linkspage'),
    path('graduates/', graduates, name='graduates'),
    path('language/<path:pagepath>', language, name='language'),
    path('notfound/', notfound, name='notfound'),
)

