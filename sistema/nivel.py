# sistema/nivel.py

class Nivel:
    def __init__(self, jugador):
        self.jugador = jugador
        self.experiencia = 0
        self.nivel = 1
        self.experiencia_necesaria = 100

    def ganar_experiencia(self, cantidad):
        self.experiencia += cantidad
        if self.experiencia >= self.experiencia_necesaria:
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.experiencia -= self.experiencia_necesaria
        self.experiencia_necesaria = int(self.experiencia_necesaria * 1.5)  # Más difícil subir
        self.jugador.puntos_vida += 20
        self.jugador.ataque += 5
        self.jugador.defensa += 3
        print(f"¡Subiste a nivel {self.nivel}!")

    def dibujar_nivel_ui(self, pantalla, fuente):
        # Opcional: muestra la barra de experiencia
        texto = fuente.render(f"Nivel: {self.nivel} | XP: {self.experiencia}/{self.experiencia_necesaria}", True, (255, 255, 255))
        pantalla.blit(texto, (10, 60))
