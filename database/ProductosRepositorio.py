import sys

sys.path.insert(0,"..")
from dominio.Producto import Producto

class ProductosRepositorio:
    
    ARCHIVO = "./database/productos.txt"


    def listar_productos(self) -> list[tuple]:

        file = open( self.ARCHIVO, "r" )

        productos = list()
        for line in file:
            productos.append(tuple( line.rstrip().split("|") ))

        file.close()
        
        return productos


    def listar_nombres_productos(self) -> list[str]:

        file = open( self.ARCHIVO, "r" )

        nombres = list()
        for line in file:
            nombres.append( line.rstrip().split("|")[1] )
        
        file.close()
        return nombres
    

    def listar_id_productos(self) -> list[int]:

        file = open( self.ARCHIVO, "r" )
        
        ids = list()
        for line in file:
            ids.append(int( line.rstrip().split("|")[0] ))
        
        file.close()
        return ids


    def guardar_producto(self, producto : Producto) -> None:
        
        file = open( self.ARCHIVO, "a" )
        file.write(f"{producto.id}|{producto.nombre}|{producto.precio}|{producto.descripcion}\n")
        file.close()

    
    def actualizar_producto(self, producto : Producto) -> None:

        # Guardar los productos diferentes
        file = open( self.ARCHIVO, "r" )
        copia_productos = list()
        for line in file:

            id = int(line.rstrip().split("|")[0])
            
            if id != producto.id:
                copia_productos.append( line.rstrip() )

        file.close()

        # escribir el nuevo producto
        file = open( self.ARCHIVO, "w" )
        file.write(f"{producto.id}|{producto.nombre}|{producto.precio}|{producto.descripcion}\n")
        file.close()

        # escribir la copia de los productos
        file = open( self.ARCHIVO, "a" )
        for copia_producto in copia_productos:
            file.write(f"{copia_producto}\n")

        file.close()


    def eliminar_producto(self, id : int) -> None:

        # Guardar los productos
        file = open( self.ARCHIVO, "r" )
        copia_productos = list()
        for line in file:

            id_producto = int(line.rstrip().split("|")[0])
            
            if id_producto != id: # Filtrando el producto a eliminar
                copia_productos.append( line.rstrip() )

        file.close()

        self.reinciar_archivo()

        # escribir la copia de los productos
        file = open( self.ARCHIVO, "a" )
        for copia_producto in copia_productos:
            file.write(f"{copia_producto}\n")

    
    def reinciar_archivo(self) -> None:

        file = open( self.ARCHIVO, "w" )
        file.write("")
        file.close()
