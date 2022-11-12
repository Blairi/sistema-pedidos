
class Cliente:

    def __init__(self, id:int, nombre:str) -> None:
        self.id = id
        self.nombre = nombre
    
    def get_id(self) -> int:
        return self.id

    def get_nombre(self) -> str:
        return self.nombre

    def __str__(self) -> str:
        return f"id: {self.id}\nnombre: {self.nombre.capitalize()}"