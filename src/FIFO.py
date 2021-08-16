from future.moves import tkinter as tk
from future.moves.tkinter import ttk
from paginas import *
import pandas as pd

# Dados
link = "C:/Users/klaub/PycharmProjects/nextfit-simulator/src/page.csv"
NUMERODEPAGINASPADRAO = 6
vetor = []
pageid = pd.read_csv(link, usecols=['id']).values.tolist()
pagetempo = pd.read_csv(link, usecols=['tempo']).values.tolist()
NOMEDASCOLUNAS = ['id', 'tempo']
dict = ['#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7']

#   Passando dados para vetor
for i in range(0, NUMERODEPAGINASPADRAO):
    aux = Pagina(pageid[i][0], pagetempo[i][0])
    vetor.append(aux)

#   janela
janela = tk.Tk()
LARGURA = 270
ALTURA = 270
janela.title('FIFO')
janela.resizable(1, 1)
janela.geometry("%dx%d" % (LARGURA, ALTURA))
janela.config(bg='#B0C4DE')

#   tabela
tabela = ttk.Treeview(janela)
tabela['columns'] = NOMEDASCOLUNAS

for i in range(0, len(NOMEDASCOLUNAS)):
    tabela.column(dict[i], width=int(LARGURA / 2), minwidth=100)
    tabela.heading(dict[i], text=NOMEDASCOLUNAS[i], anchor=tk.N)

x = 0
for i in range(0, len(vetor)):
    tabela.insert(parent='', index='end', iid=x, text=pageid[i], values=(pagetempo[i]))
    x += 1
tabela.pack(pady=5, padx=3)

#   Container
container = tk.Frame(master=janela, bg='black').pack()


def nova_pagina():
    print("Nova Paginaaaa")

    maior = 0
    idmaior = 0
    aux = 0
    for i in range(0, NUMERODEPAGINASPADRAO):
        if pagetempo[i][0] > maior:
            maior = pagetempo[i][0]
            idmaior = pageid[i][0]
            aux = i
#    print("maior é a pagina", idmaior,"de tempo", maior)
    novapagid = input("Entre com o id da nova pagina: ")
    pageid[aux][0] = novapagid
    pagetempo[aux][0] = 0
    tabela.item(aux, text=pageid[aux][0], values=[pagetempo[aux][0]])


#   Botão
botao1 = tk.Button(master=container, text="Page foult", command=lambda: nova_pagina()).pack(anchor=tk.E, padx=3)

tk.mainloop()
