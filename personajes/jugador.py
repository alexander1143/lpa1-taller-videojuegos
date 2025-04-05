import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.imagen = pygame.image.load("assets/imagenes/jugador.png").convert_alpha()
        self.image = pygame.transform.scale(self.imagen, (50, 50))
        self.rect = self.image.get_rect(topleft=(x, y))

        self.vida = 100
        self.ataque = 10
        self.defensa = 5
        self.nivel = 1
        self.inventario = []

    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 5
        if teclas[pygame.K_RIGHT]:
            self.rect.x += 5
        if teclas[pygame.K_UP]:
            self.rect.y -= 5
        if teclas[pygame.K_DOWN]:
            self.rect.y += 5

    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)