import sys

sys.path.insert(0,"..")
from helpers.limpiar_pantalla import limpiar_pantalla
from servicio.ClientesServicio import ClientesServicio

class ClientesControlador:
    
    def __init__(self) -> None:
        self.cliente_servicio = ClientesServicio()

    
    def mostrar_clientes(self):

        clientes = self.cliente_servicio.listar_clientes()

        if len(clientes) < 1:
            return

        print("====== Tus clientes ======")
        for cliente in clientes:
            print(cliente)

        
    def crear_cliente(self):

        nombre = input("Nombre del cliente: ")

        self.cliente_servicio.agregar_cliente( nombre )

        limpiar_pantalla()

    
    def actualizar_cliente(self):

        self.mostrar_clientes()

        id = input("Id del cliente a actualizar: ")

        if not id.isdigit(): # Comprobando que sea un número
            print(f"{id} no es un id válido.")
            return

        id = int( id )

        nombre = input("Nuevo nombre: ")

        actualizado = self.cliente_servicio.actualizar_cliente( id, nombre )

        if not actualizado:
            print(f"{id} no existe")
            return

        limpiar_pantalla()


    def eliminar_cliente(self):
        self.mostrar_clientes()

        id = input("Id del cliente a eliminar: ")

        if not id.isdigit(): # Comprobando que sea un número
            print(f"{id} no es un id válido.")
            return

        eliminado = self.cliente_servicio.eliminar_cliente( int(id) )

        if not eliminado:
            print(f"{id} no existe")
            return

        limpiar_pantalla()

    
    def menu(self):

        while True:
            print("===== Mis Clientes =====")

            print("0. Salir a menu principal")
            print("1. Agregar cliente")
            print("2. Actualizar cliente")
            print("3. Eliminar cliente")

            opc = int( input(": ") )

            if opc == 0:
                break

            if opc == 1:
                self.crear_cliente()

            if opc == 2:
                self.actualizar_cliente()

            if opc == 3:
                self.eliminar_cliente()

