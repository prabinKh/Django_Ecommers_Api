# Generated by Django 5.1.4 on 2024-12-27 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("allproduct", "0003_remove_tag_product"),
    ]

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
                ("product_name", models.CharField(max_length=100)),
                ("product_image", models.URLField()),
                ("description", models.TextField()),
                ("category", models.CharField(max_length=100)),
                ("price", models.FloatField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
