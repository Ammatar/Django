# Generated by Django 2.1.5 on 2019-01-21 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20190121_2158'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]