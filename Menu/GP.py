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
    def __init__(self, controle, nomeGP):
        tk.Toplevel.__init__(self)
        self.geometry('800x400')
        self.title(f"Sprint - {nomeGP}")
        self.controle = controle

        self.framePiloto = tk.Frame(self)
        self.frameHorario = tk.Frame(self)
        self.frameVoltas = tk.Frame(self)
        self.frameButton = tk.Frame(self)           #Frame para os botões

        self.framePiloto.pack()
        self.frameHorario.pack()
        self.frameVoltas.pack()
        self.frameButton.pack()

        #Cadastro de resultado de pilotos
        self.labelPiloto = tk.Label(self.framePiloto, text="Número do piloto: ")
        self.labelPiloto.pack(side="left")
        self.inputPiloto = tk.Entry(self.framePiloto, width=5)
        self.inputPiloto.pack(side="left")
        self.inputPosicao = tk.Label(self.framePiloto, text="Posição: ")
        self.inputPosicao.pack(side="left")
        self.inputPosicao = tk.Entry(self.framePiloto, width=5)
        self.inputPosicao.pack(side="left")

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

        #Informações da corrida
        #Horário de largada
        self.labelData = tk.Label(self.frameHorario, text="Horário de início da corrida: ")
        self.labelData.pack(side="top")
        # Combobox para escolher a hora
        self.labelHora = tk.Label(self.frameHorario, text="Hora: ")
        self.labelHora.pack(side="left")
        self.escolhaHora = tk.IntVar()
        self.comboHora = ttk.Combobox(self.frameHorario, width=3, textvariable=self.escolhaHora, values=list(range(1, 24)))
        self.comboHora.pack(side="left")
        # Combobox para escolher os minutos
        self.labelMinuto = tk.Label(self.frameHorario, text="Minuto: ")
        self.labelMinuto.pack(side="left")
        self.escolhaMinuto = tk.IntVar()
        self.comboMinuto = ttk.Combobox(self.frameHorario, width=3, textvariable=self.escolhaMinuto, values=list(range(1, 60)))
        self.comboMinuto.pack(side="left")

        #Número de voltas
        self.labelVoltas = tk.Label(self.frameVoltas, text="Número de voltas: ")
        self.labelVoltas.pack(side="left")
        self.inputVoltas = tk.Entry(self.frameVoltas, width=5)
        self.inputVoltas.pack(side="left")

        # Botões
        self.buttonPiloto = tk.Button(self.framePiloto, text="Cadastrar resultado do piloto", font=('negrito', 9))
        self.buttonPiloto.pack(side="left")
        self.buttonPiloto.bind("<Button>", controle.cadastrarPiloto)

        self.buttonCancela = tk.Button(self.frameButton, text="Cancelar", font=('negrito', 9))
        self.buttonCancela.pack(side="left")
        self.buttonCancela.bind("<Button>", controle.cancelaCorridaHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído", font=('negrito', 9))
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.concluiSprintHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteCadastraCorrida(tk.Toplevel):
    def __init__(self, controle, nomeGP):
        tk.Toplevel.__init__(self)
        self.geometry('800x400')
        self.title(f"Corrida - {nomeGP}")
        self.controle = controle

        self.framePiloto = tk.Frame(self)
        self.frameHorario = tk.Frame(self)
        self.frameVoltas = tk.Frame(self)
        self.frameButton = tk.Frame(self)           #Frame para os botões

        self.framePiloto.pack()
        self.frameHorario.pack()
        self.frameVoltas.pack()
        self.frameButton.pack()

        #Cadastro de resultado de pilotos
        self.labelPiloto = tk.Label(self.framePiloto, text="Número do piloto: ")
        self.labelPiloto.pack(side="left")
        self.inputPiloto = tk.Entry(self.framePiloto, width=5)
        self.inputPiloto.pack(side="left")
        self.inputPosicao = tk.Label(self.framePiloto, text="Posição: ")
        self.inputPosicao.pack(side="left")
        self.inputPosicao = tk.Entry(self.framePiloto, width=5)
        self.inputPosicao.pack(side="left")

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

        #Informações da corrida
        #Horário de largada
        self.labelData = tk.Label(self.frameHorario, text="Horário de início da corrida: ")
        self.labelData.pack(side="top")
        # Combobox para escolher a hora
        self.labelHora = tk.Label(self.frameHorario, text="Hora: ")
        self.labelHora.pack(side="left")
        self.escolhaHora = tk.IntVar()
        self.comboHora = ttk.Combobox(self.frameHorario, width=3, textvariable=self.escolhaHora, values=list(range(1, 24)))
        self.comboHora.pack(side="left")
        # Combobox para escolher os minutos
        self.labelMinuto = tk.Label(self.frameHorario, text="Minuto: ")
        self.labelMinuto.pack(side="left")
        self.escolhaMinuto = tk.IntVar()
        self.comboMinuto = ttk.Combobox(self.frameHorario, width=3, textvariable=self.escolhaMinuto, values=list(range(1, 60)))
        self.comboMinuto.pack(side="left")

        #Número de voltas
        self.labelVoltas = tk.Label(self.frameVoltas, text="Número de voltas: ")
        self.labelVoltas.pack(side="left")
        self.inputVoltas = tk.Entry(self.frameVoltas, width=5)
        self.inputVoltas.pack(side="left")
        #A corrida conta 100% dos pontos
        self.labelPontos = tk.Label(self.frameVoltas, text="A corrida foi completa: ")
        self.labelPontos.pack(side="left")
        self.marcaPontos = tk.IntVar()
        self.checkPontos = tk.Checkbutton(self.frameVoltas, variable=self.marcaPontos)
        self.checkPontos.pack(side="left")

        # Botões
        self.buttonPiloto = tk.Button(self.framePiloto, text="Cadastrar resultado do piloto", font=('negrito', 9))
        self.buttonPiloto.pack(side="left")
        self.buttonPiloto.bind("<Button>", controle.cadastrarPiloto)

        self.buttonCancela = tk.Button(self.frameButton, text="Cancelar", font=('negrito', 9))
        self.buttonCancela.pack(side="left")
        self.buttonCancela.bind("<Button>", controle.cancelaCorridaHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído", font=('negrito', 9))
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.concluiCorridaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaGP(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('600x600')
        self.title("Buscar GP")
        self.controle = controle

        self.frameGP = tk.Frame(self)
        self.frameInfo = tk.Frame(self)

        self.frameGP.pack()
        self.frameInfo.pack()

        self.labelGP = tk.Label(self.frameGP, text="Info do GP: ")
        self.labelGP.pack(side="left")
        self.inputGP = tk.Entry(self.frameGP, width=30)
        self.inputGP.pack(side="left")

        self.infoGP = tk.Text(self.frameInfo, width=40, height=30, wrap='word')
        self.infoGP.pack(side="left")

        # Botões
        self.buttonSubmit = tk.Button(self.frameGP, text="Enter", font=('negrito', 9))
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

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

        self.resultadosCorrida = []

        self.limiteGP = LimiteCriaGP(self, pistas)

    def cadastrarSprint(self, event):
        self.GP = self.cadastra()

        if self.GP == None:
            return
        
        self.tipoCorrida = 'Sprint'
        
        self.limiteCorrida = LimiteCadastraSprint(self, self.GP.nome)

    def cadastrarCorrida(self, event):
        self.GP = self.cadastra()

        if self.GP == None:
            return
        
        self.tipoCorrida = 'Corrida'

        self.limiteCorrida = LimiteCadastraCorrida(self, self.GP.nome)

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
            self.listaGPs.append(GP)
            return GP
        except ValueError as error:
            self.limiteGP.mostraJanela('Erro', str(error))

    def cancelaHandler(self, event):
        self.limiteGP.destroy()

    def concluiHandler(self, event):
        self.listaGPs.append(self.GP)
        self.limiteGP.mostraJanela('Sucesso', 'GP cadastrado com sucesso')

    def consultarGP(self):
        self.limiteConsulta = LimiteConsultaGP(self)

    def cadastrarPiloto(self, event):
        Piloto = None

        for piloto in self.ctrlPrincipal.ctrlPiloto.listaPilotos:
            if piloto.numero == int(self.limiteCorrida.inputPiloto.get()):
                Piloto = piloto
                break
        
        if Piloto in self.resultadosCorrida:  #Verifica se o piloto já foi registrado
            self.limiteCorrida.mostraJanela('Erro', 'Esse piloto já foi registrado')
            return
        elif self.limiteCorrida.marcaVoltaRapida.get():
            for resultado in self.resultadosCorrida:
                if resultado.voltaRapida:
                    self.limiteCorrida.mostraJanela('Erro', 'Já existe uma volta mais rápida registrada')
                    return

        if self.limiteCorrida.marcaDesclassificado.get():
            posicao = 3000
        elif self.limiteCorrida.marcaAbandonou.get():
            posicao = 1000
        else:
            posicao = int(self.limiteCorrida.inputPosicao.get())

        try:
            Resultado = model.Resultado(Piloto, posicao, self.limiteCorrida.marcaVoltaRapida.get())
        except ValueError as error:
            self.limiteCorrida.mostraJanela('Erro', str(error))
            return

        #Finalizações
        self.resultadosCorrida.append(Resultado)
        self.limiteCorrida.mostraJanela('Sucesso', 'Resultado do piloto cadastrado com sucesso')

        #Limpa os campos
        self.limiteCorrida.inputPiloto.delete(0, len(self.limiteCorrida.inputPiloto.get()))
        self.limiteCorrida.inputPosicao.delete(0, len(self.limiteCorrida.inputPosicao.get()))
        self.limiteCorrida.marcaAbandonou.set(0)
        self.limiteCorrida.marcaDesclassificado.set(0)
        self.limiteCorrida.marcaVoltaRapida.set(0)

    def concluiCorridaHandler(self, event):
        hora = f"{self.limiteCorrida.escolhaHora.get()}:{self.limiteCorrida.escolhaMes.get()}"  #Concatena a hora em uma string
        voltas = int(self.limiteCorrida.inputVoltas.get())

        for piloto in self.ctrlPrincipal.ctrlPiloto.listaPilotos:
            if piloto not in self.resultadosCorrida:
                Resultado = model.Resultado(piloto, 2000, False)    #Os pilotos não registrados não largaram
                self.resultadosCorrida.append(Resultado)

        try:
            self.GP.Corrida = model.Corrida(hora, voltas, self.resultadosCorrida)
            self.limiteCorrida.mostraJanela('Sucesso', 'Corrida cadastrada com sucesso')

            if self.tipoCorrida == 'Corrida':
                self.atribuiPontosCorrida(self.GP.Corrida)
            elif self.tipoCorrida == 'Sprint':
                self.atribuiPontosSprint(self.GP.Corrida)
            else:
                raise ValueError('Desculpe, ocorreu um erro inesperado')
            
            self.limiteCorrida.destroy()
        except ValueError as error:
            self.limiteCorrida.mostraJanela('Erro', str(error))
            return
        
    def concluiSprintHandler(self, event):
        #Dicinário com os pontos padrão da Sprint
        if self.GP.dataInicio.year == 2021: #É necessário checar se existia Sprint e os pontos atribuídos a ela
            pontosPadrao = {
                1: 3,
                2: 2,
                3: 1
            }
        elif self.GP.dataInicio.year >= 2022:
            pontosPadrao = {
                1: 8,
                2: 7,
                3: 6,
                4: 5,
                5: 4,
                6: 3,
                7: 2,
                8: 1
            }
        else:
            raise ValueError('Não existia corrida Sprint antes de 2021')
        
        if self.limiteCorrida.marcaPontos.get():    #Se a corrida foi completa, todos os pilotos recebem 100% dos pontos
            multiplicador = 1
        else:   #Se não, apenas 50% dos pontos são atribuidos
            multiplicador = 0.5

        for resultado in self.GP.Corrida.resultados:
            if resultado.posicao in pontosPadrao.keys():
                pontos = pontosPadrao[resultado.posicao] * multiplicador

                resultado.Piloto.adicionaPontos(pontos)
                resultado.Piloto.Equipe.adicionaPontos(pontos)
        
    def atribuiPontosCorrida(self, Corrida):
        #Dicionário com a pontuação padrão
        pontosPadrao = {
            1: 25,
            2: 18,
            3: 15,
            4: 12,
            5: 10,
            6: 8,
            7: 6,
            8: 4,
            9: 2,
            10: 1
        }

        if self.limiteCorrida.marcaPontos.get():    #Se a corrida foi completa, todos os pilotos recebem 100% dos pontos
            multiplicador = 1
        else:   #Se não, apenas 50% dos pontos são atribuidos
            multiplicador = 0.5

        for resultado in Corrida.resultados:
            if resultado.posicao in pontosPadrao.keys():  #Verifica se o piloto terminou a corrida
                pontos = pontosPadrao[resultado.posicao] * multiplicador    #Multiplica a pontuação pelo multiplicador

                if resultado.voltaRapida:   #Apenas se o piloto terminou a corrida a volta rápida é contabilizada
                    pontos += 1

                resultado.Piloto.adicionaPontos(pontos)   #Adiciona os pontos ao piloto
                resultado.Piloto.Equipe.adicionaPontos(pontos)   #Adiciona os pontos à equipe do piloto

    def cancelaCorridaHandler(self, event):
        self.limiteCorrida.destroy()

    def salvaGPs(self):
        if len(self.listaGPs) != 0:
            with open("Cadastros/GPs.pickle", "wb") as f:
                pickle.dump(self.listaGPs, f)

    def cancelaBuscaHandler(self, event):
        self.limiteConsulta.destroy()

    def enterHandler(self, event):
        busca = self.limiteConsulta.inputGP.get()
        resultado = ''
        encontrado = False

        for gp in self.listaGPs:
            if gp.nome == busca or gp.pista.nome == busca or gp.pista.pais == busca or gp.pista.cidade == busca or gp.dataInicio.strftime('%d/%m/%Y') == busca:
                resultado += str(gp) + '\n\n'
                encontrado = True
        
        if encontrado:
            self.limiteConsulta.infoGP.delete('1.0', 'end')
            self.limiteConsulta.infoGP.insert('end', resultado)
        else:
            self.limiteConsulta.infoGP.delete('1.0', 'end')
            self.limiteConsulta.infoGP.insert('end', 'GP não encontrado')