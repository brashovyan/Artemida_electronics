# Generated by Django 4.1.1 on 2022-10-26 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_corpus'),
    ]

    operations = [
        migrations.AddField(
            model_name='cooler',
            name='stock',
            field=models.IntegerField(default=10, help_text='Введите кол-во товара на складе (доступного к покупке)', verbose_name='Кол-во товара'),
        ),
        migrations.AddField(
            model_name='corpus',
            name='stock',
            field=models.IntegerField(default=10, help_text='Введите кол-во товара на складе (доступного к покупке)', verbose_name='Кол-во товара'),
        ),
        migrations.AddField(
            model_name='hdd',
            name='stock',
            field=models.IntegerField(default=10, help_text='Введите кол-во товара на складе (доступного к покупке)', verbose_name='Кол-во товара'),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='stock',
            field=models.IntegerField(default=10, help_text='Введите кол-во товара на складе (доступного к покупке)', verbose_name='Кол-во товара'),
        ),
        migrations.AddField(
            model_name='power_block',
            name='stock',
            field=models.IntegerField(default=10, help_text='Введите кол-во товара на складе (доступного к покупке)', verbose_name='Кол-во товара'),
        ),
        migrations.AddField(
            model_name='processor',
            name='stock',
            field=models.IntegerField(default=10, help_text='Введите кол-во товара на складе (доступного к покупке)', verbose_name='Кол-во товара'),
        ),
        migrations.AddField(
            model_name='ram',
            name='stock',
            field=models.IntegerField(default=10, help_text='Введите кол-во товара на складе (доступного к покупке)', verbose_name='Кол-во товара'),
        ),
        migrations.AddField(
            model_name='ssd_m2',
            name='stock',
            field=models.IntegerField(default=10, help_text='Введите кол-во товара на складе (доступного к покупке)', verbose_name='Кол-во товара'),
        ),
        migrations.AddField(
            model_name='ssd_sata',
            name='stock',
            field=models.IntegerField(default=10, help_text='Введите кол-во товара на складе (доступного к покупке)', verbose_name='Кол-во товара'),
        ),
        migrations.AddField(
            model_name='videocard',
            name='stock',
            field=models.IntegerField(default=10, help_text='Введите кол-во товара на складе (доступного к покупке)', verbose_name='Кол-во товара'),
        ),
    ]
