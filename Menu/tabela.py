import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import model

class CompetidorTabela: #Classe auxiliar para a tabela de pilotos
    def __init__(self, Competidor):
        self.__Competidor = Competidor
        self.vitorias = 0
        self.segundos = 0
        self.terceiros = 0
        self.voltasRapidas = 0
        self.sprints = 0

    @property
    def Competidor(self):
        return self.__Competidor
    
    @property
    def vitorias(self):
        return self.__vitorias
    
    @vitorias.setter
    def vitorias(self, vitorias):
        self.__vitorias = vitorias
    
    @property
    def segundos(self):
        return self.__segundos
    
    @segundos.setter
    def segundos(self, segundos):
        self.__segundos = segundos
    
    @property
    def terceiros(self):
        return self.__terceiros
    
    @terceiros.setter
    def terceiros(self, terceiros):
        self.__terceiros = terceiros

    @property
    def voltasRapidas(self):
        return self.__voltasRapidas
    
    @voltasRapidas.setter
    def voltasRapidas(self, voltasRapidas):
        self.__voltasRapidas = voltasRapidas

    @property
    def sprints(self):
        return self.__sprints
    
    @sprints.setter
    def sprints(self, sprints):
        self.__sprints = sprints

class LimiteTabelaPilotos(tk.Toplevel):
    def __init__(self, controle, listaPilotos):
        tk.Toplevel.__init__(self)
        self.geometry('900x300')
        self.title('Tabela de Pilotos')
        self.controle = controle

        self.frameTabela = tk.Frame(self, pady=10)
        self.frameTabela.pack()

        self.frameButton = tk.Frame(self)
        self.frameButton.pack()

        #Cria a tabela
        self.tabela = ttk.Treeview(self.frameTabela, columns=('pos', 'nome', 'pais', 'equipe', 'pontos', 'vitorias', 'segundos', 'terceiros', 'voltasRapidas', 'sprints'), show='headings')
        self.tabela.column('pos', minwidth=0, width=30)
        self.tabela.column('nome', minwidth=0, width=100)
        self.tabela.column('pais', minwidth=0, width=100)
        self.tabela.column('equipe', minwidth=0, width=100)
        self.tabela.column('pontos', minwidth=0, width=50)
        self.tabela.column('vitorias', minwidth=0, width=50)
        self.tabela.column('segundos', minwidth=0, width=50)
        self.tabela.column('terceiros', minwidth=0, width=50)
        self.tabela.column('voltasRapidas', minwidth=0, width=150)
        self.tabela.column('sprints', minwidth=0, width=150)

        self.tabela.heading('pos', text='Pos')
        self.tabela.heading('nome', text='Nome')
        self.tabela.heading('pais', text='País')
        self.tabela.heading('equipe', text='Equipe')
        self.tabela.heading('pontos', text='Pontos')
        self.tabela.heading('vitorias', text='Vitórias')
        self.tabela.heading('segundos', text='2ºs')
        self.tabela.heading('terceiros', text='3ºs')
        self.tabela.heading('voltasRapidas', text='Voltas mais rápidas')
        self.tabela.heading('sprints', text='Sprints vencidas')

        self.tabela.pack()

        #Preenche a tabela
        for i in range(len(listaPilotos)):
            self.tabela.insert('', 'end', values=(i+1, listaPilotos[i].Competidor.nome, listaPilotos[i].Competidor.pais, listaPilotos[i].Competidor.Equipe.nome, listaPilotos[i].Competidor.pontos, listaPilotos[i].vitorias, listaPilotos[i].segundos, listaPilotos[i].terceiros, listaPilotos[i].voltasRapidas, listaPilotos[i].sprints))

        #Botão
        self.buttonFecha = tk.Button(self.frameButton, text="Concluído", font=('negrito', 9))
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

