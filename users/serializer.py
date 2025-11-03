from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user']
        
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only':True}}
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class LoginSerializer(serializers.Serializer):
   username = serializers.CharField()
   password = serializers.CharField(write_only=True)
   
   def validate(self, data):
       username = data.get('username')
       password = data.get('password')
       user = authenticate(username=username, password=password)
       if not user:
           raise serializers.ValidationError("Invalid credentials")
       data["user"] = user
       return data
   
class LogoutSerializer(serializers.Serializer):
     def logout(self, request):
            logout(request)
            print('Logged out successfully')
            return True