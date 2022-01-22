def divisores(numero):
    divisores = []
    for x in range(numero):
        if x>0 and numero%x==0:
            divisores.append(x)
    divisores.append(numero)
    return divisores
            
'''
lista = [4, 18, 76, 123]
listaDivisores = []
coprimos = []
for x in lista:
    listaDivisores.append(divisores(x))
for y in listaDivisores:
    contador = 0
    while contador < len(y):
        
        contador+=1
print(coprimos)
'''
'''
lista = [4, 18, 76, 123]
listaDivisores = []
coprimos = []
contador = 0
    
    contador+=1
'''

def coprimos(n1,n2):
    n1Divisores = divisores(6)
    n2Divisores = divisores(3)
    coprimos = True
    contador=0
    while contador < len(n2Divisores):
        for x in n1Divisores:
            if x>1 and x==n2Divisores[contador]:
                coprimos = False
        contador+=1
            
    return coprimos

n1Divisores = divisores(8)
n2Divisores = divisores(4)
coprimos = True
contador=0
while contador < len(n2Divisores):
    for x in n1Divisores:
        if x>1 and x==n2Divisores[contador]:
            coprimos = False
    contador+=1
            
