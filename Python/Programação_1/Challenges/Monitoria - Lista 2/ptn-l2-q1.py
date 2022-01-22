# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Universidade Federal de Pernambuco - UFPE
# Centro de Informática - CIn -  Sistemas de Informação 2019.1
# 
# Discente: Pablo Timoteo do Nascimento
# Login: ptn
# Email: ptn@cin.ufpe.br
# Questão: 1
# 
# Descrição do problema: Faça um programa que percorre uma lista e exiba na tela o valor mais próximo da
# média dos valores da lista.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

listaDeNumeros = []
listaDeNumeros.append(float(input('Digite um número: ')))
while listaDeNumeros[len(listaDeNumeros)-1] != 0:
    listaDeNumeros.append(float(input('Digite outro um número: ')))
listaDeNumeros.pop(len(listaDeNumeros)-1)
media = 0
for n in listaDeNumeros:
    media += n
media = (media/len(listaDeNumeros))
contador = 0
numeroAprox = 'x'
numeroAprox2 = 0
for m in listaDeNumeros:
    if numeroAprox == 'x':
        numeroAprox = m
    elif abs(m-media) < abs(numeroAprox-media):
        numeroAprox = m
    elif abs(numeroAprox-media) == abs(m-media):
        numeroAprox2 = m
print('Média',media)
if numeroAprox2 != 0:
    print('Numeros aproximados',numeroAprox, numeroAprox2)
else:
    print('Numero aproximado', numeroAprox)
    
