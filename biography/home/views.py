from random import sample

from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.cache import cache_page
from django.http import HttpResponseRedirect
from django.utils import translation

from settings.models import Settings
from bio.models import Bio
from post.models import Post

# Create your views here.

@cache_page(0)
def homepage(request):

    response = {}

    posts = Post.objects.order_by('-id')[:10]

    response = {
        'posts': posts,
    }

    if not request.user.is_anonymous:
        response['settings'] = get_object_or_404(Settings, user=request.user)

        # footer status informations
        response['status'] = {'bios':Bio.objects.count(), }

    return render(request, 'home.html', response)

@cache_page(0)
def linkspage(request):

    response = {}

    if not request.user.is_anonymous:
        response['settings'] = get_object_or_404(Settings, user=request.user)

        # footer status informations
        response['status'] = {'bios':Bio.objects.count(), }

    return render(request, 'linkspage.html', response)

@cache_page(0)
def language(request, pagepath):

    if pagepath.startswith('/en/'):
        return HttpResponseRedirect(pagepath.replace('en', 'ar', 1))
    elif pagepath.startswith('/ar/'):
        return HttpResponseRedirect(pagepath.replace('ar', 'en', 1))
    else:
        return HttpResponseRedirect('/en/')

def notfound(request):

    response = {}

    return render(request, 'error/notfound.html', response)

