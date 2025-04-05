import pygame
import sys
from config import SCREEN_WIDTH as ANCHO, SCREEN_HEIGHT as ALTO, FPS
from sistema.escenario import Escenario
from personajes.jugador import Jugador
from ui.interfaz import Interfaz

def main():
    # Inicializar pygame
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Mi Videojuego en Pygame")
    reloj = pygame.time.Clock()

    # Cargar fondo
    fondo = pygame.image.load("assets/imagenes/fondo.png").convert()

    # Crear instancias del jugador primero
    jugador = Jugador("Héroe", vida=100, ataque=10, defensa=5)
    
    # Luego crear el escenario pasando los parámetros correctos
    escenario = Escenario(ANCHO, ALTO, 32, jugador)
    
    # Crear interfaz
    interfaz = Interfaz(jugador)

    # Loop principal
    ejecutando = True
    while ejecutando:
        reloj.tick(FPS)

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

        # Actualizar lógica del juego
        jugador.actualizar()
        escenario.actualizar(jugador)

        # Dibujar en pantalla
        pantalla.blit(fondo, (0, 0))
        escenario.dibujar(pantalla)
        jugador.dibujar(pantalla)
        interfaz.dibujar(pantalla)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()