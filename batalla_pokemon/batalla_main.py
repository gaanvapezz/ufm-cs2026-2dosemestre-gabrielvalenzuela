#Se incorpora batalla - Main
import json
from random import choice
from time import sleep
from batalla_poke import attack


#Espera
def waiting ():
    print("\n...")
    sleep (0.67)

#CARGA DE POKEMONS
with open ("pokemons.json", encoding="utf-8") as archivo: 
    pokemon_posibles = json.load(archivo)

for pokemon in pokemon_posibles: 
    pokemon["nombre"] = pokemon["nombre"].capitalize()

#Seleccionar para la batalla
poke_1 = choice(pokemon_posibles)
poke_2 = choice(pokemon_posibles)

print("\n ========== POKEMON SELECCIONADOS ========== ")
print("\n ---------- ¡HORA DE LA BATALLA ---------- ")

waiting()
print(f'\nPokemon 1: {poke_1["nombre"]} (HP: {poke_1["hp"]} | AD: {poke_1["ad"]})')
print(f'Pokemon 2: {poke_2["nombre"]} (HP: {poke_2["hp"]} | AD: {poke_2["ad"]})')

while True: 
    #TURNO POKE 1
    waiting()
    attack(poke_1, poke_2)

    #Poke 2 perdió?
    if poke_2["hp"] <= 0: 
        print("\n ========== GAME OVER ========== ")
        print(f"\nFIN DE LA BATALLA {poke_1["nombre"]} derrotó a {poke_2["nombre"]}")
        break 

    #TURNO POKE 2
    waiting()
    attack(poke_2, poke_1)

    #POKE 1 PERDIÓ?
    if poke_1["hp"] <= 0:
        print("\n ========== GAME OVER ========== ")
        print(f"\nFIN DE LA BATALLA {poke_2["nombre"]} derrotó a {poke_1["nombre"]}")
        break 


    #VIDA EN LA BATALLA

    waiting
    print("\n ===== HPs Restantes =====")
    print(f'{poke_1["nombre"]}: {poke_1["hp"]}')
    print(f'{poke_2["nombre"]}: {poke_2["hp"]}')

    