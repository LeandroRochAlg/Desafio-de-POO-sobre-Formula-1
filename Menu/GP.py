import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle
import model

class LimiteCriaGP(tk.Toplevel):
    def __init__(self, controle, pistas):
        tk.Toplevel.__init__(self)
        self.geometry('400x400')
        self.title("Registrar corrida")
        self.controle = controle

        self.frameGP = tk.Frame(self)               #Frame para o nome do GP
        self.framePista = tk.Frame(self)            #Frame para a pista
        self.frameButton = tk.Frame(self)           #Frame para os botões

        self.frameGP.pack()
        self.framePista.pack()
        self.frameButton.pack()

        self.labelGP = tk.Label(self.frameGP, text="Nome do GP: ")
        self.labelGP.pack(side="left")
        self.inputGP = tk.Entry(self.frameGP, width=30)
        self.inputGP.pack(side="left")

        # Combobox para escolher a pista
        self.labelPista = tk.Label(self.framePista, text="Pista: ")
        self.labelPista.pack(side="left")
        self.escolhaPista = tk.StringVar()
        self.comboPista = ttk.Combobox(self.framePista, width=27, textvariable=self.escolhaPista, values=pistas)
        self.comboPista.pack(side="left")

        # Botões
        self.buttonSprint = tk.Button(self.frameButton, text="Cadastrar Sprint", font=('negrito', 9))
        self.buttonSprint.pack(side="left")
        self.buttonSprint.bind("<Button>", controle.cadastrarSprint)

        self.buttonCorrida = tk.Button(self.frameButton, text="Cadastrar Corrida", font=('negrito', 9))
        self.buttonCorrida.pack(side="left")
        self.buttonCorrida.bind("<Button>", controle.cadastrarCorrida)

        self.buttonCancela = tk.Button(self.frameButton, text="Cancelar", font=('negrito', 9))
        self.buttonCancela.pack(side="left")
        self.buttonCancela.bind("<Button>", controle.cancelaHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído", font=('negrito', 9))
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.concluiHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)    
    
class CtrlGP:
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaGPs = []

        if not os.path.isfile("Cadastros/GPs.pickle"):
            self.listaGPs = []
        else:
            with open("Cadastros/GPs.pickle", "rb") as f:
                self.listaGPs = pickle.load(f)

    def cadastrarGP(self):
        pistas = []

        for pista in self.ctrlPrincipal.ctrlPista.listaPistas:
            pistas.append(pista.nome)

        self.limiteGP = LimiteCriaGP(self, pistas)

    def cadastrarSprint(self, event):
        pass

    def cadastrarCorrida(self, event):
        pass

    def concluiHandler(self, event):
        pass

    def consultarGP(self):
        pass