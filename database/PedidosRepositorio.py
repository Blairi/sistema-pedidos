import sys

sys.path.insert(0,"..")
from dominio.Pedido import Pedido

class PedidosRepositorio:

    ARCHIVO = "./database/pedidos.txt"

    def listar_pedidos(self) -> list[tuple]:

        file = open( self.ARCHIVO, "r" )

        pedidos = list()
        for line in file:
            pedidos.append(tuple( line.rstrip().split("|") ))

        file.close()

        return pedidos


    def listar_id_pedidos(self) -> list[int]:

        file = open( self.ARCHIVO, "r" )

        ids = list()
        for line in file:
            ids.append(int( line.rstrip().split("|")[0] ))
        
        file.close()
        
        return ids


    def guardar_pedido(self, pedido : Pedido) -> None:
        
        file = open( self.ARCHIVO, "a" )

        ids = ', '.join(map(str, pedido.productos_id))

        file.write(f"{pedido.id}|{pedido.creado}|{pedido.fecha}|{pedido.cliente_id}|{pedido.lugar}|{pedido.ruta}|{ids}|{pedido.total}|{pedido.entregrado}\n")

        file.close()

    
    def actualizar_pedido(self, pedido : Pedido) -> None:

        # Guardar los pedidos diferentes
        file = open( self.ARCHIVO, "r" )
        copia_pedidos = list()
        for line in file:

            id = int(line.rstrip().split("|")[0])
            
            if id != pedido.id:
                copia_pedidos.append( line.rstrip() )

        file.close()

        # escribir el nuevo pedido
        file = open( self.ARCHIVO, "w" )

        ids = ', '.join(map(str, pedido.productos_id))

        file.write(f"{pedido.id}|{pedido.creado}|{pedido.fecha}|{pedido.cliente_id}|{pedido.lugar}|{pedido.ruta}|{ids}|{pedido.total}|{pedido.entregrado}\n")
        file.close()

        # escribir la copia de los productos
        file = open( self.ARCHIVO, "a" )
        for copia_pedido in copia_pedidos:
            file.write(f"{copia_pedido}\n")

        file.close()


    def eliminar_pedido(self, id : int) -> None:

        # Guardar los pedidos
        file = open( self.ARCHIVO, "r" )
        copia_pedidos = list()
        for line in file:

            id_pedido = int(line.rstrip().split("|")[0])

            if id_pedido != id: # Filtrando el producto a eliminar
                copia_pedidos.append( line.rstrip() )

        file.close()

        self.reiniciar_archivo()

        # escribir la copia de los pedidos
        file = open( self.ARCHIVO, "a" )
        for copia_pedido in copia_pedidos:
            file.write(f"{copia_pedido}\n")


    def reiniciar_archivo(self) -> None:

        file = open( self.ARCHIVO, "w" )
        file.write("")
        file.close()

