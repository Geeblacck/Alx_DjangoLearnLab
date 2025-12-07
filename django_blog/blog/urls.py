from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

app_name = 'blog'

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),           # ✅ "post/new/"
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # ✅ "update"
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # ✅ "delete"
]


from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns += [
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
