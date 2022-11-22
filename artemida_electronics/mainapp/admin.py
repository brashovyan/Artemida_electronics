from django.contrib import admin
from .models import Processor, Motherboard, RAM, Cooler, Videocard, Power_block, SSD_M2, HDD, SSD_sata, Corpus, Review, History
from django.utils.safestring import mark_safe

class ProcessorAdmin(admin.ModelAdmin): # Имя сущности + Admin
    list_display = ('id', 'title', 'get_html_photo', 'stock') # какие поля будут отображаться у сущности в админке
    list_display_links = ('id', 'title') # какие поля будут содержать ссылку
    search_fields = ('title', 'id') # по каким полям производить поиск
    list_filter = ('cores', 'socket') # фильтрация

    def get_html_photo(self, object): # метод для отображения картинок
        if object.image:
            return mark_safe(f"<img src={object.image.url} width=40>") 

    get_html_photo.short_description = "Фото"


class HddAdmin(admin.ModelAdmin): # Имя сущности + Admin
    list_display = ('id', 'title', 'get_html_photo', 'price', 'stock') # какие поля будут отображаться у сущности в админке
    list_display_links = ('id', 'title') # какие поля будут содержать ссылку
    search_fields = ('title', 'id') # по каким полям производить поиск
    list_filter = ['capacity'] # фильтрация

    def get_html_photo(self, object): # метод для отображения картинок
        if object.image:
            return mark_safe(f"<img src={object.image.url} width=40>") 

    get_html_photo.short_description = "Фото"


class SSD_sata_Admin(admin.ModelAdmin): # Имя сущности + Admin
    list_display = ('id', 'title', 'get_html_photo', 'price', 'stock') # какие поля будут отображаться у сущности в админке
    list_display_links = ('id', 'title') # какие поля будут содержать ссылку
    search_fields = ('title', 'id') # по каким полям производить поиск
    list_filter = ['capacity'] # фильтрация

    def get_html_photo(self, object): # метод для отображения картинок
        if object.image:
            return mark_safe(f"<img src={object.image.url} width=40>") 

    get_html_photo.short_description = "Фото"


class SSD_M2_Admin(admin.ModelAdmin): # Имя сущности + Admin
    list_display = ('id', 'title', 'get_html_photo', 'price', 'stock') # какие поля будут отображаться у сущности в админке
    list_display_links = ('id', 'title') # какие поля будут содержать ссылку
    search_fields = ('title', 'id') # по каким полям производить поиск
    list_filter = ['capacity'] # фильтрация

    def get_html_photo(self, object): # метод для отображения картинок
        if object.image:
            return mark_safe(f"<img src={object.image.url} width=40>") 

    get_html_photo.short_description = "Фото"


class MotherboardAdmin(admin.ModelAdmin): # Имя сущности + Admin
    list_display = ('id', 'title', 'get_html_photo', 'price', 'stock') # какие поля будут отображаться у сущности в админке
    list_display_links = ('id', 'title') # какие поля будут содержать ссылку
    search_fields = ('title', 'id') # по каким полям производить поиск
    list_filter = ['socket'] # фильтрация

    def get_html_photo(self, object): # метод для отображения картинок
        if object.image:
            return mark_safe(f"<img src={object.image.url} width=40>") 

    get_html_photo.short_description = "Фото"


class RamAdmin(admin.ModelAdmin): # Имя сущности + Admin
    list_display = ('id', 'title', 'get_html_photo', 'price', 'stock') # какие поля будут отображаться у сущности в админке
    list_display_links = ('id', 'title') # какие поля будут содержать ссылку
    search_fields = ('title', 'id') # по каким полям производить поиск
    list_filter = ['size'] # фильтрация

    def get_html_photo(self, object): # метод для отображения картинок
        if object.image:
            return mark_safe(f"<img src={object.image.url} width=40>") 

    get_html_photo.short_description = "Фото"


class CoolerAdmin(admin.ModelAdmin): # Имя сущности + Admin
    list_display = ('id', 'title', 'get_html_photo', 'price', 'stock') # какие поля будут отображаться у сущности в админке
    list_display_links = ('id', 'title') # какие поля будут содержать ссылку
    search_fields = ('title', 'id') # по каким полям производить поиск
    #list_filter = ['power'] # фильтрация

    def get_html_photo(self, object): # метод для отображения картинок
        if object.image:
            return mark_safe(f"<img src={object.image.url} width=40>") 

    get_html_photo.short_description = "Фото"


class VideocardAdmin(admin.ModelAdmin): # Имя сущности + Admin
    list_display = ('id', 'title', 'get_html_photo', 'price', 'stock') # какие поля будут отображаться у сущности в админке
    list_display_links = ('id', 'title') # какие поля будут содержать ссылку
    search_fields = ('title', 'id') # по каким полям производить поиск
    list_filter = ['memory'] # фильтрация

    def get_html_photo(self, object): # метод для отображения картинок
        if object.image:
            return mark_safe(f"<img src={object.image.url} width=40>") 

    get_html_photo.short_description = "Фото"


class PowerAdmin(admin.ModelAdmin): # Имя сущности + Admin
    list_display = ('id', 'title', 'get_html_photo', 'price', 'stock') # какие поля будут отображаться у сущности в админке
    list_display_links = ('id', 'title') # какие поля будут содержать ссылку
    search_fields = ('title', 'id') # по каким полям производить поиск
    #list_filter = ['power'] # фильтрация

    def get_html_photo(self, object): # метод для отображения картинок
        if object.image:
            return mark_safe(f"<img src={object.image.url} width=40>") 

    get_html_photo.short_description = "Фото"


class CorpusAdmin(admin.ModelAdmin): # Имя сущности + Admin
    list_display = ('id', 'title', 'get_html_photo', 'price', 'stock') # какие поля будут отображаться у сущности в админке
    list_display_links = ('id', 'title') # какие поля будут содержать ссылку
    search_fields = ('title', 'id') # по каким полям производить поиск
    list_filter = ['form'] # фильтрация

    def get_html_photo(self, object): # метод для отображения картинок
        if object.image:
            return mark_safe(f"<img src={object.image.url} width=40>") 

    get_html_photo.short_description = "Фото"


class ReviewAdmin(admin.ModelAdmin): # Имя сущности + Admin
    list_display = ('id', 'creator', 'date_review', 'content') # какие поля будут отображаться у сущности в админке
    list_display_links = ('id', 'creator') # какие поля будут содержать ссылку
    search_fields = ('id', 'creator', 'date_review', 'content') # по каким полям производить поиск


class HistoryAdmin(admin.ModelAdmin): # Имя сущности + Admin
    list_display = ('id', 'buyer', 'date', 'content') # какие поля будут отображаться у сущности в админке
    list_display_links = ('id', 'buyer') # какие поля будут содержать ссылку
    list_display = ('id', 'buyer', 'date', 'content') # по каким полям производить поиск


admin.site.register(Processor, ProcessorAdmin)
admin.site.register(HDD, HddAdmin)
admin.site.register(SSD_sata, SSD_sata_Admin)
admin.site.register(Motherboard, MotherboardAdmin)
admin.site.register(RAM, RamAdmin)
admin.site.register(Cooler, CoolerAdmin)
admin.site.register(Videocard, VideocardAdmin)
admin.site.register(Power_block, PowerAdmin)
admin.site.register(SSD_M2, SSD_M2_Admin)
admin.site.register(Corpus, CoolerAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(History, HistoryAdmin)


