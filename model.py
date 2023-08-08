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