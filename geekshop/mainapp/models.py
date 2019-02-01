from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    image = models.ImageField(upload_to='products_category_images', blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

class Menu (models.Model):
    name = models.CharField(verbose_name='Заголовок меню', max_length=128)
    link = models.CharField(verbose_name='Ссылка', max_length=64, null=True)

    def __str__(self):
        return f"{self.name} ({self.link})"

