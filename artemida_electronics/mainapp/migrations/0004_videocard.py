# Generated by Django 4.1.1 on 2022-10-03 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_cooler_processor_tdp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videocard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите полное название видеокарты', max_length=100, verbose_name='Название видеокарты')),
                ('power', models.FloatField(default=0, help_text='Введите рекомендуемый блок питания', verbose_name='Рекомендуемый блок питания')),
                ('memory', models.CharField(help_text='Введите объём и тип памяти. Например 12гб GDDR6', max_length=20, null=True, verbose_name='Память')),
                ('image', models.ImageField(blank=True, help_text='Загрузите одно изображение', null=True, upload_to='Videocards/', verbose_name='Изображение')),
            ],
        ),
    ]