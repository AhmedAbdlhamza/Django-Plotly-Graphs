# Generated by Django 3.2.18 on 2023-03-21 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('sales', models.FloatField()),
                ('profit', models.FloatField()),
                ('inventory', models.FloatField()),
            ],
        ),
    ]
