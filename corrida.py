class Pista:
    def __init__(self, nome, pais, cidade, tamanho):
        self.__nome = nome
        self.__pais = pais
        self.__cidade = cidade
        self.__tamanho = tamanho

    @property
    def nome(self):
        return self.__nome
    
    @property
    def pais(self):
        return self.__pais
    
    @property
    def cidade(self):
        return self.__cidade
    
    @property
    def tamanho(self):
        return self.__tamanho
    
    def __str__(self):
        return f"Nome: {self.__nome}\nPaís: {self.__pais}\nCidade: {self.__cidade}\nTamanho: {self.__tamanho} km"
    
class Resultado:
    def __init__(self, Piloto, posicao):
        self.__Piloto = Piloto
        self.__posicao = posicao

    @property
    def Piloto(self):
        return self.__Piloto
    
    @property
    def posicao(self):
        return self.__posicao
    
    def __str__(self):
        ret = f"Piloto: {self.__Piloto.nome}"

        if self.__posicao == 0:
            ret += f" - Não terminou a corrida"
        elif self.__posicao == -1:
            ret += f" - Não largou"
        elif self.__posicao == -2:
            ret += f" - Desclassificado"
        else:
            ret += f" - Posição: P{self.__posicao}"

        return ret
    
class Corrida:
    def __init__(self, Pista, data, hora, resultados):
        self.__Pista = Pista
        self.__data = data
        self.__hora = hora
        self.__resultados = resultados

    @property
    def Pista(self):
        return self.__Pista
    
    @property
    def data(self):
        return self.__data
    
    @property
    def hora(self):
        return self.__hora
    
    @property
    def resultados(self):
        return self.__resultados
    
    def __str__(self):
        ret = f"Data: {self.__data}\nHora: {self.__hora}\nPista: {self.__Pista.nome}\nPaís: {self.__Pista.pais}\nCidade: {self.__Pista.cidade}\nTamanho: {self.__Pista.tamanho} km\n\nResultados:"

        for i in range(len(self.__resultados)):
            ret += f"\n{i+1}º - {self.__resultados[i].Piloto.nome}"

        return ret
    
class CtrlCorrida:
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaCorridas = []