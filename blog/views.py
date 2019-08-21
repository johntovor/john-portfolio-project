from django.shortcuts import render, get_object_or_404
from .models import MyBlog


def blog(request):
    blogs = MyBlog.objects.all()

    return render(request, 'blog/allblogs.html', {'blogs': blogs})


def detail(request, blog_id):
    detailblog = get_object_or_404(MyBlog, pk=blog_id)

    return render(request, 'blog/detailblog.html', {'detailblog': detailblog})
