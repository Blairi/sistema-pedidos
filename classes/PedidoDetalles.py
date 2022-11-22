from datetime import datetime


class PedidoDetalles:
    def __init__(
        self,
        id : int,
        creado : datetime,
        fecha : datetime,
        cliente : str,
        lugar : str,
        ruta : str,
        productos : dict[str,float],
        total : float ,
        entregado : bool) -> None:

        self.id = id
        self.creado = creado
        self.fecha = fecha
        self.cliente = cliente
        self.lugar = lugar
        self.ruta = ruta
        self.productos = productos
        self.total = total
        self.entregado = entregado


    def __str__(self) -> str:
        return f"ID: \t{self.id}\nCliente: \t{self.cliente}\nLugar: \t{self.lugar}\nRuta: \t{self.ruta}\nProductos:\n{self.formatear_productos_precios()}Total: $ {self.total}\nCreado: {self.creado}\nFecha de entrega: {self.fecha}\nTiempo restante: {'Ya debio ser entregado' if self.fecha < datetime.now() else self.tiempo_restante()}\nEstado: {'Entregado' if self.entregado else 'No entregado'}"
    

    def formatear_productos_precios(self) -> str:
        formato = ""
        for producto in self.productos:
            formato += f"{producto}..... $ {self.productos[producto]}\n"
        return formato


    def tiempo_restante(self) -> datetime:
        tiempo = self.fecha - datetime.now()
        return tiempo
