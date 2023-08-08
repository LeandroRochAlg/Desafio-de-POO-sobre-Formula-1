import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle

class CtrlPista:
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaPistas = []

        if not os.path.isfile("pistas.pickle"):
            self.listaPistas = []
        else:
            with open("pistas.pickle", "rb") as f:
                self.listaPistas = pickle.load(f)