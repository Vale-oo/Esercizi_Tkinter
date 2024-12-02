import tkinter as tk
from interfacciaCalcolatrice import *
#Stampa risultato
def stampa_Uguale(risultato):

    text_output1= tk.Label (window, text="BBBBBB", fg="white", font=("Helvetica", 16), background="#ffffff")
    text_output1.grid (row=5, column=1, columnspan=4, sticky="W")

    text_output= tk.Label (window, text=risultato, fg="#ff0000", font=("Helvetica", 16), background="#ffffff")
    text_output.grid (row=5, column=1, columnspan=4, sticky="W")


def Somma():
    
    risultato = int(num1.get()) + int(num2.get())
    stampa_Uguale(risultato)

def Sottrazione():

    risultato = int(num1.get()) - int(num2.get())
    stampa_Uguale(risultato)

def Moltiplicazione():

    risultato = int(num1.get()) * int(num2.get())
    stampa_Uguale(risultato)

def Divisione():

    risultato = int(num1.get()) / int(num2.get())
    stampa_Uguale(risultato)