import pygame
import random

from personajes.enemigo import Enemigo
from objetos.trampa import Trampa
from objetos.tesoro import Tesoro
from objetos.armamento import Armamento

class Escenario:
    def __init__(self, ancho=800, alto=600, tile_size=32, jugador=None):
        self.ancho = ancho
        self.alto = alto
        self.tile_size = tile_size
        self.jugador = jugador
        self.enemigos = []
        self.trampas = []
        self.tesoros = []
        self.tiendas = []
        self.generar_elementos()

    def generar_elementos(self):
        # Generar enemigos
        for _ in range(5):
            x = random.randint(0, self.ancho // self.tile_size - 1) * self.tile_size
            y = random.randint(0, self.alto // self.tile_size - 1) * self.tile_size
            tipo = random.choice(["volador", "terrestre"])
            enemigo = Enemigo(x, y, tipo)
            self.enemigos.append(enemigo)

        # Generar trampas
        for _ in range(3):
            x = random.randint(0, self.ancho // self.tile_size - 1) * self.tile_size
            y = random.randint(0, self.alto // self.tile_size - 1) * self.tile_size
            trampa = Trampa(x, y, alcance=1, dano=20)
            self.trampas.append(trampa)

        # Generar tesoros
        for _ in range(4):
            x = random.randint(0, self.ancho // self.tile_size - 1) * self.tile_size
            y = random.randint(0, self.alto // self.tile_size - 1) * self.tile_size
            tesoro = Tesoro(x, y, valor=random.randint(10, 50))
            self.tesoros.append(tesoro)

        # Generar zona de tienda
        self.tiendas.append({
            "x": 100,
            "y": 100,
            "items": [
                Armamento("Espada de fuego", 10, 0, 30, 15),
                Armamento("Escudo mágico", 0, 10, 25, 10)
            ]
        })

    def dibujar(self, pantalla):
        # Dibujar enemigos
        for enemigo in self.enemigos:
            enemigo.dibujar(pantalla)

        # Dibujar trampas
        for trampa in self.trampas:
            trampa.dibujar(pantalla)

        # Dibujar tesoros
        for tesoro in self.tesoros:
            tesoro.dibujar(pantalla)

        # Dibujar tiendas (como cuadrados, por ejemplo)
        for tienda in self.tiendas:
            pygame.draw.rect(pantalla, (255, 215, 0), (tienda["x"], tienda["y"], 40, 40))
            
    def actualizar(self, jugador):
        # Aquí iría la lógica de actualización del escenario
        pass