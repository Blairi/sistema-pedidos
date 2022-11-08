import sys

sys.path.insert(0,"..")

from controladores.GrafosControlador import GrafosControlador
from controladores.ProductosControlador import ProductosControlador
from controladores.ClientesControlador import ClientesControlador

from helpers.limpiar_pantalla import limpiar_pantalla

def main():

    producto_controlador = ProductosControlador()
    grafo_controlador = GrafosControlador()
    cliente_controlador = ClientesControlador()

    while True:

        print("===== Sistema de pedidos =====")
        print("Eligé escribiendo el número de la opción deseada:")

        opc = int(input("0. Salir.\n1. Mi mapa.\n2. Mis productos.\n3. Clientes.\n: "))

        if opc == 0:
            break

        if opc == 1:
            limpiar_pantalla()
            grafo_controlador.menu()

        if opc == 2:
            limpiar_pantalla()
            producto_controlador.menu()
        
        if opc == 3:
            limpiar_pantalla()
            cliente_controlador.menu()


main()