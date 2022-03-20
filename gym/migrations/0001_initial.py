# Generated by Django 4.0.2 on 2022-02-24 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GymTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gym_name', models.CharField(blank=True, max_length=100, null=True)),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField(blank=True, null=True)),
                ('exercise_in_week', models.PositiveBigIntegerField(default=1)),
                ('exercise_in_day', models.PositiveBigIntegerField(default=1)),
            ],
        ),
    ]