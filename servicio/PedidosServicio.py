import sys
import random
from datetime import datetime

sys.path.insert(0,"..")
from dominio.Pedido import Pedido
from database.PedidosRepositorio import PedidosRepositorio
from servicio.ProductosServicio import ProductosServicio
from servicio.ClientesServicio import ClientesServicio
from arbol.Arbol import Arbol
from arbol.Nodo import Nodo
from classes.PedidoDetalles import PedidoDetalles
from helpers.ManejoPDF import guardar_pdf


class PedidosServicio:

    def __init__(self) -> None:

        self.repositorio = PedidosRepositorio()
        self.productos_servicio = ProductosServicio()
        self.clientes_servicio = ClientesServicio()
    

    def listar_pedidos_detalles(self) -> list[PedidoDetalles]:

        pedidos_detallados = list()
        pedidos = self.listar_pedidos()

        for pedido in pedidos:

            cliente = self.clientes_servicio.buscar_cliente_id( pedido.cliente_id )
            if cliente == None:
                print("error en cliente")
                return []

            productos_precios = {}
            for producto_id in pedido.productos_id:

                producto = self.productos_servicio.recuperar_producto( producto_id )

                if producto == None:
                    return []

                productos_precios[producto.nombre] = producto.precio

            pedido_detallado = PedidoDetalles(
                pedido.id, 
                pedido.creado, 
                pedido.fecha, 
                cliente.nombre, 
                pedido.lugar, 
                pedido.ruta,
                productos_precios,
                pedido.total,
                pedido.entregado
            )

            pedidos_detallados.append( pedido_detallado )

        return pedidos_detallados
    

    def obtener_pedido_detalles(self, pedido:Pedido) -> PedidoDetalles:

        cliente = self.clientes_servicio.buscar_cliente_id( pedido.cliente_id )

        if cliente == None:
            print("error en cliente")
            return []

        productos_precios = {}
        for producto_id in pedido.productos_id:

            producto = self.productos_servicio.recuperar_producto( producto_id )

            if producto == None:
                return []

            productos_precios[producto.nombre] = producto.precio

        pedido_detallado = PedidoDetalles(
            pedido.id, 
            pedido.creado, 
            pedido.fecha, 
            cliente.nombre, 
            pedido.lugar, 
            pedido.ruta,
            productos_precios,
            pedido.total,
            pedido.entregado
        )

        return pedido_detallado
    
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
    

    def listar_pedidos_id(self) -> list[int]:
        return self.repositorio.listar_id_pedidos()

    
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
    

    def buscar_pedido_id(self, id:int) -> Pedido|None:

        arbol = self.construir_arbol(Pedido.get_id, Nodo.get_pedido_id)

        pedido = arbol.buscar_pedido(id, Nodo.get_pedido_id)

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

        pedido_detallado = self.obtener_pedido_detalles( nuevo_pedido )

        guardar_pdf( pedido_detallado )

        return True
    

    def actualizar_pedido(self, id:int, fecha:datetime, cliente_id:int, lugar:str, ruta:str, productos_id:list[int], entregado:bool) -> bool:

        pedido = self.buscar_pedido_id( id )

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
    

    def eliminar_pedido(self, id:int) -> bool:

        if id not in self.listar_pedidos_id():
            return False
        
        self.repositorio.eliminar_pedido( id )

        return True


    def generar_id(self) -> int:
        return random.randint(0, 9999999)
    

    def ordenar_pedidos(self, func_pedido) -> list[Pedido]:

        funciones = {
            Pedido.get_id: Nodo.get_pedido_id,
            Pedido.get_fecha: Nodo.get_pedido_fecha
        }

        arbol = self.construir_arbol(func_pedido, funciones[func_pedido])

        return arbol.recorrido_infijo_lista()
        
