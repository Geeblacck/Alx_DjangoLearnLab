from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

app_name = 'blog'

urlpatterns = [
    # Blog post URLs
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),  # create
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),     # update
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),     # delete
]

# blog/urls.py
from .views import PostSearchView, PostListView

urlpatterns += [
    path('search/', PostSearchView.as_view(), name='post-search'),
    path('tags/<str:tag_name>/', PostListView.as_view(), name='posts-by-tag'),
]


# blog/urls.py
from .views import PostByTagListView

urlpatterns += [
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),
]
