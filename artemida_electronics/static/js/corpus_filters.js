var filter_vue = new Vue({
    el: '.products',
    delimiters: ['[[', ']]'],
    data: {
        manufacturer: [], 
        price: [],
        products: [], // список все х товаров
        products_filter: [], // список товаров, удовлетворяющих фильтрам
        products_filter2: [],
        proc_filter: [],
        result: false,
        
    },

    watch: {
        manufacturer: function(){ // при смене фильтра для процов
            console.log("Ya tut");
            this.filter();
        },

        price: function(){
            this.filter();
        },
    },



    mounted:function(){
        this.load() //этот метод вызывается при загрузке страницы
    },

    methods: {
        load()
        {  
            this.products = [];
            var db = document.getElementsByClassName('box__card');      

            for(let pr of db)
            {
                this.products.push(pr.children[2].children[0].value)
            }
        },

        price_up()
        {     
            window.location.href = `/corpuses?filter=price_up`; 
        },

        price_down()
        {       
            window.location.href = `/corpuses?filter=price_down`;
        },

        filter()
        {
            this.products_filter = []; // обнуляю список продуктов, удовлетворяющих фильтру
            this.proc_filter = [];
            this.products_filter2 = [];
            this.result = true;
            

            if(this.manufacturer != '') // выбран ли этот фильтр
            {
                for(product of this.products) // самый первый фильтр проверяет тупо все продукты
                {
                    pr = product.split('%%');
                    for(manuf of this.manufacturer)
                    {
                        if(pr[0].toLowerCase().indexOf(manuf.toLowerCase()) != -1)
                        {
                            this.products_filter.push(product);
                        }
                    }
                }

                if(this.products_filter == '')
                {
                    this.result = false;
                }

            }

        
            

            if(this.result == true)
            {
                if(this.price != '') // проверка есть ли фильтр
                {
                    this.products_filter2 = [];
                    if(this.products_filter != '') // есть ли в списке продуктов фильтра что то
                    {                              // если есть, то дальше работаю с ним
                        for(product of this.products_filter) 
                        {
                            pr = product.split('%%'); 
                            for(pric of this.price)
                            {
                                pric = pric.split('-');
    
                                if(parseFloat(pr[3].replace(',', '.')) >= parseFloat(pric[0]) && parseFloat(pr[3].replace(',', '.')) <= parseFloat(pric[1]))
                                {
                                    this.products_filter2.push(product);
                                }
                            }
                        }
                        
                    }
                    else // если нет, то работаю со всеми продуктами
                    {
                        for(product of this.products) 
                        {
                            pr = product.split('%%'); 
                            for(pric of this.price)
                            {
                                pric = pric.split('-');
    
                                if(parseFloat(pr[3].replace(',', '.')) >= parseFloat(pric[0]) && parseFloat(pr[3].replace(',', '.')) <= parseFloat(pric[1]))
                                {
                                    this.products_filter2.push(product);
                                }
                            }
                        }
                    }
                    if(this.products_filter2 != '')
                    {
                        this.products_filter = [];
                        this.products_filter = this.products_filter2;
                    }
                    else
                    {
                        this.result = false;
                    }
                }
            }


            if(this.result == true)
            {
                for(product of this.products_filter) 
                {
                    pr = product.split('%%'); 
                    this.proc_filter.push(pr[1]);
                }

                
            }
            else
            {
                //alert("По таким фильтрам ничего не найдено(");
                this.proc_filter = ['not_found'];
            }
            
       
        },      
    }  
})
