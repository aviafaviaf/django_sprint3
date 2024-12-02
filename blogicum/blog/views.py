from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Post, Category
from django.utils.timezone import localdate
from django.http import HttpResponseNotFound


class HomePage(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(
            pub_date__lte=localdate(),
            is_published=True,
            category__is_published=True).order_by('id')[:5]
        return context


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(Category, slug=category_slug)
    post_list = Post.objects.filter(
        pub_date__lte=localdate(),
        is_published=True,
        category__slug=category_slug).order_by('id')
    context = {
        'category': category,
        'post_list': post_list
    }
    if category.is_published:
        return render(request, template_name, context)
    return HttpResponseNotFound()


def post_detail(request, id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post
    }
    if post.is_published and post.category.is_published and post.pub_date.date() <= localdate():
        return render(request, template_name, context)
    return HttpResponseNotFound()
