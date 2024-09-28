from django.urls import path, include

from .views import Todoviwe, UserViewSet

urlpatterns = [
    path('', Todoviwe.as_view(), name='index'),
    path('user/', UserViewSet.as_view(), name='index'),
]
