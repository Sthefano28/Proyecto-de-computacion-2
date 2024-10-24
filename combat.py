from character import Character
from enemy import *
from enemy2 import *
from items import *
from constants import*

def combat(character, enemy):
    turn = 0
    while character.is_alive() and enemy.is_alive():
        print(f">>> Acción de {character.get_name()}:")
        character.to_attack(enemy)
        
        if enemy.is_alive():
            print(f">>> Acción de {enemy.get_name()}:")
            enemy.to_attack(character)
            print(f"El número de turnos es {turn}")
        turn += 1

    if character.is_alive():
        print(f"\n{character.get_name()} ha ganado")
        
        # El character recibe el ítem del enemigo
        item_ganado = enemy.to_die()
        character.use_item(item_ganado)
        character.level_up_experience(10, 10, 10, 10, 10, 10, 10)
        print(f"El número de turnos es {turn}")
   
    elif enemy.is_alive():
        print(f"\n{enemy.get_name()} ha ganado")
    else:
        print(COMBAT_OPTION)

