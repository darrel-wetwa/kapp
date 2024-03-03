from django.db import models
class Member(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username