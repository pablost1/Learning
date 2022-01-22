class Aluno:
    def __init__(self,nome,cpf):
        self.__cpf= int(cpf)
        self.__nome= str(nome)
        self.__notas = {}
    def inicializarNota(self,nota,numeroProva):
        if len(self.__notas) < 3:
            self.__notas[numeroProva] += nota
        else:
            print("Ocorreu um erro, este aluno tem mais de 3 notas")
        return
    
    def verificaSituacaoMedia():
        if len(self.__notas) == 3:
            return ((self.__notas[1]+self.__notas[2]+self.__notas[3])/3)>7
        else:
            print("Ocorreu um erro, este aluno não tem um número de notas adequado para efetuar esta operação")
            return False
            
    def imprimeInformacoes():
        if len(self.__notas) == 3:
            print(self.__nome,"\n",self.__cpf,"\n",self.__notas[1],"\n",self.__notas[2,],"\n",self.__notas[3])
        else:
            provasPossiveis = [1,2,3]
            notasNaoFornecidas = [x for x in provasPossiveis if x not in self.__notas]
            print("A nota",notasNaoFornecidas[0],"Não fornecida")
        return
