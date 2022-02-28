from django.urls import include, path
from rest_framework.routers import DefaultRouter
from accounts.api.views import CRUDAllUsersViewset

router = DefaultRouter()
router.register('all-users', CRUDAllUsersViewset, basename='all-users')

urlpatterns = [
    path('', include(router.urls)),
]
