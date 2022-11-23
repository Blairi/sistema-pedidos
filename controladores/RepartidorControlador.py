import sys

sys.path.insert(0,"..")
from .PedidosControlador import PedidosControlador
from helpers.limpiar_pantalla import limpiar_pantalla

class RepartidorControlador:

    def __init__(self) -> None:
        self.pedidos_controlador = PedidosControlador()
    
    def menu(self):
        self.pedidos_controlador.despachar_pedido()
