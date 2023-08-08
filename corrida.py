import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle
    
class CtrlCorrida:
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaCorridas = []