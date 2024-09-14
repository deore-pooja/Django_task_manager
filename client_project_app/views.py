from django.shortcuts import render
from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

##
from rest_framework import viewsets
from .serializers import ClientSerializer, ProjectSerializer


from django.shortcuts import redirect

def home(request):
    return redirect('/api/projects/')  # Or '/api/projects/' 

# client_project_app/views.py
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project
from .serializers import ProjectSerializer

class UserProjectsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        projects = Project.objects.filter(users=user)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)



class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
##

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'updated_at', 'projects']
