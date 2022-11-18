import sys
import random

sys.path.insert(0,"..")
from dominio.Producto import Producto
from database.ProductosRepositorio import ProductosRepositorio
from busqueda.busqueda_binaria import busqueda_binaria
from ordenamiento.quick_sort import quick_sort

class ProductosServicio:

    def __init__(self) -> None:
        self.repositorio = ProductosRepositorio()


    def listar_productos(self) -> list[Producto]:

        productos = list()
        for tupla in self.repositorio.listar_productos():
            id, nombre, precio, desc, = tupla
            
            id = int(id)
            precio = float(precio)

            productos.append( Producto(id, nombre, precio, desc) )

        return productos
    

    def recuperar_producto(self, id : int) -> Producto:
        
        productos = self.listar_productos()
        
        quick_sort(productos, Producto.get_id, 0, len(productos) - 1)

        indice = busqueda_binaria(productos, id, Producto.get_id, 0, len(productos) - 1)

        if not indice and indice != 0:
            return None

        return productos[indice]


    def listar_nombre_productos(self) -> list[str]:
        return self.repositorio.listar_nombres_productos()

    
    def listar_id_productos(self) -> list[int]:
        return self.repositorio.listar_id_productos()


    def agregar_producto(self, nombre : str, precio : float, desc : str) -> bool:

        id = self.generar_id()

        while id in self.listar_id_productos(): # Asegurando que no se repita un id
            id = self.generar_id()

        nombre = nombre.lower()
        precio = float( precio )

        producto = Producto( id, nombre, precio, desc )

        self.repositorio.guardar_producto( producto )

        return True


    def actualizar_producto(self, id : int, nombre : str, precio : float, desc : str) -> bool:

        if id not in self.listar_id_productos():
            return False

        nombre = nombre.lower()
        precio = float( precio )

        producto_actualizado = Producto( id, nombre, precio, desc )

        self.repositorio.actualizar_producto( producto_actualizado )

        return True

    
    def eliminar_producto(self, id : int) -> bool:

        if id not in self.listar_id_productos():
            return False

        self.repositorio.eliminar_producto( id )
        
        return True


    def generar_id(self) -> int:
        return random.randint(0, 9999999)
