# Generated by Django 4.1.1 on 2022-09-24 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='motherboard',
            name='price',
            field=models.FloatField(default=0, help_text='Введите цену', verbose_name='цена'),
        ),
        migrations.AddField(
            model_name='processor',
            name='price',
            field=models.FloatField(default=0, help_text='Введите цену', verbose_name='цена'),
        ),
        migrations.AddField(
            model_name='ram',
            name='price',
            field=models.FloatField(default=0, help_text='Введите цену', verbose_name='цена'),
        ),
    ]
