import tkinter as tk
from Menu import equipe as eq, piloto as plt, pista as pst, corrida as cr

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x300')
    
        self.menubar = tk.Menu(self.root)   #Cria a barra de menus

        #Cria os menus
        self.equipeMenu = tk.Menu(self.menubar)
        self.pilotoMenu = tk.Menu(self.menubar)
        self.pistaMenu = tk.Menu(self.menubar)
        self.corridaMenu = tk.Menu(self.menubar)
        self.salvaMenu = tk.Menu(self.menubar)

        #Adiciona os botões dos menus
        self.equipeMenu.add_command(label="Cadastrar", command=self.controle.cadastrarEquipe)
        self.equipeMenu.add_command(label="Listar", command=self.controle.listarEquipes)

        self.pilotoMenu.add_command(label="Cadastrar", command=self.controle.cadastrarPiloto)
        self.pilotoMenu.add_command(label="Listar", command=self.controle.listarPilotos)

        self.pistaMenu.add_command(label="Cadastrar", command=self.controle.cadastrarPista)
        self.pistaMenu.add_command(label="Listar", command=self.controle.listarPistas)

        self.corridaMenu.add_command(label="Cadastrar", command=self.controle.cadastrarCorrida)
        self.corridaMenu.add_command(label="Pesquisar", command=self.controle.listarCorridas)

        self.salvaMenu.add_command(label='Salvar e sair', command=self.controle.salvaJogos)

        #Adiciona os menus a barra de menus
        self.menubar.add_cascade(label="Equipe", menu=self.equipeMenu)
        self.menubar.add_cascade(label="Piloto", menu=self.pilotoMenu)
        self.menubar.add_cascade(label="Pista", menu=self.pistaMenu)
        self.menubar.add_cascade(label="Corrida", menu=self.corridaMenu)
        self.menubar.add_cascade(label="Sair", menu=self.salvaMenu)

        #Adiciona a barra de menus a janela principal
        self.root.config(menu=self.menubar)

class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlEquipe = eq.CtrlEquipe(self)
        self.ctrlPiloto = plt.CtrlPiloto(self)
        self.ctrlPista = pst.CtrlPista(self)
        self.ctrlCorrida = cr.CtrlCorrida(self)

        self.limite = LimitePrincipal(self.root, self)  #Passa a janela principal e o controle para a classe LimitePrincipal

        self.root.mainloop()

    #Métodos para chamar os métodos de cada classe de controle
    def cadastrarEquipe(self):
        self.ctrlEquipe.cadastrarEquipe()

    def listarEquipes(self):
        self.ctrlEquipe.listarEquipes()
    
    def cadastrarPiloto(self):
        self.ctrlPiloto.cadastrarPiloto()

    def listarPilotos(self):
        self.ctrlPiloto.listarPilotos()

    def cadastrarPista(self):
        self.ctrlPista.cadastrarPista()

    def listarPistas(self):
        self.ctrlPista.listarPistas()

    def cadastrarCorrida(self):
        self.ctrlCorrida.cadastrarCorrida()

    def listarCorridas(self):
        self.ctrlCorrida.listarCorridas()

    def salvaJogos(self):
        self.ctrlEquipe.salvaEquipes()
        self.ctrlPiloto.salvaPilotos()
        self.ctrlPista.salvaPistas()
        '''self.ctrlCorrida.salvaCorridas()'''
        self.root.destroy()

if __name__ == '__main__':
    c = ControlePrincipal()