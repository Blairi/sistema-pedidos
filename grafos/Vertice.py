
class Vertice:

    nombre = None
    vecinos = list()
    distancia = 9999
    color = "blanco"
    pred = -1

    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.vecinos = list()
        self.distancia = 9999
        self.color = "blanco"
        self.pred = -1

    def agregar_vecino(self, vecino):
        if vecino not in self.vecinos:
            self.vecinos.append(vecino)
            self.vecinos.sort()