class LimiteTabelaConstrutores(tk.Toplevel):
    def __init__(self, controle, listaConstrutores):
        tk.Toplevel.__init__(self)
        self.geometry('900x300')
        self.title('Tabela de Construtores')
        self.controle = controle

        self.frameTabela = tk.Frame(self, pady=10)
        self.frameTabela.pack()

        self.frameButton = tk.Frame(self)
        self.frameButton.pack()

        #Cria a tabela
        self.tabela = ttk.Treeview(self.frameTabela, columns=('pos', 'nome', 'pais', 'pontos', 'vitorias', 'segundos', 'terceiros', 'voltasRapidas', 'sprints'), show='headings')
        self.tabela.column('pos', minwidth=0, width=30)
        self.tabela.column('nome', minwidth=0, width=100)
        self.tabela.column('pais', minwidth=0, width=150)
        self.tabela.column('pontos', minwidth=0, width=50)
        self.tabela.column('vitorias', minwidth=0, width=50)
        self.tabela.column('segundos', minwidth=0, width=50)
        self.tabela.column('terceiros', minwidth=0, width=50)
        self.tabela.column('voltasRapidas', minwidth=0, width=150)
        self.tabela.column('sprints', minwidth=0, width=150)

        self.tabela.heading('pos', text='Pos')
        self.tabela.heading('nome', text='Nome')
        self.tabela.heading('pais', text='País')
        self.tabela.heading('pontos', text='Pontos')
        self.tabela.heading('vitorias', text='Vitórias')
        self.tabela.heading('segundos', text='2ºs')
        self.tabela.heading('terceiros', text='3ºs')
        self.tabela.heading('voltasRapidas', text='Voltas mais rápidas')
        self.tabela.heading('sprints', text='Sprints vencidas')

        self.tabela.pack()

        #Preenche a tabela
        for i in range(len(listaConstrutores)):
            self.tabela.insert('', 'end', values=(i+1, listaConstrutores[i].Competidor.nome, listaConstrutores[i].Competidor.pais, listaConstrutores[i].Competidor.pontos, listaConstrutores[i].vitorias, listaConstrutores[i].segundos, listaConstrutores[i].terceiros, listaConstrutores[i].voltasRapidas, listaConstrutores[i].sprints))

        #Botão
        self.buttonFecha = tk.Button(self.frameButton, text="Concluído", font=('negrito', 9))
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)
class CtrlTabela:
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal

    def exibirTabelaPilotos(self):
        listaPilotos = self.ctrlPrincipal.ctrlPiloto.getListaPilotos()

        if len(listaPilotos) == 0:
            messagebox.showinfo(title="Alerta", message="Não há pilotos cadastrados")
            return

        #Cria uma lista de objetos CompetidorTabela
        listaPilotosTabela = []
        for piloto in listaPilotos:
            listaPilotosTabela.append(CompetidorTabela(piloto))

        #Preenche a lista de objetos CompetidorTabela com as informações de cada piloto
        for gp in self.ctrlPrincipal.ctrlGP.getListaGPs():
            if gp.Corrida != None:
                for resultado in gp.Corrida.resultados:
                    if resultado.posicao == 1:
                        for piloto in listaPilotosTabela:
                            if piloto.Competidor.numero == resultado.Piloto.numero:
                                piloto.vitorias += 1
                    elif resultado.posicao == 2:
                        for piloto in listaPilotosTabela:
                            if piloto.Competidor.numero == resultado.Piloto.numero:
                                piloto.segundos += 1
                    elif resultado.posicao == 3:
                        for piloto in listaPilotosTabela:
                            if piloto.Competidor.numero == resultado.Piloto.numero:
                                piloto.terceiros += 1

                    if resultado.voltaRapida:
                        for piloto in listaPilotosTabela:
                            if piloto.Competidor.numero == resultado.Piloto.numero:
                                piloto.voltasRapidas += 1
            if gp.Sprint != None:
                for resultado in gp.Sprint.resultados:
                    if resultado.posicao == 1:
                        for piloto in listaPilotosTabela:
                            if piloto.Competidor.numero == resultado.Piloto.numero:
                                piloto.sprints += 1

        #Ordena a lista de objetos CompetidorTabela
        listaPilotosTabela.sort(key=lambda x: x.Competidor.pontos, reverse=True)

        #Checa e ordena possíveis empates em pontos
        for i in range(len(listaPilotosTabela)):
            if i+1 < len(listaPilotosTabela):
                if listaPilotosTabela[i].Competidor.pontos == listaPilotosTabela[i+1].Competidor.pontos:
                    listaPilotosTabela = self.ordenaEmpate(listaPilotosTabela, i, i+1)

        self.limiteTabela = LimiteTabelaPilotos(self, listaPilotosTabela)

    def exibirTabelaConstrutores(self):
        listaConstrutores = self.ctrlPrincipal.ctrlEquipe.getListaEquipes()

        if len(listaConstrutores) == 0:
            messagebox.showinfo(title="Alerta", message="Não há construtores cadastrados")
            return

        #Cria uma lista de objetos CompetidorTabela
        listaConstrutoresTabela = []
        for construtor in listaConstrutores:
            listaConstrutoresTabela.append(CompetidorTabela(construtor))

        #Preenche a lista de objetos CompetidorTabela com as informações de cada construtor
        for gp in self.ctrlPrincipal.ctrlGP.getListaGPs():
            if gp.Corrida != None:
                for resultado in gp.Corrida.resultados:
                    if resultado.posicao == 1:
                        for construtor in listaConstrutoresTabela:
                            if construtor.Competidor.nome == resultado.Piloto.Equipe.nome:
                                construtor.vitorias += 1
                    elif resultado.posicao == 2:
                        for construtor in listaConstrutoresTabela:
                            if construtor.Competidor.nome == resultado.Piloto.Equipe.nome:
                                construtor.segundos += 1
                    elif resultado.posicao == 3:
                        for construtor in listaConstrutoresTabela:
                            if construtor.Competidor.nome == resultado.Piloto.Equipe.nome:
                                construtor.terceiros += 1

                    if resultado.voltaRapida:
                        for construtor in listaConstrutoresTabela:
                            if construtor.Competidor.nome == resultado.Piloto.Equipe.nome:
                                construtor.voltasRapidas += 1
            if gp.Sprint != None:
                for resultado in gp.Sprint.resultados:
                    if resultado.posicao == 1:
                        for construtor in listaConstrutoresTabela:
                            if construtor.Competidor.nome == resultado.Piloto.Equipe.nome:
                                construtor.sprints += 1

        #Ordena a lista de objetos CompetidorTabela
        listaConstrutoresTabela.sort(key=lambda x: x.Competidor.pontos, reverse=True)

        #Checa e ordena possíveis empates em pontos
        for i in range(len(listaConstrutoresTabela)):
            if i+1 < len(listaConstrutoresTabela):
                if listaConstrutoresTabela[i].Competidor.pontos == listaConstrutoresTabela[i+1].Competidor.pontos:
                    listaConstrutoresTabela = self.ordenaEmpate(listaConstrutoresTabela, i, i+1)

        self.limiteTabela = LimiteTabelaConstrutores(self, listaConstrutoresTabela)

    def ordenaEmpate(self, lista, i, j):
        #Listas de números de resultados de cada piloto
        resultadosPlt1 = [0 for i in range(len(lista))]
        resultadosPlt2 = [0 for i in range(len(lista))]

        for gp in self.ctrlPrincipal.ctrlGP.getListaGPs():  #Conta os resultados de cada piloto
            if gp.Corrida != None:
                for resultado in gp.Corrida.resultados:
                    if resultado.Piloto == lista[i].Competidor and (resultado.posicao != 1000 and resultado.posicao != 2000 and resultado.posicao != 3000): #Não conta resultados de não terminou, não largou e desclassificado
                        resultadosPlt1[resultado.posicao - 1] += 1
                    elif resultado.Piloto == lista[j].Competidor and (resultado.posicao != 1000 and resultado.posicao != 2000 and resultado.posicao != 3000):
                        resultadosPlt2[resultado.posicao - 1] += 1

        k = 0

        while resultadosPlt1[k] == resultadosPlt2[k]:   #Varre até encontrar a diferença entre os resultados
            if k == len(resultadosPlt1) - 1:
                return lista

            k += 1

        if resultadosPlt1[k] < resultadosPlt2[k]:   #Troca os pilotos de posição caso o piloto 1 tenha o resultado pior
            lista[i], lista[j] = lista[j], lista[i]

        return lista
    
    def fechaHandler(self, event):
        self.limiteTabela.destroy()