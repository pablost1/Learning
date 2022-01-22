biblioteca = []
def menu():
    c = 0
    while c < 1:
        print()
        açao = int(input('O que você deseja fazer?\n0 - Cadastrar um novo livro\n1 - Buscar um livro na biblioteca\n2 - Alterar alguma informação de um dos livros\n3 - remover uma quantidade de exemplares do estoque\nDigite o numero ação correspondente para efetua-la(Ex:0, para cadastrar):'))
        print()
        if açao > 4 or açao < 0:
            print('Ação inválida')
        elif açao == 0:
            cadastrar()
        elif açao == 1:
            buscar()
        elif açao == 2:
            alterar()
        elif açao == 3:
            remover()
    return
def cadastrar():
    livro = input('Digite o nome do livro:')
    autor = input('Digite o nome do autor:')
    codigo = input('Digite o codigo do livro:')
    lançamento = input('Digite o ano de lançamento do livro:')
    quantidade = input('Digite a quantidade de livros disponiveis:')
    confirmar = input('Deseja confirmar o cadastro?(s/n):')
    if confirmar.lower() == 's':
        biblioteca.append([livro,autor,codigo,lançamento,quantidade])
        print('Cadastro feito com sucesso!')
    return

def buscar():
    livro = input('Digite o nome do Livro o qual você deseja buscar:')
    c = 0
    while c < len(biblioteca):
        if livro.lower() ==biblioteca[c][0].lower():
            print(biblioteca[c])
            return   
        c+=1
    print('Esse livro não está cadastrado na biblioteca.')
    return 

def alterar():    
    livro = input('Digite o nome do Livro o qual você deseja alterar:')
    c = 0
    while c < len(biblioteca):
        if livro.lower() ==biblioteca[c][0].lower():
            alterar = (input('Nome do livro = 0\nNome do autor = 1\nCodigo do livro = 2\nAno de lançamento do livro = 3\nQuantidade = 4\nInsira o número correspondente da informação a qual você deseja mudar: \n'))
            if int(alterar) >= 0 and int(alterar) <= 5:
                biblioteca[c][int(alterar)] = input('Digite a nova informação:')
                print('Alteração feita com sucesso!')
            return   
        c+=1
    print('Esse livro não está cadastrado na biblioteca.')
    return

def remover():
    livro = input('Digite o nome do Livro o qual você deseja remover exemplares do estoque:')
    c = 0
    while c < len(biblioteca):
        if livro.lower() ==biblioteca[c][0].lower():
            print('Quantidade de exemplares disponível',biblioteca[c][4])
            remover = int(input('Insira a quantidade de exemplares a ser removida:'))
            if remover > int(biblioteca[c][4]) or remover < 0:
                return print('Erro! Número inválido para remoção!')
            else:
                biblioteca[c][4] = str(int(biblioteca[c][4])-remover)
                print('quantidade removida com sucesso!')
                return
        c+=1
    print('Esse livro não está cadastrado na biblioteca.')
    return

def em(oque,onde):
    tem = False
    for x in onde:
        if x == oque:
            tem = True
    return tem
menu()
