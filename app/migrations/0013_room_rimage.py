# Generated by Django 4.1.2 on 2022-10-25 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_room_rimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='rimage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]