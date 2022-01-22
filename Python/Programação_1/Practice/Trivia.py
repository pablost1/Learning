print('Insira as respostas sem letras maiúsculas ou acentuações')
contador=0
pontuaçao=0
while contador<3:
    if contador == 0:
        pergunta1=input('Qual é o protagonista da saga de jogos: The legend of Zelda?:')
        if pergunta1==('link'):
            print('Você acertou! agora para a próxima.')
            contador=contador+1
            pontuaçao=pontuaçao+1
            print()
        elif pergunta1==('zelda'):
            print('Essa é a princesa, seu burro.')
            contador=contador+1
            print()
        else:
            print('Está errado')
            contador=contador+1
            print()
            
    elif contador == 1:
        pergunta2=input('Qual foi o primeiro nome do Mário?')
        if pergunta2==('jumpman'):
            print('Parabéns! esta correto!')
            contador=contador+1
            print()
            pontuaçao=pontuaçao+1
        elif pergunta2==('que mario?') or ('qual mario?'):
            print('hehe, você que deveria saber...')
            contador=contador+1
            print()
        else:
            print('está errado')
            contador=contador+1
            
            print()
    elif contador==2:
        pergunta3=input('Qual é o nome do criador de Metal Gear?')
        if pergunta3==('hideo kojima'):
            print('Perfeito! você acertou!')
            print()
            contador=contador+1
            pontuaçao=pontuaçao+1
        else:
            print('está errado!')
            contador=contador+1
            print()
if pontuaçao==3:
    print('parabéns!! você não errou uma questão')
else:
    print('Cara... você é muito ruim, sua pontuação foi de',pontuaçao,)

        
