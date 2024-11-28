# Generated by Django 5.1.3 on 2024-11-28 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="QueryLog",
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
                ("problem_statement", models.TextField()),
                ("sql_query", models.TextField()),
                ("pandas_query", models.TextField(blank=True, null=True)),
                ("pyspark_query", models.TextField(blank=True, null=True)),
                ("result", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]