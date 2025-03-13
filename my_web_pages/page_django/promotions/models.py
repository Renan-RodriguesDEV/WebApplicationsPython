from django.db import models


class Usuarios(models.Model):
    username = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username
