from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название категории")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название продукта")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(
        upload_to="product/",
        verbose_name="Изображение (превью)",
        blank=True,
        null=True,
    )
    cost = models.IntegerField(verbose_name="Цена за покупку")
    created_at = models.DateField(verbose_name="Дата создания (записи в БД)")
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения (записи в БД)"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория товара",
        null=True,
        blank=True,
        related_name="products",
    )
    manufactured_at = models.DateField(
        null=True, blank=True, verbose_name="Дата производства продукта"
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name", "cost", "category"]

    def __str__(self):
        return self.name
