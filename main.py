from constants import*
from character import Character
from warrior import Warrior
from magician import Mage
from archer import Archer
from challenge import Challenge
from enemy import Enemy
from enemy2 import generate_enemy
from mazmorras import Mazmorra
import random
from combat import*


"""Basándome en el código proporcionado, aquí tienes una documentación general del juego:

Nombre del Juego: [No especificado, pero parece ser un juego de rol (RPG) de aventuras]

Descripción General: Este es un juego de rol basado en texto donde los jugadores pueden elegir entre tres tipos de personajes: Guerrero, Mago y Arquero. Los jugadores pueden participar en combates contra enemigos generados aleatoriamente y explorar mazmorras llenas de desafíos y jefes.

Clases Principales:

Character: Clase base para todos los personajes jugables.

Atributos: nombre, fuerza, inteligencia, defensa, vida, nivel, experiencia, agilidad, hechizo.
Métodos principales: atacar, recibir daño, subir de nivel, usar objetos.
Warrior (Guerrero): Subclase de Character especializada en combate cuerpo a cuerpo.

Atributo especial: espada
Daño basado en fuerza y tipo de ataque elegido
Mage (Mago): Subclase de Character especializada en magia.

Atributo especial: libro
Daño basado en inteligencia y tipo de hechizo elegido
Archer (Arquero): Subclase de Character especializada en ataques a distancia.

Atributo especial: arco
Daño basado en agilidad y tipo de flecha elegida
Enemy: Representa a los enemigos del juego.

Generados aleatoriamente con diferentes niveles de dificultad
Challenge: Representa desafíos no combativos en las mazmorras.

Item: Representa objetos que los personajes pueden usar para mejorar sus atributos.

Mazmorra: Representa un escenario de juego con múltiples enemigos, un jefe final y posibles desafíos.

Flujo del Juego:

El jugador elige un tipo de personaje.
Se presenta un menú con opciones para: a) Participar en un combate individual contra un enemigo. b) Explorar una mazmorra completa. c) Salir del juego.
En los combates, los turnos se alternan entre el jugador y el enemigo hasta que uno sea derrotado.
En las mazmorras, el jugador enfrenta múltiples enemigos, resuelve desafíos y finalmente se enfrenta a un jefe.
Los personajes pueden ganar experiencia, subir de nivel y obtener objetos al derrotar enemigos.
Características Adicionales:

Sistema de combate por turnos.
Generación aleatoria de enemigos y sus estadísticas.
Uso de objetos para mejorar las estadísticas del personaje.
Múltiples mazmorras con diferentes niveles de dificultad.
Este juego ofrece una experiencia de rol clásica con elementos de estrategia en la selección de ataques y la gestión de recursos del personaje a través de las diferentes mazmorras y combates. """



def main(character_1=None, character_2=None, character_3=None):

    while True:
        option = int(input(OPTION_MENU))  # MENÚ PRINCIPAL

        if option == 1:
            choose_character = int(input(OPTION_CHARACTER_MENU_ENEMY))  # ELEGIR PERSONAJE

            if choose_character == 1:
                character_1.attributes()
                enemy = generate_enemy(1)
                enemy.attributes()
                combat(character_1, enemy)

            elif choose_character == 2:
                character_2.attributes()
                enemy = generate_enemy(2)
                enemy.attributes()
                combat(character_2, enemy)

            elif choose_character == 3:
                character_3.attributes()
                enemy = generate_enemy(3)
                enemy.attributes()
                combat(character_3, enemy)

            else:
                print(VALIDATION_MENU)

        elif option == 2:
            enter_character = int(input(OPTION_CHARACTER_MENU_MAZMORRA))  # ENTRAR EN MAZMORRA

            if enter_character == 1 and character_1.is_alive():
                explore_dungeons(character_1)

            elif enter_character == 2 and character_2.is_alive():
                explore_dungeons(character_2)

            elif enter_character == 3 and character_3.is_alive():
                explore_dungeons(character_3)

            else:
                print(CHARACTER_DEAD)

        else:
            print(EXIT_TO_GAME)
            break

def explore_dungeons(character):
    # Generar enemigos y jefes para cada mazmorra
    enemy_1 = generate_enemy(5)
    enemy_2 = generate_enemy(7)
    boss_1 = generate_enemy(10)

    enemy_3 = generate_enemy(6)
    enemy_4 = generate_enemy(8)
    boss_2 = generate_enemy(12)

    enemy_5 = generate_enemy(7)
    enemy_6 = generate_enemy(9)
    boss_3 = generate_enemy(15)

    # Crear mazmorras
    mazmorra_1 = Mazmorra("Caverna Oscura", [enemy_1, enemy_2], boss_1)
    mazmorra_2 = Mazmorra("Fortaleza Abandonada", [enemy_3, enemy_4], boss_2)
    mazmorra_3 = Mazmorra("Templo Maldito", [enemy_5, enemy_6], boss_3)

    # Crear desafíos
    challenge_1 = Challenge("Cruzar el puente colgante", 5)
    challenge_2 = Challenge("Resolver el acertijo antiguo", 7)

    # Agregar desafíos a las mazmorras
    mazmorra_1.add_challenges(challenge_1)
    mazmorra_2.add_challenges(challenge_2)

    # Explorar las mazmorras
    mazmorra_1.explorare(character)
    mazmorra_2.explorare(character)
    mazmorra_3.explorare(character)



# Seleccionar personajes opcionalmente
character_1, character_2, character_3 = None, None, None

character_election = int(input(CHARACTER_ELECTION))

if character_election == 1:
    character_1 = Warrior(input(OPTION_WARRIOR))
elif character_election == 2:
    character_2 = Mage(input(OPTION_MAGICIAN))
elif character_election == 3:
    character_3 = Archer(input(OPTION_ARCHER))
else:
    print(OPTION_MENU_VALIDATION)

# Ejecutar menú del juego, incluso si solo un personaje ha sido seleccionado
main(character_1, character_2, character_3)