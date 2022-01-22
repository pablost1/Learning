print('Insira as respostas sem letras maiúsculas ou acentuações')
pontuaçao=0
pergunta = ['Qual é o protagonista da saga de jogos: The legend of Zelda?:','Qual foi o primeiro nome do Mário?','Qual é o nome do criador da saga "Metal Gear?"','Qual é o nome do pokemon criador?','O que significa o nome do professor "Yana" na quarta temporada da nova série de Doctor Who?','Nome da mãe de Dante da série de jogos "Devil May Cry']
resposta = ['link','jumpman','hideo kojima','arceus','you are not alone','eva']
contador=0
while contador<len(pergunta)-1:
    print(pergunta[contador])
    if resposta[contador]==input('Resposta:'):
        print('Você acertou! agora para a próxima.')
        pontuaçao=pontuaçao+1
    else:
        print('Você errou, porque és burro')
    contador+=1
    
if pontuaçao==6:
    print('parabéns!! você não errou uma questão')
else:
    print('Cara... você é muito ruim, sua pontuação foi de',pontuaçao,'de '+ str(len(pergunta)))

        
