import time

class Cronometro:
    def __init__(self):
        self.__inicio = 0
        self.__fim = 0
        self.__tempoDecorrido = 0.0
        return
    def __str__(self):
        return str(self.__tempoDecorrido)
    def __repr__(self):
        
        return self

    def iniciar(self):
        self.__setInicio(time.clock())
        return

    def parar(self):
        self.__setFim(time.clock())
        self.__setTempo((self.__getFim()-self.__getInicio()))
        return

    def zerar(self):
        self.__setFim(0)
        self.__setInicio(0)
        self.__setTempo(0.0)
        return

    def exibir(self):
        print("Tempo decorrido:",round(self.__getTempo(),3),"Segundos")
        return
    ################### Gets and Sets ###################
    def __getTempo(self):
        return self.__tempoDecorrido
    def __setTempo(self, novoTempo):
        self.__tempoDecorrido = novoTempo
        return

    def __getInicio(self):
        return self.__inicio
    def __setInicio(self,novoInicio):
        self.__inicio = novoInicio
        return

    def __getFim(self):
        return self.__fim
    def __setFim(self, novoFim):
        self.__fim = novoFim
        return


