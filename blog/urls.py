from django.urls import path
 
from .views import BlogListView, BlogDetailView, detail, change # новое изменение
 
urlpatterns = [
    path('post/change/<int:pk>/', change, name='post_change'),
   # path('post/delete', DeleteUserView.as_view(), name = 'profile_delete'),
    path('post/<int:pk>/', detail, name='post_detail'), # новое изменение
    path('', BlogListView.as_view(), name='home'),
]


