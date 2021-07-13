from django.urls import path
from . import views

urlpatterns = [
    path('', views.post, name='post'),
    path('<slug:slug>/', views.detail_post, name='detail_post'),
    path('add_blog', views.add_blog, name='add_blog'),
    path('edit_blog/<slug:slug>/', views.edit_blog, name='edit_blog'),
    path('delete_blog/<slug:slug>/', views.delete_blog, name='delete_blog'),
]
