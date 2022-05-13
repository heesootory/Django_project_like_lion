from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required

from .forms import PostCreateForm
from .forms import PostBaseForm
from .models import Post
# Create your views here.


def index(request):
    post_list = Post.objects.all().order_by('-created_at')
    context = {
        'post_list': post_list,
    }
    return render(request, 'index.html', context)


def post_list_view(request):
    # post_list = Post.objects.all()
    post_list = Post.objects.filter(writer=request.user)
    context = {
        'post_list': post_list,
    }
    return render(request, 'posts/post_list.html', context)


def post_detail_view(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return redirect('index')
    context = {
        'post': post,
    }

    return render(request, 'posts/post_detail.html', context)


@login_required
def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'posts/post_form.html')
    else:
        image = request.FILES.get('image')
        content = request.POST.get('content')
        print(image)
        print(content)
        Post.objects.create(
            image=image,
            content=content,
            writer=request.user,
        )
        return redirect('index')


def post_create_form_view(request):
    if request.method == 'GET':
        form = PostCreateForm()
        context = {'form': form}
        return render(request, 'posts/post_form2.html', context)
    else:
        form = PostCreateForm(request.POST, request.FILES)

        if form.is_valid():
            Post.objects.create(
                image=form.cleaned_data['image'],
                content=form.cleaned_data['content'],
                writer=request.user,
            )
        else:
            return redirect('posts:post-create')
        return redirect('index')


@ login_required
def post_update_view(request, id):
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)
    if request.method == 'GET':
        context = {'post': post}
        return render(request, 'posts/post_form.html', context)
    elif request.method == 'POST':
        new_image = request.FILES.get('image')
        content = request.POST.get('content')
        print(new_image)
        print(content)

        if new_image:
            post.image.delete()
            post.image = new_image
        post.content = content
        post.save()
        return redirect('posts:post-detail', post.id)


@ login_required
def post_delete_view(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'GET':
        context = {'post': post}
        return render(request, 'posts/post_confirm_delete.html', context)
    else:
        post.delete()
        return redirect('index')
