# Generated by Django 5.0.7 on 2024-09-24 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Spam", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="timestamp",
        ),
        migrations.AlterField(
            model_name="contact",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
