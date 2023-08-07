from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle

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
    
class LimiteCadastraEquipe(tk.Toplevel):
    def __init__(self, controle, fabricaMotores):
        tk.Toplevel().__init__(self)
        self.geometry('300x250')
        self.title("Cadastrar equipe")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.framePais = tk.Frame(self)
        self.frameChefeEquipe = tk.Frame(self)
        self.frameMotor = tk.Frame(self)

        self.frameNome.pack()
        self.framePais.pack()
        self.frameChefeEquipe.pack()
        self.frameMotor.pack()

        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelPais = tk.Label(self.framePais, text="País: ")
        self.labelChefeEquipe = tk.Label(self.frameChefeEquipe, text="Chefe de equipe: ")
        self.labelMotor = tk.Label(self.frameMotor, text="Motor: ")

        self.labelNome.pack(side="left")
        self.labelPais.pack(side="left")
        self.labelChefeEquipe.pack(side="left")
        self.labelMotor.pack(side="left")

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputPais = tk.Entry(self.framePais, width=20)
        self.inputChefeEquipe = tk.Entry(self.frameChefeEquipe, width=20)

        self.escolhaMotor = tk.StringVar()
        self.comboMotor = ttk.Combobox(self.frameMotor, width=17, textvariable=self.escolhaMotor, values=fabricaMotores)

        self.inputNome.pack(side="left")
        self.inputPais.pack(side="left")
        self.inputChefeEquipe.pack(side="left")
        self.comboMotor.pack(side="left")

        self.buttonSubmit = tk.Button(self, text="Enter", font=('negrito', 9))
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandlerEquipe)

        self.buttonClear = tk.Button(self, text="Clear", font=('negrito', 9))
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandlerEquipe)

        self.buttonFecha = tk.Button(self, text="Concluído", font=('negrito', 9))
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandlerEquipe)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraEquipes(tk.Toplevel):
    def __init__(self, equipes):
        self.janela = tk.Tk()
        self.janela.title("Equipes")

        self.frameTabela = tk.Frame(self.janela)
        self.frameTabela.pack()

        #Cria a tabela
        self.tabela = ttk.Treeview(self.frameTabela, columns=('pais', 'chefeEquipe', 'motor'), show='headings')
        self.tabela.column('pais', minwidth=0, width=100)
        self.tabela.column('chefeEquipe', minwidth=0, width=100)
        self.tabela.column('motor', minwidth=0, width=100)

        self.tabela.heading('pais', text='País')
        self.tabela.heading('chefeEquipe', text='Chefe de equipe')
        self.tabela.heading('motor', text='Motor')

        self.tabela.pack()

        #Adiciona os dados na tabela
        for equipe in equipes:
            self.tabela.insert('', 'end', values=(equipe.nome, equipe.pais, equipe.chefeEquipe, equipe.Motor.nome))

class CtrlEquipe:
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaEquipes = []
        self.listaMotores = []

        if not os.path.isfile("equipes.pickle"):
            self.listaEquipes = []
        else:
            with open("equipes.pickle", "rb") as f:
                self.listaEquipes = pickle.load(f)

        if not os.path.isfile("motores.pickle"):
            self.listaMotores = []
        else:
            with open("motores.pickle", "rb") as f:
                self.listaMotores = pickle.load(f)

    def cadastrarEquipe(self):
        self.listaMotores = ['Ferrari', 'Mercedes', 'Red Bull', 'Alpine']
        self.limiteCadastra = LimiteCadastraEquipe(self, self.listaMotores)

class CtrlPiloto:
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaPilotos = []

        if not os.path.isfile("pilotos.pickle"):
            self.listaPilotos = []
        else:
            with open("pilotos.pickle", "rb") as f:
                self.listaPilotos = pickle.load(f)

class CtrlPista:
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaPistas = []

        if not os.path.isfile("pistas.pickle"):
            self.listaPistas = []
        else:
            with open("pistas.pickle", "rb") as f:
                self.listaPistas = pickle.load(f)