from django.db import models
from django.views.generic import CreateView


# Create your models here.

class Notes(models.Model):

    name = models.CharField(max_length=100, null=True)
    text = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.text} {self.created_at}"
