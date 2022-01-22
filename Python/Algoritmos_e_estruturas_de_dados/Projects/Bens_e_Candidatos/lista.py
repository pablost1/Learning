import time

def qs(lista):
    if len(lista) == 0:
        return []
    else:
        pivot = lista.pop(0)
        menores = [x for x in lista if x < pivot]
        maiores = [x for x in lista if x >= pivot]
        return qs(menores)+[pivot]+qs(maiores) 
    
class No:
    def __init__(self, dado, anterior = None, proximo = None):
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
    
    def __init__(self, iteravel = None):
        
        self.__cabeca = None
        self.__calda = None
        self.__tamanho = 0
        
        if iteravel:
            for elemento in iteravel:
                self.anexar(elemento)
        return
    
    def anexar(self, elemento):
        if self.__tamanho > 1:
            aux = No(elemento, self.__calda)
            self.__calda.setProximo(aux)
            self.setCalda(aux)
            self.setTamanho(self.getTamanho() +1)
            return
        elif self.__tamanho == 1:
            aux = No(elemento, self.__cabeca)
            self.__cabeca.setProximo(aux)
            self.setCalda(aux)
            self.setTamanho(self.getTamanho() +1)
            return
        else:
            self.setCabeca(No(elemento))
            self.setCalda(No(elemento))
            self.setTamanho(self.getTamanho() +1)
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

    def __str__(self):
        if self.getCabeca() == None:
            return '[]'
        string = str(self.getCabeca())
        
        if self.getCabeca() and self.getCabeca().getProximo():
            ponteiro = self.getCabeca().getProximo()
            while ponteiro.getProximo():
                string = string + ', ' +  str(ponteiro.getDado())
                ponteiro = ponteiro.getProximo()
            string = string + ', ' +  str(ponteiro.getDado())
            return '['+string+']'
        else:
            return '['+string+']'

    def __repr__(self):
        if self.getCabeca() == None:
            return '[]'
        string = str(self.getCabeca())
        
        if self.getCabeca() and self.getCabeca().getProximo():
            ponteiro = self.getCabeca().getProximo()
            while ponteiro.getProximo():
                string = string + ', ' +  str(ponteiro.getDado())
                ponteiro = ponteiro.getProximo()
            string = string + ', ' +  str(ponteiro.getDado())
            return '['+string+']'
        else:
            return '['+string+']'
        
    def __contains__(self, elemento):
        if self.__cabeca == self.__calda:
            return False
        ponteiro = self.__cabeca
        while ponteiro:
            if ponteiro.getDado() == elemento:
                return True
            else:
                ponteiro = ponteiro.getProximo()
        return False
        
    def __iter__(self):
        ponteiro = self.__cabeca
        while ponteiro:
            yield ponteiro.getDado()
            ponteiro = ponteiro.getProximo()
        raise StopIteration
        return ponteiro.getProximo()
        #return self

    def concatenar(self, iteravel):
        try:
            self.getCalda().setProximo(iteravel.getCabeca())
            self.setCalda(iteravel.getCalda())
        except:
            raise Exception("Não é possível concatenar uma lista duplamente Encadeada com algo que não seja uma lista duplamente Encadeada")
        
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
            raise ValueError("O elemento não consta na lista.")
    
    def remover(self, elemento):
        print("elemento",elemento)
        print("cabeça",self.__cabeca.getDado())
        print(elemento == self.__cabeca.getDado())
        if elemento == self.__cabeca.getDado(): 
            self.setCabeca(self.__cabeca.getProximo())
            return
        indice = self.indice(elemento)
        ponteiro = self.__cabeca
        for x in range(indice):
            ponteiro = ponteiro.getProximo()
        ponteiro.getAnterior().setProximo(ponteiro.getProximo())
        return

    def pop(self, indice):

        if indice >= self.__tamanho:
            raise IndexError("Indice fora de alcance.")
        else:
            if indice >=0:
                ponteiro = self.getCabeca()
                aux = 0
                while indice != aux:
                    ponteiro = ponteiro.getProximo()
                    aux += 1
                    
                if ponteiro == self.getCabeca():
                    self.setCabeca(ponteiro.getProximo())
                else:
                    ponteiro.getAnterior().setProximo(ponteiro.getProximo())
                if ponteiro == self.getCalda():
                    self.setCalda(ponteiro.getAnterior())
                else:
                    ponteiro.getProximo().setAnterior(ponteiro.getAnterior())
                elemento = ponteiro.getDado()
            else:
                ponteiro = self.getCalda()
                aux = -1
                while indice != aux:
                    ponteiro = ponteiro.getAnterior()
                    aux -= 1
                    
                if ponteiro == self.getCabeca():
                    self.setCabeca(ponteiro.getProximo())
                else:
                    ponteiro.getAnterior().setProximo(ponteiro.getProximo())
                if ponteiro == self.getCalda():
                    self.setCalda(ponteiro.getAnterior())
                else:
                    ponteiro.getProximo().setAnterior(ponteiro.getAnterior())
                elemento = ponteiro.getDado()
            return elemento
            
            
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