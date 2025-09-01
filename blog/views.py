from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from .models import Post, Category

def post_list(request):
    search_query = request.GET.get('q', '')
    category_filter = request.GET.get('category', '')

    posts = Post.objects.all()

    if search_query:
        posts = posts.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))

    if category_filter:
        posts = posts.filter(category__name__iexact=category_filter)

    paginator = Paginator(posts.order_by('-published_date'), 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {
        'page_obj': page_obj,
        'categories': categories,
        'search_query': search_query,
        'category_filter': category_filter
    })
