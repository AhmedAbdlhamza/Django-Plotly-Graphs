from django.db import models

class WeeklyData(models.Model):
    date = models.DateField()
    sales = models.FloatField()
    profit = models.FloatField()
    inventory = models.FloatField()
    # Add other parameters here
    # ...

    def __str__(self):
        return f"WeeklyData for {self.date}"
