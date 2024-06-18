# Generated by Django 4.2.11 on 2024-04-24 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journeys', '0003_remove_notification_journey'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='journey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='journeys.journey'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='journeys.post'),
        ),
    ]