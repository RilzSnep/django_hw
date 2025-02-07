# Generated by Django 5.1.3 on 2025-01-23 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_alter_product_options_alter_category_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите фото продукта",
                null=True,
                upload_to="catalog/image/",
                verbose_name="Фото продукта",
            ),
        ),
    ]
