
from grafos.Vertice import Vertice


class GrafosRepositorio:
    
    ARCHIVO = "./database/grafos.txt"

    def recuperar_datos(self) -> list[tuple]:

        file = open( self.ARCHIVO, "r" )

        vertices_aristas = list()
        for line in file:
            vertices_aristas.append( tuple(line.rstrip().split("|")) )

        file.close()

        return vertices_aristas

    
    def listar_nombre_vertices(self) -> list[str]:

        file = open( self.ARCHIVO, "r" )

        vertices = list()
        for line in file:
            vertices.append( line.rstrip().split("|")[0] )

        file.close()

        return vertices

    
    def guardar_vertice(self, vertice : Vertice) -> None:

        file = open( self.ARCHIVO, "a" )

        file.write(f"{vertice.nombre}|\n")

        file.close()


    def guardar_arista(self, nombre_vertice1 : str, nombre_vertice2 : str) -> None:

        vertices_aristas = self.recuperar_datos()

        # Filtrar los vertices
        copia_vertices_aristas = list()
        vertices_aristas_modificar = list()
        for vertice_aristas in vertices_aristas:

            nombre_vertice = vertice_aristas[0] # Obteniendo nombre

            if nombre_vertice != nombre_vertice1 and nombre_vertice != nombre_vertice2:
                copia_vertices_aristas.append( vertice_aristas )

            else: # Guardando los vertices que modificaremos
                vertices_aristas_modificar.append( vertice_aristas )
            
        # Reiniciamos archivo
        self.reiniciar_archivo()

        # Escribir los vertices filtrados
        file = open( self.ARCHIVO, "a" )

        for copia in copia_vertices_aristas:

            vertice, aristas = copia

            file.write(f"{vertice}|{aristas}\n")

        file.close()

        # Construimos formato y guardamos las modificaciones
        
        file = open( self.ARCHIVO, "a" )

        for vertice_aristas_modificar in vertices_aristas_modificar:

            vertice, aristas = vertice_aristas_modificar

            aristas = aristas.split(",") # Formando lista separando por comas
            aristas = list(filter(None, aristas)) # Quitando strings vacios

            # Nos aseguramos de que no haya aristas apuntando al mismo nodo
            if nombre_vertice1 != vertice:
                aristas.append( nombre_vertice1 )
            
            if nombre_vertice2 != vertice:
                aristas.append( nombre_vertice2 )

            aristas = ",".join(aristas) # Tranformando la lista en texto plano

            file.write(f"{vertice}|{aristas}\n")
        
        file.close()

    def reiniciar_archivo(self) -> None:
        file = open( self.ARCHIVO, "w" )
        file.write("")
        file.close()