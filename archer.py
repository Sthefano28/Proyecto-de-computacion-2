from character import Character
from combat import *
from constants import*
class Archer(Character):
    
    def __init__(self, name, strength=0, intelligence=0, defense=60, life=100, level=1, experience=50, agility=100, spell=0, bow=1):
        super().__init__(name, strength, intelligence, defense, life, level, experience, agility, spell)
        self.__bow = bow  # Encapsulamos bow

    # Getter y Setter para bow
    def get_bow(self):
        return self.__bow

    def set_bow(self, bow):
        self.__bow = bow

    # Getter y Setter para agility (heredado)
    def get_agility(self):
        return super().get_agility()

    def set_agility(self, agility):
        super().set_agility(agility)

    # Sobreescribir el método attributes
    def attributes(self):
        super().attributes()
        print(f"· Bow: {self.get_bow()}")

    # Sobreescribir el método damage
    def damage(self, enemy):
        option = int(input(OPTION_ARCHER_DAMAGE))  # DAMAGE_ARCHER_OPTION

        if option == 1:
            self.set_bow(30)  # Usamos el setter para modificar bow
            self.set_agility(20)  # Usamos el setter para modificar agility
        elif option == 2:
            self.set_bow(15)
            self.set_agility(30)
        else:
            print(OPTION_ARCHER)  # DAMAGE_ARCHER_OPTION_INCORRECT

        # Calculamos el daño usando getters para acceder a los atributos
        return (self.get_agility() * self.get_bow() - enemy.get_defense())

    # Sobreescribir is_alive (opcional, ya está en Character)
    def is_alive(self):
        return self.get_life() > 0

    # Método to_attack_2 con getters y setters
    def to_attack_2(self, enemy):
        damage = self.damage(enemy)
        enemy.set_life(enemy.get_life() - damage)  # Usamos setter para modificar la vida del enemigo

        print(f"{self.get_name()} ha realizado {damage} puntos de daño con el arco a {enemy.get_name()}")

        if enemy.is_alive():
            print(f"La vida de {enemy.get_name()} es {enemy.get_life()}")
        else:
            enemy.to_die()

    # Setters y getters adicionales heredados de Character (si es necesario)
    def get_strength(self):
        return super().get_strength()

    def set_strength(self, strength):
        super().set_strength(strength)



