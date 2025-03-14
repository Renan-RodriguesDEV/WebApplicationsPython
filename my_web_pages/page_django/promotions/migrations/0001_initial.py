# Generated by Django 5.1.7 on 2025-03-13 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

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
                ("username", models.CharField(max_length=255)),
                ("age", models.PositiveIntegerField()),
                ("email", models.EmailField(max_length=100)),
                ("phone", models.CharField(max_length=20)),
                ("date_joined", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
