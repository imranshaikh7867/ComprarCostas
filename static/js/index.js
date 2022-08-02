console.log("hello");

let id = document.querySelector('.main-cart').id;
let sliced = id.slice(-1);

let minusBtn = document.getElementById('minus' + sliced);
let plusBtn = document.getElementById('plus' + sliced);
let count = document.getElementById('count' + sliced);
let price = document.getElementById('price' + sliced);
let originalprice = parseInt(price.innerHTML);

minusBtn.addEventListener('click', function(){
    let value = localStorage.getItem('value' + sliced);
    if (value == null) {
        valueno = []
    }
    else{
        valueno = JSON.parse(value)
    }
    val = parseInt(count.innerHTML);
    val = val - 1;
    val = Math.max(0, val);
    valueno.push(val);
    localStorage.setItem('value' + sliced, JSON.stringify(valueno));
    count.innerHTML = val;
    priceCal(count)
    
});
// let k = localStorage.getItem('value');
// console.log(k)
plusBtn.addEventListener('click', function(){
    let value = localStorage.getItem('value' + sliced);
    if (value == null) {
        valueno = []
    }
    else{
        valueno = JSON.parse(value)
    }
    val = parseInt(count.innerHTML);
    val = val + 1;
    val = Math.max(0, val);
    valueno.push(val);
    localStorage.setItem('value' + sliced, JSON.stringify(valueno));
    count.innerHTML = val;
    priceCal(count);
})

count.innerHTML = JSON.parse(localStorage.getItem('value' + sliced)).slice(-1)[0];
function priceCal(count){
    let k = parseInt(count.innerHTML);
    let value = localStorage.getItem('price' + sliced);
    if (value == null) {
        valueno = []
    }
    else{
        valueno = JSON.parse(value)
    }

    let total = k * originalprice;
    valueno.push(total);
    localStorage.setItem('price' + sliced, JSON.stringify(valueno));
    price.innerHTML = total;
}

price.innerHTML = JSON.parse(localStorage.getItem('price' + sliced)).slice(-1)[0];