# Generated by Django 2.1.5 on 2019-02-05 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20190205_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активна'),
        ),
    ]
