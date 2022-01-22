numeroMaximo = int(input('Digite um número:'))
listaDePrimos = []
numeroPrimo = 2

while numeroPrimo <= numeroMaximo:
    
#verificador de números primos
    verificador = 1
    contador = 0
 
    while verificador <= numeroPrimo:

        if numeroPrimo%verificador == 0:
            verificador+=1
            contador+=1
        else:
            verificador+=1

    if contador == 2:
        listaDePrimos.append(numeroPrimo)
        numeroPrimo+=1

    else:
        numeroPrimo+=1
#

print(listaDePrimos)
