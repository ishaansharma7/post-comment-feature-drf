from django.urls import path
from posts.api.views import ListCreatePostView, UpdateRetrieveDestroyPostView, CreateCommentView, PostCommentsView

urlpatterns = [
    path('all-posts/', ListCreatePostView.as_view(), name='posts-list-create'),
    path('all-posts/<int:pk>', UpdateRetrieveDestroyPostView.as_view(), name='post-edit'),
    path('all-posts/<int:pk>/comment-add/', CreateCommentView.as_view(), name='create-comment'),
    path('all-posts/<int:pk>/comments/', PostCommentsView.as_view(), name='list-comment'),
]
