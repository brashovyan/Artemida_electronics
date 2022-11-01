from django.db import models
from django.contrib.auth.models import User


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
    stock = models.IntegerField(default=10, help_text="Введите кол-во товара на складе (доступного к покупке)", verbose_name='Кол-во товара', null=False)
    image = models.ImageField(upload_to='processors/', help_text='Загрузите одно изображение', verbose_name='Изображение', null=True, blank=True)
    review = models.ManyToManyField('Review', blank=True)
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
    m2_slots =  models.IntegerField(default = 0, help_text="Введите кол-во разьемов М.2", verbose_name="Разьемы М.2", null=False)
    sata_slots = models.IntegerField(default = 0, help_text="Введите кол-во разьемов SATA", verbose_name="Разьемы SATA", null=False)
    price = models.FloatField(default=0, help_text="Введите цену", verbose_name="цена", null=False)
    stock = models.IntegerField(default=10, help_text="Введите кол-во товара на складе (доступного к покупке)", verbose_name='Кол-во товара', null=False)
    image = models.ImageField(upload_to='motherboards/', help_text='Загрузите одно изображение', verbose_name='Изображение', null=True, blank=True)
    review = models.ManyToManyField('Review', blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.title}, сокет {self.socket}'


class RAM(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название материнской платы", help_text="Введите полное название мат. платы.", null=False)
    type_memory = models.CharField(max_length=20, verbose_name="Тип ОЗУ", help_text="Введите тип памяти. Например DDR4", null=False)
    m_frequency = models.FloatField(help_text="Введите частоту ОЗУ", verbose_name="Частота ОЗУ", null=False)
    size = models.FloatField(help_text="Введите объём памяти в Гб.", verbose_name="Объём памяти", null=False)
    price = models.FloatField(default=0, help_text="Введите цену", verbose_name="цена", null=False)
    stock = models.IntegerField(default=10, help_text="Введите кол-во товара на складе (доступного к покупке)", verbose_name='Кол-во товара', null=False)
    image = models.ImageField(upload_to='RAM/', help_text='Загрузите одно изображение', verbose_name='Изображение', null=True, blank=True)
    review = models.ManyToManyField('Review', blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.title}, {self.type_memory}, {self.size}'


class Cooler(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название кулера", help_text="Введите полное название кулера", null=False)
    power = models.IntegerField(verbose_name="Рассеиваемая мощность", help_text="Введите рассеиваемую мощность", null=False)
    price = models.FloatField(default=0, help_text="Введите цену", verbose_name="цена", null=False)
    stock = models.IntegerField(default=10, help_text="Введите кол-во товара на складе (доступного к покупке)", verbose_name='Кол-во товара', null=False)
    image = models.ImageField(upload_to='Coolers/', help_text='Загрузите одно изображение', verbose_name='Изображение', null=True, blank=True)
    review = models.ManyToManyField('Review', blank=True)

    objects = models.Manager()

    def __str__(self):
        return f'{self.title}'


class Videocard(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название видеокарты", help_text="Введите полное название видеокарты", null=False)
    power = models.FloatField(default = 0, help_text="Введите рекомендуемый блок питания", verbose_name="Рекомендуемый блок питания", null=False)
    memory = models.CharField(max_length=20, help_text="Введите объём и тип памяти. Например 12гб GDDR6", verbose_name="Память", null=True)
    price = models.FloatField(default=0, help_text="Введите цену", verbose_name="цена", null=False)
    stock = models.IntegerField(default=10, help_text="Введите кол-во товара на складе (доступного к покупке)", verbose_name='Кол-во товара', null=False)
    image = models.ImageField(upload_to='Videocards/', help_text='Загрузите одно изображение', verbose_name='Изображение', null=True, blank=True)
    review = models.ManyToManyField('Review', blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.title}'


class Power_block(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название блока питания", help_text="Введите полное название блока питания", null=False)
    power = models.FloatField(default = 0, help_text="Введите мощность в Вт", verbose_name="Мощность", null=False)
    price = models.FloatField(default=0, help_text="Введите цену", verbose_name="цена", null=False)
    stock = models.IntegerField(default=10, help_text="Введите кол-во товара на складе (доступного к покупке)", verbose_name='Кол-во товара', null=False)
    image = models.ImageField(upload_to='Power_blocks/', help_text='Загрузите одно изображение', verbose_name='Изображение', null=True, blank=True)
    review = models.ManyToManyField('Review', blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.title}'


class SSD_M2(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название SSD M.2", help_text="Введите полное название SSD M.2", null=False)
    capacity = models.FloatField(verbose_name="Объём памяти", help_text="Введите объём памяти в Гб", null = False)
    price = models.FloatField(default=0, help_text="Введите цену", verbose_name="цена", null=False)
    stock = models.IntegerField(default=10, help_text="Введите кол-во товара на складе (доступного к покупке)", verbose_name='Кол-во товара', null=False)
    image = models.ImageField(upload_to='ssd_m2/', help_text='Загрузите одно изображение', verbose_name='Изображение', null=True, blank=True)
    review = models.ManyToManyField('Review', blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.title}'


class HDD(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название жесткого диска (HDD)", help_text="Введите полное название жесткого диска (HDD)", null=False)
    capacity = models.FloatField(verbose_name="Объём памяти", help_text="Введите объём памяти в Гб", null = False)
    price = models.FloatField(default=0, help_text="Введите цену", verbose_name="цена", null=False)
    stock = models.IntegerField(default=10, help_text="Введите кол-во товара на складе (доступного к покупке)", verbose_name='Кол-во товара', null=False)
    image = models.ImageField(upload_to='hdd/', help_text='Загрузите одно изображение', verbose_name='Изображение', null=True, blank=True)
    review = models.ManyToManyField('Review', blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.title}'


class SSD_sata(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название SSD Sata", help_text="Введите полное название SSD Sata", null=False)
    capacity = models.FloatField(verbose_name="Объём памяти", help_text="Введите объём памяти в Гб", null = False)
    price = models.FloatField(default=0, help_text="Введите цену", verbose_name="цена", null=False)
    stock = models.IntegerField(default=10, help_text="Введите кол-во товара на складе (доступного к покупке)", verbose_name='Кол-во товара', null=False)
    image = models.ImageField(upload_to='ssd_sata/', help_text='Загрузите одно изображение', verbose_name='Изображение', null=True, blank=True)
    review = models.ManyToManyField('Review', blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.title}'


class Corpus(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название SSD Sata", help_text="Введите полное название SSD Sata", null=False)
    form = models.CharField(max_length =25, verbose_name="Форм-фактор", help_text="Введите форм-фактор корпуса", null=True, blank=True)
    price = models.FloatField(default=0, help_text="Введите цену", verbose_name="цена", null=False)
    stock = models.IntegerField(default=10, help_text="Введите кол-во товара на складе (доступного к покупке)", verbose_name='Кол-во товара', null=False)
    image = models.ImageField(upload_to='corpuses/', help_text='Загрузите одно изображение', verbose_name='Изображение', null=True, blank=True)
    review = models.ManyToManyField('Review', blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.title}'


class Review(models.Model):
    content = models.TextField(verbose_name="Отзыв", help_text="Напишите отзыв", null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=False)
    date_review = models.DateTimeField(auto_now_add=True, null=False)
    objects = models.Manager()

    def __str__(self):
        return f'{self.creator}'


class History(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Покупатель', null=False)
    date = models.DateTimeField(auto_now_add=True, null=False)
    content = models.TextField(verbose_name="Чек", help_text="Введите содержимое чека")
    objects = models.Manager()

    def __str__(self):
        return f'{self.buyer} - {self.date}'






