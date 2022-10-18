from decimal import Decimal
from django.conf import settings
from mainapp.models import Processor


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session # получаем данные ссессии пользователя
        cart = self.session.get(settings.CART_SESSION_ID) # получаем его айдишник
        if not cart: # если корзины нет
            cart = self.session[settings.CART_SESSION_ID] = {} # то создаем её
        self.cart = cart # и сохраняем её в сеттингс (бд)

    
    def add(self, product, quantity=1, update_quantity=False): # product - это какая то сущность в бд
        """
        Добавить продукт в корзину или обновить его количество.
        """
        product_id = str(product.id)
        # получается корзина - это просто строка - словарь, где ключ - это айдишник, а его значение - еще один словарик с данными (словарь в словаре)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                    'price': str(product.price)} # цена у сущности - price
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()


    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True


    def remove(self, product):
        """
        Удаление товара из корзины.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def __iter__(self): # здесь особое внимание, ибо здесь уже запросы непосредственно к базе данных
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        product_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        products = Processor.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

            # Yield это ключевое слово, которое используется примерно как return — отличие в том, что функция вернёт генератор.
            # Генератор - это тоже итерируемый объект (т.е. его можно прогнать через цикл for и получить каждый элемент), но прочитать его можно лишь один раз.
            # Это связано с тем, что он не хранит значения в памяти, а генерируют их на лету:
            # максимально просто - это хитровыебанный return перебором циклом for


    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())


    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in
                self.cart.values())


    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True