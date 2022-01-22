# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Universidade Federal de Pernambuco - UFPE
# Centro de Informática - CIn -  Sistemas de Informação 2019.1
# 
# Discente: Pablo Timoteo do Nascimento
# Login: ptn
# Email: ptn@cin.ufpe.br
# Questão: 3
# 
# Descrição do problema: Tentando aprender como trabalhar com Listas em Python, Godofredo tenta
# aprender como fazer rotações de elementos contidos nessa Lista. Para isso precisa
# usar um sistema de shift (rotação à direita) de elementos. Ele pede a sua ajuda para
# criar esse sistema.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
lista = []
lista.append(int(input('Digite um número(diferente de 0): ')))
while lista[len(lista)-1] != 0:
    lista.append(int(input('Digite outro um número(para parar digite 0): ')))
lista.pop(len(lista)-1)
rotation = int(input('Numero de rotações:'))

while rotation > 0:
    contador = 0
    while contador < len(lista)-4:
        lista.insert(0,lista[len(lista)-1])
        lista.pop(len(lista)-1)
        contador+=1
    rotation-=1
    
print(lista)
        
