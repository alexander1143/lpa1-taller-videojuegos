# objetos/armamento.py

class Objeto:
    def __init__(self, nombre, tipo, aumento_ataque=0, aumento_defensa=0, precio=0):
        self.nombre = nombre
        self.tipo = tipo  # "arma" o "defensa"
        self.aumento_ataque = aumento_ataque
        self.aumento_defensa = aumento_defensa
        self.precio = precio

    def aplicar(self, jugador):
        if self.tipo == "arma":
            jugador.ataque += self.aumento_ataque
            print(f"{jugador.nombre} ha equipado {self.nombre} (+{self.aumento_ataque} ATK).")
        elif self.tipo == "defensa":
            jugador.defensa += self.aumento_defensa
            print(f"{jugador.nombre} ha equipado {self.nombre} (+{self.aumento_defensa} DEF).")

    def vender(self, jugador):
        jugador.dinero += self.precio // 2  # Recupera la mitad del precio
        print(f"{jugador.nombre} ha vendido {self.nombre} por {self.precio // 2} monedas.")
