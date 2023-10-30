import os
import subprocess
import PySimpleGUI as sg
import ctypes
import sys
import time
import re
import psutil


# GUI layout
exit_button_style = {
    'size': (7, 1),  # Rozmiar przycisku
    'font': ('Arial', 9),  # Rozmiar i rodzaj czcionki
    'button_color': ('white', 'red'),  # Kolor tła i kolor czcionki
    'border_width': 2,  # Grubość obramowania
    'pad': (5, 5),  # Wewnętrzne wypełnienie przycisku
    'key': 'exit_style',  # Klucz przycisku
    #'justification': 'right'
}

sg.theme('DarkGrey11')
layout = [
    [
        sg.Text("Type height (cm): "),
        sg.Input(size=(15, 1), enable_events=True, key="HEIGHT"),

    ],
    [
        sg.Text("Type weight (kg):"),
        sg.Input(size=(15, 1), enable_events=True, key="WEIGHT"),
    ],
    [
         sg.Text('Result: '),
         sg.Text("", key='OUTPUT')

    ],
    [
        sg.Text("", size=(15, 1), key="OUTPUT-RESULT"),
        sg.Text("", size=(40, 1), key="OUTPUT-INFO")

    ],
    [
         sg.Text('', size=(42, 1)),
         sg.Button("Submit", key="Submit"),
         sg.Button("Exit")
    ],

]


# Create the window
window = sg.Window("BMI Calculator", layout, finalize=True)


# Event loop
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Exit"):
        window.close()
        break
    elif event == "Exit":
        break
        window.close()
    elif event == "Submit":
        weight = (values["WEIGHT"])
        height = (values["HEIGHT"])
        try:
            if ',' in height:
                height = float(height.replace(',', '.'))

            elif float(height) >= 100 or float(height) <= 300:
                height = float(height)/100

            elif float(weight) <= 0 or float(weight) >= 200 or float(height) <= 0:
                window["OUTPUT-RESULT"].update("Bad Data")
                window["OUTPUT-INFO"].update(null)

        except:
            window["OUTPUT-INFO"].update("")
            window["OUTPUT-RESULT"].update("Bad Data")


        try:
            if float(height) > 0 and float(weight) > 0:
               # BMI = float(weight) / pow(float(height), 2)
                BMI = float(weight) / float(height) ** 2
                window["OUTPUT-RESULT"].update(f"BMI: {BMI:.3f}")

                if BMI < 18.5:
                    window["OUTPUT-INFO"].update("BMI less than 18.5: Underweight")
                elif BMI >= 18.5 and BMI <= 24.9:
                    window["OUTPUT-INFO"].update("BMI from 18.5 to 24.9: Normal body weight")
                elif BMI >= 25 and BMI <= 29.9:
                    window["OUTPUT-INFO"].update("BMI from 25 to 29.9: Overweight")
                elif BMI >= 30:
                    window["OUTPUT-INFO"].update("BMI over 30: Obesity")
            else:
                window["OUTPUT-INFO"].update("")
                window["OUTPUT-RESULT"].update("Bad Data")
        except:
            window["OUTPUT-INFO"].update("")
            window["OUTPUT-RESULT"].update("Bad Data")


window.close()
