# Generated by Django 5.0.4 on 2024-05-08 15:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("galeria", "0003_fotografia_publicada"),
    ]

    operations = [
        migrations.AddField(
            model_name="fotografia",
            name="data_fotografia",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
