lista1 = [[15,48,37],
          [56,25,14],
          [11,68,29]]

lista2 = [[25,20,19],
          [26,22,33],
          [47,17,62]]
listaResultado = []
x=0
while x < len(lista1):
    listaResultado.append([])
    y = 0
    while y < len(lista1[0]):
        listaResultado[x].append(lista1[x][y]+lista2[x][y])
        y+=1
    x+=1
c=0
while c < len(listaResultado):
    print(listaResultado[c])
    c+=1

