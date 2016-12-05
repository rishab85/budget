from django.db import models

class budzetMax(models.Model):
    expenditure_name = models.CharField(max_length=25)
    expenditure_amount = models.FloatField()
    expenditure_place = models.CharField(max_length=25)
    expenditure_year = models.IntegerField(default = 2016)
    expenditure_month = models.IntegerField(default = 1)
    expenduture_date = models.IntegerField(default = 1)
    def __str__(self):
        return self.expenditure_name