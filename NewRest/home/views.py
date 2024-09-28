from django.shortcuts import render
from todo.models import Todo
# from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
def index(request):
    context = {
        'todos': Todo.objects.all()
    }
    return render(request, 'index.html', context)


@api_view(['GET'])
def todos_result(request: Request):
    todos = list(Todo.objects.all().values('title'))
    return Response(todos, status=status.HTTP_200_OK)
