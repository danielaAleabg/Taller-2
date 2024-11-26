import random

puntos_jugador1 = 0
puntos_jugador2 = 0
modo = input("¿Quieres jugar contra el PC o multijugador? (PC/multijugador): ").lower()

while True:
    if modo == "pc":
        jugador = input("Jugador 1, elige entre piedra, papel o tijera: ").lower()
        opciones = ["piedra", "papel", "tijera"]
        pc = random.choice(opciones)
        print(f"PC elige: {pc}")
        
        if jugador == pc:
            print("¡Es un empate!")
        elif (jugador == "piedra" and pc == "tijera") or \
             (jugador == "papel" and pc == "piedra") or \
             (jugador == "tijera" and pc == "papel"):
            print("¡Jugador 1 gana esta ronda!")
            puntos_jugador1 += 1
        else:
            print("¡PC gana esta ronda!")
            puntos_jugador2 += 1

    elif modo == "multijugador":
        jugador1 = int(input("Elige entre: 1.piedra 2.papel 3.tijera: "))
        jugador2 = int(input("Elige entre: 1.piedra 2.papel 3.tijera: "))
        
        if jugador1 == jugador2:
            print("¡Es un empate!")
        elif (jugador1 == "piedra" and jugador2 == "tijera") or \
             (jugador1 == "papel" and jugador2 == "piedra") or \
             (jugador1 == "tijera" and jugador2 == "papel"):
            print("¡Jugador 1 gana esta ronda!")
            puntos_jugador1 += 1
        else:
            print("¡Jugador 2 gana esta ronda!")
            puntos_jugador2 += 1

    else:
        print("Opción no válida, por favor elige 'PC' o 'multijugador'.")
        break

    continuar = input("¿Quieres jugar otra ronda? (si/no): ").lower()
    if continuar != "si":
        break

print(f"\nJuego terminado. Puntos finales:")
print(f"Jugador 1: {puntos_jugador1}")
print(f"Jugador 2: {puntos_jugador2}")

if puntos_jugador1 > puntos_jugador2:
    print("¡Jugador 1 es el ganador!")
elif puntos_jugador2 > puntos_jugador1:
    print("¡Jugador 2 es el ganador!")
else:
    print("¡Es un empate final!")
