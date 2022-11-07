import sys
import copy

sys.path.insert(0,"..")
from database.GrafosRepositorio import GrafosRepositorio
from grafos.Grafo import Grafo
from grafos.Vertice import Vertice


class GrafosServicio:
    
    def __init__(self) -> None:
        self.repositorio = GrafosRepositorio()
        self.grafo = self.constuir_grafo()

    
    def buscar_camino(self, vertice_inicial : str, vertice_destino : str) -> bool:

        if not vertice_inicial in self.grafo.vertices:
            return False
        if not vertice_destino in self.grafo.vertices:
            return False
        
        # Hacemos una copia del grafo, ya que el algoritmo muta el objeto
        copia_grafo = self.constuir_grafo()
        copia_grafo.BFS( copia_grafo.vertices[ vertice_inicial ], copia_grafo.vertices[ vertice_destino ] )

        return True


    def constuir_grafo(self) -> Grafo:

        vertices_aristas = self.repositorio.recuperar_datos()

        grafo = Grafo()

        for vertice_aristas in vertices_aristas:

            # Separar vertices y aristas
            vertice, aristas = vertice_aristas
            aristas = aristas.split(",")

            # Crear vertices y aristas
            grafo.agregar_vertice( Vertice(vertice) )

            for arista in aristas:
                grafo.agregar_arista(vertice, arista)

        return grafo
    

    def mostrar_grafo(self) -> None:
        self.grafo.imprimir_grafo()


    def listar_nombre_vertices(self) -> list[str]:
        return self.repositorio.listar_nombre_vertices()

    
    def es_vacio(self) -> bool:
        return len( self.listar_nombre_vertices() ) < 1


    def agregar_vertice(self, nombre : str) -> bool:

        vertice = Vertice( nombre.lower() )

        # Lo agregamos al grafo y comprobamos que no exista
        agregado = self.grafo.agregar_vertice( vertice )

        if not agregado: # Si el vertice ya existe
            return False

        # Lo guardamos en el repositorio
        self.repositorio.guardar_vertice(vertice)

        return True

    
    def agregar_arista(self, nombre_vertice1 : str, nombre_vertice2 : str) -> bool:

        nombre_vertice1 = nombre_vertice1.lower()
        nombre_vertice2 = nombre_vertice2.lower()

        # Asegurando que el vertice exista
        if not nombre_vertice1 in self.grafo.vertices:
            return False
        if not nombre_vertice2 in self.grafo.vertices:
            return False

        # Asegurando que no existan aristas que apunten a su vertice
        if nombre_vertice1 in self.grafo.vertices[nombre_vertice2].vecinos:
            return False

        agregada = self.grafo.agregar_arista( nombre_vertice1, nombre_vertice2 )

        if not agregada: # Si ocurre algun error
            return False

        # Guardando en el repositorio
        self.repositorio.guardar_arista( nombre_vertice1, nombre_vertice2 )

        return True


    def reiniciar_grafo(self):
        self.grafo = Grafo()
        self.repositorio.reiniciar_archivo()
