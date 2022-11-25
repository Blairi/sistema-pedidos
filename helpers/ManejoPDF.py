import sys
from fpdf import FPDF
from datetime import datetime

sys.path.insert(0,"..")
from classes.PedidoDetalles import PedidoDetalles

def guardar_pdf(pedido:PedidoDetalles) -> None:

    pdf = FPDF()

    pdf.add_page()
    
    pdf.set_font("Arial", size = 15)

    # Insertando el pedido en el pdf
    atributos = [
        f"ID: {pedido.id}",
        f"Cliente: {pedido.cliente}",
        f"Lugar: {pedido.lugar}",
        f"Ruta: {pedido.ruta}",
        f"Productos: {pedido.formatear_productos_precios()}",
        f"Total: {pedido.total}",
        f"Creado: {pedido.creado}",
        f"Fecha de entrega: {pedido.fecha}"
        f"Tiempo restante: {'Ya debio ser entregado' if pedido.fecha < datetime.now() else pedido.tiempo_restante()}",
        f"Estado: {'Entregado' if pedido.entregado else 'No entregado'}"
    ]

    for i in range(len(atributos)):
        pdf.cell(200, 10, txt = atributos[i], ln = i, align = 'C')

    # Guardar el PDF
    pdf.output(f"./pedidos/{str(pedido.creado)}.pdf")