from rest_framework import generics
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog
from django.conf import settings
from .serializers import BlogSerializer

import os




def home(request):
    print("Current working directory:", os.getcwd())
    print("Template directories:", settings.TEMPLATES)
    object_list=  Blog.objects.all()
    paginator=Paginator(object_list,5)

    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)


    return render(request,'blogs/home.html',{'page_obj':page_obj})


def post_detail(request, post_id):
    post = get_object_or_404(Blog, id=post_id)
    return render(request, 'blogs/post_detail.html', {'post': post})



class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer