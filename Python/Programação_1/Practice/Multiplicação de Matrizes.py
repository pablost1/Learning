def veritriz(matriz1,matriz2):
    valida1 = True
    valida2 = True
    for x in matriz1:
        if len(x) != len(matriz1[0]):
            valida1 = False
    if valida1 == False:
        return print('A primeira matriz não serve para multiplicar!')
    else:
        for x in matriz2:
            if len(x) != len(matriz2[0]):
                valida2 = False
        if valida2 == False:
            return print('A segunda matriz não serve para multiplicar!')
        else:
            if len(matriz1[0]) == len(matriz2):
                multiplicar = True
                return multiplicar
            else:
                multiplicar = False
                return multiplicar
'''
def multriz(matriz1,matriz2):
    if veritriz(matriz1,matriz2) == True:
        listaC = []
        linha = 0
        while linha < len(matriz1):
            listaC.append([])
            y = 0
            while y < len(matriz2[0]):
                x = 0
                temp = 0
                while x < len(matriz1[linha]):          
                    temp += (matriz1[linha][x]*matriz2[x][y])            
                    x+=1
                listaC[linha].append(temp)
                y += 1
            linha += 1

            return listaC
    else:
        print('Erro: matriz(es) invalida(s)')
'''
matriz1 = [[1,2,2,3,3,4,4,5,5,6,6],
          [1,2,2,3,3,4,4,5,5,6,6],
          [1,2,2,3,3,4,4,5,5,6,6]]

matriz2 = [[3,1,7],
          [2,4,8],
          [3,6,4],
          [2,4,8],
          [3,6,4],
          [2,4,8],
          [3,6,4],
          [2,4,8],
          [3,6,4],
          [2,4,8],
          [3,6,4]]

if veritriz(matriz1,matriz2) == True:
    listaC = []
    linha = 0
    while linha < len(matriz1):
        listaC.append([])
        y = 0
        while y < len(matriz2[0]):
            x = 0
            temp = 0
            while x < len(matriz1[linha]):          
                temp += (matriz1[linha][x]*matriz2[x][y])            
                x+=1
            listaC[linha].append(temp)
            y += 1
        linha += 1

organizar = 0
while organizar < len(listaC):
    print(listaC[organizar])
    organizar+=1
