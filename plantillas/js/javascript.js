
const mas1 = document.getElementById('mas1');
const menos1 = document.getElementById('menos1');
const total1 = document.getElementById('input1');

mas1.addEventListener('click',function(){
 
    total1.value = parseInt(total1.value) + 1

})

menos1.addEventListener('click',function(){
 
    let valor = parseInt(total1.value)

    if (valor!=0){
        valor = valor - 1
    }
    total1.value = valor
})

/*--------------segundo articulo -------------*/

const mas2 = document.getElementById('mas2')
const menos2 = document.getElementById('menos2')
const total2 = document.getElementById('input2')

mas2.addEventListener('click',function(){
    total2.value = parseInt(total2.value) + 1
})

menos2.addEventListener('click',function(){
    let valor2 = parseInt(total2.value)

    if (valor2 != 0){
        valor2 = valor2 - 1
    }

    total2.value = valor2

})

/* ----------- tercer articulo---------*/

const mas3 = document.getElementById('mas3')
const menos3 = document.getElementById('menos3')
const total3 = document.getElementById('input3')

mas3.addEventListener('click',function(){
    total3.value = parseInt(total3.value) + 1
})

menos3.addEventListener('click',function(){
    let valor3 = parseInt(total3.value)

    if (valor3 != 0){
        valor3 = valor3 - 1
    }

    total3.value = valor3

})

/* ----------- cuarto articulo---------*/

const mas4 = document.getElementById('mas4')
const menos4 = document.getElementById('menos4')
const total4 = document.getElementById('input4')

mas4.addEventListener('click',function(){
    total4.value = parseInt(total4.value) + 1
})

menos4.addEventListener('click',function(){
    let valor4 = parseInt(total4.value)

    if (valor4 != 0){
        valor4 = valor4 - 1
    }

    total4.value = valor4

})