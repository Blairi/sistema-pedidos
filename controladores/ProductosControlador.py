import sys

sys.path.insert(0,"..")
from helpers.limpiar_pantalla import limpiar_pantalla
from servicio.ProductosServicio import ProductosServicio

class ProductosControlador:

    def __init__(self) -> None:
        self.producto_servicio = ProductosServicio()

    
    def mostrar_nombre_productos(self):

        productos = self.producto_servicio.listar_nombre_productos()

        if len(productos) < 1:
            return

        print("====== Tus productos ======")
        for producto in productos:
            print(producto)

        
    def mostrar_productos(self):

        productos = self.producto_servicio.listar_productos()

        if len(productos) < 1:
            return

        print("====== Tus productos ======")
        for producto in productos:
            print(producto)
            print()


    def crear_producto(self):

        nombre = input("Nombre del producto: ")
        precio = input("Precio del producto: ")
        desc = input("Descripción del producto: ")

        if not precio.replace(".", "", 1).isdigit(): # Comprobando que sea un número
            print(f"{precio} no es un precio válido.")
            return

        self.producto_servicio.agregar_producto( nombre, precio, desc )

        limpiar_pantalla()


    def actualizar_producto(self):

        self.mostrar_productos()

        id = input("Id del producto a actualizar: ")

        if not id.isdigit(): # Comprobando que sea un número
            print(f"{id} no es un id válido.")
            return

        id = int( id )
        
        precio = input("Nuevo precio: ")
        if not precio.replace(".", "", 1).isdigit(): # Comprobando que sea un número
            print(f"{precio} no es un precio válido.")
            return

        nombre = input("Nuevo nombre: ")
        desc = input("Nueva descripción: ")

        actualizado = self.producto_servicio.actualizar_producto( id, nombre, precio, desc )

        if not actualizado:
            print(f"{id} no existe")
            return

        limpiar_pantalla()

    
    def eliminar_producto(self):

        self.mostrar_productos()

        id = input("Id del producto a eliminar: ")

        if not id.isdigit(): # Comprobando que sea un número
            print(f"{id} no es un id válido.")
            return

        eliminado = self.producto_servicio.eliminar_producto( int(id) )

        if not eliminado:
            print(f"{id} no existe")
            return

        limpiar_pantalla()

    
    def menu(self):

        while True:
            print("===== Mis productos =====")

            print("0. Salir a menú principal")
            print("1. Crear producto")
            print("2. Actualizar producto")
            print("3. Eliminar producto")

            opc = input(": ")

            if not opc.isdigit():
                print(f"{opc} no es una opción válida")
                continue
            
            opc = int(opc)

            if opc == 0:
                limpiar_pantalla()
                break

            if opc == 1:
                self.crear_producto()

            if opc == 2:
                self.actualizar_producto()

            if opc == 3:
                self.eliminar_producto()