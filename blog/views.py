from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from blog.models import Post
# Create your views here.

def view_blog(request):
    return render(request, 'blog/blog.html')