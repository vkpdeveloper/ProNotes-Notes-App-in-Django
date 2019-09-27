from django.db import models
from datetime import date

class Work(models.Model):
    work_id = models.AutoField(primary_key=True)
    work = models.CharField(max_length=100, default='')
    date = models.DateField(default=date.today)
    def __str__(self):
        return self.work