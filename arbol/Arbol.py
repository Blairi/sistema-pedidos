from .Nodo import Nodo
from dominio.Pedido import Pedido

class Arbol:

    def __init__(self) -> None:
        self.raiz = None


    def obtenerRaiz(self):
        return self.raiz


    def agregar(self, pedido:Pedido, func_pedido, func_nodo):
        if self.raiz == None:
            self.raiz = Nodo( pedido )
        else:
            self.agregarNodo( pedido, func_pedido, self.raiz, func_nodo )

    
    def agregarNodo(self, pedido:Pedido, func_pedido, nodo:Nodo, func_nodo):

        if func_pedido(pedido) < func_nodo(nodo):
            if nodo.hijoIzq != None:
                self.agregarNodo( pedido, func_pedido, nodo.hijoIzq, func_nodo )
            else:
                nodo.hijoIzq = Nodo( pedido )
        else:
            if nodo.hijoDer != None:
                self.agregarNodo( pedido, func_pedido, nodo.hijoDer, func_nodo )
            else:
                nodo.hijoDer = Nodo( pedido )


    def busqueda(self, nodo:Nodo, valor, func_nodo):

        if nodo == None or valor == func_nodo(nodo):
            return nodo.pedido if nodo != None else None

        if valor < func_nodo(nodo):
            return self.busqueda(nodo.hijoIzq, valor, func_nodo)
        else:
            return self.busqueda(nodo.hijoDer, valor, func_nodo)
    
    
    def buscar_pedido(self, llave, func_nodo):
        if self.raiz != None:
            return self.busqueda( self.raiz, llave, func_nodo )


    def prefijo(self, nodo:Nodo):
        if nodo != None:
            print( str(nodo.pedido) )
            if nodo.hijoIzq != None:
                self.prefijo(nodo.hijoIzq)

            if nodo.hijoDer != None:
                self.prefijo(nodo.hijoDer)


    def imprimirPrefijo(self):
        if self.raiz != None:
            self.prefijo( self.raiz )


    def sufijo(self, nodo:Nodo):
        if nodo != None:
            if nodo.hijoIzq != None:
                self.sufijo(nodo.hijoIzq)

            if nodo.hijoDer != None:
                self.sufijo(nodo.hijoDer)

            print( str(nodo.pedido) )


    def imprimirSufijo(self):
        if self.raiz != None:
            self.sufijo( self.raiz )


    def infijo(self, nodo:Nodo):
        if nodo != None:
            if nodo.hijoIzq != None:
                self.infijo(nodo.hijoIzq)

            print( str(nodo.pedido) )

            if nodo.hijoDer != None:
                self.infijo(nodo.hijoDer)


    def imprimirInfijo(self):
        if self.raiz != None:
            self.infijo( self.raiz )
