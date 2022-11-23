import sys
from datetime import datetime

sys.path.insert(0,"..")
from servicio.PedidosServicio import PedidosServicio
from servicio.ClientesServicio import ClientesServicio
from servicio.ProductosServicio import ProductosServicio
from servicio.GrafosServicio import GrafosServicio
from dominio.Pedido import Pedido

from helpers.limpiar_pantalla import limpiar_pantalla

class PedidosControlador:
    
    def __init__(self) -> None:
        self.pedidos_servicio = PedidosServicio()
        self.clientes_servicio = ClientesServicio()
        self.productos_servicio = ProductosServicio()
        self.grafo_servicio = GrafosServicio()


    def mostrar_lugares(self):
        print("== Lugares registrados ==")
        lugares = self.grafo_servicio.listar_nombre_vertices()
        for lugar in lugares:
            print(lugar)
            print("------------")


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
    

    def mostrar_pedidos(self):
        print("== Todos los pedidos ==")
        pedidos = self.pedidos_servicio.listar_pedidos_detalles()
        for pedido in pedidos:
            print(pedido)
            print("------------")
    

    def mostrar_carrito(self, productos_id:list[int]) -> None:
        print("== Productos en el carrito ==")
        for producto_id in productos_id:
            producto = self.productos_servicio.recuperar_producto( producto_id )
            print( producto )
            print("------------")
        
    
    def construir_carrito(self) -> list[int]:
        
        limpiar_pantalla()

        carrito = list()
        while True:

            self.mostrar_productos()
            self.mostrar_carrito(carrito)

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

        return carrito
    

    def construir_fecha_hora(self) -> datetime:

        # Día de entrega
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

        return self.pedidos_servicio.castear_fecha( fecha )
    

    def construir_lugar_ruta(self, id_cliente:int) -> tuple:

        destino = "na"
        ruta = "na"
        resp = input("¿El pedido se entregara en la ubicación del cliente? s/n\n: ")
        if resp == "n":

            resp = input("¿Deseas agregar la ubicación del pedido en alguno de los lugares registrados? s/n\n: ")

            if resp == "s": # Agregar origen y destino

                self.mostrar_lugares()

                destino = input("Lugar de entrega: ")

                if not destino.lower() in self.grafo_servicio.listar_nombre_vertices():
                    print(f"{destino} no está registrado o no existe")
                    return
            
                origen = input("Lugar en el que te encuentras: ")
                if not origen.lower() in self.grafo_servicio.listar_nombre_vertices():
                    print(f"{origen} no está registrado o no existe")
                    return

                ruta = self.grafo_servicio.buscar_camino( origen.lower(), destino.lower() )
            
            else:
                ruta = "na"
                destino = "na"

        else:

            cliente = self.clientes_servicio.buscar_cliente_id( id_cliente )
            destino = cliente.ubicacion

            if destino != "na":
                self.mostrar_lugares()
                origen = input("Lugar en el que te encuentras: ")
                if not origen.lower() in self.grafo_servicio.listar_nombre_vertices():
                    print(f"{origen} no está registrado o no existe")
                    return

                ruta = self.grafo_servicio.buscar_camino( origen.lower(), destino.lower() )
        
        return destino, ruta
    

    def ver_pedidos(self):

        pedidos = self.pedidos_servicio.listar_pedidos()

        while True:

            limpiar_pantalla()

            print("==== Pedidos ====")
            for pedido in pedidos:
                print( self.pedidos_servicio.obtener_pedido_detalles(pedido) )
                print("----------------")

            print("== Ordenar por ==")
            resp = input("0. Salir\n1. Id\n2. Fecha de entrega\n: ")

            if not resp.isdigit():
                continue
            
            resp = int(resp)
                
            if resp == 0:
                limpiar_pantalla()
                break

            if resp == 1:
                pedidos = self.pedidos_servicio.ordenar_pedidos(Pedido.get_id)
            
            if resp == 2:
                pedidos = self.pedidos_servicio.ordenar_pedidos(Pedido.get_fecha)


    def actualizar_pedido(self):

        self.mostrar_pedidos()

        id = input("Id del pedido a actualizar: ")

        if not id.isdigit():
            print(f"{id} no es válido.")
            return
        
        pedido = self.pedidos_servicio.buscar_pedido_id(int(id))

        if pedido == None:
            print(f"{id} no existe.")
            return

        # Actualizando productos
        carrito = pedido.productos_id
        while True:

            limpiar_pantalla()

            self.mostrar_carrito( carrito )

            resp = input("0. Dejar de editar productos.\n1. Agregar productos\n2. Eliminar productos\n: ")

            if not resp.isdigit():
                print(f"{resp} no es vaĺida")
                return
            
            resp = int(resp)

            if resp == 0:
                break

            if resp == 1:
                carrito.extend( self.construir_carrito() ) # Combinando nuevos productos id
            
            if resp == 2:
                while True:

                    limpiar_pantalla()
                    self.mostrar_carrito( carrito )

                    id_prod = input("Ingresa el id del produto para eliminarlo del carrito\n( Para dejar de eliminar productos escribe 's':salir )\n: ")

                    if id_prod == "s":
                        break

                    if not id_prod.isdigit() or not int(id_prod) in carrito:
                        print(f"{id_prod} no es válido")
                        return

                    carrito.remove( int(id_prod) )

        # Actualizando hora y fecha
        limpiar_pantalla()
        fecha = self.construir_fecha_hora()
        if fecha == None:
            return

        # Actualizando lugar y ruta
        limpiar_pantalla()
        destino_ruta = self.construir_lugar_ruta(int(id))
        if destino_ruta == None:
            return

        destino, ruta = destino_ruta

        # estado del pedido
        estado = input("¿El pedido ya fue entregado? s/n: ")

        self.pedidos_servicio.actualizar_pedido( int(id), fecha, pedido.cliente_id, destino, ruta, carrito, estado == "s" )

    
    def crear_pedido(self):
        
        # Elegir cliente
        self.mostrar_clientes()

        cliente_id = input("Ingresa el id del cliente: ")

        if not cliente_id.isdigit() or not int(cliente_id) in self.clientes_servicio.listar_id_clientes():
            print(f"{cliente_id} no es válido o no existe.")
            return
        
        cliente_id = int( cliente_id )

        # Elegir productos
        carrito = self.construir_carrito()
        if len(carrito) < 1:
            print("Debes agregar al menos un producto.")
            return
        
        # Fecha de entrega
        limpiar_pantalla()
        fecha = self.construir_fecha_hora()
        if fecha == None:
            return

        # Lugar
        limpiar_pantalla()
        destino_ruta = self.construir_lugar_ruta(cliente_id)
        if destino_ruta == None:
            return
        
        destino, ruta = destino_ruta

        self.pedidos_servicio.guardar_pedido( fecha, cliente_id, destino, ruta, carrito )

        limpiar_pantalla()
    

    def eliminar_pedido(self):

        self.mostrar_pedidos()

        id = input("Ingresa el id del pedido a eliminar: ")

        if not id.isdigit():
            print(f"{id} no es válido")
            return
        
        self.pedidos_servicio.eliminar_pedido( int(id) )
    

    def despachar_pedido(self):

        pedidos = self.pedidos_servicio.ordenar_pedidos( Pedido.get_fecha )

        for pedido_detallado in pedidos:
            if not pedido_detallado.entregado:
                print(self.pedidos_servicio.obtener_pedido_detalles( pedido_detallado ))
                print("---------------------------------")

        id = input("Ingresa el id del pedido a despachar: ")

        if not id.isdigit():
            print(f"{id} no es válido")
            return

        if not int( id ) in self.pedidos_servicio.listar_pedidos_id():
            print(f"{id} no existe")

        pedido = self.pedidos_servicio.buscar_pedido_id(int( id ))

        pedido.entregado = not pedido.entregado

        self.pedidos_servicio.actualizar_pedido(pedido.id, pedido.fecha, pedido.cliente_id, pedido.lugar, pedido.ruta, pedido.productos_id, pedido.entregado)


    def menu(self):
        while True:
            print("===== Pedidos =====")
            print("Eligé escribiendo el número de la opción deseada:")

            opc = input("0. Salir.\n1. Crear pedido.\n2. Mostrar pedidos\n3. Actualizar pedido\n4. Eliminar pedido\n5. Despachar pedido\n: ")

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
            
            if opc == 2:
                limpiar_pantalla()
                self.ver_pedidos()
            
            if opc == 3:
                limpiar_pantalla()
                self.actualizar_pedido()
            
            if opc == 4:
                limpiar_pantalla()
                self.eliminar_pedido()
            
            if opc == 5:
                limpiar_pantalla()
                self.despachar_pedido()

