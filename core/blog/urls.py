from django.urls import path
from .views import BlogIndexView, RedticetViewTest, PostListView, PostDetailView, CreatePostView, UpdatePostView, PostDeleteView

app_name = 'blog'
urlpatterns  = [
    path('index', BlogIndexView.as_view(), name='index'),
    path('index-2/<int:pk>/', RedticetViewTest.as_view(), name='redirect_view'),
    path('posts/', PostListView.as_view(), name='posts_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/create/', CreatePostView.as_view(), name='post_create'),
    path('posts/update/<int:pk>/', UpdatePostView.as_view(), name='update_view'),
    path('posts/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete')
]