import sys
import random
from datetime import datetime

sys.path.insert(0,"..")
from dominio.Pedido import Pedido
from database.PedidosRepositorio import PedidosRepositorio
from servicio.ProductosServicio import ProductosServicio
from arbol.Arbol import Arbol
from arbol.Nodo import Nodo


class PedidosServicio:

    def __init__(self) -> None:

        self.repositorio = PedidosRepositorio()
        self.productos_servicio = ProductosServicio()
    
    # func sera una función que retorne el valor a comparar del objeto
    def construir_arbol(self, func_pedido, func_nodo) -> Arbol:

        arbol = Arbol()

        pedidos = self.listar_pedidos()
        for pedido in pedidos:
            arbol.agregar(pedido, func_pedido, func_nodo )

        return arbol


    def listar_pedidos(self) -> list[Pedido]:

        pedidos = list()
        for tupla in self.repositorio.listar_pedidos():

            id, creado, fecha, cliente_id, lugar, ruta, productos_id, total, entregado = tupla

            entregado = entregado == "True"

            creado = self.castear_fecha( creado )
            fecha = self.castear_fecha( fecha )

            productos_id = productos_id.split(",")

            productos_id = [ int(id_producto) for id_producto in productos_id ] # Conviertiendo id a entero

            pedidos.append(Pedido( int(id), creado, fecha, int(cliente_id), lugar, ruta, productos_id, float(total), entregado ))

        return pedidos

    
    def castear_fecha(self, fecha:str) -> datetime:

        dma = fecha.split(" ")[0] # Dia, Mes, Año
        anio, mes, dia = tuple( dma.split("-") )
        anio = int( anio )
        mes = int( mes )
        dia = int( dia )

        hms = fecha.split(" ")[1] # h:m:s
        hora, minuto, segundo = tuple(hms.split(":"))
        hora = int( hora )
        minuto = int( minuto )
        segundo = int( segundo.split(".")[0] ) # Quitando punto decimal

        return datetime( anio, mes, dia, hora, minuto, segundo )


    def recuperar_pedido(self, llave, func) -> Pedido|None:

        funciones_nodo = {
            Pedido.get_id: Nodo.get_pedido_id
        }

        arbol = self.construir_arbol( func, funciones_nodo[func] )

        pedido = arbol.buscar_pedido(llave, funciones_nodo[func])

        if not pedido:
            return None
        
        return pedido


    def guardar_pedido(self, fecha:datetime, cliente_id:int, lugar:str, ruta:str, productos_id:list[int]) -> bool:
        
        creado = datetime.now()

        id = self.generar_id()
        while id in self.repositorio.listar_id_pedidos():
            id = self.generar_id()

        total = float(0)
        for producto_id in productos_id:

            producto = self.productos_servicio.recuperar_producto( producto_id )

            total += producto.precio

        nuevo_pedido = Pedido( id, creado, fecha, cliente_id, lugar, ruta, productos_id, total, False )

        self.repositorio.guardar_pedido( nuevo_pedido )

        return True
    

    def actualizar_pedido(self, id:int, fecha:datetime, cliente_id:int, lugar:str, ruta:str, productos_id:list[int], entregado:bool) -> bool:

        pedido = self.recuperar_pedido( id )

        pedido.fecha = fecha
        pedido.cliente_id = cliente_id
        pedido.lugar = lugar
        pedido.ruta = ruta
        pedido.productos_id = productos_id
        pedido.entregado = entregado

        total = float(0)
        for producto_id in productos_id:

            producto = self.productos_servicio.recuperar_producto( producto_id )

            total += producto.precio
        
        pedido.total = total

        self.repositorio.actualizar_pedido( pedido )


    def generar_id(self) -> int:
        return random.randint(0, 9999999)
