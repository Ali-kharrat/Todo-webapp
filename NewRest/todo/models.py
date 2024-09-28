from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    priorty = models.IntegerField(default=1)
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='todos')

    class Meta:
        db_table = 'todos'
