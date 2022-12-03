from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator

def post_list(request):
    """Class for shoving posts"""

    posts = Post.objects.filter(status__in = [2])
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    
    context = {
        'object_list_posts': page_object,
    }
    
    return render(request, 'cv_blog/post_list.html', context)

def post_atributes(request, get_slug):
    """Class for getting post to slugs"""

    post = get_object_or_404(Post, slug = get_slug)
    context = {
        'object' : post
    }

    return render(request, 'cv_blog/post_atributes.html', context)