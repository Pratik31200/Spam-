# Generated by Django 5.0.7 on 2024-09-27 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Spam", "0002_remove_contact_timestamp_alter_contact_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]
