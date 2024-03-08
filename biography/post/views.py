from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from post.forms import PostForm, DeletePostForm
from settings.models import Settings
from post.models import Post

# Create your views here.

@login_required
def post(request):

    if request.method == 'POST':

        post = PostForm(request.POST)

        if post.is_valid():

            post = post.save(commit=False)
            post.owner = request.user
            post.save()

    return redirect('homepage')

def getpost(request, pid):

    settings = Settings.objects.filter(user=request.user.id)

    if len(settings) != 0:
        settings = settings[0]

    post = Post.objects.filter(id=pid)

    if len(post) == 0:
        return redirect('notfound')
    else:
        post = post[0]

    # footer status informations
    status = {'posts':Post.objects.count(), }

    response = {
        'settings': settings,
        'post': post,
        'status': status,
    }
    return render(request, 'post.html', response)

