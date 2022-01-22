def pot(n,x):
    contador = 0
    resultado = 1
    while contador < x:
            resultado = resultado*n
            contador +=1
    return resultado
def raiz2(N):
    margem = 0.000000000001
    continuar = True
    r=1
    while continuar:
        r = (r + N/r)/2
        if ((r * r < N - margem)| (r * r > N + margem)):
            continuar = True
        else:
            continuar = False
    print (int(r))
