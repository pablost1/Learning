import numpy as np
from auxiliar import Aux 
class Grafo:
    def __init__(self, iteravel, **kwargs):
        self.orientado = kwargs.get('orientado', False)
        self.ponderado = kwargs.get('ponderado', False)
        self.dict_adj = {}
        self.lista_de_adj(iteravel)
        self.lista = True

    def __str__(self):
        ### Lista Adjacencia ###
        if self.lista is True:
            texto = ''
            print("lista de Adjacencia"+'\n')
            for x in self.dict_adj:
                print(x,':',self.dict_adj[x])
        ### Matriz Adjacencia ###
        else:
            self.fazer_matriz()
            print('\t'+'\t'.join([str(x) for x in self.grafos_ord]))
            print('\t'+'\t'.join(['|' for x in self.grafos_ord]))
            i = 0
            while i < len(self.grafos_ord):
                texto = str(self.grafos_ord[i])
                print(texto+'    ──\t'+'\t'.join([str(x) for x in self.matriz_adj[i]])+'\n\n')
                i+=1
        return ''

    def switch(self):
        if self.lista is True:
            self.lista = False
        else:
            self.lista = True

    def lista_de_adj(self, iteravel):
        ### Grafos ponderados ###
        if self.ponderado is True:
            for tripla in iteravel:
                origem, destino, peso = tripla
                ### Grafo orientado ###
                if self.orientado is True:
                    if origem in self.dict_adj:
                        self.dict_adj[origem].append((destino,peso))
                    else:
                        self.dict_adj[origem] = [(destino, peso)]
                
                ### Grafo Não orientado ###
                else:
                    if origem in self.dict_adj:
                        if (destino, peso) not in self.dict_adj[origem]:
                            self.dict_adj[origem].append((destino, peso))
                            if destino in self.dict_adj:
                                if (origem, peso) not in self.dict_adj[destino]:
                                    self.dict_adj[destino].append((origem, peso))
                            else:
                                self.dict_adj[destino] =[(origem, peso)]
                                
                    else:
                        self.dict_adj[origem] = [(destino, peso)]
                        
                        if destino in self.dict_adj:
                            if (origem, peso) not in self.dict_adj[destino]:
                                self.dict_adj[destino].append((origem, peso))
                        else:
                            self.dict_adj[destino] =[(origem, peso)]
 
        ### Grafos Não ponderados ###            
        else:
            for tupla in iteravel:
                origem, destino = tupla
            ### Grafo orientado ###
                if self.orientado == True:
                    if origem in self.dict_adj and destino not in self.dict_adj[origem]:
                        self.dict_adj[origem].append(destino)
                    else:
                        self.dict_adj[origem] = [destino]
                
            ### Grafo não orientado ###
                else:
                    if origem in self.dict_adj and destino not in self.dict_adj[origem]:
                        self.dict_adj[origem].append(destino)
                        if destino in self.dict_adj and origem not in self.dict_adj[destino]:
                            self.dict_adj[destino].append(origem)
                        else:
                            self.dict_adj[destino] = [origem]
                    else:
                        self.dict_adj[origem] = [destino]
                        if destino in self.dict_adj and origem not in self.dict_adj[destino]:
                            self.dict_adj[destino].append(origem)
                        else:
                            self.dict_adj[destino] = [origem]
            return

    def fazer_matriz(self):
        self.grafos_ord = Aux().quick_sort([x for x in self.dict_adj])
        self.matriz_adj = np.full((len(self.dict_adj),len(self.dict_adj)),0)

        ### Ponderado ###        
        if self.ponderado is True:
            i=0
            for x in self.grafos_ord:
                for y in self.dict_adj[x]:
                    self.matriz_adj[i][Aux.ref(self, y[0], self.grafos_ord)] = y[1]
                i+=1
        ### Não ponderado ###
        else:
            i = 0
            for x in self.grafos_ord:
                for y in self.dict_adj[x]:
                    self.matriz_adj[i][Aux.ref(self, y, self.grafos_ord)] = 1
                i += 1

        return        

    def adc_vertice(self,novo, vertice, peso = 0):
        ### ponderado ###
        if self.ponderado is True:
            a = 1
        ### não ponderado ###
        else:
            a =1
        return
if __name__ == '__main__':
    #a = Grafo([(1,2),(3,4),(3,5),(4,2)])
    #a = Grafo([('a','b'),('c','d'),('c','e'),('d','b')])
    #a = Grafo([(0,1),(0,2),(0,3),(1,2),(2,3)])
    a = Grafo([(9,9,69),(1,3,97),(1,4,86),(1,9,57),(2,4,51),(2,5,20),(2,7,77),(2,9,11),(4,9,44),(5,6,13),(6,7,88),(7,9,66)], ponderado = True)
    print(a)
    a.switch()
    print(a)

