import sys

sys.path.insert(0,"..")
from helpers.limpiar_pantalla import limpiar_pantalla
from servicio.ClientesServicio import ClientesServicio
from ordenamiento.quick_sort import quick_sort
from dominio.Cliente import Cliente

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

    
    def ordenar_clientes(self):

        clientes = self.cliente_servicio.listar_clientes()

        while True:

            limpiar_pantalla()

            print("==== Todos los clientes ====\n")

            for cliente in clientes:
                print(cliente)
                print("-------")

            print("=== ORDENAR POR ===")
            print("0. Salir\n1. Id\n2. Nombre")
            opc = input("Ordenar por: ")

            if not opc.isdigit(): # Comprobando que sea un número
                print(f"{ opc } no es una opción válida.")
                return

            opc = int(opc)

            if opc == 0:
                limpiar_pantalla()
                break

            if opc == 1:
                quick_sort(clientes, Cliente.get_id, 0, len(clientes) - 1)

            if opc == 2:
                quick_sort(clientes, Cliente.get_nombre, 0, len(clientes) - 1)


    def buscar_clientes(self):

        while True:

            print("=== BUSCAR POR ===")
            print("0. Salir\n1. Id\n2. Nombre")
            opc = input("Buscar por: ")

            if not opc.isdigit(): # Comprobando que sea un número
                print(f"{ opc } no es una opción válida.")
                return

            opc = int(opc)

            if opc == 0:
                limpiar_pantalla()
                break

            if opc == 1:

                llave = input("Id a buscar: ")

                if not llave.isdigit(): # Comprobando que sea un número
                    print(f"{ llave } no es un id válido.")
                    return

                cliente = self.cliente_servicio.buscar_clientes(Cliente.get_id, int(llave))

                if not cliente:
                    print(f"{llave} no existe.")
                    continue
                
                print("== Cliente encontrado ==")
                print(cliente)
                print("========================")
            
            if opc == 2:

                llave = input("Nombre a buscar: ")

                cliente = self.cliente_servicio.buscar_clientes(Cliente.get_nombre, llave.lower())

                if not cliente:
                    print(f"{llave} no existe.")
                    continue
                
                print("== Cliente encontrado ==")
                print(cliente)
                print("========================")




    def ver_clientes(self):

        clientes = self.cliente_servicio.listar_clientes()
        
        while True:

            limpiar_pantalla()

            print("==== Todos los clientes ====\n")
            for cliente in clientes:
                print(cliente)
                print("-------")

            print("-- Opciones --")
            print("0. Salir\n1. Ordenar\n2. Buscar")

            opc = input(": ")

            if not opc.isdigit():
                print(f"{ opc } no es una opción válida.")
                return
            
            opc = int(opc)

            if opc == 0:
                limpiar_pantalla()
                break
                
            if opc == 1:
                self.ordenar_clientes()

            if opc == 2:
                self.buscar_clientes()

    
    def menu(self):

        while True:
            print("===== Mis Clientes =====")

            print("0. Salir a menu principal")
            print("1. Agregar cliente")
            print("2. Actualizar cliente")
            print("3. Eliminar cliente")
            print("4. Ver clientes")

            opc = int( input(": ") )

            if opc == 0:
                limpiar_pantalla()
                break

            if opc == 1:
                self.crear_cliente()

            if opc == 2:
                self.actualizar_cliente()

            if opc == 3:
                self.eliminar_cliente()

            if opc == 4:
                self.ver_clientes()

