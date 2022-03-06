from django.urls import path
from posts.api.views import ListCreatePostView, UpdateRetrieveDestroyPostView

urlpatterns = [
    path('all-posts/', ListCreatePostView.as_view(), name='posts-list-create'),
    path('all-posts/<int:pk>', UpdateRetrieveDestroyPostView.as_view(), name='post-edit'),
]
