class Bem:
    def __init__(self, **kwargs):
        self.__bem_codigo = kwargs.get("bem_codigo", None)
        self.__bem_descricao = kwargs.get("bem_descricao", None)
        self.__bem_descricao_detailed = kwargs.get("bem_descricao_detailed", None)
        self.__bem_valor = kwargs.get("bem_valor", None)
        return
    
    def __str__(self):
        return str(self.__bem_codigo)+" -- "+str(self.__bem_descricao)+" -- "+str(self__bem_valor)+"Descrição:"+str(self.__bemDescDetailed)
    
    def __repr(self):
        return "bem_codigo:"+str(self.__bemCodigo)+", bem_descricao:"+str(self.__bemDesc)+", bem_descricao_detailed:"+str(self.__bemDescDetailed)+", bem_valor:"+str(self.__bemValor)

    ### Gets n' Sets ##
    def getBemCodigo(self):
        return self.__bem_codigo
    def setBemCodigo(self, codigo):
        self.__bem_codigo = codigo
        return
    
    def getBemDescricao(self):
        return self.__bem_descricao
    def setBemDescricao(self, descricao):
        self.__bem_descricao = descricao
        return
    
    def getBemDescricaoDetailed(self):
        return self.__bem_descricao_detailed
    def setBemDescricaoDetailed(self, descricao):
        self.__bem_descricao_detailed = descricao
        return
    
    def getBemValor(self):
        return self.__bem_valor
    def setBemValor(self, valor):
        self._self.__bem_valor
        return