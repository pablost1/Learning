# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Universidade Federal de Pernambuco - UFPE
# Centro de Informática - CIn -  Sistemas de Informação 2019.1
# 
# Discente: Pablo Timoteo do Nascimento
# Login: ptn
# Email: ptn@cin.ufpe.br
# Questão: 2
# 
# Descrição do problema: Faça um programa que percorre uma lista com o seguinte formato:
# [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]. Essa
# lista indica o número de faltas que cada time fez em cada jogo. Na lista acima, no
# jogo entre Brasil e Itália, o Brasil fez 10 faltas e a Itália fez 9.
#
# O programa deve imprimir na tela:
# a) o total de faltas do campeonato
# b) o time que fez mais faltas
# c) o time que fez menos faltas
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#----------funções auxiliares------------
def em(oque,em):
    esta = False
    for z in em:
        if z == oque:
            esta = True
            break
        else:
            esta = False
    return esta

def refer(oque,onde):
    index = 0
    for z in onde:
        if oque == z:
            break
        elif oque != z:
            index+=1
    return index

maisFaltas = 0
menosFaltas = 0
#----------montando a lista dos paises e a soma de suas faltas----------
listaCopa =[['Brasil', 'Alemanha', [1, 3]], ['Brasil', 'Argentina', [1, 7]],['Argentina', 'Alemanha', [1,4]]]
paisesPontos = [[],[]]
c = len(listaCopa)
while c > 0:
    ref = 0
    while ref != 2:
        if em(listaCopa[c-1][ref],paisesPontos[0]) == False:
            paisesPontos[0].append(listaCopa[c-1][ref])
            paisesPontos[1].append(listaCopa[c-1][2][ref])
        elif em(listaCopa[c-1][ref],paisesPontos[0]) == True:
            paisesPontos[1][refer(listaCopa[c-1][ref],paisesPontos[0])] += listaCopa[c-1][2][ref]
        
        ref+=1
    c-=1
#----------soma de todas as faltas e distinção entre o país com mais faltas e o pais com menos faltas ----------
soma = 0
maisFaltas = paisesPontos[1][0]
menosFaltas = paisesPontos[1][0]
for x in paisesPontos[1]:
    if x > maisFaltas:
        maisFaltas = x
    if x < menosFaltas:
        menosFaltas = x
    soma+=x
#----------Saída----------    
print('total de faltas', soma)
print('País com mais faltas', paisesPontos[0][refer(maisFaltas,paisesPontos[1])],'- faltas:',maisFaltas)
print('País com menos faltas', paisesPontos[0][refer(menosFaltas,paisesPontos[1])],'- faltas:',menosFaltas)

