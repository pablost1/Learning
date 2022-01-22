class Grafo:
    def __init__(self, iteravel, **kwargs):
        self.orientado = kwargs.get('orientado', False)
        self.ponderado = kwargs.get('ponderado', False)
        self.representacao = iteravel
        self.dict_adj = {}
        self.lista_de_adj(iteravel)
        self.lista = True
        self.vertices_ordenados = set([tupla[0] for tupla in self.representacao] + [tupla[1] for tupla in self.representacao])