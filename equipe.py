import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle
import model
    
class LimiteCadastraEquipe(tk.Toplevel):
    def __init__(self, controle, fabricaMotores):
        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Cadastrar equipe")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.framePais = tk.Frame(self)
        self.frameChefeEquipe = tk.Frame(self)
        self.frameMark = tk.Frame(self)
        self.frameMotor = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameNome.pack()
        self.framePais.pack()
        self.frameChefeEquipe.pack()
        self.frameMark.pack()
        self.frameMotor.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelPais = tk.Label(self.framePais, text="País: ")
        self.labelChefeEquipe = tk.Label(self.frameChefeEquipe, text="Chefe de equipe: ")
        self.labelMark = tk.Label(self.frameMark, text="Equipe fabrica motores? ")
        self.labelMotor = tk.Label(self.frameMotor, text="Motor: ")

        self.labelNome.pack(side="left")
        self.labelPais.pack(side="left")
        self.labelChefeEquipe.pack(side="left")
        self.labelMark.pack(side="left")
        self.labelMotor.pack(side="left")

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputPais = tk.Entry(self.framePais, width=20)
        self.inputChefeEquipe = tk.Entry(self.frameChefeEquipe, width=20)

        # Mark para escolher se a equipe fabrica os próprios motores
        self.escolhaMark = tk.IntVar()
        self.checkSim = tk.Checkbutton(self.frameMark, text="Sim", variable=self.escolhaMark, onvalue=1, offvalue=0)

        # Combobox para escolher o motor
        self.escolhaMotor = tk.StringVar()
        self.comboMotor = ttk.Combobox(self.frameMotor, width=17, textvariable=self.escolhaMotor, values=fabricaMotores)

        self.inputNome.pack(side="left")
        self.inputPais.pack(side="left")
        self.inputChefeEquipe.pack(side="left")
        self.checkSim.pack(side="left")
        self.comboMotor.pack(side="left")

        # Botões
        self.buttonSubmit = tk.Button(self.frameButton, text="Enter", font=('negrito', 9))
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandlerEquipe)

        self.buttonClear = tk.Button(self.frameButton, text="Clear", font=('negrito', 9))
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandlerEquipe)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído", font=('negrito', 9))
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandlerEquipe)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraEquipes(tk.Toplevel):
    def __init__(self, equipes):
        tk.Toplevel.__init__(self)
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

        if not os.path.isfile("equipes.pickle"):
            self.listaEquipes = []
        else:
            with open("equipes.pickle", "rb") as f:
                self.listaEquipes = pickle.load(f)

    def cadastrarEquipe(self):
        listaMotores = []

        for equipe in self.listaEquipes:    #Pega os motores já cadastrados
            if equipe.Motor.nome == equipe.nome:
                listaMotores.append(equipe.Motor.nome)

        self.limiteCadastra = LimiteCadastraEquipe(self, listaMotores)

    def enterHandlerEquipe(self, event):
        nome = self.limiteCadastra.inputNome.get()
        pais = self.limiteCadastra.inputPais.get()
        chefeEquipe = self.limiteCadastra.inputChefeEquipe.get()
        motor = self.limiteCadastra.escolhaMotor.get()
        mark = self.limiteCadastra.escolhaMark.get()

        if mark == 1:
            try:
                equipe = model.Equipe(nome, pais, chefeEquipe)

                self.listaEquipes.append(equipe)
                self.limiteCadastra.mostraJanela('Sucesso', 'Equipe cadastrada com sucesso')
                self.clearHandlerEquipe(event)
            except ValueError as error:
                self.limiteCadastra.mostraJanela('Erro', error)
        else:
            for equipe in self.listaEquipes:    #Pega a classe do motor escolhido
                if motor == equipe.nome:
                    Motor = equipe

            try:
                equipe = model.Equipe(nome, pais, chefeEquipe, Motor)

                self.listaEquipes.append(equipe)
                self.limiteCadastra.mostraJanela('Sucesso', 'Equipe cadastrada com sucesso')
                self.clearHandlerEquipe(event)
            except ValueError as error:
                self.limiteCadastra.mostraJanela('Erro', error)

    def clearHandlerEquipe(self, event):
        self.limiteCadastra.inputNome.delete(0, len(self.limiteCadastra.inputNome.get()))
        self.limiteCadastra.inputPais.delete(0, len(self.limiteCadastra.inputPais.get()))
        self.limiteCadastra.inputChefeEquipe.delete(0, len(self.limiteCadastra.inputChefeEquipe.get()))
        self.limiteCadastra.comboMotor.delete(0, len(self.limiteCadastra.comboMotor.get()))

    def fechaHandlerEquipe(self, event):
        self.limiteCadastra.destroy()

    def salvaEquipes(self):
        if len(self.listaEquipes) != 0:
            with open("equipes.pickle", "wb") as f:
                pickle.dump(self.listaEquipes, f)