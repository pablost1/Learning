
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

    def adc_vertice(self, origem, destino, peso = None):
        if origem not in self.vertices_ordenados or destino not in self.vertices_ordenados:
            print("Erro: Um dos Vértices precisa existir no grafo!")
            return
        if origem in self.vertices_ordenados and destino in self.vertices_ordenados:
            print("Erro: Não há um vértice novo sendo inserido.")
    ### Ponderado ###
        if self.ponderado is True:
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
        if self.ponderado is True:
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
        else:
            lista_remocao = []
            for tripla in self.representacao:
                if vertice == tripla[0] or vertice == tripla[1]:
                    lista_remocao.append(tripla)
            for x in lista_remocao:
                self.representacao.remove(x)

    def ligados(self, vertice1, vertice2):
        check1  = False
        check2 = False
        ### Ponderado ###
        if self.ponderado is True:
            for tupla in self.dict_adj[vertice1]:
                if vertice2 == tupla[0]:
                    check1 = True
                    if self.orientado is False:
                        return True
            for tupla2 in self.dict_adj[vertice2]:
                if vertice1 == tupla2[0]:
                    check2 = True
        ### Não ponderado ###
        else:
            check1= vertice2 in self.dict_adj[vertice1]
            check2= vertice1 in self.dict_adj[vertice2]

        return check1 and check2

    def grau_entrada(self,vertice):
        g_entrada = 0
        ### Ponderado ###
        if self.ponderado is True:
            for v in self.dict_adj:
                for tupla in v:
                    if vertice == tupla[0]:
                        g_entrada+=1
        ### Não Ponderado ###
        else:
            for v in self.dict_adj:
                if vertice in v:
                    g_entrada+=1
        return g_entrada

    def grau_saida(self, vertice):
        g_saida = 0
        try:
            return len(self.dict_adj[vertice])
        except:
            raise ValueError("Vertice não existe na lista de adjacências.")

    def adjacente(self, vertice):
        try:
            return self.dict_adj[vertice]
        except:
            raise ValueError("Vértice não existe na lista de adjacências.")
    
    def menor_aresta(self): 
        ### Ponderado ###
        me_aresta = [(0,0,0)]
        if self.ponderado is True:
            for tripla in self.representacao:
                if tripla[2] < me_aresta[2]:
                    me_aresta = [tripla]
                elif tripla[2] == me_aresta[2]:
                    me_aresta.append(tripla)
        return me_aresta

    def maior_aresta(self): 
        ### Ponderado ###
        ma_aresta = [(0,0,0)]
        if self.ponderado is True:
            for tripla in self.representacao:
                if tripla[2] > me_aresta[2]:
                    me_aresta = [tripla]
                elif tripla[2] == me_aresta[2]:
                    me_aresta.append(tripla)
        return ma_aresta


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
    #print(a)
    print(a.representacao)
    a.remover_vertice(9)
    print(a.representacao)
    print(a)
    