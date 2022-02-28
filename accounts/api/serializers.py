from rest_framework import serializers
from accounts.models import AllUsers

class RegisterAllUsersSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = AllUsers
        fields = ['email', 'user_name', 'password', 'password2']
        extra_kwargs = {'password':{'write_only':True}}
    
    def save(self, **kwargs):
        
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'passwords does not match'})
        
        new_user = AllUsers.objects.create_user(email=self.validated_data['email'],
                            user_name=self.validated_data['user_name'], password=password)

        return new_user