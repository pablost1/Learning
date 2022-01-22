class Candidato:
    def __init__(self, **kwargs):
        self.__anoEleicao = kwargs.get('anoEleicao', None)
        self.__siglaUF = kwargs.get('siglaUF', None)
        self.__codigoCargo = kwargs.get('codigoCargo', None)
        self.__descricaoCargo = kwargs.get('descricaoCargo', None)
        self.__nomeCandidato = kwargs.get('nomeCandidato', None)
        self.__IDCandidato = kwargs.get('IDCandidato', None)
        self.__numeroUrna = kwargs.get('numeroUrna', None)
        self.__CPF = kwargs.get('CPF', None)
        self.__nomeUrna = kwargs.get('nomeUrna', None)
        self.__numeroPartido = kwargs.get('numeroPartido', None)
        self.__siglaPartido = kwargs.get('siglaPartido', None)
        self.__codigoOcupacaoCandidato = kwargs.get('codigoOcupacaoCandidato', None)
        self.__descricaoOcupacao = kwargs.get('descricaoOcupacao', None)
        self.__dataNascimento = kwargs.get('dataNascimento', None) #DD/MM/AAAA
        self.__sexo = kwargs.get('sexo', None) 
        self.__grauInstrucao = kwargs.get('grauInstrucao', None)
        self.__estadoCivil = kwargs.get('estadoCivil', None)
        self.__UFnascimento = kwargs.get('UFnascimento', None)
        self.__nomeMunicipioNascimento = kwargs.get('nomeMunicipioNascimento', None)
        self.__situacaoCandidatoPosPleito = kwargs.get('sitCandidatoPosPleito', None)
        self.__situacaoCandidatura = kwargs.get('situacaoCandidatura', None)
        self.__listaBens = kwargs.get('listaBens', None)
        return 
    def __str__(self):
        
        return str(str(self.__nomeUrna)+" -- "+str(self.__numeroUrna)+" -- "+str(self.__siglaPartido)+"\n"+str(self.__descricaoCargo)+"("+str(self.__siglaUF)+") "+str(self.__nomeMunicipioNascimento)+"("+str(self.__UFnascimento)+")"+"\n"+"Resumo dos bens:"+"\n"+"  - Total declarado: R$"+str(sum([x.getBemValor() for x in self.__listaBens])))
    def __repr__(self):
        return self.__str__()
        
    ### Gets n' Sets ###
    def getAnoEleicao(self):
        return self.__anoEleicao
    def setAnoEleicao(self, ano):
        self.__anoEleicao = ano
        return

    def getSiglaUF(self):
        return self.__siglaUF
    def setSiglaUF(self, sigla):
        self.__siglaUF = sigla
        return

    def getCodigoCargo(self):
        return self.__codigoCargo
    def setCodigoCargo(self, codigo):
        self.__codigoCargo = codigo
        return

    def getDescricaoCargo(self):
        return self.__descricaoCargo
    def setDescricaoCargo(self, descricaoCargo):
        self.__descricaoCargo = descricaoCargo
        return

  
    def getNomeCandidato(self):
        return self.__nomeCandidato
    def setNomeCandidato(self, nomeCandidato):
        self.__nomeCandidato = nomeCandidato
        return

    def getIDCandidato(self):
        return self.__IDCandidato
    def setIDCandidato(self, ID):
        self.__IDCandidato = ID
        return

    def getNumeroUrna(self):
        return self.__numeroUrna
    def setNumeroUrna(self, numeroUrna):
        self.__numeroUrna = numeroUrna
        return

    def getCPF(self):
        return self.__CPF
    def setCPF(self, CPF):
        self.__CPF = CPF
        return

    def getNomeUrna(self):
        return self.__nomeUrna
    def setNomeUrna(self, nomeUrna):
        self.__nomeUrna = nomeUrna
        return

    def getNumeroPartido(self):
        return self.__numeroPartido
    def setNumeroPartido(self, numeroPartido):
        self.__numeroPartido = numeroPartido
        return

    def getSiglaPartido(self):
        return self.__siglaPartido
    def setSiglaPartido(self, siglaPartido):
        self.__siglaPartida = siglaPartido
        return

    def getCodigoOcupacaoCandidato(self):
        return self.__codigoOcupacaoCandidato
    def setCodigoOcupacaoCandidato(self, codigoOcupacaoCandidato):
        self.__codigoOcupacaoCandidato = codigoOcupacaoCandidato
        return

    def getDescricaoOcupacao(self):
        return self.__descricaoOcupacao
    def setDescricaoOcupacao(self, descricaoOcupacao):
        self.__descricaoOcupacao = descricaoOcupacao
        return

    def getDataNascimento(self):
        return self.__dataNascimento
    def setDataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento
        return

    def getSexo(self):
        return self.__sexo
    def setSexo(self, sexo):
        self.__sexo = sexo
        return

    def getGrauInstrucao(self):
        return self.__grauInstrucao
    def setGrauInstrucao(self, grauInstrucao):
        self.__grauInstrucao = grauInstrucao
        return

    def getEstadoCivil(self):
        return self.__estadoCivil
    def setEstadoCivil(self, estadoCivil):
        self.__estadoCivil = estadoCivil
        return
    
    def getUFNascimento(self):
        return self.__UFnascimento
    def setUFNascimento(self, UF):
        self.__UFnascimento = UF
        return
    
    def getNomeMunicipioNascimento(self):
        return self.nomeMunicipioNascimento
    def setNomeMunicipioNascimento(self, municipio):
        self.__nomeMunicipioNascimento = municipio
        return
    
    def getSituacaoCandidatoPosPleito(self):
        return self.__situacaoCandidatoPosPleito
    def setSituacaoCandidatoPosPleito(self, situacao):
        self.__situacaoCandidatoPosPleito = situacao
        return
    
    def getSituacaoCandidatura(self):
        return self.__situacaoCandidatura
    def setSituacaoCandidatura(self, situacao):
        self.__situacaoCandidatura = situacao
        return
    
    def getListaBens(self):
        return self.__listaBens
    def setListaBens(self, lista):
        self.__listaBens = lista
        return