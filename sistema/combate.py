# sistema/combate.py

import random

def calcular_daño(atacante, defensor):
    # Fórmula básica de daño: ataque - defensa, mínimo 1
    daño = max(1, atacante.ataque - defensor.defensa)
    return daño

def atacar(atacante, defensor):
    daño = calcular_daño(atacante, defensor)
    defensor.vida -= daño
    print(f"{atacante.nombre} ataca a {defensor.nombre} causando {daño} de daño.")
    print(f"{defensor.nombre} tiene ahora {defensor.vida} puntos de vida.")

    if defensor.vida <= 0:
        print(f"{defensor.nombre} ha sido derrotado.")
        if hasattr(atacante, 'ganar_experiencia'):
            atacante.ganar_experiencia(50)  # Ganancia fija, puedes hacerla dinámica

def combate(jugador, enemigo):
    print(f"¡Comienza el combate entre {jugador.nombre} y {enemigo.nombre}!")
    
    turno = random.choice(["jugador", "enemigo"])
    while jugador.vida > 0 and enemigo.vida > 0:
        if turno == "jugador":
            atacar(jugador, enemigo)
            turno = "enemigo"
        else:
            atacar(enemigo, jugador)
            turno = "jugador"

    if jugador.vida <= 0:
        print("¡Has perdido el combate!")
        return False
    else:
        print("¡Has ganado el combate!")
        return True
