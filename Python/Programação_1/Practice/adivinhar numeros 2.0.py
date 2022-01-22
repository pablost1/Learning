numeroMaior=0
numeroMenor=0
linhasEmBranco=0
contador=0
numero3=6516849681513516587421654689151587456565156184898121321564564897894213216546546554654


numero1=int(input('Me diga um número: '))
numero2=int(input('Me diga outro número: '))
if numero1>numero2:
    numeroMaior=numero1
    numeroMenor=numero2
else:
    numeroMaior=numero2
    numeroMenor=numero1
while linhasEmBranco<60:
    print()
    linhasEmBranco=linhasEmBranco+1
#\/número a ser adivinhado\/
while contador < 10:
    numero3=int(input('Digite o número palpite: '))
    if numero3 == numero1:
        print("Parabéns, você acertou um! agora falta outro!")
        numeroMaior=numero2
        numeroMenor=numero2
        while contador < 10:
            numero3=int(input('Digite outro número palpite: '))
            if numero3 == numero1:
                print('Ei! você já deu esse palpite antes!')
                contador+=1
            elif numero3 < numeroMenor:
                print('Esse número é menor que o número atual')
                contador=contador+1
            elif numero3 > numeroMaior:
                print('Esse número é maior que o número atual')
                contador=contador+1
            else:
                print('Parabéns! você acertou ambos os números!')
                contador=10

    elif numero3 == numero2:
        print("Parabéns, você acertou um! agora falta outro!")
        numeroMaior=numero1
        numeroMenor=numero1
        while contador < 10:
            numero3=int(input('Digite outro número palpite: '))
            if numero3 == numero2:
                print('Ei! você já deu esse palpite antes!')
                contador+=1
            elif numero3 < numeroMenor:
                print('Esse número é menor que o número atual')
                contador=contador+1
            elif numero3 > numeroMaior:
                print('Esse número é maior que o número atual')
                contador=contador+1
            else:
                print('Parabéns! você acertou ambos os números!')
                contador=10
                
    elif numero3 < numeroMenor:
        print('Esse número é menor que ambos os números')
        contador=contador+1
    elif numero3 > numeroMaior:
        print('Esse número é maior que ambos os números')
        contador=contador+1
    else:
        print('Esse número esta entre os dois números')
        contador=contador+1
if numero3!=numero1 and numero3!=numero2:
    print('Infelizmente você errou, os números eram: ',numero1,' e ',numero2,)
else:
    print()
