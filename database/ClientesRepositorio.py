import sys

sys.path.insert(0,"..")
from dominio.Cliente import Cliente

class ClientesRespositorio:
    
    ARCHIVO = "./database/clientes.txt"


    def guardar_cliente(self, cliente:Cliente) -> None:

        file = open( self.ARCHIVO, "a" )
        file.write(f"{cliente.id}|{cliente.nombre}|{cliente.ubicacion}\n")
        file.close()

    
    def listar_clientes(self) -> list[tuple]:

        file = open( self.ARCHIVO, "r" )

        clientes = list()
        for line in file:
            clientes.append(tuple( line.rstrip().split("|") ))

        file.close()

        return clientes

    
    def listar_id_clientes(self) -> list[int]:

        file = open( self.ARCHIVO, "r" )
        
        ids = list()
        for line in file:
            ids.append(int( line.rstrip().split("|")[0] ))
        
        file.close()
        return ids


    def actualizar_cliente(self, cliente:Cliente) -> None:

        # Guardar los productos diferentes
        file = open( self.ARCHIVO, "r" )

        copia_clientes = list()
        for line in file:

            id = int(line.rstrip().split("|")[0])
            
            if id != cliente.id:
                copia_clientes.append( line.rstrip() )

        file.close()

        # escribir el nuevo cliente
        file = open( self.ARCHIVO, "w" )
        file.write(f"{cliente.id}|{cliente.nombre}|{cliente.ubicacion}\n")
        file.close()

        # escribir la copia de los productos
        file = open( self.ARCHIVO, "a" )
        for copia_cliente in copia_clientes:
            file.write(f"{copia_cliente}\n")

        file.close()

    
    def eliminar_cliente(self, id : int) -> None:

        # Guardar los productos
        file = open( self.ARCHIVO, "r" )
        copia_clientes = list()
        for line in file:

            id_cliente = int(line.rstrip().split("|")[0])

            if id_cliente != id: # Filtrando el producto a eliminar
                copia_clientes.append( line.rstrip() )

        file.close()

        self.reinciar_archivo()

        # escribir la copia de los productos
        file = open( self.ARCHIVO, "a" )
        for copia_cliente in copia_clientes:
            file.write(f"{copia_cliente}\n")

    
    def reinciar_archivo(self) -> None:

        file = open( self.ARCHIVO, "w" )
        file.write("")
        file.close()