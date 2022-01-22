# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Universidade Federal de Pernambuco - UFPE
# Centro de Informática - CIn -  Sistemas de Informação 2019.1
# 
# Discente: Pablo Timoteo do Nascimento
# Login: ptn
# Email: ptn@cin.ufpe.br
# Questão: 1
# 
# Descrição do problema: Se pelo menos um dos segmentos (x, y ou z) for constante em todas as
# geolocalizações fornecidas os dados dessa amostra configuram uma terra plana.
# Nos outros casos imprima que a terra não é plana
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def veriterra():
    c = 0
    xt = ()
    yt = ()
    zt = ()
    tupla = ()
    contador = int(input('Quantas coordenadas você gostaria de inserir?:'))
    while c < contador:
        i=0
        coord = input('Digite as coordenadas no modelo "X,Y,Z", separados por espaço:')
        for x in splitz(coord):
            if i == 0:
                xt += (x,)
            elif i == 1:
                yt += (x,)
            elif i == 2:
                zt += (x,)
            i+=1   
        c+=1
    tupla = (xt,yt,zt)
    for y in tupla:
        igual = True
        for z in y:
            if z != y[0]:
                igual = False
        if igual:
            return print('Terra plana')        
    return print('Terra não plana')

def splitz(texto):
    elementos = ()
    palavra = ''
    for x in texto:
        if x != ' ':
            palavra += x
        else:
            elementos += (palavra,)
            palavra = ''
    elementos += (palavra,)
    return elementos

