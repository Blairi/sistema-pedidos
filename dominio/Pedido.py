from datetime import datetime

class Pedido:

    def __init__(
        self,
        id : int|None,
        creado : datetime,
        fecha : datetime|None,
        cliente_id : int|None,
        lugar : str|None,
        ruta : str|None,
        productos_id : list[int],
        total : float ) -> None:

        self.id = id
        self.creado = creado
        self.fecha = fecha
        self.cliente_id = cliente_id
        self.lugar = lugar
        self.ruta = ruta
        self.productos_id = productos_id
        self.total = total


    def tiempo_restante(self) -> None:
        tiempo = self.fecha - datetime.now()
        return tiempo


    def __str__(self) -> str:
        return f"id: {self.id}\ncreado: {self.creado}\nfecha: {self.fecha}\ncliente_id: {self.cliente_id}\nlugar: {self.lugar}\nruta: {self.ruta}\nproductos_id: {self.productos_id}\ntotal: {self.total}"

    
    def set_productos_id(self, productos_id : list[int]) -> None:
        self.productos_id = productos_id
    

    def get_productos_id(self) -> list[int]:
        return self.productos_id

    
    def get_id(self) -> int:
        return self.id


    def get_creado(self) -> str:
        return self.creado


    def get_fecha(self) -> str:
        return self.fecha


    def get_cliente(self) -> int:
        return self.cliente_id


    def get_lugar(self) -> str:
        return self.lugar


    def get_total(self) -> float:
        return self.total

    
    def get_ruta(self) -> str:
        return self.ruta