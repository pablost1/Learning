idade1 =  int(input('Digite uma idade:'))
idade2 =  int(input('Digite outra idade'))
idade3 =  int(input('Digite a última idade:'))
parOuImpar = 0
idadeMaior = 0
idadeMenor = 0

if idade1 > idade2:
    idadeMaior = idade1
    idadeMenor = idade2
    if idade3 > idade1:
        idadeMaior = idade3
    elif idade3 < idade2:
        idadeMenor = idade3
else:
    idadeMaior = idade2
    idadeMenor = idade1
    if idade3 > idade2:
        idadeMaior = idade3
    elif idade3 < idade1:
        idadeMenor = idade3
if (idadeMaior-idadeMenor)%2 == 0:
    parOuImpar = 'par'
else:
    parOuImpar = 'Ímpar'

print('Mais velho:',idadeMaior)
print('Mais novo:',idadeMenor)
print('Diferença:',(idadeMaior-idadeMenor),' anos - ',parOuImpar)


