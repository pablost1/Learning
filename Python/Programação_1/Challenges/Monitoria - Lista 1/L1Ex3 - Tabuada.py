numero1 = int(input('Diga um numero a ser multiplicado:'))
numero2 = int(input('Agora diga até quanto você quer que vá a tabuada do numero anterior:'))
contador = 0
resultado = 0
while contador <= numero2:
    resultado = numero1*contador
    print(numero1,'x',contador,'=',resultado)
    contador+=1
