from django.urls import path
from rest_framework.routers import DefaultRouter
from accounts.api.views import ListCreateAllUsersView

urlpatterns = [
    path('all-users/', ListCreateAllUsersView.as_view(), name='list-create-users'),
]
