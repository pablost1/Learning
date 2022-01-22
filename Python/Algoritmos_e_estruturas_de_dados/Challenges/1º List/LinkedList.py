class No:
    def __init__(self,dado,anterior = None,proximo= None):
        self.__dado = dado
        self.__anterior = anterior
        self.__proximo = proximo
        return
    def __repr__(self):
        return str(self.__dado)
    
    def __str__(self):
        return str(self.__dado)

    def getDado(self):
        return self.__dado
    def setDado(self, novoDado):
        self.__dado = novoDado
        return
    def getAnterior(self):
        return self.__anterior
    def setAnterior(self,novoAnterior):
        self.__anterior = novoAnterior
        return
    def getProximo(self):
        return self.__proximo
    def setProximo(self,novoProximo):
        self.__proximo = novoProximo
        return
    






    
class ListaEncadeada:
    
    def __init__(self):
        self.__cabeca = None
        self.__calda = None
        self.__tamanho = 0
        return
    def __len__(self):
        return self.__tamanho

    def __getitem__(self,indice):
        if indice > (self.getTamanho()-1) or indice < 0:
            raise IndexError("Índice não consta na lista")
        else:
            ponteiro = self.getCabeca()
            for x in range(indice):
                ponteiro = ponteiro.getProximo()
            return ponteiro.getDado()

    def __setitem__(self, indice, novoDado):
        if indice > (self.getTamanho()-1) or indice < 0:
            raise IndexError("Índice não consta na lista")
        else:
            if indice == self.getTamanho()-1:
                self.getCalda().setDado(novoDado)
            ponteiro = self.getCabeca()
            for x in range(indice):
                ponteiro = ponteiro.getProximo()
            ponteiro.setDado(novoDado)
             

    def __repr__(self):
        if self.getCabeca() == None:
            return '[]'
        string = str(self.getCabeca())
        
        if self.getCabeca() and self.getCabeca().getProximo():
            ponteiro = self.getCabeca().getProximo()
            while ponteiro.getProximo():
                string = string + ',' +  str(ponteiro.getDado())
                ponteiro = ponteiro.getProximo()
            string = string + ',' +  str(ponteiro.getDado())
            return '['+string+']'
        else:
            return '['+string+']'

    def anexar(self, elemento):

        if self.__cabeca:
            ponteiro = self.getCabeca()
            while ponteiro.getProximo():
                ponteiro = ponteiro.getProximo()
            ponteiro.setProximo(No(elemento,ponteiro))
            self.setCalda(ponteiro.getProximo())
            self.setTamanho(self.getTamanho() +1 )

            return
        else:
            self.setCabeca(No(elemento))
            self.setCalda(No(elemento))
            self.setTamanho(self.getTamanho() +1 )
        return

    def indice(self, elemento):
        if self.getTamanho() == 0:
            raise ValueError("O elemento não consta na lista.")
        else:
            indice = 0
            ponteiro = self.getCabeca()
            while ponteiro:
                if ponteiro.getDado() == elemento:
                     return indice
                else:
                    ponteiro = ponteiro.getProximo()
                    indice+=1
            ValueError("O elemento não consta na lista.")
    def remover(self, elemento):
        try:
            ponteiro.getCabeca()
            while ponteiro.getProximo().getDado() != elemento:
                ponteiro = ponteiro.getProximo()
            ponteiro.setProximo(ponteiro.getProximo().getProximo())
            ponteiro.getProximo().setAnterior(ponteiro)
            return
        except:

            if self.getCabeca().getDado() == elemento:
                ponteiro = self.getCabeca()
                ponteiro.getProximo().setAnterior(None)
                self.setCabeca(ponteiro.getProximo())
                ponteiro.setProximo(None)
                return
            elif self.getCalda().getDado() == elemento:
                ponteiro = self.getCalda()
                self.setCalda(ponteiro.getAnterior())
                ponteiro.setAnterior(None)
                self.getCalda().setProximo(None)
                return
            ValueError("list.remover(x): x Não está na lista")
# Gets n' Sets
    def setCabeca(self, elemento):
        self.__cabeca = elemento
        return
    def getCabeca(self):
        return self.__cabeca
    def setCalda(self, elemento):
        self.__calda = elemento
        return
    def getCalda(self):
        return self.__calda

    def setTamanho(self, novoTamanho):
        self.__tamanho = novoTamanho
        return
    def getTamanho(self):
        return self.__tamanho



