import tkinter as tk
import PySimpleGUI as sg

layout = [
    [sg.Text("SimpleUI.py")],
    [sg.Button("OK")]
]
#Create the window
window = sg.Window ("Demo",layout, margins=(100,50))
#create an event loop
while True:
    event, values = window.read()
    #end program if user close window or press OK
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close
