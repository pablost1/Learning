palavra = input('Digite uma palavra:')
palavraNova = ''
for x in palavra:
    if x >='a' and x <='z' or x>='A' and x <= 'Z' or x >= '0' and x <= '9':
        palavraNova+=x
print(palavraNova)
