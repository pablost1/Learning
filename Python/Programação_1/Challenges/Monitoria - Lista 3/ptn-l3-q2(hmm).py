def em(oque,onde):
    tem = False
    for x in onde:
        if x==oque:
            tem = True
    return tem

def refer(oque,onde):
    index = 0
    for z in onde:
        if oque == z:
            break
        elif oque != z:
            index+=1
    return index

def divisores(numero):
    divisores = []
    for x in range(numero):
        if x > 0 and numero%x == 0:
            divisores.append(x)
    divisores.append(numero)
    return divisores

def primo(p):
    contador = 1
    primo = False
    i = 0
    if p>=-1 and p<=1:
        return False
    while contador <= p:
        if p%contador==0:
            i+=1
            if i>2:
                return primo
        contador+=1
    primo = True
    return primo

def nLucas(inicial,limite):
    if limite == 1:
        lucas =[inicial]
    elif limite == 2:
        lucas = [inicial,1]
    elif limite >= 3:
        lucas = [inicial,1]
        while limite > 0:
            lucas.append(lucas[-1]+lucas[-2])
            limite-=1
    return lucas

def nLucasSemPrimos(inicial,limite):
    lista = nLucas(inicial,limite)
    repete = len(lista)-1
    i = 0
    while i < repete:
        contador = 0
        for x in lista:
            if primo(x) or x == 1:
                lista.pop(contador)
            contador+=1
        i+=1
    return lista

def coprimos(n1,n2):
    n1Divisores = divisores(n1)
    n2Divisores = divisores(n2)
    coprimoss = True
    contador=0
    while contador < len(n2Divisores):
        for x in n1Divisores:
            if x>1 and x==n2Divisores[contador]:
                coprimoss = False
        contador+=1
            
    return coprimoss

def nLucasSemPrimosCoprimos(inicial,limite):
    nLucas = nLucasSemPrimos(inicial,limite)
    todosDivisores = []
    listaCoprimos = []
    for a in nLucas:
        todosDivisores.append(divisores(a))
    for x in todosDivisores:
        for xn in x:
            for y in todosDivisores:
                coprimos = True
                if y != x:
                    for yn in y:
                        if yn > 1 or xn > 1 and yn == xn:
                            coprimos = False
                if coprimos == True:
                    listaCoprimos.append([x[-1],y[-1]])
    return listaCoprimos
def comparaçaoLista(l1,l2):
    lista1 = l1
    lista2 = l2
    tem = False
    for x in lista1:
        if em(x,lista2):
            tem=True
'''

lista= [4,18,76,123]
for x in lista:
    divisores.append(divisores(x))
    
coprimos = True
contador=0
while contador < len(n2Divisores):
    for x in n1Divisores:
        if x>1 and x==n2Divisores[contador]:
            coprimos = False
    contador+=1
'''
''
nLucas = nLucasSemPrimos(2,10)
todosDivisores = []
listaCoprimos = []
c = 0
for x in nLucas:
    todosDivisores.append(divisores(x))
while c < len(todosDivisores):
    for x in todosDivisores:
        for y in todosDivisores:
            if y!=x:
                for xn in x:
                    if em(xn,y):
                        continue
                    if not em(xn,y) and not em([x[-1],y[-1]],listaCoprimos) and not em([y[-1],x[-1]],listaCoprimos) and xn>1 and comparaçaoLista(x,y) and not x[-1]%2+y[-1]%2==0:
                        listaCoprimos.append([x[-1],y[-1]])
    todosDivisores.pop(0)
    c+=1
    
listaCoprimos
''
'''
i = [5,7,8]
c = 0
while c < 3:
    for x in i:
        print(x)
    i.pop(0)
    c+=1
'''
