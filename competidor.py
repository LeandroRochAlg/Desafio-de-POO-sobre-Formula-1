from abc import ABC, abstractmethod

class Competidor(ABC):  #Classe abstrata para equipe e piloto
    def __init__(self, nome, pais):
        self.__nome = nome
        self.__pais = pais

    @property
    def nome(self):
        return self.__nome
    
    @property
    def país(self):
        return self.__pais
    
    @abstractmethod #Método abstrato para ser implementado nas classes filhas
    def __str__(self):  #Método para criar o retorno do print da classe
        pass

class Equipe(Competidor):
    def __init__(self, nome, pais, chefeEquipe, Motor = None):
        super().__init__(nome, pais)
        self.__chefeEquipe = chefeEquipe

        if Motor == None:   #Motor é um objeto da classe Equipe, pode ser ela mesma se a equipe fabrica os próprios motores
            self.__Motor = self
        else:
            self.__Motor = Motor

    @property
    def chefeEquipe(self):
        return self.__chefeEquipe
    
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

    @property
    def Equipe(self):
        return self.__Equipe
    
    @property
    def pontos(self):
        return self.__pontos
    
    def __str__(self):
        return f"Nome: {self.__nome}\nPaís: {self.__pais}\nEquipe: {self.__Equipe.nome}\nPontos: {self.__pontos}"