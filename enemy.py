import random
from items import Item
from items import items_disponibles
from character import Character


class Enemy:
    
    def __init__(self, name, level):
        self.__name = name  # Encapsulamos name
        self.__level = level  # Encapsulamos level
        self.__life = random.randint(100, 150) + level * 10  # Encapsulamos life
        self.__strength = random.randint(70, 80) + level * 2  # Encapsulamos strength
        self.__defense = random.randint(80, 100) + level * 2  # Encapsulamos defense
        self.__item = random.choice(items_disponibles)  # Encapsulamos item

    # Getters y Setters para name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Getters y Setters para level
    def get_level(self):
        return self.__level

    def set_level(self, level):
        self.__level = level

    # Getters y Setters para life
    def get_life(self):
        return self.__life

    def set_life(self, life):
        self.__life = life

    # Getters y Setters para strength
    def get_strength(self):
        return self.__strength

    def set_strength(self, strength):
        self.__strength = strength

    # Getters y Setters para defense
    def get_defense(self):
        return self.__defense

    def set_defense(self, defense):
        self.__defense = defense

    # Getters y Setters para item
    def get_item(self):
        return self.__item

    def set_item(self, item):
        self.__item = item

    # Método para mostrar atributos
    def attributes(self):
        print(f"{self.get_name()} (level {self.get_level()}):")
        print(f"· Salud: {self.get_life()}")
        print(f"· Fuerza: {self.get_strength()}")
        print(f"· Defensa: {self.get_defense()}")

    # Método para verificar si el enemigo está vivo
    def is_alive(self):
        return self.get_life() > 0

    # Método cuando el enemigo muere
    def to_die(self):
        self.set_life(0)
        print(f"{self.get_name()} ha muerto")
        print(f"{self.get_name()} ha dejado caer {self.get_item().get_name()}")
        return self.get_item()  # Devuelve el ítem que deja caer

    # Método para calcular el daño que inflige
    def damage(self, enemy):
        return max(self.get_strength() - enemy.get_defense(),0)

    # Método para atacar a otro personaje
    def to_attack(self, enemy):
        damage = self.damage(enemy)
        enemy.set_life(enemy.get_life() - damage)
        print(f"{self.get_name()} ha realizado {damage} puntos de daño a {enemy.get_name()}")
        if enemy.is_alive():
            print(f"La vida de {enemy.get_name()}: {enemy.get_life()}")
        else:
            enemy.to_die()


