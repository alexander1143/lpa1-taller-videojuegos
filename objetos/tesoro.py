# objetos/tesoro.py

class Tesoro:
    def __init__(self, valor, posicion):
        self.valor = valor  # Valor monetario del tesoro
        self.posicion = posicion  # Tupla (x, y)

    def recolectar(self, jugador):
        jugador.dinero += self.valor
        print(f"{jugador.nombre} ha recolectado un tesoro de {self.valor} monedas.")

    def dibujar(self, pantalla, imagen):
        pantalla.blit(imagen, self.posicion)
