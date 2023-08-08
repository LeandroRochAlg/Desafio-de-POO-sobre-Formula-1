import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle

class CtrlPiloto:
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaPilotos = []

        if not os.path.isfile("pilotos.pickle"):
            self.listaPilotos = []
        else:
            with open("pilotos.pickle", "rb") as f:
                self.listaPilotos = pickle.load(f)