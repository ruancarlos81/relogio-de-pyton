from tkinter import *
import tkinter
from datetime import datetime

import pyglet
pyglet.font.add_file("digital-7.ttf")

######### CORES ########
cor1 = "#000000"  # preto
cor2 = "#FFFFFF"  # braco

fundo = cor1
cor = cor2

janela = Tk()
janela.title("Relógio em python")
janela.geometry("560x240")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor1)


def relogio():
    tempo = datetime.now()

    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(100, relogio)
    l2.config(text=dia_semana + " " + str(dia) +
              "/" + str(mes) + "/" + str(ano))


l1 = Label(janela, text="", bg=fundo, fg=cor, font=("digital-7 130"))
l1.grid(row=0, column=0, stick=NW, padx=5)

l2 = Label(janela, text="", bg=fundo, fg=cor, font=("digital-7 20"))
l2.grid(row=1, column=0, stick=NW, padx=5)

relogio()

janela.mainloop()
