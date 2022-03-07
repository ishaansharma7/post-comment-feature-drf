from rest_framework import generics
from accounts.models import AllUsers
from accounts.api.serializers import RegisterAllUsersSerializer

class ListCreateAllUsersView(generics.ListCreateAPIView):
    queryset = AllUsers.objects.all()
    serializer_class = RegisterAllUsersSerializer