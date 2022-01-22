lista = [15,55,8,97,42,81,62,74,35,91,84,25]
i = 0

while i < len(lista)-1:
    c = 0
    while c < len(lista)-1:
        if lista[c] > lista[c+1]:
            temp = lista[c]
            lista[c] = lista[c+1]
            lista[c+1] = temp       
        c+=1
    i+=1
print(lista)
