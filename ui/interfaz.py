# ui/interfaz.py

import pygame
import os

# Colores
BLANCO = (255, 255, 255)
ROJO = (200, 0, 0)
VERDE = (0, 200, 0)
NEGRO = (0, 0, 0)

class Interfaz:
    def __init__(self, pantalla, jugador):
        self.pantalla = pantalla
        self.jugador = jugador
        self.fuente = pygame.font.Font(None, 30)

    def dibujar_barra_vida(self, x, y, ancho, alto):
        # Dibujar barra de fondo
        pygame.draw.rect(self.pantalla, ROJO, (x, y, ancho, alto))
        # Proporción de vida actual
        vida_ratio = self.jugador.vida / self.jugador.vida_max
        ancho_vida = int(ancho * vida_ratio)
        # Dibujar vida actual
        pygame.draw.rect(self.pantalla, VERDE, (x, y, ancho_vida, alto))
        texto = self.fuente.render(f"Vida: {self.jugador.vida}/{self.jugador.vida_max}", True, BLANCO)
        self.pantalla.blit(texto, (x + 5, y + alto + 5))

    def mostrar_info_jugador(self, x, y):
        nivel = self.fuente.render(f"Nivel: {self.jugador.nivel}", True, BLANCO)
        ataque = self.fuente.render(f"Ataque: {self.jugador.ataque}", True, BLANCO)
        defensa = self.fuente.render(f"Defensa: {self.jugador.defensa}", True, BLANCO)
        oro = self.fuente.render(f"Oro: {self.jugador.oro}", True, BLANCO)

        self.pantalla.blit(nivel, (x, y))
        self.pantalla.blit(ataque, (x, y + 30))
        self.pantalla.blit(defensa, (x, y + 60))
        self.pantalla.blit(oro, (x, y + 90))

    def mostrar_inventario(self, x, y):
        inventario_titulo = self.fuente.render("Inventario:", True, BLANCO)
        self.pantalla.blit(inventario_titulo, (x, y))
        for i, item in enumerate(self.jugador.inventario):
            item_texto = self.fuente.render(f"- {item.nombre}", True, BLANCO)
            self.pantalla.blit(item_texto, (x + 10, y + 25 + i * 25))

    def actualizar(self):
        # Llama esta función cada frame para dibujar la interfaz
        self.dibujar_barra_vida(20, 20, 200, 20)
        self.mostrar_info_jugador(20, 60)
        self.mostrar_inventario(20, 170)
