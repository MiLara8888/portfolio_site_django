from django.shortcuts import render, get_object_or_404
from .models import *


def all_blogs(request):
    blogs = Blog.objects.order_by('-time_create')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog,
                             pk=blog_id)  # ищет объект под нужным номером или 404 передаем имя класса и первичный ключ(по чему ищем)

    return render(request, 'blog/detail.html', {'blog': blog})
