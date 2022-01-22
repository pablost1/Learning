from auxiliar import Aux

import numpy as np
import time

class MatrizAdj:
    def __init__(self, iteravel, **kwargs):
        self.orientado = kwargs.get('orientado', False)
        self.ponderado = kwargs.get('ponderado', False)
        self.representacao = iteravel
        self.dict_adj = {}
        self.lista_de_adj(iteravel)
        self.lista = True
        self.vertices_ordenados = set([tupla[0] for tupla in self.representacao] + [tupla[1] for tupla in self.representacao])

class ListaAdj:
    pass

class Grafo:
    def __init__(self, iteravel, **kwargs):
        self.orientado = kwargs.get('orientado', False)
        self.ponderado = kwargs.get('ponderado', False)
        self.representacao = iteravel
        self.dict_adj = {}
        self.lista_de_adj(iteravel)
        self.lista = True
        self.vertices_ordenados = set([tupla[0] for tupla in self.representacao] + [tupla[1] for tupla in self.representacao])

    def adc_vertice(self, origem, destino, peso = None):
        if origem not in self.vertices_ordenados or destino not in self.vertices_ordenados:
            print("Erro: Um dos Vértices precisa existir no grafo!")
            return
    ### Ponderado ###
        if self.Ponderado is True:
            if peso:
                self.representacao.append((origem, destino, peso))
            else:
                print("Erro: insira o peso da Aresta entre os Vértices")
    ### Não Ponderado ###
        else:
            self.representacao.append(origem, destino)
        return

    def adc_aresta(self, origem, destino, peso = None):
        if origem not in self.vertices_ordenados and destino not in self.vertices_ordenados:
            print("Erro: Ambos os Vértices precisa existir no grafo!")
            return
    ### Ponderado ###
        if self.Ponderado is True:
            if peso:
                self.representacao.append((origem, destino, peso))
            else:
                print("Erro: insira o peso da Aresta entre os Vértices")
    ### Não Ponderado ###
        else:
            self.representacao.append(origem, destino)
        return
    
    def remover_vertice(self, vertice):
        if vertice not in self.vertices_ordenados:
            Print("Erro: Esse vertice não existe")
    
if __name__ == '__main__':
    inicio = time.time()
    #a = Grafo([(1,2),(3,4),(3,5),(4,2)])
    #a = Grafo([('a','b'),('c','d'),('c','e'),('d','b')], orientado = True)
    #a = Grafo([(0,1),(0,2),(0,3),(1,2),(2,3)])
    a = Grafo([(9,9,69),(1,3,97),(1,4,86),(1,9,57),(2,4,51),(2,5,20),(2,7,77),(2,9,11),(4,9,44),(5,6,13),(6,7,88),(7,9,66)], ponderado = True)
    print(a)
    a.switch()
    print(a)
    fim = time.time()
    
    print(fim-inicio)


