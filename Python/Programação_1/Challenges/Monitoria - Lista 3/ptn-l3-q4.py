

oitavas = [['Rússia','Alemanha'],['Brasil','Portugal'],['Argentina','Bélgica'],['Polônia','França'],['Espanha','Peru'],['Suíça','Inglaterra'],['Colômbia','México'],['Uruguai','Croácia']]
def torneio(jogos):
    c = 0
    i = 0
    novosJogos = []
    while c < int(len(jogos)//2):
        novosJogos.append([])
        c+=1
    for x in jogos:
        placar = input('Resultado do jogo:')
        if len(jogos)==1:
            if int(placar[0])>int(placar[2]):
                novosJogos = x[0]
            else:
                novosJogos = x[1]            
        elif int(placar[0])>int(placar[2]):
            novosJogos[int(i)].append(x[0])
        else:
            novosJogos[int(i)].append(x[1])
        i+=0.5
    return novosJogos

print(torneio(torneio(torneio(torneio(oitavas)))))
