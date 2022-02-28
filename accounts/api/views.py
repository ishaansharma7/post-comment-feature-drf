from rest_framework import viewsets
from accounts.models import AllUsers
from accounts.api.serializers import RegisterAllUsersSerializer

class CRUDAllUsersViewset(viewsets.ModelViewSet):
    queryset = AllUsers.objects.all()
    serializer_class = RegisterAllUsersSerializer