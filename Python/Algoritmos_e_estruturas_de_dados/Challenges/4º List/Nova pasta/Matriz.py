from auxiliar import Aux
from Lista import listaAdj
import numpy as np
import time
class MatrizAdj:
    def __init__(self, iteravel, **kwargs):
        self.orientado = kwargs.get('orientado', False)
        self.ponderado = kwargs.get('ponderado', False)
        self.representacao = iteravel
        self.vertices_ordenados = set([tupla[0] for tupla in self.representacao] + [tupla[1] for tupla in self.representacao])

    def __str__(self):
        self.fazer_matriz()
        print('\t'+'\t'.join([str(x) for x in self.vertices_ordenados]))
        print('\t'+'\t'.join(['|' for x in self.vertices_ordenados]))
        i = 0
        for x in self.vertices_ordenados:
            texto = str(x)
            print(texto+'    ──\t'+'\t'.join([str(x) for x in self.matriz_adj[i]])+'\n\n')
            i+=1
        return ''
    def __repr__(self):
        pass

    def fazer_matriz(self):
        self.matriz_adj = np.full((len(self.vertices_ordenados),len(self.vertices_ordenados)), 0)
        if type(self.representacao[0][0]) is type(''):
            self.vertices_ordenados = Aux.quick_sort(Aux(), self.vertices_ordenados)
        ### ponderado ###
        if self.ponderado is True:
            ### orientado ###
            if self.orientado is True:
                for tripla in self.representacao:
                    self.matriz_adj[Aux.ref('',tripla[0],self.vertices_ordenados)][Aux.ref('',tripla[1],self.vertices_ordenados)] = tripla[2]
            ### não orientado ###
            else:
                for tripla in self.representacao:
                    self.matriz_adj[Aux.ref('',tripla[0],self.vertices_ordenados)][Aux.ref('',tripla[1],self.vertices_ordenados)] = tripla[2]
                    self.matriz_adj[Aux.ref('',tripla[1],self.vertices_ordenados)][Aux.ref('',tripla[0],self.vertices_ordenados)] = tripla[2]
        ### Não ponderado###------------------------------------------------------------------
        else:
            ### orientado ###
            if self.orientado is True:
                for tupla in self.representacao:
                    self.matriz_adj[Aux.ref('',tupla[0],self.vertices_ordenados)][Aux.ref('',tupla[1],self.vertices_ordenados)] = 1
            ### não orientado ###
            else:
                for tupla in self.representacao:
                    self.matriz_adj[Aux.ref('',tupla[0],self.vertices_ordenados)][Aux.ref('',tupla[1],self.vertices_ordenados)] = 1
                    self.matriz_adj[Aux.ref('',tupla[1],self.vertices_ordenados)][Aux.ref('',tupla[0],self.vertices_ordenados)] = 1
        return

if __name__ == '__main__':
    start = time.time()
    #a = MatrizAdj([(1,2),(3,4),(3,5),(4,2)])
    #a = MatrizAdj([('a','b'),('c','d'),('c','e'),('d','b')], orientado = True)
    a = MatrizAdj([(0,1),(0,2),(0,3),(1,2),(2,3)])
    
    #a = MatrizAdj([(9,9,69),(1,3,97),(1,4,86),(1,9,57),(2,4,51),(2,5,20),(2,7,77),(2,9,11),(4,9,44),(5,6,13),(6,7,88),(7,9,66)], ponderado = True)
    print(a)
    end = time.time()
    print(end-start)