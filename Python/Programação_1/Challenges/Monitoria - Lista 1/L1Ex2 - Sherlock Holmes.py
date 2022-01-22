print('(Todas as respostas devem estar em letras minúsculas sem acentuações)')
nome = input('Qual é seu nome?:')
anos = int(input('Quantos anos você tem?:'))
print('Onde você se encontrava na hora do crime ',nome,'?')
print('1-Quarto;2-Sala;3-Banheiro;4-Cozinha')
local = int(input('Digite o numero do cômodo:'))
while local < 1 or local > 4:
    local = int(input('Numero do local inválido! Digite um válido:'))
gosto = int(input('Me diga, você gosta de arte? sim-1 ou não-2?:'))
while  gosto < 1 or gosto > 2:
    gosto = int(input('Resposta errada! apenas diga 1 para sim ou 2 para não!:'))
prosseguir = True
peso = 0
if anos < 10:
    print(nome+', Não és criminoso, pois tens menos de 10 anos!')
    prosseguir = False

if prosseguir  and local == 2:
    peso+=10
else:
    peso+=5
if gosto == 1 and prosseguir:
    peso+=8

if peso == 18 and prosseguir:
    print(nome+", Você é o criminoso! teje preso! ")
elif prosseguir:
    print(nome+', Você não é o criminoso! ainda bem!')

    
