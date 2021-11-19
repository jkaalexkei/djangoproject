from django import http
from django.http import HttpResponse
from django.shortcuts import render


def inicio(request):  
    
    saludo = 'hola'
    
    return render(request,'index.html',{
        
        'saludo': saludo,
    })

def login(request):
    return render(request,'login.html',{
        
    })




# def suma(request):
#     operacion = input('ingrese el tipo de operacion: ')
#     if operacion == 'suma':
#         return HttpResponse(solosuma())
#     elif operacion == 'resta':
#         a = int(input('ingrese el primer numero: '))
#         b = int(input('ingrese el segundo numero: '))
#         c = a - b
#         return HttpResponse('la resta es: {}'.format(str(c)))
#     elif operacion == 'multiplicacion':
#         a = int(input('ingrese el primer numero: '))
#         b = int(input('ingrese el segundo numero: '))
#         c = a * b
#         return HttpResponse('la multiplicación es: {}'.format(str(c)))
#     elif operacion == 'division':
#         a = int(input('ingrese el primer numero: '))
#         b = int(input('ingrese el segundo numero: '))
#         c = a / b
#         return HttpResponse('la division es: {}'.format(str(c)))
#     else:
#         return HttpResponse('operacion no especificada')


# def solosuma():
#     a = int(input('ingrese el primer numero: '))
#     b = int(input('ingrese el segundo numero: '))
#     c = a + b
#     return ('la suma es: {}'.format(str(c)))
      
    