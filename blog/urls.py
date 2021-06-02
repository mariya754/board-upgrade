from django.urls import path
 
from .views import BlogListView, BlogDetailView, detail, change, delete
 
urlpatterns = [
    path('post/change/<int:pk>/', change, name='post_change'),
    path('post/delete/<int:pk>/', delete, name ='post_delete'),
    path('post/<int:pk>/', detail, name='post_detail'), 
    path('', BlogListView.as_view(), name='home'),
]


