import sys

sys.path.insert(0,"..")
from helpers.limpiar_pantalla import limpiar_pantalla
from servicio.GrafosServicio import GrafosServicio


class GrafosControlador:
    
    def __init__(self) -> None:
        self.grafo_servicio = GrafosServicio()

    
    def mostrar_lugares(self) -> None:
        lugares = self.grafo_servicio.listar_nombre_vertices()
        for lugar in lugares:
            print( lugar )
    
    def nuevo_mapa(self) -> None:

        nombre = input("Nombre de tu establecimiento: ")

        guardado = self.grafo_servicio.agregar_vertice( nombre )

        if not guardado:
            print("Se ha producido un error")
            return

        limpiar_pantalla()


    def nuevo_lugar(self):
        
        nombre = input("Nombre del nuevo lugar: ")

        guardado = self.grafo_servicio.agregar_vertice( nombre )

        if not guardado:
            print(f"{nombre} ya existe")
            return
        
        limpiar_pantalla()


    def nuevo_camino(self):

        nombre_v1 = input("Conectar a: ")
        nombre_v2 = input("Con: ")

        guardado = self.grafo_servicio.agregar_arista( nombre_v1, nombre_v2 )

        if not guardado:
            print("Error al agregar camino. Los lugares no existen o formato incorrecto.")
            return
        
        limpiar_pantalla()


    def reiniciar_mapa(self):
        resp = input("¿Estas seguro de reiniciar tu mapa? s/n: ")

        if resp == "s":
            self.grafo_servicio.reiniciar_grafo()

        limpiar_pantalla()

    
    def buscar_camino(self):

        limpiar_pantalla()

        print("=== Lugares ===")
        self.mostrar_lugares()

        punto_inicial = input("Lugar en el que te encuentras: ")
        punto_destino = input("Destino: ")

        resp = self.grafo_servicio.buscar_camino( punto_inicial, punto_destino )

        if not resp:
            print(f"{punto_inicial} o {punto_destino} no existe en tu mapa.")
            return

    
    def menu(self):
        while True:

            print("===== Mi mapa =====")
            print("0. Salir a menu principal")

            if self.grafo_servicio.es_vacio():
                print("1. Iniciar mapa")

            else:
                print("2. Reiniciar mapa")
                print("3. Agregar nuevo camino")
                print("4. Agregar nuevo lugar")
                print("5. Buscar camino")

            opc = int( input(": ") )

            if opc == 0:
                limpiar_pantalla()
                break

            if opc == 1 and self.grafo_servicio.es_vacio():
                self.nuevo_mapa()

            if opc == 2 and not self.grafo_servicio.es_vacio():
                self.reiniciar_mapa()

            if opc == 3 and not self.grafo_servicio.es_vacio():
                self.nuevo_camino()

            if opc == 4 and not self.grafo_servicio.es_vacio():
                self.nuevo_lugar()

            if opc == 5 and not self.grafo_servicio.es_vacio():
                self.buscar_camino()

