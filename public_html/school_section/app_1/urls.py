from django.urls import path
from .views import index, teleRequest

urlpatterns = [
    path('', index),
    path('teleRequest', teleRequest, name='teleRequest'),
]

