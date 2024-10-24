import random

from enemy import Enemy
 

# Generar enemigos de un nivel específico
def generate_enemy(level):
    names = ["Orco", "Goblin", "Troll", "Dragón", "Bandido"]
    name = random.choice(names)
    return Enemy(name, level)
