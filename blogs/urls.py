from django.urls import path
from .views import BlogListCreateView, BlogDetailView,home,post_detail

urlpatterns = [

    path('home', home, name='home'),
    path('',BlogListCreateView.as_view(),name='create blog'),

    path('<int:pk>/',BlogDetailView.as_view(), name='detail_view'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
]