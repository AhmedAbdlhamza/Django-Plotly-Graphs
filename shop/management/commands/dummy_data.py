import random
import datetime
from django.core.management.base import BaseCommand
from shop.models import WeeklyData

class Command(BaseCommand):
    def handle(self, *args, **options):
        start_date = datetime.date(2020, 1, 1)
        num_weeks = 100

        for i in range(num_weeks):
            week_date = start_date + datetime.timedelta(weeks=i)
            sales = random.uniform(1000, 5000)
            profit = random.uniform(100, 2000)
            inventory = random.uniform(500, 3000)
            # Add other parameters here
            # ...

            weekly_data = WeeklyData(
                date=week_date,
                sales=sales,
                profit=profit,
                inventory=inventory,
                # Add other parameters here
                # ...
            )
            weekly_data.save()
