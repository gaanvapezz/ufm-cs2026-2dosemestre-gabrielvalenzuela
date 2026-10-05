""""
Funciones de Pokemon - Batalla
"""

def damage (pokemon: dict, hp_lost: int):
    pokemon ["hp"] = pokemon ["hp"] - hp_lost

def attack(atacante: dict, rival: dict):

    tipo = atacante["tipo"].lower()

    if atacante["tipo"] == "electrico":
        ataque = "Impactrueno"
    elif atacante["tipo"] == "planta": 
        ataque = "Hoja Navaja"
    elif tipo == "fuego": 
        ataque = "Llamarada"
    else: 
        ataque = "Cañonazo de agua"

    damage(rival, atacante["ad"])

    print(f"\n({atacante["nombre"]}) ¡Ataca! con {ataque} | -{atacante["ad"]}")
    
    
    