from django.db import models

class user(models.Model):
    user_name = models.CharField(max_length=25)
    user_password = models.CharField(max_length=25)
    def __str__(self):
        return self.user_name