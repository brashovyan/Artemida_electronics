# Generated by Django 4.1.1 on 2022-09-24 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите полное название мат. платы.', max_length=100, verbose_name='Название материнской платы')),
                ('socket', models.CharField(help_text='Введите сокет. Например AM4', max_length=20, verbose_name='Сокет')),
                ('chipset', models.CharField(blank=True, help_text='Введите чипсет. Например B450', max_length=20, null=True, verbose_name='Чипсет')),
                ('m_slots', models.IntegerField(help_text='Укадите количество слотов памяти.', verbose_name='Количество слотов памяти')),
                ('m_frequency', models.FloatField(help_text='Введите поддерживаемую частоту ОЗУ', verbose_name='Частота ОЗУ')),
                ('max_memory', models.FloatField(help_text='Введите максимальный объем ОЗУ.', verbose_name='Максимальный объём ОЗУ')),
                ('type_memory', models.CharField(help_text='Введите тип памяти. Например DDR4', max_length=20, verbose_name='Тип ОЗУ')),
                ('image', models.ImageField(blank=True, help_text='Загрузите одно изображение', null=True, upload_to='motherboards/', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='Processor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название процессора. Например Intel Core i3 10100f.', max_length=100, verbose_name='Название процессора')),
                ('socket', models.CharField(help_text='Введите сокет. Например AM4', max_length=20, verbose_name='Сокет')),
                ('cores', models.CharField(blank=True, help_text='Введите количество ядер и потоков. Например 4/8', max_length=7, null=True, verbose_name='Ядра/потоки')),
                ('frequency', models.FloatField(blank=True, help_text='Введите базовую частоту в ГГц', null=True, verbose_name='Базовая частота')),
                ('m_frequency', models.FloatField(help_text='Введите поддерживаемую частоту ОЗУ', verbose_name='Частота ОЗУ')),
                ('type_memory', models.CharField(help_text='Введите тип памяти. Например DDR4', max_length=20, verbose_name='Тип ОЗУ')),
                ('max_memory', models.FloatField(help_text='Введите максимальный объем ОЗУ.', verbose_name='Максимальный объём ОЗУ')),
                ('image', models.ImageField(blank=True, help_text='Загрузите одно изображение', null=True, upload_to='processors/', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите полное название мат. платы.', max_length=100, verbose_name='Название материнской платы')),
                ('type_memory', models.CharField(help_text='Введите тип памяти. Например DDR4', max_length=20, verbose_name='Тип ОЗУ')),
                ('m_frequency', models.FloatField(help_text='Введите частоту ОЗУ', verbose_name='Частота ОЗУ')),
                ('size', models.FloatField(help_text='Введите объём памяти в Гб.', verbose_name='Объём памяти')),
                ('image', models.ImageField(blank=True, help_text='Загрузите одно изображение', null=True, upload_to='RAM/', verbose_name='Изображение')),
            ],
        ),
    ]