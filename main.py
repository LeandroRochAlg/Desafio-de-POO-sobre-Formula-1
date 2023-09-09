import tkinter as tk
from Menu import GP, equipe, piloto, pista, tabela

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('350x300')
        self.root.title("Fórmula 1")
    
        self.menubar = tk.Menu(self.root)   #Cria a barra de menus

        #Cria os menus
        self.equipeMenu = tk.Menu(self.menubar)
        self.pilotoMenu = tk.Menu(self.menubar)
        self.pistaMenu = tk.Menu(self.menubar)
        self.GpMenu = tk.Menu(self.menubar)
        self.tabelaMenu = tk.Menu(self.menubar)
        self.salvaMenu = tk.Menu(self.menubar)

        #Adiciona os botões dos menus
        self.equipeMenu.add_command(label="Cadastrar", command=self.controle.cadastrarEquipe)
        self.equipeMenu.add_command(label="Listar", command=self.controle.listarEquipes)
        self.equipeMenu.add_command(label="Alterar equipe", command=self.controle.alterarEquipe)

        self.pilotoMenu.add_command(label="Cadastrar", command=self.controle.cadastrarPiloto)
        self.pilotoMenu.add_command(label="Listar", command=self.controle.listarPilotos)

        self.pistaMenu.add_command(label="Cadastrar", command=self.controle.cadastrarPista)
        self.pistaMenu.add_command(label="Listar", command=self.controle.listarPistas)

        self.GpMenu.add_command(label="Cadastrar", command=self.controle.cadastrarGP)
        self.GpMenu.add_command(label="Buscar", command=self.controle.consultarGP)

        self.tabelaMenu.add_command(label="Pilotos", command=self.controle.exibirTabelaPilotos)
        self.tabelaMenu.add_command(label="Construtores", command=self.controle.exibirTabelaConstrutores)

        self.salvaMenu.add_command(label='Salvar e sair', command=self.controle.salva)

        #Adiciona os menus a barra de menus
        self.menubar.add_cascade(label="Equipe", menu=self.equipeMenu)
        self.menubar.add_cascade(label="Piloto", menu=self.pilotoMenu)
        self.menubar.add_cascade(label="Pista", menu=self.pistaMenu)
        self.menubar.add_cascade(label="Grande Prêmio", menu=self.GpMenu)
        self.menubar.add_cascade(label="Tabelas", menu=self.tabelaMenu)
        self.menubar.add_cascade(label="Sair", menu=self.salvaMenu)

        #Adiciona a barra de menus a janela principal
        self.root.config(menu=self.menubar)

class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlEquipe = equipe.CtrlEquipe(self)
        self.ctrlPiloto = piloto.CtrlPiloto(self)
        self.ctrlPista = pista.CtrlPista(self)
        self.ctrlGP = GP.CtrlGP(self)
        self.ctrlTabela = tabela.CtrlTabela(self)

        self.limite = LimitePrincipal(self.root, self)  #Passa a janela principal e o controle para a classe LimitePrincipal

        self.root.mainloop()

    #Métodos para chamar os métodos de cada classe de controle
    def cadastrarEquipe(self):
        self.ctrlEquipe.cadastrarEquipe()

    def listarEquipes(self):
        self.ctrlEquipe.listarEquipes()

    def alterarEquipe(self):
        self.ctrlEquipe.alterarEquipe()
    
    def cadastrarPiloto(self):
        self.ctrlPiloto.cadastrarPiloto()

    def listarPilotos(self):
        self.ctrlPiloto.listarPilotos()

    def cadastrarPista(self):
        self.ctrlPista.cadastrarPista()

    def listarPistas(self):
        self.ctrlPista.listarPistas()

    def cadastrarGP(self):
        self.ctrlGP.cadastrarGP()

    def consultarGP(self):
        self.ctrlGP.consultarGP()

    def exibirTabelaPilotos(self):
        self.ctrlTabela.exibirTabelaPilotos()

    def exibirTabelaConstrutores(self):
        self.ctrlTabela.exibirTabelaConstrutores()

    def salva(self):
        self.ctrlEquipe.salvaEquipes()
        self.ctrlPiloto.salvaPilotos()
        self.ctrlPista.salvaPistas()
        self.ctrlGP.salvaGPs()
        self.root.destroy()

if __name__ == '__main__':
    c = ControlePrincipal()