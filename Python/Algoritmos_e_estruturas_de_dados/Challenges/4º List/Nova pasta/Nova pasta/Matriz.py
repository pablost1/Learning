from auxiliar import Aux
import numpy as np
from Lista import listaAdj

class MatrizAdj:
    def __init__(self, iteravel, **kwargs):
        self.orientado = kwargs.get('orientado', False)
        self.ponderado = kwargs.get('ponderado', False)
        self.representacao = iteravel
        self.dict_adj = {}
        self.vertices_ordenados = set([tupla[0] for tupla in self.representacao] + [tupla[1] for tupla in self.representacao])

    def __str__(self):
        self.fazer_matriz()
        aux = [str(x) for x in self.vertices_ordenados]
        ### Matriz de Adjacencia ###
        print('\t'+'\t'.join([str(x) for x in self.vertices_ordenados]))
        print('\t'+'\t'.join(['|' for x in self.vertices_ordenados]))
        i = 0
        while i < len(aux):
            texto = str(aux[i])
            print(texto+'    ──\t'+'\t'.join([str(x) for x in self.matriz_adj[i]])+'\n\n')
            i+=1
        return ''

    def __repr__(self):
        repr = ''
        ### ponderado ###
        if self.ponderado is True:
            for x in self.representacao:
                repr += f"({x[0]},{x[1]},{x[2]}),"
            repr = '['+repr[:len(repr)-1]+f'], ponderado={str(self.ponderado)}, orientado={str(self.orientado)}'
        ### Não ponderado ###
        else:
            for x in self.representacao:
                repr += f"({x[0]},{x[1]}),"
            repr = '['+repr[:len(repr)-1]+f'], ponderado={str(self.ponderado)}, orientado={str(self.orientado)}'
        return repr

    def fazer_matriz(self):
        self.matriz_adj = np.full((len(self.vertices_ordenados),len(self.vertices_ordenados)), 0)
        if type(self.representacao[0][0]) is type(''):
            self.vertices_ordenados = Aux.quick_sort(Aux(), self.vertices_ordenados)
        ### ponderado ###
        if self.ponderado is True:
            ### orientado ###
            if self.orientado is True:
                for x in self.representacao:
                    self.matriz_adj[Aux().ref(x[0],self.vertices_ordenados)][Aux().ref(x[1],self.vertices_ordenados)] = x[2]
            ### não orientado ###
            else:
                for x in self.representacao:
                    self.matriz_adj[Aux().ref(x[0],self.vertices_ordenados)][Aux().ref(x[1],self.vertices_ordenados)] = x[2]
                    self.matriz_adj[Aux().ref(x[1],self.vertices_ordenados)][Aux().ref(x[0],self.vertices_ordenados)] = x[2]
        ### Não ponderado###------------------------------------------------------------------
        else:
            ### orientado ###
            if self.orientado is True:
                for x in self.representacao:
                    self.matriz_adj[Aux().ref(x[0],self.vertices_ordenados)][Aux().ref(x[1],self.vertices_ordenados)] = 1
            ### não orientado ###
            else:
                for x in self.representacao:
                    self.matriz_adj[Aux().ref(x[0],self.vertices_ordenados)][Aux().ref(x[1],self.vertices_ordenados)] = 1
                    self.matriz_adj[Aux().ref(x[1],self.vertices_ordenados)][Aux().ref(x[0],self.vertices_ordenados)] = 1
        return       


if __name__ == '__main__':
    #a = MatrizAdj([(1,2),(3,4),(3,5),(4,2)])
    #a = MatrizAdj([('a','b'),('c','d'),('c','e'),('d','b')], orientado = True)
    #a = MatrizAdj([(0,1),(0,2),(0,3),(1,2),(2,3)])
    a = MatrizAdj([(9,9,69),(1,3,97),(1,4,86),(1,9,57),(2,4,51),(2,5,20),(2,7,77),(2,9,11),(4,9,44),(5,6,13),(6,7,88),(7,9,66)], ponderado = True)
    print(repr(a))
    b = MatrizAdj(repr(a))
    print(repr(b))