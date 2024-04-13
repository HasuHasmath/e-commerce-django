# Generated by Django 4.2.11 on 2024-04-13 20:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("product_name", models.CharField(max_length=200, null=True)),
                ("product_code", models.CharField(max_length=200, null=True)),
                ("price", models.FloatField(default=0)),
                ("vat", models.IntegerField(default=0)),
            ],
        ),
    ]
