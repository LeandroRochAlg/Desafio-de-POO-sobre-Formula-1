import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle
import model
    
class CtrlCorrida:
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaCorridas = []

        if not os.path.isfile("Cadastros/corridas.pickle"):
            self.listaCorridas = []
        else:
            with open("Cadastros/corridas.pickle", "rb") as f:
                self.listaCorridas = pickle.load(f)