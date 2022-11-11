from .Vertice import Vertice

class Grafo:
    vertices = {}

    def __init__(self) -> None:
        self.vertices = dict()

    def agregar_vertice(self, vertice : Vertice) -> bool:

        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return True
        else:
            return False


    def agregar_arista(self, u, v) -> bool:

        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.agregar_vecino(v)
                if key == v:
                    value.agregar_vecino(u)
            return True
        else:
            return False


    def BFS(self, vertice_origen : Vertice, vertice_destino : Vertice):

        vertices_padres = {}

        vertice_origen.distancia = 0
        vertice_origen.color = "gris"
        vertice_origen.pred = -1

        lista = list()
        lista.append(vertice_origen.nombre)

        while len(lista) > 0:

            u = lista.pop()
            node_u = self.vertices[u]
            
            for v in node_u.vecinos:

                node_v = self.vertices[v]

                if node_v.color == "blanco":
                    node_v.color = "gris"
                    node_v.distancia = node_u.distancia + 1
                    node_v.pred = node_u.nombre
                    lista.append(v)

                    vertices_padres[node_v.nombre] = node_u.nombre

            self.vertices[u].color = "black"
        
        camino = []
        while vertice_destino.nombre != None:
            camino.append( vertice_destino.nombre )
            vertice_destino.nombre = vertices_padres.get( vertice_destino.nombre )

        camino.reverse()

        print(f"Sigue esta ruta para llegar a tu destino: ")
        print(" => ".join(camino))

    
    def imprimir_grafo(self) -> None:
        for key in sorted(list(self.vertices.keys())):
            print(f"Vertice: { key } \nSus vecinos son: { str(self.vertices[key].vecinos) }")