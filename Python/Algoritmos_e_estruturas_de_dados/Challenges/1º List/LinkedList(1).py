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
    def setDado(self):
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
        #self.__ultimo = None
        self.__tamanho = 0
        self.__cabeca = None
        return
    def __repr__(self):
        if self.__cabeca is not None:
            ponteiro = self.__cabeca
            string = '['
            while ponteiro.getProximo() is not None:
                string += str(ponteiro.getDado)
                ponteiro = ponteiro.__proximo
            return string +']'
        else:
            return '[]'
        

    def __getitem__(self,index):
        return
    def __setitem__(self):
        return
    
    def anexar(self, elemento):
        if self.__cabeca == None:
            self.__cabeca = No(elemento)
            return 
        else:
            ponteiro = self.__cabeca
            while ponteiro.__proximo is not None:
                ponteiro = ponteiro.__proximo
            ponteiro.__proximo = No(elemento) 
            return
