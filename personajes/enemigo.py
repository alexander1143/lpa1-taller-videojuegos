class Enemigo:
    def __init__(self, tipo):
        self.tipo = tipo  # 'volador' o 'terrestre'
        self.vida = 50
        self.ataque = 7
        self.defensa = 3