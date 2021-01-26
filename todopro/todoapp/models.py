from django.db import models
import datetime


# Create your models here.
class Task(models.Model):
    def __str__(self):
        return self.Name

    Name = models.CharField(max_length=150)
    Priority = models.IntegerField()
    Date = models.DateField(default=datetime.date.today)

