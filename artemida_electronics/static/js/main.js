//product = document.querySelectorAll(".product");
//cost = document.querySelector(".result__cost");
//all = document.querySelector(".result__all");
//let sum = 0;
//let computer = [];

/*product.forEach(element => { element.addEventListener("change", function(){ // при выборе любого чекбокса запускается калькулятор
        sum = 0;
        computer = [];

        for(let pr of product)
        {
            if(pr.children[0].checked)
            {   
                sum = sum + parseInt(pr.children[0].value);
                computer.push(pr.children[0].name)
            }
        }
        
        all.textContent = computer;
        cost.textContent = sum;
    });
});*/

function showImg(elemId) // по нажатию на продукт появляется картинка с ссылкой
{
    var elem = document.getElementById(elemId);
    if(elem.style.display === "none" || elem.style.display == "")
    {
        elem.style.display = "block";
    }
    else
    {
        elem.style.display = "none";
    }
}