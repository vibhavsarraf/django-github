from django.urls import path
from .views import issuesAPI

urlpatterns = [
    path('api/', issuesAPI),
]
