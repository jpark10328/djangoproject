# Generated by Django 4.1.2 on 2022-10-24 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_remove_hotel_hcontent"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="roomtype",
            field=models.CharField(max_length=200, null=True, verbose_name="방종류"),
        ),
    ]