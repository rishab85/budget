from django.db import models

class mainBudget(models.Model):
    month = models.CharField(max_length=25)
    Amount = models.FloatField()

    def __str__(self):
        return self.month