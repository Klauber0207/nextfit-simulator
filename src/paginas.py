

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