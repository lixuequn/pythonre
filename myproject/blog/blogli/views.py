#!/usr/bin/env python
# coding=utf-8
from django.shortcuts import render
from blogli.models import *
from django.shortcuts import render_to_response

# Create your views here.
from blogli.forms import CommentForm
from django.http import Http404

def index(request):
    blog_list = Blog.objects.all()
    blog_listcom = Comment.objects.all()
    return render_to_response('index.html', {'blog_list': blog_list, 'blog_listcom': blog_listcom})


def get_blogs(request):
    blogs = Blog.objects.all().order_by('-created')
    return render_to_response('blog_list.html', {'blogs': blogs})

def get_details(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form
    }
    return render(request, 'blog_details.html', ctx)

