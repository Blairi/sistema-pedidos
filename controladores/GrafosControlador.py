import sys

sys.path.insert(0,"..")
from helpers.limpiar_pantalla import limpiar_pantalla
from servicio.GrafosServicio import GrafosServicio


class GrafosControlador:
    
    def __init__(self) -> None:
        self.grafo_servicio = GrafosServicio()

    
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

    
    def buscar_caminos(self):

        punto_inicial = input("Lugar en el que te encuentas: ")

        resp = self.grafo_servicio.buscar_caminos( punto_inicial )

        if not resp:
            print(f"{punto_inicial} no existe en tu mapa.")
            return

    
    def menu(self):
        while True:

            print("===== Mi mapa =====")
            print("0. Salir a menu principal")

            if self.grafo_servicio.es_vacio():
                print("1. Iniciar mapa")

            else:
                print("2. Reiniciar mapa")
                print("3. Nuevo camino")
                print("4. Agregar nuevo lugar")
                print("5. Mostrar rutas")

            opc = int( input(": ") )

            if opc == 0:
                break

            elif opc == 1 and self.grafo_servicio.es_vacio():
                self.nuevo_mapa()

            if opc == 2:
                self.reiniciar_mapa()

            if opc == 3:
                self.nuevo_camino()

            if opc == 4:
                self.nuevo_lugar()

            if opc == 5:
                self.buscar_caminos()

