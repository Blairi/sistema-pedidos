
class Producto:

    def __init__(self, id :int|None, nombre : str, precio : float, descripcion : str) -> None:
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    def get_id(self) -> int|None:
        return self.id

    def get_nombre(self) -> str:
        return self.nombre

    def get_descripcion(self) -> str:
        return self.descripcion

    def get_precio(self) -> float:
        return self.precio

    def __str__(self) -> str:
        return f"id: {self.id}\nNombre: {self.nombre}\nPrecio: {self.precio}\nDescripción: {self.descripcion}"
