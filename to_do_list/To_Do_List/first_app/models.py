from django.db import models


class ToDoModel(models.Model):
    # id = models.IntegerField(primary_key= True)
    titel = models.CharField(max_length= 30)
    discription = models.CharField(max_length=50)
    statas = models.BooleanField(default=False)