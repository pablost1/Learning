def refer(oque,onde):
    index = 0
    for z in onde:
        if oque == z:
            break
        elif oque != z:
            index+=1
    return index

def maiorn(lista):
    maior = 0
    for x in lista:
        if x > maior:
            maior = x
    return maior

def maiorl(listaDeListas):
    maior = 0
    c = 0
    while c < len(m):
        for x in m[c]:
            if x > maior:
                maior = x
        c+=1
    return maior
'''
def delMaior(listaDeListas):
    maior = 0
    c = 0
    while c < len(listaDeListas):
        for x in listaDeListas[c]:
            if x > maior:
                maior = x
            listaDeListas.remove(maior)
        c+=1
    return listaDeListas
'''
listaDeListas = [[1,5,3],[9,7,5],[6,2,8]]
maior = 0
c = 0
while c < len(listaDeListas):
    for x in listaDeListas[c]:
        if x > maior:
            maior = x
    listaDeListas.pop(refer(maior,listaDeListas[c]))
    c+=1
