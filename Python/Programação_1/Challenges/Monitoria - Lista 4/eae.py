def MaioresQueLimite(limite,lista):
    if len(lista) == 0:
        return []
    else:
        lissta = []
        if lista[0] > limite:
            lissta.append(lista.pop(0))
        elif lista[0] <= limite:
            lista.pop(0)
        return lissta + MaioresQueLimite(limite,lista)
        
def temRaizesInteiras(lista):
    if len(lista) == 0:
        return []
    else:
        lissta = []
        if str(lista[0]**0.5)[-1] == '0':
            lissta.append(int(lista.pop(0)))
        else:
            lista.pop(0)       
        return  lissta + temRaizesInteiras(lista)

pessoa1 = ('Roberto',1564789,'20001127')
pessoa2 = ('Pablo',1238654, '19782134')
def maioresDeIdade(lista):
    if len(lista):
        return []
    else:
        lissta = []
        if (20190522 - int(lista[0][-1]))<= 180000:
            lissta.append(lista[0][1])
            lista.pop(0)
        else:
            lista.pop(0)
    return lissta + maioresDeIdade(lista)


def dataatual():
    from datetime import date
    data_atual = date.today()
    str(data_atual).pop
    return
