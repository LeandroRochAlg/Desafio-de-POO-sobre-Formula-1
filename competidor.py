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
    def __init__(self, nome, pais, chefeEquipe, Motor):
        super().__init__(nome, pais)
        self.__chefeEquipe = chefeEquipe
        self.__Motor = Motor    #Motor é um objeto da classe Equipe, pode ser ela mesma se a equipe fabrica os próprios motores

    @property
    def chefeEquipe(self):
        return self.__chefeEquipe
    
    @property
    def Motor(self):
        return self.__Motor
    
    def __str__(self):
        return f"Nome: {self.nome}\nPaís: {self.país}\nChefe de equipe: {self.chefeEquipe}\nMotor: {self.Motor.nome}"
    
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
    def equipe(self):
        return self.__Equipe
    
    @property
    def pontos(self):
        return self.__pontos
    
    def __str__(self):
        return f"Nome: {self.nome}\nPaís: {self.país}\nEquipe: {self.Equipe.nome}\nPontos: {self.pontos}"