#Concatenação de Strings de uma lista
letras = ['s ','p ','d ','f ']
contador = 0
palavra = ''
while contador < len(letras):
    palavra+= letras[contador]
    print(palavra)
    contador+=1
    
#soma de numeros de uma lista
print()
numeros = [61,81,31,81,75]
contador = 0
total = 0
while contador < len(numeros):
    total+= numeros[contador]
    print(total)
    contador+=1
    
#numeros multiplos de 7
print()
numeros = [7,12,21,35,35,87]
contador = 0
while contador < len(numeros):
    if numeros[contador]%7 == 0:
        
        print(numeros[contador])

    contador+=1
    
    
    

