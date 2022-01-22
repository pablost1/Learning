def primo(p):
    contador = 1
    primo = False
    i = 0
    if p >=-1 and p <= 1:
        return False
    while contador <= p:
        if p%contador==0:
            i+=1
            if i>2:
                return primo
        contador+=1
    primo = True
    return primo
def distanciaEntrePrimo(a,x,b):
    contador = 0
    sequencia = []
    while contador <= x:
        sequencia.append(a*contador+b)
        contador+=1
    print('sequencia de primos:',sequencia)
    i = 0
    indice = []
    for x in sequencia:
        if primo(x):
            indice.append(i)
        i+=1
    print('indice:',indice)
    distancia = []    
    c = 0
    while c < len(indice)-1:
        distancia.append(abs(indice[c+1]-indice[c]))
        c+=1
    return print('distancia entre primos:',distancia)
