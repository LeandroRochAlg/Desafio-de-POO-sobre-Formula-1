import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle
import model
import datetime

class LimiteCriaGP(tk.Toplevel):
    def __init__(self, controle, pistas):
        tk.Toplevel.__init__(self)
        self.geometry('400x400')
        self.title("Registrar corrida")
        self.controle = controle

        self.frameGP = tk.Frame(self)               #Frame para o nome do GP
        self.framePista = tk.Frame(self)            #Frame para a pista
        self.frameData = tk.Frame(self)             #Frame para a data
        self.frameButton = tk.Frame(self)           #Frame para os botões

        self.frameGP.pack()
        self.framePista.pack()
        self.frameData.pack()
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

        # Escolha de data
        self.labelData = tk.Label(self.frameData, text="Data de início do GP: ")
        self.labelData.pack(side="top")
        # Combobox para escolher o dia
        self.labelDia = tk.Label(self.frameData, text="Dia: ")
        self.labelDia.pack(side="left")
        self.escolhaDia = tk.IntVar()
        self.comboDia = ttk.Combobox(self.frameData, width=3, textvariable=self.escolhaDia, values=list(range(1, 32)))
        self.comboDia.pack(side="left")

        # Combobox para escolher o mês
        self.labelMes = tk.Label(self.frameData, text="Mês: ")
        self.labelMes.pack(side="left")
        self.escolhaMes = tk.IntVar()
        self.comboMes = ttk.Combobox(self.frameData, width=3, textvariable=self.escolhaMes, values=list(range(1, 13)))
        self.comboMes.pack(side="left")

        # Combobox para escolher o ano
        self.labelAno = tk.Label(self.frameData, text="Ano: ")
        self.labelAno.pack(side="left")
        self.escolhaAno = tk.IntVar()
        self.comboAno = ttk.Combobox(self.frameData, width=5, textvariable=self.escolhaAno, values=list(range(1950, 2031))) #1950 foi a primeira temporada da Formula 1
        self.comboAno.pack(side="left")

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

class LimiteCadastraSprint(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x400')
        self.title("Registrar sprint")
        self.controle = controle

        self.frameSprint = tk.Frame(self)               #Frame para o nome do GP
        self.frameButton = tk.Frame(self)           #Frame para os botões

        self.frameSprint.pack()
        self.frameButton.pack()

        self.labelSprint = tk.Label(self.frameSprint, text="Sprint: ")
        self.labelSprint.pack(side="left")
        self.inputSprint = tk.Entry(self.frameSprint, width=30)
        self.inputSprint.pack(side="left")

        # Botões
        self.buttonCancela = tk.Button(self.frameButton, text="Cancelar", font=('negrito', 9))
        self.buttonCancela.pack(side="left")
        self.buttonCancela.bind("<Button>", controle.cancelaHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído", font=('negrito', 9))
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.concluiHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteCadastraCorrida(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('800x400')
        self.title("Registrar corrida")
        self.controle = controle

        self.framePiloto = tk.Frame(self)
        self.frameButton = tk.Frame(self)           #Frame para os botões

        self.framePiloto.pack()
        self.frameButton.pack()

        self.labelPiloto = tk.Label(self.framePiloto, text="Número do piloto: ")
        self.labelPiloto.pack(side="left")
        self.inputPiloto = tk.Entry(self.framePiloto, width=5)
        self.inputPiloto.pack(side="left")
        self.labelPiloto = tk.Label(self.framePiloto, text="Posição: ")
        self.labelPiloto.pack(side="left")
        self.inputPiloto = tk.Entry(self.framePiloto, width=5)
        self.inputPiloto.pack(side="left")

        self.labelVoltaRapida = tk.Label(self.framePiloto, text="Volta mais rápida: ")
        self.labelVoltaRapida.pack(side="left")
        self.marcaVoltaRapida = tk.IntVar()
        self.checkVoltaRapida = tk.Checkbutton(self.framePiloto, variable=self.marcaVoltaRapida)
        self.checkVoltaRapida.pack(side="left")

        self.labelAbandonou = tk.Label(self.framePiloto, text="Abandonou: ")
        self.labelAbandonou.pack(side="left")
        self.marcaAbandonou = tk.IntVar()
        self.checkAbandonou = tk.Checkbutton(self.framePiloto, variable=self.marcaAbandonou)
        self.checkAbandonou.pack(side="left")

        self.labelDesclassificado = tk.Label(self.framePiloto, text="Desclassificado: ")
        self.labelDesclassificado.pack(side="left")
        self.marcaDesclassificado = tk.IntVar()
        self.checkDesclassificado = tk.Checkbutton(self.framePiloto, variable=self.marcaDesclassificado)
        self.checkDesclassificado.pack(side="left")


        # Botões
        self.buttonPiloto = tk.Button(self.framePiloto, text="Cadastrar resultado do piloto", font=('negrito', 9))
        self.buttonPiloto.pack(side="left")
        self.buttonPiloto.bind("<Button>", controle.cadastrarPiloto)

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
        self.GP = self.cadastra()

        if self.GP == None:
            return
        
        self.limiteSprint = LimiteCadastraSprint(self)

    def cadastrarCorrida(self, event):
        self.GP = self.cadastra()

        if self.GP == None:
            return
        
        self.limiteCorrida = LimiteCadastraCorrida(self)

    def cadastra(self):
        nome = self.limiteGP.inputGP.get()
        pista = self.limiteGP.escolhaPista.get()
        data = f"{self.limiteGP.escolhaDia.get()}/{self.limiteGP.escolhaMes.get()}/{self.limiteGP.escolhaAno.get()}"    #Concatena a data em uma string

        for gp in self.listaGPs:
            if gp.dataInicio.strftime('%d/%m/%Y') == data:  #Verifica se já existe um GP na data escolhida
                return gp
        
        #Se não houver, cria um novo
        for pst in self.ctrlPrincipal.ctrlPista.listaPistas:
            if pst.nome == pista:
                pista = pst
                break
                
        try:
            GP = model.GP(nome, pista, data)
            return GP
        except ValueError as error:
            self.limiteGP.mostraJanela('Erro', str(error))

    def cancelaHandler(self, event):
        self.limiteGP.destroy()

    def concluiHandler(self, event):
        self.listaGPs.append(self.GP)
        self.limiteGP.mostraJanela('Sucesso', 'GP cadastrado com sucesso')

    def consultarGP(self):
        pass

    def cadastrarPiloto(self, event):
        pass

    def salvaGPs(self):
        if len(self.listaGPs) != 0:
            with open("Cadastros/GPs.pickle", "wb") as f:
                pickle.dump(self.listaGPs, f)