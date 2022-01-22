def em(oque,onde):
    esta = False
    for z in onde:
        if z == oque:
            esta = True
            break
        else:
            esta = False
    return esta
def pular(linhas):
    while linhas > 0:
        print()
        linhas-=1
    return
def boneco(tentativas):
    cabeça = ['(*u*)','(*u*)','(*u*)','(*u*)','(*u*)','(*u*)','(*u*)',' ']
    corpo = ['l','l','l','l','l','l',' ',' ']
    braçoEs = ['/','/','/','/','/','',' ',' ']
    braçoDi = ['\\','\\','\\','\\','',' ',' ',' ']
    pernaEs = ['/','/','/','',' ',' ',' ',' ']
    pernaDi = ['\\','\\','',' ',' ',' ',' ',' ']
    print(cabeça[tentativas])
    print(braçoEs[tentativas],corpo[tentativas],braçoDi[tentativas])
    print(pernaEs[tentativas],' ',pernaDi[tentativas])
    return 
    
palavra = input('Digite uma palavra:')
tema = input('Diga o tema:')
while tema == 'coisa':
    tema = input('Nem ferrando, diga um tema válido:')
listaCompleta = []
listaVazia = []
letrasUsadas = []
for x in palavra:
    listaCompleta.append(x)
qtDeLetras = len(listaCompleta)
while qtDeLetras > 0:
    listaVazia.append('_')
    qtDeLetras-=1
    
pular(100)

tentativas = 7
terminou = False
while tentativas > 0 and not terminou:
    print('Tema:' ,tema)
    print(listaVazia)
    boneco(tentativas)
    print('letras usadas:' ,letrasUsadas)
    print()
    palpite=input('diga uma letra, ou a palavra(tentativa única):')
    contador = 0
    acertou = False
    letras = 0
    for y in palpite:
        letras+=1
    if letras > 1:
        if palpite == palavra:
            terminou = True
        else:
            tentativas = 0
    for z in listaCompleta:
        if palpite == z:
            listaVazia[contador] = z
            acertou = True
        contador+=1
    if not acertou and not em(palpite,letrasUsadas):
        tentativas -=1
    if listaCompleta == listaVazia:
        terminou = True
    if not em(palpite,letrasUsadas) and letras == 1: 
        letrasUsadas.append(palpite)
if terminou:
    pular(15)
    print('parabéns! você acertou! A palavra era:',palavra)
else:
    pular(15)
    print('Você não conseguiu acertar, a resposta era:',palavra)
    
