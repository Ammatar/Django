# Generated by Django 2.1.5 on 2019-01-21 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_menu_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='link',
            field=models.CharField(max_length=64, null=True, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=128, verbose_name='имя продукта'),
        ),
    ]
