#Se incorpora batalla - Main
import json

with open("pokemons.json") as archivo:
    pokemons = json.load(archivo)

print(pokemons[0])            
print(pokemons[0]["nombre"])  
