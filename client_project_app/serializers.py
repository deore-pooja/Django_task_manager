# from rest_framework import serializers
# from .models import Client, Project
# from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username']

# class ProjectSerializer(serializers.ModelSerializer):
#     users = UserSerializer(many=True, read_only=True)

#     class Meta:
#         model = Project
#         fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']

# class ClientSerializer(serializers.ModelSerializer):
#     created_by = serializers.ReadOnlyField(source='created_by.username')
#     projects = ProjectSerializer(many=True, read_only=True)

#     class Meta:
#         model = Client
#         fields = ['id', 'client_name', 'created_at', 'created_by', 'updated_at', 'projects']

from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']  # Display user id and username

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'client_name']  # Display client id and client name

class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)  # Keep users as a nested serializer
    client = ClientSerializer(read_only=True)  # Display client name instead of id
    client_id = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), source='client', write_only=True)  # To allow client selection
    created_by = UserSerializer(read_only=True)  # Display created_by name instead of id
    created_by_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='created_by', write_only=True)  # To allow creator selection

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'client_id', 'users', 'created_at', 'created_by', 'created_by_id']
