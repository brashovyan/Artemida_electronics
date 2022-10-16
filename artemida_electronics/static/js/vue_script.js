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
      tdp: 0, // тепловыделение проца
      ram: [], // выбранная оперативка
      cooler: "", // выбранный кулер
      videocard: "", //выбранная видюха
      v_power: 0, // необходимая мощность бп для видеокарты
      power_block: "", // выбранный бп 
      m2_slots_mother: 0, // кол-во м2 слотов в материнке
      m2_slots: 0, // занятые m2 слоты
      sata_slots_mother: 0, // кол-во сата слотов в материнке
      sata_slots: 0, // кол-во занятых сата слотов
      ssd_m2: [], // выбранные ссд м2
      hdd: [], // выбранные HDD
      ssd_sata: [],
      corpus: "", // выбранный корпус

      filter_proc: [], // фильтры для процессоров
      filter_ram: [],

      result: "Сборка не завершена! Выберите недостающие комплектующие.",
    },

    watch: {
        filter_proc: function(){ // при смене фильтра для процов
            for(let pr of product)
            {
                if(pr.children[0].name !== 'videocard' && pr.children[0].name !== 'power_block' && pr.children[0].name !== 'corpus')
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
            this.ssd_m2 = [];
            this.hdd = [];
            this.tdp = 0;
            this.cooler = "";
            this.m2_slots_mother=0;
            this.m2_slots=0;
            this.sata_slots_mother=0;
            this.sata_slots=0;
            this.filter_ram = [];
            document.querySelector(".result__price").textContent = this.sum;
            this.price();
            //alert('lf');
        },

        filter_ram: function()
        {
            this.slots = 0;
            this.size_memory = 0;
            this.ram = [];
            
            for(let pr of product)
            {
                if(pr.children[0].name == 'RAM')
                {
                    pr.children[0].checked = false;
                    pr.children[1].style.display = "none"; // если галочка убрана, убираем инпут кол-ва
                    pr.children[1].children[0].children[1].value = 0;
                }
            }
            this.price();
        },
    },

    methods: {
        select_processor(title, id) // выбор процессора
        {
            //title = title.substr(0, title.length - id.length); // убираем айдишник с названия (он нужен для уникальности, ибо сущности разные, айди повторяются)
            product = document.querySelectorAll(".product"); // обновляем список продуктов, который сейчас видит пользователь
            this.processor = "";
            this.socket = "";
            for(let pr of product) // для всех продуктов
            {
                let str = pr.children[0].value.split('%%') //берем название (оно есть у всех и оно всегда первое)
                if(pr.children[0].checked == true && pr.children[0].name == 'processor' && title == str[0] && id == str[1]) // если кнопка выбрана и это то, что я нажал
                {
                    this.socket = str[2];
                    //this.processor = pr.children[0].name.substr(0, pr.children[0].name.length-id.length)
                    this.processor = str[0];
                    this.max_memory_proc = parseFloat(str[7]);
                    this.m_frequency_proc = parseFloat(str[5]);
                    this.tdp = Number(str[8]);
                }
                else if(pr.children[0].name !== 'videocard' && pr.children[0].name !== 'power_block' && pr.children[0].name !== 'corpus')
                {
                    pr.children[0].checked = false;
                    this.motherboard = "";
                    this.type_memory = "";
                    this.m_slots = 0;
                    this.slots = 0;
                    this.size_memory = 0;
                    this.ram = [];
                    this.ssd_m2 = [];
                    this.hdd = [];
                    this.ssd_sata = [];
                    this.cooler = "";
                    this.m2_slots_mother=0;
                    this.m2_slots=0;
                    this.sata_slots_mother=0;
                    this.sata_slots=0;
                    this.filter_ram = [];
                }
            }
            
            this.price();
        },

        select_motherboard(title, id) //выбор материнки
        {
            product = document.querySelectorAll(".product"); // обновляем список продуктов, который сейчас видит пользователь
            //title = title.substr(0, title.length - id.length); // нормальное название, на которое я нажал
            this.motherboard = "";
            for(let pr of product)
            {
                let str = pr.children[0].value.split('%%')
                if(pr.children[0].checked == true && title == str[0] && pr.children[0].name == 'motherboard' && id == str[1])
                {
                    this.motherboard = str[0];
                    this.m_slots = Number(str[4]);
                    this.type_memory = str[7];
                    this.m2_slots_mother = Number(str[8]);
                    this.sata_slots_mother = Number(str[9]);

                    if(parseFloat(str[6]) < this.max_memory_proc)
                    {
                        this.max_memory = parseFloat(str[6]);
                    }
                    else
                    {
                        this.max_memory = this.max_memory_proc;
                    }

                    if(parseFloat(str[5]) < this.m_frequency_proc)
                    {
                        this.m_frequency = parseFloat(str[5]);
                    }
                    else
                    {
                        this.m_frequency = this.m_frequency_proc;
                    }
                }
                else if(pr.children[0].name !== 'motherboard' && pr.children[0].name !== 'processor' && pr.children[0].name !== 'cooler' && pr.children[0].name !== 'videocard' && pr.children[0].name !== 'power_block' && pr.children[0].name !== 'corpus') // иначе сбрасываю всё кроме проца и матери
                {
                    pr.children[0].checked = false;
                    this.slots = 0;
                    this.size_memory = 0;
                    this.ram = [];
                    this.ssd_m2 = [];
                    this.hdd = [];
                    this.ssd_sata = [];
                    this.m2_slots=0;
                    this.sata_slots=0;
                    if(pr.children[0].name == 'RAM' || pr.children[0].name == 'ssd_m2' || pr.children[0].name == 'hdd')
                    {
                        pr.children[1].style.display = "none";
                        pr.children[1].children[0].children[1].value = 0;
                    }
                    this.filter_ram = [];
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
            //title = title.substr(0, title.length - id.length); // нормальное название, на которое я нажал
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

                        this.size_memory = this.size_memory + (parseFloat(str[2]) * parseFloat(pr.children[1].children[0].children[1].value));
                        //console.log(parseFloat(str[1]));

                }
            }

            for(let pr of product)
            {
                let str = pr.children[0].value.split('%%')



                if(title == str[0] && pr.children[0].name == 'RAM' && id == str[1]) // если нашли то, что мы тыкнули
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
                            this.size_memory += parseFloat(str[2]);
                        }
                        
                        if(Number(this.slots) > this.m_slots) // если мы превысили кол-во слотов 
                        {
                            pr.children[1].children[0].children[1].value = Number(pr.children[1].children[0].children[1].value) - Number(1);  
                            this.slots = this.m_slots;
                            this.size_memory = this.size_memory - parseFloat(str[2]);
                        }

                        if(parseFloat(this.max_memory) < parseFloat(this.size_memory)) // если мы превысили допустимый объём памяти
                        {
                            pr.children[1].children[0].children[1].value = Number(pr.children[1].children[0].children[1].value) - Number(1);
                            this.slots = parseFloat(this.slots) - Number(1);
                            this.size_memory = this.size_memory - parseFloat(str[2]);
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
            //title = title.substr(0, title.length - id.length); // убираем айдишник с названия (он нужен для уникальности, ибо сущности разные, айди повторяются)
            product = document.querySelectorAll(".product"); // обновляем список продуктов, который сейчас видит пользователь
            for(let pr of product) // для всех продуктов
            {
                let str = pr.children[0].value.split('%%') //берем название (оно есть у всех и оно всегда первое)
                if(pr.children[0].checked == true && pr.children[0].name == 'cooler' && title == str[0] && id == str[1]) // если кнопка выбрана и это то, что я нажал
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
            //title = title.substr(0, title.length - id.length);
            product = document.querySelectorAll(".product");
            for(let pr of product) // для всех продуктов
            {
                let str = pr.children[0].value.split('%%') //берем название (оно есть у всех и оно всегда первое)
                if(pr.children[0].checked == true && pr.children[0].name == 'videocard' && title == str[0] && id == str[1]) // если кнопка выбрана и это то, что я нажал
                {
                    this.videocard = str[0];
                    this.v_power = parseFloat(str[2]);
                }
                else if(pr.children[0].name == 'power_block')
                {
                    pr.children[0].checked = false;
                    this.power_block = "";
                }
            }
            
            this.price();

        },

        select_power_block(title, id)
        {
            //title = title.substr(0, title.length - id.length);
            product = document.querySelectorAll(".product");
            for(let pr of product) // для всех продуктов
            {
                let str = pr.children[0].value.split('%%') //берем название (оно есть у всех и оно всегда первое)
                if(pr.children[0].checked == true && pr.children[0].name == 'power_block' && title == str[0] && id == str[1]) // если кнопка выбрана и это то, что я нажал
                {
                    this.power_block = str[0];
                }
                else
                {
                    
                }
            }
            
            this.price();
        },

        select_ssd_m2_plus(title, id) // инпут кол-ва ссд м2
        {          
            product = document.querySelectorAll(".number_ssd"); // ищу все инпуты для кол-ва ssd
            for(let pr of product)
            {
                if(pr.children[1].name == title) // если это то, что я нажал
                {
                    pr.children[1].value = Number(pr.children[1].value) + Number(1); 
                    this.select_ssd_m2(title, id);
                }
            }
        },

        select_ssd_m2_minus(title, id) // инпут кол-ва ссд м2
        {
            product = document.querySelectorAll(".number_ssd"); // ищу все инпуты для кол-ва ssd
            for(let pr of product)
            {

                if(pr.children[1].name == title) // если это то, что я нажал
                {
                    
                    if(pr.children[1].value > 0)
                    {
                        pr.children[1].value = Number(pr.children[1].value) - Number(1); 
                        this.select_ssd_m2(title, id);
                    }
                    
                }
            }
        },

        select_ssd_m2(title, id)
        {
            //title = title.substr(0, title.length - id.length);
            product = document.querySelectorAll(".product");
            this.m2_slots = 0;

            for(let pr of product)
            {
                let str = pr.children[0].value.split('%%')
                if(pr.children[0].name == 'ssd_m2' && pr.children[0].checked == true)
                {
                        this.m2_slots = this.m2_slots + Number(pr.children[1].children[0].children[1].value);
                        // сначала считаем сколько слотов уже занято
                }
            }

            for(let pr of product)
            {
                let str = pr.children[0].value.split('%%')

                if(title == str[0] && pr.children[0].name == 'ssd_m2' && id == str[1]) // если нашли то, что мы тыкнули
                {
                    if(pr.children[0].checked == true) // если галочка стоит, то показываем инпут кол-ва
                    {
                        pr.children[1].style.display = "block";
                        if(pr.children[1].children[0].children[1].value == "") // если там пустота, то по умолчанию 0
                        {
                            pr.children[1].children[0].children[1].value = 0;
                        }

                        if(this.m2_slots === 0) // если все слоты пустые, то по умолчанию кол-во 1
                        {
                            pr.children[1].children[0].children[1].value = 1;
                            this.m2_slots += 1;
                            //this.size_memory += parseFloat(str[1]);
                        }
                        
                        if(Number(this.m2_slots) > this.m2_slots_mother) // если мы превысили кол-во слотов 
                        {
                            pr.children[1].children[0].children[1].value = Number(pr.children[1].children[0].children[1].value) - Number(1);  

                            this.m2_slots = this.m2_slots_mother;
                            //this.size_memory = this.size_memory - parseFloat(str[1]);
                        }

                        /*if(parseFloat(this.max_memory) < parseFloat(this.size_memory)) // если мы превысили допустимый объём памяти
                        {
                            pr.children[1].children[0].children[1].value = Number(pr.children[1].children[0].children[1].value) - Number(1);
                            this.slots = parseFloat(this.slots) - Number(1);
                            this.size_memory = this.size_memory - parseFloat(str[1]);
                        }*/
                    }
                    else
                    {
                        pr.children[1].style.display = "none"; // если галочка убрана, убираем инпут кол-ва
                        pr.children[1].children[0].children[1].value = 0;
                    }
                }
            }
            this.price();
        },

        select_hdd_plus(title, id) // инпут кол-ва ссд м2
        {          
            product = document.querySelectorAll(".number_hdd"); // ищу все инпуты для кол-ва ssd
            for(let pr of product)
            {
                if(pr.children[1].name == title) // если это то, что я нажал
                {
                    pr.children[1].value = Number(pr.children[1].value) + Number(1); 
                    this.select_hdd(title, id);
                }
            }
        },

        select_hdd_minus(title, id) // инпут кол-ва ссд м2
        {
            product = document.querySelectorAll(".number_hdd"); // ищу все инпуты для кол-ва ssd
            for(let pr of product)
            {

                if(pr.children[1].name == title) // если это то, что я нажал
                {
                    
                    if(pr.children[1].value > 0)
                    {
                        pr.children[1].value = Number(pr.children[1].value) - Number(1); 
                        this.select_hdd(title, id);
                    }
                    
                }
            }
        },

        select_hdd(title, id)
        {
            //title = title.substr(0, title.length - id.length);
            product = document.querySelectorAll(".product");
            this.sata_slots = 0;

            for(let pr of product)
            {
                let str = pr.children[0].value.split('%%')
                if((pr.children[0].name == 'hdd' && pr.children[0].checked == true) || (pr.children[0].name == 'ssd_sata' && pr.children[0].checked == true))
                {
                        this.sata_slots = this.sata_slots + Number(pr.children[1].children[0].children[1].value);
                        // сначала считаем сколько слотов уже занято
                }
            }

            for(let pr of product)
            {
                let str = pr.children[0].value.split('%%')

                if(title == str[0] && pr.children[0].name == 'hdd' && id == str[1]) // если нашли то, что мы тыкнули
                {
                    if(pr.children[0].checked == true) // если галочка стоит, то показываем инпут кол-ва
                    {
                        pr.children[1].style.display = "block";
                        if(pr.children[1].children[0].children[1].value == "") // если там пустота, то по умолчанию 0
                        {
                            pr.children[1].children[0].children[1].value = 0;
                        }

                        if(this.sata_slots === 0) // если все слоты пустые, то по умолчанию кол-во 1
                        {
                            pr.children[1].children[0].children[1].value = 1;
                            this.sata_slots += 1;
                            //this.size_memory += parseFloat(str[1]);
                        }
                        
                        if(Number(this.sata_slots) > this.sata_slots_mother) // если мы превысили кол-во слотов 
                        {
                            pr.children[1].children[0].children[1].value = Number(pr.children[1].children[0].children[1].value) - Number(1);  

                            this.sata_slots = this.sata_slots_mother;
                            //this.size_memory = this.size_memory - parseFloat(str[1]);
                        }

                        /*if(parseFloat(this.max_memory) < parseFloat(this.size_memory)) // если мы превысили допустимый объём памяти
                        {
                            pr.children[1].children[0].children[1].value = Number(pr.children[1].children[0].children[1].value) - Number(1);
                            this.slots = parseFloat(this.slots) - Number(1);
                            this.size_memory = this.size_memory - parseFloat(str[1]);
                        }*/
                    }
                    else
                    {
                        pr.children[1].style.display = "none"; // если галочка убрана, убираем инпут кол-ва
                        pr.children[1].children[0].children[1].value = 0;
                    }
                }
            }
            this.price();
        },

        select_ssd_sata_plus(title, id) // инпут кол-ва ссд м2
        {          
            product = document.querySelectorAll(".number_ssds"); // ищу все инпуты для кол-ва ssd
            for(let pr of product)
            {
                if(pr.children[1].name == title) // если это то, что я нажал
                {
                    pr.children[1].value = Number(pr.children[1].value) + Number(1); 
                    this.select_ssd_sata(title, id);
                }
            }
        },

        select_ssd_sata_minus(title, id) // инпут кол-ва ссд м2
        {
            product = document.querySelectorAll(".number_ssds"); // ищу все инпуты для кол-ва ssd
            for(let pr of product)
            {

                if(pr.children[1].name == title) // если это то, что я нажал
                {
                    
                    if(pr.children[1].value > 0)
                    {
                        pr.children[1].value = Number(pr.children[1].value) - Number(1); 
                        this.select_ssd_sata(title, id);
                    }
                }
            }
        },

        select_ssd_sata(title, id)
        {
            //title = title.substr(0, title.length - id.length);
            product = document.querySelectorAll(".product");
            this.sata_slots = 0;
            
            for(let pr of product)
            {
                let str = pr.children[0].value.split('%%')
                if((pr.children[0].name == 'hdd' && pr.children[0].checked == true) || (pr.children[0].name == 'ssd_sata' && pr.children[0].checked == true))
                {
                        this.sata_slots = this.sata_slots + Number(pr.children[1].children[0].children[1].value);
                        // сначала считаем сколько слотов уже занято
                }
            }

            for(let pr of product)
            {
                let str = pr.children[0].value.split('%%')

                if(title == str[0] && pr.children[0].name == 'ssd_sata' && id == str[1]) // если нашли то, что мы тыкнули
                {
                    if(pr.children[0].checked == true) // если галочка стоит, то показываем инпут кол-ва
                    {
                        pr.children[1].style.display = "block";
                        if(pr.children[1].children[0].children[1].value == "") // если там пустота, то по умолчанию 0
                        {
                            pr.children[1].children[0].children[1].value = 0;
                        }

                        if(this.sata_slots === 0) // если все слоты пустые, то по умолчанию кол-во 1
                        {
                            pr.children[1].children[0].children[1].value = 1;
                            this.sata_slots += 1;
                            //this.size_memory += parseFloat(str[1]);
                        }
                        
                        if(Number(this.sata_slots) > this.sata_slots_mother) // если мы превысили кол-во слотов 
                        {
                            pr.children[1].children[0].children[1].value = Number(pr.children[1].children[0].children[1].value) - Number(1);  

                            this.sata_slots = this.sata_slots_mother;
                            //this.size_memory = this.size_memory - parseFloat(str[1]);
                        }

                        /*if(parseFloat(this.max_memory) < parseFloat(this.size_memory)) // если мы превысили допустимый объём памяти
                        {
                            pr.children[1].children[0].children[1].value = Number(pr.children[1].children[0].children[1].value) - Number(1);
                            this.slots = parseFloat(this.slots) - Number(1);
                            this.size_memory = this.size_memory - parseFloat(str[1]);
                        }*/
                    }
                    else
                    {
                        pr.children[1].style.display = "none"; // если галочка убрана, убираем инпут кол-ва
                        pr.children[1].children[0].children[1].value = 0;
                    }
                }
            }
            this.price();
        },

        select_corpus(title, id)
        {
            //title = title.substr(0, title.length - id.length);
            product = document.querySelectorAll(".product");
            for(let pr of product) // для всех продуктов
            {
                let str = pr.children[0].value.split('%%') //берем название (оно есть у всех и оно всегда первое)
                if(pr.children[0].checked == true && pr.children[0].name == 'corpus' && title == str[0] && id == str[1]) // если кнопка выбрана и это то, что я нажал
                {
                    this.corpus = str[0];
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
            this.ssd_m2 = [];
            this.hdd = [];
            this.ssd_sata = [];
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
                    else if(pr.children[0].name == "power_block")
                    {
                        this.sum = this.sum + parseFloat(str[str.length - 1]);
                        this.power_block = str[0];
                    }
                    else if(pr.children[0].name == 'ssd_m2') 
                    {
                        this.sum = this.sum + (parseFloat(str[str.length - 1])*parseFloat(pr.children[1].children[0].children[1].value)); // тут цену умножаем на кол-во
                        if(pr.children[1].children[0].children[1].value > 0)
                        {
                            this.ssd_m2.push(str[0] + ' - ' + pr.children[1].children[0].children[1].value + 'шт');
                        }
                    }
                    else if(pr.children[0].name == 'hdd') 
                    {
                        this.sum = this.sum + (parseFloat(str[str.length - 1])*parseFloat(pr.children[1].children[0].children[1].value)); // тут цену умножаем на кол-во
                        if(pr.children[1].children[0].children[1].value > 0)
                        {
                            this.hdd.push(str[0] + ' - ' + pr.children[1].children[0].children[1].value + 'шт');
                        }
                    }
                    else if(pr.children[0].name == 'ssd_sata') 
                    {
                        this.sum = this.sum + (parseFloat(str[str.length - 1])*parseFloat(pr.children[1].children[0].children[1].value)); // тут цену умножаем на кол-во
                        if(pr.children[1].children[0].children[1].value > 0)
                        {
                            this.ssd_sata.push(str[0] + ' - ' + pr.children[1].children[0].children[1].value + 'шт');
                        }
                    }
                    else if(pr.children[0].name == "corpus")
                    {
                        this.sum = this.sum + parseFloat(str[str.length - 1]);
                        this.corpus = str[0];
                    }
                }
            }
            document.querySelector(".result__price").textContent = this.sum;

            if(this.processor == "" || this.motherboard == "" || this.cooler == "" || this.ram == "" || this.videocard == "" || this.power_block == "" || (this.ssd_m2 == "" && this.hdd == "" && this.ssd_sata == ""))
            {
                this.result = "Сборка не завершена! Выберите недостающие комплектующие."
            }
            else
            {
                this.result = "Компьютер собран!"
            }
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
            this.ssd_m2 = [];
            this.hdd = [];
            this.ssd_sata = [];
            this.tdp = 0;
            this.cooler = "";
            this.videocard = "";
            this.v_power = 0;
            this.power_block = "";
            this.corpus = "";
            this.result = "Сборка не завершена! Выберите недостающие комплектующие.";
            document.querySelector(".result__price").textContent = this.sum;
        },

        order()
        {
            $.ajax({
                type: "GET",
                url: '/aja',
                data: {
                    "test": 'Тестим отправку заказа',
                },
                dataType: "json",
                success: function (data) {
                    // any process in data
                    alert("Заказ успешно оформлен! Вы будете перемещены на главную страницу.")
                    window.location.href = `/`;
                },
                failure: function () {
                    alert("Во время обработки заказа произошла ошибка!");
                }
            });
        },
    }
  })