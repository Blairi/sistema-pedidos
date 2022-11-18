import sys
from datetime import datetime

sys.path.insert(0,"..")
from servicio.PedidosServicio import PedidosServicio
from servicio.ClientesServicio import ClientesServicio
from servicio.ProductosServicio import ProductosServicio

from helpers.limpiar_pantalla import limpiar_pantalla

class PedidosControlador:
    
    def __init__(self) -> None:
        self.pedidos_servicio = PedidosServicio()
        self.clientes_servicio = ClientesServicio()
        self.productos_servicio = ProductosServicio()


    def mostrar_clientes(self):
        print("== Tus clientes ==")
        clientes = self.clientes_servicio.listar_clientes()
        for cliente in clientes:
            print(cliente)
            print("------------")
    

    def mostrar_productos(self):
        print("== Tus productos ==")
        productos = self.productos_servicio.listar_productos()
        for producto in productos:
            print(producto)
            print("------------")

    
    def crear_pedido(self):
        
        # Elegir cliente
        self.mostrar_clientes()

        cliente_id = input("Ingresa el id del cliente: ")

        if not cliente_id.isdigit() or not int(cliente_id) in self.clientes_servicio.listar_id_clientes():
            print(f"{cliente_id} no es válido o no existe.")
            return
        
        cliente_id = int( cliente_id )

        # Elegir productos
        self.mostrar_productos()

        carrito = list()
        while True:

            id_producto = input("Ingresa el id del produto para agregarlo al carrito\n( Para dejar de agregar productos escribe 's':salir )\n: ")

            if id_producto == "s" or id_producto == "salir":
                break

            if not id_producto.isdigit():
                print(f"{id_producto} no es válido")
                continue
            
            id_producto = int( id_producto )

            if not id_producto in self.productos_servicio.listar_id_productos():
                print(f"{id_producto} no existe.")
                continue

            carrito.append( id_producto )
        
        if len(carrito) < 1:
            print("Debes agregar al menos un producto.")
            return
        
        # Fecha de entrega
        anio, mes, dia, hora, minuto = 0, 0, 0, 0, 0
        resp = input("¿Tu pedido se entrega hoy? s/n\n: ")
        if resp == "n" or resp == "no":

            print("Ingresa la fecha de entrega")

            anio = input("Año: ")
            if not anio.isdigit() or len(anio) != 4:
                print(f"{anio} no es válido.")
                return
            
            mes = input("Mes: ")
            if not mes.isdigit() or len(mes) > 2:
                print(f"{mes} no es válido.")
                return
            
            dia = input("Día: ")
            if not dia.isdigit() or len(dia) > 2:
                print(f"{dia} no es válido")
                return
        else:
            anio = str(datetime.now().year)
            mes = str(datetime.now().month)
            dia = str(datetime.now().day)

        # Hora de entrega
        resp = input("¿Ingresar hora de entrega? s/n\n: ")
        if resp == "s" or resp == "si":

            print("Ingresa la hora de entrega")

            hora = input("Ingresa la hora a entregar en este formato: 00:00\n:")

            hora_minuto = hora.split(":")
            if not len(hora_minuto) == 2:
                print(f"{hora_minuto} no es un formato válido")
                return
            
            hora = hora_minuto[0]
            minuto = hora_minuto[1]

            if not hora.isdigit() or not minuto.isdigit() or len(hora) > 2 or len(minuto) > 2:
                print(f"{hora_minuto} no es un formato válido")
                return
            
        else:
            hora = str(datetime.now().hour)
            minuto = str(datetime.now().minute)
        
        fecha = anio + "-" + mes + "-" + dia + " " + hora + ":" + minuto + ":" + "0" # Formateando fecha
        fecha = self.pedidos_servicio.castear_fecha( fecha )
        
        
        self.pedidos_servicio.guardar_pedido(fecha, cliente_id, "casa", "casa=>escuela", carrito)

    def menu(self):
        while True:
            print("===== Pedidos =====")
            print("Eligé escribiendo el número de la opción deseada:")

            opc = input("0. Salir.\n1. Crear pedido.\n: ")

            if not opc.isdigit():
                print(f"{opc} no es una opción válida")
                continue
                
            opc = int(opc)

            if opc == 0:
                limpiar_pantalla()
                break

            if opc == 1:
                limpiar_pantalla()
                self.crear_pedido()

