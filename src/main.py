from future.moves import tkinter as tk
from future.moves.tkinter import ttk

dict = ['#0', '#1', '#2']


def NextFit(blockSize, m, processSize, n):
    # Stores block id of the block
    # allocated to a process

    # Initially no block is assigned
    # to any process
    allocation = [-1] * n
    j = 0

    # pick each process and find suitable blocks
    # according to its size ad assign to it
    for i in range(n):

        # Do not start from beginning
        while j < m:

            if blockSize[j] >= processSize[i]:
                # allocate block j to p[i] process
                allocation[i] = j

                # Reduce available memory in this block.
                blockSize[j] -= processSize[i]

                break

            # mod m will help in traversing the
            # blocks from starting block after
            # we reach the end.
            j = (j + 1) % m

    colunas = ['Process No', 'Process Size', 'Block no']
    conteudo = []
    for i in range(n):
        print(i + 1, "         ", processSize[i],
                    end="     ")

        if allocation[i] != -1:
            print(allocation[i] + 1)
            conteudo.append([[i + 1], [processSize[i]], [allocation[i] + 1]])
        else:
            print("Not Allocated")

    return colunas, conteudo


blockSize = [7, 9, 3]
processSize = [2, 1, 5]
m = len(blockSize)
n = len(processSize)

nomecolunas, conteudo = NextFit(blockSize, m, processSize, n)
# print(nomecolunas)
# print(conteudo)

#   janela
janela = tk.Tk()
LARGURA = 300
ALTURA = 200
janela.title('NextFit')
janela.resizable(0, 0)
janela.geometry("%dx%d" % (LARGURA, ALTURA))
janela.config(bg='#B0C4DE')

#   tabela
tabela = ttk.Treeview(janela)
tabela['columns'] = nomecolunas

for i in range(0, len(nomecolunas)):
    tabela.column(dict[i], width=100, minwidth=85)
    tabela.heading(dict[i], text=nomecolunas[i], anchor=tk.W)

x = 0
for i in range(0, len(conteudo)):
    tabela.insert(parent='', index='end', iid=x, text=conteudo[i][0], values=(conteudo[i][1], conteudo[i][2]))
    x += 1
tabela.pack(pady=4, padx=2)

tk.mainloop()
