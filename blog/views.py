from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CommentForm
from .forms import PostForm


def post(request):
    """ Post A Blog """
    posts = Post.objects.all()

    template = 'blog/blog.html'
    context = {
        'posts': posts,
    }

    return render(request, template, context)


def detail_post(request, slug):
    """ Details on Blog Post """
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.save()
            return redirect('detail_post', slug=post.slug)
    else:
        form = CommentForm()

    template = 'blog/blog_detail.html'
    context = {
        'post': post,
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_blog(request):
    """ Add a blog post to the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Only our STILE team has access to this.')
        return redirect(reverse('homepage'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully added a blog post!')
            return redirect(reverse('detail_post', args=[post.slug]))
        else:
            messages.error(request, 'Failed to add the blog post. Please ensure the form is valid.')
    else:
        form = PostForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, slug):
    """ Edit a Blog Post """
    if not request.user.is_superuser:
        messages.error(request, 'Only our STILE team has access to this.')
        return redirect(reverse('homepage'))

    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog post!')
            return redirect(reverse('detail_post', args=[post.slug]))
        else:
            messages.error(request, 'Failed to update blog post. Please ensure the form is valid.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, slug):
    """ Delete a blog post from the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Only our STILE team has access to this.')
        return redirect(reverse('homepage'))

    blog = get_object_or_404(Post, slug=slug)
    blog.delete()
    messages.success(request, 'Blog post deleted!')
    return redirect(reverse('detail_post'))
