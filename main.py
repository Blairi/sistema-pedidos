import sys

sys.path.insert(0,"..")
from controladores.GrafosControlador import GrafosControlador
from controladores.ProductosControlador import ProductosControlador
from controladores.ClientesControlador import ClientesControlador
from controladores.PedidosControlador import PedidosControlador
from controladores.RepartidorControlador import RepartidorControlador

from helpers.limpiar_pantalla import limpiar_pantalla

def main():

    producto_controlador = ProductosControlador()
    grafo_controlador = GrafosControlador()
    cliente_controlador = ClientesControlador()
    pedidos_controlador = PedidosControlador()
    repartidor_controlador = RepartidorControlador()

    while True:

        print("===== Sistema de pedidos =====")
        print("Eligé escribiendo el número de la opción deseada:")

        resp = input("Iniciar como\n0. Salir\n1. Persona a cargo\n2. Repartidor\n: ")

        if not resp.isdigit():
            print(f"{resp} no es una opción válida")
            continue

        resp = int(resp)

        if resp == 0:
            break

        if resp == 1: # Persona a cargo
            limpiar_pantalla()

            opc = input("0. Salir.\n1. Mi mapa.\n2. Mis productos.\n3. Clientes.\n4. Pedidos. \n: ")

            if not opc.isdigit():
                print(f"{opc} no es una opción válida")
                continue
                
            opc = int(opc)

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
            
            if opc == 4:
                limpiar_pantalla()
                pedidos_controlador.menu()

        if resp == 2: # Repartidor
            limpiar_pantalla()
            repartidor_controlador.menu()


main()