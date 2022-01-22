mensagem = input('digite uma mensagem:')
numero = 0
vogalMaiuscula = 0
vogalMinuscula = 0
consoanteMaiuscula = 0
consoanteMinuscula = 0
caracterEspecial = 0

for x in mensagem:
    if x == 'a' or x == 'o' or x == 'i' or x == 'e' or x == 'u':
        vogalMinuscula += 1
    elif x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U':
        vogalMaiuscula += 1
    elif x >= 'a' and x <= 'z' and x != 'a' and x != 'e' and x != 'i' and x != 'o' and x != 'u':
        consoanteMinuscula += 1
    elif x >= 'A' and x <= 'Z' and x != 'A' and x != 'E' and x != 'I' and x != 'O' and x != 'U':
        consoanteMaiuscula += 1
    elif x >= '1' and x <= '9':
        numero += 1
    else:
        caracterEspecial += 1
        
if vogalMaiuscula > 1:
    print('Vogais maiúsculas:',vogalMaiuscula)
else:    
    print('Vogal maiúscula:',vogalMaiuscula)
if vogalMinuscula > 1:
    print('Vogais minúsculas:',vogalMinuscula)
else:
    print('Vogal minúscula:',vogalMinuscula)
if consoanteMinuscula > 1:
    print('Consoantes minúsculas:',consoanteMinuscula)
else:
    print('Consoante minúscula:',consoanteMinuscula)
if consoanteMaiuscula > 1:
    print('Consoantes maiúsculas:',consoanteMinuscula)
else:
    print('Consoante maiúscula:',consoanteMaiuscula)
if numero > 1:
    print('numeros:',numero)
else:
    print('numero:',numero)
if caracterEspecial > 1:
    print('caracteres especiais:',caracterEspecial)
else:
    print('caractere especial:',caracterEspecial)
        
        
