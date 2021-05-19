from django.urls import path
 
from .views import BlogListView, BlogDetailView, detail # новое изменение
 
urlpatterns = [
    path('post/<int:pk>/', detail, name='post_detail'), # новое изменение
    path('', BlogListView.as_view(), name='home'),
]
