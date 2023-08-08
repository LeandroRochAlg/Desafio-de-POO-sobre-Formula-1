import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle
    
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