import time

from lista import No
from lista import ListaEncadeada
from bem import Bem
from candidato import Candidato

class Controle:

    def __init__(self):
        self.__listaCandidatos = ListaEncadeada()
        self.__listaBens = ListaEncadeada()
        return

    def carregarBens(self, caminho = "bem_candidato_2014_BRASIL.csv"):

        dicionario = {}
        bens = open(caminho, "r", encoding = "latin-1")
        linhas = bens.readlines()
        tamanhoTotal = len(linhas)
        linhaAtual = 0
        listaBens = ListaEncadeada()
        for bem in linhas:
            informacoes = bem.split(";")
            if informacoes[0] == '"DT_GERACAO"':
                linhaAtual+=1
            else:
                novoBem = Bem(
                    bem_codigo = informacoes[13][1:-1],
                    bem_descricao = informacoes[14][1:-1],
                    bem_descricao_detailed = informacoes[15][1:-1],
                    bem_valor = informacoes[16][1:-1]
                    )         
                if int(informacoes[11][1:-1]) not in dicionario:
                    dicionario[11][1:-1] = ListaEncadeada([novoBem])
                else:
                    dicionario[11][1:-1].anexar(novoBem)

        return dicionario
    
    def carregarCandidatos(self, caminho = "consulta_cand_2014_BRASIL.csv"):
        dicionario_bens = self.carregarBens()
        print(dicionario_bens)
        return
        candidatos = open(caminho, "r", encoding = "latin-1")
        linhas = candidatos.readlines()
        tamanhoTotal = len(linhas)
        linhaAtual = 0
        for cand in linhas:
            informacoes = cand.split(";")
            if informacoes[0] == '"DT_GERACAO"':
                linhaAtual +=1
            else:
                print(informacoes[17])
                novoCand = Candidato(
                anoEleicao = informacoes[2][1:-1],
                siglaUF = informacoes[10][1:-1],
                codigoCargo = informacoes[13][1:-1],
                descricaoCargo = informacoes[14][1:-1],
                nomeCandidato = informacoes[17][1:-1],
                IDCandidato = informacoes[15][1:-1],
                numeroUrna = informacoes[16][1:-1],
                CPF = informacoes[20][1:-1],
                nomeUrna = informacoes[18][1:-1],
                numeroPartido =informacoes[27][1:-1],
                siglaPartido =informacoes[29][1:-1],
                codigoOcupacaoCandidato = informacoes[28][1:-1],
                descricaoOcupacao =informacoes[50][1:-1],
                dataNascimento = informacoes[38][1:-1],
                sexo = informacoes[42][1:-1],
                estadoCivil = informacoes[46][1:-1],
                UFnascimento = informacoes[35][1:-1],
                nomeMunicipioNascimento = informacoes[37][1:-1],
                sitCandidatoPosPleito = informacoes[-5][1:-1],
                situacaoCandidatura = informacoes[25][1:-1],
                listaBens = self.carregarBens(caminho = "bem_candidato_2014_BRASIL.csv", IDCandidato = informacoes[15][1:-1])
            )
                self.__listaCandidatos.anexar(novoCand)
        return
    def getListaCandidatos(self):
        return self.__listaCandidatos
if __name__ == "__main__":
    controle = Controle()
    controle.carregarCandidatos("./candidatos/consulta_cand_2014_BRASIL.csv")
    print([x for x in controle.getListaCandidatos()][:50])
    '''
    lista = ListaEncadeada([5,5,2,4,7,98,1,2,3,5,0,55,1,23,564,6773,21,53,11,2])
    lista2 = ListaEncadeada([5,5,2,4,7,98,1,2,3,5,0,55,1,23,564,6773,21,53,11,2])

    lista.anexar(7)
    lista.anexar(3)

    lista.anexar(4)

    lista.anexar(5)

    lista.anexar(7)
   
    print("- - - - - -")
    print(lista.getCabeca())
    print(lista.getCabeca().getProximo())
    print(lista.getCabeca().getProximo().getProximo())
    print(lista.getCabeca().getProximo().getProximo().getProximo())
    
    lista.concatenar(lista2)
    print(qs(lista))'''
    