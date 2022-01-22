palavra = input('Digite uma palavra ou frase:')
palavra1 = []
palavraInv = []

for x in palavra.lower():
    if x >= 'a' and x <= 'z':
        palavra1.append(x)

contador = len(palavra1)
while contador > 0:
    palavraInv.append(palavra1[contador-1])
    contador-=1

print(palavra1==palavraInv)

