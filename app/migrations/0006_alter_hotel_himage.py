# Generated by Django 4.1.2 on 2022-10-24 07:42

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_room_roomtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='himage',
            field=models.ImageField(blank=True, null=True, upload_to=app.models.image_upload_to),
        ),
    ]