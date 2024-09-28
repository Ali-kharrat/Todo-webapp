from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Todo
from .serialaizer import TodoSerializer, UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


user = get_user_model()


# @api_view(['GET', 'POST'])
# def all_todos(request: Request):
#     if request.method == 'GET':
#         todos = Todo.objects.all()
#         todo_serializer = TodoSerializer(todos, many=True)
#         return Response(todo_serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     return Response(None, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def all_todo_det(request: Request, todo_id: int):
#     try:
#         todo = Todo.objects.get(pk=todo_id)
#     except Todo.DoesNotExist:
#         return Response(None, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'PUT':
#         serializer = TodoSerializer(todo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(request.data, status=status.HTTP_202_ACCEPTED)
#         else:
#             return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         todo.delete()
#         return Response(None, status=status.HTTP_204_NO_CONTENT)
#


# class TodoView(APIView):
#     def get(self, request: Request):
#         todos = Todo.objects.all()
#         serializer = TodoSerializer(todos, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request: Request):
#         serializer = TodoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(request.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(None, status=status.HTTP_400_BAD_REQUEST)
#
# class TodoDetailView(APIView):
#     def get_todo_id(self, todo_id:int):
#         try:
#             todo = Todo.objects.get(pk=todo_id)
#             return todo
#         except Todo.DoesNotExist:
#             return Response(None, status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request: Request, todo_id:int):
#         todo = self.get_todo_id(todo_id)
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request: Request, todo_id:int):
#         todo = Todo.objects.get(pk=todo_id)
#         serializer = TodoSerializer(request.data, instance=todo)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(request.data, status=status.HTTP_201_CREATED)
#
#         else:
#             return Response(None, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request: Request, todo_id:int):
#         todo = self.get_todo_id(todo_id)
#         todo.delete()
#         return Response(None, status=status.HTTP_204_NO_CONTENT)

# class todomixin(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#
#     def get(self, request: Request):
#         return self.list(request.data)
#
#     def post(self, request: Request):
#         return self.create(request.data)
#
#
# class TodoList(generics.DestroyAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#
#     def get(self, request:Request, pk: int):
#         return self.retrieve(request, pk)
#
#     def put(self, request: Request, pk: int):
#         return self.update(request, pk)
#
#     def delete(self, request: Request, pk: int):
#         return self.destroy(request, pk)
#

#
# class TodogenericView(generics.ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#
# class TodosView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


# class page_number(PageNumberPagination):
#     page_size = 3


class Todoviwe(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    pagination_class = PageNumberPagination


class UserViewSet(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = user.objects.all()
    pagination_class = LimitOffsetPagination
