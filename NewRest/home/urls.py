from django.urls import path
from .views import index, todos_result

urlpatterns = [
    path('',todos_result,name='index')
]