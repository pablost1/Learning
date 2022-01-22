numero = int(input('Digite um número:'))
acabar = False
numeroVerificador = 1
while not acabar:
    if (numeroVerificador * numeroVerificador * numeroVerificador) == numero:
        print('A raiz cúbica de',numero,' é:',numeroVerificador,)
        acabar=True
    elif (numeroVerificador*numeroVerificador*numeroVerificador) > numero:
        print('Não existe raiz.')
        acabar=True
    else:
        numeroVerificador+=1
        
