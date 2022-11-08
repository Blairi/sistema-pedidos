import sys
import random

sys.path.insert(0,"..")
from dominio.Cliente import Cliente
from database.ClientesRepositorio import ClientesRespositorio

class ClientesServicio:
    
    def __init__(self) -> None:
        self.repositorio = ClientesRespositorio()

    
    def listar_clientes(self) -> list[Cliente]:

        clientes = list()
        for tupla in self.repositorio.listar_clientes():
            id, nombre = tupla
            
            id = int(id)

            clientes.append( Cliente(id, nombre) )

        return clientes

    
    def listar_id_clientes(self) -> list[int]:
        return self.repositorio.listar_id_clientes()

    
    def agregar_cliente(self, nombre:str) -> bool:

        id = self.generar_id()

        while id in self.listar_id_clientes(): # Asegurando que no se repita un id
            id = self.generar_id()

        nombre = nombre.lower()

        cliente = Cliente( id, nombre )

        self.repositorio.guardar_cliente( cliente )

        return True
    

    def actualizar_cliente(self, id:int, nombre:str) -> bool:

        if id not in self.listar_id_clientes():
            return False

        nombre = nombre.lower()

        cliente_actualizado = Cliente( id, nombre )

        self.repositorio.actualizar_cliente( cliente_actualizado )

        return True


    def eliminar_cliente(self, id : int) -> bool:

        if id not in self.listar_id_clientes():
            return False

        self.repositorio.eliminar_cliente( id )
        
        return True


    def generar_id(self) -> int:
        return random.randint(0, 9999999)

