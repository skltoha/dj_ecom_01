# Generated by Django 4.2.4 on 2023-08-18 08:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("menu", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="menu",
            name="url",
        ),
    ]
