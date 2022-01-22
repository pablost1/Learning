#from Matriz import MatrizAdj

class listaAdj:
    def __init__(self, iteravel, **kwargs):
        self.orientado = kwargs.get('orientado', False)
        self.ponderado = kwargs.get('ponderado', False)
        self.representacao = iteravel
        self.dict_adj = {}
        self.vertices_ordenados = set([tupla[0] for tupla in self.representacao] + [tupla[1] for tupla in self.representacao])

    def lista_de_adj(self, iteravel):
        ### listaAdjs ponderados ###
        if self.ponderado is True:
            for tripla in iteravel:
                origem, destino, peso = tripla
                ### listaAdj orientado ###
                if self.orientado is True:
                    if origem in self.dict_adj:
                        self.dict_adj[origem].append((destino,peso))
                    else:
                        self.dict_adj[origem] = [(destino, peso)]
                
                ### listaAdj Não orientado ###
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
 
        ### listaAdjs Não ponderados ###            
        else:
            for tupla in iteravel:
                origem, destino = tupla
            ### listaAdj orientado ###
                if self.orientado == True:
                    if origem in self.dict_adj and destino not in self.dict_adj[origem]:
                        self.dict_adj[origem].append(destino)
                    else:
                        self.dict_adj[origem] = [destino]
                
            ### listaAdj não orientado ###
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
    def __str__(self):
        self.lista_de_adj(self.representacao)
        ### Lista Adjacencia ###
        texto = ''
        print("lista de Adjacencia"+'\n')
        for x in self.dict_adj:
                print(x,':',self.dict_adj[x])
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

    def adc_vertice(self, origem, destino, ponderado = 0):
        ### Ponderado ###
        if self.ponderado is True:
            pass
        ### Não Ponderado ###
        else:
            pass
    def adc_aresta(self):
        pass
    def remover_vertice(self):
        pass
    def remover_aresta(self):
        pass
    def grau_entrada(self):
        pass
    def grau_saida(self):
        pass
    def adjacente(self):
        pass
    def menor_aresta(self):
        pass
    def maior_aresta(self):
        pass

if __name__ == '__main__':
    '''
    a = listaAdj([(1,2),(3,4),(3,5),(4,2)])
    print(a)
    a = listaAdj([('a','b'),('c','d'),('c','e'),('d','b')], orientado = True)
    print(a)
    a = listaAdj([(0,1),(0,2),(0,3),(1,2),(2,3)])
    print(a)
'''
    a = listaAdj([(9,9,69),(1,3,97),(1,4,86),(1,9,57),(2,4,51),(2,5,20),(2,7,77),(2,9,11),(4,9,44),(5,6,13),(6,7,88),(7,9,66)], ponderado = True)
    print(a)

    