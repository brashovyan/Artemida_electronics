var builder = new Vue({
    el: '.main',
    delimiters: ['[[', ']]'],
    data: {
      processor: "", // выбранный процессор
      motherboard: "", // выбранная материнка
      sum: 0, // итоговая стоимость
      socket: "", // текущий сокет
      m_slots: 0, // кол-во слотов для ОЗУ
      slots: 0, // занятые слоты
      type_memory: "", // тип ОЗУ
      max_memory: 0, // максимальный объём ОЗУ
      size_memory: 0, // текущий объём ОЗУ
      m_frequency: 0, // допустимая частота ОЗУ
      max_memory_proc: 0, // максимальный объём памяти для проца
      m_frequency_proc: 0, // допустимая частота ОЗУ для проца
      tdp: 0,
      ram: [],
      cooler: "",
      videocard: "",

      filter_proc: [],

      //product: document.querySelectorAll(".product"),
      //cost: document.querySelector(".result__cost"),
      //all: document.querySelector(".result__all"),
    },

    watch: {
        filter_proc: function(){
            for(let pr of product)
            {
                if(pr.children[0].name != 'videocard')
                {
                    pr.children[0].checked = false;
                }
            }

            this.processor = "";
            this.motherboard = "";
            this.sum = 0;
            this.socket= "";
            this.type_memory = "";
            this.m_slots = 0;
            this.slots = 0;
            this.max_memory = 0;
            this.size_memory = 0;
            this.m_frequency = 0;
            this.max_memory_proc = 0;
            this.m_frequency_proc = 0;
            this.ram = [];
            this.tdp = 0;
            this.cooler = "";
            document.querySelector(".result__price").textContent = this.sum;
            document.querySelector(".result__processor").textContent = this.processor;
            document.querySelector(".result__motherboard").textContent = this.motherboard;
            document.querySelector(".result__cooler").textContent = this.cooler;
            this.price();
            //alert('lf');
        },

        videocard: function(){
            alert("Бери 1050ti");
        }
    },

    methods: {
        select_processor(title, id) // выбор процессора
        {
            title = title.substr(0, title.length - id.length); // убираем айдишник с названия (он нужен для уникальности, ибо сущности разные, айди повторяются)
            product = document.querySelectorAll(".product"); // обновляем список продуктов, который сейчас видит пользователь
            this.processor = "";
            this.socket = "";
            for(let pr of product) // для всех продуктов
            {
                let str = pr.children[0].value.split('%%') //берем название (оно есть у всех и оно всегда первое)
                if(pr.children[0].checked == true && pr.children[0].name == 'processor' && title == str[0]) // если кнопка выбрана и это то, что я нажал
                {
                    this.socket = str[1];
                    //this.processor = pr.children[0].name.substr(0, pr.children[0].name.length-id.length)
                    this.processor = str[0];
                    this.max_memory_proc = parseFloat(str[6]);
                    this.m_frequency_proc = parseFloat(str[4]);
                    this.tdp = Number(str[7]);
                }
                else // иначе я всё сбрасываю кроме процессора
                {
                    pr.children[0].checked = false;
                    this.motherboard = "";
                    this.type_memory = "";
                    this.m_slots = 0;
                    this.slots = 0;
                    this.size_memory = 0;
                    this.ram = [];
                    this.cooler = "";
                }
            }
            
            this.price();
        },

        select_motherboard(title, id) //выбор материнки
        {
            product = document.querySelectorAll(".product"); // обновляем список продуктов, который сейчас видит пользователь
            title = title.substr(0, title.length - id.length); // нормальное название, на которое я нажал
            this.motherboard = "";
            for(let pr of product)
            {
                let str = pr.children[0].value.split('%%')
                if(pr.children[0].checked == true && title == str[0] && pr.children[0].name == 'motherboard')
                {
                    this.motherboard = str[0];
                    this.m_slots = Number(str[3]);
                    this.type_memory = str[6];

                    if(parseFloat(str[5]) < this.max_memory_proc)
                    {
                        this.max_memory = parseFloat(str[5]);
                    }
                    else
                    {
                        this.max_memory = this.max_memory_proc;
                    }

                    if(parseFloat(str[4]) < this.m_frequency_proc)
                    {
                        this.m_frequency = parseFloat(str[4]);
                    }
                    else
                    {
                        this.m_frequency = this.m_frequency_proc;
                    }
                }
                else if(pr.children[0].name != 'motherboard' && pr.children[0].name != 'processor' && pr.children[0].name != 'cooler') // иначе сбрасываю всё кроме проца и матери
                {
                    pr.children[0].checked = false;
                    this.slots = 0;
                    this.size_memory = 0;
                    this.ram = [];
                    if(pr.children[0].name == 'RAM')
                    {
                        pr.children[1].style.display = "none";
                        pr.children[1].children[0].children[1].value = 0;
                    }
                }
            }
            this.price();
        },

        select_ram_plus(title, id) // инпут кол-ва озу плюс
        {          
            product = document.querySelectorAll(".number"); // ищу все инпуты для кол-ва
            for(let pr of product)
            {
                if(pr.children[1].name == title) // если это то, что я нажал
                {
                    pr.children[1].value = Number(pr.children[1].value) + Number(1); 
                    this.select_ram(title, id);
                }
            }
        },

        select_ram_minus(title, id) // инпут кол-ва озу минус
        {
            product = document.querySelectorAll(".number"); // ищу все инпуты для кол-ва
            for(let pr of product)
            {
                if(pr.children[1].name == title) // если это то, что я нажал
                {
                    if(pr.children[1].value > 0)
                    {
                        pr.children[1].value = Number(pr.children[1].value) - Number(1); 
                        this.select_ram(title, id);
                    }
                }
            }
        },

        select_ram(title, id) //выбор оперативки
        {
            product = document.querySelectorAll(".product"); // обновляем список продуктов, который сейчас видит пользователь
            title = title.substr(0, title.length - id.length); // нормальное название, на которое я нажал
            this.slots = 0;
            this.size_memory = 0;

            for(let pr of product)
            {
                let str = pr.children[0].value.split('%%')

                

                if(pr.children[0].name == 'RAM' && pr.children[0].checked == true)
                {
                        //console.log(pr.children[1].children[0].children[1].value);
                        this.slots = this.slots + Number(pr.children[1].children[0].children[1].value);
                        // сначала считаем сколько слотов уже занято

                        this.size_memory = this.size_memory + (parseFloat(str[1]) * parseFloat(pr.children[1].children[0].children[1].value));
                        //console.log(parseFloat(str[1]));

                }
            }

            for(let pr of product)
            {
                let str = pr.children[0].value.split('%%')



                if(title == str[0] && pr.children[0].name == 'RAM') // если нашли то, что мы тыкнули
                {
                    //console.log(this.slots);
                    if(pr.children[0].checked == true) // если галочка стоит, то показываем инпут кол-ва
                    {
                        pr.children[1].style.display = "block";
                        if(pr.children[1].children[0].children[1].value == "") // если там пустота, то по умолчанию 0
                        {
                            pr.children[1].children[0].children[1].value = 0;
                        }

                        if(this.slots === 0) // если все слоты пустые, то по умолчанию кол-во 1
                        {
                            pr.children[1].children[0].children[1].value = 1;
                            this.slots += 1;
                            this.size_memory += parseFloat(str[1]);
                        }
                        
                        if(Number(this.slots) > this.m_slots) // если мы превысили кол-во слотов 
                        {
                            pr.children[1].children[0].children[1].value = Number(pr.children[1].children[0].children[1].value) - Number(1);  // 
                            // по хорошему можно просто минус 1, но я могу инпут зажать и ввести например сто
                            // можно инпуту указать возможный максимум, но пока не могу этого сделать
                            this.slots = this.m_slots;
                            this.size_memory = this.size_memory - parseFloat(str[1]);
                        }

                        if(parseFloat(this.max_memory) < parseFloat(this.size_memory)) // если мы превысили допустимый объём памяти
                        {
                            pr.children[1].children[0].children[1].value = Number(pr.children[1].children[0].children[1].value) - Number(1);
                            this.slots = parseFloat(this.slots) - Number(1);
                            this.size_memory = this.size_memory - parseFloat(str[1]);
                        }
                    }
                    else
                    {
                        pr.children[1].style.display = "none"; // если галочка убрана, убираем инпут кол-ва
                        pr.children[1].children[0].children[1].value = 0;
                    }
                }

            }
            //console.log(this.size_memory);
            this.price();
        },

        select_cooler(title, id)
        {
            title = title.substr(0, title.length - id.length); // убираем айдишник с названия (он нужен для уникальности, ибо сущности разные, айди повторяются)
            product = document.querySelectorAll(".product"); // обновляем список продуктов, который сейчас видит пользователь
            for(let pr of product) // для всех продуктов
            {
                let str = pr.children[0].value.split('%%') //берем название (оно есть у всех и оно всегда первое)
                if(pr.children[0].checked == true && pr.children[0].name == 'cooler' && title == str[0]) // если кнопка выбрана и это то, что я нажал
                {
                    this.cooler = str[0];
                }
                else // иначе я всё сбрасываю кроме процессора
                {
                    
                }
            }
            
            this.price();
        },

        select_videocard(title, id)
        {
            title = title.substr(0, title.length - id.length);
            product = document.querySelectorAll(".product");
            for(let pr of product) // для всех продуктов
            {
                let str = pr.children[0].value.split('%%') //берем название (оно есть у всех и оно всегда первое)
                if(pr.children[0].checked == true && pr.children[0].name == 'videocard' && title == str[0]) // если кнопка выбрана и это то, что я нажал
                {
                    this.videocard = str[0];
                }
                else
                {
                    
                }
            }
            
            this.price();

        },



        price() // расчёт цены
        {
            //console.log("Меня вызвали");
            product = document.querySelectorAll(".product"); // обновляем список продуктов, который сейчас видит пользователь
            this.sum = 0;
            this.ram = [];
            for(let pr of product)
            {
                if(pr.children[0].checked) // ищем все "галочки"
                {
                    let str = pr.children[0].value.split('%%'); // парсим value

                    if(pr.children[0].name == 'processor') // если это процессор
                    {
                        this.processor = str[0];
                        this.sum = this.sum + parseFloat(str[str.length - 1]); // цена у всех указана последней
                    }
                    else if(pr.children[0].name == 'motherboard') // если это материнка
                    {
                        this.motherboard = str[0];
                        this.sum = this.sum + parseFloat(str[str.length - 1]); // цена у всех указана последней
                    }
                    else if(pr.children[0].name == 'RAM') // если это оперативка
                    {
                        this.sum = this.sum + (parseFloat(str[str.length - 1])*parseFloat(pr.children[1].children[0].children[1].value)); // тут цену умножаем на кол-во
                        if(pr.children[1].children[0].children[1].value > 0)
                        {
                            this.ram.push(str[0] + ' - ' + pr.children[1].children[0].children[1].value + 'шт');
                        }
                        
                    }
                    else if(pr.children[0].name == 'cooler')
                    {
                        this.sum = this.sum + parseFloat(str[str.length - 1]);
                        this.cooler = str[0];
                    }
                    else if(pr.children[0].name == "videocard")
                    {
                        this.sum = this.sum + parseFloat(str[str.length - 1]);
                        this.videocard = str[0];
                    }
                }
            }
            document.querySelector(".result__price").textContent = this.sum;
            document.querySelector(".result__processor").textContent = this.processor;
            document.querySelector(".result__motherboard").textContent = this.motherboard;
            document.querySelector(".result__cooler").textContent = this.cooler;
        },

        clear() // отчистка. Все сбрасывается, как будто мы перезагрузили страницу
        {
            for(let pr of product)
            {
                pr.children[0].checked = false;
            }

            this.processor = "";
            this.motherboard = "";
            this.sum = 0;
            this.socket= "";
            this.type_memory = "";
            this.m_slots = 0;
            this.slots = 0;
            this.max_memory = 0;
            this.size_memory = 0;
            this.m_frequency = 0;
            this.max_memory_proc = 0;
            this.m_frequency_proc = 0;
            this.ram = [];
            this.tdp = 0;
            this.cooler = "";
            this.videocard = "";
            document.querySelector(".result__price").textContent = this.sum;
            document.querySelector(".result__processor").textContent = this.processor;
            document.querySelector(".result__motherboard").textContent = this.motherboard;
            document.querySelector(".result__cooler").textContent = this.cooler;
            document.querySelector(".result__videocard").textContent = this.videocard;
        },
    }
  })