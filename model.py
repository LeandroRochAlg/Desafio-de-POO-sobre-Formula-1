from abc import ABC, abstractmethod

class Competidor(ABC):  #Classe abstrata para equipe e piloto
    def __init__(self, nome, pais):
        self.nome = nome
        self.pais = pais
        self.pontos = 0

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

    @property
    def pontos(self):
        return self.__pontos
    
    @pontos.setter
    def pontos(self, pontos):
        self.__pontos = pontos

    def adicionaPontos(self, pontos):
        self.__pontos += pontos
    
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
    def __init__(self, nome, pais, numero, Equipe):
        super().__init__(nome, pais)
        self.numero = numero
        self.__Equipe = Equipe

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        if numero == "":
            raise ValueError("O número não pode ser vazio")
        elif numero <= 0:
            raise ValueError("O número não pode ser negativo ou zero")
        else:
            self.__numero = numero

    @property
    def Equipe(self):
        return self.__Equipe
    
    def __str__(self):
        return f"Nome: {self.nome}\nPaís: {self.pais}\nEquipe: {self.__Equipe.nome}\nPontos: {self.__pontos}"
    
class Pista:
    def __init__(self, nome, pais, cidade, tamanho):
        self.__nome = nome
        self.__pais = pais
        self.__cidade = cidade
        self.tamanho = tamanho

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
    
    @tamanho.setter
    def tamanho(self, tamanho):
        if tamanho <= 3000 and self.__pais != 'Mônaco':  #Mônaco é exceção pois tem menos de 3000 m
            raise ValueError("O tamanho da pista não pode ser menor que 3000 m")
        elif tamanho >= 7000 and self.__nome != 'Spa-Francorchamps':    #Spa é exceção pois tem 7004 m
            raise ValueError("O tamanho da pista não pode ser maior que 7000 m")
        else:
            self.__tamanho = tamanho
    
    def __str__(self):
        return f"Nome: {self.__nome}\nPaís: {self.__pais}\nCidade: {self.__cidade}\nTamanho: {self.__tamanho} m"
    
class Resultado:
    def __init__(self, Piloto, posicao, voltaRapida):
        self.__Piloto = Piloto
        self.__posicao = posicao
        self.__voltaRapida = voltaRapida

    @property
    def Piloto(self):
        return self.__Piloto
    
    @property
    def posicao(self):
        return self.__posicao
    
    @property
    def voltaRapida(self):
        return self.__voltaRapida
    
    def __str__(self):
        ret = f"Piloto: {self.__Piloto.nome}"

        if self.__posicao == 1000:
            ret += f" - Não terminou"
        elif self.__posicao == 2000:
            ret += f" - Não largou"
        elif self.__posicao == 3000:
            ret += f" - Desclassificado"
        else:
            ret += f" - P{self.__posicao}"

        if self.__voltaRapida:
            ret += " - Volta mais rápida"

        return ret
    
class Corrida:
    def __init__(self, data, nVoltas, resultados):
        self.__data = data
        self.__nVoltas = nVoltas
        self.__resultados = resultados
    
    @property
    def data(self):
        return self.__data
    
    @property
    def nVoltas(self):
        return self.__nVoltas
    
    @property
    def resultados(self):
        return self.__resultados
    
    @resultados.setter
    def resultados(self, resultados):
        self.__resultados = resultados

    def adicionaResultado(self, Resultado):
        self.__resultados.append(Resultado)
    
    def __str__(self):
        ret = f"Data: {self.__data}\nResultados:"

        #Ordena os resultados pela posição
        for i in range(len(self.__resultados)):
            for j in range(len(self.__resultados)):
                if self.__resultados[i].posicao < self.__resultados[j].posicao:
                    aux = self.__resultados[i]
                    self.__resultados[i] = self.__resultados[j]
                    self.__resultados[j] = aux

            ret += f"\n{i+1}º - {self.__resultados[i]}"

        return ret
    
class GP:
    def __init__(self, nome, Pista, Corrida, Sprint = None):
        self.__nome = nome
        self.__Pista = Pista
        self.__Corrida = Corrida
        self.__Sprint = Sprint

    @property
    def nome(self):
        return self.__nome
    
    @property
    def Pista(self):
        return self.__Pista

    @property
    def Corrida(self):
        return self.__Corrida
    
    @property
    def Sprint(self):
        return self.__Sprint
    
    def __str__(self):
        ret = f"Nome: {self.__nome}\nPista: {self.__Pista.nome}\n"

        if self.__Sprint != None:   #Se tiver sprint, adiciona no retorno
            ret += f"\nSPRINT"
            ret += f"{self.__Sprint}"   #Chama o método __str__ da classe Corrida

        ret += f"\nCORRIDA"
        ret += f"{self.__Corrida}"

        return ret