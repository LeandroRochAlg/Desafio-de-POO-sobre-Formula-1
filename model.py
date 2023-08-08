from abc import ABC, abstractmethod

class Competidor(ABC):  #Classe abstrata para equipe e piloto
    def __init__(self, nome, pais):
        self.nome = nome
        self.pais = pais

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if nome == "":
            raise ValueError("O nome não pode ser vazio")
        else:
            self.__nome = nome
    
    @property
    def pais(self):
        return self.__pais
    
    @pais.setter
    def pais(self, pais):
        if pais == "":
            raise ValueError("O país não pode ser vazio")
        else:
            self.__pais = pais
    
    @abstractmethod #Método abstrato para ser implementado nas classes filhas
    def __str__(self):  #Método para criar o retorno do print da classe
        pass

class Equipe(Competidor):
    def __init__(self, nome, pais, chefeEquipe, Motor = None):
        super().__init__(nome, pais)
        self.chefeEquipe = chefeEquipe

        if Motor == None:   #Motor é um objeto da classe Equipe, pode ser ela mesma se a equipe fabrica os próprios motores
            self.__Motor = self
        else:
            self.__Motor = Motor

    @property
    def chefeEquipe(self):
        return self.__chefeEquipe
    
    @chefeEquipe.setter
    def chefeEquipe(self, chefeEquipe):
        if chefeEquipe == "":
            raise ValueError("O chefe de equipe não pode ser vazio")
        else:
            self.__chefeEquipe = chefeEquipe
    
    @property
    def Motor(self):
        return self.__Motor
    
    def __str__(self):
        return f"Nome: {self.__nome}\nPaís: {self.__pais}\nChefe de equipe: {self.__chefeEquipe}\nMotor: {self.__Motor.nome}"
    
class Piloto(Competidor):
    def __init__(self, nome, pais, numero, Equipe, pontos):
        super().__init__(nome, pais)
        self.__numero = numero
        self.__Equipe = Equipe
        self.__pontos = pontos

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        if numero == "":
            raise ValueError("O número não pode ser vazio")
        elif not numero.isdigit():  #Verifica se o número é um inteiro
            raise ValueError("O número deve ser um inteiro")
        elif int(numero) <= 0:
            raise ValueError("O número não pode ser negativo ou zero")
        else:
            self.__numero = numero

    @property
    def Equipe(self):
        return self.__Equipe
    
    @property
    def pontos(self):
        return self.__pontos
    
    @pontos.setter
    def pontos(self, pontos):
        if pontos == "":
            raise ValueError("Os pontos não podem ser vazios")
        else:
            self.__pontos = pontos
    
    def __str__(self):
        return f"Nome: {self.__nome}\nPaís: {self.__pais}\nEquipe: {self.__Equipe.nome}\nPontos: {self.__pontos}"
    
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