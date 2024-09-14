# """
# URL configuration for machine_test project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """

# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from client_project_app.views import ClientViewSet, ProjectViewSet
# from client_project_app.views import home

# router = DefaultRouter()
# router.register(r'clients', ClientViewSet)
# router.register(r'projects', ProjectViewSet, basename='project')

# ##

# # client_project_app/urls.py

# from .views import UserProjectsView

# urlpatterns = [
#     # ... other url patterns
#     path('projects/', UserProjectsView.as_view(), name='user-projects'),
# ]

# # client_project_app/urls.py
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import ClientViewSet, ProjectViewSet, UserProjectsView

# router = DefaultRouter()
# router.register(r'clients', ClientViewSet)
# router.register(r'projects', ProjectViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('projects/', UserProjectsView.as_view(), name='user-projects'),
# ]

# urlpatterns = [
#     path('', home),
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),
# ]

# ##

# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('api/', include(router.urls)),
# # ]

# URL configuration for machine_test project.

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from client_project_app.views import ClientViewSet, ProjectViewSet, UserProjectsView, home

# Router setup
router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'projects', ProjectViewSet, basename='project')

# URL patterns for the client_project_app
client_project_patterns = [
    path('projects/', UserProjectsView.as_view(), name='user-projects'),
]

# Main URL configuration
urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(client_project_patterns)),  # Make sure this path doesn't conflict with router paths
]
