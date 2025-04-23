from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('members/', views.members, name='members'),
    path('about/', views.about, name='about'),
]
