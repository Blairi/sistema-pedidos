from dominio.Pedido import Pedido

class Nodo:

    def __init__(self, pedido:Pedido) -> None:
        self.hijoIzq = None
        self.hijoDer = None
        self.pedido = pedido
    
    def get_pedido_id(self) -> int:
        return self.pedido.get_id()
    