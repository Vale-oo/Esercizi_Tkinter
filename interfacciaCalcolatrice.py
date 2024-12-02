import tkinter as tk
#from operazioni import *

window = tk.Tk() # all'interno di tkinker c'è una classe Tk che costruisce la finestra
window.title("Esercizio Calcolatrice") # title è una funzione che scrive un titolo in modo da presentarlo all'utente
window.geometry("600x600") # geometry dà la dimensione alla finestra dell'interfaccia ( in questo caso è un quadrato)
window.resizable(False, False) # resizable permette o non permette di ridimensionare l'interfaccia 'window' creata, mettendo True o False, per quante non si restringe in questo caso
window.configure(background = "lightgrey") # configura in questo caso lo sfondo e il suo colore

#Operazioni e stampa
def stampa_Uguale(risultato):
    text_output2= tk.Label (window, text="BBBBBB", fg="lightgrey", font=("Helvetica", 16), background="lightgrey")
    text_output2.grid (row=6, column=0, columnspan=4, sticky="W")

    text_output1= tk.Label (window, text="BBBBBBBBBBBBBBBBBBBBBB", fg="lightgrey", font=("Helvetica", 16), background="lightgrey")
    text_output1.grid (row=7, column=0, columnspan=4, sticky="W")

    text_output= tk.Label (window, text=risultato, fg="black", font=("Helvetica", 14), background="lightgrey")
    text_output.grid (row=7, column=0, columnspan=4, sticky="W")

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

    if float(num1.get()) > float(num2.get()):
        risultato = float(num1.get()) / float(num2.get())
    elif float(num1.get()) < float(num2.get()):
        risultato = "Errore, dammi altri numeri"
    elif float(num1.get()) == float(num2.get()):
        risultato = float(num1.get()) / float(num2.get())
    
    stampa_Uguale(risultato)


#Etichette
etichetta = tk.Label( window, text ="Calcolatrice", fg="black", font=("Helvetica", 20 ), background="lightgrey" )
etichetta.grid(row=0, column=1, sticky="W", padx=10, pady=20) 

etichetta = tk.Label( window, text ="Scrivi i numeri che vuoi operare nelle caselle sottostanti:", fg="black", font=("Helvetica", 16 ), background="lightgrey" )
etichetta.grid(row=1, column=0,  columnspan=10, sticky="W", padx=10, pady=20) 

etichettaNum1 = tk.Label( window, text ="Numero 1: ", fg="black", font=("Helvetica", 14 ), background="lightgrey" )
etichettaNum1.grid(row=2, column=0, sticky="W", padx=10, pady=20) 

etichettaNum2 = tk.Label( window, text ="Numero 2:", fg="black", font=("Helvetica", 14 ), background="lightgrey" )
etichettaNum2.grid(row=3, column=0,  columnspan=10, sticky="W", padx=10, pady=20) 

 #Casella Input
num1 = tk.Entry(window)
num1.grid( row = 2, column = 1 , sticky = "W" )

num2 = tk.Entry(window)
num2.grid( row = 3, column = 1 , sticky = "W" )


#Pulsante di scelta
first_button = tk.Button(text = "+", command = Somma ) #Somma(window, num1, num2)
first_button.grid(row = 2 , column = 2 , sticky="W" )

second_button = tk.Button(text = "-", command = Sottrazione ) #Sottrazione(window, num1, num2)
second_button.grid(row = 3, column = 2 , sticky="W" )

third_button = tk.Button(text = "x", command = Moltiplicazione) #Moltiplicazione(window, num1, num2)
third_button.grid(row = 2, column = 3 , sticky="W" )

fourth_button = tk.Button(text = " /", command = Divisione ) #"""Divisione(window, num1, num2)""" )
fourth_button.grid(row = 3 , column = 3 , sticky="W" )

if __name__ == "__main__":
    window.mainloop() # questo permette di mantenere l'interfaccia attiva sul monitor

