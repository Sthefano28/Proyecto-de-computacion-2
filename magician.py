from character import Character
from constants import*

class Mage(Character):

    def __init__(self, name, strength=0, intelligence=50, defense=60, life=60, level=1, experience=50, agility=0, spell=50, book=1):
        super().__init__(name, strength, intelligence, defense, life, level, experience, agility, spell)
        self.__book = book  # Encapsulamos book

    # Getter y Setter para book
    def get_book(self):
        return self.__book

    def set_book(self, book):
        self.__book = book

    # Getter y Setter para intelligence (heredado de Character)
    def get_intelligence(self):
        return super().get_intelligence()

    def set_intelligence(self, intelligence):
        super().set_intelligence(intelligence)

    # Sobreescribir el método attributes
    def attributes(self):
        super().attributes()
        print(f"· Book: {self.get_book()}")

    # Sobreescribir el método damage
    def damage(self, enemy):
        option = int(input(DAMAGE_MAGICIAN))  # MAGICIAN_OPTION
        
        if option == 1:
            self.set_book(30)  # Usamos el setter para modificar book
            self.set_intelligence(20)  # Usamos el setter para modificar intelligence
        elif option == 2:
            self.set_book(20)
            self.set_intelligence(30)
        else:
            print()  # MAGICIAN_OPTION_INCORRECT

        # Calculamos el daño usando getters para acceder a los atributos
        return self.get_intelligence() * self.get_book() - enemy.get_defense()

    # Sobreescribir is_alive (opcional, ya está en Character)
    def is_alive(self):
        return self.get_life() > 0

    # Método to_attack_1 con getters y setters
    def to_attack_1(self, enemy):
        damage = self.damage(enemy)
        enemy.set_life(enemy.get_life() - damage)  # Usamos setter para modificar la vida del enemigo

        print(f"{self.get_name()} ha realizado {damage} puntos de daño mágico a {enemy.get_name()}")

        if enemy.is_alive():
            print(f"La vida de {enemy.get_name()} es {enemy.get_life()}")
        else:
            enemy.to_die()

    # Getters y setters adicionales heredados de Character (si es necesario)
    def get_strength(self):
        return super().get_strength()

    def set_strength(self, strength):
        super().set_strength(strength)