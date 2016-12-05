from django.db import models

class dueDates(models.Model):
    payment_field = models.CharField(max_length=25)
    due_date = models.CharField(max_length=35)

    def __str__(self):
        return self.payment_field