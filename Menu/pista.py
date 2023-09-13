import tkinter as tk
from tkinter import messagebox
import os.path
import pickle
import model

class LimiteCadastraPista(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Cadastrar pista")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.framePais = tk.Frame(self)
        self.frameCidade = tk.Frame(self)
        self.frameExtensao = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameNome.pack()
        self.framePais.pack()
        self.frameCidade.pack()
        self.frameExtensao.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelPais = tk.Label(self.framePais, text="País: ")
        self.labelCidade = tk.Label(self.frameCidade, text="Cidade: ")
        self.labelExtensao = tk.Label(self.frameExtensao, text="Extensão em metros: ")

        self.labelNome.pack(side="left")
        self.labelPais.pack(side="left")
        self.labelCidade.pack(side="left")
        self.labelExtensao.pack(side="left")

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputPais = tk.Entry(self.framePais, width=20)
        self.inputCidade = tk.Entry(self.frameCidade, width=20)
        self.inputExtensao = tk.Entry(self.frameExtensao, width=20)

        self.inputNome.pack(side="left")
        self.inputPais.pack(side="left")
        self.inputCidade.pack(side="left")
        self.inputExtensao.pack(side="left")

        # Botões
        self.buttonSubmit = tk.Button(self.frameButton, text="Enter", font=('negrito', 9))
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Clear", font=('negrito', 9))
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído", font=('negrito', 9))
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraPistas(tk.Toplevel):
    def __init__(self, controle, listaPistas):
        tk.Toplevel.__init__(self)
        self.geometry('600x550')
        self.title("Pistas cadastradas")
        self.controle = controle

        self.framePistas = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.framePistas.pack()
        self.frameButton.pack()

        self.labelPistas = tk.Label(self.framePistas, text="Pistas: ")
        self.labelPistas.pack(side="left")

        self.textPistas = tk.Text(self.framePistas, height=30, width=50, wrap=tk.WORD)
        self.textPistas.pack(side="left")
        self.textPistas.insert(tk.END, listaPistas)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído", font=('negrito', 9))
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaListaHandler)

class CtrlPista:
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaPistas = []

        if not os.path.isfile("Cadastros/pistas.pickle"):
            self.listaPistas = []
        else:
            with open("Cadastros/pistas.pickle", "rb") as f:
                self.listaPistas = pickle.load(f)

    def cadastrarPista(self):
        self.limiteCadastra = LimiteCadastraPista(self)

    def enterHandler(self, event):
        nome = self.limiteCadastra.inputNome.get()
        pais = self.limiteCadastra.inputPais.get()
        cidade = self.limiteCadastra.inputCidade.get()

        # Verifica se a extensão é um número
        try:
            extensao = int(self.limiteCadastra.inputExtensao.get())
        except ValueError:
            self.limiteCadastra.mostraJanela('Erro', 'A extensão deve ser um número inteiro')

        try:
            pista = model.Pista(nome, pais, cidade, extensao)
            self.listaPistas.append(pista)
            self.limiteCadastra.mostraJanela('Sucesso', 'Pista cadastrada com sucesso')
            self.clearHandler(event)
        except ValueError as error:
            self.limiteCadastra.mostraJanela('Erro', error)

    def clearHandler(self, event):
        self.limiteCadastra.inputNome.delete(0, len(self.limiteCadastra.inputNome.get()))
        self.limiteCadastra.inputPais.delete(0, len(self.limiteCadastra.inputPais.get()))
        self.limiteCadastra.inputCidade.delete(0, len(self.limiteCadastra.inputCidade.get()))
        self.limiteCadastra.inputExtensao.delete(0, len(self.limiteCadastra.inputExtensao.get()))

    def fechaHandler(self, event):
        self.limiteCadastra.destroy()

    def listarPistas(self):
        pistas = ''

        for pista in self.listaPistas:
            pistas += str(pista) + '\n\n'

        self.limiteLista = LimiteMostraPistas(self, pistas)

    def fechaListaHandler(self, event):
        self.limiteLista.destroy()

    def salvaPistas(self):
        if len(self.listaPistas) != 0:
            with open("Cadastros/pistas.pickle", "wb") as f:
                pickle.dump(self.listaPistas, f)