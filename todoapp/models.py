from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    work = models.CharField(max_length=123)

    
    def __str__(self):
        return self.work

    def get_absolute_url(self):
        return reverse('ListView')
