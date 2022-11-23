import sys

sys.path.insert(0,"..")
from servicio.ProductosServicio import ProductosServicio
from dominio.Producto import Producto

from ordenamiento.quick_sort import quick_sort
from helpers.limpiar_pantalla import limpiar_pantalla

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
    

    def ordenar_productos(self):

        productos = self.producto_servicio.listar_productos()

        while True:

            limpiar_pantalla()

            print("==== Todos los productos ====\n")

            for producto in productos:
                print(producto)
                print("-------")

            print("=== ORDENAR POR ===")
            print("0. Salir\n1. Id\n2. Nombre\n3. Precio")
            opc = input("Ordenar por: ")

            if not opc.isdigit(): # Comprobando que sea un número
                print(f"{ opc } no es una opción válida.")
                return

            opc = int(opc)

            if opc == 0:
                limpiar_pantalla()
                break

            if opc == 1:
                quick_sort(productos, Producto.get_id, 0, len(productos) - 1)

            if opc == 2:
                quick_sort(productos, Producto.get_nombre, 0, len(productos) - 1)
            
            if opc == 3:
                quick_sort(productos, Producto.get_precio, 0, len(productos) - 1)


    def buscar_producto(self):


        print("=== Buscar producto ===")

        id = input("Id a buscar: ")

        if not id.isdigit(): # Comprobando que sea un número
            print(f"{ id } no es un id válido.")
            return

        producto = self.producto_servicio.recuperar_producto(int(id))

        if not producto:
            print(f"{id} no existe.")
            return
        
        print("== Producto encontrado ==")
        print(producto)
        print("========================")


    def ver_productos(self):

        productos = self.producto_servicio.listar_productos()
        
        while True:

            print("==== Todos los productos ====\n")
            for producto in productos:
                print(producto)
                print("-------")

            print("\n---- Opciones ----")
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
                self.ordenar_productos()

            if opc == 2:
                self.buscar_producto()

    
    def menu(self):

        while True:
            print("===== Mis productos =====")

            print("0. Salir a menú principal")
            print("1. Crear producto")
            print("2. Actualizar producto")
            print("3. Eliminar producto")
            print("4. Ver productos")

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
            
            if opc == 4:
                self.ver_productos()