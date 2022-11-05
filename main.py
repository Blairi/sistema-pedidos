import sys

sys.path.insert(0,"..")
from controladores.GrafosControlador import GrafosControlador
from controladores.ProductosControlador import ProductosControlador

def main():
    producto_controlador = ProductosControlador()
    grafo_controlador = GrafosControlador()
        