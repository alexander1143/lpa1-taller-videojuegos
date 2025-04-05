# sistema/inventario.py

class Inventario:
    def __init__(self):
        self.objetos = []

    def agregar_objeto(self, objeto):
        """Agrega un objeto al inventario."""
        self.objetos.append(objeto)
        print(f"Objeto agregado: {objeto.nombre}")

    def eliminar_objeto(self, objeto):
        """Elimina un objeto del inventario si existe."""
        if objeto in self.objetos:
            self.objetos.remove(objeto)
            print(f"Objeto eliminado: {objeto.nombre}")
        else:
            print("El objeto no está en el inventario.")

    def usar_objeto(self, personaje, objeto):
        """Usa un objeto (como armamento o trampa)."""
        if objeto in self.objetos:
            objeto.usar(personaje)  # Método definido en el objeto
            self.eliminar_objeto(objeto)
        else:
            print("No puedes usar un objeto que no tienes.")

    def vender_objeto(self, objeto):
        """Simula la venta de un objeto, retorna el valor si se vende."""
        if objeto in self.objetos:
            self.eliminar_objeto(objeto)
            return objeto.precio_venta
        else:
            return 0

    def listar_objetos(self):
        """Muestra todos los objetos en el inventario."""
        for obj in self.objetos:
            print(f"- {obj.nombre} (tipo: {obj.tipo})")

    def buscar_por_tipo(self, tipo):
        """Devuelve los objetos de cierto tipo (e.g. 'trampa', 'armamento')."""
        return [obj for obj in self.objetos if obj.tipo == tipo]

