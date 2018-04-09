from django.shortcuts import render, get_object_or_404

from .models import Blog


def allblogs(request):
    allblogs = Blog.objects.all()
    return render(request, 'blog/blog.html', {'allblogs': allblogs})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'blog/detail.html', {'blog': blog})
