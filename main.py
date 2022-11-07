import sys

sys.path.insert(0,"..")

from controladores.GrafosControlador import GrafosControlador
from controladores.ProductosControlador import ProductosControlador

from helpers.limpiar_pantalla import limpiar_pantalla

def main():
    producto_controlador = ProductosControlador()
    grafo_controlador = GrafosControlador()

    while True:

        print("===== Sistema de pedidos =====")
        print("Eligé escribiendo el número de la opción deseada:")

        opc = int(input("0. Salir.\n1. Mi mapa.\n2. Mis productos.\n: "))

        if opc == 0:
            break

        if opc == 1:
            limpiar_pantalla()
            grafo_controlador.menu()

        if opc == 2:
            limpiar_pantalla()
            producto_controlador.menu()


main()