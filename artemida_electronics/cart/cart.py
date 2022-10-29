from decimal import Decimal
from django.conf import settings
from mainapp.models import Processor, Motherboard, Cooler, RAM, HDD, SSD_M2, SSD_sata, Videocard, Power_block, Corpus


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

    
    def add(self, product, quantity=1, update_quantity='None'): # product - это какая то сущность в бд
        """
        Добавить продукт в корзину или обновить его количество.
        """
        product_id = str(product.id) # получаем его айдишник
        product_type = str(product.__class__.__name__) # и его тип (Это видеокарта или процессор и т.д. )
        product_info = f'{product_type}*{product_id}'

        # получается корзина - это просто строка - словарь, где ключ - это айдишник + тип, а его значение - еще один словарик с данными (словарь в словаре)
        if product_info not in self.cart:
            self.cart[product_info] = {'quantity': 0, 'price': str(product.price)} # цена у сущности - price

        if update_quantity == 'None':
            self.cart[product_info]['quantity'] = quantity
        else:
            if update_quantity == 'Plus':
                self.cart[product_info]['quantity'] += 1
            elif self.cart[product_info]['quantity'] > 1:
                self.cart[product_info]['quantity'] -= 1
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
        product_id = str(product.id) # получаем его айдишник
        product_type = str(product.__class__.__name__) # и его тип (Это видеокарта или процессор и т.д. )
        product_info = f'{product_type}*{product_id}'

        if product_info in self.cart:
            del self.cart[product_info]
            self.save()


    def __iter__(self): # здесь особое внимание, ибо здесь уже запросы непосредственно к базе данных
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        products = self.cart.keys()

        for product in products:

            product_split = str(product).split('*')

            #Да, костыльно и топорно, но надо так отдельно для каждого типа продукта
            
            if(product_split[0] == 'Processor'):

                product2 = Processor.objects.filter(id=product_split[1])
          
                for product3 in product2:
                    product3_id = str(product3.id)
                    product3_type = str(product3.__class__.__name__)
                    product3_info = f'{product3_type}*{product3_id}'
               
                    self.cart[product3_info]['product'] = product3             

            elif(product_split[0] == 'Motherboard'):

                product2 = Motherboard.objects.filter(id=product_split[1])
    
                for product3 in product2:
                    product3_id = str(product3.id)
                    product3_type = str(product3.__class__.__name__)
                    product3_info = f'{product3_type}*{product3_id}'
             
                    self.cart[product3_info]['product'] = product3

            elif(product_split[0] == 'Cooler'):
     
                product2 = Cooler.objects.filter(id=product_split[1])
         
                for product3 in product2:
                    product3_id = str(product3.id)
                    product3_type = str(product3.__class__.__name__)
                    product3_info = f'{product3_type}*{product3_id}'
           
                    self.cart[product3_info]['product'] = product3

            elif(product_split[0] == 'HDD'):
        
                product2 = HDD.objects.filter(id=product_split[1])
          
                for product3 in product2:
                    product3_id = str(product3.id)
                    product3_type = str(product3.__class__.__name__)
                    product3_info = f'{product3_type}*{product3_id}'
         
                    self.cart[product3_info]['product'] = product3

            elif(product_split[0] == 'SSD_M2'):
    
                product2 = SSD_M2.objects.filter(id=product_split[1])
      
                for product3 in product2:
                    product3_id = str(product3.id)
                    product3_type = str(product3.__class__.__name__)
                    product3_info = f'{product3_type}*{product3_id}'
          
                    self.cart[product3_info]['product'] = product3

            elif(product_split[0] == 'SSD_sata'):
    
                product2 = SSD_sata.objects.filter(id=product_split[1])
         
                for product3 in product2:
                    product3_id = str(product3.id)
                    product3_type = str(product3.__class__.__name__)
                    product3_info = f'{product3_type}*{product3_id}'
            
                    self.cart[product3_info]['product'] = product3

            elif(product_split[0] == 'RAM'):
   
                product2 = RAM.objects.filter(id=product_split[1])

                for product3 in product2:
                    product3_id = str(product3.id)
                    product3_type = str(product3.__class__.__name__)
                    product3_info = f'{product3_type}*{product3_id}'
      
                    self.cart[product3_info]['product'] = product3

            elif(product_split[0] == 'Videocard'):
         
                product2 = Videocard.objects.filter(id=product_split[1])
         
                for product3 in product2:
                    product3_id = str(product3.id)
                    product3_type = str(product3.__class__.__name__)
                    product3_info = f'{product3_type}*{product3_id}'
           
                    self.cart[product3_info]['product'] = product3

            elif(product_split[0] == 'Power_block'):
         
                product2 = Power_block.objects.filter(id=product_split[1])
          
                for product3 in product2:
                    product3_id = str(product3.id)
                    product3_type = str(product3.__class__.__name__)
                    product3_info = f'{product3_type}*{product3_id}'
       
                    self.cart[product3_info]['product'] = product3

            elif(product_split[0] == 'Corpus'):
    
                product2 = Corpus.objects.filter(id=product_split[1])
           
                for product3 in product2:
                    product3_id = str(product3.id)
                    product3_type = str(product3.__class__.__name__)
                    product3_info = f'{product3_type}*{product3_id}'
           
                    self.cart[product3_info]['product'] = product3


        # получение объектов product и добавление их в корзину
        #products = Processor.objects.filter(id__in=product_ids)
        #for product in products:
            #self.cart[product]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

            # Yield это ключевое слово, которое используется примерно как return — отличие в том, что функция вернёт генератор.
            # Генератор - это тоже итерируемый объект (т.е. его можно прогнать через цикл for и получить каждый элемент), но прочитать его можно лишь один раз.
            # Это связано с тем, что он не хранит значения в памяти, а генерируют их на лету:
            # максимально просто - это хитровыебанный return перебором циклом for


    def len(self):
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