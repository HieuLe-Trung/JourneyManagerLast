# Generated by Django 4.2.11 on 2024-05-03 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journeys', '0007_journey_background'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='lock_cmt',
        ),
        migrations.AddField(
            model_name='journey',
            name='lock_cmt',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='journey',
            name='departure_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
