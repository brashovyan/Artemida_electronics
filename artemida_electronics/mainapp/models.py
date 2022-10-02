from email.policy import default
from tabnanny import verbose
from django.db import models


class Processor(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название процессора", help_text="Введите название процессора. Например Intel Core i3 10100f.", null=False)
    socket = models.CharField(max_length=20, verbose_name="Сокет", help_text="Введите сокет. Например AM4", null=False)
    cores = models.CharField(max_length=7, verbose_name="Ядра/потоки", help_text="Введите количество ядер и потоков. Например 4/8", null=True, blank=True)
    frequency = models.FloatField(help_text="Введите базовую частоту в ГГц", verbose_name="Базовая частота", null=True, blank=True)
    m_frequency = models.FloatField(help_text="Введите поддерживаемую частоту ОЗУ", verbose_name="Частота ОЗУ", null=False)
    type_memory = models.CharField(max_length=20, verbose_name="Тип ОЗУ", help_text="Введите тип памяти. Например DDR4", null=False)
    max_memory = models.FloatField(help_text="Введите максимальный объем ОЗУ.", verbose_name="Максимальный объём ОЗУ", null=False)
    tdp = models.IntegerField(default=0, help_text="Введите тепловыделение процессора (TDP)", verbose_name="Тепловыделение (TDP)", null=False)
    price = models.FloatField(default=0, help_text="Введите цену", verbose_name="цена", null=False)
    image = models.ImageField(upload_to='processors/', help_text='Загрузите одно изображение', verbose_name='Изображение', null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.title}'


class Motherboard(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название материнской платы", help_text="Введите полное название мат. платы.", null=False)
    socket = models.CharField(max_length=20, verbose_name="Сокет", help_text="Введите сокет. Например AM4", null=False)
    chipset = models.CharField(max_length=20, verbose_name="Чипсет", help_text="Введите чипсет. Например B450", null=True, blank=True)
    m_slots = models.IntegerField(verbose_name="Количество слотов памяти", help_text="Укадите количество слотов памяти.", null=False)
    m_frequency = models.FloatField(help_text="Введите поддерживаемую частоту ОЗУ", verbose_name="Частота ОЗУ", null=False)
    max_memory = models.FloatField(help_text="Введите максимальный объем ОЗУ.", verbose_name="Максимальный объём ОЗУ", null=False)
    type_memory = models.CharField(max_length=20, verbose_name="Тип ОЗУ", help_text="Введите тип памяти. Например DDR4", null=False)
    price = models.FloatField(default=0, help_text="Введите цену", verbose_name="цена", null=False)
    image = models.ImageField(upload_to='motherboards/', help_text='Загрузите одно изображение', verbose_name='Изображение', null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.title}, сокет {self.socket}'


class RAM(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название материнской платы", help_text="Введите полное название мат. платы.", null=False)
    type_memory = models.CharField(max_length=20, verbose_name="Тип ОЗУ", help_text="Введите тип памяти. Например DDR4", null=False)
    m_frequency = models.FloatField(help_text="Введите частоту ОЗУ", verbose_name="Частота ОЗУ", null=False)
    size = models.FloatField(help_text="Введите объём памяти в Гб.", verbose_name="Объём памяти", null=False)
    price = models.FloatField(default=0, help_text="Введите цену", verbose_name="цена", null=False)
    image = models.ImageField(upload_to='RAM/', help_text='Загрузите одно изображение', verbose_name='Изображение', null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.title}, {self.type_memory}, {self.size}'


class Cooler(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название кулера", help_text="Введите полное название кулера", null=False)
    power = models.IntegerField(verbose_name="Рассеиваемая мощность", help_text="Введите рассеиваемую мощность", null=False)
    price = models.FloatField(default=0, help_text="Введите цену", verbose_name="цена", null=False)
    image = models.ImageField(upload_to='Coolers/', help_text='Загрузите одно изображение', verbose_name='Изображение', null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return f'{self.title}'


