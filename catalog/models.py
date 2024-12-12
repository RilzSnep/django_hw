from django.db import models
from django.core.validators import MaxValueValidator


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название продукта",  # product name for admin panel
        help_text="Введите название продукта",  # text for help in admin panel
    )
    description = models.TextField(
        verbose_name="Описание продукта",  # product description for admin panel
        help_text="Введите описание продукта",  # text for help in admin panel
    )
    image = models.ImageField(
        upload_to="catalog/image",  # directory for images
        blank=True,
        null=True,  # check on null values
        verbose_name="Фото продукта",  # product photo for admin panel
        help_text="Загрзите фото продукта",  # text for help in admin panel
    )
    category = models.CharField(
        max_length=100,
        verbose_name="Категория",  # product category for admin panel
        help_text="Введите категорию",  # text for help in admin panel
    )
    price = models.IntegerField(
        default=0,  # default price value
        validators=[MaxValueValidator(10000)],  # Restricts the price to a maximum of 10000
        verbose_name="Цена за продукт",  # Display name for admin panel
    )
    created_at = models.DateField(
        blank=True,  # Field is optional
        null=True,  # Allows storing null values
        verbose_name="Дата создания",  # Display name for admin panel
        help_text="Введите дату создания",  # text for help in admin panel
    )
    updated_at = models.DateField(
        blank=True,  # Field is optional
        null=True,  # Allows storing null values
        verbose_name="дата последнего изменения",  # Display name for admin panel
        help_text="Введите дату последнего изменения",  # text for help in admin panel
    )

    # Meta information for the Product model
    class Meta:
        verbose_name = "Продукт"  # Singular name for admin panel
        verbose_name_plural = "Продукты"  # Plural name for admin panel
        ordering = ["name", "category"]  # Default ordering by name and category

    # String representation of the Product object
    def __str__(self):
        return self.name


# Model representing a Category entity
class Category(models.Model):
    """Represents a category with name and optional description."""

    name = models.CharField(
        max_length=100,
        verbose_name="Название категории",  # Display name for admin panel
        help_text="Введите название категории",  # Tooltip/help text in admin panel
    )
    description = models.TextField(
        blank=True,  # Field is optional
        null=True,  # Allows storing null values
        verbose_name="Описание категории",  # Display name for admin panel
        help_text="Введите описание категории",  # Tooltip/help text in admin panel
    )

    # Meta information for the Category model
    class Meta:
        verbose_name = "Категория"  # Singular name for admin panel
        verbose_name_plural = "Категории"  # Plural name for admin panel

    # String representation of the Category object
    def __str__(self):
        return self.name
