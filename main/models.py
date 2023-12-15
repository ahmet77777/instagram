from django.db import models

class Login(models.Model):
    name = models.CharField(max_length=1000)
    passwordd = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
# Create your models here.
