# Generated by Django 4.0.5 on 2022-06-04 09:00

from django.db import migrations, models
import program.utils


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=program.utils.program_images),
        ),
    ]
