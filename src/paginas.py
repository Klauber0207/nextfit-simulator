import tkinter as tk

class Pagina:

    def __init__(self, id, tempo):
        self.id = id
        self.tempo = tempo


    def setID(self, id):
        self.id = id

    def setTempo(self, tempo):
        self.tempo = tempo

    def getID(self):
        return self.id

    def getTempo(self):
        return self.tempo


    def __str__(self):
        return ("Pagina: " + str(self.getID()) + " Tempo:" + str(self.getTempo()))

class MyDialog:

    def __init__(self, parent):
        top = self.top = tk.Toplevel(parent)
        self.myLabel = tk.Label(top, text='ID da nova pagina')
        self.myLabel.pack()
        self.myEntryBox = tk.Entry(top)
        self.myEntryBox.pack()
        self.mySubmitButton = tk.Button(top, text='OK', command=self.send)
        self.mySubmitButton.pack()

    def send(self):
        self.id = self.myEntryBox.get()
        self.top.destroy()

