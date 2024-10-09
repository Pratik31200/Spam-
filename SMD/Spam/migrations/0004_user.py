# Generated by Django 5.0.7 on 2024-09-27 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Spam", "0003_alter_contact_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=150, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=128)),
            ],
        ),
    ]
