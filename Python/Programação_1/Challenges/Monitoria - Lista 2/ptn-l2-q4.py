# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Universidade Federal de Pernambuco - UFPE
# Centro de Informática - CIn -  Sistemas de Informação 2019.1
# 
# Discente: Pablo Timoteo do Nascimento
# Login: ptn
# Email: ptn@cin.ufpe.br
# Questão: 4
# 
# Descrição do problema: Duas amigas estabeleceram o código abaixo para que suas mensagens não fossem
# lidas pelas demais pessoas.

# Formato de Entrada:
# Devem ser adicionados números em uma lista até que o usuário aperte enter e não
# tenha valor algum digitado.
# Formato de Saída:
# O programa deve pegar os valores desta lista e devolver uma string traduzida.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
listaCodigo = []
listaLetras = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
listaCodigo.append(input('digite o numero da letra'))
while listaCodigo[-1] != '':
    listaCodigo.append(input('digite o numero da letra(aperte enter sem um valor digitado para encerrar):'))
                       
listaCodigo.pop(-1)
palavra = ''
for x in listaCodigo:
    if int(x) <= 26 and int(x) >=0:
        palavra+=listaLetras[int(x)]
    
print(palavra)
