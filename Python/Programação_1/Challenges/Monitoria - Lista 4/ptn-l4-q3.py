# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Universidade Federal de Pernambuco - UFPE
# Centro de Informática - CIn -  Sistemas de Informação 2019.1
# 
# Discente: Pablo Timoteo do Nascimento
# Login: ptn
# Email: ptn@cin.ufpe.br
# Questão: 3
# 
# Descrição do problema: Na questão a seguir, você deve ler 3 tuplas de dados contendo as coordenadas de 3
# pontos num plano cartesiano e seu programa deve ser capaz de retornar o tamanho das
# arestas ligando esses pontos (também numa tupla) e indicar qual tipo de triângulo ele é.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def veriangulo():
    rep = 3
    triangulo = ()
    ponto = ()
    arestas = ()
    while rep > 0:
        ponto = input('Insira o ponto no modelo "x y":')
        triangulo += (splitz(ponto),)
        rep-=1
    arestas = ( (rounds((((int(triangulo[0][0])-int(triangulo[1][0]))**2)+((int(triangulo[0][1])-int(triangulo[1][1]))**2))**(1/2),2)),(rounds((((int(triangulo[0][0])-int(triangulo[2][0]))**2)+((int(triangulo[0][1])-int(triangulo[2][1]))**2))**(1/2),2)),(rounds((((int(triangulo[2][0])-int(triangulo[1][0]))**2)+((int(triangulo[2][1])-int(triangulo[1][1]))**2))**(1/2),2)) )
    print(arestas)
    if arestas[0] == arestas[1] or arestas[2] == arestas[1] or arestas[2] == arestas[0]:
        print('tipo: Isóceles')
    elif arestas[0] == arestas[1] and arestas[2] == arestas[1]:
        print('tipo: Equilátero')
    else:
        print('tipo: Escaleno')
    return 

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


def rounds(nfloat,limite):
    c = 0
    for x in str(nfloat):
        if x =='.':
            return str(nfloat)[0:c+1+limite]
        c+=1
    return
