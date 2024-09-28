from rest_framework import serializers
from django.contrib.auth import get_user_model
from todo.models import Todo

user = get_user_model()


class TodoSerializer(serializers.ModelSerializer):

    def validate_title(self, title):
        if len(title)>=100:
            raise serializers.ValidationError("tooo long")

        return title

    class Meta:
        model = Todo
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'

    todos = TodoSerializer(many=True, read_only=True)
